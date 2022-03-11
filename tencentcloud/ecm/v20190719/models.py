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


class Address(AbstractModel):
    """EIP information

    """

    def __init__(self):
        r"""
        :param AddressId: Unique EIP ID.
        :type AddressId: str
        :param AddressName: EIP name.
        :type AddressName: str
        :param AddressStatus: EIP status, including 'CREATING' (creating), 'BINDING' (binding), 'BIND' (bound), 'UNBINDING' (unbinding), 'UNBIND' (unbound), 'OFFLINING' (releasing), and 'BIND_ENI' (binding dangling ENI)
        :type AddressStatus: str
        :param AddressIp: Public IP address
        :type AddressIp: str
        :param InstanceId: ID of the bound resource instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param CreatedTime: Creation time in ISO 8601 format (YYYY-MM-DDTHH:mm:ss.sssZ)
        :type CreatedTime: str
        :param NetworkInterfaceId: ID of the bound ENI
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetworkInterfaceId: str
        :param PrivateAddressIp: Private IP of the bound resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateAddressIp: str
        :param IsArrears: Isolation status of the resource. true: isolated; false: not isolated.
        :type IsArrears: bool
        :param IsBlocked: Blockage status of the EIP resource. true: blocked; false: not blocked
        :type IsBlocked: bool
        :param IsEipDirectConnection: Whether the EIP supports direct access mode. true: yes; false: no.
        :type IsEipDirectConnection: bool
        :param AddressType: Resource type of the EIP, including `CalcIP` (device IP), `WanIP` (general public IP), `EIP` (elastic IP), and `AnycastEip` (accelerated EIP).
        :type AddressType: str
        :param CascadeRelease: Whether the EIP is automatically released after being unbound. true: yes; false: no
        :type CascadeRelease: bool
        :param InternetServiceProvider: ISP. CTCC: China Telecom; CUCC: China Unicom; CMCC: China Mobile
Note: this field may return null, indicating that no valid values can be obtained.
        :type InternetServiceProvider: str
        :param Bandwidth: Bandwidth cap
Note: this field may return null, indicating that no valid values can be obtained.
        :type Bandwidth: int
        :param PayMode: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
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
        self.InternetServiceProvider = None
        self.Bandwidth = None
        self.PayMode = None


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
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.Bandwidth = params.get("Bandwidth")
        self.PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressInfo(AbstractModel):
    """IP address information structure.

    """

    def __init__(self):
        r"""
        :param PublicIPAddressInfo: Public IP information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicIPAddressInfo: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`
        :param PrivateIPAddressInfo: Private IP information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIPAddressInfo: :class:`tencentcloud.ecm.v20190719.models.PrivateIPAddressInfo`
        :param PublicIPv6AddressInfo: Public IPv6 information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicIPv6AddressInfo: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`
        """
        self.PublicIPAddressInfo = None
        self.PrivateIPAddressInfo = None
        self.PublicIPv6AddressInfo = None


    def _deserialize(self, params):
        if params.get("PublicIPAddressInfo") is not None:
            self.PublicIPAddressInfo = PublicIPAddressInfo()
            self.PublicIPAddressInfo._deserialize(params.get("PublicIPAddressInfo"))
        if params.get("PrivateIPAddressInfo") is not None:
            self.PrivateIPAddressInfo = PrivateIPAddressInfo()
            self.PrivateIPAddressInfo._deserialize(params.get("PrivateIPAddressInfo"))
        if params.get("PublicIPv6AddressInfo") is not None:
            self.PublicIPv6AddressInfo = PublicIPAddressInfo()
            self.PublicIPv6AddressInfo._deserialize(params.get("PublicIPv6AddressInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplateSpecification(AbstractModel):
    """IP address template

    """

    def __init__(self):
        r"""
        :param AddressId: IP address ID, such as `eipm-2uw6ujo6`.
        :type AddressId: str
        :param AddressGroupId: IP address group ID, such as `eipmg-2uw6ujo6`.
        :type AddressGroupId: str
        """
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
        


class AllocateAddressesRequest(AbstractModel):
    """AllocateAddresses request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param AddressCount: Number of EIPs. Default value: 1.
        :type AddressCount: int
        :param InternetServiceProvider: CMCC: China Mobile
CTCC: China Telecom
CUCC: China Unicom
        :type InternetServiceProvider: str
        :param InternetMaxBandwidthOut: 1–5000 Mbps. Default value: 1 Mbps.
        :type InternetMaxBandwidthOut: int
        :param Tags: List of tags to be bound.
        :type Tags: list of Tag
        :param InstanceId: ID of the instance to be bound.
        :type InstanceId: str
        :param NetworkInterfaceId: ID of the ENI to be bound, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. The ENI ID can be obtained from the `networkInterfaceId` field in the returned value of the `DescribeNetworkInterfaces` API.
        :type NetworkInterfaceId: str
        :param PrivateIpAddress: Private IP to be bound. If you specify `NetworkInterfaceId`, you must also specify `PrivateIpAddress`, which means to bind the EIP to the specified private IP of the specified ENI. You must also make sure that the specified `PrivateIpAddress` is a private IP of the specified `NetworkInterfaceId`. The private IP of the specified ENI can be obtained from the `privateIpAddress` field in the returned value of the `DescribeNetworkInterfaces` API.
        :type PrivateIpAddress: str
        """
        self.EcmRegion = None
        self.AddressCount = None
        self.InternetServiceProvider = None
        self.InternetMaxBandwidthOut = None
        self.Tags = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressCount = params.get("AddressCount")
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
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
        r"""
        :param AddressSet: List of unique IDs of the EIPs applied for.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressSet: list of str
        :param TaskId: Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
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


class Area(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param AreaId: Region ID
        :type AreaId: str
        :param AreaName: Region name
        :type AreaName: str
        """
        self.AreaId = None
        self.AreaName = None


    def _deserialize(self, params):
        self.AreaId = params.get("AreaId")
        self.AreaName = params.get("AreaName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6AddressesRequest(AbstractModel):
    """AssignIpv6Addresses request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param NetworkInterfaceId: ENI instance ID, such as `eni-1snva0vd`. Currently, only the primary ENI will be assigned the ID.
        :type NetworkInterfaceId: str
        :param Ipv6Addresses: List of specified IPv6 addresses. You can specify up to 10 IPv6 addresses at a time. The quota is calculated together with that of `Ipv6AddressCount`, a required input parameter alternative to this one.
        :type Ipv6Addresses: list of Ipv6Address
        :param Ipv6AddressCount: Number of automatically assigned IPv6 addresses. The total number of private IP addresses cannot exceed the quota. The quota is calculated together with that of `Ipv6Addresses`, a required input parameter alternative to this one.
        :type Ipv6AddressCount: int
        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param Ipv6AddressSet: List of IPv6 addresses assigned to ENIs.
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


class AssignPrivateIpAddressesRequest(AbstractModel):
    """AssignPrivateIpAddresses request structure.

    """

    def __init__(self):
        r"""
        :param NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param PrivateIpAddresses: Information of the specified private IPs. You can specify up to 10 IPs at a time. You must provide either this parameter or `SecondaryPrivateIpAddressCount`, or both.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param SecondaryPrivateIpAddressCount: Number of private IP addresses applied for. You must provide either this parameter or `PrivateIpAddresses`, or both. The total number of private IP addresses cannot exceed the quota.
        :type SecondaryPrivateIpAddressCount: int
        """
        self.NetworkInterfaceId = None
        self.EcmRegion = None
        self.PrivateIpAddresses = None
        self.SecondaryPrivateIpAddressCount = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param PrivateIpAddressSet: Private IP details.
Note: this field may return null, indicating that no valid values can be obtained.
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
    """Secondary CIDR information of the VPC.

    """

    def __init__(self):
        r"""
        :param VpcId: VPC instance ID, such as `vpc-6v2ht8q5`
        :type VpcId: str
        :param CidrBlock: Secondary CIDR, such as `172.16.0.0/16`
        :type CidrBlock: str
        :param AssistantType: Secondary CIDR block type. 0: general secondary CIDR block; 1: container secondary CIDR block. Default value: 0.
        :type AssistantType: int
        :param SubnetSet: Subnets divided by the secondary CIDR block.
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
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
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param AddressId: Unique EIP ID, such as `eip-11112222`.
        :type AddressId: str
        :param InstanceId: ID of the instance to be bound.
        :type InstanceId: str
        :param NetworkInterfaceId: ID of the ENI to be bound, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. The ENI ID can be obtained from the `networkInterfaceId` field in the returned value of the `DescribeNetworkInterfaces` API.
        :type NetworkInterfaceId: str
        :param PrivateIpAddress: Private IP to be bound. If you specify `NetworkInterfaceId`, you must also specify `PrivateIpAddress`, which means to bind the EIP to the specified private IP of the specified ENI. You must also make sure that the specified `PrivateIpAddress` is a private IP of the specified `NetworkInterfaceId`. The private IP of the specified ENI can be obtained from the `privateIpAddress` field in the returned value of the `DescribeNetworkInterfaces` API.
        :type PrivateIpAddress: str
        """
        self.EcmRegion = None
        self.AddressId = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressId = params.get("AddressId")
        self.InstanceId = params.get("InstanceId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
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
        r"""
        :param TaskId: Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param SecurityGroupIds: ID of the security group to be bound, such as `esg-efil73jd`. You can bind only one security group.
        :type SecurityGroupIds: list of str
        :param InstanceIds: ID of the bound instance, such as `ein-lesecurk`. You can specify multiple instances and request up to 100 instances at a time.
        :type InstanceIds: list of str
        """
        self.SecurityGroupIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param InstanceId: Instance ID, such as `ein-r8hr2upy`.
        :type InstanceId: str
        :param EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        """
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Backend(AbstractModel):
    """CLB backend information

    """

    def __init__(self):
        r"""
        :param InstanceId: Unique real server ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param Port: Listening port of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param Weight: Forwarding weight of the real server. Value range: [0, 100]. Default value: 10.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param PrivateIpAddresses: Private IP of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param RegisteredTime: Real server binding time
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegisteredTime: str
        :param EniId: Unique ENI ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type EniId: str
        :param PublicIpAddresses: Public IP of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param InstanceName: Real server instance name
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        """
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PrivateIpAddresses = None
        self.RegisteredTime = None
        self.EniId = None
        self.PublicIpAddresses = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.RegisteredTime = params.get("RegisteredTime")
        self.EniId = params.get("EniId")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsRequest(AbstractModel):
    """BatchDeregisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param Targets: Unbound targets
        :type Targets: list of BatchTarget
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsResponse(AbstractModel):
    """BatchDeregisterTargets response structure.

    """

    def __init__(self):
        r"""
        :param FailListenerIdSet: IDs of the listeners failed to be unbound
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailListenerIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ModifyList: List of weights to be modified in batches
        :type ModifyList: list of TargetsWeightRule
        """
        self.LoadBalancerId = None
        self.ModifyList = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModifyList") is not None:
            self.ModifyList = []
            for item in params.get("ModifyList"):
                obj = TargetsWeightRule()
                obj._deserialize(item)
                self.ModifyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTargetWeightResponse(AbstractModel):
    """BatchModifyTargetWeight response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param Targets: Bound targets
        :type Targets: list of BatchTarget
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterTargetsResponse(AbstractModel):
    """BatchRegisterTargets response structure.

    """

    def __init__(self):
        r"""
        :param FailListenerIdSet: IDs of the listeners failed to be bound. If this parameter is empty, all listeners have been bound successfully.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailListenerIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchTarget(AbstractModel):
    """CLB batch targets

    """

    def __init__(self):
        r"""
        :param ListenerId: Listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param Port: Bound port
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param InstanceId: CVM instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param EniIp: ENI IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type EniIp: str
        :param Weight: Weight of the CVM instance. Value range: [0, 100]. If it is not specified for binding the instance, 10 will be used by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        """
        self.ListenerId = None
        self.Port = None
        self.InstanceId = None
        self.EniIp = None
        self.Weight = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.EniIp = params.get("EniIp")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class City(AbstractModel):
    """City information

    """

    def __init__(self):
        r"""
        :param CityId: City ID
        :type CityId: str
        :param CityName: City name
        :type CityName: str
        """
        self.CityId = None
        self.CityName = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.CityName = params.get("CityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Country(AbstractModel):
    """Country/Region information

    """

    def __init__(self):
        r"""
        :param CountryId: Country/Region ID
        :type CountryId: str
        :param CountryName: Country/Region name
        :type CountryName: str
        """
        self.CountryId = None
        self.CountryName = None


    def _deserialize(self, params):
        self.CountryId = params.get("CountryId")
        self.CountryName = params.get("CountryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHaVipRequest(AbstractModel):
    """CreateHaVip request structure.

    """

    def __init__(self):
        r"""
        :param VpcId: VPC ID of the HAVIP.
        :type VpcId: str
        :param SubnetId: Subnet ID of the HAVIP.
        :type SubnetId: str
        :param HaVipName: HAVIP name.
        :type HaVipName: str
        :param Vip: The specified virtual IP address, which must be within the IP range of the VPC and not in use. It will be automatically assigned if not specified.
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
        r"""
        :param HaVip: HAVIP object.
        :type HaVip: :class:`tencentcloud.ecm.v20190719.models.HaVip`
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


class CreateImageRequest(AbstractModel):
    """CreateImage request structure.

    """

    def __init__(self):
        r"""
        :param ImageName: Image name.
        :type ImageName: str
        :param InstanceId: ID of the instance for which to make an image.
        :type InstanceId: str
        :param ImageDescription: Image description.
        :type ImageDescription: str
        :param ForcePoweroff: Whether to perform a forced shutdown to make an image. Valid values:
TRUE: yes
FALSE: no
Default value: FALSE.
        :type ForcePoweroff: str
        """
        self.ImageName = None
        self.InstanceId = None
        self.ImageDescription = None
        self.ForcePoweroff = None


    def _deserialize(self, params):
        self.ImageName = params.get("ImageName")
        self.InstanceId = params.get("InstanceId")
        self.ImageDescription = params.get("ImageDescription")
        self.ForcePoweroff = params.get("ForcePoweroff")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    """CreateImage response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair request structure.

    """

    def __init__(self):
        r"""
        :param KeyName: Key pair name, which can contain up to 25 digits, letters, and underscores.
        :type KeyName: str
        """
        self.KeyName = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyPairResponse(AbstractModel):
    """CreateKeyPair response structure.

    """

    def __init__(self):
        r"""
        :param KeyPair: Key pair information.
        :type KeyPair: :class:`tencentcloud.ecm.v20190719.models.KeyPair`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyPair = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyPair") is not None:
            self.KeyPair = KeyPair()
            self.KeyPair._deserialize(params.get("KeyPair"))
        self.RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    """CreateListener request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param Ports: Specifies for which ports to create listeners. Each port corresponds to a new listener
        :type Ports: list of int
        :param Protocol: Listener protocol. Valid values: TCP, UDP
        :type Protocol: str
        :param ListenerNames: List of names of the listeners to be created. The array of names and array of ports are in one-to-one correspondence. If you do not want to name them now, you do not need to provide this parameter.
        :type ListenerNames: list of str
        :param HealthCheck: Health check parameters
        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        :param SessionExpireTime: Session persistence time in seconds. Value range: 30–3600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.
        :type SessionExpireTime: int
        :param Scheduler: Forwarding method of the listener. Valid values: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR.
        :type Scheduler: str
        :param SessionType: Session persistence type. Valid values: NORMAL: the default session persistence type; QUIC_CID: session persistence by QUIC connection ID. The `QUIC_CID` value can only be configured in UDP listeners. If this field is not specified, the default session persistence type will be used.
        :type SessionType: str
        :param EndPorts: End ports of port ranges, which must be the same as `Ports` in length.
        :type EndPorts: list of int
        """
        self.LoadBalancerId = None
        self.Ports = None
        self.Protocol = None
        self.ListenerNames = None
        self.HealthCheck = None
        self.SessionExpireTime = None
        self.Scheduler = None
        self.SessionType = None
        self.EndPorts = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Ports = params.get("Ports")
        self.Protocol = params.get("Protocol")
        self.ListenerNames = params.get("ListenerNames")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.Scheduler = params.get("Scheduler")
        self.SessionType = params.get("SessionType")
        self.EndPorts = params.get("EndPorts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    """CreateListener response structure.

    """

    def __init__(self):
        r"""
        :param ListenerIds: Array of unique IDs of the created listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param LoadBalancerType: Network type of the CLB instance. Currently, you can pass in only `OPEN`, which indicates public network.
        :type LoadBalancerType: str
        :param VipIsp: CMCC: China Mobile; CTCC: China Telecom; CUCC: China Unicom.
        :type VipIsp: str
        :param LoadBalancerName: CLB instance name, which will take effect only when one instance is created. It can contain 1–50 letters, digits, hyphens, and underscores.
Note: if the name of the new CLB instance already exists, a default name will be generated automatically.
        :type LoadBalancerName: str
        :param VpcId: Network ID of the target device on the CLB backend, such as `vpc-12345678`.
        :type VpcId: str
        :param Number: Number of CLB instances to be created. Default value: 1.
        :type Number: int
        :param InternetAccessible: CLB information such as bandwidth limit.
        :type InternetAccessible: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        :param Tags: Tags.
        :type Tags: list of TagInfo
        :param SecurityGroups: Security groups.
        :type SecurityGroups: list of str
        """
        self.EcmRegion = None
        self.LoadBalancerType = None
        self.VipIsp = None
        self.LoadBalancerName = None
        self.VpcId = None
        self.Number = None
        self.InternetAccessible = None
        self.Tags = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.VipIsp = params.get("VipIsp")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.VpcId = params.get("VpcId")
        self.Number = params.get("Number")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = LoadBalancerInternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerIds: Array of CLB instance IDs
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.RequestId = params.get("RequestId")


class CreateModuleRequest(AbstractModel):
    """CreateModule request structure.

    """

    def __init__(self):
        r"""
        :param ModuleName: Module name, such as video live streaming module name. It cannot start with a space or exceed 60 characters.
        :type ModuleName: str
        :param DefaultBandWidth: Default bandwidth in Mbps. It cannot exceed the bandwidth range. For more information, see `DescribeConfig`.
        :type DefaultBandWidth: int
        :param DefaultImageId: Default image ID, such as `img-qsdf3ff2`.
        :type DefaultImageId: str
        :param InstanceType: Model ID.
        :type InstanceType: str
        :param DefaultSystemDiskSize: Default system disk size in GB. It is 50 GB by default and cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :type DefaultSystemDiskSize: int
        :param DefaultDataDiskSize: Default data disk size in GB. It cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :type DefaultDataDiskSize: int
        :param CloseIpDirect: Whether to disable IP direct access. Valid values:
true: yes
false: no
        :type CloseIpDirect: bool
        :param TagSpecification: List of tags.
        :type TagSpecification: list of TagSpecification
        :param SecurityGroups: List of default module security groups
        :type SecurityGroups: list of str
        :param DefaultBandWidthIn: Default inbound bandwidth in Mbps. It cannot exceed the bandwidth range. For more information, see `DescribeConfig`.
        :type DefaultBandWidthIn: int
        :param DisableWanIp: Whether to prohibit public IP assignment
        :type DisableWanIp: bool
        :param SystemDisk: System disk information.
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param DataDisks: Data disk information.
        :type DataDisks: list of DataDisk
        """
        self.ModuleName = None
        self.DefaultBandWidth = None
        self.DefaultImageId = None
        self.InstanceType = None
        self.DefaultSystemDiskSize = None
        self.DefaultDataDiskSize = None
        self.CloseIpDirect = None
        self.TagSpecification = None
        self.SecurityGroups = None
        self.DefaultBandWidthIn = None
        self.DisableWanIp = None
        self.SystemDisk = None
        self.DataDisks = None


    def _deserialize(self, params):
        self.ModuleName = params.get("ModuleName")
        self.DefaultBandWidth = params.get("DefaultBandWidth")
        self.DefaultImageId = params.get("DefaultImageId")
        self.InstanceType = params.get("InstanceType")
        self.DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self.DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        self.CloseIpDirect = params.get("CloseIpDirect")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.SecurityGroups = params.get("SecurityGroups")
        self.DefaultBandWidthIn = params.get("DefaultBandWidthIn")
        self.DisableWanIp = params.get("DisableWanIp")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModuleResponse(AbstractModel):
    """CreateModule response structure.

    """

    def __init__(self):
        r"""
        :param ModuleId: Module ID. It is the ID assigned to a module after it is created successfully.
        :type ModuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ModuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.RequestId = params.get("RequestId")


class CreateNetworkInterfaceRequest(AbstractModel):
    """CreateNetworkInterface request structure.

    """

    def __init__(self):
        r"""
        :param VpcId: VPC instance ID, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :type VpcId: str
        :param NetworkInterfaceName: ENI name, which can contain up to 60 bytes.
        :type NetworkInterfaceName: str
        :param SubnetId: Subnet instance ID of the ENI, such as 'subnet-0ap8nwca'.
        :type SubnetId: str
        :param EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param NetworkInterfaceDescription: ENI description. You can enter any information within 60 characters.
        :type NetworkInterfaceDescription: str
        :param SecondaryPrivateIpAddressCount: Number of private IP addresses applied for. The total number of private IP addresses cannot exceed the quota.
        :type SecondaryPrivateIpAddressCount: int
        :param SecurityGroupIds: The security group to be bound with, such as ['sg-1dd51d'].
        :type SecurityGroupIds: list of str
        :param PrivateIpAddresses: Information of the specified private IPs. You can specify up to 10 IPs at a time.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param Tags: List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.NetworkInterfaceName = None
        self.SubnetId = None
        self.EcmRegion = None
        self.NetworkInterfaceDescription = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.PrivateIpAddresses = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.SubnetId = params.get("SubnetId")
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param NetworkInterface: ENI instance.
        :type NetworkInterface: :class:`tencentcloud.ecm.v20190719.models.NetworkInterface`
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
        r"""
        :param VpcId: ID of the VPC instance to be manipulated, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :type VpcId: str
        :param RouteTableName: Route table name, which can contain up to 60 bytes.
        :type RouteTableName: str
        :param EcmRegion: ECM region
        :type EcmRegion: str
        """
        self.VpcId = None
        self.RouteTableName = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.RouteTableName = params.get("RouteTableName")
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param RouteTable: Route table object
        :type RouteTable: :class:`tencentcloud.ecm.v20190719.models.RouteTable`
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
        r"""
        :param RouteTableId: Route table instance ID.
        :type RouteTableId: str
        :param Routes: Routing policy object to be created.
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
        r"""
        :param TotalCount: Number of added instances.
        :type TotalCount: int
        :param RouteTableSet: Route table object.
Note: this field may return null, indicating that no valid values can be obtained.
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
        r"""
        :param SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: Security group policy set.
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
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
        r"""
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
        r"""
        :param GroupName: Security group name, which can be customized with up to 60 characters.
        :type GroupName: str
        :param GroupDescription: Security group remarks, which can contain up to 100 characters.
        :type GroupDescription: str
        :param Tags: List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.GroupName = None
        self.GroupDescription = None
        self.Tags = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
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
        r"""
        :param SecurityGroup: Security group object.
        :type SecurityGroup: :class:`tencentcloud.ecm.v20190719.models.SecurityGroup`
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


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet request structure.

    """

    def __init__(self):
        r"""
        :param VpcId: ID of the VPC instance to be manipulated, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :type VpcId: str
        :param SubnetName: Subnet name, which can contain up to 60 bytes.
        :type SubnetName: str
        :param CidrBlock: Subnet IP address range. It must be within the VPC IP address range. Subnet IP address ranges cannot overlap with each other within the same VPC.
        :type CidrBlock: str
        :param Zone: AZ ID of the subnet. You can select different AZs for different subnets for cross-AZ disaster recovery.
        :type Zone: str
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param Tags: List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.Zone = None
        self.EcmRegion = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        self.EcmRegion = params.get("EcmRegion")
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
        


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet response structure.

    """

    def __init__(self):
        r"""
        :param Subnet: Subnet object.
        :type Subnet: :class:`tencentcloud.ecm.v20190719.models.Subnet`
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


class CreateVpcRequest(AbstractModel):
    """CreateVpc request structure.

    """

    def __init__(self):
        r"""
        :param VpcName: VPC name, which can contain up to 60 bytes.
        :type VpcName: str
        :param CidrBlock: VPC CIDR block, which must fall within the following private network IP ranges: 10.*.0.0/16, 172.[16-31].0.0/16, and 192.168.0.0/16.
        :type CidrBlock: str
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param EnableMulticast: Whether multicast is enabled. true: enabled; false: disabled. This parameter is not supported currently
        :type EnableMulticast: str
        :param DnsServers: DNS address (not supported currently). Up to 4 addresses can be supported.
        :type DnsServers: list of str
        :param DomainName: Domain name. This parameter is not supported currently
        :type DomainName: str
        :param Tags: List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        :param Description: Description
        :type Description: str
        """
        self.VpcName = None
        self.CidrBlock = None
        self.EcmRegion = None
        self.EnableMulticast = None
        self.DnsServers = None
        self.DomainName = None
        self.Tags = None
        self.Description = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.EcmRegion = params.get("EcmRegion")
        self.EnableMulticast = params.get("EnableMulticast")
        self.DnsServers = params.get("DnsServers")
        self.DomainName = params.get("DomainName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Description = params.get("Description")
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
        r"""
        :param Vpc: VPC object.
        :type Vpc: :class:`tencentcloud.ecm.v20190719.models.VpcInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Vpc = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self.Vpc = VpcInfo()
            self.Vpc._deserialize(params.get("Vpc"))
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Data disk information

    """

    def __init__(self):
        r"""
        :param DiskSize: Data disk size in GB.
        :type DiskSize: int
        :param DiskType: Data disk type. Valid values:
- LOCAL_BASIC: local disk
- CLOUD_PREMIUM: Premium Cloud Storage

Default value: LOCAL_BASIC.
        :type DiskType: str
        """
        self.DiskSize = None
        self.DiskType = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHaVipRequest(AbstractModel):
    """DeleteHaVip request structure.

    """

    def __init__(self):
        r"""
        :param HaVipId: Unique HAVIP ID, such as `havip-9o233uri`.
        :type HaVipId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageRequest(AbstractModel):
    """DeleteImage request structure.

    """

    def __init__(self):
        r"""
        :param ImageIDSet: List of image IDs.
        :type ImageIDSet: list of str
        """
        self.ImageIDSet = None


    def _deserialize(self, params):
        self.ImageIDSet = params.get("ImageIDSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageResponse(AbstractModel):
    """DeleteImage response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    """DeleteListener request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: ID of the listener to be deleted
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    """DeleteListener response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerIds: Array of IDs of the listeners to be deleted. If this parameter is left empty, all listeners of the CLB instance will be deleted
        :type ListenerIds: list of str
        """
        self.LoadBalancerId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerListenersResponse(AbstractModel):
    """DeleteLoadBalancerListeners response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerIds: Array of IDs of the CLB instances to be deleted. Array length limit: 20
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteModuleRequest(AbstractModel):
    """DeleteModule request structure.

    """

    def __init__(self):
        r"""
        :param ModuleId: Module ID, such as `em-qn46snq8`.
        :type ModuleId: str
        """
        self.ModuleId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModuleResponse(AbstractModel):
    """DeleteModule response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        """
        self.NetworkInterfaceId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
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
        r"""
        :param RouteTableId: Route table instance ID, such as `rtb-azd4dt1c`
        :type RouteTableId: str
        """
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
        r"""
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
        r"""
        :param RouteTableId: Unique route table ID.
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
        r"""
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
        r"""
        :param SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: Security group policy set. You can only delete one or more policies in one direction in one request. Both PolicyIndex-matching deletion and security group policy-matching deletion methods are supported. You can use only one matching method in one request.
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
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
        r"""
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
        r"""
        :param SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :type SecurityGroupId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param SnapshotIds: List of IDs of the snapshots to be deleted, which can be queried through [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :type SnapshotIds: list of str
        :param DeleteBindImages: Whether to force delete the images associated with the snapshot.
        :type DeleteBindImages: bool
        """
        self.SnapshotIds = None
        self.DeleteBindImages = None


    def _deserialize(self, params):
        self.SnapshotIds = params.get("SnapshotIds")
        self.DeleteBindImages = params.get("DeleteBindImages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param SubnetId: Subnet instance ID, which can be obtained from the `SubnetId` field in the returned value of the `DescribeSubnets` API.
        :type SubnetId: str
        :param EcmRegion: ECM region
        :type EcmRegion: str
        """
        self.SubnetId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
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
        r"""
        :param VpcId: VPC instance ID, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :type VpcId: str
        :param EcmRegion: ECM region
        :type EcmRegion: str
        """
        self.VpcId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAddressQuotaRequest(AbstractModel):
    """DescribeAddressQuota request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        """
        self.EcmRegion = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressQuotaResponse(AbstractModel):
    """DescribeAddressQuota response structure.

    """

    def __init__(self):
        r"""
        :param QuotaSet: Quota information of EIPs in the account.
        :type QuotaSet: list of EipQuota
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = EipQuota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressesRequest(AbstractModel):
    """DescribeAddresses request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param AddressIds: List of unique IDs of EIPs, such as `eip-11112222`. `AddressIds` and `Filters` cannot be specified at the same time.
        :type AddressIds: list of str
        :param Filters: Each request can contain up to 10 `Filters` and 5 `Filter.Values`. `AddressIds` and `Filters` cannot be specified at the same time. The detailed filters are as follows:
address-id - String - Required: no - (Filter) Filter by unique EIP ID, such as `eip-11112222`.
address-name - String - Required: no - (Filter) Filter by EIP name. Fuzzy filtering is not supported.
address-ip - String - Required: no - (Filter) Filter by EIP IP address.
address-status - String - Required: no - (Filter) Filter by EIP status. Value range: see the list of EIP status.
instance-id - String - Required: no - (Filter) Filter by the ID of the instance bound to the EIP, such as `ins-11112222`.
private-ip-address - String - Required: no - (Filter) Filter by the private IP bound to the EIP.
network-interface-id - String - Required: no - (Filter) Filter by ID of the ENI bound to the EIP, such as `eni-11112222`.
is-arrears - String - Required: no - (Filter) Filter by whether the EIP is overdue (TRUE: the EIP is overdue | FALSE: the billing status of the EIP is normal)
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.EcmRegion = None
        self.AddressIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param TotalCount: Number of eligible EIPs.
        :type TotalCount: int
        :param AddressSet: List of EIP details.
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


class DescribeBaseOverviewRequest(AbstractModel):
    """DescribeBaseOverview request structure.

    """


class DescribeBaseOverviewResponse(AbstractModel):
    """DescribeBaseOverview response structure.

    """

    def __init__(self):
        r"""
        :param ModuleNum: Number of modules
        :type ModuleNum: int
        :param NodeNum: Number of nodes
        :type NodeNum: int
        :param VcpuNum: Number of CPU cores
        :type VcpuNum: int
        :param MemoryNum: Memory size in GB
        :type MemoryNum: int
        :param StorageNum: Disk size in GB
        :type StorageNum: int
        :param NetworkNum: Yesterday's network peak in Mbps
        :type NetworkNum: int
        :param InstanceNum: Number of instances
        :type InstanceNum: int
        :param RunningNum: Number of running instances
        :type RunningNum: int
        :param IsolationNum: Number of isolated instances
        :type IsolationNum: int
        :param ExpiredNum: Number of expired instances
        :type ExpiredNum: int
        :param WillExpireNum: Number of instances about to expire
        :type WillExpireNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ModuleNum = None
        self.NodeNum = None
        self.VcpuNum = None
        self.MemoryNum = None
        self.StorageNum = None
        self.NetworkNum = None
        self.InstanceNum = None
        self.RunningNum = None
        self.IsolationNum = None
        self.ExpiredNum = None
        self.WillExpireNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModuleNum = params.get("ModuleNum")
        self.NodeNum = params.get("NodeNum")
        self.VcpuNum = params.get("VcpuNum")
        self.MemoryNum = params.get("MemoryNum")
        self.StorageNum = params.get("StorageNum")
        self.NetworkNum = params.get("NetworkNum")
        self.InstanceNum = params.get("InstanceNum")
        self.RunningNum = params.get("RunningNum")
        self.IsolationNum = params.get("IsolationNum")
        self.ExpiredNum = params.get("ExpiredNum")
        self.WillExpireNum = params.get("WillExpireNum")
        self.RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig request structure.

    """


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig response structure.

    """

    def __init__(self):
        r"""
        :param NetworkStorageRange: Range of the network bandwidth disk size.
        :type NetworkStorageRange: :class:`tencentcloud.ecm.v20190719.models.NetworkStorageRange`
        :param ImageWhiteSet: Image OS allowlist.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageWhiteSet: list of str
        :param InstanceNetworkLimitConfigs: Network quota information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceNetworkLimitConfigs: list of InstanceNetworkLimitConfig
        :param ImageLimits: Image quota information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageLimits: :class:`tencentcloud.ecm.v20190719.models.ImageLimitConfig`
        :param DefaultIPDirect: Default IP direct access, used in scenarios with direct access parameters such as module creation and virtual machine purchase.
        :type DefaultIPDirect: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NetworkStorageRange = None
        self.ImageWhiteSet = None
        self.InstanceNetworkLimitConfigs = None
        self.ImageLimits = None
        self.DefaultIPDirect = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkStorageRange") is not None:
            self.NetworkStorageRange = NetworkStorageRange()
            self.NetworkStorageRange._deserialize(params.get("NetworkStorageRange"))
        self.ImageWhiteSet = params.get("ImageWhiteSet")
        if params.get("InstanceNetworkLimitConfigs") is not None:
            self.InstanceNetworkLimitConfigs = []
            for item in params.get("InstanceNetworkLimitConfigs"):
                obj = InstanceNetworkLimitConfig()
                obj._deserialize(item)
                self.InstanceNetworkLimitConfigs.append(obj)
        if params.get("ImageLimits") is not None:
            self.ImageLimits = ImageLimitConfig()
            self.ImageLimits._deserialize(params.get("ImageLimits"))
        self.DefaultIPDirect = params.get("DefaultIPDirect")
        self.RequestId = params.get("RequestId")


class DescribeCustomImageTaskRequest(AbstractModel):
    """DescribeCustomImageTask request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Supports querying by key and value.
task-id: async task ID
image-id: image ID
image-name: image name
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
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
        


class DescribeCustomImageTaskResponse(AbstractModel):
    """DescribeCustomImageTask response structure.

    """

    def __init__(self):
        r"""
        :param ImageTaskSet: Import task details
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageTaskSet: list of ImageTask
        :param TotalCount: Total number
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ImageTaskSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageTaskSet") is not None:
            self.ImageTaskSet = []
            for item in params.get("ImageTaskSet"):
                obj = ImageTask()
                obj._deserialize(item)
                self.ImageTaskSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDefaultSubnetRequest(AbstractModel):
    """DescribeDefaultSubnet request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param Zone: ECM AZ
        :type Zone: str
        """
        self.EcmRegion = None
        self.Zone = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultSubnetResponse(AbstractModel):
    """DescribeDefaultSubnet response structure.

    """

    def __init__(self):
        r"""
        :param Subnet: Default subnet information. If there is no subnet, this parameter will be empty.
        :type Subnet: :class:`tencentcloud.ecm.v20190719.models.Subnet`
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


class DescribeHaVipsRequest(AbstractModel):
    """DescribeHaVips request structure.

    """

    def __init__(self):
        r"""
        :param HaVipIds: Array of unique HAVIP IDs, such as `havip-9o233uri`.
        :type HaVipIds: list of str
        :param Filters: Filter. `HaVipIds` and `Filters` cannot be specified at the same time.
havip-id - String - Unique HAVIP ID, such as `havip-9o233uri`.
havip-name - String - HAVIP name.
vpc-id - String - VPC ID of the HAVIP.
subnet-id - String - Subnet ID of the HAVIP.
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param EcmRegion: ECM region. If this parameter is left empty, it will indicate all regions.
        :type EcmRegion: str
        """
        self.HaVipIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None


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
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param TotalCount: Number of eligible objects.
        :type TotalCount: int
        :param HaVipSet: Array of HAVIP objects.
Note: this field may return null, indicating that no valid values can be obtained.
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


class DescribeImageRequest(AbstractModel):
    """DescribeImage request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter. Each request can contain up to 10 `Filters`. The detailed filters are as follows:
image-id - String - Required: no - (Filter) Filter by image ID.
image-type - String - Required: no - (Filter) Filter by image type. Valid values:
PRIVATE_IMAGE: private image created by the current account 
PUBLIC_IMAGE: public image created by Tencent Cloud
instance-type -String - Required: no - (Filter) Filter supported images by model.
image-name - String - Required: no - (Filter) Fuzzy match by image name. You can provide only one value.
image-os - String - Required: no - (Filter) Fuzzy match by image system name. You can provide only one value.
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API overview.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API overview.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageResponse(AbstractModel):
    """DescribeImage response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of images
        :type TotalCount: int
        :param ImageSet: Image array
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageSet: list of Image
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSet") is not None:
            self.ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self.ImageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImportImageOsRequest(AbstractModel):
    """DescribeImportImageOs request structure.

    """


class DescribeImportImageOsResponse(AbstractModel):
    """DescribeImportImageOs response structure.

    """

    def __init__(self):
        r"""
        :param ImportImageOsListSupported: Supported OS types of imported images.
        :type ImportImageOsListSupported: :class:`tencentcloud.ecm.v20190719.models.ImageOsList`
        :param ImportImageOsVersionSet: Supported OS versions of imported images.
        :type ImportImageOsVersionSet: list of OsVersion
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ImportImageOsListSupported = None
        self.ImportImageOsVersionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImportImageOsListSupported") is not None:
            self.ImportImageOsListSupported = ImageOsList()
            self.ImportImageOsListSupported._deserialize(params.get("ImportImageOsListSupported"))
        if params.get("ImportImageOsVersionSet") is not None:
            self.ImportImageOsVersionSet = []
            for item in params.get("ImportImageOsVersionSet"):
                obj = OsVersion()
                obj._deserialize(item)
                self.ImportImageOsVersionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTypeConfigRequest(AbstractModel):
    """DescribeInstanceTypeConfig request structure.

    """


class DescribeInstanceTypeConfigResponse(AbstractModel):
    """DescribeInstanceTypeConfig response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param InstanceTypeConfigSet: Model configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceTypeConfigSet") is not None:
            self.InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self.InstanceTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceVncUrlRequest(AbstractModel):
    """DescribeInstanceVncUrl request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID, which can be obtained from the `InstanceId` field in the returned value of the `DescribeInstances` API.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceVncUrlResponse(AbstractModel):
    """DescribeInstanceVncUrl response structure.

    """

    def __init__(self):
        r"""
        :param InstanceVncUrl: Instance VNC URL.
        :type InstanceVncUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceVncUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceVncUrl = params.get("InstanceVncUrl")
        self.RequestId = params.get("RequestId")


class DescribeInstancesDeniedActionsRequest(AbstractModel):
    """DescribeInstancesDeniedActions request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: None
        :type InstanceIdSet: list of str
        """
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDeniedActionsResponse(AbstractModel):
    """DescribeInstancesDeniedActions response structure.

    """

    def __init__(self):
        r"""
        :param InstanceOperatorSet: Prohibited operations for the instance
        :type InstanceOperatorSet: list of InstanceOperator
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceOperatorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceOperatorSet") is not None:
            self.InstanceOperatorSet = []
            for item in params.get("InstanceOperatorSet"):
                obj = InstanceOperator()
                obj._deserialize(item)
                self.InstanceOperatorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter.
zone      String      Required: no     (Filter) Filter by AZ abbreviation.
zone-name      String      Required: no     (Filter) Filter by AZ name. Fuzzy match is supported.
module-id      String      Required: no     (Filter) Filter by module ID.
instance-id      String      Required: no      (Filter) Filter by instance ID.
instance-name      String      Required: no      (Filter) Filter by instance name. Fuzzy match is supported.
ip-address      String      Required: no      (Filter) Filter by the instance's private/public IP.
instance-uuid   string Required: no (Filter) Filter instances by `uuid`.
instance-state  string  Required: no (Filter) Update instances by instance status.
internet-service-provider      String      Required: no      (Filter) Filter by the ISP of the instance's public IP.
tag-key      String      Required: no      (Filter) Filter by tag key.
tag:tag-key      String      Required: no      (Filter) Filter by tag key-value pair. Replace `tag-key` with the specific tag key.
instance-family      String      Required: no      (Filter) Filter by model family.
module-name      String      Required: no      (Filter) Filter by module name. Fuzzy match is supported.
image-id      String      Required: no      (Filter) Filter by instance image ID.
vpc-id String      Required: no      (Filter) Filter by instance VPC ID.
subnet-id String      Required: no      (Filter) Filter by instance subnet ID.

If the `Filters` parameter is not specified, the information of all relevant instances will be queried.
Each request can contain up to 5 `Filter.Values`.
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20 (if the number of query results is greater than or equal to 20). Maximum value: 100.
        :type Limit: int
        :param OrderByField: Specified sort by field. Currently, valid values are as follows:
timestamp: sort by instance creation time.
Note: you can sort only by creation time currently. More sort criteria may be supported in the future.
If this parameter is not specified, instances will be sorted by creation time by default.
        :type OrderByField: str
        :param OrderDirection: Sorting order. 0: descending; 1: ascending. If this parameter is not specified, it will be descending by default.
        :type OrderDirection: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderByField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByField = params.get("OrderByField")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Length of the list of the returned instance information.
        :type TotalCount: int
        :param InstanceSet: List of the returned instance information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceSet: list of Instance
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
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerIds: Array of IDs of the CLB listeners to be queried
        :type ListenerIds: list of str
        :param Protocol: Protocol type of the listener to be queried. Valid values: TCP, UDP.
        :type Protocol: str
        :param Port: Port of the listener to be queried
        :type Port: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners response structure.

    """

    def __init__(self):
        r"""
        :param Listeners: List of listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :type Listeners: list of Listener
        :param TotalCount: Total number of listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Listeners = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalanceTaskStatusRequest(AbstractModel):
    """DescribeLoadBalanceTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Request ID, i.e., the `RequestId` parameter returned by the API
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalanceTaskStatusResponse(AbstractModel):
    """DescribeLoadBalanceTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: Current task status. 0: succeeded; 1: failed; 2: in progress.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: Region. If this parameter is not specified, the information of all regions will be queried by default.
        :type EcmRegion: str
        :param LoadBalancerIds: CLB instance ID.
        :type LoadBalancerIds: list of str
        :param LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param LoadBalancerVips: VIP address of the CLB instance. There can be multiple addresses.
        :type LoadBalancerVips: list of str
        :param BackendPrivateIps: Private IP of the real server bound to the CLB.
        :type BackendPrivateIps: list of str
        :param Offset: Data offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned CLB instances. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param WithBackend: Whether the CLB instance is bound to a real server. 0: no; 1: yes; -1: query all. 
If this parameter is not specified, all will be queried by default.
        :type WithBackend: int
        :param VpcId: Unique VPC ID of the CLB instance, such as `vpc-bhqkbhdx`.
        :type VpcId: str
        :param Filters: Each request can contain up to 10 `Filters` and 100 `Filter.Values`. The detailed filters are as follows:
tag-key - String - Required: no - (Filter) Filter by tag key.
        :type Filters: list of Filter
        :param SecurityGroup: Security group.
        :type SecurityGroup: str
        """
        self.EcmRegion = None
        self.LoadBalancerIds = None
        self.LoadBalancerName = None
        self.LoadBalancerVips = None
        self.BackendPrivateIps = None
        self.Offset = None
        self.Limit = None
        self.WithBackend = None
        self.VpcId = None
        self.Filters = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.BackendPrivateIps = params.get("BackendPrivateIps")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.WithBackend = params.get("WithBackend")
        self.VpcId = params.get("VpcId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SecurityGroup = params.get("SecurityGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of eligible CLB instances. This value is independent of the `Limit` in the input parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param LoadBalancerSet: Array of returned CLB instances.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerSet: list of LoadBalancer
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoadBalancerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeModuleDetailRequest(AbstractModel):
    """DescribeModuleDetail request structure.

    """

    def __init__(self):
        r"""
        :param ModuleId: Module ID, such as `em-qn46snq8`.
        :type ModuleId: str
        """
        self.ModuleId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModuleDetailResponse(AbstractModel):
    """DescribeModuleDetail response structure.

    """

    def __init__(self):
        r"""
        :param Module: Module details. For more information, see `ModuleInfo` in the data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`
        :param ModuleCounter: Module statistics. For more information, see `ModuleCounterInfo` in the data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModuleCounter: :class:`tencentcloud.ecm.v20190719.models.ModuleCounter`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Module = None
        self.ModuleCounter = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Module") is not None:
            self.Module = Module()
            self.Module._deserialize(params.get("Module"))
        if params.get("ModuleCounter") is not None:
            self.ModuleCounter = ModuleCounter()
            self.ModuleCounter._deserialize(params.get("ModuleCounter"))
        self.RequestId = params.get("RequestId")


class DescribeModuleRequest(AbstractModel):
    """DescribeModule request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter.
module-name - string - Required: no - (Filter) Filter by module name.
module-id - string - Required: no - (Filter) Filter by module ID.
image-id      String      Required: no      (Filter) Filter by image ID.
instance-family      String      Required: no      (Filter) Filter by model family.
security-group-id - string Required: no - (Filter) Filter by ID of the security group bound to the module.
Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API overview.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API overview.
        :type Limit: int
        :param OrderByField: Specified sort by field. Currently, valid values are as follows:
instance-num: sort by the number of instances.
node-num: sort by the number of nodes.
timestamp: sort by instance creation time.
If this parameter is not specified, instances will be sorted by creation time by default.
        :type OrderByField: str
        :param OrderDirection: Sorting order. 0: descending; 1: ascending. If this parameter is not specified, it will be descending by default.
        :type OrderDirection: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderByField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByField = params.get("OrderByField")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModuleResponse(AbstractModel):
    """DescribeModule response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible modules.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ModuleItemSet: List of module details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModuleItemSet: list of ModuleItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ModuleItemSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ModuleItemSet") is not None:
            self.ModuleItemSet = []
            for item in params.get("ModuleItemSet"):
                obj = ModuleItem()
                obj._deserialize(item)
                self.ModuleItemSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMonthPeakNetworkRequest(AbstractModel):
    """DescribeMonthPeakNetwork request structure.

    """

    def __init__(self):
        r"""
        :param Month: Month (xxxx-xx), such as `2021-03`. Default value: the last month
        :type Month: str
        :param Filters: Filter
        :type Filters: list of Filter
        """
        self.Month = None
        self.Filters = None


    def _deserialize(self, params):
        self.Month = params.get("Month")
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
        


class DescribeMonthPeakNetworkResponse(AbstractModel):
    """DescribeMonthPeakNetwork response structure.

    """

    def __init__(self):
        r"""
        :param MonthNetWorkData: None
Note: this field may return null, indicating that no valid values can be obtained.
        :type MonthNetWorkData: list of MonthNetwork
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MonthNetWorkData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MonthNetWorkData") is not None:
            self.MonthNetWorkData = []
            for item in params.get("MonthNetWorkData"):
                obj = MonthNetwork()
                obj._deserialize(item)
                self.MonthNetWorkData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces request structure.

    """

    def __init__(self):
        r"""
        :param NetworkInterfaceIds: Queries the ID of the ENI instance, such as `eni-pxir56ns`. Each request supports a maximum of 100 instances. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.
        :type NetworkInterfaceIds: list of str
        :param Filters: Filter. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.
vpc-id - String - (Filter) VPC instance ID, such as `vpc-f49l6u0z`.
subnet-id - String - (Filter) Subnet instance ID, such as `subnet-f49l6u0z`.
network-interface-id - String - (Filter) ENI instance ID, such as `eni-5k56k7k7`.
attachment.instance-id - String - (Filter) ID of the bound CVM instance, such as `ein-3nqpdn3i`.
groups.security-group-id - String - (Filter) ID of the bound security group instance, such as `sg-f9ekbxeq`.
network-interface-name - String - (Filter) ENI instance name.
network-interface-description - String - (Filter) ENI instance description.
address-ip - String - (Filter) Private IPv4 address.
tag-key - String - Required: no - (Filter) Filter by tag key. For directions, see Sample 2.
tag:tag-key - String - Required: no - (Filter) Filter by tag key-value pair. Replace `tag-key` with the specific tag key. For directions, see Sample 3.
is-primary - Boolean - Required: no - (Filter) Filter by whether it is a primary ENI. true: filter only by primary ENI; false: filter only by secondary ENI. If this parameter is not specified, filtering by both primary and secondary ENIs will be used.
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        """
        self.NetworkInterfaceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None


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
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param NetworkInterfaceSet: List of instance details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetworkInterfaceSet: list of NetworkInterface
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.NetworkInterfaceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NetworkInterfaceSet") is not None:
            self.NetworkInterfaceSet = []
            for item in params.get("NetworkInterfaceSet"):
                obj = NetworkInterface()
                obj._deserialize(item)
                self.NetworkInterfaceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNodeRequest(AbstractModel):
    """DescribeNode request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter. InstanceFamily: instance family.
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
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
        


class DescribeNodeResponse(AbstractModel):
    """DescribeNode response structure.

    """

    def __init__(self):
        r"""
        :param NodeSet: List of node details
Note: this field may return null, indicating that no valid values can be obtained.
        :type NodeSet: list of Node
        :param TotalCount: Total number of nodes.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NodeSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = Node()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePackingQuotaGroupRequest(AbstractModel):
    """DescribePackingQuotaGroup request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter. Zone: AZ; InstanceType: instance type; DataDiskSize: data disk size.
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
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
        


class DescribePackingQuotaGroupResponse(AbstractModel):
    """DescribePackingQuotaGroup response structure.

    """

    def __init__(self):
        r"""
        :param PackingQuotaSet: Set of packing quotas.
        :type PackingQuotaSet: list of PackingQuotaGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PackingQuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PackingQuotaSet") is not None:
            self.PackingQuotaSet = []
            for item in params.get("PackingQuotaSet"):
                obj = PackingQuotaGroup()
                obj._deserialize(item)
                self.PackingQuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePeakBaseOverviewRequest(AbstractModel):
    """DescribePeakBaseOverview request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time (xxxx-xx-xx), such as `2019-08-14`. It is 7 days ago by default and should not be more than 90 days ago.
        :type StartTime: str
        :param EndTime: End time (xxxx-xx-xx), such as `2019-08-14`. It is yesterday by default and should not be more than 90 days ago. When the time period between the start time and end time is within 30 days, data at the 1-hour granularity will be returned; otherwise, data at the 3-hour granularity will be returned.
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePeakBaseOverviewResponse(AbstractModel):
    """DescribePeakBaseOverview response structure.

    """

    def __init__(self):
        r"""
        :param PeakFamilyInfoSet: List of basic peaks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeakFamilyInfoSet: list of PeakFamilyInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PeakFamilyInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PeakFamilyInfoSet") is not None:
            self.PeakFamilyInfoSet = []
            for item in params.get("PeakFamilyInfoSet"):
                obj = PeakFamilyInfo()
                obj._deserialize(item)
                self.PeakFamilyInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePeakNetworkOverviewRequest(AbstractModel):
    """DescribePeakNetworkOverview request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time (xxxx-xx-xx), such as `2019-08-14`. It is 7 days ago by default and should not be more than 30 days ago.
        :type StartTime: str
        :param EndTime: End time (xxxx-xx-xx), such as `2019-08-14`. It is yesterday by default and should not be more than 30 days ago. When the time period between the start time and end time is within 1 day, data at the 1-minute granularity will be returned; when the time period is within 7 days, data at the 5-minute granularity will be returned; otherwise, data at the 1-hour granularity will be returned.
        :type EndTime: str
        :param Filters: Filter.

region    String      Required: no     (Filter) Filter by region. Fuzzy match is not supported. Note: you need to enter the ECM region to be queried before data can be returned.
area       String      Required: no     (Filter) Filter by region. Fuzzy match is not supported. Regions include `china-central`, `china-east`, etc. You can call `DescribeNode` to get the information of all regions. You can also use `ALL_REGION` to indicate all regions.
isp         String      Required: no     (Filter) Filter region traffic by ISP. ISPs include CTCC, CUCC, and CMCC. This parameter must be used together with `area`, and you can specify only one ISP at a time.

You can specify either `region` or `area`.
        :type Filters: list of Filter
        :param Period: Statistical period in seconds. Valid values: 60, 300.
        :type Period: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Filters = None
        self.Period = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePeakNetworkOverviewResponse(AbstractModel):
    """DescribePeakNetworkOverview response structure.

    """

    def __init__(self):
        r"""
        :param PeakNetworkRegionSet: Array of network peaks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeakNetworkRegionSet: list of PeakNetworkRegionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PeakNetworkRegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PeakNetworkRegionSet") is not None:
            self.PeakNetworkRegionSet = []
            for item in params.get("PeakNetworkRegionSet"):
                obj = PeakNetworkRegionInfo()
                obj._deserialize(item)
                self.PeakNetworkRegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePriceRunInstanceRequest(AbstractModel):
    """DescribePriceRunInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceType: Instance model information
        :type InstanceType: str
        :param SystemDisk: System disk information
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param InstanceCount: Number of instances
        :type InstanceCount: int
        :param DataDisk: Data disk information
        :type DataDisk: list of DataDisk
        """
        self.InstanceType = None
        self.SystemDisk = None
        self.InstanceCount = None
        self.DataDisk = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        self.InstanceCount = params.get("InstanceCount")
        if params.get("DataDisk") is not None:
            self.DataDisk = []
            for item in params.get("DataDisk"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisk.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePriceRunInstanceResponse(AbstractModel):
    """DescribePriceRunInstance response structure.

    """

    def __init__(self):
        r"""
        :param InstancePrice: Instance price information
        :type InstancePrice: :class:`tencentcloud.ecm.v20190719.models.InstancesPrice`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstancePrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = InstancesPrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        self.RequestId = params.get("RequestId")


class DescribeRouteConflictsRequest(AbstractModel):
    """DescribeRouteConflicts request structure.

    """

    def __init__(self):
        r"""
        :param RouteTableId: Route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        :param DestinationCidrBlocks: List of conflicting destination ports to be checked.
        :type DestinationCidrBlocks: list of str
        """
        self.RouteTableId = None
        self.DestinationCidrBlocks = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.DestinationCidrBlocks = params.get("DestinationCidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteConflictsResponse(AbstractModel):
    """DescribeRouteConflicts response structure.

    """

    def __init__(self):
        r"""
        :param RouteConflictSet: List of routing policy conflicts.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RouteConflictSet: list of RouteConflict
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RouteConflictSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteConflictSet") is not None:
            self.RouteConflictSet = []
            for item in params.get("RouteConflictSet"):
                obj = RouteConflict()
                obj._deserialize(item)
                self.RouteConflictSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteTablesRequest(AbstractModel):
    """DescribeRouteTables request structure.

    """

    def __init__(self):
        r"""
        :param RouteTableIds: Route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableIds: list of str
        :param Filters: Filter. `RouteTableIds` and `Filters` cannot be specified at the same time.
route-table-id - String - (Filter) Route table instance ID.
route-table-name - String - (Filter) Route table name.
vpc-id - String - (Filter) VPC instance ID, such as `vpc-f49l6u0z`.
association.main - String - (Filter) Whether it is the main route table.
        :type Filters: list of Filter
        :param Offset: Offset
        :type Offset: int
        :param Limit: Limit
        :type Limit: int
        :param EcmRegion: ECM region. If this parameter is left empty or not specified, it will indicate all regions.
        :type EcmRegion: str
        """
        self.RouteTableIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None


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
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param TotalCount: Number of eligible instances
        :type TotalCount: int
        :param RouteTableSet: List of route tables
Note: this field may return null, indicating that no valid values can be obtained.
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
        r"""
        :param SecurityGroupIds: Security instance ID, such as `esg-33ocnj9n`, which can be obtained through [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/1108/47697?from_cn_redirect=1).
        :type SecurityGroupIds: list of str
        """
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
        r"""
        :param SecurityGroupAssociationStatisticsSet: Statistics on the instances associated with the security group.
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


class DescribeSecurityGroupLimitsRequest(AbstractModel):
    """DescribeSecurityGroupLimits request structure.

    """


class DescribeSecurityGroupLimitsResponse(AbstractModel):
    """DescribeSecurityGroupLimits response structure.

    """

    def __init__(self):
        r"""
        :param SecurityGroupLimitSet: Security group quota limit.
        :type SecurityGroupLimitSet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupLimitSet`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecurityGroupLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupLimitSet") is not None:
            self.SecurityGroupLimitSet = SecurityGroupLimitSet()
            self.SecurityGroupLimitSet._deserialize(params.get("SecurityGroupLimitSet"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupPoliciesRequest(AbstractModel):
    """DescribeSecurityGroupPolicies request structure.

    """

    def __init__(self):
        r"""
        :param SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/1108/47697?from_cn_redirect=1).
        :type SecurityGroupId: str
        """
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
        r"""
        :param SecurityGroupPolicySet: Security group policy set.
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
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


class DescribeSecurityGroupsRequest(AbstractModel):
    """DescribeSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param SecurityGroupIds: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/1108/47697?from_cn_redirect=1). Each request supports a maximum of 100 instances. `SecurityGroupIds` and `Filters` cannot be specified at the same time.
        :type SecurityGroupIds: list of str
        :param Filters: Filter. `SecurityGroupIds` and `Filters` cannot be specified at the same time.
security-group-id - String - (Filter) Security group ID.
security-group-name - String - (Filter) Security group name.
tag-key - String - Required: no - (Filter) Filter by tag key.
tag:tag-key - String - Required: no - (Filter) Filter by tag key-value pair. Replace `tag-key` with the specific tag key.
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
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
        r"""
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param SecurityGroupSet: Security group object.
        :type SecurityGroupSet: list of SecurityGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.SecurityGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SecurityGroupSet") is not None:
            self.SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.SecurityGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param SnapshotIds: List of IDs of the snapshots to be queried. `SnapshotIds` and `Filters` cannot be specified at the same time.
        :type SnapshotIds: list of str
        :param Filters: Filter. `SnapshotIds` and `Filters` cannot be specified at the same time.<br><li>snapshot-id - Array of String - Required: no - (Filter) Filter by snapshot ID, such as `snap-11112222`.<br><li>snapshot-name - Array of String - Required: no - (Filter) Filter by snapshot name.<br><li>snapshot-state - Array of String - Required: no - (Filter) Filter by snapshot status. NORMAL: normal; CREATING: creating; ROLLBACKING: rolling back.<br><li>disk-usage - Array of String - Required: no - (Filter) Filter by the type of the cloud disk from which a snapshot is created. SYSTEM_DISK: system disk; DATA_DISK: data disk.<br><li>project-id  - Array of String - Required: no - (Filter) Filter by the project ID of the cloud disk.<br><li>disk-id  - Array of String - Required: no - (Filter) Filter by the ID of the cloud disk from which a snapshot is created.<br><li>zone - Array of String - Required: no - (Filter) Filter by [AZ](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo).<br><li>encrypt - Array of String - Required: no - (Filter) Filter by whether a snapshot is created from an encrypted cloud disk. TRUE: yes; FALSE: no.
<li>snapshot-type- Array of String - Required: no - (Filter) Filter by the snapshot type specified in `snapshot-type`.
(SHARED_SNAPSHOT: shared snapshot | PRIVATE_SNAPSHOT: private snapshot.)
        :type Filters: list of Filter
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param OrderField: Field by which snapshots are sorted. Valid values:<br><li>CREATE_TIME: sort by snapshot creation time<br>Snapshots are sorted by creation time by default.
        :type OrderField: str
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param Order: Sorting order of cloud disks. Valid values:<br><li>ASC: ascending<br><li>DESC: descending.
        :type Order: str
        """
        self.SnapshotIds = None
        self.Filters = None
        self.Limit = None
        self.OrderField = None
        self.Offset = None
        self.Order = None


    def _deserialize(self, params):
        self.SnapshotIds = params.get("SnapshotIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of snapshots.
        :type TotalCount: int
        :param SnapshotSet: List of snapshot details.
        :type SnapshotSet: list of Snapshot
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.SnapshotSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotSet") is not None:
            self.SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self.SnapshotSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets request structure.

    """

    def __init__(self):
        r"""
        :param SubnetIds: Subnet instance ID, such as `subnet-pxir56ns`. Each request supports a maximum of 100 instances. `SubnetIds` and `Filters` cannot be specified at the same time.
        :type SubnetIds: list of str
        :param Filters: Filter. `SubnetIds` and `Filters` cannot be specified at the same time.
subnet-id - String - Subnet instance name.
subnet-name - String - Subnet name. Only fuzzy query by a single value is supported.
cidr-block - String - Subnet IP address range, such as `192.168.1.0`. Only fuzzy query by a single value is supported.
vpc-id - String - VPC instance ID, such as `vpc-f49l6u0z`.
vpc-cidr-block  - String - VPC IP address range, such as `192.168.1.0`. Only fuzzy query by a single value is supported.
region - String - ECM region.
zone - String - AZ.
tag-key - String - Required: no - Filter by tag key.
tag:tag-key - String - Required: no - Filter by tag key-value pair.
        :type Filters: list of Filter
        :param Offset: Offset
        :type Offset: str
        :param Limit: Number of returned results.
        :type Limit: str
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param Sort: Sorting method. time: sort in reverse chronological order; default: sort by network planning.
        :type Sort: str
        """
        self.SubnetIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None
        self.Sort = None


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
        self.EcmRegion = params.get("EcmRegion")
        self.Sort = params.get("Sort")
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
        r"""
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param SubnetSet: Subnet object.
Note: this field may return null, indicating that no valid values can be obtained.
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


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerIds: List of IDs of CLB instances to be queried.
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancers: List of CLB instances.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancers: list of LoadBalancerHealth
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancers = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancerHealth()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerIds: List of listener IDs.
        :type ListenerIds: list of str
        :param Protocol: Listener protocol type.
        :type Protocol: int
        :param Port: Listener port.
        :type Port: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets response structure.

    """

    def __init__(self):
        r"""
        :param Listeners: Information of real servers bound to the listener.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Listeners: list of ListenerBackend
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerBackend()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param TaskId: Async task ID.
        :type TaskId: str
        """
        self.EcmRegion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.TaskId = params.get("TaskId")
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
        r"""
        :param TaskId: Async task ID.
        :type TaskId: str
        :param Result: Execution result. Valid values: SUCCESS; FAILED; RUNNING.
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


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param TaskSet: Task description.
        :type TaskSet: list of TaskInput
        """
        self.TaskSet = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskInput()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param TaskSet: Task description.
        :type TaskSet: list of TaskOutput
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskOutput()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs request structure.

    """

    def __init__(self):
        r"""
        :param VpcIds: VPC instance ID, such as `vpc-f49l6u0z`. Each request supports a maximum of 100 instances. `VpcIds` and `Filters` cannot be specified at the same time.
        :type VpcIds: list of str
        :param Filters: Filter. `VpcIds` and `Filters` cannot be specified at the same time.
vpc-name - String - VPC instance name. Only fuzzy query by a single value is supported.
vpc-id - String - VPC instance ID, such as `vpc-f49l6u0z`.
cidr-block - String - VPC CIDR. Only fuzzy query by a single value is supported.
region - String - VPC region.
tag-key - String - Required: no - Filter by tag key.
tag:tag-key - String - Required: no - Filter by tag key-value pair.
        :type Filters: list of Filter
        :param Offset: Offset
        :type Offset: int
        :param Limit: Number of returned results.
        :type Limit: int
        :param EcmRegion: Region
        :type EcmRegion: str
        :param Sort: Sorting method. time: sort in reverse chronological order; default: sort by network planning.
        :type Sort: str
        """
        self.VpcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None
        self.Sort = None


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
        self.EcmRegion = params.get("EcmRegion")
        self.Sort = params.get("Sort")
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
        r"""
        :param TotalCount: Number of eligible objects.
        :type TotalCount: int
        :param VpcSet: VPC object.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcSet: list of VpcInfo
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
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface request structure.

    """

    def __init__(self):
        r"""
        :param NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param InstanceId: Instance ID, such as `ein-hcs7jkg4`.
        :type InstanceId: str
        :param EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        """
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableRoutesRequest(AbstractModel):
    """DisableRoutes request structure.

    """

    def __init__(self):
        r"""
        :param RouteTableId: Unique route table ID.
        :type RouteTableId: str
        :param RouteIds: Routing policy ID.
        :type RouteIds: list of int non-negative
        """
        self.RouteTableId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRoutesResponse(AbstractModel):
    """DisableRoutes response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param AddressId: Unique EIP ID, such as `eip-11112222`.
        :type AddressId: str
        :param ReallocateNormalPublicIp: Indicates whether to assign a general public IP after unbinding an EIP. Valid values:
TRUE: yes
FALSE: no.
Default value: FALSE.

You can specify this parameter only under the following conditions:
You can specify this parameter only when you unbind an EIP from the primary private IP of the primary ENI.
An account can reassign a general public IP after unbinding an EIP 10 times a day. More information can be obtained through the `DescribeAddressQuota` API.
        :type ReallocateNormalPublicIp: bool
        """
        self.EcmRegion = None
        self.AddressId = None
        self.ReallocateNormalPublicIp = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param TaskId: Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: You can get available instance IDs in the following ways:
Log in to the console to query instance IDs.
Get the instance IDs from the `InstanceId` field in the information returned by the `DescribeInstances` API.
        :type InstanceIds: list of str
        :param KeyIds: List of key pair IDs. Each request can contain up to 100 key pairs. The key pair ID takes the form of `skey-11112222`.

You can get available key IDs in the following ways:
Log in to the console to query key IDs.
Get the key pair IDs from the `KeyId` field in the information returned by the `DescribeKeyPairs` API.
        :type KeyIds: list of str
        :param ForceStop: Whether to force shut down the running instance. We recommend you manually shut down the running instance before unbinding the key. Valid values:
TRUE: yes.
FALSE: no.

Default value: FALSE.
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.KeyIds = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.KeyIds = params.get("KeyIds")
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    """DisassociateInstancesKeyPairs response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param SecurityGroupIds: ID of the security group to be unbound, such as `esg-efil73jd`. You can unbind only one security group at a time.
        :type SecurityGroupIds: list of str
        :param InstanceIds: ID of the instance to be unbound, such as `ein-lesecurk`. You can specify multiple instances.
        :type InstanceIds: list of str
        """
        self.SecurityGroupIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DiskInfo(AbstractModel):
    """Disk information

    """

    def __init__(self):
        r"""
        :param DiskType: Disk type: LOCAL_BASIC.
        :type DiskType: str
        :param DiskId: Disk ID
        :type DiskId: str
        :param DiskSize: Disk size in GB
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipQuota(AbstractModel):
    """EIP quota information

    """

    def __init__(self):
        r"""
        :param QuotaId: Quota name. Valid values:
TOTAL_EIP_QUOTA: quota of EIPs in the current region;
DAILY_EIP_APPLY: today's number of applications in the current region;
DAILY_PUBLIC_IP_ASSIGN: number of public IP reassignments in the current region.
        :type QuotaId: str
        :param QuotaCurrent: Current quantity
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRoutesRequest(AbstractModel):
    """EnableRoutes request structure.

    """

    def __init__(self):
        r"""
        :param RouteTableId: Unique route table ID.
        :type RouteTableId: str
        :param RouteIds: Routing policy ID.
        :type RouteIds: list of int non-negative
        """
        self.RouteTableId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRoutesResponse(AbstractModel):
    """EnableRoutes response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """Enhanced service

    """

    def __init__(self):
        r"""
        :param SecurityService: Whether to enable CWP.
        :type SecurityService: :class:`tencentcloud.ecm.v20190719.models.RunSecurityServiceEnabled`
        :param MonitorService: Whether to enable CM.
        :type MonitorService: :class:`tencentcloud.ecm.v20190719.models.RunMonitorServiceEnabled`
        :param EIPDirectService: Whether to enable IP direct access. If this parameter is not specified, IP direct access will be enabled by default for Linux images and is currently not supported for Windows images.
        :type EIPDirectService: :class:`tencentcloud.ecm.v20190719.models.RunEIPDirectServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None
        self.EIPDirectService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))
        if params.get("EIPDirectService") is not None:
            self.EIPDirectService = RunEIPDirectServiceEnabled()
            self.EIPDirectService._deserialize(params.get("EIPDirectService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Key-Value pair filter for conditional filtering queries.

    """

    def __init__(self):
        r"""
        :param Values: One or more filter values.
        :type Values: list of str
        :param Name: Filter name.
        :type Name: str
        """
        self.Values = None
        self.Name = None


    def _deserialize(self, params):
        self.Values = params.get("Values")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HaVip(AbstractModel):
    """HAVIP object.

    """

    def __init__(self):
        r"""
        :param HaVipId: Unique HAVIP ID.
        :type HaVipId: str
        :param HaVipName: HAVIP name.
        :type HaVipName: str
        :param Vip: Virtual IP address.
        :type Vip: str
        :param VpcId: VPC ID of the HAVIP.
        :type VpcId: str
        :param SubnetId: Subnet ID of the HAVIP.
        :type SubnetId: str
        :param NetworkInterfaceId: ID of the ENI associated with the HAVIP.
        :type NetworkInterfaceId: str
        :param InstanceId: ID of the bound instance.
        :type InstanceId: str
        :param AddressIp: Bound EIP.
        :type AddressIp: str
        :param State: Status:
AVAILABLE: running.
UNBIND: unbound.
        :type State: str
        :param CreatedTime: Creation time.
        :type CreatedTime: str
        :param Business: ID of businesses that use HAVIP.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheck(AbstractModel):
    """CLB health check

    """

    def __init__(self):
        r"""
        :param HealthSwitch: Whether to enable health check. Valid values: 1: enable; 0: disable
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthSwitch: int
        :param TimeOut: Health check response timeout period in seconds. Value range: 2–60. Default value: 2. The value of this parameter should be smaller than the check interval.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeOut: int
        :param IntervalTime: Health check interval in seconds. Value range: 5–300. Default value: 5.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IntervalTime: int
        :param HealthNum: Health threshold. Value range: 2–10. Default value: 3, indicating that if a forward is found healthy three consecutive times, it will be considered normal.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthNum: int
        :param UnHealthyNum: Unhealthy threshold. Value range: 2–10. Default value: 3, indicating that if a forward is found unhealthy three consecutive times, it will be considered exceptional.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UnHealthyNum: int
        :param CheckPort: Health check port (a custom check parameter), which is the port of the real server by default. Unless you want to specify a port, we recommend you leave it empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CheckPort: int
        :param ContextType: Health check protocol (a custom check parameter), which is required if the value of `CheckType` is `CUSTOM`. This parameter represents the input format of the health check. Valid values: HEX, TEXT. If the value is `HEX`, the characters of `SendContext` and `RecvContext` can only be selected from `0123456789ABCDEF`, and the length must be an even number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContextType: str
        :param SendContext: Health check protocol (a custom check parameter), which is required if the value of `CheckType` is `CUSTOM`. This parameter represents the content of the request sent by the health check. It can contain up to 500 visible ASCII characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SendContext: str
        :param RecvContext: Health check protocol (a custom check parameter), which is required if the value of `CheckType` is `CUSTOM`. This parameter represents the result returned by the health check. It can contain up to 500 visible ASCII characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RecvContext: str
        :param CheckType: Health check protocol (a custom check parameter). Valid values: TCP, CUSTOM (applicable only to UDP listeners. If custom health check is used, this parameter will be required).
Note: this field may return null, indicating that no valid values can be obtained.
        :type CheckType: str
        """
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnHealthyNum = None
        self.CheckPort = None
        self.ContextType = None
        self.SendContext = None
        self.RecvContext = None
        self.CheckType = None


    def _deserialize(self, params):
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnHealthyNum = params.get("UnHealthyNum")
        self.CheckPort = params.get("CheckPort")
        self.ContextType = params.get("ContextType")
        self.SendContext = params.get("SendContext")
        self.RecvContext = params.get("RecvContext")
        self.CheckType = params.get("CheckType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISP(AbstractModel):
    """ISP information

    """

    def __init__(self):
        r"""
        :param ISPId: ISP ID
        :type ISPId: str
        :param ISPName: ISP name
        :type ISPName: str
        """
        self.ISPId = None
        self.ISPName = None


    def _deserialize(self, params):
        self.ISPId = params.get("ISPId")
        self.ISPName = params.get("ISPName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISPCounter(AbstractModel):
    """ISP statistics

    """

    def __init__(self):
        r"""
        :param ProviderName: ISP name
        :type ProviderName: str
        :param ProviderNodeNum: Number of nodes
        :type ProviderNodeNum: int
        :param ProvederInstanceNum: Number of instances
        :type ProvederInstanceNum: int
        :param ZoneInstanceInfoSet: Zone instance information structure array
        :type ZoneInstanceInfoSet: list of ZoneInstanceInfo
        """
        self.ProviderName = None
        self.ProviderNodeNum = None
        self.ProvederInstanceNum = None
        self.ZoneInstanceInfoSet = None


    def _deserialize(self, params):
        self.ProviderName = params.get("ProviderName")
        self.ProviderNodeNum = params.get("ProviderNodeNum")
        self.ProvederInstanceNum = params.get("ProvederInstanceNum")
        if params.get("ZoneInstanceInfoSet") is not None:
            self.ZoneInstanceInfoSet = []
            for item in params.get("ZoneInstanceInfoSet"):
                obj = ZoneInstanceInfo()
                obj._deserialize(item)
                self.ZoneInstanceInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    """Image information

    """

    def __init__(self):
        r"""
        :param ImageId: Image ID
        :type ImageId: str
        :param ImageName: Image name
        :type ImageName: str
        :param ImageState: Image status
        :type ImageState: str
        :param ImageType: Image type
        :type ImageType: str
        :param ImageOsName: OS name
        :type ImageOsName: str
        :param ImageDescription: Image description
        :type ImageDescription: str
        :param ImageCreateTime: Image import time
        :type ImageCreateTime: str
        :param Architecture: Number of bits of the OS
        :type Architecture: str
        :param OsType: OS type
        :type OsType: str
        :param OsVersion: OS version
        :type OsVersion: str
        :param Platform: OS platform
        :type Platform: str
        :param ImageOwner: Image owner
        :type ImageOwner: int
        :param ImageSize: Image size in GB
        :type ImageSize: int
        :param SrcImage: Image source information
        :type SrcImage: :class:`tencentcloud.ecm.v20190719.models.SrcImage`
        :param ImageSource: Image source type
        :type ImageSource: str
        :param TaskId: ID of the task in intermediate or failed status
        :type TaskId: str
        :param IsSupportCloudInit: Whether cloud-init is supported
        :type IsSupportCloudInit: bool
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageState = None
        self.ImageType = None
        self.ImageOsName = None
        self.ImageDescription = None
        self.ImageCreateTime = None
        self.Architecture = None
        self.OsType = None
        self.OsVersion = None
        self.Platform = None
        self.ImageOwner = None
        self.ImageSize = None
        self.SrcImage = None
        self.ImageSource = None
        self.TaskId = None
        self.IsSupportCloudInit = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageState = params.get("ImageState")
        self.ImageType = params.get("ImageType")
        self.ImageOsName = params.get("ImageOsName")
        self.ImageDescription = params.get("ImageDescription")
        self.ImageCreateTime = params.get("ImageCreateTime")
        self.Architecture = params.get("Architecture")
        self.OsType = params.get("OsType")
        self.OsVersion = params.get("OsVersion")
        self.Platform = params.get("Platform")
        self.ImageOwner = params.get("ImageOwner")
        self.ImageSize = params.get("ImageSize")
        if params.get("SrcImage") is not None:
            self.SrcImage = SrcImage()
            self.SrcImage._deserialize(params.get("SrcImage"))
        self.ImageSource = params.get("ImageSource")
        self.TaskId = params.get("TaskId")
        self.IsSupportCloudInit = params.get("IsSupportCloudInit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageLimitConfig(AbstractModel):
    """Image size configuration

    """

    def __init__(self):
        r"""
        :param MaxImageSize: Supported maximum image size in GB, including custom image size for import and central cloud image size.
        :type MaxImageSize: int
        """
        self.MaxImageSize = None


    def _deserialize(self, params):
        self.MaxImageSize = params.get("MaxImageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOsList(AbstractModel):
    """Supported OS type. Valid values: Windows, Linux.

    """

    def __init__(self):
        r"""
        :param Windows: Supported Windows OS
Note: this field may return null, indicating that no valid values can be obtained.
        :type Windows: list of str
        :param Linux: Supported Linux OS
Note: this field may return null, indicating that no valid values can be obtained.
        :type Linux: list of str
        """
        self.Windows = None
        self.Linux = None


    def _deserialize(self, params):
        self.Windows = params.get("Windows")
        self.Linux = params.get("Linux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTask(AbstractModel):
    """Image task

    """

    def __init__(self):
        r"""
        :param State: Image import status. Valid values: PENDING, PROCESSING, SUCCESS, FAILED
        :type State: str
        :param Message: Cause of import failure (FAILED)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param ImageName: Image name
        :type ImageName: str
        :param CreateTime: Creation time
        :type CreateTime: str
        """
        self.State = None
        self.Message = None
        self.ImageName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.Message = params.get("Message")
        self.ImageName = params.get("ImageName")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageRequest(AbstractModel):
    """ImportImage request structure.

    """

    def __init__(self):
        r"""
        :param ImageId: Image ID.
        :type ImageId: str
        :param ImageDescription: Image description.
        :type ImageDescription: str
        :param SourceRegion: Source region
        :type SourceRegion: str
        """
        self.ImageId = None
        self.ImageDescription = None
        self.SourceRegion = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageDescription = params.get("ImageDescription")
        self.SourceRegion = params.get("SourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageResponse(AbstractModel):
    """ImportImage response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """Instance information.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param InstanceName: Instance name, such as `ens-34241f3s`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param InstanceState: Instance status. Valid values:
PENDING: creating
LAUNCH_FAILED: failed to create
RUNNING: running
STOPPED: shut down
STARTING: starting
STOPPING: shutting down
REBOOTING: restarting
SHUTDOWN: to be terminated
TERMINATING: terminating.
        :type InstanceState: str
        :param Image: Information of the image currently used by the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Image: :class:`tencentcloud.ecm.v20190719.models.Image`
        :param SimpleModule: Basic information of the current module of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SimpleModule: :class:`tencentcloud.ecm.v20190719.models.SimpleModule`
        :param Position: Location information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Position: :class:`tencentcloud.ecm.v20190719.models.Position`
        :param Internet: Network information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Internet: :class:`tencentcloud.ecm.v20190719.models.Internet`
        :param InstanceTypeConfig: Configuration information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        :param CreateTime: Instance creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param TagSet: Instance tag information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param LatestOperation: Last operation on the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestOperation: str
        :param LatestOperationState: Result of the last operation on the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestOperationState: str
        :param RestrictState: Instance business status. Valid values:
NORMAL: normal
EXPIRED: expired
PROTECTIVELY_ISOLATED: isolated.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RestrictState: str
        :param SystemDiskSize: System disk size in GB.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SystemDiskSize: int
        :param DataDiskSize: Data disk size in GB.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataDiskSize: int
        :param UUID: Instance UUID
Note: this field may return null, indicating that no valid values can be obtained.
        :type UUID: str
        :param PayMode: Billing mode.
    0: postpaid.
    1: prepaid.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PayMode: int
        :param ExpireTime: Expiration time in the format of `yyyy-mm-dd HH:mm:ss`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param IsolatedTime: Isolation time in the format of `yyyy-mm-dd HH:mm:ss`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsolatedTime: str
        :param RenewFlag: Auto-Renewal flag.
      0: no.
      1: yes.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        :param ExpireState: Expiration status.
    NORMAL: normal.
    WILL_EXPIRE: about to expire.
    EXPIRED: expired.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireState: str
        :param SystemDisk: System disk information
Note: this field may return null, indicating that no valid values can be obtained.
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.DiskInfo`
        :param DataDisks: Data disk information
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataDisks: list of DiskInfo
        :param NewFlag: New instance flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type NewFlag: int
        :param SecurityGroupIds: Security group of the instance, which can be obtained from the `sgId` field in the returned value of the `DescribeSecurityGroups` API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecurityGroupIds: list of str
        :param VirtualPrivateCloud: VPC attribute
Note: this field may return null, indicating that no valid values can be obtained.
        :type VirtualPrivateCloud: :class:`tencentcloud.ecm.v20190719.models.VirtualPrivateCloud`
        :param ISP: ISP field of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ISP: str
        :param PhysicalPosition: Physical location information. Note that this field is currently a reserved field and null.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhysicalPosition: :class:`tencentcloud.ecm.v20190719.models.PhysicalPosition`
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceState = None
        self.Image = None
        self.SimpleModule = None
        self.Position = None
        self.Internet = None
        self.InstanceTypeConfig = None
        self.CreateTime = None
        self.TagSet = None
        self.LatestOperation = None
        self.LatestOperationState = None
        self.RestrictState = None
        self.SystemDiskSize = None
        self.DataDiskSize = None
        self.UUID = None
        self.PayMode = None
        self.ExpireTime = None
        self.IsolatedTime = None
        self.RenewFlag = None
        self.ExpireState = None
        self.SystemDisk = None
        self.DataDisks = None
        self.NewFlag = None
        self.SecurityGroupIds = None
        self.VirtualPrivateCloud = None
        self.ISP = None
        self.PhysicalPosition = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceState = params.get("InstanceState")
        if params.get("Image") is not None:
            self.Image = Image()
            self.Image._deserialize(params.get("Image"))
        if params.get("SimpleModule") is not None:
            self.SimpleModule = SimpleModule()
            self.SimpleModule._deserialize(params.get("SimpleModule"))
        if params.get("Position") is not None:
            self.Position = Position()
            self.Position._deserialize(params.get("Position"))
        if params.get("Internet") is not None:
            self.Internet = Internet()
            self.Internet._deserialize(params.get("Internet"))
        if params.get("InstanceTypeConfig") is not None:
            self.InstanceTypeConfig = InstanceTypeConfig()
            self.InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        self.CreateTime = params.get("CreateTime")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.LatestOperation = params.get("LatestOperation")
        self.LatestOperationState = params.get("LatestOperationState")
        self.RestrictState = params.get("RestrictState")
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.DataDiskSize = params.get("DataDiskSize")
        self.UUID = params.get("UUID")
        self.PayMode = params.get("PayMode")
        self.ExpireTime = params.get("ExpireTime")
        self.IsolatedTime = params.get("IsolatedTime")
        self.RenewFlag = params.get("RenewFlag")
        self.ExpireState = params.get("ExpireState")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = DiskInfo()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.NewFlag = params.get("NewFlag")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ISP = params.get("ISP")
        if params.get("PhysicalPosition") is not None:
            self.PhysicalPosition = PhysicalPosition()
            self.PhysicalPosition._deserialize(params.get("PhysicalPosition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyConfig(AbstractModel):
    """Model family configuration

    """

    def __init__(self):
        r"""
        :param InstanceFamilyName: Model name
        :type InstanceFamilyName: str
        :param InstanceFamily: Model ID
        :type InstanceFamily: str
        """
        self.InstanceFamilyName = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.InstanceFamilyName = params.get("InstanceFamilyName")
        self.InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyTypeConfig(AbstractModel):
    """Instance family type configuration

    """

    def __init__(self):
        r"""
        :param InstanceFamilyType: Instance model family type ID
        :type InstanceFamilyType: str
        :param InstanceFamilyTypeName: Instance model family type name
        :type InstanceFamilyTypeName: str
        """
        self.InstanceFamilyType = None
        self.InstanceFamilyTypeName = None


    def _deserialize(self, params):
        self.InstanceFamilyType = params.get("InstanceFamilyType")
        self.InstanceFamilyTypeName = params.get("InstanceFamilyTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNetworkInfo(AbstractModel):
    """Instance ENI IP information array

    """

    def __init__(self):
        r"""
        :param AddressInfoSet: Private and public IP information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressInfoSet: list of AddressInfo
        :param NetworkInterfaceId: ENI ID.
        :type NetworkInterfaceId: str
        :param NetworkInterfaceName: ENI name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetworkInterfaceName: str
        :param Primary: Primary ENI attribute. Valid values: true: primary ENI; false: secondary ENI.
        :type Primary: bool
        """
        self.AddressInfoSet = None
        self.NetworkInterfaceId = None
        self.NetworkInterfaceName = None
        self.Primary = None


    def _deserialize(self, params):
        if params.get("AddressInfoSet") is not None:
            self.AddressInfoSet = []
            for item in params.get("AddressInfoSet"):
                obj = AddressInfo()
                obj._deserialize(item)
                self.AddressInfoSet.append(obj)
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.Primary = params.get("Primary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNetworkLimitConfig(AbstractModel):
    """Network resource limit of the instance

    """

    def __init__(self):
        r"""
        :param CpuNum: Number of CPU cores
        :type CpuNum: int
        :param NetworkInterfaceLimit: ENI quantity limit
        :type NetworkInterfaceLimit: int
        :param InnerIpPerNetworkInterface: Private IP quantity limit per ENI
        :type InnerIpPerNetworkInterface: int
        :param PublicIpPerInstance: Public IP limit per instance
        :type PublicIpPerInstance: int
        """
        self.CpuNum = None
        self.NetworkInterfaceLimit = None
        self.InnerIpPerNetworkInterface = None
        self.PublicIpPerInstance = None


    def _deserialize(self, params):
        self.CpuNum = params.get("CpuNum")
        self.NetworkInterfaceLimit = params.get("NetworkInterfaceLimit")
        self.InnerIpPerNetworkInterface = params.get("InnerIpPerNetworkInterface")
        self.PublicIpPerInstance = params.get("PublicIpPerInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceOperator(AbstractModel):
    """Executable operations for the instance

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param DeniedActions: Prohibited operations for the instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeniedActions: list of OperatorAction
        """
        self.InstanceId = None
        self.DeniedActions = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DeniedActions") is not None:
            self.DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = OperatorAction()
                obj._deserialize(item)
                self.DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancePricesPartDetail(AbstractModel):
    """Instance price information

    """

    def __init__(self):
        r"""
        :param CpuPrice: CPU price information
        :type CpuPrice: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        :param MemPrice: Memory price information
        :type MemPrice: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        :param DisksPrice: Disk price information
        :type DisksPrice: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        """
        self.CpuPrice = None
        self.MemPrice = None
        self.DisksPrice = None


    def _deserialize(self, params):
        if params.get("CpuPrice") is not None:
            self.CpuPrice = PriceDetail()
            self.CpuPrice._deserialize(params.get("CpuPrice"))
        if params.get("MemPrice") is not None:
            self.MemPrice = PriceDetail()
            self.MemPrice._deserialize(params.get("MemPrice"))
        if params.get("DisksPrice") is not None:
            self.DisksPrice = PriceDetail()
            self.DisksPrice._deserialize(params.get("DisksPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStatistic(AbstractModel):
    """Instance statistics

    """

    def __init__(self):
        r"""
        :param InstanceType: Instance type
        :type InstanceType: str
        :param InstanceCount: Number of instances
        :type InstanceCount: int
        """
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
        


class InstanceTypeConfig(AbstractModel):
    """Model configuration

    """

    def __init__(self):
        r"""
        :param InstanceFamilyConfig: Model family configuration information
        :type InstanceFamilyConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyConfig`
        :param InstanceType: Model
        :type InstanceType: str
        :param Vcpu: Number of CPU cores
        :type Vcpu: int
        :param Memory: Memory size
        :type Memory: int
        :param Frequency: Clock rate
        :type Frequency: str
        :param CpuModelName: CPU model
        :type CpuModelName: str
        :param InstanceFamilyTypeConfig: Instance family type configuration information
        :type InstanceFamilyTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        :param ExtInfo: Extra model information, which is a JSON string in the format of `{"dataDiskSize":3200,"systemDiskSize":60, "systemDiskSizeShow":"default system disk size:60 GB","dataDiskSizeShow":"local NVMe SSD: 3200 GB"}`. It indicates a special model if it exists
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExtInfo: str
        :param Vgpu: Number of GPU cards
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vgpu: float
        :param GpuModelName: GPU model
Note: this field may return null, indicating that no valid values can be obtained.
        :type GpuModelName: str
        """
        self.InstanceFamilyConfig = None
        self.InstanceType = None
        self.Vcpu = None
        self.Memory = None
        self.Frequency = None
        self.CpuModelName = None
        self.InstanceFamilyTypeConfig = None
        self.ExtInfo = None
        self.Vgpu = None
        self.GpuModelName = None


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfig") is not None:
            self.InstanceFamilyConfig = InstanceFamilyConfig()
            self.InstanceFamilyConfig._deserialize(params.get("InstanceFamilyConfig"))
        self.InstanceType = params.get("InstanceType")
        self.Vcpu = params.get("Vcpu")
        self.Memory = params.get("Memory")
        self.Frequency = params.get("Frequency")
        self.CpuModelName = params.get("CpuModelName")
        if params.get("InstanceFamilyTypeConfig") is not None:
            self.InstanceFamilyTypeConfig = InstanceFamilyTypeConfig()
            self.InstanceFamilyTypeConfig._deserialize(params.get("InstanceFamilyTypeConfig"))
        self.ExtInfo = params.get("ExtInfo")
        self.Vgpu = params.get("Vgpu")
        self.GpuModelName = params.get("GpuModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancesPrice(AbstractModel):
    """Instance price information

    """

    def __init__(self):
        r"""
        :param InstancePricesPartDetail: Instance price details
        :type InstancePricesPartDetail: :class:`tencentcloud.ecm.v20190719.models.InstancePricesPartDetail`
        :param Discount: Discount on the total instance price
        :type Discount: int
        :param DiscountPrice: Discounted price
        :type DiscountPrice: int
        :param OriginalPrice: Original cost
        :type OriginalPrice: int
        """
        self.InstancePricesPartDetail = None
        self.Discount = None
        self.DiscountPrice = None
        self.OriginalPrice = None


    def _deserialize(self, params):
        if params.get("InstancePricesPartDetail") is not None:
            self.InstancePricesPartDetail = InstancePricesPartDetail()
            self.InstancePricesPartDetail._deserialize(params.get("InstancePricesPartDetail"))
        self.Discount = params.get("Discount")
        self.DiscountPrice = params.get("DiscountPrice")
        self.OriginalPrice = params.get("OriginalPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Internet(AbstractModel):
    """Network information of the instance.

    """

    def __init__(self):
        r"""
        :param PrivateIPAddressSet: Private network information list of the instance, with the primary ENI followed by secondary ENIs in the order of binding.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIPAddressSet: list of PrivateIPAddressInfo
        :param PublicIPAddressSet: Public network information list of the instance, with the primary ENI followed by secondary ENIs in the order of binding.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicIPAddressSet: list of PublicIPAddressInfo
        :param InstanceNetworkInfoSet: Network information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceNetworkInfoSet: list of InstanceNetworkInfo
        """
        self.PrivateIPAddressSet = None
        self.PublicIPAddressSet = None
        self.InstanceNetworkInfoSet = None


    def _deserialize(self, params):
        if params.get("PrivateIPAddressSet") is not None:
            self.PrivateIPAddressSet = []
            for item in params.get("PrivateIPAddressSet"):
                obj = PrivateIPAddressInfo()
                obj._deserialize(item)
                self.PrivateIPAddressSet.append(obj)
        if params.get("PublicIPAddressSet") is not None:
            self.PublicIPAddressSet = []
            for item in params.get("PublicIPAddressSet"):
                obj = PublicIPAddressInfo()
                obj._deserialize(item)
                self.PublicIPAddressSet.append(obj)
        if params.get("InstanceNetworkInfoSet") is not None:
            self.InstanceNetworkInfoSet = []
            for item in params.get("InstanceNetworkInfoSet"):
                obj = InstanceNetworkInfo()
                obj._deserialize(item)
                self.InstanceNetworkInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Address(AbstractModel):
    """IPv6 address information.

    """

    def __init__(self):
        r"""
        :param Address: IPv6 address, such as `3402:4e00:20:100:0:8cd9:2a67:71f3`
        :type Address: str
        :param Primary: Whether it is the primary IP.
        :type Primary: bool
        :param AddressId: EIP instance ID, such as `eip-hxlqja90`.
        :type AddressId: str
        :param Description: Description.
        :type Description: str
        :param IsWanIpBlocked: Whether the public IP is blocked.
        :type IsWanIpBlocked: bool
        :param State: IPv6 address status:
PENDING: generating
MIGRATING: migrating
DELETING: deleting
AVAILABLE: available
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyPair(AbstractModel):
    """Key pair information

    """

    def __init__(self):
        r"""
        :param KeyId: Key pair ID, which is the unique identifier of a key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param KeyName: Key pair name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyName: str
        :param ProjectId: Project ID of the key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param Description: Key pair description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param PublicKey: Public key (in plain text) of key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicKey: str
        :param PrivateKey: Private key (in plaintext) of a key pair. Tencent Cloud do not store private keys. Therefore, keep them secure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateKey: str
        :param AssociatedInstanceIds: List of IDs of the instances associated with the key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssociatedInstanceIds: list of str
        :param CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        """
        self.KeyId = None
        self.KeyName = None
        self.ProjectId = None
        self.Description = None
        self.PublicKey = None
        self.PrivateKey = None
        self.AssociatedInstanceIds = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        self.Description = params.get("Description")
        self.PublicKey = params.get("PublicKey")
        self.PrivateKey = params.get("PrivateKey")
        self.AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Listener(AbstractModel):
    """CLB listener

    """

    def __init__(self):
        r"""
        :param ListenerId: CLB listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param Protocol: Listener protocol
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param Port: Listener port.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param HealthCheck: Health check information of the listener
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        :param Scheduler: Request scheduling method
Note: this field may return null, indicating that no valid values can be obtained.
        :type Scheduler: str
        :param SessionExpireTime: Session persistence time
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionExpireTime: int
        :param ListenerName: Listener name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param CreateTime: Listener creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param SessionType: Session type of the listener
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionType: str
        :param EndPort: End port of the port range
Note: this field may return null, indicating that no valid values can be obtained.
        :type EndPort: int
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.ListenerName = None
        self.CreateTime = None
        self.SessionType = None
        self.EndPort = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.ListenerName = params.get("ListenerName")
        self.CreateTime = params.get("CreateTime")
        self.SessionType = params.get("SessionType")
        self.EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerBackend(AbstractModel):
    """Listener backend

    """

    def __init__(self):
        r"""
        :param ListenerId: Listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param Protocol: Listener protocol
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param Port: Listener port
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param Targets: List of real servers bound to the CLB instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type Targets: list of Backend
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Targets = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerHealth(AbstractModel):
    """Listener health status

    """

    def __init__(self):
        r"""
        :param ListenerId: Listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param ListenerName: Listener name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param Protocol: Listener protocol
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param Port: Listener port
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param Rules: List of forwarding rules of the listener
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rules: list of RuleHealth
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.Port = None
        self.Rules = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleHealth()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    """CLB instance information

    """

    def __init__(self):
        r"""
        :param Region: Region.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param Position: Location information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Position: :class:`tencentcloud.ecm.v20190719.models.Position`
        :param LoadBalancerId: CLB instance ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerId: str
        :param LoadBalancerName: CLB instance name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerName: str
        :param LoadBalancerType: Network type of the CLB instance. Valid values: OPEN: public network
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerType: str
        :param LoadBalancerVips: List of VIPs of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerVips: list of str
        :param Status: CLB instance status. Valid values:
 0: creating; 1: running.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param CreateTime: CLB instance creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param StatusTime: Last status change time of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusTime: str
        :param VpcId: VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param Tags: CLB instance tag information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagInfo
        :param VipIsp: ISP of the CLB IP address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VipIsp: str
        :param NetworkAttributes: Network attribute of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetworkAttributes: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        :param SecureGroups: Security group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecureGroups: list of str
        :param LoadBalancerPassToTarget: Whether the real server opens the traffic from ELB to the internet.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerPassToTarget: bool
        """
        self.Region = None
        self.Position = None
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.LoadBalancerType = None
        self.LoadBalancerVips = None
        self.Status = None
        self.CreateTime = None
        self.StatusTime = None
        self.VpcId = None
        self.Tags = None
        self.VipIsp = None
        self.NetworkAttributes = None
        self.SecureGroups = None
        self.LoadBalancerPassToTarget = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        if params.get("Position") is not None:
            self.Position = Position()
            self.Position._deserialize(params.get("Position"))
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.StatusTime = params.get("StatusTime")
        self.VpcId = params.get("VpcId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.VipIsp = params.get("VipIsp")
        if params.get("NetworkAttributes") is not None:
            self.NetworkAttributes = LoadBalancerInternetAccessible()
            self.NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        self.SecureGroups = params.get("SecureGroups")
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerHealth(AbstractModel):
    """CLB health status

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerId: str
        :param LoadBalancerName: CLB instance name
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerName: str
        :param Listeners: List of listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :type Listeners: list of ListenerHealth
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.Listeners = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerHealth()
                obj._deserialize(item)
                self.Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerInternetAccessible(AbstractModel):
    """CLB information such as bandwidth limit.

    """

    def __init__(self):
        r"""
        :param InternetMaxBandwidthOut: Maximum outbound bandwidth in Mbps. Default value: 10.
        :type InternetMaxBandwidthOut: int
        """
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
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
        r"""
        :param EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param SourceInstanceId: ID of the ECM instance bound to the ENI, such as `ein-r8hr2upy`.
        :type SourceInstanceId: str
        :param DestinationInstanceId: ID of the destination ECM instance to be migrated.
        :type DestinationInstanceId: str
        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.SourceInstanceId = None
        self.DestinationInstanceId = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.SourceInstanceId = params.get("SourceInstanceId")
        self.DestinationInstanceId = params.get("DestinationInstanceId")
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
        r"""
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
        r"""
        :param EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param SourceNetworkInterfaceId: ID of the ENI instance bound to the private IP, such as `eni-11112222`.
        :type SourceNetworkInterfaceId: str
        :param DestinationNetworkInterfaceId: ID of the destination ENI instance to be migrated.
        :type DestinationNetworkInterfaceId: str
        :param PrivateIpAddress: Private IP address to be migrated, such as `10.0.0.6`.
        :type PrivateIpAddress: str
        """
        self.EcmRegion = None
        self.SourceNetworkInterfaceId = None
        self.DestinationNetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
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
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param AddressId: Unique EIP ID, such as `eip-11112222`.
        :type AddressId: str
        :param AddressName: New EIP name, which can contain up to 20 characters.
        :type AddressName: str
        :param EipDirectConnection: Whether "direct access" is enabled for the EIP. TRUE: yes. FALSE: no. Note that this parameter is available only to users who have activated the EIP direct access feature.
        :type EipDirectConnection: str
        """
        self.EcmRegion = None
        self.AddressId = None
        self.AddressName = None
        self.EipDirectConnection = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
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
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param AddressIds: Unique EIP ID, such as `eip-xxxxxxx`
        :type AddressIds: list of str
        :param InternetMaxBandwidthOut: Target bandwidth value
        :type InternetMaxBandwidthOut: int
        """
        self.EcmRegion = None
        self.AddressIds = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressIds = params.get("AddressIds")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
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
        r"""
        :param TaskId: Async task ID.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyDefaultSubnetRequest(AbstractModel):
    """ModifyDefaultSubnet request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param Zone: ECM AZ
        :type Zone: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        """
        self.EcmRegion = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDefaultSubnetResponse(AbstractModel):
    """ModifyDefaultSubnet response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param HaVipId: Unique HAVIP ID, such as `havip-9o233uri`.
        :type HaVipId: str
        :param HaVipName: HAVIP name, which can be customized with up to 60 characters.
        :type HaVipName: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute request structure.

    """

    def __init__(self):
        r"""
        :param ImageId: Image ID, such as `img-gvbnzy6f`
        :type ImageId: str
        :param ImageName: Image name, which must meet the following requirements:
It can contain up to 20 characters.
- The image name cannot be the same as existing image names.
        :type ImageName: str
        :param ImageDescription: Image description, which must meet the following requirements:
- It cannot exceed 60 characters.
        :type ImageDescription: str
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageDescription = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAttributeResponse(AbstractModel):
    """ModifyImageAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: List of IDs of the instances to be modified. You can request up to 100 instances at a time.
        :type InstanceIdSet: list of str
        :param InstanceName: Instance name displayed after successful modification, which can contain up to 60 characters. If this parameter is not specified, an empty value will be displayed.
        :type InstanceName: str
        :param SecurityGroups: List of IDs of the security groups of the instance. The instance will be associated with the specified security groups and will be disassociated from the original security groups. The maximum quantity is 5.
        :type SecurityGroups: list of str
        """
        self.InstanceIdSet = None
        self.InstanceName = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.InstanceName = params.get("InstanceName")
        self.SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param Ipv6Addresses: Information of the specified IPv6 addresses.
        :type Ipv6Addresses: list of Ipv6Address
        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyListenerRequest(AbstractModel):
    """ModifyListener request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param ListenerName: New listener name
        :type ListenerName: str
        :param SessionExpireTime: Session persistence time in seconds. Value range: 30–3600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.
        :type SessionExpireTime: int
        :param HealthCheck: Health check parameters
        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        :param Scheduler: Forwarding method of the listener. Valid values: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR.
        :type Scheduler: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Scheduler = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerResponse(AbstractModel):
    """ModifyListener response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: Unique CLB ID
        :type LoadBalancerId: str
        :param LoadBalancerName: CLB instance name
        :type LoadBalancerName: str
        :param InternetChargeInfo: Network billing and bandwidth parameters
        :type InternetChargeInfo: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        :param LoadBalancerPassToTarget: Whether to allow ELB traffic to the target group. `true`: allows ELB traffic to the target group and verifies security groups only on ELB; `false`: denies ELB traffic to the target group and verifies security groups on both ELB and backend instances.
        :type LoadBalancerPassToTarget: bool
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.InternetChargeInfo = None
        self.LoadBalancerPassToTarget = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("InternetChargeInfo") is not None:
            self.InternetChargeInfo = LoadBalancerInternetAccessible()
            self.InternetChargeInfo._deserialize(params.get("InternetChargeInfo"))
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleConfigRequest(AbstractModel):
    """ModifyModuleConfig request structure.

    """

    def __init__(self):
        r"""
        :param ModuleId: Module ID.
        :type ModuleId: str
        :param InstanceType: Model ID.
        :type InstanceType: str
        :param DefaultDataDiskSize: Default data disk size in GB. It cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :type DefaultDataDiskSize: int
        :param DefaultSystemDiskSize: Default system disk size in GB. It cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :type DefaultSystemDiskSize: int
        :param SystemDisk: System disk
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param DataDisks: Data disk
        :type DataDisks: list of DataDisk
        """
        self.ModuleId = None
        self.InstanceType = None
        self.DefaultDataDiskSize = None
        self.DefaultSystemDiskSize = None
        self.SystemDisk = None
        self.DataDisks = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.InstanceType = params.get("InstanceType")
        self.DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        self.DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleConfigResponse(AbstractModel):
    """ModifyModuleConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleDisableWanIpRequest(AbstractModel):
    """ModifyModuleDisableWanIp request structure.

    """

    def __init__(self):
        r"""
        :param ModuleId: Module ID
        :type ModuleId: str
        :param DisableWanIp: Whether to prohibit public IP assignment. Valid values: true: no; false: yes.
        :type DisableWanIp: bool
        """
        self.ModuleId = None
        self.DisableWanIp = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.DisableWanIp = params.get("DisableWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleDisableWanIpResponse(AbstractModel):
    """ModifyModuleDisableWanIp response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleImageRequest(AbstractModel):
    """ModifyModuleImage request structure.

    """

    def __init__(self):
        r"""
        :param DefaultImageId: Default image ID
        :type DefaultImageId: str
        :param ModuleId: Module ID
        :type ModuleId: str
        """
        self.DefaultImageId = None
        self.ModuleId = None


    def _deserialize(self, params):
        self.DefaultImageId = params.get("DefaultImageId")
        self.ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleImageResponse(AbstractModel):
    """ModifyModuleImage response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleIpDirectRequest(AbstractModel):
    """ModifyModuleIpDirect request structure.

    """

    def __init__(self):
        r"""
        :param ModuleId: Module ID.
        :type ModuleId: str
        :param CloseIpDirect: Whether to disable IP direct access. Valid values:
true: yes
false: no
        :type CloseIpDirect: bool
        """
        self.ModuleId = None
        self.CloseIpDirect = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.CloseIpDirect = params.get("CloseIpDirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleIpDirectResponse(AbstractModel):
    """ModifyModuleIpDirect response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleNameRequest(AbstractModel):
    """ModifyModuleName request structure.

    """

    def __init__(self):
        r"""
        :param ModuleId: Module ID.
        :type ModuleId: str
        :param ModuleName: Module name.
        :type ModuleName: str
        """
        self.ModuleId = None
        self.ModuleName = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleNameResponse(AbstractModel):
    """ModifyModuleName response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleNetworkRequest(AbstractModel):
    """ModifyModuleNetwork request structure.

    """

    def __init__(self):
        r"""
        :param ModuleId: Module ID
        :type ModuleId: str
        :param DefaultBandwidth: Default outbound bandwidth cap
        :type DefaultBandwidth: int
        :param DefaultBandwidthIn: Default inbound bandwidth cap
        :type DefaultBandwidthIn: int
        """
        self.ModuleId = None
        self.DefaultBandwidth = None
        self.DefaultBandwidthIn = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.DefaultBandwidth = params.get("DefaultBandwidth")
        self.DefaultBandwidthIn = params.get("DefaultBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleNetworkResponse(AbstractModel):
    """ModifyModuleNetwork response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleSecurityGroupsRequest(AbstractModel):
    """ModifyModuleSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param SecurityGroupIdSet: List of up to 5 security groups.
        :type SecurityGroupIdSet: list of str
        :param ModuleId: Module ID.
        :type ModuleId: str
        """
        self.SecurityGroupIdSet = None
        self.ModuleId = None


    def _deserialize(self, params):
        self.SecurityGroupIdSet = params.get("SecurityGroupIdSet")
        self.ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleSecurityGroupsResponse(AbstractModel):
    """ModifyModuleSecurityGroups response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: Information of the specified private IP addresses.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param EcmRegion: Region information of the ECM node, such as `ap-xian-ecm`.
        :type EcmRegion: str
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
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
        r"""
        :param RouteTableId: Route table instance ID, such as `rtb-azd4dt1c`
        :type RouteTableId: str
        :param RouteTableName: Route table name
        :type RouteTableName: str
        """
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
        r"""
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
        r"""
        :param SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :type SecurityGroupId: str
        :param GroupName: Security group name, which can be customized with up to 60 characters.
        :type GroupName: str
        :param GroupDescription: Security group remarks, which can contain up to 100 characters.
        :type GroupDescription: str
        """
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
        r"""
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
        r"""
        :param SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: Security group policy set. You must specify both new egress and ingress policies for the `SecurityGroupPolicySet` object. You cannot customize the index (PolicyIndex) of the `SecurityGroupPolicy` object.
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        :param SortPolicys: Whether security group sorting is supported. `True` indicates yes. If `SortPolicys` doesn't exist or is set to `False`, the security group policy can be modified.
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
        r"""
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
        r"""
        :param SubnetId: Subnet instance ID, such as `subnet-pxir56ns`.
        :type SubnetId: str
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param SubnetName: Subnet name, which can contain up to 60 bytes.
        :type SubnetName: str
        :param EnableBroadcast: Whether to enable broadcast for the subnet.
        :type EnableBroadcast: str
        :param Tags: Tag key value of the subnet
        :type Tags: list of Tag
        """
        self.SubnetId = None
        self.EcmRegion = None
        self.SubnetName = None
        self.EnableBroadcast = None
        self.Tags = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.EcmRegion = params.get("EcmRegion")
        self.SubnetName = params.get("SubnetName")
        self.EnableBroadcast = params.get("EnableBroadcast")
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
        


class ModifySubnetAttributeResponse(AbstractModel):
    """ModifySubnetAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param Targets: List of real servers for which to modify the ports
        :type Targets: list of Target
        :param NewPort: New port of the real server bound to the listener or forwarding rule
        :type NewPort: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.NewPort = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.NewPort = params.get("NewPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetPortResponse(AbstractModel):
    """ModifyTargetPort response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param ListenerId: CLB listener ID
        :type ListenerId: str
        :param Targets: List of real servers for which to modify the weights
        :type Targets: list of Target
        :param Weight: New forwarding weight of the real server. Value range: 0-100. Default value: 10. This parameter will not take effect if the `Targets.Weight` parameter is set.
        :type Weight: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.Weight = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetWeightResponse(AbstractModel):
    """ModifyTargetWeight response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param VpcId: VPC instance ID, such as `vpc-f49l6u0z`.
        :type VpcId: str
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param VpcName: VPC name, which can be customized with up to 60 characters.
        :type VpcName: str
        :param Tags: Tags
        :type Tags: list of Tag
        :param Description: VPC description
        :type Description: str
        """
        self.VpcId = None
        self.EcmRegion = None
        self.VpcName = None
        self.Tags = None
        self.Description = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.EcmRegion = params.get("EcmRegion")
        self.VpcName = params.get("VpcName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Description = params.get("Description")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Module(AbstractModel):
    """Module information

    """

    def __init__(self):
        r"""
        :param ModuleId: Module ID.
        :type ModuleId: str
        :param ModuleName: Module name.
        :type ModuleName: str
        :param ModuleState: Module status. Valid values:
NORMAL: normal.
DELETING: deleting 
DELETEFAILED: failed to delete.
        :type ModuleState: str
        :param DefaultSystemDiskSize: Default system disk size.
        :type DefaultSystemDiskSize: int
        :param DefaultDataDiskSize: Default data disk size.
        :type DefaultDataDiskSize: int
        :param InstanceTypeConfig: Default model.
        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        :param DefaultImage: Default image.
        :type DefaultImage: :class:`tencentcloud.ecm.v20190719.models.Image`
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param DefaultBandwidth: Default outbound bandwidth.
        :type DefaultBandwidth: int
        :param TagSet: Tag set.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param CloseIpDirect: Whether to disable IP direct access.
        :type CloseIpDirect: int
        :param SecurityGroupIds: List of default security group IDs.
        :type SecurityGroupIds: list of str
        :param DefaultBandwidthIn: Default inbound bandwidth.
        :type DefaultBandwidthIn: int
        :param UserData: Custom script data
        :type UserData: str
        :param SystemDisk: System disk information.
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param DataDisks: Data disk information.
        :type DataDisks: list of DataDisk
        """
        self.ModuleId = None
        self.ModuleName = None
        self.ModuleState = None
        self.DefaultSystemDiskSize = None
        self.DefaultDataDiskSize = None
        self.InstanceTypeConfig = None
        self.DefaultImage = None
        self.CreateTime = None
        self.DefaultBandwidth = None
        self.TagSet = None
        self.CloseIpDirect = None
        self.SecurityGroupIds = None
        self.DefaultBandwidthIn = None
        self.UserData = None
        self.SystemDisk = None
        self.DataDisks = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")
        self.ModuleState = params.get("ModuleState")
        self.DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self.DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        if params.get("InstanceTypeConfig") is not None:
            self.InstanceTypeConfig = InstanceTypeConfig()
            self.InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        if params.get("DefaultImage") is not None:
            self.DefaultImage = Image()
            self.DefaultImage._deserialize(params.get("DefaultImage"))
        self.CreateTime = params.get("CreateTime")
        self.DefaultBandwidth = params.get("DefaultBandwidth")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.CloseIpDirect = params.get("CloseIpDirect")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.DefaultBandwidthIn = params.get("DefaultBandwidthIn")
        self.UserData = params.get("UserData")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModuleCounter(AbstractModel):
    """Node statistics

    """

    def __init__(self):
        r"""
        :param ISPCounterSet: ISP statistics list
        :type ISPCounterSet: list of ISPCounter
        :param ProvinceNum: Number of provinces/states
        :type ProvinceNum: int
        :param CityNum: Number of cities
        :type CityNum: int
        :param NodeNum: Number of nodes
        :type NodeNum: int
        :param InstanceNum: Number of instances
        :type InstanceNum: int
        """
        self.ISPCounterSet = None
        self.ProvinceNum = None
        self.CityNum = None
        self.NodeNum = None
        self.InstanceNum = None


    def _deserialize(self, params):
        if params.get("ISPCounterSet") is not None:
            self.ISPCounterSet = []
            for item in params.get("ISPCounterSet"):
                obj = ISPCounter()
                obj._deserialize(item)
                self.ISPCounterSet.append(obj)
        self.ProvinceNum = params.get("ProvinceNum")
        self.CityNum = params.get("CityNum")
        self.NodeNum = params.get("NodeNum")
        self.InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModuleItem(AbstractModel):
    """Item information of the module list

    """

    def __init__(self):
        r"""
        :param NodeInstanceNum: Instance statistics of the node
        :type NodeInstanceNum: :class:`tencentcloud.ecm.v20190719.models.NodeInstanceNum`
        :param Module: Module information
        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`
        """
        self.NodeInstanceNum = None
        self.Module = None


    def _deserialize(self, params):
        if params.get("NodeInstanceNum") is not None:
            self.NodeInstanceNum = NodeInstanceNum()
            self.NodeInstanceNum._deserialize(params.get("NodeInstanceNum"))
        if params.get("Module") is not None:
            self.Module = Module()
            self.Module._deserialize(params.get("Module"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonthNetwork(AbstractModel):
    """Bandwidth information of the corresponding month

    """

    def __init__(self):
        r"""
        :param ZoneInfo: Zone information of the node
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param Month: Bandwidth month, such as `202103`
        :type Month: str
        :param BandwidthPkgId: Bandwidth package ID format, such as `bwp-xxxxxxxx`
        :type BandwidthPkgId: str
        :param Isp: ISP abbreviation. Valid values: CUCC, CTCC, CMCC
        :type Isp: str
        :param TrafficMaxIn: Inbound bandwidth package peak. Value range: 0.0–xxx.xxx
        :type TrafficMaxIn: float
        :param TrafficMaxOut: Outbound bandwidth package peak. Value range: 0.0–xxx.xxx
        :type TrafficMaxOut: float
        :param FeeTraffic: Billable bandwidth. Value range: 0.0–xxx.xxx
        :type FeeTraffic: float
        :param StartTime: Start time of the monthly billable bandwidth in the format of `yyyy-mm-dd HH:mm:ss`
        :type StartTime: str
        :param EndTime: End time of the monthly billable bandwidth in the format of `yyyy-mm-dd HH:mm:ss`
        :type EndTime: str
        :param EffectiveDays: Number of actual valid days for the monthly billable bandwidth, which must be an integer greater than or equal to 0
        :type EffectiveDays: int
        :param MonthDays: Actual number of days in the specified month, such as 30
        :type MonthDays: int
        :param EffectiveDaysRate: Proportion of the number of valid days, accurate to four decimal places, such as `0.2134`
        :type EffectiveDaysRate: float
        :param BandwidthPkgType: Billable bandwidth package type. Valid values: Address, LoadBalance, AddressIpv6
        :type BandwidthPkgType: str
        """
        self.ZoneInfo = None
        self.Month = None
        self.BandwidthPkgId = None
        self.Isp = None
        self.TrafficMaxIn = None
        self.TrafficMaxOut = None
        self.FeeTraffic = None
        self.StartTime = None
        self.EndTime = None
        self.EffectiveDays = None
        self.MonthDays = None
        self.EffectiveDaysRate = None
        self.BandwidthPkgType = None


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self.ZoneInfo = ZoneInfo()
            self.ZoneInfo._deserialize(params.get("ZoneInfo"))
        self.Month = params.get("Month")
        self.BandwidthPkgId = params.get("BandwidthPkgId")
        self.Isp = params.get("Isp")
        self.TrafficMaxIn = params.get("TrafficMaxIn")
        self.TrafficMaxOut = params.get("TrafficMaxOut")
        self.FeeTraffic = params.get("FeeTraffic")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.EffectiveDays = params.get("EffectiveDays")
        self.MonthDays = params.get("MonthDays")
        self.EffectiveDaysRate = params.get("EffectiveDaysRate")
        self.BandwidthPkgType = params.get("BandwidthPkgType")
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
        r"""
        :param NetworkInterfaceId: ENI instance ID, such as `eni-f1xjkw1b`.
        :type NetworkInterfaceId: str
        :param NetworkInterfaceName: ENI name.
        :type NetworkInterfaceName: str
        :param NetworkInterfaceDescription: ENI description.
        :type NetworkInterfaceDescription: str
        :param SubnetId: Subnet instance ID.
        :type SubnetId: str
        :param VpcId: VPC instance ID.
        :type VpcId: str
        :param GroupSet: Bound security groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupSet: list of str
        :param Primary: Whether it is the primary ENI.
        :type Primary: bool
        :param MacAddress: MAC address.
        :type MacAddress: str
        :param State: ENI status:
PENDING: creating
AVAILABLE: available
ATTACHING: binding
DETACHING: unbinding
DELETING: deleting
        :type State: str
        :param PrivateIpAddressSet: Private IP information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param Attachment: Bound CVM object.
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Attachment: :class:`tencentcloud.ecm.v20190719.models.NetworkInterfaceAttachment`
        :param Zone: AZ.
        :type Zone: str
        :param CreatedTime: Creation time.
        :type CreatedTime: str
        :param Ipv6AddressSet: List of IPv6 addresses.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ipv6AddressSet: list of Ipv6Address
        :param TagSet: Tag key-value pairs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param EniType: ENI type. Valid values: 0: ENI; 1: EVM ENI.
        :type EniType: int
        :param EcmRegion: ECM region (EcmRegion)
        :type EcmRegion: str
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
        self.EcmRegion = None


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
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param InstanceId: CVM instance ID.
        :type InstanceId: str
        :param DeviceIndex: Serial number of the ENI in the CVM instance.
        :type DeviceIndex: int
        :param InstanceAccountId: Account information of the CVM instance owner.
        :type InstanceAccountId: str
        :param AttachTime: Binding time.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkStorageRange(AbstractModel):
    """Upper and lower limits of the disk

    """

    def __init__(self):
        r"""
        :param MaxBandwidth: Network bandwidth cap
        :type MaxBandwidth: int
        :param MaxSystemDiskSize: Upper limit of the data disk size
        :type MaxSystemDiskSize: int
        :param MinBandwidth: Lower limit of the network bandwidth
        :type MinBandwidth: int
        :param MinSystemDiskSize: Lower limit of the data disk size
        :type MinSystemDiskSize: int
        :param MaxDataDiskSize: Maximum data disk size
        :type MaxDataDiskSize: int
        :param MinDataDiskSize: Minimum data disk size
        :type MinDataDiskSize: int
        :param SuggestBandwidth: Suggested bandwidth
        :type SuggestBandwidth: int
        :param SuggestDataDiskSize: Suggested disk size
        :type SuggestDataDiskSize: int
        :param SuggestSystemDiskSize: Suggested system disk size
        :type SuggestSystemDiskSize: int
        :param MaxVcpu: Peak number of CPU cores
        :type MaxVcpu: int
        :param MinVcpu: Minimum number of CPU cores
        :type MinVcpu: int
        :param MaxVcpuPerReq: Maximum number of CPU cores per request
        :type MaxVcpuPerReq: int
        :param PerBandwidth: Bandwidth increment
        :type PerBandwidth: int
        :param PerDataDisk: Data disk increment
        :type PerDataDisk: int
        :param MaxModuleNum: Total number of modules
        :type MaxModuleNum: int
        """
        self.MaxBandwidth = None
        self.MaxSystemDiskSize = None
        self.MinBandwidth = None
        self.MinSystemDiskSize = None
        self.MaxDataDiskSize = None
        self.MinDataDiskSize = None
        self.SuggestBandwidth = None
        self.SuggestDataDiskSize = None
        self.SuggestSystemDiskSize = None
        self.MaxVcpu = None
        self.MinVcpu = None
        self.MaxVcpuPerReq = None
        self.PerBandwidth = None
        self.PerDataDisk = None
        self.MaxModuleNum = None


    def _deserialize(self, params):
        self.MaxBandwidth = params.get("MaxBandwidth")
        self.MaxSystemDiskSize = params.get("MaxSystemDiskSize")
        self.MinBandwidth = params.get("MinBandwidth")
        self.MinSystemDiskSize = params.get("MinSystemDiskSize")
        self.MaxDataDiskSize = params.get("MaxDataDiskSize")
        self.MinDataDiskSize = params.get("MinDataDiskSize")
        self.SuggestBandwidth = params.get("SuggestBandwidth")
        self.SuggestDataDiskSize = params.get("SuggestDataDiskSize")
        self.SuggestSystemDiskSize = params.get("SuggestSystemDiskSize")
        self.MaxVcpu = params.get("MaxVcpu")
        self.MinVcpu = params.get("MinVcpu")
        self.MaxVcpuPerReq = params.get("MaxVcpuPerReq")
        self.PerBandwidth = params.get("PerBandwidth")
        self.PerDataDisk = params.get("PerDataDisk")
        self.MaxModuleNum = params.get("MaxModuleNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Node(AbstractModel):
    """Node information

    """

    def __init__(self):
        r"""
        :param ZoneInfo: Zone information.
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param Country: Country/Region information.
        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`
        :param Area: Region information.
        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`
        :param Province: Province/State information.
        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`
        :param City: City information.
        :type City: :class:`tencentcloud.ecm.v20190719.models.City`
        :param RegionInfo: Region information.
        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        :param ISPSet: List of ISPs.
        :type ISPSet: list of ISP
        :param ISPNum: Number of ISPs.
        :type ISPNum: int
        """
        self.ZoneInfo = None
        self.Country = None
        self.Area = None
        self.Province = None
        self.City = None
        self.RegionInfo = None
        self.ISPSet = None
        self.ISPNum = None


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self.ZoneInfo = ZoneInfo()
            self.ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self.Country = Country()
            self.Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self.Area = Area()
            self.Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self.Province = Province()
            self.Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self.City = City()
            self.City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))
        if params.get("ISPSet") is not None:
            self.ISPSet = []
            for item in params.get("ISPSet"):
                obj = ISP()
                obj._deserialize(item)
                self.ISPSet.append(obj)
        self.ISPNum = params.get("ISPNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInstanceNum(AbstractModel):
    """Instance number of the node

    """

    def __init__(self):
        r"""
        :param NodeNum: Number of nodes
        :type NodeNum: int
        :param InstanceNum: Number of instances
        :type InstanceNum: int
        """
        self.NodeNum = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperatorAction(AbstractModel):
    """Operation (action)

    """

    def __init__(self):
        r"""
        :param Action: Executable operation
        :type Action: str
        :param Code: Code
Note: this field may return null, indicating that no valid values can be obtained.
        :type Code: str
        :param Message: Specific information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Message: str
        """
        self.Action = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsVersion(AbstractModel):
    """Supported OS types.

    """

    def __init__(self):
        r"""
        :param OsName: OS type
        :type OsName: str
        :param OsVersions: Supported OS versions
Note: this field may return null, indicating that no valid values can be obtained.
        :type OsVersions: list of str
        :param Architecture: Supported OS architecture
Note: this field may return null, indicating that no valid values can be obtained.
        :type Architecture: list of str
        """
        self.OsName = None
        self.OsVersions = None
        self.Architecture = None


    def _deserialize(self, params):
        self.OsName = params.get("OsName")
        self.OsVersions = params.get("OsVersions")
        self.Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackingQuotaGroup(AbstractModel):
    """A set of correlated packing quotas sorted by instance type priority

    """

    def __init__(self):
        r"""
        :param Zone: AZ
        :type Zone: str
        :param ZoneId: AZ ID
        :type ZoneId: int
        :param ISPId: ISP id
        :type ISPId: str
        :param PackingQuotaInfos: A set of correlated packing quotas
        :type PackingQuotaInfos: list of PackingQuotaInfo
        """
        self.Zone = None
        self.ZoneId = None
        self.ISPId = None
        self.PackingQuotaInfos = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ISPId = params.get("ISPId")
        if params.get("PackingQuotaInfos") is not None:
            self.PackingQuotaInfos = []
            for item in params.get("PackingQuotaInfos"):
                obj = PackingQuotaInfo()
                obj._deserialize(item)
                self.PackingQuotaInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackingQuotaInfo(AbstractModel):
    """The information of a set of correlated packing quotas

    """

    def __init__(self):
        r"""
        :param InstanceType: Instance type
        :type InstanceType: str
        :param PackingQuota: Packing quota
        :type PackingQuota: int
        """
        self.InstanceType = None
        self.PackingQuota = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.PackingQuota = params.get("PackingQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakBase(AbstractModel):
    """Peak information

    """

    def __init__(self):
        r"""
        :param PeakCpuNum: Peak CPU
        :type PeakCpuNum: int
        :param PeakMemoryNum: Peak memory
        :type PeakMemoryNum: int
        :param PeakStorageNum: Peak disk
        :type PeakStorageNum: int
        :param RecordTime: Recording time
        :type RecordTime: str
        """
        self.PeakCpuNum = None
        self.PeakMemoryNum = None
        self.PeakStorageNum = None
        self.RecordTime = None


    def _deserialize(self, params):
        self.PeakCpuNum = params.get("PeakCpuNum")
        self.PeakMemoryNum = params.get("PeakMemoryNum")
        self.PeakStorageNum = params.get("PeakStorageNum")
        self.RecordTime = params.get("RecordTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakFamilyInfo(AbstractModel):
    """PeakFamilyInfo: peak information of data such as CPU by model type

    """

    def __init__(self):
        r"""
        :param InstanceFamily: Model type information.
        :type InstanceFamily: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        :param PeakBaseSet: Peak information of basic data.
        :type PeakBaseSet: list of PeakBase
        """
        self.InstanceFamily = None
        self.PeakBaseSet = None


    def _deserialize(self, params):
        if params.get("InstanceFamily") is not None:
            self.InstanceFamily = InstanceFamilyTypeConfig()
            self.InstanceFamily._deserialize(params.get("InstanceFamily"))
        if params.get("PeakBaseSet") is not None:
            self.PeakBaseSet = []
            for item in params.get("PeakBaseSet"):
                obj = PeakBase()
                obj._deserialize(item)
                self.PeakBaseSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakNetwork(AbstractModel):
    """Peak network data

    """

    def __init__(self):
        r"""
        :param RecordTime: Recording time.
        :type RecordTime: str
        :param PeakInNetwork: Inbound bandwidth data.
        :type PeakInNetwork: str
        :param PeakOutNetwork: Outbound bandwidth data.
        :type PeakOutNetwork: str
        :param ChargeNetwork: Billable bandwidth in bps
        :type ChargeNetwork: str
        """
        self.RecordTime = None
        self.PeakInNetwork = None
        self.PeakOutNetwork = None
        self.ChargeNetwork = None


    def _deserialize(self, params):
        self.RecordTime = params.get("RecordTime")
        self.PeakInNetwork = params.get("PeakInNetwork")
        self.PeakOutNetwork = params.get("PeakOutNetwork")
        self.ChargeNetwork = params.get("ChargeNetwork")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakNetworkRegionInfo(AbstractModel):
    """Peak network information by region

    """

    def __init__(self):
        r"""
        :param Region: Region information
        :type Region: str
        :param PeakNetworkSet: Peak network set
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeakNetworkSet: list of PeakNetwork
        """
        self.Region = None
        self.PeakNetworkSet = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        if params.get("PeakNetworkSet") is not None:
            self.PeakNetworkSet = []
            for item in params.get("PeakNetworkSet"):
                obj = PeakNetwork()
                obj._deserialize(item)
                self.PeakNetworkSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhysicalPosition(AbstractModel):
    """Physical location information

    """

    def __init__(self):
        r"""
        :param PosId: Rack unit
Note: this field may return null, indicating that no valid values can be obtained.
        :type PosId: str
        :param RackId: Rack
Note: this field may return null, indicating that no valid values can be obtained.
        :type RackId: str
        :param SwitchId: Switch
Note: this field may return null, indicating that no valid values can be obtained.
        :type SwitchId: str
        """
        self.PosId = None
        self.RackId = None
        self.SwitchId = None


    def _deserialize(self, params):
        self.PosId = params.get("PosId")
        self.RackId = params.get("RackId")
        self.SwitchId = params.get("SwitchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """Abstract location of the instance, including its AZ, project, and dedicated cluster ID and name.

    """

    def __init__(self):
        r"""
        :param Zone: [AZ ID](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) of the cloud disk, which can be obtained from the `Zone` field in the returned value of the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1) API.
        :type Zone: str
        :param CageId: Cage ID. When it is used as an input parameter, it indicates to manipulate the resources in the cage with the specified `CageId` and can be left empty. When it is used as an output parameter, it represents the cage ID of the resource and can be left empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CageId: str
        :param ProjectId: Project ID of the instance, which can be obtained from the `projectId` field in the returned value of the [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1) API. If this parameter is not specified, the default project ID will be used.
        :type ProjectId: int
        :param CdcName: Name of the dedicated cluster. When it is used as an input parameter, it is ignored. When it is used as an output parameter, it represents the name of the dedicated cluster to which the cloud disk belongs, and it can be left empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CdcName: str
        :param CdcId: Dedicated cluster ID of the instance. When it is used as an input parameter, it indicates to manipulate the resources in the dedicated cluster with the specified `CdcId` and can be left empty. When it is used as an output parameter, it represents the dedicated cluster ID of the resource and can be left empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CdcId: str
        """
        self.Zone = None
        self.CageId = None
        self.ProjectId = None
        self.CdcName = None
        self.CdcId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.CageId = params.get("CageId")
        self.ProjectId = params.get("ProjectId")
        self.CdcName = params.get("CdcName")
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Position(AbstractModel):
    """Location information of the instance.

    """

    def __init__(self):
        r"""
        :param ZoneInfo: Zone information of the instance.
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param Country: Country/Region information of the instance.
        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`
        :param Area: Area information of the instance.
        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`
        :param Province: Province/State information of the instance.
        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`
        :param City: City information of the instance.
        :type City: :class:`tencentcloud.ecm.v20190719.models.City`
        :param RegionInfo: Region information of the instance.
        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        """
        self.ZoneInfo = None
        self.Country = None
        self.Area = None
        self.Province = None
        self.City = None
        self.RegionInfo = None


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self.ZoneInfo = ZoneInfo()
            self.ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self.Country = Country()
            self.Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self.Area = Area()
            self.Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self.Province = Province()
            self.Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self.City = City()
            self.City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceDetail(AbstractModel):
    """Prices of CPU, memory, and other resources

    """

    def __init__(self):
        r"""
        :param Discount: Discount, such as `20`, which represents 80% off
        :type Discount: int
        :param DiscountPrice: Discounted price in cents
        :type DiscountPrice: int
        :param OriginalPrice: Original price in cents
        :type OriginalPrice: int
        """
        self.Discount = None
        self.DiscountPrice = None
        self.OriginalPrice = None


    def _deserialize(self, params):
        self.Discount = params.get("Discount")
        self.DiscountPrice = params.get("DiscountPrice")
        self.OriginalPrice = params.get("OriginalPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateIPAddressInfo(AbstractModel):
    """Private IP information of the instance.

    """

    def __init__(self):
        r"""
        :param PrivateIPAddress: Private IP of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIPAddress: str
        """
        self.PrivateIPAddress = None


    def _deserialize(self, params):
        self.PrivateIPAddress = params.get("PrivateIPAddress")
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
        r"""
        :param PrivateIpAddress: Private IP address.
        :type PrivateIpAddress: str
        :param Primary: Whether it is the primary IP.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Primary: bool
        :param PublicIpAddress: Public IP address.
        :type PublicIpAddress: str
        :param AddressId: EIP instance ID, such as `eip-11112222`.
        :type AddressId: str
        :param Description: Private IP description.
        :type Description: str
        :param IsWanIpBlocked: Whether the public IP is blocked.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsWanIpBlocked: bool
        :param State: IP status:
PENDING: generating
MIGRATING: migrating
DELETING: deleting
AVAILABLE: available
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Province(AbstractModel):
    """Province/State information

    """

    def __init__(self):
        r"""
        :param ProvinceId: Province/State ID
        :type ProvinceId: str
        :param ProvinceName: Province/State name
        :type ProvinceName: str
        """
        self.ProvinceId = None
        self.ProvinceName = None


    def _deserialize(self, params):
        self.ProvinceId = params.get("ProvinceId")
        self.ProvinceName = params.get("ProvinceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicIPAddressInfo(AbstractModel):
    """Public IP information of the instance.

    """

    def __init__(self):
        r"""
        :param ChargeMode: Billing mode.
        :type ChargeMode: str
        :param PublicIPAddress: Public IP of the instance.
        :type PublicIPAddress: str
        :param ISP: Public IP ISP of the instance.
        :type ISP: :class:`tencentcloud.ecm.v20190719.models.ISP`
        :param MaxBandwidthOut: Outbound bandwidth cap of the instance in Mbps.
        :type MaxBandwidthOut: int
        :param MaxBandwidthIn: Inbound bandwidth cap of the instance in Mbps.
        :type MaxBandwidthIn: int
        """
        self.ChargeMode = None
        self.PublicIPAddress = None
        self.ISP = None
        self.MaxBandwidthOut = None
        self.MaxBandwidthIn = None


    def _deserialize(self, params):
        self.ChargeMode = params.get("ChargeMode")
        self.PublicIPAddress = params.get("PublicIPAddress")
        if params.get("ISP") is not None:
            self.ISP = ISP()
            self.ISP._deserialize(params.get("ISP"))
        self.MaxBandwidthOut = params.get("MaxBandwidthOut")
        self.MaxBandwidthIn = params.get("MaxBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesRequest(AbstractModel):
    """RebootInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: List of IDs of the instances to be restarted. You can request up to 100 instances in a region at a time.
        :type InstanceIdSet: list of str
        :param ForceReboot: Whether to force restart the instance after it failed to be restarted normally. Valid values:
TRUE: yes;
FALSE: no;
Default value: FALSE.
        :type ForceReboot: bool
        :param StopType: Shutdown type. Valid values:
SOFT: soft shutdown
HARD: hard shutdown
SOFT_FIRST: perform a soft shutdown first; if it fails, perform a hard shutdown

Default value: SOFT.
        :type StopType: str
        """
        self.InstanceIdSet = None
        self.ForceReboot = None
        self.StopType = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ForceReboot = params.get("ForceReboot")
        self.StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    """RebootInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Region and region name (RegionName)

    """

    def __init__(self):
        r"""
        :param Region: Region
        :type Region: str
        :param RegionName: Region name
        :type RegionName: str
        :param RegionId: RegionID
        :type RegionId: int
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseAddressesRequest(AbstractModel):
    """ReleaseAddresses request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param AddressIds: List of unique IDs of EIPs.
        :type AddressIds: list of str
        """
        self.EcmRegion = None
        self.AddressIds = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
        :param TaskId: Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ReleaseIpv6AddressesRequest(AbstractModel):
    """ReleaseIpv6Addresses request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region
        :type EcmRegion: str
        :param NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param Ipv6Addresses: List of the specified IPv6 addresses. You can specify up to 10 IPv6 addresses at a time.
        :type Ipv6Addresses: list of Ipv6Address
        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        


class ReleaseIpv6AddressesResponse(AbstractModel):
    """ReleaseIpv6Addresses response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID. You can use the `DescribeTaskResult` API to query the task status
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RemovePrivateIpAddressesRequest(AbstractModel):
    """RemovePrivateIpAddresses request structure.

    """

    def __init__(self):
        r"""
        :param EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param NetworkInterfaceId: ENI instance ID, such as `eni-11112222`.
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: Information of the specified private IPs. You can specify up to 10 IPs at a time.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        


class RemovePrivateIpAddressesResponse(AbstractModel):
    """RemovePrivateIpAddresses response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param SubnetId: Subnet instance ID, such as `subnet-3x5lf5q0`, which can be queried through the `DescribeSubnets` API.
        :type SubnetId: str
        :param RouteTableId: Route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        :param EcmRegion: ECM region
        :type EcmRegion: str
        """
        self.SubnetId = None
        self.RouteTableId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")
        self.EcmRegion = params.get("EcmRegion")
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: Security group policy set object.
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
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
        


class ReplaceSecurityGroupPolicyResponse(AbstractModel):
    """ReplaceSecurityGroupPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesMaxBandwidthRequest(AbstractModel):
    """ResetInstancesMaxBandwidth request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: List of IDs of the instances for which to reset the bandwidth cap. You can request up to 100 instances in a region at a time.
        :type InstanceIdSet: list of str
        :param MaxBandwidthOut: Modified outbound bandwidth cap.
        :type MaxBandwidthOut: int
        :param MaxBandwidthIn: Modified inbound bandwidth cap.
        :type MaxBandwidthIn: int
        """
        self.InstanceIdSet = None
        self.MaxBandwidthOut = None
        self.MaxBandwidthIn = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.MaxBandwidthOut = params.get("MaxBandwidthOut")
        self.MaxBandwidthIn = params.get("MaxBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesMaxBandwidthResponse(AbstractModel):
    """ResetInstancesMaxBandwidth response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: List of IDs of the instances for which to set the password. You can request up to 100 instances in a region at a time.
        :type InstanceIdSet: list of str
        :param Password: New password. The password of a Linux instance must contain 8–16 characters in at least two of the following character types: letters, digits, and special symbols [( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /] and cannot start with `/`.
The password of a Windows instance must contain 12–16 characters in at least three of the following character types: letters, digits, and special symbols [( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /] and cannot start with `/`.
If the instances include both Linux instances and Windows instances, the password complexity limit for Windows instances will apply.
        :type Password: str
        :param ForceStop: Whether to force shut down. Default value: false.
        :type ForceStop: bool
        :param UserName: Username of the instance for which to reset the password, which can contain up to 64 characters. If this parameter is not specified, the password of the root user will be reset by default for Linux, and the password of the admin will be reset by default for Windows.
        :type UserName: str
        """
        self.InstanceIdSet = None
        self.Password = None
        self.ForceStop = None
        self.UserName = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.Password = params.get("Password")
        self.ForceStop = params.get("ForceStop")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesRequest(AbstractModel):
    """ResetInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: List of IDs of the instances to be reinstalled.
        :type InstanceIdSet: list of str
        :param ImageId: ID of the image from which to install the instance. If this parameter is not specified, the current image of the instance will be used.
        :type ImageId: str
        :param Password: Password. If this parameter is not specified, the password will be subsequently displayed in the Message Center.
        :type Password: str
        :param EnhancedService: Whether to enable CM and CWP. If this parameter is not specified, they will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        :param KeepData: Whether to retain the data on the data disk. Valid values: true, false. Default value: true
        :type KeepData: str
        :param KeepImageLogin: Whether to keep the original settings for the image. You cannot specify this parameter if `Password` or `KeyIds.N` is specified. You can specify this parameter as `TRUE` only when you create an instance by using a custom image, shared image, or image imported from an external resource. Valid values:
TRUE: yes
FALSE: no

Default value: FALSE.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeepImageLogin: str
        """
        self.InstanceIdSet = None
        self.ImageId = None
        self.Password = None
        self.EnhancedService = None
        self.KeepData = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.KeepData = params.get("KeepData")
        self.KeepImageLogin = params.get("KeepImageLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesResponse(AbstractModel):
    """ResetInstances response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param RouteTableId: Route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        :param RouteTableName: Route table name, which can contain up to 60 bytes.
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Route(AbstractModel):
    """Routing policy

    """

    def __init__(self):
        r"""
        :param DestinationCidrBlock: Destination IPv4 IP range
        :type DestinationCidrBlock: str
        :param GatewayType: Next hop type
NORMAL_CVM: general CVM;
        :type GatewayType: str
        :param GatewayId: Next hop address
You simply need to specify the gateway ID of a different next hop type, and the system will automatically match the next hop address
When `GatewayType` is `EIP`, the value of `GatewayId` will be fixed at `0`
        :type GatewayId: str
        :param RouteItemId: Unique routing policy ID
        :type RouteItemId: str
        :param RouteDescription: Routing policy description
        :type RouteDescription: str
        :param Enabled: Whether to enable
        :type Enabled: bool
        :param RouteType: Route type. Valid values:
USER: user route;
NETD: network probe route, which will be delivered by the system by default when you create a network probe instance and cannot be edited or deleted;
CCN: CCN route, which will be delivered by the system by default and cannot be edited or deleted.
You can only add and manipulate routes of `USER` type.
        :type RouteType: str
        :param RouteId: Routing policy ID. The IPv4 routing policy will have a meaningful value, while the IPv6 routing policy is always 0. We recommend you use the unique ID `RouteItemId` for the routing policy
        :type RouteId: int
        """
        self.DestinationCidrBlock = None
        self.GatewayType = None
        self.GatewayId = None
        self.RouteItemId = None
        self.RouteDescription = None
        self.Enabled = None
        self.RouteType = None
        self.RouteId = None


    def _deserialize(self, params):
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayType = params.get("GatewayType")
        self.GatewayId = params.get("GatewayId")
        self.RouteItemId = params.get("RouteItemId")
        self.RouteDescription = params.get("RouteDescription")
        self.Enabled = params.get("Enabled")
        self.RouteType = params.get("RouteType")
        self.RouteId = params.get("RouteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteConflict(AbstractModel):
    """Route conflict object

    """

    def __init__(self):
        r"""
        :param RouteTableId: Route table instance ID
        :type RouteTableId: str
        :param DestinationCidrBlock: The conflicting destination ports to be checked
        :type DestinationCidrBlock: str
        :param ConflictSet: List of conflicting routing policies
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConflictSet: list of Route
        """
        self.RouteTableId = None
        self.DestinationCidrBlock = None
        self.ConflictSet = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        if params.get("ConflictSet") is not None:
            self.ConflictSet = []
            for item in params.get("ConflictSet"):
                obj = Route()
                obj._deserialize(item)
                self.ConflictSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTable(AbstractModel):
    """Route table

    """

    def __init__(self):
        r"""
        :param VpcId: VPC instance ID
        :type VpcId: str
        :param RouteTableId: Route table instance ID
        :type RouteTableId: str
        :param RouteTableName: Route table name
        :type RouteTableName: str
        :param AssociationSet: Association relationships of the route table
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssociationSet: list of RouteTableAssociation
        :param RouteSet: IPv4 routing policy set
Note: this field may return null, indicating that no valid values can be obtained.
        :type RouteSet: list of Route
        :param Main: Whether it is the default route table
        :type Main: bool
        :param CreatedTime: Creation time
        :type CreatedTime: str
        """
        self.VpcId = None
        self.RouteTableId = None
        self.RouteTableName = None
        self.AssociationSet = None
        self.RouteSet = None
        self.Main = None
        self.CreatedTime = None


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableAssociation(AbstractModel):
    """Association relationships of the route table

    """

    def __init__(self):
        r"""
        :param SubnetId: Subnet instance ID
        :type SubnetId: str
        :param RouteTableId: Route table instance ID
        :type RouteTableId: str
        """
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
        


class RuleHealth(AbstractModel):
    """List of forwarding rules and health status

    """

    def __init__(self):
        r"""
        :param Targets: Health check status of the real server bound to the rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type Targets: list of TargetHealth
        """
        self.Targets = None


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = TargetHealth()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunEIPDirectServiceEnabled(AbstractModel):
    """IP direct access information

    """

    def __init__(self):
        r"""
        :param Enabled: Whether to enable IP direct access. Valid values:
TRUE: yes
FALSE: no
Default value: TRUE.
Currently, Windows images do not support IP direct access.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesRequest(AbstractModel):
    """RunInstances request structure.

    """

    def __init__(self):
        r"""
        :param ZoneInstanceCountISPSet: List of AZs in which to create instances, the number of instances to be created, and the ISPs. You can create up to 100 instances in a region at a time.
        :type ZoneInstanceCountISPSet: list of ZoneInstanceCountISP
        :param Password: Instance login password. Different OS types have different limits on password complexity as detailed below:
The password of a Linux instance must contain 8–30 characters in at least two of the following character types: letters, digits, and special symbols [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? / ]. The password of a Windows instance must contain 12–30 characters in at least three of the following character types: letters, digits, and special symbols [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? /].
        :type Password: str
        :param InternetMaxBandwidthOut: Public network outbound bandwidth cap in Mbps.
1. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used.
2. If you don't specify this parameter or specify it as `0` without specifying the module, the value of `InternetMaxBandwidthIn` will be used
        :type InternetMaxBandwidthOut: int
        :param ModuleId: Module ID. If you don't specify this parameter, you must specify the `ImageId`, `InstanceType`, `DataDiskSize`, and `InternetMaxBandwidthOut` parameters
        :type ModuleId: str
        :param ImageId: Image ID. If you don't specify this parameter or specify it as null, the default value under the corresponding module will be used.
        :type ImageId: str
        :param InstanceName: Instance display name.
If this parameter is not specified, `Not named` will be displayed by default.
If you purchase multiple instances and specify the pattern string `{R:x}`, display names will be generated based on `[x, x+n-1]`, where `n` is the number of the purchased instances. For example, if you specify `server\_{R:3}` and purchase 1 instance, the display name will be `server\_3`, and if you purchase 2 instances, the display names will be `server\_3` and `server\_4` respectively.
You can specify multiple pattern strings `{R:x}`.
If you purchase multiple instances and don't specify the pattern string, the instance display names will be suffixed with 1, 2...n, where `n` indicates the number of the purchased instances. For example, if you specify `server_` and purchase 2 instances, the instance display names will be `server\_1` and `server\_2` respectively.
If the purchased instances belong to different regions or ISPs, the above rules will apply to each region and ISP independently.
It can contain up to 60 characters (including pattern string).
        :type InstanceName: str
        :param HostName: Server name
`HostName` cannot start or end with a dot or hyphen and cannot contain consecutive dots or hyphens.
Windows instance: the name can contain 2–15 letters, digits, and hyphens but not dots or only digits.
Other types (such as Linux) of instances: the name should be a combination of 2 to 60 characters, supporting multiple dots. A string between two dots can contain letters, digits, and hyphens.
        :type HostName: str
        :param ClientToken: The string used to ensure the idempotency of the request. Currently, it is a reserved parameter; therefore, do not use it.
        :type ClientToken: str
        :param EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled for public images by default.
        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        :param TagSpecification: Tag list
        :type TagSpecification: list of TagSpecification
        :param UserData: The user data provided to the instance, which needs to be Base64-encoded with a maximum size of 16 KB
        :type UserData: str
        :param InstanceType: Model. If you don't specify this parameter or specify it as null, the default value under the corresponding module will be used.
        :type InstanceType: str
        :param DataDiskSize: Data disk size in GB. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used
        :type DataDiskSize: int
        :param SecurityGroupIds: Security group of the instance, which can be obtained from the `sgId` field in the returned value of the `DescribeSecurityGroups` API. If this parameter is not specified, the default security group will be bound by default.
        :type SecurityGroupIds: list of str
        :param SystemDiskSize: System disk size in GB. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used
        :type SystemDiskSize: int
        :param InternetMaxBandwidthIn: Public network inbound bandwidth cap in Mbps.
1. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used.
2. If you don't specify this parameter or specify it as `0` without specifying the module, the value of `InternetMaxBandwidthOut` will be used
        :type InternetMaxBandwidthIn: int
        :param InstanceChargeType: Instance billing type. Valid values:
0: postpaid by resource usage, where the daily peak usage of the CPU, memory, and disk will be calculated. This billing mode applies only to non-GNR models;
1: hourly postpaid at the unit price of xx USD/instance/hour. This billing mode applies only to GNR models. To enable it, submit a ticket for application;
2: monthly postpaid at the unit price of xx USD/instance/month. This billing mode applies only to GNR models;
If this field is left empty, `0` will be selected by default for non-GNR models, and `2` will be selected by default for GNR models.
        :type InstanceChargeType: int
        :param KeyIds: Key pair.
        :type KeyIds: list of str
        :param KeepImageLogin: Whether to keep the original settings for the image. You cannot specify this parameter if `Password` or `KeyIds.N` is specified. You can specify this parameter as `TRUE` only when you create an instance by using a custom image, shared image, or image imported from an external resource. Valid values:
TRUE: yes
FALSE: no

Default value: FALSE.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeepImageLogin: str
        :param SystemDisk: System disk information.
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param DataDisks: Data disk information.
        :type DataDisks: list of DataDisk
        """
        self.ZoneInstanceCountISPSet = None
        self.Password = None
        self.InternetMaxBandwidthOut = None
        self.ModuleId = None
        self.ImageId = None
        self.InstanceName = None
        self.HostName = None
        self.ClientToken = None
        self.EnhancedService = None
        self.TagSpecification = None
        self.UserData = None
        self.InstanceType = None
        self.DataDiskSize = None
        self.SecurityGroupIds = None
        self.SystemDiskSize = None
        self.InternetMaxBandwidthIn = None
        self.InstanceChargeType = None
        self.KeyIds = None
        self.KeepImageLogin = None
        self.SystemDisk = None
        self.DataDisks = None


    def _deserialize(self, params):
        if params.get("ZoneInstanceCountISPSet") is not None:
            self.ZoneInstanceCountISPSet = []
            for item in params.get("ZoneInstanceCountISPSet"):
                obj = ZoneInstanceCountISP()
                obj._deserialize(item)
                self.ZoneInstanceCountISPSet.append(obj)
        self.Password = params.get("Password")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.ModuleId = params.get("ModuleId")
        self.ImageId = params.get("ImageId")
        self.InstanceName = params.get("InstanceName")
        self.HostName = params.get("HostName")
        self.ClientToken = params.get("ClientToken")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.UserData = params.get("UserData")
        self.InstanceType = params.get("InstanceType")
        self.DataDiskSize = params.get("DataDiskSize")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.InternetMaxBandwidthIn = params.get("InternetMaxBandwidthIn")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesResponse(AbstractModel):
    """RunInstances response structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: List of IDs of the instances being created
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """CM

    """

    def __init__(self):
        r"""
        :param Enabled: Whether to enable.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """CWP;

    """

    def __init__(self):
        r"""
        :param Enabled: Whether to enable.
        :type Enabled: bool
        :param Version: CWP edition. Valid values: 0: Basic Edition; 1: Pro Edition. Currently, only Basic Edition is supported
        :type Version: int
        """
        self.Enabled = None
        self.Version = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Version = params.get("Version")
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
        r"""
        :param SecurityGroupId: Security group instance ID, such as `esg-ohuuioma`.
        :type SecurityGroupId: str
        :param SecurityGroupName: Security group name, which can be customized with up to 60 characters.
        :type SecurityGroupName: str
        :param SecurityGroupDesc: Security group remarks, which can contain up to 100 characters.
        :type SecurityGroupDesc: str
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
        self.IsDefault = None
        self.CreatedTime = None
        self.TagSet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupDesc = params.get("SecurityGroupDesc")
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
    """Statistics on the resources associated with the security group

    """

    def __init__(self):
        r"""
        :param SecurityGroupId: Security group instance ID.
        :type SecurityGroupId: str
        :param ECM: Number of ECM instances.
        :type ECM: int
        :param Module: Number of ECM modules.
        :type Module: int
        :param ENI: Number of ENI instances.
        :type ENI: int
        :param SG: Number of times the security group is referenced by other security groups.
        :type SG: int
        :param CLB: Number of CLB instances.
        :type CLB: int
        :param InstanceStatistics: Binding statistics of all instances.
        :type InstanceStatistics: list of InstanceStatistic
        :param TotalCount: Total number of all resources (excluding resources referenced by security groups).
        :type TotalCount: int
        """
        self.SecurityGroupId = None
        self.ECM = None
        self.Module = None
        self.ENI = None
        self.SG = None
        self.CLB = None
        self.InstanceStatistics = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.ECM = params.get("ECM")
        self.Module = params.get("Module")
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
        


class SecurityGroupLimitSet(AbstractModel):
    """Security group quota limit

    """

    def __init__(self):
        r"""
        :param SecurityGroupLimit: Total number of security groups that can be created
        :type SecurityGroupLimit: int
        :param SecurityGroupPolicyLimit: Maximum number of rules under the security group
        :type SecurityGroupPolicyLimit: int
        :param ReferedSecurityGroupLimit: Number of nested security group rules under the security group
        :type ReferedSecurityGroupLimit: int
        :param SecurityGroupInstanceLimit: Number of instances associated with the security group
        :type SecurityGroupInstanceLimit: int
        :param InstanceSecurityGroupLimit: Number of security groups associated with the instance
        :type InstanceSecurityGroupLimit: int
        :param SecurityGroupModuleLimit: Number of modules associated with the security group
        :type SecurityGroupModuleLimit: int
        :param ModuleSecurityGroupLimit: Number of security groups associated with the module
        :type ModuleSecurityGroupLimit: int
        """
        self.SecurityGroupLimit = None
        self.SecurityGroupPolicyLimit = None
        self.ReferedSecurityGroupLimit = None
        self.SecurityGroupInstanceLimit = None
        self.InstanceSecurityGroupLimit = None
        self.SecurityGroupModuleLimit = None
        self.ModuleSecurityGroupLimit = None


    def _deserialize(self, params):
        self.SecurityGroupLimit = params.get("SecurityGroupLimit")
        self.SecurityGroupPolicyLimit = params.get("SecurityGroupPolicyLimit")
        self.ReferedSecurityGroupLimit = params.get("ReferedSecurityGroupLimit")
        self.SecurityGroupInstanceLimit = params.get("SecurityGroupInstanceLimit")
        self.InstanceSecurityGroupLimit = params.get("InstanceSecurityGroupLimit")
        self.SecurityGroupModuleLimit = params.get("SecurityGroupModuleLimit")
        self.ModuleSecurityGroupLimit = params.get("ModuleSecurityGroupLimit")
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
        r"""
        :param PolicyIndex: Security group policy index number
        :type PolicyIndex: int
        :param Protocol: Protocol. Valid values: TCP, UDP, ICMP.
        :type Protocol: str
        :param Port: Port. Valid values: all, discrete port, range.
        :type Port: str
        :param ServiceTemplate: Protocol port ID or protocol port group ID. `ServiceTemplate` and `Protocol+Port` are mutually exclusive.
        :type ServiceTemplate: :class:`tencentcloud.ecm.v20190719.models.ServiceTemplateSpecification`
        :param CidrBlock: IP range or IP address (mutually exclusive).
        :type CidrBlock: str
        :param SecurityGroupId: Security group instance ID, such as `esg-ohuuioma`.
        :type SecurityGroupId: str
        :param AddressTemplate: IP address ID or IP address group ID.
        :type AddressTemplate: :class:`tencentcloud.ecm.v20190719.models.AddressTemplateSpecification`
        :param Action: `ACCEPT` or `DROP`.
        :type Action: str
        :param PolicyDescription: Security group policy description.
        :type PolicyDescription: str
        :param ModifyTime: Modification time, such as `2020-07-22 19:27:23`
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifyTime: str
        :param Ipv6CidrBlock: IP range or IPv6 address (mutually exclusive).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ipv6CidrBlock: str
        """
        self.PolicyIndex = None
        self.Protocol = None
        self.Port = None
        self.ServiceTemplate = None
        self.CidrBlock = None
        self.SecurityGroupId = None
        self.AddressTemplate = None
        self.Action = None
        self.PolicyDescription = None
        self.ModifyTime = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.PolicyIndex = params.get("PolicyIndex")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("ServiceTemplate") is not None:
            self.ServiceTemplate = ServiceTemplateSpecification()
            self.ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self.CidrBlock = params.get("CidrBlock")
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("AddressTemplate") is not None:
            self.AddressTemplate = AddressTemplateSpecification()
            self.AddressTemplate._deserialize(params.get("AddressTemplate"))
        self.Action = params.get("Action")
        self.PolicyDescription = params.get("PolicyDescription")
        self.ModifyTime = params.get("ModifyTime")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
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
        r"""
        :param Version: The version number of the security group policy, which will automatically increase by one each time you update the security group policy, so as to prevent expiration of the updated routing policies. If it is left empty, any conflicts will be ignored.
        :type Version: str
        :param Egress: Outbound rule. You must select either an outbound rule or inbound rule.
        :type Egress: list of SecurityGroupPolicy
        :param Ingress: Inbound rule. You must select either outbound rule or inbound rule.
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
        r"""
        :param ServiceId: Protocol port ID, such as `eppm-f5n1f8da`.
        :type ServiceId: str
        :param ServiceGroupId: Protocol port group ID, such as `eppmg-f5n1f8da`.
        :type ServiceGroupId: str
        """
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
        


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param SecurityGroups: Array of security group IDs. You can bind up to 5 security groups to a CLB instance. If you want to unbind all security groups, leave this parameter empty or pass in an empty array
        :type SecurityGroups: list of str
        """
        self.LoadBalancerId = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    """SetLoadBalancerSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers request structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancerIds: Array of CLB instance IDs
        :type LoadBalancerIds: list of str
        :param SecurityGroup: Security group ID, such as `esg-12345678`
        :type SecurityGroup: str
        :param OperationType: ADD: bind security group;
DEL: unbind security group
        :type OperationType: str
        """
        self.LoadBalancerIds = None
        self.SecurityGroup = None
        self.OperationType = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.SecurityGroup = params.get("SecurityGroup")
        self.OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetSecurityGroupForLoadbalancersResponse(AbstractModel):
    """SetSecurityGroupForLoadbalancers response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SimpleModule(AbstractModel):
    """Basic information of the module

    """

    def __init__(self):
        r"""
        :param ModuleId: Module ID
        :type ModuleId: str
        :param ModuleName: Module name
        :type ModuleName: str
        """
        self.ModuleId = None
        self.ModuleName = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """Snapshot details

    """

    def __init__(self):
        r"""
        :param Placement: Snapshot location.
        :type Placement: :class:`tencentcloud.ecm.v20190719.models.Placement`
        :param CopyFromRemote: Whether the snapshot is replicated across regions. Valid values:<br><li>true: yes;<br><li>false: no.
        :type CopyFromRemote: bool
        :param IsPermanent: Whether the snapshot is a permanent snapshot. Valid values:<br><li>true: yes<br><li>false: no.
        :type IsPermanent: bool
        :param SnapshotName: Snapshot name, i.e., the user-defined snapshot alias. You can call [ModifySnapshotAttribute](https://intl.cloud.tencent.com/document/product/362/15650?from_cn_redirect=1) to modify this field.
        :type SnapshotName: str
        :param Percent: Snapshot creation progress in percentage. This field will always be `100` once the snapshot is created successfully.
        :type Percent: int
        :param Images: List of images associated with the snapshot.
        :type Images: list of Image
        :param ShareReference: Number of snapshots currently shared.
        :type ShareReference: int
        :param SnapshotType: Snapshot type. Valid values: PRIVATE_SNAPSHOT, SHARED_SNAPSHOT
        :type SnapshotType: str
        :param DiskSize: Size in GB of the cloud disk for which the snapshot is created.
        :type DiskSize: int
        :param DiskId: ID of the cloud disk for which the snapshot is created.
        :type DiskId: str
        :param CopyingToRegions: Destination region to which the snapshot is being replicated. Default value: [].
        :type CopyingToRegions: list of str
        :param SnapshotId: Snapshot ID.
        :type SnapshotId: str
        :param DiskUsage: Type of the cloud disk for which the snapshot is created. Valid values:<br><li>SYSTEM_DISK: system disk<br><li>DATA_DISK: data disk.
        :type DiskUsage: str
        :param Encrypt: Whether the snapshot is created from an encrypted disk. Valid values:<br><li>true: yes<br><li>false: no.
        :type Encrypt: bool
        :param CreateTime: Snapshot creation time.
        :type CreateTime: str
        :param ImageCount: Number of images associated with the snapshot.
        :type ImageCount: int
        :param SnapshotState: Snapshot status. Valid values:<br><li>NORMAL: normal<br><li>CREATING: creating<br><li>ROLLBACKING: rolling back<br><li>COPYING_FROM_REMOTE: cross-region replicating<br><li>CHECKING_COPIED: verifying the cross-region replicated data<br><li>TORECYCLE: to be repossessed.
        :type SnapshotState: str
        :param DeadlineTime: Snapshot expiration time.
        :type DeadlineTime: str
        :param TimeStartShare: Time when snapshot sharing starts.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeStartShare: str
        """
        self.Placement = None
        self.CopyFromRemote = None
        self.IsPermanent = None
        self.SnapshotName = None
        self.Percent = None
        self.Images = None
        self.ShareReference = None
        self.SnapshotType = None
        self.DiskSize = None
        self.DiskId = None
        self.CopyingToRegions = None
        self.SnapshotId = None
        self.DiskUsage = None
        self.Encrypt = None
        self.CreateTime = None
        self.ImageCount = None
        self.SnapshotState = None
        self.DeadlineTime = None
        self.TimeStartShare = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CopyFromRemote = params.get("CopyFromRemote")
        self.IsPermanent = params.get("IsPermanent")
        self.SnapshotName = params.get("SnapshotName")
        self.Percent = params.get("Percent")
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self.Images.append(obj)
        self.ShareReference = params.get("ShareReference")
        self.SnapshotType = params.get("SnapshotType")
        self.DiskSize = params.get("DiskSize")
        self.DiskId = params.get("DiskId")
        self.CopyingToRegions = params.get("CopyingToRegions")
        self.SnapshotId = params.get("SnapshotId")
        self.DiskUsage = params.get("DiskUsage")
        self.Encrypt = params.get("Encrypt")
        self.CreateTime = params.get("CreateTime")
        self.ImageCount = params.get("ImageCount")
        self.SnapshotState = params.get("SnapshotState")
        self.DeadlineTime = params.get("DeadlineTime")
        self.TimeStartShare = params.get("TimeStartShare")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SrcImage(AbstractModel):
    """Image source information

    """

    def __init__(self):
        r"""
        :param ImageId: Image ID
        :type ImageId: str
        :param ImageName: Image name
        :type ImageName: str
        :param ImageOsName: System name
        :type ImageOsName: str
        :param ImageDescription: Image description
        :type ImageDescription: str
        :param Region: Region
        :type Region: str
        :param RegionID: Region ID
        :type RegionID: int
        :param RegionName: Region name
        :type RegionName: str
        :param InstanceName: Source instance name
        :type InstanceName: str
        :param InstanceId: Source instance ID
        :type InstanceId: str
        :param ImageType: Source image type
        :type ImageType: str
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageOsName = None
        self.ImageDescription = None
        self.Region = None
        self.RegionID = None
        self.RegionName = None
        self.InstanceName = None
        self.InstanceId = None
        self.ImageType = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageOsName = params.get("ImageOsName")
        self.ImageDescription = params.get("ImageDescription")
        self.Region = params.get("Region")
        self.RegionID = params.get("RegionID")
        self.RegionName = params.get("RegionName")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.ImageType = params.get("ImageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesRequest(AbstractModel):
    """StartInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: List of IDs of the instances to be started. You can request up to 100 instances in a region at a time.
        :type InstanceIdSet: list of str
        """
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesResponse(AbstractModel):
    """StartInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopInstancesRequest(AbstractModel):
    """StopInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: List of IDs of the instances to be shut down. You can request up to 100 instances in a region at a time.
        :type InstanceIdSet: list of str
        :param ForceStop: Whether to force shut down the instance after it failed to be shut down normally. Default value: false: no.
        :type ForceStop: bool
        :param StopType: Instance shutdown mode. Valid values:
SOFT_FIRST: perform a forced shutdown in case of a failure of the normal shutdown;
HARD: forced shutdown;
SOFT: Soft shutdown;
Default value: SOFT.
        :type StopType: str
        """
        self.InstanceIdSet = None
        self.ForceStop = None
        self.StopType = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ForceStop = params.get("ForceStop")
        self.StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    """StopInstances response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param VpcId: VPC instance ID.
        :type VpcId: str
        :param SubnetId: Subnet instance ID, such as `subnet-bthucmmy`.
        :type SubnetId: str
        :param SubnetName: Subnet name.
        :type SubnetName: str
        :param CidrBlock: IPv4 CIDR block of the subnet.
        :type CidrBlock: str
        :param IsDefault: Whether it is the default subnet.
        :type IsDefault: bool
        :param EnableBroadcast: Whether to enable broadcast.
        :type EnableBroadcast: bool
        :param RouteTableId: Route table instance ID, such as `rtb-l2h8d7c2`.
        :type RouteTableId: str
        :param CreatedTime: Creation time.
        :type CreatedTime: str
        :param AvailableIpAddressCount: Number of available IPs.
        :type AvailableIpAddressCount: int
        :param Ipv6CidrBlock: IPv6 CIDR block of the subnet.
        :type Ipv6CidrBlock: str
        :param NetworkAclId: Associated ACLID
        :type NetworkAclId: str
        :param IsRemoteVpcSnat: Whether it is an SNAT address pool subnet.
        :type IsRemoteVpcSnat: bool
        :param TagSet: Tag key-value pairs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param Zone: Region
        :type Zone: str
        :param ZoneName: AZ name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneName: str
        :param InstanceCount: Number of instances
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceCount: int
        :param VpcCidrBlock: IPv4 CIDR block of the VPC.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcCidrBlock: str
        :param VpcIpv6CidrBlock: IPv6 CIDR block of the VPC.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcIpv6CidrBlock: str
        :param Region: Region
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.IsDefault = None
        self.EnableBroadcast = None
        self.RouteTableId = None
        self.CreatedTime = None
        self.AvailableIpAddressCount = None
        self.Ipv6CidrBlock = None
        self.NetworkAclId = None
        self.IsRemoteVpcSnat = None
        self.TagSet = None
        self.Zone = None
        self.ZoneName = None
        self.InstanceCount = None
        self.VpcCidrBlock = None
        self.VpcIpv6CidrBlock = None
        self.Region = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.IsDefault = params.get("IsDefault")
        self.EnableBroadcast = params.get("EnableBroadcast")
        self.RouteTableId = params.get("RouteTableId")
        self.CreatedTime = params.get("CreatedTime")
        self.AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.NetworkAclId = params.get("NetworkAclId")
        self.IsRemoteVpcSnat = params.get("IsRemoteVpcSnat")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.InstanceCount = params.get("InstanceCount")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.VpcIpv6CidrBlock = params.get("VpcIpv6CidrBlock")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemDisk(AbstractModel):
    """System disk description.

    """

    def __init__(self):
        r"""
        :param DiskType: Disk type. Valid values:
- LOCAL_BASIC: local disk;
- CLOUD_PREMIUM: Premium Cloud Storage;
Default value: CLOUD_BASIC.
        :type DiskType: str
        :param DiskId: Disk ID. This parameter is temporarily unavailable.
        :type DiskId: str
        :param DiskSize: Disk size in GB.
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag information.

    """

    def __init__(self):
        r"""
        :param Key: Tag key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param Value: Tag value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
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
        


class TagInfo(AbstractModel):
    """Tag information.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key.
        :type TagKey: str
        :param TagValue: Tag value.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSpecification(AbstractModel):
    """Resource type tag

    """

    def __init__(self):
        r"""
        :param ResourceType: Resource type. Valid values: instance, module
        :type ResourceType: str
        :param Tags: Tag list
        :type Tags: list of Tag
        """
        self.ResourceType = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
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
        


class Target(AbstractModel):
    """CLB backend target

    """

    def __init__(self):
        r"""
        :param Port: Listening port of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param InstanceId: CVM instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param Weight: Forwarding weight of the real server. Value range: [0, 100]. Default value: 10.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param EniIp: You need to pass in this parameter when binding an ENI. It represents the IP address of the ENI. You must bind an ENI to a CVM instance first before you can bind it to a CLB instance. Note: you must pass in either `InstanceId` or `EniIp`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EniIp: str
        """
        self.Port = None
        self.InstanceId = None
        self.Weight = None
        self.EniIp = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.EniIp = params.get("EniIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetHealth(AbstractModel):
    """Health check status of the backend

    """

    def __init__(self):
        r"""
        :param IP: Private IP of the target
Note: this field may return null, indicating that no valid values can be obtained.
        :type IP: str
        :param Port: Port bound to the target
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param HealthStatus: Current health status. Valid values: true: healthy; false: unhealthy (e.g., check not started, checking, or exceptional status). CLB instance will route traffic to only healthy real servers whose weights are greater than 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthStatus: bool
        :param TargetId: Instance ID of the target
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetId: str
        :param HealthStatusDetail: Detailed information of the current health status. Valid values: Alive: healthy; Dead: exceptional; Unknown: check not started/checking/unknown status; Close: health check not configured.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthStatusDetail: str
        """
        self.IP = None
        self.Port = None
        self.HealthStatus = None
        self.TargetId = None
        self.HealthStatusDetail = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.HealthStatus = params.get("HealthStatus")
        self.TargetId = params.get("TargetId")
        self.HealthStatusDetail = params.get("HealthStatusDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetsWeightRule(AbstractModel):
    """Description of targets and their weights

    """

    def __init__(self):
        r"""
        :param ListenerId: CLB listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param Targets: List of real servers for which to modify the weights
Note: this field may return null, indicating that no valid values can be obtained.
        :type Targets: list of Target
        :param Weight: New forwarding weight of the real server. Value range: 0–100.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        """
        self.ListenerId = None
        self.Targets = None
        self.Weight = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInput(AbstractModel):
    """Task query

    """

    def __init__(self):
        r"""
        :param Operation: Operation name, i.e., API name, such as `CreateImage`
        :type Operation: str
        :param TaskId: Task ID
        :type TaskId: str
        """
        self.Operation = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Operation = params.get("Operation")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOutput(AbstractModel):
    """Output parameter of the task query

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID
        :type TaskId: str
        :param Message: Status description
        :type Message: str
        :param Status: Status value. Valid values: SUCCESS, FAILED, OPERATING
        :type Status: str
        :param AddTime: Task submission time
        :type AddTime: str
        :param EndTime: Task end time
        :type EndTime: str
        :param Operation: Operation name
        :type Operation: str
        """
        self.TaskId = None
        self.Message = None
        self.Status = None
        self.AddTime = None
        self.EndTime = None
        self.Operation = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Message = params.get("Message")
        self.Status = params.get("Status")
        self.AddTime = params.get("AddTime")
        self.EndTime = params.get("EndTime")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: List of IDs of the instances to be terminated.
        :type InstanceIdSet: list of str
        :param TerminateDelay: Whether to enable scheduled termination. Default value: no.
        :type TerminateDelay: bool
        :param TerminateTime: Scheduled termination time, such as `2019-08-05 12:01:30`. If you don't enable scheduled termination, you can ignore this parameter.
        :type TerminateTime: str
        :param AssociatedResourceDestroy: Whether to delete the bound ENI and EIP. Default value: true.
true: the ENI and EIP will also be deleted;
false: only the server will be terminated, while the ENI and EIP will be retained.
        :type AssociatedResourceDestroy: bool
        """
        self.InstanceIdSet = None
        self.TerminateDelay = None
        self.TerminateTime = None
        self.AssociatedResourceDestroy = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.TerminateDelay = params.get("TerminateDelay")
        self.TerminateTime = params.get("TerminateTime")
        self.AssociatedResourceDestroy = params.get("AssociatedResourceDestroy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VirtualPrivateCloud(AbstractModel):
    """VPC information configuration.

    """

    def __init__(self):
        r"""
        :param VpcId: VPC ID, such as `vpc-xxx`.
        :type VpcId: str
        :param SubnetId: Subnet ID of the VPC, such as `subnet-xxx`.
        :type SubnetId: str
        :param AsVpcGateway: Whether it is used as a public gateway. The public gateway can be used only when the instance has a public IP and resides in a VPC. Valid values:
TRUE: yes
FALSE: no

Default value: FALSE.
        :type AsVpcGateway: bool
        :param PrivateIpAddresses: Array of VPC subnet IPs. This parameter can be used to create instances or modify the VPC attributes of instances.
        :type PrivateIpAddresses: list of str
        :param Ipv6AddressCount: Number of the IPv6 addresses to be randomly generated for the ENI.
        :type Ipv6AddressCount: int
        """
        self.VpcId = None
        self.SubnetId = None
        self.AsVpcGateway = None
        self.PrivateIpAddresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AsVpcGateway = params.get("AsVpcGateway")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """VPC object.

    """

    def __init__(self):
        r"""
        :param VpcName: VPC name.
        :type VpcName: str
        :param VpcId: VPC instance ID, such as `vpc-azd4dt1c`.
        :type VpcId: str
        :param CidrBlock: IPv4 CIDR block of the VPC.
        :type CidrBlock: str
        :param IsDefault: Whether it is the default VPC.
        :type IsDefault: bool
        :param EnableMulticast: Whether to enable multicast.
        :type EnableMulticast: bool
        :param CreatedTime: Creation time.
        :type CreatedTime: str
        :param DnsServerSet: List of DNS servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DnsServerSet: list of str
        :param DomainName: DHCP domain option value.
        :type DomainName: str
        :param DhcpOptionsId: DHCP option set ID.
        :type DhcpOptionsId: str
        :param EnableDhcp: Whether to enable DHCP.
        :type EnableDhcp: bool
        :param Ipv6CidrBlock: IPv6 CIDR block of the VPC.
        :type Ipv6CidrBlock: str
        :param TagSet: Tag key-value pair
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param AssistantCidrSet: Secondary CIDR block
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssistantCidrSet: list of AssistantCidr
        :param Region: Region
        :type Region: str
        :param Description: Description
        :type Description: str
        :param RegionName: Region name
        :type RegionName: str
        :param SubnetCount: Number of included subnets
        :type SubnetCount: int
        :param InstanceCount: Number of included instances
        :type InstanceCount: int
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
        self.Region = None
        self.Description = None
        self.RegionName = None
        self.SubnetCount = None
        self.InstanceCount = None


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
        self.Region = params.get("Region")
        self.Description = params.get("Description")
        self.RegionName = params.get("RegionName")
        self.SubnetCount = params.get("SubnetCount")
        self.InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """Zone information

    """

    def __init__(self):
        r"""
        :param ZoneId: ZoneId
        :type ZoneId: int
        :param ZoneName: ZoneName
        :type ZoneName: str
        :param Zone: Zone
        :type Zone: str
        """
        self.ZoneId = None
        self.ZoneName = None
        self.Zone = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInstanceCountISP(AbstractModel):
    """Combination of the instance AZ, number of instances to be created, and ISP;

    """

    def __init__(self):
        r"""
        :param Zone: The AZ in which to create an instance.
        :type Zone: str
        :param InstanceCount: Number of instances to be created in the current AZ.
        :type InstanceCount: int
        :param ISP: ISP name. Valid values:
CTCC: China Telecom
CUCC: China Unicom
CMCC: China Mobile
If there are multiple ISP names, you need to separate them by semicolons, such as `CMCC;CUCC;CTCC`. To use multiple ISPs, contact Tencent Cloud customer service for assistance.
        :type ISP: str
        :param VpcId: ID of the specified VPC. You must specify both `SubnetId` and `VpcId` or neither
        :type VpcId: str
        :param SubnetId: ID of the specified subnet. You must specify both `SubnetId` and `VpcId` or neither
        :type SubnetId: str
        :param PrivateIpAddresses: Private IP of the specified primary ENI. You must specify both `SubnetId` and `VpcId` at the same time. The number of IP addresses must be the same as `InstanceCount`. You can get the private IP of the secondary ENI of a multi-IP server through DHCP in the same subnet.
        :type PrivateIpAddresses: list of str
        :param Ipv6AddressCount: Number of the IPv6 addresses to be randomly generated for the ENI, which cannot be greater than 1.
        :type Ipv6AddressCount: int
        """
        self.Zone = None
        self.InstanceCount = None
        self.ISP = None
        self.VpcId = None
        self.SubnetId = None
        self.PrivateIpAddresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceCount = params.get("InstanceCount")
        self.ISP = params.get("ISP")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInstanceInfo(AbstractModel):
    """Instance information of the zone

    """

    def __init__(self):
        r"""
        :param ZoneName: Zone name
        :type ZoneName: str
        :param InstanceNum: Number of instances
        :type InstanceNum: int
        """
        self.ZoneName = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        