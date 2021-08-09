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


class AcceptAttachCcnInstancesRequest(AbstractModel):
    """AcceptAttachCcnInstances request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        :param Instances: List of associated instances.\n        :type Instances: list of CcnInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptAttachCcnInstancesResponse(AbstractModel):
    """AcceptAttachCcnInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AccountAttribute(AbstractModel):
    """Account attribute object

    """

    def __init__(self):
        """
        :param AttributeName: Attribute name\n        :type AttributeName: str\n        :param AttributeValues: Attribute values\n        :type AttributeValues: list of str\n        """
        self.AttributeName = None
        self.AttributeValues = None


    def _deserialize(self, params):
        self.AttributeName = params.get("AttributeName")
        self.AttributeValues = params.get("AttributeValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddBandwidthPackageResourcesRequest(AbstractModel):
    """AddBandwidthPackageResources request structure.

    """

    def __init__(self):
        """
        :param ResourceIds: The unique ID of the source, such as 'eip-xxxx' and 'lb-xxxx'. EIP and LB resources are currently supported.\n        :type ResourceIds: list of str\n        :param BandwidthPackageId: The unique ID of the bandwidth package, such as 'bwp-xxxx'.\n        :type BandwidthPackageId: str\n        :param NetworkType: The network type of the bandwidth package. Valid value: `BGP`, indicating that the internal resource is a BGP IP.\n        :type NetworkType: str\n        :param ResourceType: The resource type, including `Address` and `LoadBalance`.\n        :type ResourceType: str\n        :param Protocol: The protocol type of the bandwidth package. Valid values: `ipv4` and `ipv6`.\n        :type Protocol: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddBandwidthPackageResourcesResponse(AbstractModel):
    """AddBandwidthPackageResources response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Address(AbstractModel):
    """Detailed EIP information

    """

    def __init__(self):
        """
        :param AddressId: `EIP` `ID`, the unique ID of the `EIP`.\n        :type AddressId: str\n        :param AddressName: The `EIP` name.\n        :type AddressName: str\n        :param AddressStatus: Possible `EIP` states are 'CREATING', 'BINDING', 'BIND', 'UNBINDING', 'UNBIND', 'OFFLINING', and 'BIND_ENI'.\n        :type AddressStatus: str\n        :param AddressIp: The public IP address\n        :type AddressIp: str\n        :param InstanceId: The ID of the bound resource instance. This can be a `CVM` or `NAT`.\n        :type InstanceId: str\n        :param CreatedTime: The creation time, which follows the `ISO8601` standard and uses `UTC` time in the format of `YYYY-MM-DDThh:mm:ssZ`.\n        :type CreatedTime: str\n        :param NetworkInterfaceId: The ID of the bound ENI\n        :type NetworkInterfaceId: str\n        :param PrivateAddressIp: The private IP of the bound resources\n        :type PrivateAddressIp: str\n        :param IsArrears: The isolation status of the resource. `True` indicates the EIP is isolated. `False` indicates that the resource is not isolated.\n        :type IsArrears: bool\n        :param IsBlocked: The block status of the resource. `True` indicates the EIP is blocked. `False` indicates that the EIP is not blocked.\n        :type IsBlocked: bool\n        :param IsEipDirectConnection: Whether the EIP supports direct connection mode. `True` indicates the EIP supports direct connection. `False` indicates that the resource does not support direct connection.\n        :type IsEipDirectConnection: bool\n        :param AddressType: The resource type of the EIP. This includes `CalcIP`, `WanIP`, `EIP`, and `AnycastEIP`. Among these, `CalcIP` indicates the device IP, `WanIP` indicates the common public IP, `EIP` indicates Elastic IP, and `AnycastEip` indicates accelerated EIP.\n        :type AddressType: str\n        :param CascadeRelease: Whether the EIP is automatically released after being unbound. `True` indicates the EIP will be automatically released after being unbound. `False` indicates the EIP will not be automatically released after being unbound.\n        :type CascadeRelease: bool\n        :param EipAlgType: Type of the protocol used in EIP ALG\n        :type EipAlgType: :class:`tencentcloud.vpc.v20170312.models.AlgType`\n        :param InternetServiceProvider: The ISP of an EIP/Elastic IP, with possible return values currently including "CMCC", "CTCC", "CUCC" and "BGP"\n        :type InternetServiceProvider: str\n        :param LocalBgp: Whether the EIP is in a local BGP.\n        :type LocalBgp: bool\n        :param Bandwidth: Bandwidth value of EIP. The EIP for the bill-by-CVM account will return `null`.
Note: this field may return `null`, indicating that no valid value was found.\n        :type Bandwidth: int\n        :param InternetChargeType: Network billing mode of EIP. The EIP for the bill-by-CVM account will return `null`.
Note: this field may return `null`, indicating that no valid value was found.\n        :type InternetChargeType: str\n        :param TagSet: List of tags associated with the EIP
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TagSet: list of Tag\n        """
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
        self.TagSet = None


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
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressChargePrepaid(AbstractModel):
    """EIP cost object

    """

    def __init__(self):
        """
        :param Period: Purchased usage period, in month. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36\n        :type Period: int\n        :param AutoRenewFlag: Setting of renewal. Valid values: 0: manual renewal; 1: auto-renewal; 2: no renewal after expiration. Default value: 0\n        :type AutoRenewFlag: int\n        """
        self.Period = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplate(AbstractModel):
    """IP address template

    """

    def __init__(self):
        """
        :param AddressTemplateName: IP address template name.\n        :type AddressTemplateName: str\n        :param AddressTemplateId: The unique ID of the IP address template instance.\n        :type AddressTemplateId: str\n        :param AddressSet: IP address information.\n        :type AddressSet: list of str\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        """
        self.AddressTemplateName = None
        self.AddressTemplateId = None
        self.AddressSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.AddressTemplateId = params.get("AddressTemplateId")
        self.AddressSet = params.get("AddressSet")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplateGroup(AbstractModel):
    """IP address template group

    """

    def __init__(self):
        """
        :param AddressTemplateGroupName: IP address template group name.\n        :type AddressTemplateGroupName: str\n        :param AddressTemplateGroupId: IP address template group instance ID, such as `ipmg-dih8xdbq`.\n        :type AddressTemplateGroupId: str\n        :param AddressTemplateIdSet: IP address template ID.\n        :type AddressTemplateIdSet: list of str\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        :param AddressTemplateSet: IP address template instance\n        :type AddressTemplateSet: list of AddressTemplateItem\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplateItem(AbstractModel):
    """Address information

    """

    def __init__(self):
        """
        :param From: Start address\n        :type From: str\n        :param To: End address\n        :type To: str\n        """
        self.From = None
        self.To = None


    def _deserialize(self, params):
        self.From = params.get("From")
        self.To = params.get("To")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplateSpecification(AbstractModel):
    """IP address template.

    """

    def __init__(self):
        """
        :param AddressId: The ID of the IP address, such as `ipm-2uw6ujo6`.\n        :type AddressId: str\n        :param AddressGroupId: The ID of the IP address group, such as `ipmg-2uw6ujo6`.\n        :type AddressGroupId: str\n        """
        self.AddressId = None
        self.AddressGroupId = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressGroupId = params.get("AddressGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgType(AbstractModel):
    """ALG protocol type

    """

    def __init__(self):
        """
        :param Ftp: Whether FTP ALG is enabled\n        :type Ftp: bool\n        :param Sip: Whether SIP ALG is enabled\n        :type Sip: bool\n        """
        self.Ftp = None
        self.Sip = None


    def _deserialize(self, params):
        self.Ftp = params.get("Ftp")
        self.Sip = params.get("Sip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateAddressesRequest(AbstractModel):
    """AllocateAddresses request structure.

    """

    def __init__(self):
        """
        :param AddressCount: The number of EIPs. Default: 1.\n        :type AddressCount: int\n        :param InternetServiceProvider: The EIP line type. Default: BGP.
<ul style="margin:0"><li>For a user who has activated the static single-line IP allowlist, possible values are:<ul><li>CMCC: China Mobile</li>
<li>CTCC: China Telecom</li>
<li>CUCC: China Unicom</li></ul>Note: Only certain regions support static single-line IP addresses.</li></ul>\n        :type InternetServiceProvider: str\n        :param InternetChargeType: The EIP billing method.
<ul style="margin:0"><li>For bill-by-IP account beta users, valid values: <ul><li>BANDWIDTH_PACKAGE: paid by the [bandwidth package](https://intl.cloud.tencent.com/document/product/684/15255?from_cn_redirect=1)(who must also be bandwidth package beta users)</li>
<li>BANDWIDTH_POSTPAID_BY_HOUR: billed by hourly bandwidth on a pay-as-you-go basis</li>
<li>BANDWIDTH_PREPAID_BY_MONTH: monthly bandwidth subscription</li>
<li>TRAFFIC_POSTPAID_BY_HOUR: billed by hourly traffic on a pay-as-you-go basis</li></ul>Default value: TRAFFIC_POSTPAID_BY_HOUR</li>
<li>If you are not a bill-by-IP account beta user, the EIP billing is the same as that for the instance bound to the EIP. Therefore, you do not need to pass in this parameter.</li></ul>\n        :type InternetChargeType: str\n        :param InternetMaxBandwidthOut: The EIP outbound bandwidth cap, in Mbps.
<ul style="margin:0"><li>For bill-by-IP account beta users, valid values:<ul><li>BANDWIDTH_PACKAGE: 1 Mbps to 1000 Mbps</li>
<li>BANDWIDTH_POSTPAID_BY_HOUR: 1 Mbps to 100 Mbps</li>
<li>BANDWIDTH_PREPAID_BY_MONTH: 1 Mbps to 200 Mbps</li>
<li>TRAFFIC_POSTPAID_BY_HOUR: 1 Mbps to 100 Mbps</li></ul>Default value: 1 Mbps</li>
<li>If you are not a bill-by-IP account beta user, the EIP outbound bandwidth cap is subject to that of the instance bound to the EIP. Therefore, you do not need to pass in this parameter.</li></ul>\n        :type InternetMaxBandwidthOut: int\n        :param AddressChargePrepaid: A required billing parameter for an EIP billed by monthly bandwidth subscription. For EIPs using other billing modes, it can be ignored.\n        :type AddressChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.AddressChargePrepaid`\n        :param AddressType: The EIP type. Default: `EIP`.
<ul style="margin:0"><li>For AIA beta users, the value should be:<ul><li>`AnycastEIP`: an AIA IP address. For more information, see [Anycast Internet Acceleration](https://intl.cloud.tencent.com/document/product/644?from_cn_redirect=1).</li></ul>Note: Anycast EIPs are only supported in some of the regions.</li></ul>
<ul style="margin:0"><li>For high-quality IP beta users, the value should be: <ul><li>`HighQualityEIP`: high-quality IP</li></ul>Note: High-quality IPs are only supported in some of the regions.</li></ul>\n        :type AddressType: str\n        :param AnycastZone: Anycast publishing region
<ul style="margin:0"><li>Valid for users who have activated AIA. Values:<ul><li>ANYCAST_ZONE_GLOBAL: global publishing region </li><li>ANYCAST_ZONE_OVERSEAS: overseas publishing region</li><li><b>**[Disused]**</b> ANYCAST_ZONE_A: publishing region A (updated to ANYCAST_ZONE_GLOBAL)</li><li><b>**[Disused]**</b> ANYCAST_ZONE_B: publishing region B (updated to ANYCAST_ZONE_GLOBAL)</li></ul>Default: ANYCAST_ZONE_OVERSEAS.</li></ul>\n        :type AnycastZone: str\n        :param ApplicableForCLB: <b>**[Disused]**</b>
Whether the Anycast EIP can be bound to CLB instances.
<ul style="margin:0"><li>Valid for users who have activated the AIA. Values:<ul><li>TRUE: the Anycast EIP can be bound to CLB instances.</li>
<li>FALSE: the Anycast EIP can be bound to CVMs, NAT gateways, and HAVIPs.</li></ul>Default: FALSE.</li></ul>\n        :type ApplicableForCLB: bool\n        :param Tags: List of tags to be bound.\n        :type Tags: list of Tag\n        :param BandwidthPackageId: The unique ID of a BGP bandwidth package. If you configure this parameter and set InternetChargeType as BANDWIDTH_PACKAGE, the new EIP is added to this package and billed by the bandwidth package mode.\n        :type BandwidthPackageId: str\n        :param AddressName: EIP name, which is the custom EIP name given by the user when applying for the EIP. Default: not named\n        :type AddressName: str\n        """
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
        self.AddressName = None


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
        self.AddressName = params.get("AddressName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateAddressesResponse(AbstractModel):
    """AllocateAddresses response structure.

    """

    def __init__(self):
        """
        :param AddressSet: List of the unique IDs of the requested EIPs.\n        :type AddressSet: list of str\n        :param TaskId: The Async task ID. You can use the [DescribeTaskResult](https://intl.cloud.tencent.com/document/api/215/36271?from_cn_redirect=1) API to query the task status.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param NetworkInterfaceId: The `ID` of the ENI instance, such as `eni-m6dyj72l`.\n        :type NetworkInterfaceId: str\n        :param Ipv6Addresses: A list of `IPv6` addresses. You can specify a maximum of 10 at one time. The quota is calculated together with that of `Ipv6AddressCount`, a required input parameter alternative to this one.\n        :type Ipv6Addresses: list of Ipv6Address\n        :param Ipv6AddressCount: The number of automatically assigned `IPv6` addresses. The total number of private IP addresses cannot exceed the quota. The quota is calculated together with that of `Ipv6Addresses`, a required input parameter alternative to this one.\n        :type Ipv6AddressCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6AddressesResponse(AbstractModel):
    """AssignIpv6Addresses response structure.

    """

    def __init__(self):
        """
        :param Ipv6AddressSet: The list of `IPv6` addresses assigned to ENIs.\n        :type Ipv6AddressSet: list of Ipv6Address\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The `ID` of the `VPC`, such as `vpc-f49l6u0z`.\n        :type VpcId: str\n        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6CidrBlockResponse(AbstractModel):
    """AssignIpv6CidrBlock response structure.

    """

    def __init__(self):
        """
        :param Ipv6CidrBlock: The assigned `IPv6` IP range, such as `3402:4e00:20:1000::/56`\n        :type Ipv6CidrBlock: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The `ID` of the VPC where the subnet is located, such as `vpc-f49l6u0z`.\n        :type VpcId: str\n        :param Ipv6SubnetCidrBlocks: The assigned `IPv6` subnet IP range list.\n        :type Ipv6SubnetCidrBlocks: list of Ipv6SubnetCidrBlock\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6SubnetCidrBlockResponse(AbstractModel):
    """AssignIpv6SubnetCidrBlock response structure.

    """

    def __init__(self):
        """
        :param Ipv6SubnetCidrBlockSet: The assigned `IPv6` subnet IP range list.\n        :type Ipv6SubnetCidrBlockSet: list of Ipv6SubnetCidrBlock\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddresses: The information on private IP addresses, of which you can specify a maximum of 10 at a time. You should provide either this parameter or SecondaryPrivateIpAddressCount, or both.\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        :param SecondaryPrivateIpAddressCount: The number of newly-applied private IP addresses. You should provide either this parameter or PrivateIpAddresses, or both. The total number of private IP addresses cannot exceed the quota. For more information, see<a href="/document/product/576/18527">ENI Use Limits</a>.\n        :type SecondaryPrivateIpAddressCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignPrivateIpAddressesResponse(AbstractModel):
    """AssignPrivateIpAddresses response structure.

    """

    def __init__(self):
        """
        :param PrivateIpAddressSet: The detailed information of the Private IP.\n        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The `ID` of a `VPC` instance, such as `vpc-6v2ht8q5`.\n        :type VpcId: str\n        :param CidrBlock: The secondary CIDR, such as `172.16.0.0/16`.\n        :type CidrBlock: str\n        :param AssistantType: The secondary CIDR block type. 0: common secondary CIDR block. 1: container secondary CIDR block. Default: 0.\n        :type AssistantType: int\n        :param SubnetSet: Subnets divided by the secondary CIDR.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type SubnetSet: list of Subnet\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAddressRequest(AbstractModel):
    """AssociateAddress request structure.

    """

    def __init__(self):
        """
        :param AddressId: The unique ID of the EIP, such as `eip-11112222`.\n        :type AddressId: str\n        :param InstanceId: The ID of the instance to be bound, such as `ins-11112222`. You can query the instance ID by logging into the [Console](https://console.cloud.tencent.com/cvm). You can also obtain the parameter value from the `InstanceId` field in the returned result of [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API.\n        :type InstanceId: str\n        :param NetworkInterfaceId: The ID of the ENI to be bonud, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. You can query the ENI ID by logging into the [Console](https://console.cloud.tencent.com/vpc/eni). You can also obtain the parameter value from the `networkInterfaceId` field in the returned result of [DescribeNetworkInterfaces](https://intl.cloud.tencent.com/document/api/215/15817?from_cn_redirect=1) API.\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddress: The private IP to be bound. If you specify `NetworkInterfaceId`, then you must also specify `PrivateIpAddress`, indicating the EIP is bound to the specified private IP of the specified ENI. At the same time, you must ensure the specified `PrivateIpAddress` is a private IP on the `NetworkInterfaceId`. You can query the private IP of the specified ENI by logging into the [Console](https://console.cloud.tencent.com/vpc/eni). You can also obtain the parameter value from the `privateIpAddress` field in the returned result of [DescribeNetworkInterfaces](https://intl.cloud.tencent.com/document/api/215/15817?from_cn_redirect=1) API.\n        :type PrivateIpAddress: str\n        :param EipDirectConnection: Whether to enable direct access when binding a specified EIP. For more information, see [EIP Direct Access](https://intl.cloud.tencent.com/document/product/1199/41709?from_cn_redirect=1). Valid values: `True` and `False`; default value: `False`. You can set this parameter to `True` when binding an EIP to a CVM instance or an EKS elastic cluster. This parameter is currently in beta. To use it, please [submit a ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20CLB&level3_id=1071&queue=96&scene_code=34639&step=2).\n        :type EipDirectConnection: bool\n        """
        self.AddressId = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None
        self.EipDirectConnection = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.InstanceId = params.get("InstanceId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.EipDirectConnection = params.get("EipDirectConnection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAddressResponse(AbstractModel):
    """AssociateAddress response structure.

    """

    def __init__(self):
        """
        :param TaskId: The async task ID. You can use the [DescribeTaskResult](https://intl.cloud.tencent.com/document/api/215/36271?from_cn_redirect=1) API to query the task status.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The direct connect gateway ID.\n        :type VpcId: str\n        :param NatGatewayId: The NAT Gateway ID.\n        :type NatGatewayId: str\n        :param DirectConnectGatewayId: The ID of the VPC instance, which can be obtained from the `VpcId` field in response of the `DescribeVpcs` API.\n        :type DirectConnectGatewayId: str\n        """
        self.VpcId = None
        self.NatGatewayId = None
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NatGatewayId = params.get("NatGatewayId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDirectConnectGatewayNatGatewayResponse(AbstractModel):
    """AssociateDirectConnectGatewayNatGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNatGatewayAddressRequest(AbstractModel):
    """AssociateNatGatewayAddress request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.\n        :type NatGatewayId: str\n        :param AddressCount: The number of EIPs you want to apply for. The system will create the same number of EIPs as you require. Either `AddressCount` or `PublicAddresses` must be passed in.\n        :type AddressCount: int\n        :param PublicIpAddresses: Array of the EIPs bound to the NAT gateway. Either `AddressCount` or `PublicAddresses` must be passed in.\n        :type PublicIpAddresses: list of str\n        :param Zone: The availability zone of the EIP, which is passed in when the EIP is automatically assigned.\n        :type Zone: str\n        """
        self.NatGatewayId = None
        self.AddressCount = None
        self.PublicIpAddresses = None
        self.Zone = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.AddressCount = params.get("AddressCount")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateNatGatewayAddressResponse(AbstractModel):
    """AssociateNatGatewayAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNetworkAclSubnetsRequest(AbstractModel):
    """AssociateNetworkAclSubnets request structure.

    """

    def __init__(self):
        """
        :param NetworkAclId: Network ACL instance ID. Example: acl-12345678.\n        :type NetworkAclId: str\n        :param SubnetIds: Array of subnet instance IDs. Example: [subnet-12345678]\n        :type SubnetIds: list of str\n        """
        self.NetworkAclId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateNetworkAclSubnetsResponse(AbstractModel):
    """AssociateNetworkAclSubnets response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNetworkInterfaceSecurityGroupsRequest(AbstractModel):
    """AssociateNetworkInterfaceSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: ENI instance ID, e.g. eni-pxir56ns. You can enter up to 100 instances for each request.\n        :type NetworkInterfaceIds: list of str\n        :param SecurityGroupIds: The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups. You can enter up to 100 instances for each request.\n        :type SecurityGroupIds: list of str\n        """
        self.NetworkInterfaceIds = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateNetworkInterfaceSecurityGroupsResponse(AbstractModel):
    """AssociateNetworkInterfaceSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachCcnInstancesRequest(AbstractModel):
    """AttachCcnInstances request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        :param Instances: List of associated network instances\n        :type Instances: list of CcnInstance\n        :param CcnUin: The UIN (root account) of the CCN. By default, the current account belongs to the UIN\n        :type CcnUin: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCcnInstancesResponse(AbstractModel):
    """AttachCcnInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachClassicLinkVpcRequest(AbstractModel):
    """AttachClassicLinkVpc request structure.

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID\n        :type VpcId: str\n        :param InstanceIds: CVM Instance ID\n        :type InstanceIds: list of str\n        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachClassicLinkVpcResponse(AbstractModel):
    """AttachClassicLinkVpc response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachNetworkInterfaceRequest(AbstractModel):
    """AttachNetworkInterface request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.\n        :type NetworkInterfaceId: str\n        :param InstanceId: The ID of the CVM instance, such as `ins-r8hr2upy`.\n        :type InstanceId: str\n        :param AttachType: ENI mounting type. Valid values: `0` (standard); `1` (extension); default value: `0`\n        :type AttachType: int\n        """
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.AttachType = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.AttachType = params.get("AttachType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachNetworkInterfaceResponse(AbstractModel):
    """AttachNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AuditCrossBorderComplianceRequest(AbstractModel):
    """AuditCrossBorderCompliance request structure.

    """

    def __init__(self):
        """
        :param ServiceProvider: Service provider. Valid values: `UNICOM`.\n        :type ServiceProvider: str\n        :param ComplianceId: Unique ID of compliance review request.\n        :type ComplianceId: int\n        :param AuditBehavior: Audit behavior. Valid values: `APPROVED` and `DENY`.\n        :type AuditBehavior: str\n        """
        self.ServiceProvider = None
        self.ComplianceId = None
        self.AuditBehavior = None


    def _deserialize(self, params):
        self.ServiceProvider = params.get("ServiceProvider")
        self.ComplianceId = params.get("ComplianceId")
        self.AuditBehavior = params.get("AuditBehavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditCrossBorderComplianceResponse(AbstractModel):
    """AuditCrossBorderCompliance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BandwidthPackage(AbstractModel):
    """The structure of information of the bandwidth package.

    """

    def __init__(self):
        """
        :param BandwidthPackageId: The unique ID of the bandwidth package.\n        :type BandwidthPackageId: str\n        :param NetworkType: The bandwidth package type. Valid values: 'BGP', 'SINGLEISP', and 'ANYCAST'\n        :type NetworkType: str\n        :param ChargeType: The bandwidth package billing mode. Valid values: 'TOP5_POSTPAID_BY_MONTH' and 'PERCENT95_POSTPAID_BY_MONTH'\n        :type ChargeType: str\n        :param BandwidthPackageName: The name of the bandwidth package.\n        :type BandwidthPackageName: str\n        :param CreatedTime: The creation time of the bandwidth package, which follows the `ISO8601` standard and uses `UTC` time in the format of `YYYY-MM-DDThh:mm:ssZ`.\n        :type CreatedTime: str\n        :param Status: The status of the bandwidth package. Valid values: 'CREATING', 'CREATED', 'DELETING', and 'DELETED'.\n        :type Status: str\n        :param ResourceSet: The resource information of the bandwidth package.\n        :type ResourceSet: list of Resource\n        :param Bandwidth: The limit of the bandwidth package in Mbps. The value '-1' indicates there is no limit.\n        :type Bandwidth: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BandwidthPackageBillBandwidth(AbstractModel):
    """Current billable usage of a pay-as-you-go bandwidth package

    """

    def __init__(self):
        """
        :param BandwidthUsage: Current billable usage, in Mbps\n        :type BandwidthUsage: int\n        """
        self.BandwidthUsage = None


    def _deserialize(self, params):
        self.BandwidthUsage = params.get("BandwidthUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCN(AbstractModel):
    """The CCN object

    """

    def __init__(self):
        """
        :param CcnId: The unique ID of the CCN\n        :type CcnId: str\n        :param CcnName: The name of the CCN\n        :type CcnName: str\n        :param CcnDescription: The detailed information of the CCN\n        :type CcnDescription: str\n        :param InstanceCount: The number of associated instances\n        :type InstanceCount: int\n        :param CreateTime: The creation time\n        :type CreateTime: str\n        :param State: The instance status. 'ISOLATED': Being isolated (instance is in arrears and service is suspended). 'AVAILABLE': Operating.\n        :type State: str\n        :param QosLevel: The instance service quality. ’PT’: Platinum , 'AU': Gold, 'AG': Silver.\n        :type QosLevel: str\n        :param InstanceChargeType: The billing method. POSTPAID indicates postpaid.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type InstanceChargeType: str\n        :param BandwidthLimitType: The limit type. INTER_REGION_LIMIT is the limit between regions. OUTER_REGION_LIMIT is a region egress limit.
Note: This field may return null, indicating no valid value.\n        :type BandwidthLimitType: str\n        :param TagSet: Tag key-value pairs.\n        :type TagSet: list of Tag\n        :param RoutePriorityFlag: Whether the CCN route priority feature is supported. Valid values: False: do not support; True: support.\n        :type RoutePriorityFlag: bool\n        :param RouteTableCount: Number of route tables associated with the instance.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type RouteTableCount: int\n        :param RouteTableFlag: Whether the multiple route tables feature is enabled for the CCN instance. Valid values: `False`: no; `True`: yes. Default value: `False`.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type RouteTableFlag: bool\n        """
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
        self.RouteTableCount = None
        self.RouteTableFlag = None


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
        self.RouteTableCount = params.get("RouteTableCount")
        self.RouteTableFlag = params.get("RouteTableFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnAttachedInstance(AbstractModel):
    """The instance object associated with a CCN

    """

    def __init__(self):
        """
        :param CcnId: The ID of a CCN instance.\n        :type CcnId: str\n        :param InstanceType: The type of associated instances:
<li>`VPC`: VPC</li>
<li>`DIRECTCONNECT`: Direct Connect</li>
<li>`BMVPC`: BM VPC</li>\n        :type InstanceType: str\n        :param InstanceId: The ID of the associated instance.\n        :type InstanceId: str\n        :param InstanceName: The name of the associated instance.\n        :type InstanceName: str\n        :param InstanceRegion: The region to which the associated instance belongs, such as `ap-guangzhou`.\n        :type InstanceRegion: str\n        :param InstanceUin: The UIN (root account) to which the associated instance belongs.\n        :type InstanceUin: str\n        :param CidrBlock: The CIDR of the associated instance.\n        :type CidrBlock: list of str\n        :param State: The status of the associated instance:
<li>`PENDING`: In application</li>
<li>`ACTIVE`: Connected</li>
<li>`EXPIRED`: Expired</li>
<li>`REJECTED`: Rejected</li>
<li>`DELETED`: Deleted</li>
<li>`FAILED`: Failed (it will be asynchronously unbound after 2 hours)</li>
<li>`ATTACHING`: binding</li>
<li>`DETACHING`: Unbinding</li>
<li>`DETACHFAILED`: The unbinding failed (it will be asynchronously unbound after 2 hours)</li>\n        :type State: str\n        :param AttachedTime: Association Time.\n        :type AttachedTime: str\n        :param CcnUin: The UIN (root account) to which the CCN belongs.\n        :type CcnUin: str\n        :param InstanceArea: General location of the associated instance, such as CHINA_MAINLAND.\n        :type InstanceArea: str\n        :param Description: Description\n        :type Description: str\n        :param RouteTableId: Route table ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type RouteTableId: str\n        :param RouteTableName: Route table name
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type RouteTableName: str\n        """
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
        self.Description = None
        self.RouteTableId = None
        self.RouteTableName = None


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
        self.Description = params.get("Description")
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnBandwidthInfo(AbstractModel):
    """The information of the cross-region bandwidth limit for CCN instances.

    """

    def __init__(self):
        """
        :param CcnId: The CCN ID that the bandwidth belongs to.
Note: this field may return null, indicating that no valid value was found.\n        :type CcnId: str\n        :param CreatedTime: The creation time of the instance.
Note: this field may return null, indicating that no valid value was found.\n        :type CreatedTime: str\n        :param ExpiredTime: The expiration time of the instance.
Note: this field may return null, indicating that no valid value was found.\n        :type ExpiredTime: str\n        :param RegionFlowControlId: The unique ID of the bandwidth instance.
Note: this field may return null, indicating that no valid value was found.\n        :type RegionFlowControlId: str\n        :param RenewFlag: The billing flag.
Note: this field may return null, indicating that no valid value was found.\n        :type RenewFlag: str\n        :param CcnRegionBandwidthLimit: The information of the bandwidth regions and bandwidth caps. The parameter is only returned for the cross-region limit mode, but not for egress limit.
Note: this field may return null, indicating that no valid value was found.\n        :type CcnRegionBandwidthLimit: :class:`tencentcloud.vpc.v20170312.models.CcnRegionBandwidthLimit`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnInstance(AbstractModel):
    """The instance object associated with a CCN.

    """

    def __init__(self):
        """
        :param InstanceId: The ID of the associated instance.\n        :type InstanceId: str\n        :param InstanceRegion: The region to which the associated instance ID belongs, such as `ap-guangzhou`.\n        :type InstanceRegion: str\n        :param InstanceType: The type of the associated instance. Available values are:
<li>`VPC`: VPC</li>
<li>`DIRECTCONNECT`: Direct Connect</li>
<li>`BMVPC`: BM VPC</li>\n        :type InstanceType: str\n        :param Description: Description\n        :type Description: str\n        :param RouteTableId: The ID of the route table associated with the instance
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type RouteTableId: str\n        """
        self.InstanceId = None
        self.InstanceRegion = None
        self.InstanceType = None
        self.Description = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceRegion = params.get("InstanceRegion")
        self.InstanceType = params.get("InstanceType")
        self.Description = params.get("Description")
        self.RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnRegionBandwidthLimit(AbstractModel):
    """The outbound bandwidth cap of the CCN region

    """

    def __init__(self):
        """
        :param Region: Region, such as `ap-guangzhou`\n        :type Region: str\n        :param BandwidthLimit: The outbound bandwidth cap. Units: Mbps\n        :type BandwidthLimit: int\n        :param IsBm: Whether it is a BM region. The default is `false`.\n        :type IsBm: bool\n        :param DstRegion: The target region, such as `ap-shanghai`
Note: This field may return null, indicating no valid value.\n        :type DstRegion: str\n        :param DstIsBm: Whether the target region is a BM region. The default is `false`.\n        :type DstIsBm: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnRoute(AbstractModel):
    """The CCN routing policy object

    """

    def __init__(self):
        """
        :param RouteId: The ID of the routing policy\n        :type RouteId: str\n        :param DestinationCidrBlock: Destination\n        :type DestinationCidrBlock: str\n        :param InstanceType: The type of the next hop (associated instance type). Available types: VPC, DIRECTCONNECT\n        :type InstanceType: str\n        :param InstanceId: The next hop (associated instance)\n        :type InstanceId: str\n        :param InstanceName: The name of the next hop (associated instance name)\n        :type InstanceName: str\n        :param InstanceRegion: The region of the next hop (the region of the associated instance)\n        :type InstanceRegion: str\n        :param UpdateTime: Update Time\n        :type UpdateTime: str\n        :param Enabled: Whether the route is enabled\n        :type Enabled: bool\n        :param InstanceUin: The UIN (root account) to which the associated instance belongs\n        :type InstanceUin: str\n        :param ExtraState: Additional status of the route\n        :type ExtraState: str\n        :param IsBgp: Whether it is a dynamic route\n        :type IsBgp: bool\n        :param RoutePriority: Route priority\n        :type RoutePriority: int\n        :param InstanceExtraName: Next hop port name (associated instance’s port name)\n        :type InstanceExtraName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAssistantCidrRequest(AbstractModel):
    """CheckAssistantCidr request structure.

    """

    def __init__(self):
        """
        :param VpcId: `VPC` instance `ID`, e.g. `vpc-6v2ht8q5`.\n        :type VpcId: str\n        :param NewCidrBlocks: Load CIDR blocks to add. CIDR block set; format: e.g. ["10.0.0.0/16", "172.16.0.0/16"]\n        :type NewCidrBlocks: list of str\n        :param OldCidrBlocks: Load CIDR blocks to delete. CIDR block set; Format: e.g. ["10.0.0.0/16", "172.16.0.0/16"]\n        :type OldCidrBlocks: list of str\n        """
        self.VpcId = None
        self.NewCidrBlocks = None
        self.OldCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NewCidrBlocks = params.get("NewCidrBlocks")
        self.OldCidrBlocks = params.get("OldCidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAssistantCidrResponse(AbstractModel):
    """CheckAssistantCidr response structure.

    """

    def __init__(self):
        """
        :param ConflictSourceSet: Array of conflict resources.\n        :type ConflictSourceSet: list of ConflictSource\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param DetectDestinationIp: The array of detection destination IPv4 addresses, which contains at most two IP addresses.\n        :type DetectDestinationIp: list of str\n        :param NextHopType: The type of the next hop. Currently supported types are:
VPN: VPN gateway;
DIRECTCONNECT: direct connect gateway;
PEERCONNECTION: peering connection;
NAT: NAT gateway;
NORMAL_CVM: normal CVM.\n        :type NextHopType: str\n        :param NextHopDestination: The next-hop destination gateway. The value is related to NextHopType.
If NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.
If NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.
If NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.
If NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.
If NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12.\n        :type NextHopDestination: str\n        :param NetDetectId: ID of a network inspector instance, e.g. netd-12345678. Enter at least one of this parameter, VpcId, SubnetId, and NetDetectName. Use NetDetectId if it is present.\n        :type NetDetectId: str\n        :param VpcId: ID of a `VPC` instance, e.g. `vpc-12345678`, which is used together with SubnetId and NetDetectName. You should enter either this parameter or NetDetectId, or both. Use NetDetectId if it is present.\n        :type VpcId: str\n        :param SubnetId: ID of a subnet instance, e.g. `subnet-12345678`, which is used together with VpcId and NetDetectName. You should enter either this parameter or NetDetectId, or both. Use NetDetectId if it is present.\n        :type SubnetId: str\n        :param NetDetectName: The name of a network inspector, up to 60 bytes in length. It is used together with VpcId and NetDetectName. You should enter either this parameter or NetDetectId, or both. Use NetDetectId if it is present.\n        :type NetDetectName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckNetDetectStateResponse(AbstractModel):
    """CheckNetDetectState response structure.

    """

    def __init__(self):
        """
        :param NetDetectIpStateSet: The array of network detection verification results.\n        :type NetDetectIpStateSet: list of NetDetectIpState\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class CidrForCcn(AbstractModel):
    """Publishes the routing policy of the VPC subnet to CCN

    """

    def __init__(self):
        """
        :param Cidr: Local CIDR block, including subnet CIDR block and secondary CIDR block
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Cidr: str\n        :param PublishedToVbc: Whether the routing policy of the VPC subnet is published to CCN.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type PublishedToVbc: bool\n        """
        self.Cidr = None
        self.PublishedToVbc = None


    def _deserialize(self, params):
        self.Cidr = params.get("Cidr")
        self.PublishedToVbc = params.get("PublishedToVbc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicLinkInstance(AbstractModel):
    """Classiclink instance

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID\n        :type VpcId: str\n        :param InstanceId: The unique ID of the CVM instance\n        :type InstanceId: str\n        """
        self.VpcId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneSecurityGroupRequest(AbstractModel):
    """CloneSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: ID of the security group to be cloned, such as `sg-33ocnj9n`. This can be obtained through the `DescribeSecurityGroups` API.\n        :type SecurityGroupId: str\n        :param GroupName: The name of security group clone. You can enter any name within 60 characters. If this parameter is left empty, the security group clone will use the name of the source security group.\n        :type GroupName: str\n        :param GroupDescription: Description of the security group clone. You can enter up to 100 characters. If this parameter is left empty, the security group clone will use the description of the source security group.\n        :type GroupDescription: str\n        :param ProjectId: Project ID of the security group clone. The default is 0. You can query it on the project management page of the Tencent Cloud console.\n        :type ProjectId: str\n        :param RemoteRegion: The region of the source security group for a cross-region clone. For example, to clone the security group in Guangzhou to Shanghai, set it to `ap-guangzhou`.\n        :type RemoteRegion: str\n        """
        self.SecurityGroupId = None
        self.GroupName = None
        self.GroupDescription = None
        self.ProjectId = None
        self.RemoteRegion = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        self.ProjectId = params.get("ProjectId")
        self.RemoteRegion = params.get("RemoteRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneSecurityGroupResponse(AbstractModel):
    """CloneSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param SecurityGroup: Security group object
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class ConflictItem(AbstractModel):
    """Conflict resource items.

    """

    def __init__(self):
        """
        :param ConfilctId: Conflict resource ID\n        :type ConfilctId: str\n        :param DestinationItem: Conflict destination resource\n        :type DestinationItem: str\n        """
        self.ConfilctId = None
        self.DestinationItem = None


    def _deserialize(self, params):
        self.ConfilctId = params.get("ConfilctId")
        self.DestinationItem = params.get("DestinationItem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConflictSource(AbstractModel):
    """Conflict resource.

    """

    def __init__(self):
        """
        :param ConflictSourceId: Conflict resource ID\n        :type ConflictSourceId: str\n        :param SourceItem: Conflict resource\n        :type SourceItem: str\n        :param ConflictItemSet: Conflict resource items\n        :type ConflictItemSet: list of ConflictItem\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAddressTemplateGroupRequest(AbstractModel):
    """CreateAddressTemplateGroup request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateGroupName: The name of the IP address template group.\n        :type AddressTemplateGroupName: str\n        :param AddressTemplateIds: The instance ID of the IP address template, such as `ipm-mdunqeb6`.\n        :type AddressTemplateIds: list of str\n        """
        self.AddressTemplateGroupName = None
        self.AddressTemplateIds = None


    def _deserialize(self, params):
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateIds = params.get("AddressTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAddressTemplateGroupResponse(AbstractModel):
    """CreateAddressTemplateGroup response structure.

    """

    def __init__(self):
        """
        :param AddressTemplateGroup: Group object of the IP address template.\n        :type AddressTemplateGroup: :class:`tencentcloud.vpc.v20170312.models.AddressTemplateGroup`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param AddressTemplateName: The name of the IP address template\n        :type AddressTemplateName: str\n        :param Addresses: Address information, including IP, CIDR and IP address range.\n        :type Addresses: list of str\n        """
        self.AddressTemplateName = None
        self.Addresses = None


    def _deserialize(self, params):
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.Addresses = params.get("Addresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAddressTemplateResponse(AbstractModel):
    """CreateAddressTemplate response structure.

    """

    def __init__(self):
        """
        :param AddressTemplate: The template object of the IP address.\n        :type AddressTemplate: :class:`tencentcloud.vpc.v20170312.models.AddressTemplate`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the `VpcId` field in the returned result of the `DescribeVpcs` API.\n        :type VpcId: str\n        :param NetworkInterfaceName: The name of the ENI. The maximum length is 60 bytes.\n        :type NetworkInterfaceName: str\n        :param SubnetId: The subnet instance ID of the ENI, such as 'subnet-0ap8nwca'.\n        :type SubnetId: str\n        :param InstanceId: CVM instance ID.\n        :type InstanceId: str\n        :param PrivateIpAddresses: The information of the specified private IPs. You can specify a maximum of 10 IPs each time.\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        :param SecondaryPrivateIpAddressCount: The number of private IP addresses you can apply for. The total number of private IP addresses cannot exceed the quota.\n        :type SecondaryPrivateIpAddressCount: int\n        :param SecurityGroupIds: The security group to be bound with, such as ['sg-1dd51d'].\n        :type SecurityGroupIds: list of str\n        :param NetworkInterfaceDescription: The ENI description. You can enter any information within 60 characters.\n        :type NetworkInterfaceDescription: str\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        :param AttachType: ENI mounting type. Valid values: `0` (standard); `1` (extension); default value: `0`\n        :type AttachType: int\n        """
        self.VpcId = None
        self.NetworkInterfaceName = None
        self.SubnetId = None
        self.InstanceId = None
        self.PrivateIpAddresses = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.NetworkInterfaceDescription = None
        self.Tags = None
        self.AttachType = None


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
        self.AttachType = params.get("AttachType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndAttachNetworkInterfaceResponse(AbstractModel):
    """CreateAndAttachNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param NetworkInterface: The ENI instance.\n        :type NetworkInterface: :class:`tencentcloud.vpc.v20170312.models.NetworkInterface`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: `VPC` instance `ID`, e.g. `vpc-6v2ht8q5`.\n        :type VpcId: str\n        :param CidrBlocks: CIDR set, e.g. ["10.0.0.0/16", "172.16.0.0/16"]\n        :type CidrBlocks: list of str\n        """
        self.VpcId = None
        self.CidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlocks = params.get("CidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssistantCidrResponse(AbstractModel):
    """CreateAssistantCidr response structure.

    """

    def __init__(self):
        """
        :param AssistantCidrSet: A set of secondary CIDR blocks.
Note: This field may return null, indicating that no valid value was found.\n        :type AssistantCidrSet: list of AssistantCidr\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param NetworkType: The type of the bandwidth package. Valid values: `HIGH_QUALITY_BGP`, `BGP`, `SINGLEISP`, and `ANYCAST`.\n        :type NetworkType: str\n        :param ChargeType: The bandwidth package billing mode. Valid values: 'TOP5_POSTPAID_BY_MONTH' and 'PERCENT95_POSTPAID_BY_MONTH'.\n        :type ChargeType: str\n        :param BandwidthPackageName: The name of the bandwidth package.\n        :type BandwidthPackageName: str\n        :param BandwidthPackageCount: The number of bandwidth packages (It can only be “1” for bill-by-CVM accounts)\n        :type BandwidthPackageCount: int\n        :param InternetMaxBandwidth: The limit of the bandwidth package in Mbps. The value '-1' indicates there is no limit. This feature is currently in beta.\n        :type InternetMaxBandwidth: int\n        :param Tags: The list of tags to be bound.\n        :type Tags: list of Tag\n        :param Protocol: The protocol type of the bandwidth package. Valid values: 'ipv4' and 'ipv6'. Default value: 'ipv4'.\n        :type Protocol: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBandwidthPackageResponse(AbstractModel):
    """CreateBandwidthPackage response structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageId: The unique ID of the bandwidth package.\n        :type BandwidthPackageId: str\n        :param BandwidthPackageIds: The unique ID list of the bandwidth package (effective only when you apply for more than 1 bandwidth packages).\n        :type BandwidthPackageIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param CcnName: The name of the CCN. The maximum length is 60 characters.\n        :type CcnName: str\n        :param CcnDescription: The description of the CCN. The maximum length is 100 characters.\n        :type CcnDescription: str\n        :param QosLevel: CCN service quality, 'PT': Platinum, 'AU': Gold, 'AG': Silver. The default is 'AU'.\n        :type QosLevel: str\n        :param InstanceChargeType: The billing method. POSTPAID: postpaid by traffic. Default: POSTPAID.\n        :type InstanceChargeType: str\n        :param BandwidthLimitType: The bandwidth limit type. Valid values: OUTER_REGION_LIMIT: region outbound bandwidth limit; INTER_REGION_LIMIT: inter-region bandwidth limit. Default value: OUTER_REGION_LIMIT. Monthly-subscribed CCN instances only support inter-region bandwidth limit, while pay-as-you-go CCN instances support the both bandwidth limit types.\n        :type BandwidthLimitType: str\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCcnResponse(AbstractModel):
    """CreateCcn response structure.

    """

    def __init__(self):
        """
        :param Ccn: The CCN object.\n        :type Ccn: :class:`tencentcloud.vpc.v20170312.models.CCN`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param CustomerGatewayName: Customer gateway can be named freely, but the maximum length is 60 characters.\n        :type CustomerGatewayName: str\n        :param IpAddress: Customer gateway public IP.\n        :type IpAddress: str\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomerGatewayResponse(AbstractModel):
    """CreateCustomerGateway response structure.

    """

    def __init__(self):
        """
        :param CustomerGateway: Customer gateway object\n        :type CustomerGateway: :class:`tencentcloud.vpc.v20170312.models.CustomerGateway`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Zone: The ID of the availability zone in which the subnet resides. This parameter can be obtained through the [`DescribeZones`](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1) API, such as `ap-guangzhou-1`. If it’s not specified, a random availability zone will be used.\n        :type Zone: str\n        :param Force: Whether to forcibly return a default VPC\n        :type Force: bool\n        """
        self.Zone = None
        self.Force = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDefaultVpcResponse(AbstractModel):
    """CreateDefaultVpc response structure.

    """

    def __init__(self):
        """
        :param Vpc: Default VPC and subnet IDs\n        :type Vpc: :class:`tencentcloud.vpc.v20170312.models.DefaultVpcSubnet`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param DirectConnectGatewayId: The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`\n        :type DirectConnectGatewayId: str\n        :param Routes: The list of IDC IP range that must be connected\n        :type Routes: list of DirectConnectGatewayCcnRoute\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """CreateDirectConnectGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDirectConnectGatewayRequest(AbstractModel):
    """CreateDirectConnectGateway request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayName: The name of the direct connect gateway.\n        :type DirectConnectGatewayName: str\n        :param NetworkType: The type of the associated network. Valid values:
<li>VPC</li>
<li>CCN</li>\n        :type NetworkType: str\n        :param NetworkInstanceId: <li>When the NetworkType is VPC, this value is the VPC instance ID</li>
<li>When the NetworkType is CCN, this value is the CCN instance ID</li>\n        :type NetworkInstanceId: str\n        :param GatewayType: The type of the gateway. Valid values:
<li>NORMAL - (Default) Standard type. Note: CCN only supports the standard type</li>
<li>NAT - NAT type</li>NAT gateway supports network address translation. The specified type cannot be modified. A VPC can create one NAT direct connect gateway and one non-NAT direct connect gateway\n        :type GatewayType: str\n        :param ModeType: CCN route publishing method. Valid values: `standard` and `exquisite`. This parameter is only valid for the CCN direct connect gateway.\n        :type ModeType: str\n        :param Zone: Availability zone where the direct connect gateway resides.\n        :type Zone: str\n        """
        self.DirectConnectGatewayName = None
        self.NetworkType = None
        self.NetworkInstanceId = None
        self.GatewayType = None
        self.ModeType = None
        self.Zone = None


    def _deserialize(self, params):
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.NetworkType = params.get("NetworkType")
        self.NetworkInstanceId = params.get("NetworkInstanceId")
        self.GatewayType = params.get("GatewayType")
        self.ModeType = params.get("ModeType")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectGatewayResponse(AbstractModel):
    """CreateDirectConnectGateway response structure.

    """

    def __init__(self):
        """
        :param DirectConnectGateway: The object of the direct connect gateway.\n        :type DirectConnectGateway: :class:`tencentcloud.vpc.v20170312.models.DirectConnectGateway`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: ID of the VPC instance\n        :type VpcId: str\n        :param FlowLogName: The name of the flow log instance.\n        :type FlowLogName: str\n        :param ResourceType: The type of resources to which the flow log belongs. Valid values: 'VPC', 'SUBNET' and 'NETWORKINTERFACE'.\n        :type ResourceType: str\n        :param ResourceId: The unique ID of the resource.\n        :type ResourceId: str\n        :param TrafficType: Type of the flow logs to be collected. Valid values: `ACCEPT`, `REJECT` and `ALL`.\n        :type TrafficType: str\n        :param CloudLogId: The storage ID of the flow log.\n        :type CloudLogId: str\n        :param FlowLogDescription: The description of the flow log instance\n        :type FlowLogDescription: str\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowLogResponse(AbstractModel):
    """CreateFlowLog response structure.

    """

    def __init__(self):
        """
        :param FlowLog: The information of the flow log created.\n        :type FlowLog: list of FlowLog\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The `ID` of the VPC to which the `HAVIP` belongs.\n        :type VpcId: str\n        :param SubnetId: The `ID` of the subnet to which the `HAVIP` belongs.\n        :type SubnetId: str\n        :param HaVipName: The name of the `HAVIP`.\n        :type HaVipName: str\n        :param Vip: The specified virtual IP address, which must be within the IP range of the `VPC` and not in use. It will be automatically assigned if not specified.\n        :type Vip: str\n        """
        self.VpcId = None
        self.SubnetId = None
        self.HaVipName = None
        self.Vip = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.HaVipName = params.get("HaVipName")
        self.Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHaVipResponse(AbstractModel):
    """CreateHaVip response structure.

    """

    def __init__(self):
        """
        :param HaVip: `HAVIP` object.\n        :type HaVip: :class:`tencentcloud.vpc.v20170312.models.HaVip`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.HaVip = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HaVip") is not None:
            self.HaVip = HaVip()
            self.HaVip._deserialize(params.get("HaVip"))
        self.RequestId = params.get("RequestId")


class CreateLocalGatewayRequest(AbstractModel):
    """CreateLocalGateway request structure.

    """

    def __init__(self):
        """
        :param LocalGatewayName: Local gateway name\n        :type LocalGatewayName: str\n        :param VpcId: VPC instance ID\n        :type VpcId: str\n        :param CdcId: CDC instance ID\n        :type CdcId: str\n        """
        self.LocalGatewayName = None
        self.VpcId = None
        self.CdcId = None


    def _deserialize(self, params):
        self.LocalGatewayName = params.get("LocalGatewayName")
        self.VpcId = params.get("VpcId")
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLocalGatewayResponse(AbstractModel):
    """CreateLocalGateway response structure.

    """

    def __init__(self):
        """
        :param LocalGateway: Local gateway information\n        :type LocalGateway: :class:`tencentcloud.vpc.v20170312.models.LocalGateway`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LocalGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LocalGateway") is not None:
            self.LocalGateway = LocalGateway()
            self.LocalGateway._deserialize(params.get("LocalGateway"))
        self.RequestId = params.get("RequestId")


class CreateNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """CreateNatGatewayDestinationIpPortTranslationNatRule request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.\n        :type NatGatewayId: str\n        :param DestinationIpPortTranslationNatRules: The port forwarding rules of the NAT gateway.\n        :type DestinationIpPortTranslationNatRules: list of DestinationIpPortTranslationNatRule\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """CreateNatGatewayDestinationIpPortTranslationNatRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNatGatewayRequest(AbstractModel):
    """CreateNatGateway request structure.

    """

    def __init__(self):
        """
        :param NatGatewayName: NAT gateway name\n        :type NatGatewayName: str\n        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.\n        :type VpcId: str\n        :param InternetMaxBandwidthOut: The maximum outbound bandwidth of the NAT gateway (unit: Mbps). Supported parameter values: `20, 50, 100, 200, 500, 1000, 2000, 5000`. Default: `100Mbps`.\n        :type InternetMaxBandwidthOut: int\n        :param MaxConcurrentConnection: The concurrent connection cap of the NAT gateway. Supported parameter values: `1000000, 3000000, 10000000`. The default value is `100000`.\n        :type MaxConcurrentConnection: int\n        :param AddressCount: The number of EIPs that needs to be applied for. The system will create N number of EIPs according to your requirements. Either AddressCount or PublicAddresses must be passed in.\n        :type AddressCount: int\n        :param PublicIpAddresses: The EIP array bound to the NAT gateway. Either AddressCount or PublicAddresses must be passed in.\n        :type PublicIpAddresses: list of str\n        :param Zone: The availability zone, such as `ap-guangzhou-1`.\n        :type Zone: str\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        :param SubnetId: Subnet of the NAT gateway\n        :type SubnetId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatGatewayResponse(AbstractModel):
    """CreateNatGateway response structure.

    """

    def __init__(self):
        """
        :param NatGatewaySet: NAT gateway object array.\n        :type NatGatewaySet: list of NatGateway\n        :param TotalCount: The number of NAT gateway objects meeting the conditions.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class CreateNatGatewaySourceIpTranslationNatRuleRequest(AbstractModel):
    """CreateNatGatewaySourceIpTranslationNatRule request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT Gateway, such as `nat-df45454`\n        :type NatGatewayId: str\n        :param SourceIpTranslationNatRules: The SNAT forwarding rule of the NAT Gateway\n        :type SourceIpTranslationNatRules: list of SourceIpTranslationNatRule\n        """
        self.NatGatewayId = None
        self.SourceIpTranslationNatRules = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("SourceIpTranslationNatRules") is not None:
            self.SourceIpTranslationNatRules = []
            for item in params.get("SourceIpTranslationNatRules"):
                obj = SourceIpTranslationNatRule()
                obj._deserialize(item)
                self.SourceIpTranslationNatRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatGatewaySourceIpTranslationNatRuleResponse(AbstractModel):
    """CreateNatGatewaySourceIpTranslationNatRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNetDetectRequest(AbstractModel):
    """CreateNetDetect request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of a `VPC` instance, such as `vpc-12345678`.\n        :type VpcId: str\n        :param SubnetId: The ID of a subnet instance, such as subnet-12345678.\n        :type SubnetId: str\n        :param NetDetectName: The name of a network detection instance. The maximum length is 60 characters.\n        :type NetDetectName: str\n        :param DetectDestinationIp: The array of detection destination IPv4 addresses, which contains at most two IP addresses.\n        :type DetectDestinationIp: list of str\n        :param NextHopType: Type of the next hop. Valid values:
`VPN`: VPN gateway;
`DIRECTCONNECT`: direct connect gateway;
`PEERCONNECTION`: peering connection;
`NAT`: NAT gateway;
`NORMAL_CVM`: normal CVM;
`CCN`: CCN gateway.\n        :type NextHopType: str\n        :param NextHopDestination: Next-hop destination gateway. Its value is determined by `NextHopType`.
If `NextHopType` is set to `VPN`, the parameter value is the VPN gateway ID, such as `vpngw-12345678`.
If `NextHopType` is set to `DIRECTCONNECT`, the parameter value is the direct connect gateway ID, such as `dcg-12345678`.
If `NextHopType` is set to `PEERCONNECTION`, the parameter value is the peering connection ID, such as `pcx-12345678`.
If `NextHopType` is set to `NAT`, the parameter value is the NAT gateway ID, such as `nat-12345678`.
If `NextHopType` is set to `NORMAL_CVM`, the parameter value is the IPv4 address of the CVM instance, such as `10.0.0.12`.
If `NextHopType` is set to `CCN`, the parameter value is the CCN ID, such as `ccn-12345678`.\n        :type NextHopDestination: str\n        :param NetDetectDescription: Network detection description.\n        :type NetDetectDescription: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetDetectResponse(AbstractModel):
    """CreateNetDetect response structure.

    """

    def __init__(self):
        """
        :param NetDetect: The network detection (NetDetect) object.\n        :type NetDetect: :class:`tencentcloud.vpc.v20170312.models.NetDetect`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of the DescribeVpcs API.\n        :type VpcId: str\n        :param NetworkAclName: Name of the network ACL. The maximum length is 60 bytes.\n        :type NetworkAclName: str\n        """
        self.VpcId = None
        self.NetworkAclName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkAclName = params.get("NetworkAclName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetworkAclResponse(AbstractModel):
    """CreateNetworkAcl response structure.

    """

    def __init__(self):
        """
        :param NetworkAcl: Network ACL instance\n        :type NetworkAcl: :class:`tencentcloud.vpc.v20170312.models.NetworkAcl`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.\n        :type VpcId: str\n        :param NetworkInterfaceName: The name of the ENI. The maximum length is 60 characters.\n        :type NetworkInterfaceName: str\n        :param SubnetId: The subnet instance ID of the ENI, such as `subnet-0ap8nwca`.\n        :type SubnetId: str\n        :param NetworkInterfaceDescription: ENI description can be named freely, but the maximum length is 60 characters.\n        :type NetworkInterfaceDescription: str\n        :param SecondaryPrivateIpAddressCount: The number of private IP addresses that is newly applied for. The total number of private IP addresses cannot exceed the quota.\n        :type SecondaryPrivateIpAddressCount: int\n        :param SecurityGroupIds: Specifies the security group to be bound with, such as ['sg-1dd51d'].\n        :type SecurityGroupIds: list of str\n        :param PrivateIpAddresses: The information of the specified private IPs. You can specify a maximum of 10 each time.\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetworkInterfaceResponse(AbstractModel):
    """CreateNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param NetworkInterface: ENI instance.\n        :type NetworkInterface: :class:`tencentcloud.vpc.v20170312.models.NetworkInterface`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The ID of the VPC instance to be operated on. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.\n        :type VpcId: str\n        :param RouteTableName: The route table name. The maximum length is 60 characters.\n        :type RouteTableName: str\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRouteTableResponse(AbstractModel):
    """CreateRouteTable response structure.

    """

    def __init__(self):
        """
        :param RouteTable: Route table object.\n        :type RouteTable: :class:`tencentcloud.vpc.v20170312.models.RouteTable`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param RouteTableId: Route table instance ID.\n        :type RouteTableId: str\n        :param Routes: Routing policy object.\n        :type Routes: list of Route\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoutesResponse(AbstractModel):
    """CreateRoutes response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of newly added instances.\n        :type TotalCount: int\n        :param RouteTableSet: Route table object.\n        :type RouteTableSet: list of RouteTable\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: Security group policy set.\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupPoliciesResponse(AbstractModel):
    """CreateSecurityGroupPolicies response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param GroupName: Security group can be named freely, but cannot exceed 60 characters.\n        :type GroupName: str\n        :param GroupDescription: The remarks for the security group. The maximum length is 100 characters.\n        :type GroupDescription: str\n        :param ProjectId: Project ID. The default is 0. You can query it on the project management page of the Qcloud console.\n        :type ProjectId: str\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupResponse(AbstractModel):
    """CreateSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param SecurityGroup: Security group object.\n        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param GroupName: Security group can be named freely, but cannot exceed 60 characters.\n        :type GroupName: str\n        :param GroupDescription: The remarks for the security group. The maximum length is 100 characters.\n        :type GroupDescription: str\n        :param ProjectId: The project id is 0 by default. You can query this in the project management page of the Qcloud console.\n        :type ProjectId: str\n        :param SecurityGroupPolicySet: Security group policy set.\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupWithPoliciesResponse(AbstractModel):
    """CreateSecurityGroupWithPolicies response structure.

    """

    def __init__(self):
        """
        :param SecurityGroup: Security group object.\n        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceTemplateGroupName: Group name of the protocol port template.\n        :type ServiceTemplateGroupName: str\n        :param ServiceTemplateIds: Instance ID of the protocol port template, such as `ppm-4dw6agho`.\n        :type ServiceTemplateIds: list of str\n        """
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIds = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIds = params.get("ServiceTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceTemplateGroupResponse(AbstractModel):
    """CreateServiceTemplateGroup response structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateGroup: Group object of the protocol port template.\n        :type ServiceTemplateGroup: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplateGroup`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceTemplateName: Template name of the protocol port\n        :type ServiceTemplateName: str\n        :param Services: It supports single port, multiple ports, consecutive ports and all ports. Supported protocols include TCP, UDP, ICMP, and GRE.\n        :type Services: list of str\n        """
        self.ServiceTemplateName = None
        self.Services = None


    def _deserialize(self, params):
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.Services = params.get("Services")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceTemplateResponse(AbstractModel):
    """CreateServiceTemplate response structure.

    """

    def __init__(self):
        """
        :param ServiceTemplate: Protocol port template object.\n        :type ServiceTemplate: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplate`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The ID of the VPC instance to be operated on. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.\n        :type VpcId: str\n        :param SubnetName: The subnet name. The maximum length is 60 bytes.\n        :type SubnetName: str\n        :param CidrBlock: The subnet IP address range. It must be within the VPC IP address range. Subnet IP address ranges cannot overlap with each other within the same VPC.\n        :type CidrBlock: str\n        :param Zone: The ID of the availability zone in which the subnet resides. You can set up disaster recovery across availability zones by choosing different availability zones for different subnets.\n        :type Zone: str\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        :param CdcId: CDC instance ID\n        :type CdcId: str\n        """
        self.VpcId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.Zone = None
        self.Tags = None
        self.CdcId = None


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
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet response structure.

    """

    def __init__(self):
        """
        :param Subnet: Subnet object.\n        :type Subnet: :class:`tencentcloud.vpc.v20170312.models.Subnet`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The `ID` of the `VPC` instance, such as `vpc-6v2ht8q5`.\n        :type VpcId: str\n        :param Subnets: The subnet object list.\n        :type Subnets: list of SubnetInput\n        :param Tags: Bound tags. Note that the collection of tags here is shared by all subnet objects in the list. You cannot specify tags for each subnet. Example: [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        :param CdcId: ID of the CDC instance to which the subnets will be created\n        :type CdcId: str\n        """
        self.VpcId = None
        self.Subnets = None
        self.Tags = None
        self.CdcId = None


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
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubnetsResponse(AbstractModel):
    """CreateSubnets response structure.

    """

    def __init__(self):
        """
        :param SubnetSet: The list of newly created subnets.\n        :type SubnetSet: list of Subnet\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class CreateVpcEndPointRequest(AbstractModel):
    """CreateVpcEndPoint request structure.

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID\n        :type VpcId: str\n        :param SubnetId: Subnet instance ID\n        :type SubnetId: str\n        :param EndPointName: Endpoint name\n        :type EndPointName: str\n        :param EndPointServiceId: Endpoint service ID\n        :type EndPointServiceId: str\n        :param EndPointVip: Endpoint VIP. You can apply for a specified IP.\n        :type EndPointVip: str\n        :param SecurityGroupId: Security group ID\n        :type SecurityGroupId: str\n        """
        self.VpcId = None
        self.SubnetId = None
        self.EndPointName = None
        self.EndPointServiceId = None
        self.EndPointVip = None
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.EndPointName = params.get("EndPointName")
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.EndPointVip = params.get("EndPointVip")
        self.SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcEndPointResponse(AbstractModel):
    """CreateVpcEndPoint response structure.

    """

    def __init__(self):
        """
        :param EndPoint: Endpoint details\n        :type EndPoint: :class:`tencentcloud.vpc.v20170312.models.EndPoint`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.EndPoint = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EndPoint") is not None:
            self.EndPoint = EndPoint()
            self.EndPoint._deserialize(params.get("EndPoint"))
        self.RequestId = params.get("RequestId")


class CreateVpcEndPointServiceRequest(AbstractModel):
    """CreateVpcEndPointService request structure.

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID\n        :type VpcId: str\n        :param EndPointServiceName: Endpoint service name\n        :type EndPointServiceName: str\n        :param AutoAcceptFlag: Whether to automatically accept\n        :type AutoAcceptFlag: bool\n        :param ServiceInstanceId: Real server ID, such as `lb-xxx`.\n        :type ServiceInstanceId: str\n        :param IsPassService: Whether it is of the type `PassService`. Valid values: true: yes; false: no. Default value: false\n        :type IsPassService: bool\n        """
        self.VpcId = None
        self.EndPointServiceName = None
        self.AutoAcceptFlag = None
        self.ServiceInstanceId = None
        self.IsPassService = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.EndPointServiceName = params.get("EndPointServiceName")
        self.AutoAcceptFlag = params.get("AutoAcceptFlag")
        self.ServiceInstanceId = params.get("ServiceInstanceId")
        self.IsPassService = params.get("IsPassService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcEndPointServiceResponse(AbstractModel):
    """CreateVpcEndPointService response structure.

    """

    def __init__(self):
        """
        :param EndPointService: Endpoint service details\n        :type EndPointService: :class:`tencentcloud.vpc.v20170312.models.EndPointService`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.EndPointService = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EndPointService") is not None:
            self.EndPointService = EndPointService()
            self.EndPointService._deserialize(params.get("EndPointService"))
        self.RequestId = params.get("RequestId")


class CreateVpcEndPointServiceWhiteListRequest(AbstractModel):
    """CreateVpcEndPointServiceWhiteList request structure.

    """

    def __init__(self):
        """
        :param UserUin: UIN\n        :type UserUin: str\n        :param EndPointServiceId: Endpoint service ID\n        :type EndPointServiceId: str\n        :param Description: Allowlist description\n        :type Description: str\n        """
        self.UserUin = None
        self.EndPointServiceId = None
        self.Description = None


    def _deserialize(self, params):
        self.UserUin = params.get("UserUin")
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcEndPointServiceWhiteListResponse(AbstractModel):
    """CreateVpcEndPointServiceWhiteList response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc request structure.

    """

    def __init__(self):
        """
        :param VpcName: The VPC name. The maximum length is 60 bytes.\n        :type VpcName: str\n        :param CidrBlock: VPC CIDR blocks, which must fall within the following three private network IP ranges: 10.0.0.0/16, 172.16.0.0/16 and 192.168.0.0/16.\n        :type CidrBlock: str\n        :param EnableMulticast: Whether multicast is enabled. `true`: Enabled. `false`: Not enabled.\n        :type EnableMulticast: str\n        :param DnsServers: DNS address. A maximum of 4 addresses is supported.\n        :type DnsServers: list of str\n        :param DomainName: Domain name of DHCP\n        :type DomainName: str\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcResponse(AbstractModel):
    """CreateVpc response structure.

    """

    def __init__(self):
        """
        :param Vpc: The VPC object.\n        :type Vpc: :class:`tencentcloud.vpc.v20170312.models.Vpc`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: VPC instance ID, which can be obtained from the `VpcId` field in the response of the [`DescribeVpcs`](https://intl.cloud.tencent.com/document/product/215/15778?from_cn_redirect=1) API.\n        :type VpcId: str\n        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param CustomerGatewayId: The ID of the customer gateway, such as `cgw-2wqq41m9`. You can query the customer gateway by using the `DescribeCustomerGateways` API.\n        :type CustomerGatewayId: str\n        :param VpnConnectionName: Gateway can be named freely, but the maximum length is 60 characters.\n        :type VpnConnectionName: str\n        :param PreShareKey: The pre-shared key.\n        :type PreShareKey: str\n        :param SecurityPolicyDatabases: The SPD policy group, for example: {"10.0.0.5/24":["172.123.10.5/16"]}. 10.0.0.5/24 is the VPC internal IP range, and 172.123.10.5/16 is the IDC IP range. The user specifies the IP range in the VPC that can communicate with the IP range in the IDC.\n        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase\n        :param IKEOptionsSpecification: Internet Key Exchange (IKE) configuration. IKE has a self-protection mechanism. The network security protocol is configured by the user.\n        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`\n        :param IPSECOptionsSpecification: IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud.\n        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        :param EnableHealthCheck: Whether the tunnel health check is supported.\n        :type EnableHealthCheck: bool\n        :param HealthCheckLocalIp: Local IP address for the health check\n        :type HealthCheckLocalIp: str\n        :param HealthCheckRemoteIp: Peer IP address for the health check\n        :type HealthCheckRemoteIp: str\n        """
        self.VpcId = None
        self.VpnGatewayId = None
        self.CustomerGatewayId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None
        self.Tags = None
        self.EnableHealthCheck = None
        self.HealthCheckLocalIp = None
        self.HealthCheckRemoteIp = None


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
        self.EnableHealthCheck = params.get("EnableHealthCheck")
        self.HealthCheckLocalIp = params.get("HealthCheckLocalIp")
        self.HealthCheckRemoteIp = params.get("HealthCheckRemoteIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpnConnectionResponse(AbstractModel):
    """CreateVpnConnection response structure.

    """

    def __init__(self):
        """
        :param VpnConnection: Tunnel instance object.\n        :type VpnConnection: :class:`tencentcloud.vpc.v20170312.models.VpnConnection`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: VPC instance ID, which can be obtained from the `VpcId` field in the response of the [`DescribeVpcs`](https://intl.cloud.tencent.com/document/product/215/15778?from_cn_redirect=1) API.\n        :type VpcId: str\n        :param VpnGatewayName: The VPN gateway name. The maximum length is 60 bytes.\n        :type VpnGatewayName: str\n        :param InternetMaxBandwidthOut: The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps\n        :type InternetMaxBandwidthOut: int\n        :param InstanceChargeType: The VPN gateway billing mode. PREPAID: prepaid means monthly subscription. POSTPAID_BY_HOUR: postpaid means pay-as-you-go. Default: POSTPAID_BY_HOUR. If prepaid mode is specified, the `InstanceChargePrepaid` parameter must be entered.\n        :type InstanceChargeType: str\n        :param InstanceChargePrepaid: Parameter settings for prepaid billing mode, also known as monthly subscription. This parameter can specify the purchase period and other attributes such as auto-renewal. This parameter is mandatory for prepaid instances.\n        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`\n        :param Zone: The availability zone, such as `ap-guangzhou-2`.\n        :type Zone: str\n        :param Type: VPN gateway type. Value: `CCN`, indicates CCN-type VPN gateway\n        :type Type: str\n        :param Tags: Bound tags, such as [{"Key": "city", "Value": "shanghai"}].\n        :type Tags: list of Tag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpnGatewayResponse(AbstractModel):
    """CreateVpnGateway response structure.

    """

    def __init__(self):
        """
        :param VpnGateway: VPN gateway object.\n        :type VpnGateway: :class:`tencentcloud.vpc.v20170312.models.VpnGateway`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.VpnGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpnGateway") is not None:
            self.VpnGateway = VpnGateway()
            self.VpnGateway._deserialize(params.get("VpnGateway"))
        self.RequestId = params.get("RequestId")


class CreateVpnGatewayRoutesRequest(AbstractModel):
    """CreateVpnGatewayRoutes request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN gateway ID\n        :type VpnGatewayId: str\n        :param Routes: Destination route list of a VPN gateway\n        :type Routes: list of VpnGatewayRoute\n        """
        self.VpnGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpnGatewayRoute()
                obj._deserialize(item)
                self.Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpnGatewayRoutesResponse(AbstractModel):
    """CreateVpnGatewayRoutes response structure.

    """

    def __init__(self):
        """
        :param Routes: Destination routes of a VPN gateway\n        :type Routes: list of VpnGatewayRoute\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Routes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpnGatewayRoute()
                obj._deserialize(item)
                self.Routes.append(obj)
        self.RequestId = params.get("RequestId")


class CrossBorderCompliance(AbstractModel):
    """Compliance review request

    """

    def __init__(self):
        """
        :param ServiceProvider: Service provider. Valid values: `UNICOM`.\n        :type ServiceProvider: str\n        :param ComplianceId: ID of compliance review request.\n        :type ComplianceId: int\n        :param Company: Full company name.\n        :type Company: str\n        :param UniformSocialCreditCode: Unified Social Credit Code.\n        :type UniformSocialCreditCode: str\n        :param LegalPerson: Legal person.\n        :type LegalPerson: str\n        :param IssuingAuthority: Issuing authority.\n        :type IssuingAuthority: str\n        :param BusinessLicense: Business license.\n        :type BusinessLicense: str\n        :param BusinessAddress: Business address.\n        :type BusinessAddress: str\n        :param PostCode: Zip code.\n        :type PostCode: int\n        :param Manager: Operator.\n        :type Manager: str\n        :param ManagerId: Operator ID card number.\n        :type ManagerId: str\n        :param ManagerIdCard: Operator ID card.\n        :type ManagerIdCard: str\n        :param ManagerAddress: Operator address.\n        :type ManagerAddress: str\n        :param ManagerTelephone: Operator phone number.\n        :type ManagerTelephone: str\n        :param Email: Email.\n        :type Email: str\n        :param ServiceHandlingForm: Service handling form.\n        :type ServiceHandlingForm: str\n        :param AuthorizationLetter: Authorization letter.\n        :type AuthorizationLetter: str\n        :param SafetyCommitment: Information security commitment.\n        :type SafetyCommitment: str\n        :param ServiceStartDate: Service start date.\n        :type ServiceStartDate: str\n        :param ServiceEndDate: Service end date.\n        :type ServiceEndDate: str\n        :param State: Status. Valid values: `PENDING`, `APPROVED`, and `DENY`.\n        :type State: str\n        :param CreatedTime: Creation time of the review form.\n        :type CreatedTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomerGateway(AbstractModel):
    """Customer Gateway

    """

    def __init__(self):
        """
        :param CustomerGatewayId: The unique ID of the customer gateway\n        :type CustomerGatewayId: str\n        :param CustomerGatewayName: Gateway Name\n        :type CustomerGatewayName: str\n        :param IpAddress: Public network address\n        :type IpAddress: str\n        :param CreatedTime: The creation time.\n        :type CreatedTime: str\n        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None
        self.IpAddress = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomerGatewayVendor(AbstractModel):
    """Customer gateway vendor information object.

    """

    def __init__(self):
        """
        :param Platform: Platform.\n        :type Platform: str\n        :param SoftwareVersion: Software version.\n        :type SoftwareVersion: str\n        :param VendorName: Vendor name.\n        :type VendorName: str\n        """
        self.Platform = None
        self.SoftwareVersion = None
        self.VendorName = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.SoftwareVersion = params.get("SoftwareVersion")
        self.VendorName = params.get("VendorName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CvmInstance(AbstractModel):
    """A CVM instance.

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID.\n        :type VpcId: str\n        :param SubnetId: Subnet instance ID.\n        :type SubnetId: str\n        :param InstanceId: CVM instance ID.\n        :type InstanceId: str\n        :param InstanceName: CVM Name\n        :type InstanceName: str\n        :param InstanceState: CVM status.\n        :type InstanceState: str\n        :param CPU: Number of CPU cores in an instance (in core).\n        :type CPU: int\n        :param Memory: Instance’s memory capacity. Unit: GB.\n        :type Memory: int\n        :param CreatedTime: The creation time.\n        :type CreatedTime: str\n        :param InstanceType: Instance type.\n        :type InstanceType: str\n        :param EniLimit: Instance ENI quota (including primary ENIs).\n        :type EniLimit: int\n        :param EniIpLimit: Private IP quoata for instance ENIs (including primary ENIs).\n        :type EniIpLimit: int\n        :param InstanceEniCount: The number of ENIs (including primary ENIs) bound to a instance.\n        :type InstanceEniCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultVpcSubnet(AbstractModel):
    """Default VPC and subnet

    """

    def __init__(self):
        """
        :param VpcId: Default VpcId\n        :type VpcId: str\n        :param SubnetId: Default SubnetId\n        :type SubnetId: str\n        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAddressTemplateGroupRequest(AbstractModel):
    """DeleteAddressTemplateGroup request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateGroupId: The IP address template group instance ID, such as `ipmg-90cex8mq`.\n        :type AddressTemplateGroupId: str\n        """
        self.AddressTemplateGroupId = None


    def _deserialize(self, params):
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAddressTemplateGroupResponse(AbstractModel):
    """DeleteAddressTemplateGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAddressTemplateRequest(AbstractModel):
    """DeleteAddressTemplate request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateId: The IP address template instance ID, such as `ipm-09o5m8kc`.\n        :type AddressTemplateId: str\n        """
        self.AddressTemplateId = None


    def _deserialize(self, params):
        self.AddressTemplateId = params.get("AddressTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAddressTemplateResponse(AbstractModel):
    """DeleteAddressTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAssistantCidrRequest(AbstractModel):
    """DeleteAssistantCidr request structure.

    """

    def __init__(self):
        """
        :param VpcId: `VPC` instance `ID`, e.g. `vpc-6v2ht8q5`.\n        :type VpcId: str\n        :param CidrBlocks: CIDR set, e.g. ["10.0.0.0/16", "172.16.0.0/16"]\n        :type CidrBlocks: list of str\n        """
        self.VpcId = None
        self.CidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlocks = params.get("CidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAssistantCidrResponse(AbstractModel):
    """DeleteAssistantCidr response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBandwidthPackageRequest(AbstractModel):
    """DeleteBandwidthPackage request structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageId: The unique ID of the bandwidth package to be deleted.\n        :type BandwidthPackageId: str\n        """
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBandwidthPackageResponse(AbstractModel):
    """DeleteBandwidthPackage response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCcnRequest(AbstractModel):
    """DeleteCcn request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCcnResponse(AbstractModel):
    """DeleteCcn response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCustomerGatewayRequest(AbstractModel):
    """DeleteCustomerGateway request structure.

    """

    def __init__(self):
        """
        :param CustomerGatewayId: The ID of the customer gateway, such as `cgw-2wqq41m9`. You can query the customer gateway by using the `DescribeCustomerGateways` API.\n        :type CustomerGatewayId: str\n        """
        self.CustomerGatewayId = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomerGatewayResponse(AbstractModel):
    """DeleteCustomerGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """DeleteDirectConnectGatewayCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`\n        :type DirectConnectGatewayId: str\n        :param RouteIds: The route ID, such as `ccnr-f49l6u0z`.\n        :type RouteIds: list of str\n        """
        self.DirectConnectGatewayId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """DeleteDirectConnectGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectGatewayRequest(AbstractModel):
    """DeleteDirectConnectGateway request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: The unique `ID` of the direct connect gateway, such as `dcg-9o233uri`.\n        :type DirectConnectGatewayId: str\n        """
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectGatewayResponse(AbstractModel):
    """DeleteDirectConnectGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFlowLogRequest(AbstractModel):
    """DeleteFlowLog request structure.

    """

    def __init__(self):
        """
        :param VpcId: ID of the VPC instance\n        :type VpcId: str\n        :param FlowLogId: The unique ID of the flow log.\n        :type FlowLogId: str\n        """
        self.VpcId = None
        self.FlowLogId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFlowLogResponse(AbstractModel):
    """DeleteFlowLog response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteHaVipRequest(AbstractModel):
    """DeleteHaVip request structure.

    """

    def __init__(self):
        """
        :param HaVipId: The unique `ID` of the `HAVIP`, such as `havip-9o233uri`.\n        :type HaVipId: str\n        """
        self.HaVipId = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHaVipResponse(AbstractModel):
    """DeleteHaVip response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLocalGatewayRequest(AbstractModel):
    """DeleteLocalGateway request structure.

    """

    def __init__(self):
        """
        :param LocalGatewayId: Local gateway instance ID\n        :type LocalGatewayId: str\n        :param CdcId: CDC instance ID\n        :type CdcId: str\n        :param VpcId: VPC instance ID\n        :type VpcId: str\n        """
        self.LocalGatewayId = None
        self.CdcId = None
        self.VpcId = None


    def _deserialize(self, params):
        self.LocalGatewayId = params.get("LocalGatewayId")
        self.CdcId = params.get("CdcId")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLocalGatewayResponse(AbstractModel):
    """DeleteLocalGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """DeleteNatGatewayDestinationIpPortTranslationNatRule request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.\n        :type NatGatewayId: str\n        :param DestinationIpPortTranslationNatRules: The port forwarding rules of the NAT gateway.\n        :type DestinationIpPortTranslationNatRules: list of DestinationIpPortTranslationNatRule\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """DeleteNatGatewayDestinationIpPortTranslationNatRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNatGatewayRequest(AbstractModel):
    """DeleteNatGateway request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.\n        :type NatGatewayId: str\n        """
        self.NatGatewayId = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNatGatewayResponse(AbstractModel):
    """DeleteNatGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNatGatewaySourceIpTranslationNatRuleRequest(AbstractModel):
    """DeleteNatGatewaySourceIpTranslationNatRule request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT Gateway, such as `nat-df45454`\n        :type NatGatewayId: str\n        :param NatGatewaySnatIds: The list of SNAT rule IDs of a NAT Gateway, such as `snat-df43254`\n        :type NatGatewaySnatIds: list of str\n        """
        self.NatGatewayId = None
        self.NatGatewaySnatIds = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.NatGatewaySnatIds = params.get("NatGatewaySnatIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNatGatewaySourceIpTranslationNatRuleResponse(AbstractModel):
    """DeleteNatGatewaySourceIpTranslationNatRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetDetectRequest(AbstractModel):
    """DeleteNetDetect request structure.

    """

    def __init__(self):
        """
        :param NetDetectId: The `ID` of a network detection instance, such as `netd-12345678`.\n        :type NetDetectId: str\n        """
        self.NetDetectId = None


    def _deserialize(self, params):
        self.NetDetectId = params.get("NetDetectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNetDetectResponse(AbstractModel):
    """DeleteNetDetect response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetworkAclRequest(AbstractModel):
    """DeleteNetworkAcl request structure.

    """

    def __init__(self):
        """
        :param NetworkAclId: Network ACL instance ID. Example: acl-12345678.\n        :type NetworkAclId: str\n        """
        self.NetworkAclId = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNetworkAclResponse(AbstractModel):
    """DeleteNetworkAcl response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetworkInterfaceRequest(AbstractModel):
    """DeleteNetworkInterface request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.\n        :type NetworkInterfaceId: str\n        """
        self.NetworkInterfaceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNetworkInterfaceResponse(AbstractModel):
    """DeleteNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRouteTableRequest(AbstractModel):
    """DeleteRouteTable request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.\n        :type RouteTableId: str\n        """
        self.RouteTableId = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteTableResponse(AbstractModel):
    """DeleteRouteTable response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoutesRequest(AbstractModel):
    """DeleteRoutes request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: Route table instance ID.\n        :type RouteTableId: str\n        :param Routes: Routing policy object. Only the `RouteId` field is required when deleting a routing policy.\n        :type Routes: list of Route\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoutesResponse(AbstractModel):
    """DeleteRoutes response structure.

    """

    def __init__(self):
        """
        :param RouteSet: Details of the routing policy that has been deleted.\n        :type RouteSet: list of Route\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = Route()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupPoliciesRequest(AbstractModel):
    """DeleteSecurityGroupPolicies request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: The policy set of the security group. One request can only delete one or more policies in one direction. Both PolicyIndex-matching deletion and security group policy-matching deletion methods are supported. Each request can use only one matching method.\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupPoliciesResponse(AbstractModel):
    """DeleteSecurityGroupPolicies response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.\n        :type SecurityGroupId: str\n        """
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupResponse(AbstractModel):
    """DeleteSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceTemplateGroupRequest(AbstractModel):
    """DeleteServiceTemplateGroup request structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: The protocol port template group instance ID, such as `ppmg-n17uxvve`.\n        :type ServiceTemplateGroupId: str\n        """
        self.ServiceTemplateGroupId = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceTemplateGroupResponse(AbstractModel):
    """DeleteServiceTemplateGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceTemplateRequest(AbstractModel):
    """DeleteServiceTemplate request structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateId: Protocol port template instance ID, such as `ppm-e6dy460g`.\n        :type ServiceTemplateId: str\n        """
        self.ServiceTemplateId = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceTemplateResponse(AbstractModel):
    """DeleteServiceTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet request structure.

    """

    def __init__(self):
        """
        :param SubnetId: The ID of the subnet instance. You can obtain the parameter value from the SubnetId field in the returned result of DescribeSubnets API.\n        :type SubnetId: str\n        """
        self.SubnetId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubnetResponse(AbstractModel):
    """DeleteSubnet response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpcEndPointRequest(AbstractModel):
    """DeleteVpcEndPoint request structure.

    """

    def __init__(self):
        """
        :param EndPointId: Endpoint ID\n        :type EndPointId: str\n        """
        self.EndPointId = None


    def _deserialize(self, params):
        self.EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcEndPointResponse(AbstractModel):
    """DeleteVpcEndPoint response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpcEndPointServiceRequest(AbstractModel):
    """DeleteVpcEndPointService request structure.

    """

    def __init__(self):
        """
        :param EndPointServiceId: Endpoint ID\n        :type EndPointServiceId: str\n        """
        self.EndPointServiceId = None


    def _deserialize(self, params):
        self.EndPointServiceId = params.get("EndPointServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcEndPointServiceResponse(AbstractModel):
    """DeleteVpcEndPointService response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpcEndPointServiceWhiteListRequest(AbstractModel):
    """DeleteVpcEndPointServiceWhiteList request structure.

    """

    def __init__(self):
        """
        :param UserUin: Array of user UINs\n        :type UserUin: list of str\n        :param EndPointServiceId: Endpoint service ID\n        :type EndPointServiceId: str\n        """
        self.UserUin = None
        self.EndPointServiceId = None


    def _deserialize(self, params):
        self.UserUin = params.get("UserUin")
        self.EndPointServiceId = params.get("EndPointServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcEndPointServiceWhiteListResponse(AbstractModel):
    """DeleteVpcEndPointServiceWhiteList response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpcRequest(AbstractModel):
    """DeleteVpc request structure.

    """

    def __init__(self):
        """
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.\n        :type VpcId: str\n        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcResponse(AbstractModel):
    """DeleteVpc response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpnConnectionRequest(AbstractModel):
    """DeleteVpnConnection request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param VpnConnectionId: The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`.\n        :type VpnConnectionId: str\n        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpnConnectionResponse(AbstractModel):
    """DeleteVpnConnection response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpnGatewayRequest(AbstractModel):
    """DeleteVpnGateway request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        """
        self.VpnGatewayId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpnGatewayResponse(AbstractModel):
    """DeleteVpnGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpnGatewayRoutesRequest(AbstractModel):
    """DeleteVpnGatewayRoutes request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: Instance ID of the VPN gateway\n        :type VpnGatewayId: str\n        :param RouteIds: List of route IDs\n        :type RouteIds: list of str\n        """
        self.VpnGatewayId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpnGatewayRoutesResponse(AbstractModel):
    """DeleteVpnGatewayRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param AccountAttributeSet: User account attribute object\n        :type AccountAttributeSet: list of AccountAttribute\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param QuotaSet: The quota information of EIPs in an account.\n        :type QuotaSet: list of Quota\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
<li>address-template-group-id - String - (Filter condition) IP address template group instance ID, such as `ipmg-mdunqeb6`.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. The default value is 0.\n        :type Offset: str\n        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.\n        :type Limit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressTemplateGroupsResponse(AbstractModel):
    """DescribeAddressTemplateGroups response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.\n        :type TotalCount: int\n        :param AddressTemplateGroupSet: IP address template.\n        :type AddressTemplateGroupSet: list of AddressTemplateGroup\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
<li>address-template-id - String - (Filter condition) IP address template instance ID, such as `ipm-mdunqeb6`.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. The default value is 0.\n        :type Offset: str\n        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.\n        :type Limit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressTemplatesResponse(AbstractModel):
    """DescribeAddressTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.\n        :type TotalCount: int\n        :param AddressTemplateSet: IP address template.\n        :type AddressTemplateSet: list of AddressTemplate\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param AddressIds: The list of unique IDs of EIPs in the format of `eip-11112222`. `AddressIds` and `Filters.address-id` cannot be specified at the same time.\n        :type AddressIds: list of str\n        :param Filters: Each request can have up to 10 `Filters` and 5 `Filter.Values`. `AddressIds` and `Filters` cannot be specified at the same time. The specific filter conditions are as follows:
<li> address-id - String - Required: No - (Filter condition) Filter by the unique EIP ID, such as `eip-11112222`.</li>
<li> address-name - String - Required: No - (Filter condition) Filter by the EIP name. Fuzzy filtering is not supported.</li>
<li> address-ip - String - Required: No - (Filter condition) Filter by EIP.</li>
<li> address-status - String - Required: No - (Filter condition) Filter by the EIP state. Valid values: `CREATING`, `BINDING`, `BIND`, `UNBINDING`, `UNBIND`, `OFFLINING`, and `BIND_ENI`.</li>
<li> instance-id - String - Required: No - (Filter condition) Filter by the ID of the instance bound to the EIP, such as `ins-11112222`.</li>
<li> private-ip-address - String - Required: No - (Filter condition) Filter by the private IP address bound to the EIP.</li>
<li> network-interface-id - String - Required: No - (Filter condition) Filter by ID of the ENI bound to the EIP, such as `eni-11112222`.</li>
<li> is-arrears - String - Required: No - (Filter condition) Whether the EIP is overdue (TRUE: the EIP is overdue | FALSE: the billing status of the EIP is normal).</li>
<li> address-type - String - Required: No - (Filter condition) Filter by the IP type. Valid values: `EIP`, `AnycastEIP`, and `HighQualityEIP`.</li>
<li> address-isp - String - Required: No - (Filter condition) Filter by the ISP type. Valid values: `BGP`, `CMCC`, `CUCC`, and `CTCC`.</li>
<li> dedicated-cluster-id - String - Required: No - (Filter condition) Filter by the unique CDC ID, such as `cluster-11112222`.</li>
<li> tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>
<li> tag-value - String - Required: No - (Filter condition) Filter by tag value.</li>
<li> tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. Use a specific tag key to replace `tag-key`.</li>\n        :type Filters: list of Filter\n        :param Offset: The Offset. The default value is 0. For more information on `Offset`, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/product/11646).\n        :type Offset: int\n        :param Limit: Number of returned results. The default value is 20. The maximum is 100. For more information on `Limit`, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/product/11646).\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressesResponse(AbstractModel):
    """DescribeAddresses response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of EIPs meeting the condition.\n        :type TotalCount: int\n        :param AddressSet: List of EIPs details.\n        :type AddressSet: list of Address\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcIds: The ID of a VPC instance set, such as `vpc-6v2ht8q5`.\n        :type VpcIds: list of str\n        :param Filters: Filter condition. `VpcIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssistantCidrResponse(AbstractModel):
    """DescribeAssistantCidr response structure.

    """

    def __init__(self):
        """
        :param AssistantCidrSet: A set of eligible secondary CIDR blocks
Note: This field may return null, indicating that no valid value was found.\n        :type AssistantCidrSet: list of AssistantCidr\n        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param BandwidthPackageId: Unique ID of the pay-as-you-go bandwidth package.\n        :type BandwidthPackageId: str\n        """
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBandwidthPackageBillUsageResponse(AbstractModel):
    """DescribeBandwidthPackageBillUsage response structure.

    """

    def __init__(self):
        """
        :param BandwidthPackageBillBandwidthSet: Current billable usage.\n        :type BandwidthPackageBillBandwidthSet: list of BandwidthPackageBillBandwidth\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param QuotaSet: The quota of the bandwidth package.\n        :type QuotaSet: list of Quota\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param BandwidthPackageId: Unique ID of the bandwidth package in the form of `bwp-11112222`.\n        :type BandwidthPackageId: str\n        :param Filters: Each request can have up to 10 `Filters` and 5 `Filter.Values`. `AddressIds` and `Filters` cannot be specified at the same time. The specific filter conditions are as follows:
<li>resource-id - String - Required: no -  (Filter condition) Filters by the unique ID of resources in a bandwidth package, such as `eip-11112222`.</li>
<li>resource-type - String - Required: no - (Filter condition) Filters by the type of resources in a bandwidth package. It now supports only EIP (`Address`) and load balancer (`LoadBalance`).</li>\n        :type Filters: list of Filter\n        :param Offset: The offset. Default value: 0. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/11646?from_cn_redirect=1).\n        :type Offset: int\n        :param Limit: The number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/11646?from_cn_redirect=1).\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBandwidthPackageResourcesResponse(AbstractModel):
    """DescribeBandwidthPackageResources response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of eligible resources in the bandwidth package.\n        :type TotalCount: int\n        :param ResourceSet: The list of resources in the bandwidth package.\n        :type ResourceSet: list of Resource\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param BandwidthPackageIds: The unique ID list of bandwidth packages.\n        :type BandwidthPackageIds: list of str\n        :param Filters: Each request can have up to 10 `Filters`. `BandwidthPackageIds` and `Filters` cannot be specified at the same time. The specific filter conditions are as follows:
<li> bandwidth-package_id - String - Required: No - (Filter condition) Filter by the unique ID of the bandwidth package.</li>
<li> bandwidth-package-name - String - Required: No - (Filter condition) Filter by the bandwidth package name. Fuzzy filtering is not supported.</li>
<li> network-type - String - Required: No - (Filter condition) Filter by the bandwidth package type. Valid values: `HIGH_QUALITY_BGP`, `BGP`, `SINGLEISP`, and `ANYCAST`.</li>
<li> charge-type - String - Required: No - (Filter condition) Filter by the bandwidth package billing mode. Valid values: `TOP5_POSTPAID_BY_MONTH` and `PERCENT95_POSTPAID_BY_MONTH`.</li>
<li> resource.resource-type - String - Required: No - (Filter condition) Filter by the bandwidth package resource type. Valid values: `Address` and `LoadBalance`.</li>
<li> resource.resource-id - String - Required: No - (Filter condition) Filter by the bandwidth package resource ID, such as `eip-xxxx` and `lb-xxxx`.</li>
<li> resource.address-ip - String - Required: No - (Filter condition) Filter by the bandwidth package resource IP.</li>
<li> tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>
<li> tag-value - String - Required: No - (Filter condition) Filter by tag value.</li>
<li> tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. Use a specific tag key to replace `tag-key`.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset of the query results\n        :type Offset: int\n        :param Limit: Max number of the bandwidth packages to be returned.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBandwidthPackagesResponse(AbstractModel):
    """DescribeBandwidthPackages response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of eligible bandwidth packages.\n        :type TotalCount: int\n        :param BandwidthPackageSet: Detail information of the bandwidth package.\n        :type BandwidthPackageSet: list of BandwidthPackage\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Offset: Offset\n        :type Offset: int\n        :param Limit: The returned quantity\n        :type Limit: int\n        :param Filters: Filter conditions:
<li>ccn-id - String - (Filter condition) The CCN instance ID.</li>
<li>instance-type - String - (Filter condition) The associated instance type.</li>
<li>instance-region - String - (Filter condition) The associated instance region.</li>
<li>instance-type - String - (Filter condition) The instance ID of the associated instance.</li>\n        :type Filters: list of Filter\n        :param CcnId: The ID of the CCN instance\n        :type CcnId: str\n        :param OrderField: The order field supports `CcnId`, `InstanceType`, `InstanceId`, `InstanceName`, `InstanceRegion`, `AttachedTime`, and `State`.\n        :type OrderField: str\n        :param OrderDirection: Order methods. Ascending: `ASC`, Descending: `DESC`.\n        :type OrderDirection: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcnAttachedInstancesResponse(AbstractModel):
    """DescribeCcnAttachedInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.\n        :type TotalCount: int\n        :param InstanceSet: The list of associated instances.\n        :type InstanceSet: list of CcnAttachedInstance\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeCcnRegionBandwidthLimitsRequest(AbstractModel):
    """DescribeCcnRegionBandwidthLimits request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID in the format of `ccn-f49l6u0z`.\n        :type CcnId: str\n        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcnRegionBandwidthLimitsResponse(AbstractModel):
    """DescribeCcnRegionBandwidthLimits response structure.

    """

    def __init__(self):
        """
        :param CcnRegionBandwidthLimitSet: The outbound bandwidth caps of all regions connected with the specified CCN instance\n        :type CcnRegionBandwidthLimitSet: list of CcnRegionBandwidthLimit\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CcnRegionBandwidthLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CcnRegionBandwidthLimitSet") is not None:
            self.CcnRegionBandwidthLimitSet = []
            for item in params.get("CcnRegionBandwidthLimitSet"):
                obj = CcnRegionBandwidthLimit()
                obj._deserialize(item)
                self.CcnRegionBandwidthLimitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnRoutesRequest(AbstractModel):
    """DescribeCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-gree226l`.\n        :type CcnId: str\n        :param RouteIds: The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`.\n        :type RouteIds: list of str\n        :param Filters: Filter condition. `RouteIds` and `Filters` cannot be specified at the same time.
<li>route-id - String - (Filter condition) Routing policy ID.</li>
<li>cidr-block - String - (Filter condition) Destination port.</li>
<li>instance-type - String - (Filter condition) The next hop type.</li>
<li>instance-region - String - (Filter condition) The next hop region.</li>
<li>instance-type - String - (Filter condition) The instance ID of the next hop.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: The returned quantity\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcnRoutesResponse(AbstractModel):
    """DescribeCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.\n        :type TotalCount: int\n        :param RouteSet: The CCN routing policy object.\n        :type RouteSet: list of CcnRoute\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param CcnIds: The CCN instance ID, such as `ccn-f49l6u0z`. Each request can have a maximum of 100 instances. `CcnIds` and `Filters` cannot be specified at the same time\n        :type CcnIds: list of str\n        :param Filters: Filter conditions. `CcnIds` and `Filters` cannot be specified at the same time.
<li>ccn-id - String - (Filter condition) The unique ID of the CCN, such as `vpc-f49l6u0z`.</li>
<li>ccn-name - String - (Filter condition) The CCN name.</li>
<li>ccn-description - String - (Filter condition) CCN description.</li>
<li>state - String - (Filter condition) The instance status. 'ISOLATED': Isolated (the account is in arrears and the service is suspended.) 'AVAILABLE': Running.</li>
<li>tag-key - String - Required: no - (Filter condition) Filters by tag key.</li>
<li>`tag:tag-key` - String - Required: no - (Filter condition) Filters by tag key pair. For this parameter, `tag-key` will be replaced with a specific tag key. For more information, see this example: **Querying the list of CCNs bound to tags**.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: The returned quantity\n        :type Limit: int\n        :param OrderField: Order fields support `CcnId`, `CcnName`, `CreateTime`, `State`, and `QosLevel`\n        :type OrderField: str\n        :param OrderDirection: Order methods. Ascending: `ASC`, Descending: `DESC`.\n        :type OrderDirection: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcnsResponse(AbstractModel):
    """DescribeCcns response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.\n        :type TotalCount: int\n        :param CcnSet: CCN object.\n        :type CcnSet: list of CCN\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
<li>vm-ip - String - (Filter condition) The IP address of the CVM on the basic network.</li>\n        :type Filters: list of FilterObject\n        :param Offset: Offset\n        :type Offset: str\n        :param Limit: The returned quantity\n        :type Limit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicLinkInstancesResponse(AbstractModel):
    """DescribeClassicLinkInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.\n        :type TotalCount: int\n        :param ClassicLinkInstanceSet: Classiclink instance.\n        :type ClassicLinkInstanceSet: list of ClassicLinkInstance\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param ServiceProvider: (Exact match) Service provider. Valid values: `UNICOM`.\n        :type ServiceProvider: str\n        :param ComplianceId: (Exact match) ID of compliance review request.\n        :type ComplianceId: int\n        :param Company: (Fuzzy match) Company name.\n        :type Company: str\n        :param UniformSocialCreditCode: (Fuzzy match) Unified Social Credit Code.\n        :type UniformSocialCreditCode: str\n        :param LegalPerson: (Fuzzy match) Legal person.\n        :type LegalPerson: str\n        :param IssuingAuthority: (Fuzzy match) Issuing authority.\n        :type IssuingAuthority: str\n        :param BusinessAddress: (Fuzzy match) Business address.\n        :type BusinessAddress: str\n        :param PostCode: (Exact match) Zip code.\n        :type PostCode: int\n        :param Manager: (Fuzzy match) Operator.\n        :type Manager: str\n        :param ManagerId: (Exact match) Operator ID card number.\n        :type ManagerId: str\n        :param ManagerAddress: (Fuzzy match) Operator address.\n        :type ManagerAddress: str\n        :param ManagerTelephone: (Exact match) Operator phone number.\n        :type ManagerTelephone: str\n        :param Email: (Exact match) Email.\n        :type Email: str\n        :param ServiceStartDate: (Exact match) Service start date, such as `2020-07-28`.\n        :type ServiceStartDate: str\n        :param ServiceEndDate: (Exact match) Service end date, such as `2020-07-28`.\n        :type ServiceEndDate: str\n        :param State: (Exact match) Status. Valid values: `PENDING`, `APPROVED`, and `DENY`.\n        :type State: str\n        :param Offset: The offset value\n        :type Offset: int\n        :param Limit: Quantity of returned items\n        :type Limit: int\n        """
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
        self.Offset = None
        self.Limit = None


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
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCrossBorderComplianceResponse(AbstractModel):
    """DescribeCrossBorderCompliance response structure.

    """

    def __init__(self):
        """
        :param CrossBorderComplianceSet: List of compliance review requests.\n        :type CrossBorderComplianceSet: list of CrossBorderCompliance\n        :param TotalCount: Total number of compliance review requests.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param CustomerGatewayVendorSet: Customer gateway vendor information object.\n        :type CustomerGatewayVendorSet: list of CustomerGatewayVendor\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param CustomerGatewayIds: Customer gateway ID, such as `cgw-2wqq41m9`. Each request can have a maximum of 100 instances. `CustomerGatewayIds` and `Filters` cannot be specified at the same time.\n        :type CustomerGatewayIds: list of str\n        :param Filters: The filter condition. For details, see the Instance Filter Conditions Table. The upper limit for `Filters` in each request is 10 and 5 for `Filter.Values`. `CustomerGatewayIds` and `Filters` cannot be specified at the same time.
<li>customer-gateway-id - String - (Filter condition) The unique ID of the user gateway, such as `cgw-mgp33pll`.</li>
<li>customer-gateway-name - String - (Filter condition) The name of the user gateway, such as `test-cgw`.</li>
<li>ip-address - String - (Filter condition) The public IP address, such as `58.211.1.12`.</li>\n        :type Filters: list of Filter\n        :param Offset: The Offset. The default value is 0. For more information about Offset, see the relevant section in the API Introduction.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerGatewaysResponse(AbstractModel):
    """DescribeCustomerGateways response structure.

    """

    def __init__(self):
        """
        :param CustomerGatewaySet: Customer gateway object list\n        :type CustomerGatewaySet: list of CustomerGateway\n        :param TotalCount: Number of eligible instances\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param DirectConnectGatewayId: The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`.\n        :type DirectConnectGatewayId: str\n        :param CcnRouteType: The route learning type of the CCN. Available values:
<li>`BGP` - Automatic learning.</li>
<li>`STATIC` - Static means user-configured. This is the default value.</li>\n        :type CcnRouteType: str\n        :param Offset: Offset.\n        :type Offset: int\n        :param Limit: The returned quantity.\n        :type Limit: int\n        """
        self.DirectConnectGatewayId = None
        self.CcnRouteType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.CcnRouteType = params.get("CcnRouteType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """DescribeDirectConnectGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.\n        :type TotalCount: int\n        :param RouteSet: The CCN route (IDC IP range) list.\n        :type RouteSet: list of DirectConnectGatewayCcnRoute\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param DirectConnectGatewayIds: The unique ID of the direct connect gateway, such as `dcg-9o233uri`.\n        :type DirectConnectGatewayIds: list of str\n        :param Filters: Filter condition. `DirectConnectGatewayIds` and `Filters` cannot be specified at the same time.
<li>direct-connect-gateway-id - String - The unique ID of the direct connect gateway, such as `dcg-9o233uri`.</li>
<li>direct-connect-gateway-name - String - The name of the direct connect gateway. The default is fuzzy query.</li>
<li>direct-connect-gateway-ip - String - The IP of the direct connect gateway.</li>
<li>gateway-type - String - The gateway type. Valid values: `NORMAL` (Standard type), `NAT` (NAT type).</li>
<li>network-type- String - The network type. Valid values: `VPC` (VPC type), `CCN` (CCN type).</li>
<li>ccn-id - String - The ID of the CCN where the direct connect gateway resides.</li>
<li>vpc-id - String - The ID of the VPC where the direct connect gateway resides.</li>\n        :type Filters: list of Filter\n        :param Offset: The offset.\n        :type Offset: int\n        :param Limit: Max number of results returned\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectGatewaysResponse(AbstractModel):
    """DescribeDirectConnectGateways response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of eligible objects.\n        :type TotalCount: int\n        :param DirectConnectGatewaySet: The object array of the direct connect gateway.\n        :type DirectConnectGatewaySet: list of DirectConnectGateway\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: ID of the VPC instance\n        :type VpcId: str\n        :param FlowLogId: The unique ID of the flow log.\n        :type FlowLogId: str\n        """
        self.VpcId = None
        self.FlowLogId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowLogResponse(AbstractModel):
    """DescribeFlowLog response structure.

    """

    def __init__(self):
        """
        :param FlowLog: The flow log information.\n        :type FlowLog: list of FlowLog\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: ID of the VPC instance\n        :type VpcId: str\n        :param FlowLogId: The unique ID of the flow log.\n        :type FlowLogId: str\n        :param FlowLogName: The name of the flow log instance.\n        :type FlowLogName: str\n        :param ResourceType: The resource type of the flow log. Valid values: 'VPC', 'SUBNET', and 'NETWORKINTERFACE'.\n        :type ResourceType: str\n        :param ResourceId: The unique ID of the resource.\n        :type ResourceId: str\n        :param TrafficType: Type of flow logs to be collected. Valid values: 'ACCEPT', 'REJECT' and 'ALL'.\n        :type TrafficType: str\n        :param CloudLogId: The storage ID of the flow log.\n        :type CloudLogId: str\n        :param CloudLogState: The storage ID status of the flow log.\n        :type CloudLogState: str\n        :param OrderField: Order by field. Valid values: 'flowLogName' and 'createTime'. Default value: 'createTime'.\n        :type OrderField: str\n        :param OrderDirection: In ascending (`asc`) or descending (`desc`) order. Default value: 'desc'.\n        :type OrderDirection: str\n        :param Offset: The offset. Default value: 0.\n        :type Offset: int\n        :param Limit: The number of rows per page. Default value: 10.\n        :type Limit: int\n        :param Filters: Filter condition. `FlowLogIds` and `Filters` cannot be specified at the same time.
<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>
<li> tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key should be replaced with a specified tag key.</li>\n        :type Filters: :class:`tencentcloud.vpc.v20170312.models.Filter`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowLogsResponse(AbstractModel):
    """DescribeFlowLogs response structure.

    """

    def __init__(self):
        """
        :param FlowLog: The instance set of flow logs.\n        :type FlowLog: list of FlowLog\n        :param TotalNum: The total number of flow logs.\n        :type TotalNum: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param TimePoint: The point in time. This indicates details of this minute will be queried. For example, in `2019-02-28 18:15:20`, details at `18:15` will be queried.\n        :type TimePoint: str\n        :param VpnId: The instance ID of the VPN gateway, such as `vpn-ltjahce6`.\n        :type VpnId: str\n        :param DirectConnectGatewayId: The instance ID of the Direct Connect gateway, such as `dcg-ltjahce6`.\n        :type DirectConnectGatewayId: str\n        :param PeeringConnectionId: The instance ID of the peering connection, such as `pcx-ltjahce6`.\n        :type PeeringConnectionId: str\n        :param NatId: The instance ID of the NAT gateway, such as `nat-ltjahce6`.\n        :type NatId: str\n        :param Offset: Offset.\n        :type Offset: int\n        :param Limit: The returned quantity.\n        :type Limit: int\n        :param OrderField: The order field supports `InPkg`, `OutPkg`, `InTraffic`, and `OutTraffic`.\n        :type OrderField: str\n        :param OrderDirection: Order methods. Ascending: `ASC`, Descending: `DESC`.\n        :type OrderDirection: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayFlowMonitorDetailResponse(AbstractModel):
    """DescribeGatewayFlowMonitorDetail response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.\n        :type TotalCount: int\n        :param GatewayFlowMonitorDetailSet: The gateway traffic monitoring details.\n        :type GatewayFlowMonitorDetailSet: list of GatewayFlowMonitorDetail\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
ID of VPN gateway instance, e.g. `vpn-ltjahce6`.\n        :type GatewayId: str\n        :param IpAddresses: CVM private IP addresses with limited bandwidth.\n        :type IpAddresses: list of str\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        """
        self.GatewayId = None
        self.IpAddresses = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.IpAddresses = params.get("IpAddresses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayFlowQosResponse(AbstractModel):
    """DescribeGatewayFlowQos response structure.

    """

    def __init__(self):
        """
        :param GatewayQosSet: List of instance details.\n        :type GatewayQosSet: list of GatewayQos\n        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param HaVipIds: The unique `ID` of the `HAVIP`, such as `havip-9o233uri`.\n        :type HaVipIds: list of str\n        :param Filters: Filter condition. `HaVipIds` and `Filters` cannot be specified at the same time.
li>havip-id - String - The unique ID of the HAVIP, such as `havip-9o233uri`.</li>
<li>havip-name - String - HAVIP name.</li>
<li>vpc-id - String - VPC ID of the HAVIP.</li>
<li>subnet-id - String - Subnet ID of the HAVIP.</li>
<li>vip - String - Virtual IP address of the HAVIP.</li>
<li>address-ip - String - Bound EIP.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: The returned quantity\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHaVipsResponse(AbstractModel):
    """DescribeHaVips response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.\n        :type TotalCount: int\n        :param HaVipSet: `HAVIP` object array.\n        :type HaVipSet: list of HaVip\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Type: Protocol type for an IP location database. Valid value: `ipv4`.\n        :type Type: str\n        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpGeolocationDatabaseUrlResponse(AbstractModel):
    """DescribeIpGeolocationDatabaseUrl response structure.

    """

    def __init__(self):
        """
        :param DownLoadUrl: Download link of an IP location database\n        :type DownLoadUrl: str\n        :param ExpiredAt: Link expiration time in UTC format following the ISO8601 standard.\n        :type ExpiredAt: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param AddressIps: IP addresses to be queried. Both IPv4 and IPv6 addresses are supported.\n        :type AddressIps: list of str\n        :param Fields: Fields of the IP addresses to be queried, including `Country`, `Province`, `City`, `Region`, `Isp`, `AsName` and `AsId`\n        :type Fields: :class:`tencentcloud.vpc.v20170312.models.IpField`\n        """
        self.AddressIps = None
        self.Fields = None


    def _deserialize(self, params):
        self.AddressIps = params.get("AddressIps")
        if params.get("Fields") is not None:
            self.Fields = IpField()
            self.Fields._deserialize(params.get("Fields"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpGeolocationInfosResponse(AbstractModel):
    """DescribeIpGeolocationInfos response structure.

    """

    def __init__(self):
        """
        :param AddressInfo: IP address details\n        :type AddressInfo: list of IpGeolocationInfo\n        :param Total: Number of IP addresses\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeLocalGatewayRequest(AbstractModel):
    """DescribeLocalGateway request structure.

    """

    def __init__(self):
        """
        :param Filters: Query criteria:
vpc-id: filter by VPC ID; local-gateway-name: filter by local gateway name (fuzzy search is supported); local-gateway-id: filter by local gateway instance ID; cdc-id: filter by CDC instance ID.\n        :type Filters: list of Filter\n        :param Offset: The offset. Default value: 0. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/11646?from_cn_redirect=1).\n        :type Offset: int\n        :param Limit: The number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/11646?from_cn_redirect=1).\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalGatewayResponse(AbstractModel):
    """DescribeLocalGateway response structure.

    """

    def __init__(self):
        """
        :param LocalGatewaySet: Information set of local gateways\n        :type LocalGatewaySet: list of LocalGateway\n        :param TotalCount: Total number of local gateways\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LocalGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LocalGatewaySet") is not None:
            self.LocalGatewaySet = []
            for item in params.get("LocalGatewaySet"):
                obj = LocalGateway()
                obj._deserialize(item)
                self.LocalGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest(AbstractModel):
    """DescribeNatGatewayDestinationIpPortTranslationNatRules request structure.

    """

    def __init__(self):
        """
        :param NatGatewayIds: NAT gateway ID.\n        :type NatGatewayIds: list of str\n        :param Filters: Filter conditions:
`NatGatewayIds` and `Filters` cannot be specified at the same time.
<li> nat-gateway-id, the NAT gateway ID, such as `nat-0yi4hekt`.</li>
<li> vpc-id, the VPC ID, such as `vpc-0yi4hekt`.</li>
<li> public-ip-address, the EIP, such as `139.199.232.238`.</li>
<li>public-port, the public network port.</li>
<li>private-ip-address, the private IP, such as `10.0.0.1`.</li>
<li>private-port, the private network port.</li>
<li>description, the rule description.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. The default value is 0.\n        :type Offset: int\n        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse(AbstractModel):
    """DescribeNatGatewayDestinationIpPortTranslationNatRules response structure.

    """

    def __init__(self):
        """
        :param NatGatewayDestinationIpPortTranslationNatRuleSet: The object array of port forwarding rules for the NAT gateway.\n        :type NatGatewayDestinationIpPortTranslationNatRuleSet: list of NatGatewayDestinationIpPortTranslationNatRule\n        :param TotalCount: The number of object arrays of NAT port forwarding rules meeting the conditions.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeNatGatewaySourceIpTranslationNatRulesRequest(AbstractModel):
    """DescribeNatGatewaySourceIpTranslationNatRules request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The unique ID of the NAT Gateway, such as `nat-123xx454`.\n        :type NatGatewayId: str\n        :param Filters: Filter conditions:
<li> resource-id, the subnet ID (such as `subnet-0yi4hekt`) or CVM ID</li>
<li> public-ip-address, the EIP, such as `139.199.232.238`</li>
<li>description, the rule description</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. Default is 0.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        """
        self.NatGatewayId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
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
        


class DescribeNatGatewaySourceIpTranslationNatRulesResponse(AbstractModel):
    """DescribeNatGatewaySourceIpTranslationNatRules response structure.

    """

    def __init__(self):
        """
        :param SourceIpTranslationNatRuleSet: Object array of the SNAT rule for a NAT Gateway.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SourceIpTranslationNatRuleSet: list of SourceIpTranslationNatRule\n        :param TotalCount: The number of object arrays of eligible forwarding rules for a NAT Gateway\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SourceIpTranslationNatRuleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SourceIpTranslationNatRuleSet") is not None:
            self.SourceIpTranslationNatRuleSet = []
            for item in params.get("SourceIpTranslationNatRuleSet"):
                obj = SourceIpTranslationNatRule()
                obj._deserialize(item)
                self.SourceIpTranslationNatRuleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNatGatewaysRequest(AbstractModel):
    """DescribeNatGateways request structure.

    """

    def __init__(self):
        """
        :param NatGatewayIds: The unified ID of the NAT gateways, such as `nat-123xx454`.\n        :type NatGatewayIds: list of str\n        :param Filters: Filter condition. `NatGatewayIds` and `Filters` cannot be specified at the same time.
<li>nat-gateway-id - String - (Filter condition) The ID of the protocol port template instance, such as `nat-123xx454`.</li>
<li>vpc-id - String - (Filter condition) The unique ID of the VPC, such as `vpc-123xx454`.</li>
<li>nat-gateway-name - String - (Filter condition) The name of the protocol port template instance, such as `test_nat`.</li>
<li>tag-key - String - (Filter condition) The tag key, such as `test-key`.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. The default value is 0.\n        :type Offset: int\n        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatGatewaysResponse(AbstractModel):
    """DescribeNatGateways response structure.

    """

    def __init__(self):
        """
        :param NatGatewaySet: NAT gateway object array.\n        :type NatGatewaySet: list of NatGateway\n        :param TotalCount: The number of NAT gateway object sets meeting the conditions.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param NetDetectIds: The array of network detection instance `IDs`, such as [`netd-12345678`].\n        :type NetDetectIds: list of str\n        :param Filters: Filter conditions. `NetDetectIds` and `Filters` cannot be specified at the same time.
<li>net-detect-id - String - (Filter condition) The network detection instance ID, such as netd-12345678.</li>\n        :type Filters: list of Filter\n        :param Offset: The offset. Default: 0.\n        :type Offset: int\n        :param Limit: The number of returned values. Default: 20. Maximum: 100.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetDetectStatesResponse(AbstractModel):
    """DescribeNetDetectStates response structure.

    """

    def __init__(self):
        """
        :param NetDetectStateSet: The array of network detection verification results that meet requirements.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type NetDetectStateSet: list of NetDetectState\n        :param TotalCount: The number of network detection verification results that meet requirements.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param NetDetectIds: The array of network detection instance `IDs`, such as [`netd-12345678`].\n        :type NetDetectIds: list of str\n        :param Filters: Filter conditions. `NetDetectIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) The VPC instance ID, such as vpc-12345678.</li>
<li>net-detect-id - String - (Filter condition) The network detection instance ID, such as netd-12345678.</li>
<li>subnet-id - String - (Filter condition) The subnet instance ID, such as subnet-12345678.</li>
<li>net-detect-name - String - (Filter condition) The network detection name.</li>\n        :type Filters: list of Filter\n        :param Offset: The offset. Default: 0.\n        :type Offset: int\n        :param Limit: The number of returned values. Default: 20. Maximum: 100.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetDetectsResponse(AbstractModel):
    """DescribeNetDetects response structure.

    """

    def __init__(self):
        """
        :param NetDetectSet: The array of network detection objects that meet requirements.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type NetDetectSet: list of NetDetect\n        :param TotalCount: The number of network detection objects that meet requirements.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param NetworkAclIds: Array of network ACL instance IDs, such as [acl-12345678]. Up to 100 instances are allowed for each request. This parameter does not support specifying `NetworkAclIds` and `Filters` at the same time.\n        :type NetworkAclIds: list of str\n        :param Filters: Filter condition. `NetworkAclIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) VPC instance ID, such as vpc-12345678.</li>
<li>network-acl-id - String - (Filter condition) Network ACL instance ID, such as acl-12345678.</li>
<li>network-acl-name - String - (Filter condition) Network ACL instance name.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. Default: 0.\n        :type Offset: int\n        :param Limit: Returned quantity. Default: 20. Value range: 1-100.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetworkAclsResponse(AbstractModel):
    """DescribeNetworkAcls response structure.

    """

    def __init__(self):
        """
        :param NetworkAclSet: List of instance details.\n        :type NetworkAclSet: list of NetworkAcl\n        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: ID of a CVM instance or ENI to query\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetworkInterfaceLimitResponse(AbstractModel):
    """DescribeNetworkInterfaceLimit response structure.

    """

    def __init__(self):
        """
        :param EniQuantity: Quota of ENIs mounted to a CVM instance in a standard way\n        :type EniQuantity: int\n        :param EniPrivateIpAddressQuantity: Quota of IP addresses that can be allocated to each standard-mounted ENI\n        :type EniPrivateIpAddressQuantity: int\n        :param ExtendEniQuantity: Quota of ENIs mounted to a CVM instance as an extension
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ExtendEniQuantity: int\n        :param ExtendEniPrivateIpAddressQuantity: Quota of IP addresses that can be allocated to each extension-mounted ENI.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ExtendEniPrivateIpAddressQuantity: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.EniQuantity = None
        self.EniPrivateIpAddressQuantity = None
        self.ExtendEniQuantity = None
        self.ExtendEniPrivateIpAddressQuantity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EniQuantity = params.get("EniQuantity")
        self.EniPrivateIpAddressQuantity = params.get("EniPrivateIpAddressQuantity")
        self.ExtendEniQuantity = params.get("ExtendEniQuantity")
        self.ExtendEniPrivateIpAddressQuantity = params.get("ExtendEniPrivateIpAddressQuantity")
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: Queries the ID of the ENI instance, such as `eni-pxir56ns`. Each request can have a maximum of 100 instances. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.\n        :type NetworkInterfaceIds: list of str\n        :param Filters: Filter condition. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.
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
<li>is-primary - Boolean - Required: no - (Filter condition) Filters based on whether it is a primary ENI. If the value is ‘true’, filter only the primary ENI. If the value is ‘false’, filter only the secondary ENI. If the secondary filter parameter is provided, filter the both.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetworkInterfacesResponse(AbstractModel):
    """DescribeNetworkInterfaces response structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceSet: List of instance details.\n        :type NetworkInterfaceSet: list of NetworkInterface\n        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Filters: Filter condition. `RouteTableIds` and `Filters` cannot be specified at the same time.
<li>route-table-id - String - (Filter condition) Route table instance ID.</li>
<li>route-table-name - String - (Filter condition) Route table name.</li>
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>association.main - String - (Filter condition) Whether it is the main route table.</li>
<li>tag-key - String - Required: no - (Filter condition) Filter by tag key.</li>
<li>tag:tag-key - String - Required: no - (Filter condition) Filter by tag key-value pair. Use a specific tag key to replace `tag-key`. See Example 2 for the detailed usage.</li>\n        :type Filters: list of Filter\n        :param RouteTableIds: The route table instance ID, such as `rtb-azd4dt1c`.\n        :type RouteTableIds: list of str\n        :param Offset: Offset.\n        :type Offset: str\n        :param Limit: The number of request objects.\n        :type Limit: str\n        """
        self.Filters = None
        self.RouteTableIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.RouteTableIds = params.get("RouteTableIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteTablesResponse(AbstractModel):
    """DescribeRouteTables response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances.\n        :type TotalCount: int\n        :param RouteTableSet: Route table object.\n        :type RouteTableSet: list of RouteTable\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param SecurityGroupIds: The Security instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups.\n        :type SecurityGroupIds: list of str\n        """
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupAssociationStatisticsResponse(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics response structure.

    """

    def __init__(self):
        """
        :param SecurityGroupAssociationStatisticsSet: Statistics on the instances associated with a security group.\n        :type SecurityGroupAssociationStatisticsSet: list of SecurityGroupAssociationStatistics\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups.\n        :type SecurityGroupId: str\n        """
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupPoliciesResponse(AbstractModel):
    """DescribeSecurityGroupPolicies response structure.

    """

    def __init__(self):
        """
        :param SecurityGroupPolicySet: Security group policy set.\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param SecurityGroupIds: A set of security group instance IDs, e.g. ['sg-12345678']\n        :type SecurityGroupIds: list of str\n        """
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupReferencesResponse(AbstractModel):
    """DescribeSecurityGroupReferences response structure.

    """

    def __init__(self):
        """
        :param ReferredSecurityGroupSet: Referred security groups.\n        :type ReferredSecurityGroupSet: list of ReferredSecurityGroup\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param SecurityGroupIds: The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through `DescribeSecurityGroups`. Each request can have a maximum of 100 instances. `SecurityGroupIds` and `Filters` cannot be specified at the same time.\n        :type SecurityGroupIds: list of str\n        :param Filters: Filter conditions. `SecurityGroupIds` and `Filters` cannot be specified at the same time.
<li>security-group-id - String - (Filter condition) The security group ID.</li>
<li>project-id - Integer - (Filter condition) The project ID.</li>
<li>security-group-name - String - (Filter condition) The security group name.</li>
<li>tag-key - String - Required: no - (Filter condition) Filters by tag key. For more information, see Example 2.</li>
<li> `tag:tag-key` - String - Required: no - (Filter condition) Filters by tag key pair. For this parameter, `tag-key` will be replaced with a specific tag key. For more information, see Example 3.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. Default value: 0.\n        :type Offset: str\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupsResponse(AbstractModel):
    """DescribeSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param SecurityGroupSet: Security group object.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SecurityGroupSet: list of SecurityGroup\n        :param TotalCount: The number of instances meeting the filter condition.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
<li>service-template-group-id - String - (Filter condition) Protocol port template group instance ID, such as `ppmg-e6dy460g`.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. The default value is 0.\n        :type Offset: str\n        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.\n        :type Limit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceTemplateGroupsResponse(AbstractModel):
    """DescribeServiceTemplateGroups response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.\n        :type TotalCount: int\n        :param ServiceTemplateGroupSet: Protocol port template group.\n        :type ServiceTemplateGroupSet: list of ServiceTemplateGroup\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
<li>service-template-id - String - (Filter condition) Protocol port template instance ID, such as `ppm-e6dy460g`.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. The default value is 0.\n        :type Offset: str\n        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.\n        :type Limit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceTemplatesResponse(AbstractModel):
    """DescribeServiceTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.\n        :type TotalCount: int\n        :param ServiceTemplateSet: Protocol port template object.\n        :type ServiceTemplateSet: list of ServiceTemplate\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param SubnetIds: Queries the ID of the subnet instance, such as `subnet-pxir56ns`. Each request can have a maximum of 100 instances. `SubnetIds` and `Filters` cannot be specified at the same time.\n        :type SubnetIds: list of str\n        :param Filters: Filter condition. `SubnetIds` and `Filters` cannot be specified at the same time.
<li>subnet-id - String - (Filter condition) Subnet instance name.</li>
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>cidr-block - String - (Filter condition) Subnet IP range, such as `192.168.1.0`.</li>
<li>is-default - Boolean - (Filter condition) Whether it is the default subnet.</li>
<li>is-remote-vpc-snat - Boolean - (Filter condition) Whether it is a VPC SNAT address pool subnet.</li>
<li>subnet-name - String - (Filter condition) Subnet name.</li>
<li>zone - String - (Filter condition) Availability zone.</li>
<li> tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>
<li>tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. Use a specific tag key to replace `tag-key`. For its usage, see example 2.</li>
<li>cdc-id - String - Required: No - (Filter condition) Filter by CDC ID to obtain subnets in the specified CDC.</li>
<li>is-cdc-subnet - String - Required: No - (Filter condition) Whether it is a CDC subnet. Valid values: `0` (no); `1` (yes).</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. Default value: 0.\n        :type Offset: str\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetsResponse(AbstractModel):
    """DescribeSubnets response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.\n        :type TotalCount: int\n        :param SubnetSet: Subnet object.\n        :type SubnetSet: list of Subnet\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param TaskId: Async task ID. Either TaskId or DealName must be entered.\n        :type TaskId: int\n        :param DealName: Billing order No. Either TaskId or DealName must be entered.\n        :type DealName: str\n        """
        self.TaskId = None
        self.DealName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult response structure.

    """

    def __init__(self):
        """
        :param TaskId: Job ID\n        :type TaskId: int\n        :param Result: The execution results, including `SUCCESS`, `FAILED`, and `RUNNING`\n        :type Result: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeVpcEndPointRequest(AbstractModel):
    """DescribeVpcEndPoint request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter condition
<li> end-point-service-id - String - (Filter condition) Endpoint service ID.</li>
<li>end-point-name - String - (Filter condition) Endpoint instance name.</li>
<li> end-point-id - String - (Filter condition) Endpoint instance ID.</li>
<li> vpc-id - String - (Filter condition) VPC instance ID.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of results per page; default value: 20; maximum value: 100.\n        :type Limit: int\n        :param EndPointId: Endpoint ID list\n        :type EndPointId: list of str\n        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EndPointId = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcEndPointResponse(AbstractModel):
    """DescribeVpcEndPoint response structure.

    """

    def __init__(self):
        """
        :param EndPointSet: Endpoint\n        :type EndPointSet: list of EndPoint\n        :param TotalCount: Number of matched endpoints\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.EndPointSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EndPointSet") is not None:
            self.EndPointSet = []
            for item in params.get("EndPointSet"):
                obj = EndPoint()
                obj._deserialize(item)
                self.EndPointSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcEndPointServiceRequest(AbstractModel):
    """DescribeVpcEndPointService request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter condition
<li> service-id - String - (Filter condition) Unique endpoint service ID.</li>
<li>service-name - String - (Filter condition) Endpoint service instance name.</li>
<li>service-instance-id - String - (Filter condition) Unique real server ID in the format of `lb-xxx`.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of results per page; default value: 20; maximum value: 100.\n        :type Limit: int\n        :param EndPointServiceIds: Endpoint service ID\n        :type EndPointServiceIds: list of str\n        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EndPointServiceIds = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.EndPointServiceIds = params.get("EndPointServiceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcEndPointServiceResponse(AbstractModel):
    """DescribeVpcEndPointService response structure.

    """

    def __init__(self):
        """
        :param EndPointServiceSet: Array of endpoint services\n        :type EndPointServiceSet: list of EndPointService\n        :param TotalCount: Number of matched results\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.EndPointServiceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EndPointServiceSet") is not None:
            self.EndPointServiceSet = []
            for item in params.get("EndPointServiceSet"):
                obj = EndPointService()
                obj._deserialize(item)
                self.EndPointServiceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcEndPointServiceWhiteListRequest(AbstractModel):
    """DescribeVpcEndPointServiceWhiteList request structure.

    """

    def __init__(self):
        """
        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of results per page; default value: 20; maximum value: 100.\n        :type Limit: int\n        :param Filters: Filter condition
<li> user-uin - String - (Filter condition) UIN.</li>
<li> end-point-service-id - String - (Filter condition) Endpoint service ID.</li>\n        :type Filters: list of Filter\n        """
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
        


class DescribeVpcEndPointServiceWhiteListResponse(AbstractModel):
    """DescribeVpcEndPointServiceWhiteList response structure.

    """

    def __init__(self):
        """
        :param VpcEndpointServiceUserSet: Array of allowed endpoint services\n        :type VpcEndpointServiceUserSet: list of VpcEndPointServiceUser\n        :param TotalCount: Number of matched allowlists\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.VpcEndpointServiceUserSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcEndpointServiceUserSet") is not None:
            self.VpcEndpointServiceUserSet = []
            for item in params.get("VpcEndpointServiceUserSet"):
                obj = VpcEndPointServiceUser()
                obj._deserialize(item)
                self.VpcEndpointServiceUserSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcInstancesRequest(AbstractModel):
    """DescribeVpcInstances request structure.

    """

    def __init__(self):
        """
        :param Filters: Filter condition. `RouteTableIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>instance-type - String - (Filter condition) CVM instance ID.</li>
<li>instance-name - String - (Filter condition) CVM name.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset.\n        :type Offset: int\n        :param Limit: The number of requested objects.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcInstancesResponse(AbstractModel):
    """DescribeVpcInstances response structure.

    """

    def __init__(self):
        """
        :param InstanceSet: List of CVM instances.\n        :type InstanceSet: list of CvmInstance\n        :param TotalCount: The number of eligible CVM instances.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The `ID` of the `VPC`, such as `vpc-f49l6u0z`.\n        :type VpcId: str\n        :param Ipv6Addresses: The `IP` address list. Each request supports a maximum of `10` batch querying.\n        :type Ipv6Addresses: list of str\n        :param Offset: Offset.\n        :type Offset: int\n        :param Limit: The returned quantity.\n        :type Limit: int\n        """
        self.VpcId = None
        self.Ipv6Addresses = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Ipv6Addresses = params.get("Ipv6Addresses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcIpv6AddressesResponse(AbstractModel):
    """DescribeVpcIpv6Addresses response structure.

    """

    def __init__(self):
        """
        :param Ipv6AddressSet: The `IPv6` address list.\n        :type Ipv6AddressSet: list of VpcIpv6Address\n        :param TotalCount: The total number of `IPv6` addresses.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The `ID` of the `VPC`, such as `vpc-f49l6u0z`.\n        :type VpcId: str\n        :param PrivateIpAddresses: The private `IP` address list. Each request supports a maximum of `10` batch querying.\n        :type PrivateIpAddresses: list of str\n        """
        self.VpcId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcPrivateIpAddressesResponse(AbstractModel):
    """DescribeVpcPrivateIpAddresses response structure.

    """

    def __init__(self):
        """
        :param VpcPrivateIpAddressSet: The list of private `IP` address information.\n        :type VpcPrivateIpAddressSet: list of VpcPrivateIpAddress\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcIds: Vpc instance ID, e.g. vpc-f1xjkw1b.\n        :type VpcIds: list of str\n        """
        self.VpcIds = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcResourceDashboardResponse(AbstractModel):
    """DescribeVpcResourceDashboard response structure.

    """

    def __init__(self):
        """
        :param ResourceDashboardSet: List of resource objects.\n        :type ResourceDashboardSet: list of ResourceDashboard\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeVpcTaskResultRequest(AbstractModel):
    """DescribeVpcTaskResult request structure.

    """

    def __init__(self):
        """
        :param TaskId: `RequestId` returned by an async task\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcTaskResultResponse(AbstractModel):
    """DescribeVpcTaskResult response structure.

    """

    def __init__(self):
        """
        :param Status: Execution result of an async task Valid values: `SUCCESS`: the task has been successfully executed; `FAILED`: the job execution failed; `RUNNING`: the job is executing.\n        :type Status: str\n        :param Output: Output of the async task execution result\n        :type Output: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Status = None
        self.Output = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Output = params.get("Output")
        self.RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs request structure.

    """

    def __init__(self):
        """
        :param VpcIds: The VPC instance ID, such as `vpc-f49l6u0z`. Each request supports a maximum of 100 instances. `VpcIds` and `Filters` cannot be specified at the same time.\n        :type VpcIds: list of str\n        :param Filters: Filter condition. `VpcIds` and `Filters` cannot be specified at the same time.
<li>vpc-name - String - (Filter condition) VPC instance name.</li>
<li>is-default - String - (Filter condition) Indicates whether it is the default VPC.</li>
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>cidr-block - String - (Filter condition) VPC CIDR.</li>
<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>
<li>tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key is replaced with the specific tag key. For usage, refer to case 2.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset. Default value: 0.\n        :type Offset: str\n        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.\n        :type Limit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcsResponse(AbstractModel):
    """DescribeVpcs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of objects meeting the condition.\n        :type TotalCount: int\n        :param VpcSet: The VPC object.\n        :type VpcSet: list of Vpc\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpnConnectionIds: The instance ID of the VPN tunnel, such as `vpnx-f49l6u0z`. Each request can have a maximum of 100 instances. `VpnConnectionIds` and `Filters` cannot be specified at the same time.\n        :type VpnConnectionIds: list of str\n        :param Filters: Filter condition. In each request, the upper limit for `Filters` is 10 and 5 for `Filter.Values`. `VpnConnectionIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - VPC instance ID, such as `vpc-0a36uwkr`.</li>
<li>vpn-gateway-id - String - VPN gateway instance ID, such as `vpngw-p4lmqawn`.</li>
<li>customer-gateway-id - String - Customer gateway instance ID, such as `cgw-l4rblw63`.</li>
<li>vpn-connection-name - String - Connection name, such as `test-vpn`.</li>
<li>vpn-connection-id - String - Connection instance ID, such as `vpnx-5p7vkch8"`.</li>\n        :type Filters: list of Filter\n        :param Offset: The Offset. The default value is 0. For more information about Offset, see the relevant section in the API Introduction.\n        :type Offset: int\n        :param Limit: Number of values to be returned. The default value is 20. Maximum is 100.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpnConnectionsResponse(AbstractModel):
    """DescribeVpnConnections response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.\n        :type TotalCount: int\n        :param VpnConnectionSet: VPN tunnel instance.\n        :type VpnConnectionSet: list of VpnConnection\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param Offset: Offset.\n        :type Offset: int\n        :param Limit: The returned quantity\n        :type Limit: int\n        """
        self.VpnGatewayId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpnGatewayCcnRoutesResponse(AbstractModel):
    """DescribeVpnGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RouteSet: The CCN route (IDC IP range) list.\n        :type RouteSet: list of VpngwCcnRoutes\n        :param TotalCount: Number of objects that meet the condition.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeVpnGatewayRoutesRequest(AbstractModel):
    """DescribeVpnGatewayRoutes request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN gateway ID\n        :type VpnGatewayId: str\n        :param Filters: Filter condition. Valid values: `DestinationCidr`, `InstanceId`, and `InstanceType`.\n        :type Filters: list of Filter\n        :param Offset: Offset. Default value: 0\n        :type Offset: int\n        :param Limit: Number of returned results per page. Default value: 20; maximum value: 100\n        :type Limit: int\n        """
        self.VpnGatewayId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
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
        


class DescribeVpnGatewayRoutesResponse(AbstractModel):
    """DescribeVpnGatewayRoutes response structure.

    """

    def __init__(self):
        """
        :param Routes: Destination routes of the VPN gateway\n        :type Routes: list of VpnGatewayRoute\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Routes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpnGatewayRoute()
                obj._deserialize(item)
                self.Routes.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpnGatewaysRequest(AbstractModel):
    """DescribeVpnGateways request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayIds: The VPN gateway instance ID, such as `vpngw-f49l6u0z`. Each request can have a maximum of 100 instances. `VpnGatewayIds` and `Filters` cannot be specified at the same time.\n        :type VpnGatewayIds: list of str\n        :param Filters: Filter condition. `VpnGatewayIds` and `Filters` cannot be specified at the same time.
<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>
<li>vpn-gateway-id - String - (Filter condition) VPN instance ID, such as `vpngw-5aluhh9t`.</li>
<li>vpn-gateway-name - String - (Filter condition) VPN instance name.</li>
<li>type - String - (Filter condition) VPN gateway type: 'IPSEC', 'SSL'.</li>
<li>public-ip-address- String - (Filter condition) Public IP.</li>
<li>renew-flag - String - (Filter condition) Gateway renewal type. Manual renewal: `NOTIFY_AND_MANUAL_RENEW`, Automatic renewal: `NOTIFY_AND_AUTO_RENEW`.</li>
<li>zone - String - (Filter condition) The availability zone where the VPN is located, such as `ap-guangzhou-2`.</li>\n        :type Filters: list of FilterObject\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: The number of request objects.\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpnGatewaysResponse(AbstractModel):
    """DescribeVpnGateways response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of instances meeting the filter condition.\n        :type TotalCount: int\n        :param VpnGatewaySet: The list of details of VPN gateway instances.\n        :type VpnGatewaySet: list of VpnGateway\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param IpProtocol: Network protocol. Available choices: `TCP`, `UDP`.\n        :type IpProtocol: str\n        :param PublicIpAddress: EIP.\n        :type PublicIpAddress: str\n        :param PublicPort: Public port.\n        :type PublicPort: int\n        :param PrivateIpAddress: Private network address.\n        :type PrivateIpAddress: str\n        :param PrivatePort: Private network port.\n        :type PrivatePort: int\n        :param Description: NAT gateway forwarding rule description.\n        :type Description: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnInstancesRequest(AbstractModel):
    """DetachCcnInstances request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        :param Instances: The list of network instances to be unbound\n        :type Instances: list of CcnInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnInstancesResponse(AbstractModel):
    """DetachCcnInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachClassicLinkVpcRequest(AbstractModel):
    """DetachClassicLinkVpc request structure.

    """

    def __init__(self):
        """
        :param VpcId: The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API.\n        :type VpcId: str\n        :param InstanceIds: Queries the ID of the CVM instance, such as `ins-r8hr2upy`.\n        :type InstanceIds: list of str\n        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachClassicLinkVpcResponse(AbstractModel):
    """DetachClassicLinkVpc response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.\n        :type NetworkInterfaceId: str\n        :param InstanceId: The ID of the CVM instance, such as `ins-r8hr2upy`.\n        :type InstanceId: str\n        """
        self.NetworkInterfaceId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachNetworkInterfaceResponse(AbstractModel):
    """DetachNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DirectConnectGateway(AbstractModel):
    """Direct Connect gateway object.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: Direct Connect `ID`.\n        :type DirectConnectGatewayId: str\n        :param DirectConnectGatewayName: Direct Connect gateway name.\n        :type DirectConnectGatewayName: str\n        :param VpcId: The `ID` of the `VPC` instance associated with the Direct Connect gateway.\n        :type VpcId: str\n        :param NetworkType: The associated network type:
<li>`VPC` - VPC</li>
<li>`CCN` - CCN</li>\n        :type NetworkType: str\n        :param NetworkInstanceId: The `ID` of the associated network instance:
<li>When the NetworkType is `VPC`, this value is the VPC instance `ID`</li>
<li>When the NetworkType is `CCN`, this value is the CCN instance `ID`</li>\n        :type NetworkInstanceId: str\n        :param GatewayType: Gateway type:
<li>NORMAL - Standard type. Note: CCN only supports the standard type</li>
<li>NAT - NAT type</li>
NAT type supports network address switch configuration. After the type is confirmed, it cannot be modified. A VPC can create one NAT-type Direct Connect gateway and one non-NAT-type Direct Connect gateway\n        :type GatewayType: str\n        :param CreateTime: Creation Time.\n        :type CreateTime: str\n        :param DirectConnectGatewayIp: Direct Connect gateway IP.\n        :type DirectConnectGatewayIp: str\n        :param CcnId: The `ID` of the `CCN` instance associated with the Direct Connect gateway.\n        :type CcnId: str\n        :param CcnRouteType: The route-learning type of the CCN:
<li>`BGP` - Automatic learning.</li>
<li>`STATIC` - Static, that is, user-configured.</li>\n        :type CcnRouteType: str\n        :param EnableBGP: Whether BGP is enabled.\n        :type EnableBGP: bool\n        :param EnableBGPCommunity: Whether to enable BGP's `community` attribute. Valid values: enable, disable\n        :type EnableBGPCommunity: bool\n        :param NatGatewayId: ID of the NAT gateway bound.
Note: this field may return `null`, indicating that no valid value was found.\n        :type NatGatewayId: str\n        :param VXLANSupport: Whether the direct connect gateway supports the VXLAN architecture.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type VXLANSupport: list of bool\n        :param ModeType: CCN route publishing mode. Valid values: `standard` and `exquisite`.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ModeType: str\n        :param LocalZone: Whether the direct connect gateway is for an edge zone.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type LocalZone: bool\n        :param Zone: Availability zone where the direct connect gateway resides.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Zone: str\n        """
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
        self.LocalZone = None
        self.Zone = None


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
        self.LocalZone = params.get("LocalZone")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectGatewayCcnRoute(AbstractModel):
    """The object of the CCN route (IDC IP range) of the Direct Connect gateway

    """

    def __init__(self):
        """
        :param RouteId: Route ID.\n        :type RouteId: str\n        :param DestinationCidrBlock: IDC IP range.\n        :type DestinationCidrBlock: str\n        :param ASPath: The `AS-Path` attribute of `BGP`.\n        :type ASPath: list of str\n        """
        self.RouteId = None
        self.DestinationCidrBlock = None
        self.ASPath = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.ASPath = params.get("ASPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCcnRoutesRequest(AbstractModel):
    """DisableCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        :param RouteIds: The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`.\n        :type RouteIds: list of str\n        """
        self.CcnId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCcnRoutesResponse(AbstractModel):
    """DisableCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
ID of VPN gateway instance, e.g. `vpn-ltjahce6`.\n        :type GatewayId: str\n        """
        self.GatewayId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableGatewayFlowMonitorResponse(AbstractModel):
    """DisableGatewayFlowMonitor response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateAddressRequest(AbstractModel):
    """DisassociateAddress request structure.

    """

    def __init__(self):
        """
        :param AddressId: The unique ID of the EIP, such as `eip-11112222`.\n        :type AddressId: str\n        :param ReallocateNormalPublicIp: Whether a common public IP is assigned after the EIP is unbound. Value range:<br><li>TRUE: Indicates that after the EIP is unbound, a common public IP is assigned.<br><li>FALSE: Indicates that after the EIP is unbound, a common public IP is not assigned.<br>Default value: FALSE.<br><br>The parameter can be specified only under the following conditions:<br><li>It can only be specified when you unbind an EIP from the primary private IP of the primary ENI.<br><li>After an EIP is unbound, you can assign public IPs to an account up to 10 times per day. For more information, use the [DescribeAddressQuota] (https://intl.cloud.tencent.com/document/api/213/1378?from_cn_redirect=1) API.\n        :type ReallocateNormalPublicIp: bool\n        """
        self.AddressId = None
        self.ReallocateNormalPublicIp = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.ReallocateNormalPublicIp = params.get("ReallocateNormalPublicIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateAddressResponse(AbstractModel):
    """DisassociateAddress response structure.

    """

    def __init__(self):
        """
        :param TaskId: The async task ID. You can use the [DescribeTaskResult](https://intl.cloud.tencent.com/document/api/215/36271?from_cn_redirect=1) API to query the task status.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: The direct connect gateway ID.\n        :type VpcId: str\n        :param NatGatewayId: The NAT Gateway ID.\n        :type NatGatewayId: str\n        :param DirectConnectGatewayId: The ID of the VPC instance, which can be obtained from the `VpcId` field in response of the `DescribeVpcs` API.\n        :type DirectConnectGatewayId: str\n        """
        self.VpcId = None
        self.NatGatewayId = None
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NatGatewayId = params.get("NatGatewayId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateDirectConnectGatewayNatGatewayResponse(AbstractModel):
    """DisassociateDirectConnectGatewayNatGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNatGatewayAddressRequest(AbstractModel):
    """DisassociateNatGatewayAddress request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.\n        :type NatGatewayId: str\n        :param PublicIpAddresses: Array of the EIPs to be unbound from the NAT gateway.\n        :type PublicIpAddresses: list of str\n        """
        self.NatGatewayId = None
        self.PublicIpAddresses = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateNatGatewayAddressResponse(AbstractModel):
    """DisassociateNatGatewayAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNetworkAclSubnetsRequest(AbstractModel):
    """DisassociateNetworkAclSubnets request structure.

    """

    def __init__(self):
        """
        :param NetworkAclId: Network ACL instance ID. Example: acl-12345678.\n        :type NetworkAclId: str\n        :param SubnetIds: Array of subnet instance IDs. Example: [subnet-12345678].\n        :type SubnetIds: list of str\n        """
        self.NetworkAclId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateNetworkAclSubnetsResponse(AbstractModel):
    """DisassociateNetworkAclSubnets response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNetworkInterfaceSecurityGroupsRequest(AbstractModel):
    """DisassociateNetworkInterfaceSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: ENI instance ID, e.g. eni-pxir56ns. You can enter up to 100 instances for each request.\n        :type NetworkInterfaceIds: list of str\n        :param SecurityGroupIds: The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups. You can enter up to 100 instances for each request.\n        :type SecurityGroupIds: list of str\n        """
        self.NetworkInterfaceIds = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateNetworkInterfaceSecurityGroupsResponse(AbstractModel):
    """DisassociateNetworkInterfaceSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateVpcEndPointSecurityGroupsRequest(AbstractModel):
    """DisassociateVpcEndPointSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupIds: Array of security group IDs\n        :type SecurityGroupIds: list of str\n        :param EndPointId: Endpoint ID\n        :type EndPointId: str\n        """
        self.SecurityGroupIds = None
        self.EndPointId = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateVpcEndPointSecurityGroupsResponse(AbstractModel):
    """DisassociateVpcEndPointSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DownloadCustomerGatewayConfigurationRequest(AbstractModel):
    """DownloadCustomerGatewayConfiguration request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param VpnConnectionId: The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`.\n        :type VpnConnectionId: str\n        :param CustomerGatewayVendor: Customer gateway vendor information object, which can be obtained through DescribeCustomerGatewayVendors.\n        :type CustomerGatewayVendor: :class:`tencentcloud.vpc.v20170312.models.CustomerGatewayVendor`\n        :param InterfaceName: Name of the physical API for tunnel access device.\n        :type InterfaceName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadCustomerGatewayConfigurationResponse(AbstractModel):
    """DownloadCustomerGatewayConfiguration response structure.

    """

    def __init__(self):
        """
        :param CustomerGatewayConfiguration: Configuration information in XML format.\n        :type CustomerGatewayConfiguration: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        :param RouteIds: The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`.\n        :type RouteIds: list of str\n        """
        self.CcnId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableCcnRoutesResponse(AbstractModel):
    """EnableCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
ID of VPN gateway instance, e.g. `vpn-ltjahce6`.\n        :type GatewayId: str\n        """
        self.GatewayId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGatewayFlowMonitorResponse(AbstractModel):
    """EnableGatewayFlowMonitor response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableVpcEndPointConnectRequest(AbstractModel):
    """EnableVpcEndPointConnect request structure.

    """

    def __init__(self):
        """
        :param EndPointServiceId: Endpoint service ID\n        :type EndPointServiceId: str\n        :param EndPointId: Endpoint ID\n        :type EndPointId: list of str\n        :param AcceptFlag: Whether to accept the request of connecting with an endpoint\n        :type AcceptFlag: bool\n        """
        self.EndPointServiceId = None
        self.EndPointId = None
        self.AcceptFlag = None


    def _deserialize(self, params):
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.EndPointId = params.get("EndPointId")
        self.AcceptFlag = params.get("AcceptFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableVpcEndPointConnectResponse(AbstractModel):
    """EnableVpcEndPointConnect response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EndPoint(AbstractModel):
    """Endpoint details

    """

    def __init__(self):
        """
        :param EndPointId: Endpoint ID\n        :type EndPointId: str\n        :param VpcId: VPC ID\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        :param EndPointOwner: APP ID\n        :type EndPointOwner: str\n        :param EndPointName: Endpoint name\n        :type EndPointName: str\n        :param ServiceVpcId: Endpoint service VPC ID\n        :type ServiceVpcId: str\n        :param ServiceVip: Endpoint service VIP\n        :type ServiceVip: str\n        :param EndPointServiceId: Endpoint service ID\n        :type EndPointServiceId: str\n        :param EndPointVip: Endpoint VIP\n        :type EndPointVip: str\n        :param State: Endpoint status. Valid values: `ACTIVE` (available), `PENDING` (to be accepted), `ACCEPTING` (being accepted), `REJECTED` (rejected), and `FAILED` (failed).\n        :type State: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param GroupSet: ID list of security group instances bound with endpoints\n        :type GroupSet: list of str\n        :param ServiceName: Endpoint service name
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ServiceName: str\n        """
        self.EndPointId = None
        self.VpcId = None
        self.SubnetId = None
        self.EndPointOwner = None
        self.EndPointName = None
        self.ServiceVpcId = None
        self.ServiceVip = None
        self.EndPointServiceId = None
        self.EndPointVip = None
        self.State = None
        self.CreateTime = None
        self.GroupSet = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.EndPointId = params.get("EndPointId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.EndPointOwner = params.get("EndPointOwner")
        self.EndPointName = params.get("EndPointName")
        self.ServiceVpcId = params.get("ServiceVpcId")
        self.ServiceVip = params.get("ServiceVip")
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.EndPointVip = params.get("EndPointVip")
        self.State = params.get("State")
        self.CreateTime = params.get("CreateTime")
        self.GroupSet = params.get("GroupSet")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndPointService(AbstractModel):
    """Endpoint service

    """

    def __init__(self):
        """
        :param EndPointServiceId: Endpoint service ID\n        :type EndPointServiceId: str\n        :param VpcId: VPC ID\n        :type VpcId: str\n        :param ServiceOwner: APP ID\n        :type ServiceOwner: str\n        :param ServiceName: Endpoint service name\n        :type ServiceName: str\n        :param ServiceVip: Real server VIP\n        :type ServiceVip: str\n        :param ServiceInstanceId: Real server ID in the format of `lb-xxx`.\n        :type ServiceInstanceId: str\n        :param AutoAcceptFlag: Whether to automatically accept\n        :type AutoAcceptFlag: bool\n        :param EndPointCount: Number of associated endpoints
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type EndPointCount: int\n        :param EndPointSet: Array of endpoints
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type EndPointSet: list of EndPoint\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        """
        self.EndPointServiceId = None
        self.VpcId = None
        self.ServiceOwner = None
        self.ServiceName = None
        self.ServiceVip = None
        self.ServiceInstanceId = None
        self.AutoAcceptFlag = None
        self.EndPointCount = None
        self.EndPointSet = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.VpcId = params.get("VpcId")
        self.ServiceOwner = params.get("ServiceOwner")
        self.ServiceName = params.get("ServiceName")
        self.ServiceVip = params.get("ServiceVip")
        self.ServiceInstanceId = params.get("ServiceInstanceId")
        self.AutoAcceptFlag = params.get("AutoAcceptFlag")
        self.EndPointCount = params.get("EndPointCount")
        if params.get("EndPointSet") is not None:
            self.EndPointSet = []
            for item in params.get("EndPointSet"):
                obj = EndPoint()
                obj._deserialize(item)
                self.EndPointSet.append(obj)
        self.CreateTime = params.get("CreateTime")
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
        :param Name: The attribute name. If more than one Filter exists, the logical relation between these Filters is `AND`.\n        :type Name: str\n        :param Values: The attribute value. If there are multiple Values for one Filter, the logical relation between these Values under the same Filter is `OR`.\n        :type Values: list of str\n        """
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
        


class FilterObject(AbstractModel):
    """Filter key-value pair

    """

    def __init__(self):
        """
        :param Name: The attribute name. If more than one Filter exists, the logical relation between these Filters is `AND`.\n        :type Name: str\n        :param Values: The attribute value. If there are multiple Values for one Filter, the logical relation between these Values under the same Filter is `OR`.\n        :type Values: list of str\n        """
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
        


class FlowLog(AbstractModel):
    """Flow Log

    """

    def __init__(self):
        """
        :param VpcId: ID of the VPC instance\n        :type VpcId: str\n        :param FlowLogId: The unique ID of the flow log.\n        :type FlowLogId: str\n        :param FlowLogName: The name of the flow log instance.\n        :type FlowLogName: str\n        :param ResourceType: The resource type of the flow log. Valid values: 'VPC', 'SUBNET', and 'NETWORKINTERFACE'.\n        :type ResourceType: str\n        :param ResourceId: The unique ID of the resource.\n        :type ResourceId: str\n        :param TrafficType: Type of flow logs to be collected. Valid values: `ACCEPT`, `REJECT` and `ALL`.\n        :type TrafficType: str\n        :param CloudLogId: The storage ID of the flow log.\n        :type CloudLogId: str\n        :param CloudLogState: The storage ID status of the flow log.\n        :type CloudLogState: str\n        :param FlowLogDescription: The flow log description.\n        :type FlowLogDescription: str\n        :param CreatedTime: The creation time of the flow log.\n        :type CreatedTime: str\n        :param TagSet: Tag list, such as [{"Key": "city", "Value": "shanghai"}]\n        :type TagSet: list of Tag\n        """
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
        self.TagSet = None


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
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayFlowMonitorDetail(AbstractModel):
    """The gateway traffic monitoring details

    """

    def __init__(self):
        """
        :param PrivateIpAddress: Origin `IP`.\n        :type PrivateIpAddress: str\n        :param InPkg: Inbound packets.\n        :type InPkg: int\n        :param OutPkg: Outbound packets.\n        :type OutPkg: int\n        :param InTraffic: Inbound traffic, in Byte.\n        :type InTraffic: int\n        :param OutTraffic: Outbound traffic, in Byte.\n        :type OutTraffic: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayQos(AbstractModel):
    """Gateway bandwidth limit information

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID.\n        :type VpcId: str\n        :param IpAddress: CVM Private IP.\n        :type IpAddress: str\n        :param Bandwidth: Bandwidth limit value.\n        :type Bandwidth: int\n        :param CreateTime: The creation time.\n        :type CreateTime: str\n        """
        self.VpcId = None
        self.IpAddress = None
        self.Bandwidth = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.IpAddress = params.get("IpAddress")
        self.Bandwidth = params.get("Bandwidth")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCcnRegionBandwidthLimitsRequest(AbstractModel):
    """GetCcnRegionBandwidthLimits request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        :param Filters: The filter condition.
<li>sregion - String - (Filter condition) Filter by the source region, such as 'ap-guangzhou'.</li>
<li>dregion - String - (Filter condition) Filter by the destination region, such as 'ap-shanghai-bm'.</li>\n        :type Filters: list of Filter\n        :param SortedBy: The sorting condition. Valid values: `BandwidthLimit` and `ExpireTime`.\n        :type SortedBy: str\n        :param Offset: The offset.\n        :type Offset: int\n        :param Limit: The returned quantity.\n        :type Limit: int\n        :param OrderBy: In ascending or descending order. Valid values: 'ASC' and 'DESC'.\n        :type OrderBy: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCcnRegionBandwidthLimitsResponse(AbstractModel):
    """GetCcnRegionBandwidthLimits response structure.

    """

    def __init__(self):
        """
        :param CcnBandwidthSet: The outbound bandwidth limits of regions in a CCN instance.
Note: this field may return null, indicating that no valid value was found.\n        :type CcnBandwidthSet: list of CcnBandwidthInfo\n        :param TotalCount: The number of eligible objects.
Note: this field may return null, indicating that no valid value was found.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param HaVipId: The `ID` of the `HAVIP`. This is the unique identifier of the `HAVIP`.\n        :type HaVipId: str\n        :param HaVipName: The name of the `HAVIP`.\n        :type HaVipName: str\n        :param Vip: The virtual IP address.\n        :type Vip: str\n        :param VpcId: The `ID` of the VPC to which the `HAVIP` belongs.\n        :type VpcId: str\n        :param SubnetId: The `ID` of the subnet to which the `HAVIP` belongs.\n        :type SubnetId: str\n        :param NetworkInterfaceId: The `ID` of the ENI associated with the `HAVIP`.\n        :type NetworkInterfaceId: str\n        :param InstanceId: The `ID` of the bound instance.\n        :type InstanceId: str\n        :param AddressIp: Bound `EIP`.\n        :type AddressIp: str\n        :param State: Status:
<li>`AVAILABLE`: Operating</li>
<li>`UNBIND`: Not bound</li>\n        :type State: str\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        :param Business: Identifier for businesses that use HAVIP.\n        :type Business: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HaVipAssociateAddressIpRequest(AbstractModel):
    """HaVipAssociateAddressIp request structure.

    """

    def __init__(self):
        """
        :param HaVipId: The unique `ID` of the `HAVIP`, such as `havip-9o233uri`. This must be a `HAVIP` that has not been bound to an `EIP`\n        :type HaVipId: str\n        :param AddressIp: The Elastic `IP`. This must be an `EIP` that has not been bound to a `HAVIP`\n        :type AddressIp: str\n        """
        self.HaVipId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.AddressIp = params.get("AddressIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HaVipAssociateAddressIpResponse(AbstractModel):
    """HaVipAssociateAddressIp response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class HaVipDisassociateAddressIpRequest(AbstractModel):
    """HaVipDisassociateAddressIp request structure.

    """

    def __init__(self):
        """
        :param HaVipId: The unique `ID` of the `HAVIP`, such as `havip-9o233uri`. This must be an `HAVIP` that has been bound to an `EIP`.\n        :type HaVipId: str\n        """
        self.HaVipId = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HaVipDisassociateAddressIpResponse(AbstractModel):
    """HaVipDisassociateAddressIp response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IKEOptionsSpecification(AbstractModel):
    """Internet Key Exchange (IKE) configuration. IKE has a self-protection mechanism. The network security protocol is configured by the user.

    """

    def __init__(self):
        """
        :param PropoEncryAlgorithm: Encryption algorithm. Valid values: `3DES-CBC`, `AES-CBC-128`, `AES-CBS-192`, `AES-CBC-256`, `DES-CBC`, and `SM4`; default value: `3DES-CBC`.\n        :type PropoEncryAlgorithm: str\n        :param PropoAuthenAlgorithm: Authentication algorithm. Valid values: `MD5`, `SHA1` and `SHA-256`; default value: `MD5`.\n        :type PropoAuthenAlgorithm: str\n        :param ExchangeMode: Negotiation mode. Available values: 'AGGRESSIVE' and 'MAIN'. Default is MAIN.\n        :type ExchangeMode: str\n        :param LocalIdentity: Type of local identity. Available values: 'ADDRESS' and 'FQDN'. Default is ADDRESS.\n        :type LocalIdentity: str\n        :param RemoteIdentity: Type of remote identity. Available values: 'ADDRESS' and 'FQDN'. Default is ADDRESS.\n        :type RemoteIdentity: str\n        :param LocalAddress: Local identity. When ADDRESS is selected for LocalIdentity, LocalAddress is required. The default LocalAddress is the public IP of the VPN gateway.\n        :type LocalAddress: str\n        :param RemoteAddress: Remote identity. When ADDRESS is selected for RemoteIdentity, RemoteAddress is required.\n        :type RemoteAddress: str\n        :param LocalFqdnName: Local identity. When FQDN is selected for LocalIdentity, LocalFqdnName is required.\n        :type LocalFqdnName: str\n        :param RemoteFqdnName: Remote identity. When FQDN is selected for RemoteIdentity, RemoteFqdnName is required.\n        :type RemoteFqdnName: str\n        :param DhGroupName: DH group. Specify the DH group used for exchanging the key via IKE. Available values: 'GROUP1', 'GROUP2', 'GROUP5', 'GROUP14', and 'GROUP24'.\n        :type DhGroupName: str\n        :param IKESaLifetimeSeconds: IKE SA lifetime (in sec). Value range: 60-604800\n        :type IKESaLifetimeSeconds: int\n        :param IKEVersion: IKE version\n        :type IKEVersion: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPSECOptionsSpecification(AbstractModel):
    """IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud.

    """

    def __init__(self):
        """
        :param EncryptAlgorithm: Encryption algorithm. Valid values: `3DES-CBC`, `AES-CBC-128`, `AES-CBC-192`, `AES-CBC-256`, `DES-CBC`, `SM4`, and `NULL`; default value: `AES-CBC-128`.\n        :type EncryptAlgorithm: str\n        :param IntegrityAlgorith: Authentication algorithm. Valid values: `MD5`, `SHA1` and `SHA-256`; default value: `SHA1`.\n        :type IntegrityAlgorith: str\n        :param IPSECSaLifetimeSeconds: IPsec SA lifetime (in sec). Value range: 180-604800\n        :type IPSECSaLifetimeSeconds: int\n        :param PfsDhGroup: PFS. Available value: 'NULL', 'DH-GROUP1', 'DH-GROUP2', 'DH-GROUP5', 'DH-GROUP14', and 'DH-GROUP24'. Default is NULL.\n        :type PfsDhGroup: str\n        :param IPSECSaLifetimeTraffic: IPsec SA lifetime (in KB). Value range: 2560-604800\n        :type IPSECSaLifetimeTraffic: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateDirectConnectGatewayRequest(AbstractModel):
    """InquirePriceCreateDirectConnectGateway request structure.

    """


class InquirePriceCreateDirectConnectGatewayResponse(AbstractModel):
    """InquirePriceCreateDirectConnectGateway response structure.

    """

    def __init__(self):
        """
        :param TotalCost: Standard access fee for a direct connect gateway
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TotalCost: int\n        :param RealTotalCost: Actual access fee for a direct connect gateway
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type RealTotalCost: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InternetMaxBandwidthOut: The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps.\n        :type InternetMaxBandwidthOut: int\n        :param InstanceChargeType: The VPN gateway billing mode. PREPAID: prepaid means monthly subscription. POSTPAID_BY_HOUR: postpaid means pay-as-you-go. Default: POSTPAID_BY_HOUR. If prepaid mode is specified, the `InstanceChargePrepaid` parameter must be entered.\n        :type InstanceChargeType: str\n        :param InstanceChargePrepaid: Parameter settings for prepaid billing mode, also known as monthly subscription. This parameter can specify the purchase period and other attributes such as auto-renewal. This parameter is mandatory for prepaid instances.\n        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`\n        """
        self.InternetMaxBandwidthOut = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateVpnGatewayResponse(AbstractModel):
    """InquiryPriceCreateVpnGateway response structure.

    """

    def __init__(self):
        """
        :param Price: Product price.\n        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param InstanceChargePrepaid: Specifies the purchased validity period, whether to enable auto-renewal. This parameter is required for monthly-subscription instances.\n        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`\n        """
        self.VpnGatewayId = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewVpnGatewayResponse(AbstractModel):
    """InquiryPriceRenewVpnGateway response structure.

    """

    def __init__(self):
        """
        :param Price: Product price.\n        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param InternetMaxBandwidthOut: The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps.\n        :type InternetMaxBandwidthOut: int\n        """
        self.VpnGatewayId = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetVpnGatewayInternetMaxBandwidth response structure.

    """

    def __init__(self):
        """
        :param Price: Product price.\n        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Period: Purchased usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36].\n        :type Period: int\n        :param RenewFlag: Auto-renewal ID. Value range: NOTIFY_AND_AUTO_RENEW: notify expiry and renew automatically, NOTIFY_AND_MANUAL_RENEW: notify expiry but do not renew automatically. The default is NOTIFY_AND_MANUAL_RENEW\n        :type RenewFlag: str\n        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStatistic(AbstractModel):
    """Statistics used to describe the instance

    """

    def __init__(self):
        """
        :param InstanceType: Type of instance\n        :type InstanceType: str\n        :param InstanceCount: Number of instances\n        :type InstanceCount: int\n        """
        self.InstanceType = None
        self.InstanceCount = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpField(AbstractModel):
    """IP information to be queried

    """

    def __init__(self):
        """
        :param Country: Country/region of the IP\n        :type Country: bool\n        :param Province: Province/municipality/state of the IP\n        :type Province: bool\n        :param City: City of the IP\n        :type City: bool\n        :param Region: City district of the IP\n        :type Region: bool\n        :param Isp: Access ISP field\n        :type Isp: bool\n        :param AsName: ISP backbone network’s AS field\n        :type AsName: bool\n        :param AsId: Backbone AS ID\n        :type AsId: bool\n        :param Comment: Comment\n        :type Comment: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpGeolocationInfo(AbstractModel):
    """IP location

    """

    def __init__(self):
        """
        :param Country: Country/region
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Country: str\n        :param Province: Province- or municipality-level administrative region
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Province: str\n        :param City: Municipal administrative region
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type City: str\n        :param Region: Urban area
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Region: str\n        :param Isp: Access ISP
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Isp: str\n        :param AsName: ISP backbone network’s AS name
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AsName: str\n        :param AsId: ISP backbone network’s AS ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AsId: str\n        :param Comment: Comment. The APN value of mobile users is entered currently. If there is no APN attribute, this is `null`.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Comment: str\n        :param AddressIp: IP address
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AddressIp: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Address(AbstractModel):
    """`IPv6` address information.

    """

    def __init__(self):
        """
        :param Address: `IPv6` address, such as `3402:4e00:20:100:0:8cd9:2a67:71f3`\n        :type Address: str\n        :param Primary: Whether it is a primary `IP`.\n        :type Primary: bool\n        :param AddressId: The `ID` of the `EIP` instance, such as `eip-hxlqja90`.\n        :type AddressId: str\n        :param Description: Message description\n        :type Description: str\n        :param IsWanIpBlocked: Whether the public IP is blocked.\n        :type IsWanIpBlocked: bool\n        :param State: `IPv6` address status:
<li>`PENDING`: Creating</li>
<li>`MIGRATING`: Migrating</li>
<li>`DELETING`: Deleting</li>
<li>`AVAILABLE`: Available</li>\n        :type State: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6SubnetCidrBlock(AbstractModel):
    """IPv6 subnet IP range object.

    """

    def __init__(self):
        """
        :param SubnetId: The `ID` of the subnet instance, such as `subnet-pxir56ns`.\n        :type SubnetId: str\n        :param Ipv6CidrBlock: The `IPv6` subnet IP range, such as `3402:4e00:20:1001::/64`\n        :type Ipv6CidrBlock: str\n        """
        self.SubnetId = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    """The pricing information of a single billing item

    """

    def __init__(self):
        """
        :param UnitPrice: The pay-as-you-go billing method. Unit: CNY.\n        :type UnitPrice: float\n        :param ChargeUnit: Pay-as-you-go billing method. Value Range: HOUR: Indicates billing by the hour. Scenarios using this hourly billing unit include: Instances postpaid on an hourly basis (POSTPAID_BY_HOUR), and bandwidth postpaid on an hourly basis (BANDWIDTH_POSTPAID_BY_HOUR). GB: Indicates billing on a per-GB basis. Scenarios using this billing unit include: Traffic postpaid on an hourly basis (TRAFFIC_POSTPAID_BY_HOUR).\n        :type ChargeUnit: str\n        :param OriginalPrice: Original price of the prepaid product. Unit: CNY.\n        :type OriginalPrice: float\n        :param DiscountPrice: Discount price of the prepaid product. Unit: CNY.\n        :type DiscountPrice: float\n        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalGateway(AbstractModel):
    """Local gateway information

    """

    def __init__(self):
        """
        :param CdcId: CDC instance ID\n        :type CdcId: str\n        :param VpcId: VPC instance ID\n        :type VpcId: str\n        :param UniqLocalGwId: Local gateway instance ID\n        :type UniqLocalGwId: str\n        :param LocalGatewayName: Local gateway name\n        :type LocalGatewayName: str\n        :param LocalGwIp: Local gateway IP\n        :type LocalGwIp: str\n        :param CreateTime: Creation time of the local gateway\n        :type CreateTime: str\n        """
        self.CdcId = None
        self.VpcId = None
        self.UniqLocalGwId = None
        self.LocalGatewayName = None
        self.LocalGwIp = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.CdcId = params.get("CdcId")
        self.VpcId = params.get("VpcId")
        self.UniqLocalGwId = params.get("UniqLocalGwId")
        self.LocalGatewayName = params.get("LocalGatewayName")
        self.LocalGwIp = params.get("LocalGwIp")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateNetworkInterfaceRequest(AbstractModel):
    """MigrateNetworkInterface request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.\n        :type NetworkInterfaceId: str\n        :param SourceInstanceId: The ID of the CVM bound to the ENI, such as `ins-r8hr2upy`.\n        :type SourceInstanceId: str\n        :param DestinationInstanceId: ID of the destination CVM instance to be migrated.\n        :type DestinationInstanceId: str\n        :param AttachType: ENI mount method. Valid values: 0: standard; 1: extension; default value: 0\n        :type AttachType: int\n        """
        self.NetworkInterfaceId = None
        self.SourceInstanceId = None
        self.DestinationInstanceId = None
        self.AttachType = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.SourceInstanceId = params.get("SourceInstanceId")
        self.DestinationInstanceId = params.get("DestinationInstanceId")
        self.AttachType = params.get("AttachType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateNetworkInterfaceResponse(AbstractModel):
    """MigrateNetworkInterface response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MigratePrivateIpAddressRequest(AbstractModel):
    """MigratePrivateIpAddress request structure.

    """

    def __init__(self):
        """
        :param SourceNetworkInterfaceId: ID of the ENI instance bound with the private IP, such as `eni-m6dyj72l`.\n        :type SourceNetworkInterfaceId: str\n        :param DestinationNetworkInterfaceId: ID of the destination ENI instance to be migrated.\n        :type DestinationNetworkInterfaceId: str\n        :param PrivateIpAddress: The private IP to be migrated, such as 10.0.0.6.\n        :type PrivateIpAddress: str\n        """
        self.SourceNetworkInterfaceId = None
        self.DestinationNetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.SourceNetworkInterfaceId = params.get("SourceNetworkInterfaceId")
        self.DestinationNetworkInterfaceId = params.get("DestinationNetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigratePrivateIpAddressResponse(AbstractModel):
    """MigratePrivateIpAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressAttributeRequest(AbstractModel):
    """ModifyAddressAttribute request structure.

    """

    def __init__(self):
        """
        :param AddressId: The unique ID of the EIP, such as `eip-11112222`.\n        :type AddressId: str\n        :param AddressName: The EIP name after modification. The maximum length is 20 characters.\n        :type AddressName: str\n        :param EipDirectConnection: Whether the set EIP is a direct connection EIP. TRUE: yes. FALSE: no. Note that this parameter is available only to users who have activated the EIP direct connection function.\n        :type EipDirectConnection: str\n        """
        self.AddressId = None
        self.AddressName = None
        self.EipDirectConnection = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressName = params.get("AddressName")
        self.EipDirectConnection = params.get("EipDirectConnection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressAttributeResponse(AbstractModel):
    """ModifyAddressAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressInternetChargeTypeRequest(AbstractModel):
    """ModifyAddressInternetChargeType request structure.

    """

    def __init__(self):
        """
        :param AddressId: Unique EIP ID, such as "eip-xxxx"\n        :type AddressId: str\n        :param InternetChargeType: The target billing method. It can be `BANDWIDTH_PREPAID_BY_MONTH` or `TRAFFIC_POSTPAID_BY_HOUR`\n        :type InternetChargeType: str\n        :param InternetMaxBandwidthOut: The target bandwidth value\n        :type InternetMaxBandwidthOut: int\n        :param AddressChargePrepaid: Billing details of monthly-subscribed network bandwidth. This parameter is required if the target billing method is `BANDWIDTH_PREPAID_BY_MONTH`.\n        :type AddressChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.AddressChargePrepaid`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressInternetChargeTypeResponse(AbstractModel):
    """ModifyAddressInternetChargeType response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressTemplateAttributeRequest(AbstractModel):
    """ModifyAddressTemplateAttribute request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateId: IP address template instance ID, such as `ipm-mdunqeb6`.\n        :type AddressTemplateId: str\n        :param AddressTemplateName: IP address template name.\n        :type AddressTemplateName: str\n        :param Addresses: Address information, including IP, CIDR and IP address range.\n        :type Addresses: list of str\n        """
        self.AddressTemplateId = None
        self.AddressTemplateName = None
        self.Addresses = None


    def _deserialize(self, params):
        self.AddressTemplateId = params.get("AddressTemplateId")
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.Addresses = params.get("Addresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressTemplateAttributeResponse(AbstractModel):
    """ModifyAddressTemplateAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressTemplateGroupAttributeRequest(AbstractModel):
    """ModifyAddressTemplateGroupAttribute request structure.

    """

    def __init__(self):
        """
        :param AddressTemplateGroupId: IP address template group instance ID, such as `ipmg-2uw6ujo6`.\n        :type AddressTemplateGroupId: str\n        :param AddressTemplateGroupName: IP address template group name.\n        :type AddressTemplateGroupName: str\n        :param AddressTemplateIds: IP address template instance ID, such as `ipm-mdunqeb6`.\n        :type AddressTemplateIds: list of str\n        """
        self.AddressTemplateGroupId = None
        self.AddressTemplateGroupName = None
        self.AddressTemplateIds = None


    def _deserialize(self, params):
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateIds = params.get("AddressTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressTemplateGroupAttributeResponse(AbstractModel):
    """ModifyAddressTemplateGroupAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressesBandwidthRequest(AbstractModel):
    """ModifyAddressesBandwidth request structure.

    """

    def __init__(self):
        """
        :param AddressIds: List of EIP IDs, such as “eip-xxxx”.\n        :type AddressIds: list of str\n        :param InternetMaxBandwidthOut: Target bandwidth value adjustment\n        :type InternetMaxBandwidthOut: int\n        :param StartTime: (Disused) The start time of the monthly bandwidth subscription\n        :type StartTime: str\n        :param EndTime: (Disused) The end time of the monthly bandwidth subscription\n        :type EndTime: str\n        """
        self.AddressIds = None
        self.InternetMaxBandwidthOut = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressesBandwidthResponse(AbstractModel):
    """ModifyAddressesBandwidth response structure.

    """

    def __init__(self):
        """
        :param TaskId: The async task ID. You can use the [DescribeTaskResult](https://intl.cloud.tencent.com/document/api/215/36271?from_cn_redirect=1) API to query the task status.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param VpcId: `VPC` instance `ID`, e.g. `vpc-6v2ht8q5`.\n        :type VpcId: str\n        :param NewCidrBlocks: Array of the secondary CIDR blocks to be added, such as ["10.0.0.0/16", "172.16.0.0/16"]. Either or both of `NewCidrBlocks` and `OldCidrBlocks` must be specified.\n        :type NewCidrBlocks: list of str\n        :param OldCidrBlocks: Array of the secondary CIDR blocks to be deleted, such as ["10.0.0.0/16", "172.16.0.0/16"]. Either or both of `NewCidrBlocks` and `OldCidrBlocks` must be specified.\n        :type OldCidrBlocks: list of str\n        """
        self.VpcId = None
        self.NewCidrBlocks = None
        self.OldCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NewCidrBlocks = params.get("NewCidrBlocks")
        self.OldCidrBlocks = params.get("OldCidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAssistantCidrResponse(AbstractModel):
    """ModifyAssistantCidr response structure.

    """

    def __init__(self):
        """
        :param AssistantCidrSet: A set of secondary CIDR blocks.
Note: This field may return null, indicating that no valid value was found.\n        :type AssistantCidrSet: list of AssistantCidr\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param BandwidthPackageId: The unique ID of the bandwidth package.\n        :type BandwidthPackageId: str\n        :param BandwidthPackageName: The name of the bandwidth package.\n        :type BandwidthPackageName: str\n        :param ChargeType: The billing mode of the bandwidth package.\n        :type ChargeType: str\n        """
        self.BandwidthPackageId = None
        self.BandwidthPackageName = None
        self.ChargeType = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.ChargeType = params.get("ChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBandwidthPackageAttributeResponse(AbstractModel):
    """ModifyBandwidthPackageAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnAttachedInstancesAttributeRequest(AbstractModel):
    """ModifyCcnAttachedInstancesAttribute request structure.

    """

    def __init__(self):
        """
        :param CcnId: CCN instance ID in the format of `ccn-f49l6u0z`\n        :type CcnId: str\n        :param Instances: List of associated network instances\n        :type Instances: list of CcnInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCcnAttachedInstancesAttributeResponse(AbstractModel):
    """ModifyCcnAttachedInstancesAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnAttributeRequest(AbstractModel):
    """ModifyCcnAttribute request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        :param CcnName: The name of the CCN. The maximum length is 60 characters.\n        :type CcnName: str\n        :param CcnDescription: The description of the CCN. The maximum length is 100 characters.\n        :type CcnDescription: str\n        """
        self.CcnId = None
        self.CcnName = None
        self.CcnDescription = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCcnAttributeResponse(AbstractModel):
    """ModifyCcnAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnRegionBandwidthLimitsTypeRequest(AbstractModel):
    """ModifyCcnRegionBandwidthLimitsType request structure.

    """

    def __init__(self):
        """
        :param CcnId: CCN instance ID.\n        :type CcnId: str\n        :param BandwidthLimitType: CCN bandwidth limit type. INTER_REGION_LIMIT: limit between regions. OUTER_REGION_LIMIT: region egress limit.\n        :type BandwidthLimitType: str\n        """
        self.CcnId = None
        self.BandwidthLimitType = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.BandwidthLimitType = params.get("BandwidthLimitType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCcnRegionBandwidthLimitsTypeResponse(AbstractModel):
    """ModifyCcnRegionBandwidthLimitsType response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCustomerGatewayAttributeRequest(AbstractModel):
    """ModifyCustomerGatewayAttribute request structure.

    """

    def __init__(self):
        """
        :param CustomerGatewayId: The ID of the customer gateway, such as `cgw-2wqq41m9`. You can query the customer gateway by using the `DescribeCustomerGateways` API.\n        :type CustomerGatewayId: str\n        :param CustomerGatewayName: Customer gateway can be named freely, but the maximum length is 60 characters.\n        :type CustomerGatewayName: str\n        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomerGatewayAttributeResponse(AbstractModel):
    """ModifyCustomerGatewayAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectGatewayAttributeRequest(AbstractModel):
    """ModifyDirectConnectGatewayAttribute request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: The unique ID of the direct connect gateway, such as `dcg-9o233uri`.\n        :type DirectConnectGatewayId: str\n        :param DirectConnectGatewayName: The direct connect gateway name. You can enter any name within 60 characters.\n        :type DirectConnectGatewayName: str\n        :param CcnRouteType: The CCN route-learning type. Valid values: `BGP` (Automatic learning), `STATIC` (Static, that is, user-configured). You can only modify `CcnRouteType` for a CCN direct connect gateway with BGP enabled.\n        :type CcnRouteType: str\n        :param ModeType: CCN route publishing method. Valid values: `standard` and `exquisite`. You can only modify `ModeType` for a CCN direct connect gateway.\n        :type ModeType: str\n        """
        self.DirectConnectGatewayId = None
        self.DirectConnectGatewayName = None
        self.CcnRouteType = None
        self.ModeType = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.CcnRouteType = params.get("CcnRouteType")
        self.ModeType = params.get("ModeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectGatewayAttributeResponse(AbstractModel):
    """ModifyDirectConnectGatewayAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyFlowLogAttributeRequest(AbstractModel):
    """ModifyFlowLogAttribute request structure.

    """

    def __init__(self):
        """
        :param VpcId: ID of the VPC instance\n        :type VpcId: str\n        :param FlowLogId: The unique ID of the flow log.\n        :type FlowLogId: str\n        :param FlowLogName: The name of the flow log.\n        :type FlowLogName: str\n        :param FlowLogDescription: The description of the flow log.\n        :type FlowLogDescription: str\n        """
        self.VpcId = None
        self.FlowLogId = None
        self.FlowLogName = None
        self.FlowLogDescription = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        self.FlowLogName = params.get("FlowLogName")
        self.FlowLogDescription = params.get("FlowLogDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFlowLogAttributeResponse(AbstractModel):
    """ModifyFlowLogAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
ID of VPN gateway instance, e.g. `vpn-ltjahce6`.\n        :type GatewayId: str\n        :param Bandwidth: Bandwidth limit value.\n        :type Bandwidth: int\n        :param IpAddresses: CVM private IP addresses with limited bandwidth.\n        :type IpAddresses: list of str\n        """
        self.GatewayId = None
        self.Bandwidth = None
        self.IpAddresses = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.Bandwidth = params.get("Bandwidth")
        self.IpAddresses = params.get("IpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGatewayFlowQosResponse(AbstractModel):
    """ModifyGatewayFlowQos response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHaVipAttributeRequest(AbstractModel):
    """ModifyHaVipAttribute request structure.

    """

    def __init__(self):
        """
        :param HaVipId: The unique `ID` of the `HAVIP`, such as `havip-9o233uri`.\n        :type HaVipId: str\n        :param HaVipName: `HAVIP` can be named freely, but the maximum length is 60 characters.\n        :type HaVipName: str\n        """
        self.HaVipId = None
        self.HaVipName = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.HaVipName = params.get("HaVipName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHaVipAttributeResponse(AbstractModel):
    """ModifyHaVipAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIpv6AddressesAttributeRequest(AbstractModel):
    """ModifyIpv6AddressesAttribute request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The `ID` of the ENI instance, such as `eni-m6dyj72l`.\n        :type NetworkInterfaceId: str\n        :param Ipv6Addresses: The information of the specified private `IPv6` addresses.\n        :type Ipv6Addresses: list of Ipv6Address\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIpv6AddressesAttributeResponse(AbstractModel):
    """ModifyIpv6AddressesAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLocalGatewayRequest(AbstractModel):
    """ModifyLocalGateway request structure.

    """

    def __init__(self):
        """
        :param LocalGatewayName: Local gateway name\n        :type LocalGatewayName: str\n        :param CdcId: CDC instance ID\n        :type CdcId: str\n        :param LocalGatewayId: Local gateway instance ID\n        :type LocalGatewayId: str\n        :param VpcId: VPC instance ID\n        :type VpcId: str\n        """
        self.LocalGatewayName = None
        self.CdcId = None
        self.LocalGatewayId = None
        self.VpcId = None


    def _deserialize(self, params):
        self.LocalGatewayName = params.get("LocalGatewayName")
        self.CdcId = params.get("CdcId")
        self.LocalGatewayId = params.get("LocalGatewayId")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLocalGatewayResponse(AbstractModel):
    """ModifyLocalGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatGatewayAttributeRequest(AbstractModel):
    """ModifyNatGatewayAttribute request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.\n        :type NatGatewayId: str\n        :param NatGatewayName: The NAT gateway name, such as `test_nat`.\n        :type NatGatewayName: str\n        :param InternetMaxBandwidthOut: The maximum outbound bandwidth of the NAT gateway. Unit: Mbps.\n        :type InternetMaxBandwidthOut: int\n        :param ModifySecurityGroup: Whether to modify the security group bound to the NAT Gateway\n        :type ModifySecurityGroup: bool\n        :param SecurityGroupIds: The final security groups bound to the NAT Gateway, such as `['sg-1n232323', 'sg-o4242424']`. An empty list indicates that all the security groups have been deleted.\n        :type SecurityGroupIds: list of str\n        """
        self.NatGatewayId = None
        self.NatGatewayName = None
        self.InternetMaxBandwidthOut = None
        self.ModifySecurityGroup = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.NatGatewayName = params.get("NatGatewayName")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.ModifySecurityGroup = params.get("ModifySecurityGroup")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatGatewayAttributeResponse(AbstractModel):
    """ModifyNatGatewayAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """ModifyNatGatewayDestinationIpPortTranslationNatRule request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT gateway, such as `nat-df45454`.\n        :type NatGatewayId: str\n        :param SourceNatRule: The port forwarding rule of the source NAT gateway.\n        :type SourceNatRule: :class:`tencentcloud.vpc.v20170312.models.DestinationIpPortTranslationNatRule`\n        :param DestinationNatRule: The port forwarding rule of the destination NAT gateway.\n        :type DestinationNatRule: :class:`tencentcloud.vpc.v20170312.models.DestinationIpPortTranslationNatRule`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """ModifyNatGatewayDestinationIpPortTranslationNatRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatGatewaySourceIpTranslationNatRuleRequest(AbstractModel):
    """ModifyNatGatewaySourceIpTranslationNatRule request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: The ID of the NAT Gateway, such as `nat-df453454`\n        :type NatGatewayId: str\n        :param SourceIpTranslationNatRule: The SNAT forwarding rule of the NAT Gateway\n        :type SourceIpTranslationNatRule: :class:`tencentcloud.vpc.v20170312.models.SourceIpTranslationNatRule`\n        """
        self.NatGatewayId = None
        self.SourceIpTranslationNatRule = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("SourceIpTranslationNatRule") is not None:
            self.SourceIpTranslationNatRule = SourceIpTranslationNatRule()
            self.SourceIpTranslationNatRule._deserialize(params.get("SourceIpTranslationNatRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatGatewaySourceIpTranslationNatRuleResponse(AbstractModel):
    """ModifyNatGatewaySourceIpTranslationNatRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetDetectRequest(AbstractModel):
    """ModifyNetDetect request structure.

    """

    def __init__(self):
        """
        :param NetDetectId: The ID of a network detection instance, such as `netd-12345678`.\n        :type NetDetectId: str\n        :param NetDetectName: The name of a network detection instance. The maximum length is 60 characters.\n        :type NetDetectName: str\n        :param DetectDestinationIp: The array of detection destination IPv4 addresses, which contains at most two IP addresses.\n        :type DetectDestinationIp: list of str\n        :param NextHopType: The type of the next hop. Currently supported types are:
VPN: VPN gateway;
DIRECTCONNECT: direct connect gateway;
PEERCONNECTION: peering connection;
NAT: NAT gateway;
NORMAL_CVM: normal CVM.\n        :type NextHopType: str\n        :param NextHopDestination: The next-hop destination gateway. The value is related to NextHopType.
If NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.
If NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.
If NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.
If NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.
If NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12.\n        :type NextHopDestination: str\n        :param NetDetectDescription: Network detection description.\n        :type NetDetectDescription: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetDetectResponse(AbstractModel):
    """ModifyNetDetect response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkAclAttributeRequest(AbstractModel):
    """ModifyNetworkAclAttribute request structure.

    """

    def __init__(self):
        """
        :param NetworkAclId: Network ACL instance ID. Example: acl-12345678.\n        :type NetworkAclId: str\n        :param NetworkAclName: Name of the network ACL. The maximum length is 60 bytes.\n        :type NetworkAclName: str\n        """
        self.NetworkAclId = None
        self.NetworkAclName = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.NetworkAclName = params.get("NetworkAclName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkAclAttributeResponse(AbstractModel):
    """ModifyNetworkAclAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkAclEntriesRequest(AbstractModel):
    """ModifyNetworkAclEntries request structure.

    """

    def __init__(self):
        """
        :param NetworkAclId: Network ACL instance ID. Example: acl-12345678.\n        :type NetworkAclId: str\n        :param NetworkAclEntrySet: Network ACL rule set.\n        :type NetworkAclEntrySet: :class:`tencentcloud.vpc.v20170312.models.NetworkAclEntrySet`\n        """
        self.NetworkAclId = None
        self.NetworkAclEntrySet = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        if params.get("NetworkAclEntrySet") is not None:
            self.NetworkAclEntrySet = NetworkAclEntrySet()
            self.NetworkAclEntrySet._deserialize(params.get("NetworkAclEntrySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkAclEntriesResponse(AbstractModel):
    """ModifyNetworkAclEntries response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkInterfaceAttributeRequest(AbstractModel):
    """ModifyNetworkInterfaceAttribute request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-pxir56ns`.\n        :type NetworkInterfaceId: str\n        :param NetworkInterfaceName: The name of the ENI. The maximum length is 60 characters.\n        :type NetworkInterfaceName: str\n        :param NetworkInterfaceDescription: ENI description can be named freely, but the maximum length is 60 characters.\n        :type NetworkInterfaceDescription: str\n        :param SecurityGroupIds: The specified security groups to be bound with, such as ['sg-1dd51d'].\n        :type SecurityGroupIds: list of str\n        """
        self.NetworkInterfaceId = None
        self.NetworkInterfaceName = None
        self.NetworkInterfaceDescription = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkInterfaceAttributeResponse(AbstractModel):
    """ModifyNetworkInterfaceAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateIpAddressesAttributeRequest(AbstractModel):
    """ModifyPrivateIpAddressesAttribute request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddresses: The specified private IP information.\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateIpAddressesAttributeResponse(AbstractModel):
    """ModifyPrivateIpAddressesAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRouteTableAttributeRequest(AbstractModel):
    """ModifyRouteTableAttribute request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.\n        :type RouteTableId: str\n        :param RouteTableName: Route table name.\n        :type RouteTableName: str\n        """
        self.RouteTableId = None
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRouteTableAttributeResponse(AbstractModel):
    """ModifyRouteTableAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupAttributeRequest(AbstractModel):
    """ModifySecurityGroupAttribute request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.\n        :type SecurityGroupId: str\n        :param GroupName: Security group can be named freely, but cannot exceed 60 characters.\n        :type GroupName: str\n        :param GroupDescription: The remarks for the security group. The maximum length is 100 characters.\n        :type GroupDescription: str\n        """
        self.SecurityGroupId = None
        self.GroupName = None
        self.GroupDescription = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupAttributeResponse(AbstractModel):
    """ModifySecurityGroupAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupPoliciesRequest(AbstractModel):
    """ModifySecurityGroupPolicies request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: The security group policy set. SecurityGroupPolicySet object must specify new egress and ingress policies at the same time. SecurityGroupPolicy object does not support custom index (PolicyIndex).\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        :param SortPolicys: Whether the security group rule is sorted. Default value: False. If it is set to `True`, security group rules will be strictly sorted according to the sequence specified in the `SecurityGroupPolicySet` parameter. Manual entry may cause omission, so we recommend sorting security group rules in the console.\n        :type SortPolicys: bool\n        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None
        self.SortPolicys = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self.SortPolicys = params.get("SortPolicys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupPoliciesResponse(AbstractModel):
    """ModifySecurityGroupPolicies response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyServiceTemplateAttributeRequest(AbstractModel):
    """ModifyServiceTemplateAttribute request structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateId: Protocol port template instance ID, such as `ppm-529nwwj8`.\n        :type ServiceTemplateId: str\n        :param ServiceTemplateName: Protocol port template name.\n        :type ServiceTemplateName: str\n        :param Services: It supports single port, multiple ports, consecutive ports and all ports. Supported protocols include TCP, UDP, ICMP, and GRE.\n        :type Services: list of str\n        """
        self.ServiceTemplateId = None
        self.ServiceTemplateName = None
        self.Services = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.Services = params.get("Services")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceTemplateAttributeResponse(AbstractModel):
    """ModifyServiceTemplateAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyServiceTemplateGroupAttributeRequest(AbstractModel):
    """ModifyServiceTemplateGroupAttribute request structure.

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: The protocol port template group instance ID, such as `ppmg-ei8hfd9a`.\n        :type ServiceTemplateGroupId: str\n        :param ServiceTemplateGroupName: Protocol port template group name.\n        :type ServiceTemplateGroupName: str\n        :param ServiceTemplateIds: Instance ID of the protocol port template, such as `ppm-4dw6agho`.\n        :type ServiceTemplateIds: list of str\n        """
        self.ServiceTemplateGroupId = None
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIds = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIds = params.get("ServiceTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceTemplateGroupAttributeResponse(AbstractModel):
    """ModifyServiceTemplateGroupAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubnetAttributeRequest(AbstractModel):
    """ModifySubnetAttribute request structure.

    """

    def __init__(self):
        """
        :param SubnetId: Subnet instance ID, such as `subnet-pxir56ns`.\n        :type SubnetId: str\n        :param SubnetName: The subnet name. The maximum length is 60 bytes.\n        :type SubnetName: str\n        :param EnableBroadcast: Whether the subnet has broadcast enabled.\n        :type EnableBroadcast: str\n        """
        self.SubnetId = None
        self.SubnetName = None
        self.EnableBroadcast = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.EnableBroadcast = params.get("EnableBroadcast")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubnetAttributeResponse(AbstractModel):
    """ModifySubnetAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcAttributeRequest(AbstractModel):
    """ModifyVpcAttribute request structure.

    """

    def __init__(self):
        """
        :param VpcId: Security group can be named freely, but cannot exceed 60 characters.\n        :type VpcId: str\n        :param VpcName: VPC can be named freely, but the maximum length is 60 characters.\n        :type VpcName: str\n        :param EnableMulticast: Whether multicast is enabled. `true`: Enabled. `false`: Off.\n        :type EnableMulticast: str\n        :param DnsServers: DNS address. A maximum of 4 addresses is supported. The first one is primary server by default, and the rest are secondary servers.\n        :type DnsServers: list of str\n        :param DomainName: Domain name\n        :type DomainName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcAttributeResponse(AbstractModel):
    """ModifyVpcAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcEndPointAttributeRequest(AbstractModel):
    """ModifyVpcEndPointAttribute request structure.

    """

    def __init__(self):
        """
        :param EndPointId: Endpoint ID\n        :type EndPointId: str\n        :param EndPointName: Endpoint name\n        :type EndPointName: str\n        :param SecurityGroupIds: List of security group IDs\n        :type SecurityGroupIds: list of str\n        """
        self.EndPointId = None
        self.EndPointName = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.EndPointId = params.get("EndPointId")
        self.EndPointName = params.get("EndPointName")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcEndPointAttributeResponse(AbstractModel):
    """ModifyVpcEndPointAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcEndPointServiceAttributeRequest(AbstractModel):
    """ModifyVpcEndPointServiceAttribute request structure.

    """

    def __init__(self):
        """
        :param EndPointServiceId: Endpoint service ID\n        :type EndPointServiceId: str\n        :param VpcId: VPC ID\n        :type VpcId: str\n        :param EndPointServiceName: Endpoint service name\n        :type EndPointServiceName: str\n        :param AutoAcceptFlag: Whether to automatically accept\n        :type AutoAcceptFlag: bool\n        :param ServiceInstanceId: Real server ID in the format of `lb-xxx`.\n        :type ServiceInstanceId: str\n        """
        self.EndPointServiceId = None
        self.VpcId = None
        self.EndPointServiceName = None
        self.AutoAcceptFlag = None
        self.ServiceInstanceId = None


    def _deserialize(self, params):
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.VpcId = params.get("VpcId")
        self.EndPointServiceName = params.get("EndPointServiceName")
        self.AutoAcceptFlag = params.get("AutoAcceptFlag")
        self.ServiceInstanceId = params.get("ServiceInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcEndPointServiceAttributeResponse(AbstractModel):
    """ModifyVpcEndPointServiceAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcEndPointServiceWhiteListRequest(AbstractModel):
    """ModifyVpcEndPointServiceWhiteList request structure.

    """

    def __init__(self):
        """
        :param UserUin: User UIN\n        :type UserUin: str\n        :param EndPointServiceId: Endpoint service ID\n        :type EndPointServiceId: str\n        :param Description: Allowlist description\n        :type Description: str\n        """
        self.UserUin = None
        self.EndPointServiceId = None
        self.Description = None


    def _deserialize(self, params):
        self.UserUin = params.get("UserUin")
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcEndPointServiceWhiteListResponse(AbstractModel):
    """ModifyVpcEndPointServiceWhiteList response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnConnectionAttributeRequest(AbstractModel):
    """ModifyVpnConnectionAttribute request structure.

    """

    def __init__(self):
        """
        :param VpnConnectionId: The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`.\n        :type VpnConnectionId: str\n        :param VpnConnectionName: VPN tunnel can be named freely, but the maximum length is 60 characters.\n        :type VpnConnectionName: str\n        :param PreShareKey: The pre-shared key.\n        :type PreShareKey: str\n        :param SecurityPolicyDatabases: The SPD policy group, for example: {"10.0.0.5/24":["172.123.10.5/16"]}. 10.0.0.5/24 is the VPC internal IP range, and 172.123.10.5/16 is the IDC IP range. The user specifies the IP range in the VPC that can communicate with the IP range in the IDC.\n        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase\n        :param IKEOptionsSpecification: IKE (Internet Key Exchange) configuration. IKE comes with a self-protection mechanism. The network security protocol is configured by the user.\n        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`\n        :param IPSECOptionsSpecification: IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud.\n        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`\n        :param EnableHealthCheck: Whether to enable the tunnel health check.\n        :type EnableHealthCheck: bool\n        :param HealthCheckLocalIp: Local IP address for the tunnel health check\n        :type HealthCheckLocalIp: str\n        :param HealthCheckRemoteIp: Peer IP address for the tunnel health check\n        :type HealthCheckRemoteIp: str\n        """
        self.VpnConnectionId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None
        self.EnableHealthCheck = None
        self.HealthCheckLocalIp = None
        self.HealthCheckRemoteIp = None


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
        self.EnableHealthCheck = params.get("EnableHealthCheck")
        self.HealthCheckLocalIp = params.get("HealthCheckLocalIp")
        self.HealthCheckRemoteIp = params.get("HealthCheckRemoteIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpnConnectionAttributeResponse(AbstractModel):
    """ModifyVpnConnectionAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayAttributeRequest(AbstractModel):
    """ModifyVpnGatewayAttribute request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param VpnGatewayName: The VPN gateway name. The maximum length is 60 bytes.\n        :type VpnGatewayName: str\n        :param InstanceChargeType: VPN gateway billing mode. Currently, only the conversion of prepaid (monthly subscription) to postpaid (that is, pay-as-you-go) is supported. That is, the parameters only supports POSTPAID_BY_HOUR.\n        :type InstanceChargeType: str\n        """
        self.VpnGatewayId = None
        self.VpnGatewayName = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpnGatewayAttributeResponse(AbstractModel):
    """ModifyVpnGatewayAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayCcnRoutesRequest(AbstractModel):
    """ModifyVpnGatewayCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param Routes: The CCN route (IDC IP range) list.\n        :type Routes: list of VpngwCcnRoutes\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpnGatewayCcnRoutesResponse(AbstractModel):
    """ModifyVpnGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayRoutesRequest(AbstractModel):
    """ModifyVpnGatewayRoutes request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN gateway ID\n        :type VpnGatewayId: str\n        :param Routes: Route parameters to modify\n        :type Routes: list of VpnGatewayRouteModify\n        """
        self.VpnGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpnGatewayRouteModify()
                obj._deserialize(item)
                self.Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpnGatewayRoutesResponse(AbstractModel):
    """ModifyVpnGatewayRoutes response structure.

    """

    def __init__(self):
        """
        :param Routes: Route information of the VPN gateway
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Routes: list of VpnGatewayRoute\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Routes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpnGatewayRoute()
                obj._deserialize(item)
                self.Routes.append(obj)
        self.RequestId = params.get("RequestId")


class NatGateway(AbstractModel):
    """NAT gateway object.

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT gateway ID.\n        :type NatGatewayId: str\n        :param NatGatewayName: NAT gateway name.\n        :type NatGatewayName: str\n        :param CreatedTime: NAT gateway creation time.\n        :type CreatedTime: str\n        :param State: The status of the NAT gateway.
 'PENDING': Creating, 'DELETING': Deleting, 'AVAILABLE': Operating, 'UPDATING': Upgrading,
‘FAILED’: Failed.\n        :type State: str\n        :param InternetMaxBandwidthOut: The maximum outbound bandwidth of the gateway. Unit: Mbps.\n        :type InternetMaxBandwidthOut: int\n        :param MaxConcurrentConnection: The concurrent connections cap of the gateway.\n        :type MaxConcurrentConnection: int\n        :param PublicIpAddressSet: The public IP object array of the bound NAT gateway.\n        :type PublicIpAddressSet: list of NatGatewayAddress\n        :param NetworkState: The NAT gateway status. `AVAILABLE`: Operating, `UNAVAILABLE`: Unavailable, `INSUFFICIENT`: Account is in arrears and the service is suspended.\n        :type NetworkState: str\n        :param DestinationIpPortTranslationNatRuleSet: The port forwarding rules of the NAT gateway.\n        :type DestinationIpPortTranslationNatRuleSet: list of DestinationIpPortTranslationNatRule\n        :param VpcId: VPC instance ID.\n        :type VpcId: str\n        :param Zone: The availability zone in which the NAT gateway is located.\n        :type Zone: str\n        :param DirectConnectGatewayIds: IDs of direct connect gateway associated.\n        :type DirectConnectGatewayIds: list of str\n        :param SubnetId: Subnet ID.\n        :type SubnetId: str\n        :param TagSet: Tag key-value pair.\n        :type TagSet: list of Tag\n        :param SecurityGroupSet: The list of the security groups bound to the NAT Gateway
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SecurityGroupSet: list of str\n        :param SourceIpTranslationNatRuleSet: SNAT forwarding rule of the NAT Gateway.
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type SourceIpTranslationNatRuleSet: list of SourceIpTranslationNatRule\n        :param IsExclusive: Whether the NAT Gateway is dedicated.
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type IsExclusive: bool\n        :param ExclusiveGatewayBandwidth: Bandwidth of the gateway cluster where the dedicated NAT Gateway resides. Unit: Mbps. This field does not exist when the `IsExclusive` field is set to `false`.
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type ExclusiveGatewayBandwidth: int\n        """
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
        self.SecurityGroupSet = None
        self.SourceIpTranslationNatRuleSet = None
        self.IsExclusive = None
        self.ExclusiveGatewayBandwidth = None


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
        self.SecurityGroupSet = params.get("SecurityGroupSet")
        if params.get("SourceIpTranslationNatRuleSet") is not None:
            self.SourceIpTranslationNatRuleSet = []
            for item in params.get("SourceIpTranslationNatRuleSet"):
                obj = SourceIpTranslationNatRule()
                obj._deserialize(item)
                self.SourceIpTranslationNatRuleSet.append(obj)
        self.IsExclusive = params.get("IsExclusive")
        self.ExclusiveGatewayBandwidth = params.get("ExclusiveGatewayBandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatGatewayAddress(AbstractModel):
    """The EIP bound to the NAT gateway

    """

    def __init__(self):
        """
        :param AddressId: The unique ID of the Elastic IP (EIP), such as `eip-11112222`.\n        :type AddressId: str\n        :param PublicIpAddress: The public IP address, such as `123.121.34.33`.\n        :type PublicIpAddress: str\n        :param IsBlocked: The block status of the resource. `true` indicates the EIP is blocked. `false` indicates that the EIP is not blocked.\n        :type IsBlocked: bool\n        """
        self.AddressId = None
        self.PublicIpAddress = None
        self.IsBlocked = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.IsBlocked = params.get("IsBlocked")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatGatewayDestinationIpPortTranslationNatRule(AbstractModel):
    """The port forwarding rules of the NAT gateway

    """

    def __init__(self):
        """
        :param IpProtocol: Network protocol. Available choices: `TCP`, `UDP`.\n        :type IpProtocol: str\n        :param PublicIpAddress: EIP.\n        :type PublicIpAddress: str\n        :param PublicPort: Public port.\n        :type PublicPort: int\n        :param PrivateIpAddress: Private network address.\n        :type PrivateIpAddress: str\n        :param PrivatePort: Private network port.\n        :type PrivatePort: int\n        :param Description: NAT gateway forwarding rule description.\n        :type Description: str\n        :param NatGatewayId: NAT gateway ID.
Note: This field may return null, indicating no valid value.\n        :type NatGatewayId: str\n        :param VpcId: VPC ID.
Note: This field may return null, indicating no valid value.\n        :type VpcId: str\n        :param CreatedTime: The creation time of the NAT gateway forwarding rule.
Note: This field may return null, indicating no valid value.\n        :type CreatedTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetDetect(AbstractModel):
    """The network detection object.

    """

    def __init__(self):
        """
        :param VpcId: The ID of a VPC instance, such as `vpc-12345678`.\n        :type VpcId: str\n        :param VpcName: The name of a VPC instance.\n        :type VpcName: str\n        :param SubnetId: The ID of a subnet instance, such as subnet-12345678.\n        :type SubnetId: str\n        :param SubnetName: The name of a subnet instance.\n        :type SubnetName: str\n        :param NetDetectId: The ID of a network detection instance, such as netd-12345678.\n        :type NetDetectId: str\n        :param NetDetectName: The name of a network detection instance. The maximum length is 60 characters.\n        :type NetDetectName: str\n        :param DetectDestinationIp: The array of detection destination IPv4 addresses, which contains at most two IP addresses.\n        :type DetectDestinationIp: list of str\n        :param DetectSourceIp: The array of detection source IPv4 addresses automatically allocated by the system. The length is 2.\n        :type DetectSourceIp: list of str\n        :param NextHopType: Type of the next hop. Valid values:
VPN: VPN gateway;
DIRECTCONNECT: direct connect gateway;
PEERCONNECTION: peering connection;
NAT: NAT gateway;
NORMAL_CVM: normal CVM.
CCN: CCN gateway.\n        :type NextHopType: str\n        :param NextHopDestination: Next-hop destination gateway. Its value is determined by `NextHopType`.
If `NextHopType` is set to `VPN`, the parameter value is the VPN gateway ID, such as `vpngw-12345678`.
If `NextHopType` is set to `DIRECTCONNECT`, the parameter value is the direct connect gateway ID, such as `dcg-12345678`.
If `NextHopType` is set to `PEERCONNECTION`, the parameter value is the peering connection ID, such as `pcx-12345678`.
If `NextHopType` is set to `NAT`, the parameter value is the NAT gateway ID, such as `nat-12345678`.
If `NextHopType` is set to `NORMAL_CVM`, the parameter value is the IPv4 address of the CVM instance, such as `10.0.0.12`.
If `NextHopType` is set to `CCN`, the parameter value is the CCN ID, such as `ccn-12345678`.\n        :type NextHopDestination: str\n        :param NextHopName: The name of the next-hop gateway.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type NextHopName: str\n        :param NetDetectDescription: Network detection description.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type NetDetectDescription: str\n        :param CreateTime: The creation time.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type CreateTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetDetectIpState(AbstractModel):
    """The verification result of the network detection destination IP address.

    """

    def __init__(self):
        """
        :param DetectDestinationIp: The destination IPv4 address of network detection.\n        :type DetectDestinationIp: str\n        :param State: The detection result.
0: successful;
-1: no packet loss occurred during routing;
-2: packet loss occurred when outbound traffic is blocked by the ACL;
-3: packet loss occurred when inbound traffic is blocked by the ACL;
-4: other errors.\n        :type State: int\n        :param Delay: The latency. Unit: ms.\n        :type Delay: int\n        :param PacketLossRate: The packet loss rate.\n        :type PacketLossRate: int\n        """
        self.DetectDestinationIp = None
        self.State = None
        self.Delay = None
        self.PacketLossRate = None


    def _deserialize(self, params):
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.State = params.get("State")
        self.Delay = params.get("Delay")
        self.PacketLossRate = params.get("PacketLossRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetDetectState(AbstractModel):
    """The network detection verification result.

    """

    def __init__(self):
        """
        :param NetDetectId: The ID of a network detection instance, such as netd-12345678.\n        :type NetDetectId: str\n        :param NetDetectIpStateSet: The array of network detection destination IP verification results.\n        :type NetDetectIpStateSet: list of NetDetectIpState\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkAcl(AbstractModel):
    """Network ACL

    """

    def __init__(self):
        """
        :param VpcId: `ID` of the `VPC` instance.\n        :type VpcId: str\n        :param NetworkAclId: `ID` of the network ACL instance.\n        :type NetworkAclId: str\n        :param NetworkAclName: Name of the network ACL. The maximum length is 60 bytes.\n        :type NetworkAclName: str\n        :param CreatedTime: Creation time.\n        :type CreatedTime: str\n        :param SubnetSet: Array of subnets associated with the network ACL.\n        :type SubnetSet: list of Subnet\n        :param IngressEntries: Inbound rules of the network ACL.\n        :type IngressEntries: list of NetworkAclEntry\n        :param EgressEntries: Outbound rules of the network ACL.\n        :type EgressEntries: list of NetworkAclEntry\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkAclEntry(AbstractModel):
    """Network ACL rules.

    """

    def __init__(self):
        """
        :param ModifyTime: Modification time.\n        :type ModifyTime: str\n        :param Protocol: Protocol. Valid values: TCP, UDP, ICMP, ALL.\n        :type Protocol: str\n        :param Port: Port. Valid values: all, single port, range. When Protocol takes the value `ALL` or `ICMP`, Port cannot be specified.\n        :type Port: str\n        :param CidrBlock: IP range or IP address (mutually exclusive).\n        :type CidrBlock: str\n        :param Ipv6CidrBlock: CIDR block or IPv6 address (mutually exclusive).\n        :type Ipv6CidrBlock: str\n        :param Action: ACCEPT or DROP.\n        :type Action: str\n        :param Description: Rule description, which is up to 100 bytes.\n        :type Description: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkAclEntrySet(AbstractModel):
    """Network ACL rule set

    """

    def __init__(self):
        """
        :param Ingress: Inbound rules.\n        :type Ingress: list of NetworkAclEntry\n        :param Egress: Outbound rules.\n        :type Egress: list of NetworkAclEntry\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkInterface(AbstractModel):
    """ENI

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-f1xjkw1b`.\n        :type NetworkInterfaceId: str\n        :param NetworkInterfaceName: ENI Name\n        :type NetworkInterfaceName: str\n        :param NetworkInterfaceDescription: ENI description.\n        :type NetworkInterfaceDescription: str\n        :param SubnetId: Subnet instance ID.\n        :type SubnetId: str\n        :param VpcId: VPC instance ID.\n        :type VpcId: str\n        :param GroupSet: Bound security group.\n        :type GroupSet: list of str\n        :param Primary: Whether it is the primary ENI.\n        :type Primary: bool\n        :param MacAddress: MAC address\n        :type MacAddress: str\n        :param State: ENI status:
<li>`PENDING`: Creating</li>
<li>`AVAILABLE`: Available</li>
<li>`ATTACHING`: Binding</li>
<li>`DETACHING`: Unbinding</li>
<li>`DELETING`: Deleting</li>\n        :type State: str\n        :param PrivateIpAddressSet: Private IP information.\n        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification\n        :param Attachment: Bound CVM object.
Note: This field may return null, indicating no valid value.\n        :type Attachment: :class:`tencentcloud.vpc.v20170312.models.NetworkInterfaceAttachment`\n        :param Zone: Availability Zone.\n        :type Zone: str\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        :param Ipv6AddressSet: The `IPv6` address list.\n        :type Ipv6AddressSet: list of Ipv6Address\n        :param TagSet: Tag key-value pair.\n        :type TagSet: list of Tag\n        :param EniType: The ENI type. 0: ENI. 1: EVM ENI.\n        :type EniType: int\n        :param Business: Type of the resource bound with an ENI. Valid values: cvm, eks.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Business: str\n        :param CdcId: ID of the CDC instance associated with the ENI
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type CdcId: str\n        :param AttachType: ENI type. Valid values: `0` (standard); `1` (extension). Default value: `0`.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type AttachType: int\n        """
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
        self.Business = None
        self.CdcId = None
        self.AttachType = None


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
        self.Business = params.get("Business")
        self.CdcId = params.get("CdcId")
        self.AttachType = params.get("AttachType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkInterfaceAttachment(AbstractModel):
    """Binding relationship of the ENI

    """

    def __init__(self):
        """
        :param InstanceId: CVM instance ID.\n        :type InstanceId: str\n        :param DeviceIndex: The serial number of ENI in the CVM instance.\n        :type DeviceIndex: int\n        :param InstanceAccountId: The account information of the CVM owner.\n        :type InstanceAccountId: str\n        :param AttachTime: Binding time\n        :type AttachTime: str\n        """
        self.InstanceId = None
        self.DeviceIndex = None
        self.InstanceAccountId = None
        self.AttachTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DeviceIndex = params.get("DeviceIndex")
        self.InstanceAccountId = params.get("InstanceAccountId")
        self.AttachTime = params.get("AttachTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotifyRoutesRequest(AbstractModel):
    """NotifyRoutes request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: The unique ID of the route table\n        :type RouteTableId: str\n        :param RouteItemIds: The unique ID of the routing policy\n        :type RouteItemIds: list of str\n        """
        self.RouteTableId = None
        self.RouteItemIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteItemIds = params.get("RouteItemIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotifyRoutesResponse(AbstractModel):
    """NotifyRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Price(AbstractModel):
    """Price

    """

    def __init__(self):
        """
        :param InstancePrice: Instance price.\n        :type InstancePrice: :class:`tencentcloud.vpc.v20170312.models.ItemPrice`\n        :param BandwidthPrice: Network price.\n        :type BandwidthPrice: :class:`tencentcloud.vpc.v20170312.models.ItemPrice`\n        """
        self.InstancePrice = None
        self.BandwidthPrice = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = ItemPrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self.BandwidthPrice = ItemPrice()
            self.BandwidthPrice._deserialize(params.get("BandwidthPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateIpAddressSpecification(AbstractModel):
    """Private IP information

    """

    def __init__(self):
        """
        :param PrivateIpAddress: Private IP address.\n        :type PrivateIpAddress: str\n        :param Primary: Whether it is a primary IP.\n        :type Primary: bool\n        :param PublicIpAddress: Public IP address.\n        :type PublicIpAddress: str\n        :param AddressId: EIP instance ID, such as `eip-11112222`.\n        :type AddressId: str\n        :param Description: Private IP description.\n        :type Description: str\n        :param IsWanIpBlocked: Whether the public IP is blocked.\n        :type IsWanIpBlocked: bool\n        :param State: IP status:
PENDING: Creating
MIGRATING: Migrating
DELETING: Deleting
AVAILABLE: Available\n        :type State: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """Quota description information

    """

    def __init__(self):
        """
        :param QuotaId: Quota name. Value range:<br><li>`TOTAL_EIP_QUOTA`:EIP quota under the user's current region<br><li>`DAILY_EIP_APPLY`: Number of EIP applications submitted daily under the user's current region<br><li>`DAILY_PUBLIC_IP_ASSIGN`: Number of public IP reassignments under the user's current region.\n        :type QuotaId: str\n        :param QuotaCurrent: Current count\n        :type QuotaCurrent: int\n        :param QuotaLimit: Quota\n        :type QuotaLimit: int\n        """
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
        


class ReferredSecurityGroup(AbstractModel):
    """Referred security groups

    """

    def __init__(self):
        """
        :param SecurityGroupId: Security group instance ID.\n        :type SecurityGroupId: str\n        :param ReferredSecurityGroupIds: IDs of all referred security group instances.\n        :type ReferredSecurityGroupIds: list of str\n        """
        self.SecurityGroupId = None
        self.ReferredSecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.ReferredSecurityGroupIds = params.get("ReferredSecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectAttachCcnInstancesRequest(AbstractModel):
    """RejectAttachCcnInstances request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        :param Instances: The list of instances whose association is rejected.\n        :type Instances: list of CcnInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectAttachCcnInstancesResponse(AbstractModel):
    """RejectAttachCcnInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseAddressesRequest(AbstractModel):
    """ReleaseAddresses request structure.

    """

    def __init__(self):
        """
        :param AddressIds: The unique ID list of the EIP. The unique ID of an EIP is as follows: `eip-11112222`.\n        :type AddressIds: list of str\n        """
        self.AddressIds = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseAddressesResponse(AbstractModel):
    """ReleaseAddresses response structure.

    """

    def __init__(self):
        """
        :param TaskId: The async task ID. You can use the [DescribeTaskResult](https://intl.cloud.tencent.com/document/api/215/36271?from_cn_redirect=1) API to query the task status.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param BandwidthPackageId: The unique ID of the bandwidth package, such as `bwp-xxxx`.\n        :type BandwidthPackageId: str\n        :param ResourceType: The resource type. Valid values: `Address` and `LoadBalance`.\n        :type ResourceType: str\n        :param ResourceIds: The resource IP, such as `eip-xxxx` and `lb-xxxx`.\n        :type ResourceIds: list of str\n        """
        self.BandwidthPackageId = None
        self.ResourceType = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveBandwidthPackageResourcesResponse(AbstractModel):
    """RemoveBandwidthPackageResources response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewVpnGatewayRequest(AbstractModel):
    """RenewVpnGateway request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param InstanceChargePrepaid: Billing Methods\n        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`\n        """
        self.VpnGatewayId = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewVpnGatewayResponse(AbstractModel):
    """RenewVpnGateway response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """ReplaceDirectConnectGatewayCcnRoutes request structure.

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`\n        :type DirectConnectGatewayId: str\n        :param Routes: The list of IDC IP range that must be connected\n        :type Routes: list of DirectConnectGatewayCcnRoute\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """ReplaceDirectConnectGatewayCcnRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceRouteTableAssociationRequest(AbstractModel):
    """ReplaceRouteTableAssociation request structure.

    """

    def __init__(self):
        """
        :param SubnetId: Subnet instance ID, such as `subnet-3x5lf5q0`. This can be queried using the DescribeSubnets API.\n        :type SubnetId: str\n        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.\n        :type RouteTableId: str\n        """
        self.SubnetId = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceRouteTableAssociationResponse(AbstractModel):
    """ReplaceRouteTableAssociation response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceRoutesRequest(AbstractModel):
    """ReplaceRoutes request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.\n        :type RouteTableId: str\n        :param Routes: Routing policy object. The routing policy ID (RouteId) must be specified.\n        :type Routes: list of Route\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceRoutesResponse(AbstractModel):
    """ReplaceRoutes response structure.

    """

    def __init__(self):
        """
        :param OldRouteSet: Old routing policy\n        :type OldRouteSet: list of Route\n        :param NewRouteSet: New routing policy\n        :type NewRouteSet: list of Route\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.OldRouteSet = None
        self.NewRouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OldRouteSet") is not None:
            self.OldRouteSet = []
            for item in params.get("OldRouteSet"):
                obj = Route()
                obj._deserialize(item)
                self.OldRouteSet.append(obj)
        if params.get("NewRouteSet") is not None:
            self.NewRouteSet = []
            for item in params.get("NewRouteSet"):
                obj = Route()
                obj._deserialize(item)
                self.NewRouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class ReplaceSecurityGroupPolicyRequest(AbstractModel):
    """ReplaceSecurityGroupPolicy request structure.

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups.\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: Security group policy set object.\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        :param OriginalSecurityGroupPolicySet: (Optional) The old policy set of the security group, which is used for log records.\n        :type OriginalSecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceSecurityGroupPolicyResponse(AbstractModel):
    """ReplaceSecurityGroupPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetAttachCcnInstancesRequest(AbstractModel):
    """ResetAttachCcnInstances request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        :param CcnUin: The UIN (root account) to which the CCN belongs.\n        :type CcnUin: str\n        :param Instances: The list of network instances that re-apply for association.\n        :type Instances: list of CcnInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAttachCcnInstancesResponse(AbstractModel):
    """ResetAttachCcnInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetNatGatewayConnectionRequest(AbstractModel):
    """ResetNatGatewayConnection request structure.

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT gateway ID.\n        :type NatGatewayId: str\n        :param MaxConcurrentConnection: Concurrent connections cap of the NAT gateway, such as 1000000, 3000000, 10000000.\n        :type MaxConcurrentConnection: int\n        """
        self.NatGatewayId = None
        self.MaxConcurrentConnection = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.MaxConcurrentConnection = params.get("MaxConcurrentConnection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetNatGatewayConnectionResponse(AbstractModel):
    """ResetNatGatewayConnection response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetRoutesRequest(AbstractModel):
    """ResetRoutes request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.\n        :type RouteTableId: str\n        :param RouteTableName: The route table name. The maximum length is 60 characters.\n        :type RouteTableName: str\n        :param Routes: Routing policy.\n        :type Routes: list of Route\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetRoutesResponse(AbstractModel):
    """ResetRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetVpnConnectionRequest(AbstractModel):
    """ResetVpnConnection request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param VpnConnectionId: The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`.\n        :type VpnConnectionId: str\n        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetVpnConnectionResponse(AbstractModel):
    """ResetVpnConnection response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetVpnGatewayInternetMaxBandwidthRequest(AbstractModel):
    """ResetVpnGatewayInternetMaxBandwidth request structure.

    """

    def __init__(self):
        """
        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param InternetMaxBandwidthOut: The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps.\n        :type InternetMaxBandwidthOut: int\n        """
        self.VpnGatewayId = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetVpnGatewayInternetMaxBandwidthResponse(AbstractModel):
    """ResetVpnGatewayInternetMaxBandwidth response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """The structure of information of the bandwidth package.

    """

    def __init__(self):
        """
        :param ResourceType: The bandwidth package resource type, including `Address`, and `LoadBalance`\n        :type ResourceType: str\n        :param ResourceId: The bandwidth package ID, such as `eip-xxxx` and `lb-xxxx`.\n        :type ResourceId: str\n        :param AddressIp: The bandwidth package resource IP.\n        :type AddressIp: str\n        """
        self.ResourceType = None
        self.ResourceId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.AddressIp = params.get("AddressIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceDashboard(AbstractModel):
    """VPC resource dashboard (all resource counts)

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID, such as `vpc-bq4bzxpj`.\n        :type VpcId: str\n        :param SubnetId: Subnet instance ID, such as subnet-bthucmmy.\n        :type SubnetId: str\n        :param Classiclink: Classiclink.\n        :type Classiclink: int\n        :param Dcg: Direct Connect gateway.\n        :type Dcg: int\n        :param Pcx: Peering connection.\n        :type Pcx: int\n        :param Ip: Total number of used IPs except for CVM IP, EIP and network probe IP. The three IP types will be independently counted.\n        :type Ip: int\n        :param Nat: NAT gateway.\n        :type Nat: int\n        :param Vpngw: VPN gateway.\n        :type Vpngw: int\n        :param FlowLog: Flow log.\n        :type FlowLog: int\n        :param NetworkDetect: Network probing.\n        :type NetworkDetect: int\n        :param NetworkACL: Network ACL.\n        :type NetworkACL: int\n        :param CVM: Cloud Virtual Machine.\n        :type CVM: int\n        :param LB: Load balancer.\n        :type LB: int\n        :param CDB: Relational database.\n        :type CDB: int\n        :param Cmem: TencentDB for Memcached.\n        :type Cmem: int\n        :param CTSDB: Cloud time series database.\n        :type CTSDB: int\n        :param MariaDB: TencentDB for MariaDB (TDSQL).\n        :type MariaDB: int\n        :param SQLServer: TencentDB for SQL Server.\n        :type SQLServer: int\n        :param Postgres: TencentDB for PostgreSQL.\n        :type Postgres: int\n        :param NAS: Network attached storage.\n        :type NAS: int\n        :param Greenplumn: Snova data warehouse.\n        :type Greenplumn: int\n        :param Ckafka: Cloud Kafka (CKafka).\n        :type Ckafka: int\n        :param Grocery: Grocery.\n        :type Grocery: int\n        :param HSM: Data encryption service.\n        :type HSM: int\n        :param Tcaplus: Game storage - Tcaplus.\n        :type Tcaplus: int\n        :param Cnas: Cnas.\n        :type Cnas: int\n        :param TiDB: HTAP database - TiDB.\n        :type TiDB: int\n        :param Emr: EMR cluster.\n        :type Emr: int\n        :param SEAL: SEAL.\n        :type SEAL: int\n        :param CFS: Cloud file storage - CFS.\n        :type CFS: int\n        :param Oracle: Oracle.\n        :type Oracle: int\n        :param ElasticSearch: ElasticSearch Service.\n        :type ElasticSearch: int\n        :param TBaaS: Blockchain service.\n        :type TBaaS: int\n        :param Itop: Itop.\n        :type Itop: int\n        :param DBAudit: Cloud database audit.\n        :type DBAudit: int\n        :param CynosDBPostgres: Enterprise TencentDB - CynosDB for Postgres.\n        :type CynosDBPostgres: int\n        :param Redis: TencentDB for Redis.\n        :type Redis: int\n        :param MongoDB: TencentDB for MongoDB.\n        :type MongoDB: int\n        :param DCDB: A distributed cloud database - TencentDB for TDSQL.\n        :type DCDB: int\n        :param CynosDBMySQL: An enterprise-grade TencentDB - CynosDB for MySQL.\n        :type CynosDBMySQL: int\n        :param Subnet: Subnets.\n        :type Subnet: int\n        :param RouteTable: Route table.\n        :type RouteTable: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Route(AbstractModel):
    """Routing policy object

    """

    def __init__(self):
        """
        :param DestinationCidrBlock: Destination IP range, such as 112.20.51.0/24. Values cannot be in the VPC IP range.\n        :type DestinationCidrBlock: str\n        :param GatewayType: Type of the next hop. Valid values:
`CVM`: public gateway CVM;
`VPN`: VPN gateway;
`DIRECTCONNECT`: direct connect gateway;
`PEERCONNECTION`: peering connection;
`HAVIP`: HAVIP;
`NAT`: NAT Gateway; 
`NORMAL_CVM`: normal CVM;
`EIP`: public IP address of the CVM;
`LOCAL_GATEWAY`: local gateway.\n        :type GatewayType: str\n        :param GatewayId: Next hop address. You simply need to specify the gateway ID of a different next hop type, and the system will automatically match the next hop address.
Important note: When the GatewayType is EIP, the GatewayId has a fixed value `0`\n        :type GatewayId: str\n        :param RouteId: Routing policy ID. The IPv4 routing policy will have a meaningful value, while the IPv6 routing policy is always 0. We recommend using the unique ID `RouteItemId` for the routing policy.
This field is required when you want to delete a routing policy.\n        :type RouteId: int\n        :param RouteDescription: The description of the routing policy.\n        :type RouteDescription: str\n        :param Enabled: Whether it is enabled\n        :type Enabled: bool\n        :param RouteType: The route type. Currently, the following types are supported:
USER: User route;
NETD: Network probe route. When creating a network probe route, the system delivers by default. It cannot be edited or deleted;
CCN: CCN route. The system delivers by default. It cannot be edited or deleted.
Users can only add and operate USER-type routes.\n        :type RouteType: str\n        :param RouteTableId: Route table instance ID, such as rtb-azd4dt1c.\n        :type RouteTableId: str\n        :param DestinationIpv6CidrBlock: Destination IPv6 IP range, which cannot be included in VPC IP range, such as 2402:4e00:1000:810b::/64.\n        :type DestinationIpv6CidrBlock: str\n        :param RouteItemId: Unique routing policy ID.\n        :type RouteItemId: str\n        :param PublishedToVbc: Whether the routing policy is published to CCN.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type PublishedToVbc: bool\n        :param CreatedTime: Creation time of the routing policy\n        :type CreatedTime: str\n        """
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
        self.PublishedToVbc = None
        self.CreatedTime = None


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
        self.PublishedToVbc = params.get("PublishedToVbc")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTable(AbstractModel):
    """Route table object

    """

    def __init__(self):
        """
        :param VpcId: VPC instance ID.\n        :type VpcId: str\n        :param RouteTableId: The route table instance ID, such as `rtb-azd4dt1c`.\n        :type RouteTableId: str\n        :param RouteTableName: Route table name.\n        :type RouteTableName: str\n        :param AssociationSet: The association relationships of the route table.\n        :type AssociationSet: list of RouteTableAssociation\n        :param RouteSet: IPv4 routing policy set.\n        :type RouteSet: list of Route\n        :param Main: Whether it is the default route table.\n        :type Main: bool\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        :param TagSet: Tag key-value pairs.\n        :type TagSet: list of Tag\n        :param LocalCidrForCcn: Whether the local route is published to CCN.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type LocalCidrForCcn: list of CidrForCcn\n        """
        self.VpcId = None
        self.RouteTableId = None
        self.RouteTableName = None
        self.AssociationSet = None
        self.RouteSet = None
        self.Main = None
        self.CreatedTime = None
        self.TagSet = None
        self.LocalCidrForCcn = None


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
        if params.get("LocalCidrForCcn") is not None:
            self.LocalCidrForCcn = []
            for item in params.get("LocalCidrForCcn"):
                obj = CidrForCcn()
                obj._deserialize(item)
                self.LocalCidrForCcn.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableAssociation(AbstractModel):
    """The association relationships of the route table

    """

    def __init__(self):
        """
        :param SubnetId: Subnet instance ID.\n        :type SubnetId: str\n        :param RouteTableId: Route table instance ID.\n        :type RouteTableId: str\n        """
        self.SubnetId = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """Security group object

    """

    def __init__(self):
        """
        :param SecurityGroupId: The security group instance ID, such as `sg-ohuuioma`.\n        :type SecurityGroupId: str\n        :param SecurityGroupName: Security group can be named freely, but cannot exceed 60 characters.\n        :type SecurityGroupName: str\n        :param SecurityGroupDesc: The remarks for the security group. The maximum length is 100 characters.\n        :type SecurityGroupDesc: str\n        :param ProjectId: The project id is 0 by default. You can query this in the project management page of the Qcloud console.\n        :type ProjectId: str\n        :param IsDefault: Whether it is the default security group (which cannot be deleted).\n        :type IsDefault: bool\n        :param CreatedTime: Security group creation time.\n        :type CreatedTime: str\n        :param TagSet: Tag key-value pairs.\n        :type TagSet: list of Tag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupAssociationStatistics(AbstractModel):
    """Statistics on the instances associated with the security group

    """

    def __init__(self):
        """
        :param SecurityGroupId: Security group instance ID.\n        :type SecurityGroupId: str\n        :param CVM: Number of CVM instances.\n        :type CVM: int\n        :param CDB: Number of TencentDB for MySQL instances\n        :type CDB: int\n        :param ENI: Number of ENI instances.\n        :type ENI: int\n        :param SG: Number of times a security group is referenced by other security groups\n        :type SG: int\n        :param CLB: Number of load balancer instances.\n        :type CLB: int\n        :param InstanceStatistics: The binding statistics for all instances.\n        :type InstanceStatistics: list of InstanceStatistic\n        :param TotalCount: Total count of all resources (excluding resources referenced by security groups).\n        :type TotalCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicy(AbstractModel):
    """Security group policy object

    """

    def __init__(self):
        """
        :param PolicyIndex: The index number of security group rules, which dynamically changes with the rules. This parameter can be obtained via the `DescribeSecurityGroupPolicies` API and used with the `Version` field in the returned value of the API.\n        :type PolicyIndex: int\n        :param Protocol: Protocol. Valid values: TCP, UDP, ICMP, ICMPv6, ALL.\n        :type Protocol: str\n        :param Port: Port (all, discrete port, range).\n        :type Port: str\n        :param ServiceTemplate: Protocol port ID or protocol port group ID. ServiceTemplate and Protocol+Port are mutually exclusive.\n        :type ServiceTemplate: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplateSpecification`\n        :param CidrBlock: IP range or IP (mutually exclusive).\n        :type CidrBlock: str\n        :param Ipv6CidrBlock: The CIDR block or IPv6 (mutually exclusive).\n        :type Ipv6CidrBlock: str\n        :param SecurityGroupId: The security group instance ID, such as `sg-ohuuioma`.\n        :type SecurityGroupId: str\n        :param AddressTemplate: IP address ID or IP address group ID.\n        :type AddressTemplate: :class:`tencentcloud.vpc.v20170312.models.AddressTemplateSpecification`\n        :param Action: ACCEPT or DROP.\n        :type Action: str\n        :param PolicyDescription: Security group policy description.\n        :type PolicyDescription: str\n        :param ModifyTime: The last modification time of the security group.\n        :type ModifyTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicySet(AbstractModel):
    """Security group policy set

    """

    def __init__(self):
        """
        :param Version: The version of the security group policy. The version number is automatically increased by one each time users update the security policy, to prevent the expiration of updated routing policies. Conflict is ignored if it is left empty.\n        :type Version: str\n        :param Egress: Outbound policy.\n        :type Egress: list of SecurityGroupPolicy\n        :param Ingress: Inbound policy.\n        :type Ingress: list of SecurityGroupPolicy\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyDatabase(AbstractModel):
    """SecurityPolicyDatabase policy

    """

    def __init__(self):
        """
        :param LocalCidrBlock: Local IP range\n        :type LocalCidrBlock: str\n        :param RemoteCidrBlock: Opposite IP range\n        :type RemoteCidrBlock: list of str\n        """
        self.LocalCidrBlock = None
        self.RemoteCidrBlock = None


    def _deserialize(self, params):
        self.LocalCidrBlock = params.get("LocalCidrBlock")
        self.RemoteCidrBlock = params.get("RemoteCidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceTemplate(AbstractModel):
    """Protocol port template

    """

    def __init__(self):
        """
        :param ServiceTemplateId: Protocol port instance ID, such as `ppm-f5n1f8da`.\n        :type ServiceTemplateId: str\n        :param ServiceTemplateName: Template name.\n        :type ServiceTemplateName: str\n        :param ServiceSet: Protocol port information.\n        :type ServiceSet: list of str\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        """
        self.ServiceTemplateId = None
        self.ServiceTemplateName = None
        self.ServiceSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.ServiceSet = params.get("ServiceSet")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceTemplateGroup(AbstractModel):
    """Protocol port template group

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: Protocol port template group instance ID, such as `ppmg-2klmrefu`.\n        :type ServiceTemplateGroupId: str\n        :param ServiceTemplateGroupName: Protocol port template group name.\n        :type ServiceTemplateGroupName: str\n        :param ServiceTemplateIdSet: Protocol port template instance ID.\n        :type ServiceTemplateIdSet: list of str\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        :param ServiceTemplateSet: Protocol port template instance information.\n        :type ServiceTemplateSet: list of ServiceTemplate\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceTemplateSpecification(AbstractModel):
    """Protocol port template

    """

    def __init__(self):
        """
        :param ServiceId: Protocol port ID, such as `ppm-f5n1f8da`.\n        :type ServiceId: str\n        :param ServiceGroupId: Protocol port group ID, such as `ppmg-f5n1f8da`.\n        :type ServiceGroupId: str\n        """
        self.ServiceId = None
        self.ServiceGroupId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceGroupId = params.get("ServiceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCcnRegionBandwidthLimitsRequest(AbstractModel):
    """SetCcnRegionBandwidthLimits request structure.

    """

    def __init__(self):
        """
        :param CcnId: The CCN instance ID, such as `ccn-f49l6u0z`.\n        :type CcnId: str\n        :param CcnRegionBandwidthLimits: The outbound bandwidth cap of each CCN region.\n        :type CcnRegionBandwidthLimits: list of CcnRegionBandwidthLimit\n        :param SetDefaultLimitFlag: Whether to restore the region outbound bandwidth limit or inter-region bandwidth limit to default 1 Gbps. Valid values: `false` (no); `true` (yes). Default value: `false`. When the parameter is set to `true`, the CCN instance created will not be displayed in the console.\n        :type SetDefaultLimitFlag: bool\n        """
        self.CcnId = None
        self.CcnRegionBandwidthLimits = None
        self.SetDefaultLimitFlag = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("CcnRegionBandwidthLimits") is not None:
            self.CcnRegionBandwidthLimits = []
            for item in params.get("CcnRegionBandwidthLimits"):
                obj = CcnRegionBandwidthLimit()
                obj._deserialize(item)
                self.CcnRegionBandwidthLimits.append(obj)
        self.SetDefaultLimitFlag = params.get("SetDefaultLimitFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCcnRegionBandwidthLimitsResponse(AbstractModel):
    """SetCcnRegionBandwidthLimits response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SourceIpTranslationNatRule(AbstractModel):
    """SNAT rule of a NAT Gateway

    """

    def __init__(self):
        """
        :param ResourceId: Resource ID\n        :type ResourceId: str\n        :param ResourceType: Resource type. Valid values: SUBNET, NETWORKINTERFACE
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ResourceType: str\n        :param PrivateIpAddress: Source IP/IP range\n        :type PrivateIpAddress: str\n        :param PublicIpAddresses: Elastic IP address pool\n        :type PublicIpAddresses: list of str\n        :param Description: Description\n        :type Description: str\n        :param NatGatewaySnatId: SNAT rule ID\n        :type NatGatewaySnatId: str\n        :param NatGatewayId: NAT Gateway ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type NatGatewayId: str\n        :param VpcId: VPC ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type VpcId: str\n        :param CreatedTime: Creation time of a SNAT rule for a NAT Gateway
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type CreatedTime: str\n        """
        self.ResourceId = None
        self.ResourceType = None
        self.PrivateIpAddress = None
        self.PublicIpAddresses = None
        self.Description = None
        self.NatGatewaySnatId = None
        self.NatGatewayId = None
        self.VpcId = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceType = params.get("ResourceType")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.Description = params.get("Description")
        self.NatGatewaySnatId = params.get("NatGatewaySnatId")
        self.NatGatewayId = params.get("NatGatewayId")
        self.VpcId = params.get("VpcId")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Subnet(AbstractModel):
    """Subnet object

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the `VPC` instance.\n        :type VpcId: str\n        :param SubnetId: Subnet instance `ID`, such as `subnet-bthucmmy`.\n        :type SubnetId: str\n        :param SubnetName: Subnet name.\n        :type SubnetName: str\n        :param CidrBlock: The `IPv4` `CIDR` of the subnet.\n        :type CidrBlock: str\n        :param IsDefault: Whether it is the default subnet.\n        :type IsDefault: bool\n        :param EnableBroadcast: Whether to enable broadcast.\n        :type EnableBroadcast: bool\n        :param Zone: Availability Zone.\n        :type Zone: str\n        :param RouteTableId: The route table instance ID, such as `rtb-l2h8d7c2`.\n        :type RouteTableId: str\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        :param AvailableIpAddressCount: The number of available IPv4 addresses\n        :type AvailableIpAddressCount: int\n        :param Ipv6CidrBlock: The `IPv6` `CIDR` of the subnet.\n        :type Ipv6CidrBlock: str\n        :param NetworkAclId: The associated `ACL`ID\n        :type NetworkAclId: str\n        :param IsRemoteVpcSnat: Whether it is a `SNAT` address pool subnet.\n        :type IsRemoteVpcSnat: bool\n        :param TotalIpAddressCount: The total number of IPv4 addresses in the subnet.\n        :type TotalIpAddressCount: int\n        :param TagSet: Tag key-value pairs\n        :type TagSet: list of Tag\n        :param CdcId: CDC instance ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type CdcId: str\n        :param IsCdcSubnet: Whether it is a CDC subnet. Valid values: 0: no; 1: yes
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type IsCdcSubnet: int\n        """
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
        self.CdcId = None
        self.IsCdcSubnet = None


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
        self.CdcId = params.get("CdcId")
        self.IsCdcSubnet = params.get("IsCdcSubnet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetInput(AbstractModel):
    """Subnet object

    """

    def __init__(self):
        """
        :param CidrBlock: The `CIDR` of the subnet.\n        :type CidrBlock: str\n        :param SubnetName: Subnet name.\n        :type SubnetName: str\n        :param Zone: The availability zone, such as `ap-guangzhou-2`.\n        :type Zone: str\n        :param RouteTableId: The specified associated route table, such as `rtb-3ryrwzuu`.\n        :type RouteTableId: str\n        """
        self.CidrBlock = None
        self.SubnetName = None
        self.Zone = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.CidrBlock = params.get("CidrBlock")
        self.SubnetName = params.get("SubnetName")
        self.Zone = params.get("Zone")
        self.RouteTableId = params.get("RouteTableId")
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
Note: This field may return null, indicating no valid value.\n        :type Key: str\n        :param Value: Tag value
Note: This field may return null, indicating no valid value.\n        :type Value: str\n        """
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
        


class TransformAddressRequest(AbstractModel):
    """TransformAddress request structure.

    """

    def __init__(self):
        """
        :param InstanceId: The ID of the instance with a common public IP to be operated on, such as `ins-11112222`. You can query the instance ID by logging into the [Console](https://console.cloud.tencent.com/cvm). You can also obtain the parameter value from the `InstanceId` field in the returned result of [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/9389?from_cn_redirect=1) API.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransformAddressResponse(AbstractModel):
    """TransformAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6AddressesRequest(AbstractModel):
    """UnassignIpv6Addresses request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The `ID` of the ENI instance, such as `eni-m6dyj72l`.\n        :type NetworkInterfaceId: str\n        :param Ipv6Addresses: The list of specified `IPv6` addresses. A maximum of 10 can be specified each time.\n        :type Ipv6Addresses: list of Ipv6Address\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassignIpv6AddressesResponse(AbstractModel):
    """UnassignIpv6Addresses response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6CidrBlockRequest(AbstractModel):
    """UnassignIpv6CidrBlock request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the `VPC`, such as `vpc-f49l6u0z`.\n        :type VpcId: str\n        :param Ipv6CidrBlock: The `IPv6` IP range, such as `3402:4e00:20:1000::/56`\n        :type Ipv6CidrBlock: str\n        """
        self.VpcId = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassignIpv6CidrBlockResponse(AbstractModel):
    """UnassignIpv6CidrBlock response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6SubnetCidrBlockRequest(AbstractModel):
    """UnassignIpv6SubnetCidrBlock request structure.

    """

    def __init__(self):
        """
        :param VpcId: The `ID` of the VPC where the subnet is located, such as `vpc-f49l6u0z`.\n        :type VpcId: str\n        :param Ipv6SubnetCidrBlocks: The `IPv6` subnet IP range list.\n        :type Ipv6SubnetCidrBlocks: list of Ipv6SubnetCidrBlock\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassignIpv6SubnetCidrBlockResponse(AbstractModel):
    """UnassignIpv6SubnetCidrBlock response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignPrivateIpAddressesRequest(AbstractModel):
    """UnassignPrivateIpAddresses request structure.

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: The ID of the ENI instance, such as `eni-m6dyj72l`.\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddresses: The information of the specified private IPs. You can specify a maximum of 10 each time.\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassignPrivateIpAddressesResponse(AbstractModel):
    """UnassignPrivateIpAddresses response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Vpc(AbstractModel):
    """Virtual Private Cloud (VPC) object.

    """

    def __init__(self):
        """
        :param VpcName: `VPC` name.\n        :type VpcName: str\n        :param VpcId: `VPC` instance `ID`, such as `vpc-azd4dt1c`.\n        :type VpcId: str\n        :param CidrBlock: The `IPv4` `CIDR` of the `VPC`.\n        :type CidrBlock: str\n        :param IsDefault: Whether it is the default `VPC`.\n        :type IsDefault: bool\n        :param EnableMulticast: Whether multicast is enabled.\n        :type EnableMulticast: bool\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        :param DnsServerSet: `DNS` list.\n        :type DnsServerSet: list of str\n        :param DomainName: DHCP domain name option value.\n        :type DomainName: str\n        :param DhcpOptionsId: `DHCP` option set `ID`.\n        :type DhcpOptionsId: str\n        :param EnableDhcp: Whether `DHCP` is enabled.\n        :type EnableDhcp: bool\n        :param Ipv6CidrBlock: The `IPv6` `CIDR` of the `VPC`.\n        :type Ipv6CidrBlock: str\n        :param TagSet: Tag key-value pair\n        :type TagSet: list of Tag\n        :param AssistantCidrSet: The secondary CIDR block.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type AssistantCidrSet: list of AssistantCidr\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcEndPointServiceUser(AbstractModel):
    """Details of allowed endpoint services

    """

    def __init__(self):
        """
        :param Owner: APP ID\n        :type Owner: int\n        :param UserUin: User UIN\n        :type UserUin: str\n        :param Description: Description\n        :type Description: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param EndPointServiceId: Endpoint service ID\n        :type EndPointServiceId: str\n        """
        self.Owner = None
        self.UserUin = None
        self.Description = None
        self.CreateTime = None
        self.EndPointServiceId = None


    def _deserialize(self, params):
        self.Owner = params.get("Owner")
        self.UserUin = params.get("UserUin")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.EndPointServiceId = params.get("EndPointServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcIpv6Address(AbstractModel):
    """VPC private IPv6 object.

    """

    def __init__(self):
        """
        :param Ipv6Address: `VPC` private `IPv6` address\n        :type Ipv6Address: str\n        :param CidrBlock: The `IPv6` `CIDR` belonging to the subnet.\n        :type CidrBlock: str\n        :param Ipv6AddressType: `IPv6` type.\n        :type Ipv6AddressType: str\n        :param CreatedTime: `IPv6` application time.\n        :type CreatedTime: str\n        """
        self.Ipv6Address = None
        self.CidrBlock = None
        self.Ipv6AddressType = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.Ipv6Address = params.get("Ipv6Address")
        self.CidrBlock = params.get("CidrBlock")
        self.Ipv6AddressType = params.get("Ipv6AddressType")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcPrivateIpAddress(AbstractModel):
    """VPC private IP object.

    """

    def __init__(self):
        """
        :param PrivateIpAddress: `VPC` private `IP`.\n        :type PrivateIpAddress: str\n        :param CidrBlock: The `CIDR` belonging to the subnet.\n        :type CidrBlock: str\n        :param PrivateIpAddressType: Private `IP` type.\n        :type PrivateIpAddressType: str\n        :param CreatedTime: `IP` application time.\n        :type CreatedTime: str\n        """
        self.PrivateIpAddress = None
        self.CidrBlock = None
        self.PrivateIpAddressType = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.CidrBlock = params.get("CidrBlock")
        self.PrivateIpAddressType = params.get("PrivateIpAddressType")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnConnection(AbstractModel):
    """VPN tunnel object.

    """

    def __init__(self):
        """
        :param VpnConnectionId: Tunnel instance ID.\n        :type VpnConnectionId: str\n        :param VpnConnectionName: Tunnel name.\n        :type VpnConnectionName: str\n        :param VpcId: VPC instance ID.\n        :type VpcId: str\n        :param VpnGatewayId: The ID of the VPN gateway instance.\n        :type VpnGatewayId: str\n        :param CustomerGatewayId: Customer gateway instance ID.\n        :type CustomerGatewayId: str\n        :param PreShareKey: The pre-shared key.\n        :type PreShareKey: str\n        :param VpnProto: Tunnel transmission protocol.\n        :type VpnProto: str\n        :param EncryptProto: Tunnel encryption protocol.\n        :type EncryptProto: str\n        :param RouteType: Route Type.\n        :type RouteType: str\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        :param State: Production status of the tunnel. PENDING: Creating; AVAILABLE: Running; DELETING: Deleting.\n        :type State: str\n        :param NetStatus: Connection status of the tunnel. AVAILABLE: Connected.\n        :type NetStatus: str\n        :param SecurityPolicyDatabaseSet: SPD.\n        :type SecurityPolicyDatabaseSet: list of SecurityPolicyDatabase\n        :param IKEOptionsSpecification: IKE options.\n        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`\n        :param IPSECOptionsSpecification: IPSEC options.\n        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`\n        :param EnableHealthCheck: Whether the health check is supported.\n        :type EnableHealthCheck: bool\n        :param HealthCheckLocalIp: Local IP address for the health check\n        :type HealthCheckLocalIp: str\n        :param HealthCheckRemoteIp: Peer IP address for the health check\n        :type HealthCheckRemoteIp: str\n        :param HealthCheckStatus: Tunnel health check status. Valid values: AVAILABLE: healthy; UNAVAILABLE: unhealthy. This parameter will be returned only after health check is enabled.\n        :type HealthCheckStatus: str\n        """
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
        self.EnableHealthCheck = None
        self.HealthCheckLocalIp = None
        self.HealthCheckRemoteIp = None
        self.HealthCheckStatus = None


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
        self.EnableHealthCheck = params.get("EnableHealthCheck")
        self.HealthCheckLocalIp = params.get("HealthCheckLocalIp")
        self.HealthCheckRemoteIp = params.get("HealthCheckRemoteIp")
        self.HealthCheckStatus = params.get("HealthCheckStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnGateway(AbstractModel):
    """VPN gateway object.

    """

    def __init__(self):
        """
        :param VpnGatewayId: Gateway instance ID.\n        :type VpnGatewayId: str\n        :param VpcId: VPC instance ID.\n        :type VpcId: str\n        :param VpnGatewayName: Gateway instance name.\n        :type VpnGatewayName: str\n        :param Type: Gateway instance type. Valid values: 'IPSEC', 'SSL', and 'CCN'.\n        :type Type: str\n        :param State: Gateway instance status. 'PENDING': Creating; 'DELETING': Deleting; 'AVAILABLE': Running.\n        :type State: str\n        :param PublicIpAddress: Gateway public IP.\n        :type PublicIpAddress: str\n        :param RenewFlag: Gateway renewal type: 'NOTIFY_AND_MANUAL_RENEW': Manual renewal. 'NOTIFY_AND_AUTO_RENEW': Automatic renewal. 'NOT_NOTIFY_AND_NOT_RENEW': No renewal after expiration.\n        :type RenewFlag: str\n        :param InstanceChargeType: Gateway billing type: POSTPAID_BY_HOUR: Postpaid by hour; PREPAID: Prepaid.\n        :type InstanceChargeType: str\n        :param InternetMaxBandwidthOut: Outbound bandwidth of gateway.\n        :type InternetMaxBandwidthOut: int\n        :param CreatedTime: Creation Time.\n        :type CreatedTime: str\n        :param ExpiredTime: Expiration time of the prepaid gateway.\n        :type ExpiredTime: str\n        :param IsAddressBlocked: Whether the public IP is blocked.\n        :type IsAddressBlocked: bool\n        :param NewPurchasePlan: Change of billing method. PREPAID_TO_POSTPAID: Monthly subscription prepaid to postpaid by hour.\n        :type NewPurchasePlan: str\n        :param RestrictState: Gateway billing status. PROTECTIVELY_ISOLATED: Instance is isolated; NORMAL: Normal.\n        :type RestrictState: str\n        :param Zone: The availability zone, such as `ap-guangzhou-2`\n        :type Zone: str\n        :param VpnGatewayQuotaSet: Gateway bandwidth quota information.\n        :type VpnGatewayQuotaSet: list of VpnGatewayQuota\n        :param Version: Gateway instance version.\n        :type Version: str\n        :param NetworkInstanceId: CCN instance ID when the value of Type is CCN.\n        :type NetworkInstanceId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnGatewayQuota(AbstractModel):
    """VPN gateway quota object

    """

    def __init__(self):
        """
        :param Bandwidth: The bandwidth quota.\n        :type Bandwidth: int\n        :param Cname: The bandwidth quota name in Chinese.\n        :type Cname: str\n        :param Name: The bandwidth quota name in English.\n        :type Name: str\n        """
        self.Bandwidth = None
        self.Cname = None
        self.Name = None


    def _deserialize(self, params):
        self.Bandwidth = params.get("Bandwidth")
        self.Cname = params.get("Cname")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnGatewayRoute(AbstractModel):
    """Destination routes of a VPN gateway

    """

    def __init__(self):
        """
        :param DestinationCidrBlock: Destination IDC IP range\n        :type DestinationCidrBlock: str\n        :param InstanceType: Next hop type (type of the associated instance). Valid values: `VPNCONN` (VPN tunnel) and `CCN` (CCN instance)\n        :type InstanceType: str\n        :param InstanceId: Instance ID of the next hop\n        :type InstanceId: str\n        :param Priority: Priority. Valid values: `0` and `100`\n        :type Priority: int\n        :param Status: Status. Valid values: `ENABLE` and `DISABLE`\n        :type Status: str\n        :param RouteId: Route ID\n        :type RouteId: str\n        :param Type: Route type. Valid values: `VPC`, `CCN` (CCN-propagated route), `Static`, and `BGP`.\n        :type Type: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param UpdateTime: Update time\n        :type UpdateTime: str\n        """
        self.DestinationCidrBlock = None
        self.InstanceType = None
        self.InstanceId = None
        self.Priority = None
        self.Status = None
        self.RouteId = None
        self.Type = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")
        self.Priority = params.get("Priority")
        self.Status = params.get("Status")
        self.RouteId = params.get("RouteId")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnGatewayRouteModify(AbstractModel):
    """Modify route status of the VPN gateway

    """

    def __init__(self):
        """
        :param RouteId: Route ID of the VPN gateway\n        :type RouteId: str\n        :param Status: Route status of the VPN gateway. Valid values: `ENABLE`, and `DISABLE`.\n        :type Status: str\n        """
        self.RouteId = None
        self.Status = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpngwCcnRoutes(AbstractModel):
    """Information on VPN gateway-based CCN routes.

    """

    def __init__(self):
        """
        :param RouteId: Route ID\n        :type RouteId: str\n        :param Status: Enable the route or not
ENABLE: enable the route
DISABLE: do not enable the route\n        :type Status: str\n        """
        self.RouteId = None
        self.Status = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawNotifyRoutesRequest(AbstractModel):
    """WithdrawNotifyRoutes request structure.

    """

    def __init__(self):
        """
        :param RouteTableId: The unique ID of the route table\n        :type RouteTableId: str\n        :param RouteItemIds: The unique ID of the routing policy\n        :type RouteItemIds: list of str\n        """
        self.RouteTableId = None
        self.RouteItemIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteItemIds = params.get("RouteItemIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawNotifyRoutesResponse(AbstractModel):
    """WithdrawNotifyRoutes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")