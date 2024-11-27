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
        :param _AddressId: Unique EIP ID.
        :type AddressId: str
        :param _AddressName: EIP name.
        :type AddressName: str
        :param _AddressStatus: EIP status, including 'CREATING' (creating), 'BINDING' (binding), 'BIND' (bound), 'UNBINDING' (unbinding), 'UNBIND' (unbound), 'OFFLINING' (releasing), and 'BIND_ENI' (binding dangling ENI)
        :type AddressStatus: str
        :param _AddressIp: Public IP address
        :type AddressIp: str
        :param _InstanceId: ID of the bound resource instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _CreatedTime: Creation time in ISO 8601 format (YYYY-MM-DDTHH:mm:ss.sssZ)
        :type CreatedTime: str
        :param _NetworkInterfaceId: ID of the bound ENI
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetworkInterfaceId: str
        :param _PrivateAddressIp: Private IP of the bound resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateAddressIp: str
        :param _IsArrears: Isolation status of the resource. true: isolated; false: not isolated.
        :type IsArrears: bool
        :param _IsBlocked: Blockage status of the EIP resource. true: blocked; false: not blocked
        :type IsBlocked: bool
        :param _IsEipDirectConnection: Whether the EIP supports direct access mode. true: yes; false: no.
        :type IsEipDirectConnection: bool
        :param _AddressType: Resource type of the EIP, including `CalcIP` (device IP), `WanIP` (general public IP), `EIP` (elastic IP), and `AnycastEip` (accelerated EIP).
        :type AddressType: str
        :param _CascadeRelease: Whether the EIP is automatically released after being unbound. true: yes; false: no
        :type CascadeRelease: bool
        :param _InternetServiceProvider: ISP. CTCC: China Telecom; CUCC: China Unicom; CMCC: China Mobile
Note: this field may return null, indicating that no valid values can be obtained.
        :type InternetServiceProvider: str
        :param _Bandwidth: Bandwidth cap
Note: this field may return null, indicating that no valid values can be obtained.
        :type Bandwidth: int
        :param _PayMode: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        """
        self._AddressId = None
        self._AddressName = None
        self._AddressStatus = None
        self._AddressIp = None
        self._InstanceId = None
        self._CreatedTime = None
        self._NetworkInterfaceId = None
        self._PrivateAddressIp = None
        self._IsArrears = None
        self._IsBlocked = None
        self._IsEipDirectConnection = None
        self._AddressType = None
        self._CascadeRelease = None
        self._InternetServiceProvider = None
        self._Bandwidth = None
        self._PayMode = None

    @property
    def AddressId(self):
        """Unique EIP ID.
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def AddressName(self):
        """EIP name.
        :rtype: str
        """
        return self._AddressName

    @AddressName.setter
    def AddressName(self, AddressName):
        self._AddressName = AddressName

    @property
    def AddressStatus(self):
        """EIP status, including 'CREATING' (creating), 'BINDING' (binding), 'BIND' (bound), 'UNBINDING' (unbinding), 'UNBIND' (unbound), 'OFFLINING' (releasing), and 'BIND_ENI' (binding dangling ENI)
        :rtype: str
        """
        return self._AddressStatus

    @AddressStatus.setter
    def AddressStatus(self, AddressStatus):
        self._AddressStatus = AddressStatus

    @property
    def AddressIp(self):
        """Public IP address
        :rtype: str
        """
        return self._AddressIp

    @AddressIp.setter
    def AddressIp(self, AddressIp):
        self._AddressIp = AddressIp

    @property
    def InstanceId(self):
        """ID of the bound resource instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreatedTime(self):
        """Creation time in ISO 8601 format (YYYY-MM-DDTHH:mm:ss.sssZ)
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def NetworkInterfaceId(self):
        """ID of the bound ENI
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def PrivateAddressIp(self):
        """Private IP of the bound resource
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateAddressIp

    @PrivateAddressIp.setter
    def PrivateAddressIp(self, PrivateAddressIp):
        self._PrivateAddressIp = PrivateAddressIp

    @property
    def IsArrears(self):
        """Isolation status of the resource. true: isolated; false: not isolated.
        :rtype: bool
        """
        return self._IsArrears

    @IsArrears.setter
    def IsArrears(self, IsArrears):
        self._IsArrears = IsArrears

    @property
    def IsBlocked(self):
        """Blockage status of the EIP resource. true: blocked; false: not blocked
        :rtype: bool
        """
        return self._IsBlocked

    @IsBlocked.setter
    def IsBlocked(self, IsBlocked):
        self._IsBlocked = IsBlocked

    @property
    def IsEipDirectConnection(self):
        """Whether the EIP supports direct access mode. true: yes; false: no.
        :rtype: bool
        """
        return self._IsEipDirectConnection

    @IsEipDirectConnection.setter
    def IsEipDirectConnection(self, IsEipDirectConnection):
        self._IsEipDirectConnection = IsEipDirectConnection

    @property
    def AddressType(self):
        """Resource type of the EIP, including `CalcIP` (device IP), `WanIP` (general public IP), `EIP` (elastic IP), and `AnycastEip` (accelerated EIP).
        :rtype: str
        """
        return self._AddressType

    @AddressType.setter
    def AddressType(self, AddressType):
        self._AddressType = AddressType

    @property
    def CascadeRelease(self):
        """Whether the EIP is automatically released after being unbound. true: yes; false: no
        :rtype: bool
        """
        return self._CascadeRelease

    @CascadeRelease.setter
    def CascadeRelease(self, CascadeRelease):
        self._CascadeRelease = CascadeRelease

    @property
    def InternetServiceProvider(self):
        """ISP. CTCC: China Telecom; CUCC: China Unicom; CMCC: China Mobile
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InternetServiceProvider

    @InternetServiceProvider.setter
    def InternetServiceProvider(self, InternetServiceProvider):
        self._InternetServiceProvider = InternetServiceProvider

    @property
    def Bandwidth(self):
        """Bandwidth cap
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def PayMode(self):
        """Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._AddressId = params.get("AddressId")
        self._AddressName = params.get("AddressName")
        self._AddressStatus = params.get("AddressStatus")
        self._AddressIp = params.get("AddressIp")
        self._InstanceId = params.get("InstanceId")
        self._CreatedTime = params.get("CreatedTime")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._PrivateAddressIp = params.get("PrivateAddressIp")
        self._IsArrears = params.get("IsArrears")
        self._IsBlocked = params.get("IsBlocked")
        self._IsEipDirectConnection = params.get("IsEipDirectConnection")
        self._AddressType = params.get("AddressType")
        self._CascadeRelease = params.get("CascadeRelease")
        self._InternetServiceProvider = params.get("InternetServiceProvider")
        self._Bandwidth = params.get("Bandwidth")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressInfo(AbstractModel):
    """IP address information structure.

    """

    def __init__(self):
        r"""
        :param _PublicIPAddressInfo: Public IP information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicIPAddressInfo: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`
        :param _PrivateIPAddressInfo: Private IP information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIPAddressInfo: :class:`tencentcloud.ecm.v20190719.models.PrivateIPAddressInfo`
        :param _PublicIPv6AddressInfo: Public IPv6 information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicIPv6AddressInfo: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`
        """
        self._PublicIPAddressInfo = None
        self._PrivateIPAddressInfo = None
        self._PublicIPv6AddressInfo = None

    @property
    def PublicIPAddressInfo(self):
        """Public IP information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`
        """
        return self._PublicIPAddressInfo

    @PublicIPAddressInfo.setter
    def PublicIPAddressInfo(self, PublicIPAddressInfo):
        self._PublicIPAddressInfo = PublicIPAddressInfo

    @property
    def PrivateIPAddressInfo(self):
        """Private IP information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PrivateIPAddressInfo`
        """
        return self._PrivateIPAddressInfo

    @PrivateIPAddressInfo.setter
    def PrivateIPAddressInfo(self, PrivateIPAddressInfo):
        self._PrivateIPAddressInfo = PrivateIPAddressInfo

    @property
    def PublicIPv6AddressInfo(self):
        """Public IPv6 information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`
        """
        return self._PublicIPv6AddressInfo

    @PublicIPv6AddressInfo.setter
    def PublicIPv6AddressInfo(self, PublicIPv6AddressInfo):
        self._PublicIPv6AddressInfo = PublicIPv6AddressInfo


    def _deserialize(self, params):
        if params.get("PublicIPAddressInfo") is not None:
            self._PublicIPAddressInfo = PublicIPAddressInfo()
            self._PublicIPAddressInfo._deserialize(params.get("PublicIPAddressInfo"))
        if params.get("PrivateIPAddressInfo") is not None:
            self._PrivateIPAddressInfo = PrivateIPAddressInfo()
            self._PrivateIPAddressInfo._deserialize(params.get("PrivateIPAddressInfo"))
        if params.get("PublicIPv6AddressInfo") is not None:
            self._PublicIPv6AddressInfo = PublicIPAddressInfo()
            self._PublicIPv6AddressInfo._deserialize(params.get("PublicIPv6AddressInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplateSpecification(AbstractModel):
    """IP address template

    """

    def __init__(self):
        r"""
        :param _AddressId: IP address ID, such as `eipm-2uw6ujo6`.
        :type AddressId: str
        :param _AddressGroupId: IP address group ID, such as `eipmg-2uw6ujo6`.
        :type AddressGroupId: str
        """
        self._AddressId = None
        self._AddressGroupId = None

    @property
    def AddressId(self):
        """IP address ID, such as `eipm-2uw6ujo6`.
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def AddressGroupId(self):
        """IP address group ID, such as `eipmg-2uw6ujo6`.
        :rtype: str
        """
        return self._AddressGroupId

    @AddressGroupId.setter
    def AddressGroupId(self, AddressGroupId):
        self._AddressGroupId = AddressGroupId


    def _deserialize(self, params):
        self._AddressId = params.get("AddressId")
        self._AddressGroupId = params.get("AddressGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateAddressesRequest(AbstractModel):
    """AllocateAddresses request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _AddressCount: Number of EIPs. Default value: 1.
        :type AddressCount: int
        :param _InternetServiceProvider: CMCC: China Mobile
CTCC: China Telecom
CUCC: China Unicom
        :type InternetServiceProvider: str
        :param _InternetMaxBandwidthOut: 1–5000 Mbps. Default value: 1 Mbps.
        :type InternetMaxBandwidthOut: int
        :param _Tags: List of tags to be bound.
        :type Tags: list of Tag
        :param _InstanceId: ID of the instance to be bound.
        :type InstanceId: str
        :param _NetworkInterfaceId: ID of the ENI to be bound, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. The ENI ID can be obtained from the `networkInterfaceId` field in the returned value of the `DescribeNetworkInterfaces` API.
        :type NetworkInterfaceId: str
        :param _PrivateIpAddress: Private IP to be bound. If you specify `NetworkInterfaceId`, you must also specify `PrivateIpAddress`, which means to bind the EIP to the specified private IP of the specified ENI. You must also make sure that the specified `PrivateIpAddress` is a private IP of the specified `NetworkInterfaceId`. The private IP of the specified ENI can be obtained from the `privateIpAddress` field in the returned value of the `DescribeNetworkInterfaces` API.
        :type PrivateIpAddress: str
        """
        self._EcmRegion = None
        self._AddressCount = None
        self._InternetServiceProvider = None
        self._InternetMaxBandwidthOut = None
        self._Tags = None
        self._InstanceId = None
        self._NetworkInterfaceId = None
        self._PrivateIpAddress = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressCount(self):
        """Number of EIPs. Default value: 1.
        :rtype: int
        """
        return self._AddressCount

    @AddressCount.setter
    def AddressCount(self, AddressCount):
        self._AddressCount = AddressCount

    @property
    def InternetServiceProvider(self):
        """CMCC: China Mobile
CTCC: China Telecom
CUCC: China Unicom
        :rtype: str
        """
        return self._InternetServiceProvider

    @InternetServiceProvider.setter
    def InternetServiceProvider(self, InternetServiceProvider):
        self._InternetServiceProvider = InternetServiceProvider

    @property
    def InternetMaxBandwidthOut(self):
        """1–5000 Mbps. Default value: 1 Mbps.
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def Tags(self):
        """List of tags to be bound.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        """ID of the instance to be bound.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NetworkInterfaceId(self):
        """ID of the ENI to be bound, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. The ENI ID can be obtained from the `networkInterfaceId` field in the returned value of the `DescribeNetworkInterfaces` API.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def PrivateIpAddress(self):
        """Private IP to be bound. If you specify `NetworkInterfaceId`, you must also specify `PrivateIpAddress`, which means to bind the EIP to the specified private IP of the specified ENI. You must also make sure that the specified `PrivateIpAddress` is a private IP of the specified `NetworkInterfaceId`. The private IP of the specified ENI can be obtained from the `privateIpAddress` field in the returned value of the `DescribeNetworkInterfaces` API.
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressCount = params.get("AddressCount")
        self._InternetServiceProvider = params.get("InternetServiceProvider")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateAddressesResponse(AbstractModel):
    """AllocateAddresses response structure.

    """

    def __init__(self):
        r"""
        :param _AddressSet: List of unique IDs of the EIPs applied for.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressSet: list of str
        :param _TaskId: Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AddressSet = None
        self._TaskId = None
        self._RequestId = None

    @property
    def AddressSet(self):
        """List of unique IDs of the EIPs applied for.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AddressSet

    @AddressSet.setter
    def AddressSet(self, AddressSet):
        self._AddressSet = AddressSet

    @property
    def TaskId(self):
        """Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AddressSet = params.get("AddressSet")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Area(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param _AreaId: Region ID
        :type AreaId: str
        :param _AreaName: Region name
        :type AreaName: str
        """
        self._AreaId = None
        self._AreaName = None

    @property
    def AreaId(self):
        """Region ID
        :rtype: str
        """
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def AreaName(self):
        """Region name
        :rtype: str
        """
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName


    def _deserialize(self, params):
        self._AreaId = params.get("AreaId")
        self._AreaName = params.get("AreaName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6AddressesRequest(AbstractModel):
    """AssignIpv6Addresses request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-1snva0vd`. Currently, only the primary ENI will be assigned the ID.
        :type NetworkInterfaceId: str
        :param _Ipv6Addresses: List of specified IPv6 addresses. You can specify up to 10 IPv6 addresses at a time. The quota is calculated together with that of `Ipv6AddressCount`, a required input parameter alternative to this one.
        :type Ipv6Addresses: list of Ipv6Address
        :param _Ipv6AddressCount: Number of automatically assigned IPv6 addresses. The total number of private IP addresses cannot exceed the quota. The quota is calculated together with that of `Ipv6Addresses`, a required input parameter alternative to this one.
        :type Ipv6AddressCount: int
        :param _Ipv6ISP: Ipv6 ISP. Valid values:
`CTCC`: China Telecom
`CUCC`: China Unicom
`CMCC`: China Mobile
        :type Ipv6ISP: str
        """
        self._EcmRegion = None
        self._NetworkInterfaceId = None
        self._Ipv6Addresses = None
        self._Ipv6AddressCount = None
        self._Ipv6ISP = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-1snva0vd`. Currently, only the primary ENI will be assigned the ID.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def Ipv6Addresses(self):
        """List of specified IPv6 addresses. You can specify up to 10 IPv6 addresses at a time. The quota is calculated together with that of `Ipv6AddressCount`, a required input parameter alternative to this one.
        :rtype: list of Ipv6Address
        """
        return self._Ipv6Addresses

    @Ipv6Addresses.setter
    def Ipv6Addresses(self, Ipv6Addresses):
        self._Ipv6Addresses = Ipv6Addresses

    @property
    def Ipv6AddressCount(self):
        """Number of automatically assigned IPv6 addresses. The total number of private IP addresses cannot exceed the quota. The quota is calculated together with that of `Ipv6Addresses`, a required input parameter alternative to this one.
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def Ipv6ISP(self):
        """Ipv6 ISP. Valid values:
`CTCC`: China Telecom
`CUCC`: China Unicom
`CMCC`: China Mobile
        :rtype: str
        """
        return self._Ipv6ISP

    @Ipv6ISP.setter
    def Ipv6ISP(self, Ipv6ISP):
        self._Ipv6ISP = Ipv6ISP


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self._Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6Addresses.append(obj)
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        self._Ipv6ISP = params.get("Ipv6ISP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6AddressesResponse(AbstractModel):
    """AssignIpv6Addresses response structure.

    """

    def __init__(self):
        r"""
        :param _Ipv6AddressSet: List of IPv6 addresses assigned to ENIs.
        :type Ipv6AddressSet: list of Ipv6Address
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ipv6AddressSet = None
        self._RequestId = None

    @property
    def Ipv6AddressSet(self):
        """List of IPv6 addresses assigned to ENIs.
        :rtype: list of Ipv6Address
        """
        return self._Ipv6AddressSet

    @Ipv6AddressSet.setter
    def Ipv6AddressSet(self, Ipv6AddressSet):
        self._Ipv6AddressSet = Ipv6AddressSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Ipv6AddressSet") is not None:
            self._Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6AddressSet.append(obj)
        self._RequestId = params.get("RequestId")


class AssignPrivateIpAddressesRequest(AbstractModel):
    """AssignPrivateIpAddresses request structure.

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param _EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param _PrivateIpAddresses: Information of the specified private IPs. You can specify up to 10 IPs at a time. You must provide either this parameter or `SecondaryPrivateIpAddressCount`, or both.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param _SecondaryPrivateIpAddressCount: Number of private IP addresses applied for. You must provide either this parameter or `PrivateIpAddresses`, or both. The total number of private IP addresses cannot exceed the quota.
        :type SecondaryPrivateIpAddressCount: int
        """
        self._NetworkInterfaceId = None
        self._EcmRegion = None
        self._PrivateIpAddresses = None
        self._SecondaryPrivateIpAddressCount = None

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-m6dyj72l`.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def EcmRegion(self):
        """ECM region, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def PrivateIpAddresses(self):
        """Information of the specified private IPs. You can specify up to 10 IPs at a time. You must provide either this parameter or `SecondaryPrivateIpAddressCount`, or both.
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def SecondaryPrivateIpAddressCount(self):
        """Number of private IP addresses applied for. You must provide either this parameter or `PrivateIpAddresses`, or both. The total number of private IP addresses cannot exceed the quota.
        :rtype: int
        """
        return self._SecondaryPrivateIpAddressCount

    @SecondaryPrivateIpAddressCount.setter
    def SecondaryPrivateIpAddressCount(self, SecondaryPrivateIpAddressCount):
        self._SecondaryPrivateIpAddressCount = SecondaryPrivateIpAddressCount


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._EcmRegion = params.get("EcmRegion")
        if params.get("PrivateIpAddresses") is not None:
            self._PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddresses.append(obj)
        self._SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignPrivateIpAddressesResponse(AbstractModel):
    """AssignPrivateIpAddresses response structure.

    """

    def __init__(self):
        r"""
        :param _PrivateIpAddressSet: Private IP details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PrivateIpAddressSet = None
        self._RequestId = None

    @property
    def PrivateIpAddressSet(self):
        """Private IP details.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddressSet

    @PrivateIpAddressSet.setter
    def PrivateIpAddressSet(self, PrivateIpAddressSet):
        self._PrivateIpAddressSet = PrivateIpAddressSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PrivateIpAddressSet") is not None:
            self._PrivateIpAddressSet = []
            for item in params.get("PrivateIpAddressSet"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddressSet.append(obj)
        self._RequestId = params.get("RequestId")


class AssistantCidr(AbstractModel):
    """Secondary CIDR information of the VPC.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC instance ID, such as `vpc-6v2ht8q5`
        :type VpcId: str
        :param _CidrBlock: Secondary CIDR, such as `172.16.0.0/16`
        :type CidrBlock: str
        :param _AssistantType: Secondary CIDR block type. 0: general secondary CIDR block; 1: container secondary CIDR block. Default value: 0.
        :type AssistantType: int
        :param _SubnetSet: Subnets divided by the secondary CIDR block.
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubnetSet: list of Subnet
        """
        self._VpcId = None
        self._CidrBlock = None
        self._AssistantType = None
        self._SubnetSet = None

    @property
    def VpcId(self):
        """VPC instance ID, such as `vpc-6v2ht8q5`
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def CidrBlock(self):
        """Secondary CIDR, such as `172.16.0.0/16`
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def AssistantType(self):
        """Secondary CIDR block type. 0: general secondary CIDR block; 1: container secondary CIDR block. Default value: 0.
        :rtype: int
        """
        return self._AssistantType

    @AssistantType.setter
    def AssistantType(self, AssistantType):
        self._AssistantType = AssistantType

    @property
    def SubnetSet(self):
        """Subnets divided by the secondary CIDR block.
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Subnet
        """
        return self._SubnetSet

    @SubnetSet.setter
    def SubnetSet(self, SubnetSet):
        self._SubnetSet = SubnetSet


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._CidrBlock = params.get("CidrBlock")
        self._AssistantType = params.get("AssistantType")
        if params.get("SubnetSet") is not None:
            self._SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self._SubnetSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAddressRequest(AbstractModel):
    """AssociateAddress request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _AddressId: Unique EIP ID, such as `eip-11112222`.
        :type AddressId: str
        :param _InstanceId: ID of the instance to be bound.
        :type InstanceId: str
        :param _NetworkInterfaceId: ID of the ENI to be bound, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. The ENI ID can be obtained from the `networkInterfaceId` field in the returned value of the `DescribeNetworkInterfaces` API.
        :type NetworkInterfaceId: str
        :param _PrivateIpAddress: Private IP to be bound. If you specify `NetworkInterfaceId`, you must also specify `PrivateIpAddress`, which means to bind the EIP to the specified private IP of the specified ENI. You must also make sure that the specified `PrivateIpAddress` is a private IP of the specified `NetworkInterfaceId`. The private IP of the specified ENI can be obtained from the `privateIpAddress` field in the returned value of the `DescribeNetworkInterfaces` API.
        :type PrivateIpAddress: str
        """
        self._EcmRegion = None
        self._AddressId = None
        self._InstanceId = None
        self._NetworkInterfaceId = None
        self._PrivateIpAddress = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressId(self):
        """Unique EIP ID, such as `eip-11112222`.
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def InstanceId(self):
        """ID of the instance to be bound.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NetworkInterfaceId(self):
        """ID of the ENI to be bound, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. The ENI ID can be obtained from the `networkInterfaceId` field in the returned value of the `DescribeNetworkInterfaces` API.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def PrivateIpAddress(self):
        """Private IP to be bound. If you specify `NetworkInterfaceId`, you must also specify `PrivateIpAddress`, which means to bind the EIP to the specified private IP of the specified ENI. You must also make sure that the specified `PrivateIpAddress` is a private IP of the specified `NetworkInterfaceId`. The private IP of the specified ENI can be obtained from the `privateIpAddress` field in the returned value of the `DescribeNetworkInterfaces` API.
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressId = params.get("AddressId")
        self._InstanceId = params.get("InstanceId")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAddressResponse(AbstractModel):
    """AssociateAddress response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: ID of the security group to be bound, such as `esg-efil73jd`. You can bind only one security group.
        :type SecurityGroupIds: list of str
        :param _InstanceIds: ID of the bound instance, such as `ein-lesecurk`. You can specify multiple instances and request up to 100 instances at a time.
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        """ID of the security group to be bound, such as `esg-efil73jd`. You can bind only one security group.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        """ID of the bound instance, such as `ein-lesecurk`. You can specify multiple instances and request up to 100 instances at a time.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AttachNetworkInterfaceRequest(AbstractModel):
    """AttachNetworkInterface request structure.

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param _InstanceId: Instance ID, such as `ein-r8hr2upy`.
        :type InstanceId: str
        :param _EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        """
        self._NetworkInterfaceId = None
        self._InstanceId = None
        self._EcmRegion = None

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-m6dyj72l`.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def InstanceId(self):
        """Instance ID, such as `ein-r8hr2upy`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EcmRegion(self):
        """ECM region, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._InstanceId = params.get("InstanceId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachNetworkInterfaceResponse(AbstractModel):
    """AttachNetworkInterface response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Backend(AbstractModel):
    """CLB backend information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Unique real server ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Port: Listening port of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _Weight: Forwarding weight of the real server. Value range: [0, 100]. Default value: 10.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param _PrivateIpAddresses: Private IP of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param _RegisteredTime: Real server binding time
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegisteredTime: str
        :param _EniId: Unique ENI ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type EniId: str
        :param _PublicIpAddresses: Public IP of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param _InstanceName: Real server instance name
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        """
        self._InstanceId = None
        self._Port = None
        self._Weight = None
        self._PrivateIpAddresses = None
        self._RegisteredTime = None
        self._EniId = None
        self._PublicIpAddresses = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        """Unique real server ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        """Listening port of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        """Forwarding weight of the real server. Value range: [0, 100]. Default value: 10.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PrivateIpAddresses(self):
        """Private IP of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def RegisteredTime(self):
        """Real server binding time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegisteredTime

    @RegisteredTime.setter
    def RegisteredTime(self, RegisteredTime):
        self._RegisteredTime = RegisteredTime

    @property
    def EniId(self):
        """Unique ENI ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId

    @property
    def PublicIpAddresses(self):
        """Public IP of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def InstanceName(self):
        """Real server instance name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._RegisteredTime = params.get("RegisteredTime")
        self._EniId = params.get("EniId")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsRequest(AbstractModel):
    """BatchDeregisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _Targets: Unbound targets
        :type Targets: list of BatchTarget
        """
        self._LoadBalancerId = None
        self._Targets = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Targets(self):
        """Unbound targets
        :rtype: list of BatchTarget
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsResponse(AbstractModel):
    """BatchDeregisterTargets response structure.

    """

    def __init__(self):
        r"""
        :param _FailListenerIdSet: IDs of the listeners failed to be unbound
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailListenerIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FailListenerIdSet = None
        self._RequestId = None

    @property
    def FailListenerIdSet(self):
        """IDs of the listeners failed to be unbound
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._FailListenerIdSet

    @FailListenerIdSet.setter
    def FailListenerIdSet(self, FailListenerIdSet):
        self._FailListenerIdSet = FailListenerIdSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailListenerIdSet = params.get("FailListenerIdSet")
        self._RequestId = params.get("RequestId")


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ModifyList: List of weights to be modified in batches
        :type ModifyList: list of TargetsWeightRule
        """
        self._LoadBalancerId = None
        self._ModifyList = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ModifyList(self):
        """List of weights to be modified in batches
        :rtype: list of TargetsWeightRule
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
                obj = TargetsWeightRule()
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
    """BatchModifyTargetWeight response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _Targets: Bound targets
        :type Targets: list of BatchTarget
        """
        self._LoadBalancerId = None
        self._Targets = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Targets(self):
        """Bound targets
        :rtype: list of BatchTarget
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterTargetsResponse(AbstractModel):
    """BatchRegisterTargets response structure.

    """

    def __init__(self):
        r"""
        :param _FailListenerIdSet: IDs of the listeners failed to be bound. If this parameter is empty, all listeners have been bound successfully.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailListenerIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FailListenerIdSet = None
        self._RequestId = None

    @property
    def FailListenerIdSet(self):
        """IDs of the listeners failed to be bound. If this parameter is empty, all listeners have been bound successfully.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._FailListenerIdSet

    @FailListenerIdSet.setter
    def FailListenerIdSet(self, FailListenerIdSet):
        self._FailListenerIdSet = FailListenerIdSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailListenerIdSet = params.get("FailListenerIdSet")
        self._RequestId = params.get("RequestId")


class BatchTarget(AbstractModel):
    """CLB batch targets

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param _Port: Bound port
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _InstanceId: CVM instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _EniIp: ENI IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type EniIp: str
        :param _Weight: Weight of the CVM instance. Value range: [0, 100]. If it is not specified for binding the instance, 10 will be used by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        """
        self._ListenerId = None
        self._Port = None
        self._InstanceId = None
        self._EniIp = None
        self._Weight = None

    @property
    def ListenerId(self):
        """Listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Port(self):
        """Bound port
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        """CVM instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EniIp(self):
        """ENI IP
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp

    @property
    def Weight(self):
        """Weight of the CVM instance. Value range: [0, 100]. If it is not specified for binding the instance, 10 will be used by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        self._EniIp = params.get("EniIp")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class City(AbstractModel):
    """City information

    """

    def __init__(self):
        r"""
        :param _CityId: City ID
        :type CityId: str
        :param _CityName: City name
        :type CityName: str
        """
        self._CityId = None
        self._CityName = None

    @property
    def CityId(self):
        """City ID
        :rtype: str
        """
        return self._CityId

    @CityId.setter
    def CityId(self, CityId):
        self._CityId = CityId

    @property
    def CityName(self):
        """City name
        :rtype: str
        """
        return self._CityName

    @CityName.setter
    def CityName(self, CityName):
        self._CityName = CityName


    def _deserialize(self, params):
        self._CityId = params.get("CityId")
        self._CityName = params.get("CityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Country(AbstractModel):
    """Country/Region information

    """

    def __init__(self):
        r"""
        :param _CountryId: Country/Region ID
        :type CountryId: str
        :param _CountryName: Country/Region name
        :type CountryName: str
        """
        self._CountryId = None
        self._CountryName = None

    @property
    def CountryId(self):
        """Country/Region ID
        :rtype: str
        """
        return self._CountryId

    @CountryId.setter
    def CountryId(self, CountryId):
        self._CountryId = CountryId

    @property
    def CountryName(self):
        """Country/Region name
        :rtype: str
        """
        return self._CountryName

    @CountryName.setter
    def CountryName(self, CountryName):
        self._CountryName = CountryName


    def _deserialize(self, params):
        self._CountryId = params.get("CountryId")
        self._CountryName = params.get("CountryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHaVipRequest(AbstractModel):
    """CreateHaVip request structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID of the HAVIP.
        :type VpcId: str
        :param _SubnetId: Subnet ID of the HAVIP.
        :type SubnetId: str
        :param _HaVipName: HAVIP name.
        :type HaVipName: str
        :param _Vip: The specified virtual IP address, which must be within the IP range of the VPC and not in use. It will be automatically assigned if not specified.
        :type Vip: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._HaVipName = None
        self._Vip = None

    @property
    def VpcId(self):
        """VPC ID of the HAVIP.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID of the HAVIP.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def HaVipName(self):
        """HAVIP name.
        :rtype: str
        """
        return self._HaVipName

    @HaVipName.setter
    def HaVipName(self, HaVipName):
        self._HaVipName = HaVipName

    @property
    def Vip(self):
        """The specified virtual IP address, which must be within the IP range of the VPC and not in use. It will be automatically assigned if not specified.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._HaVipName = params.get("HaVipName")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHaVipResponse(AbstractModel):
    """CreateHaVip response structure.

    """

    def __init__(self):
        r"""
        :param _HaVip: HAVIP object.
        :type HaVip: :class:`tencentcloud.ecm.v20190719.models.HaVip`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HaVip = None
        self._RequestId = None

    @property
    def HaVip(self):
        """HAVIP object.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.HaVip`
        """
        return self._HaVip

    @HaVip.setter
    def HaVip(self, HaVip):
        self._HaVip = HaVip

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HaVip") is not None:
            self._HaVip = HaVip()
            self._HaVip._deserialize(params.get("HaVip"))
        self._RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    """CreateImage request structure.

    """

    def __init__(self):
        r"""
        :param _ImageName: Image name.
        :type ImageName: str
        :param _InstanceId: ID of the instance for which to make an image.
        :type InstanceId: str
        :param _ImageDescription: Image description.
        :type ImageDescription: str
        :param _ForcePoweroff: Whether to perform a forced shutdown to make an image. Valid values:
TRUE: yes
FALSE: no
Default value: FALSE.
        :type ForcePoweroff: str
        """
        self._ImageName = None
        self._InstanceId = None
        self._ImageDescription = None
        self._ForcePoweroff = None

    @property
    def ImageName(self):
        """Image name.
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def InstanceId(self):
        """ID of the instance for which to make an image.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageDescription(self):
        """Image description.
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def ForcePoweroff(self):
        """Whether to perform a forced shutdown to make an image. Valid values:
TRUE: yes
FALSE: no
Default value: FALSE.
        :rtype: str
        """
        return self._ForcePoweroff

    @ForcePoweroff.setter
    def ForcePoweroff(self, ForcePoweroff):
        self._ForcePoweroff = ForcePoweroff


    def _deserialize(self, params):
        self._ImageName = params.get("ImageName")
        self._InstanceId = params.get("InstanceId")
        self._ImageDescription = params.get("ImageDescription")
        self._ForcePoweroff = params.get("ForcePoweroff")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    """CreateImage response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair request structure.

    """

    def __init__(self):
        r"""
        :param _KeyName: Key pair name, which can contain up to 25 digits, letters, and underscores.
        :type KeyName: str
        """
        self._KeyName = None

    @property
    def KeyName(self):
        """Key pair name, which can contain up to 25 digits, letters, and underscores.
        :rtype: str
        """
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyPairResponse(AbstractModel):
    """CreateKeyPair response structure.

    """

    def __init__(self):
        r"""
        :param _KeyPair: Key pair information.
        :type KeyPair: :class:`tencentcloud.ecm.v20190719.models.KeyPair`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyPair = None
        self._RequestId = None

    @property
    def KeyPair(self):
        """Key pair information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.KeyPair`
        """
        return self._KeyPair

    @KeyPair.setter
    def KeyPair(self, KeyPair):
        self._KeyPair = KeyPair

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyPair") is not None:
            self._KeyPair = KeyPair()
            self._KeyPair._deserialize(params.get("KeyPair"))
        self._RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    """CreateListener request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _Ports: Specifies for which ports to create listeners. Each port corresponds to a new listener
        :type Ports: list of int
        :param _Protocol: Listener protocol. Valid values: TCP, UDP
        :type Protocol: str
        :param _ListenerNames: List of names of the listeners to be created. The array of names and array of ports are in one-to-one correspondence. If you do not want to name them now, you do not need to provide this parameter.
        :type ListenerNames: list of str
        :param _HealthCheck: Health check parameters
        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        :param _SessionExpireTime: Session persistence time in seconds. Value range: 30–3600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.
        :type SessionExpireTime: int
        :param _Scheduler: Forwarding method of the listener. Valid values: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR.
        :type Scheduler: str
        :param _SessionType: Session persistence type. Valid values: NORMAL: the default session persistence type; QUIC_CID: session persistence by QUIC connection ID. The `QUIC_CID` value can only be configured in UDP listeners. If this field is not specified, the default session persistence type will be used.
        :type SessionType: str
        :param _EndPorts: End ports of port ranges, which must be the same as `Ports` in length.
        :type EndPorts: list of int
        """
        self._LoadBalancerId = None
        self._Ports = None
        self._Protocol = None
        self._ListenerNames = None
        self._HealthCheck = None
        self._SessionExpireTime = None
        self._Scheduler = None
        self._SessionType = None
        self._EndPorts = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Ports(self):
        """Specifies for which ports to create listeners. Each port corresponds to a new listener
        :rtype: list of int
        """
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Protocol(self):
        """Listener protocol. Valid values: TCP, UDP
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerNames(self):
        """List of names of the listeners to be created. The array of names and array of ports are in one-to-one correspondence. If you do not want to name them now, you do not need to provide this parameter.
        :rtype: list of str
        """
        return self._ListenerNames

    @ListenerNames.setter
    def ListenerNames(self, ListenerNames):
        self._ListenerNames = ListenerNames

    @property
    def HealthCheck(self):
        """Health check parameters
        :rtype: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def SessionExpireTime(self):
        """Session persistence time in seconds. Value range: 30–3600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.
        :rtype: int
        """
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def Scheduler(self):
        """Forwarding method of the listener. Valid values: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR.
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SessionType(self):
        """Session persistence type. Valid values: NORMAL: the default session persistence type; QUIC_CID: session persistence by QUIC connection ID. The `QUIC_CID` value can only be configured in UDP listeners. If this field is not specified, the default session persistence type will be used.
        :rtype: str
        """
        return self._SessionType

    @SessionType.setter
    def SessionType(self, SessionType):
        self._SessionType = SessionType

    @property
    def EndPorts(self):
        """End ports of port ranges, which must be the same as `Ports` in length.
        :rtype: list of int
        """
        return self._EndPorts

    @EndPorts.setter
    def EndPorts(self, EndPorts):
        self._EndPorts = EndPorts


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Ports = params.get("Ports")
        self._Protocol = params.get("Protocol")
        self._ListenerNames = params.get("ListenerNames")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._SessionExpireTime = params.get("SessionExpireTime")
        self._Scheduler = params.get("Scheduler")
        self._SessionType = params.get("SessionType")
        self._EndPorts = params.get("EndPorts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    """CreateListener response structure.

    """

    def __init__(self):
        r"""
        :param _ListenerIds: Array of unique IDs of the created listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ListenerIds = None
        self._RequestId = None

    @property
    def ListenerIds(self):
        """Array of unique IDs of the created listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ListenerIds = params.get("ListenerIds")
        self._RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param _LoadBalancerType: Network type of the CLB instance. Currently, you can pass in only `OPEN`, which indicates public network.
        :type LoadBalancerType: str
        :param _VipIsp: CMCC: China Mobile; CTCC: China Telecom; CUCC: China Unicom.
        :type VipIsp: str
        :param _LoadBalancerName: CLB instance name, which will take effect only when one instance is created. It can contain 1–50 letters, digits, hyphens, and underscores.
Note: if the name of the new CLB instance already exists, a default name will be generated automatically.
        :type LoadBalancerName: str
        :param _VpcId: Network ID of the target device on the CLB backend, such as `vpc-12345678`.
        :type VpcId: str
        :param _Number: Number of CLB instances to be created. Default value: 1.
        :type Number: int
        :param _InternetAccessible: CLB information such as bandwidth limit.
        :type InternetAccessible: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        :param _Tags: Tags.
        :type Tags: list of TagInfo
        :param _SecurityGroups: Security groups.
        :type SecurityGroups: list of str
        :param _AddressIPVersion: IP version. Valid values: `IPV4` (default), `IPv6FullChain` (IPv6 version). This parameter is only for public network CLB instances.
        :type AddressIPVersion: str
        :param _SubnetId: Subnet ID. This parameter is required for IPv6 CLB instances.
        :type SubnetId: str
        """
        self._EcmRegion = None
        self._LoadBalancerType = None
        self._VipIsp = None
        self._LoadBalancerName = None
        self._VpcId = None
        self._Number = None
        self._InternetAccessible = None
        self._Tags = None
        self._SecurityGroups = None
        self._AddressIPVersion = None
        self._SubnetId = None

    @property
    def EcmRegion(self):
        """ECM region, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def LoadBalancerType(self):
        """Network type of the CLB instance. Currently, you can pass in only `OPEN`, which indicates public network.
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def VipIsp(self):
        """CMCC: China Mobile; CTCC: China Telecom; CUCC: China Unicom.
        :rtype: str
        """
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def LoadBalancerName(self):
        """CLB instance name, which will take effect only when one instance is created. It can contain 1–50 letters, digits, hyphens, and underscores.
Note: if the name of the new CLB instance already exists, a default name will be generated automatically.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def VpcId(self):
        """Network ID of the target device on the CLB backend, such as `vpc-12345678`.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Number(self):
        """Number of CLB instances to be created. Default value: 1.
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def InternetAccessible(self):
        """CLB information such as bandwidth limit.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def Tags(self):
        """Tags.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SecurityGroups(self):
        """Security groups.
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def AddressIPVersion(self):
        """IP version. Valid values: `IPV4` (default), `IPv6FullChain` (IPv6 version). This parameter is only for public network CLB instances.
        :rtype: str
        """
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def SubnetId(self):
        """Subnet ID. This parameter is required for IPv6 CLB instances.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._VipIsp = params.get("VipIsp")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._VpcId = params.get("VpcId")
        self._Number = params.get("Number")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = LoadBalancerInternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SecurityGroups = params.get("SecurityGroups")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: Array of CLB instance IDs
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancerIds = None
        self._RequestId = None

    @property
    def LoadBalancerIds(self):
        """Array of CLB instance IDs
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._RequestId = params.get("RequestId")


class CreateModuleRequest(AbstractModel):
    """CreateModule request structure.

    """

    def __init__(self):
        r"""
        :param _ModuleName: Module name, such as video live streaming module name. It cannot start with a space or exceed 60 characters.
        :type ModuleName: str
        :param _DefaultBandWidth: Default bandwidth in Mbps. It cannot exceed the bandwidth range. For more information, see `DescribeConfig`.
        :type DefaultBandWidth: int
        :param _DefaultImageId: Default image ID, such as `img-qsdf3ff2`.
        :type DefaultImageId: str
        :param _InstanceType: Model ID.
        :type InstanceType: str
        :param _DefaultSystemDiskSize: Default system disk size in GB. It is 50 GB by default and cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :type DefaultSystemDiskSize: int
        :param _DefaultDataDiskSize: Default data disk size in GB. It cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :type DefaultDataDiskSize: int
        :param _CloseIpDirect: Whether to disable IP direct access. Valid values:
true: yes
false: no
        :type CloseIpDirect: bool
        :param _TagSpecification: List of tags.
        :type TagSpecification: list of TagSpecification
        :param _SecurityGroups: List of default module security groups
        :type SecurityGroups: list of str
        :param _DefaultBandWidthIn: Default inbound bandwidth in Mbps. It cannot exceed the bandwidth range. For more information, see `DescribeConfig`.
        :type DefaultBandWidthIn: int
        :param _DisableWanIp: Whether to prohibit public IP assignment
        :type DisableWanIp: bool
        :param _SystemDisk: System disk information.
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param _DataDisks: Data disk information.
        :type DataDisks: list of DataDisk
        """
        self._ModuleName = None
        self._DefaultBandWidth = None
        self._DefaultImageId = None
        self._InstanceType = None
        self._DefaultSystemDiskSize = None
        self._DefaultDataDiskSize = None
        self._CloseIpDirect = None
        self._TagSpecification = None
        self._SecurityGroups = None
        self._DefaultBandWidthIn = None
        self._DisableWanIp = None
        self._SystemDisk = None
        self._DataDisks = None

    @property
    def ModuleName(self):
        """Module name, such as video live streaming module name. It cannot start with a space or exceed 60 characters.
        :rtype: str
        """
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName

    @property
    def DefaultBandWidth(self):
        """Default bandwidth in Mbps. It cannot exceed the bandwidth range. For more information, see `DescribeConfig`.
        :rtype: int
        """
        return self._DefaultBandWidth

    @DefaultBandWidth.setter
    def DefaultBandWidth(self, DefaultBandWidth):
        self._DefaultBandWidth = DefaultBandWidth

    @property
    def DefaultImageId(self):
        """Default image ID, such as `img-qsdf3ff2`.
        :rtype: str
        """
        return self._DefaultImageId

    @DefaultImageId.setter
    def DefaultImageId(self, DefaultImageId):
        self._DefaultImageId = DefaultImageId

    @property
    def InstanceType(self):
        """Model ID.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DefaultSystemDiskSize(self):
        """Default system disk size in GB. It is 50 GB by default and cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :rtype: int
        """
        return self._DefaultSystemDiskSize

    @DefaultSystemDiskSize.setter
    def DefaultSystemDiskSize(self, DefaultSystemDiskSize):
        self._DefaultSystemDiskSize = DefaultSystemDiskSize

    @property
    def DefaultDataDiskSize(self):
        """Default data disk size in GB. It cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :rtype: int
        """
        return self._DefaultDataDiskSize

    @DefaultDataDiskSize.setter
    def DefaultDataDiskSize(self, DefaultDataDiskSize):
        self._DefaultDataDiskSize = DefaultDataDiskSize

    @property
    def CloseIpDirect(self):
        """Whether to disable IP direct access. Valid values:
true: yes
false: no
        :rtype: bool
        """
        return self._CloseIpDirect

    @CloseIpDirect.setter
    def CloseIpDirect(self, CloseIpDirect):
        self._CloseIpDirect = CloseIpDirect

    @property
    def TagSpecification(self):
        """List of tags.
        :rtype: list of TagSpecification
        """
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def SecurityGroups(self):
        """List of default module security groups
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def DefaultBandWidthIn(self):
        """Default inbound bandwidth in Mbps. It cannot exceed the bandwidth range. For more information, see `DescribeConfig`.
        :rtype: int
        """
        return self._DefaultBandWidthIn

    @DefaultBandWidthIn.setter
    def DefaultBandWidthIn(self, DefaultBandWidthIn):
        self._DefaultBandWidthIn = DefaultBandWidthIn

    @property
    def DisableWanIp(self):
        """Whether to prohibit public IP assignment
        :rtype: bool
        """
        return self._DisableWanIp

    @DisableWanIp.setter
    def DisableWanIp(self, DisableWanIp):
        self._DisableWanIp = DisableWanIp

    @property
    def SystemDisk(self):
        """System disk information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """Data disk information.
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks


    def _deserialize(self, params):
        self._ModuleName = params.get("ModuleName")
        self._DefaultBandWidth = params.get("DefaultBandWidth")
        self._DefaultImageId = params.get("DefaultImageId")
        self._InstanceType = params.get("InstanceType")
        self._DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self._DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        self._CloseIpDirect = params.get("CloseIpDirect")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._SecurityGroups = params.get("SecurityGroups")
        self._DefaultBandWidthIn = params.get("DefaultBandWidthIn")
        self._DisableWanIp = params.get("DisableWanIp")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModuleResponse(AbstractModel):
    """CreateModule response structure.

    """

    def __init__(self):
        r"""
        :param _ModuleId: Module ID. It is the ID assigned to a module after it is created successfully.
        :type ModuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ModuleId = None
        self._RequestId = None

    @property
    def ModuleId(self):
        """Module ID. It is the ID assigned to a module after it is created successfully.
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._RequestId = params.get("RequestId")


class CreateNetworkInterfaceRequest(AbstractModel):
    """CreateNetworkInterface request structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC instance ID, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :type VpcId: str
        :param _NetworkInterfaceName: ENI name, which can contain up to 60 bytes.
        :type NetworkInterfaceName: str
        :param _SubnetId: Subnet instance ID of the ENI, such as 'subnet-0ap8nwca'.
        :type SubnetId: str
        :param _EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param _NetworkInterfaceDescription: ENI description. You can enter any information within 60 characters.
        :type NetworkInterfaceDescription: str
        :param _SecondaryPrivateIpAddressCount: Number of private IP addresses applied for. The total number of private IP addresses cannot exceed the quota.
        :type SecondaryPrivateIpAddressCount: int
        :param _SecurityGroupIds: The security group to be bound with, such as ['sg-1dd51d'].
        :type SecurityGroupIds: list of str
        :param _PrivateIpAddresses: Information of the specified private IPs. You can specify up to 10 IPs at a time.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param _Tags: List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self._VpcId = None
        self._NetworkInterfaceName = None
        self._SubnetId = None
        self._EcmRegion = None
        self._NetworkInterfaceDescription = None
        self._SecondaryPrivateIpAddressCount = None
        self._SecurityGroupIds = None
        self._PrivateIpAddresses = None
        self._Tags = None

    @property
    def VpcId(self):
        """VPC instance ID, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def NetworkInterfaceName(self):
        """ENI name, which can contain up to 60 bytes.
        :rtype: str
        """
        return self._NetworkInterfaceName

    @NetworkInterfaceName.setter
    def NetworkInterfaceName(self, NetworkInterfaceName):
        self._NetworkInterfaceName = NetworkInterfaceName

    @property
    def SubnetId(self):
        """Subnet instance ID of the ENI, such as 'subnet-0ap8nwca'.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EcmRegion(self):
        """ECM region, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceDescription(self):
        """ENI description. You can enter any information within 60 characters.
        :rtype: str
        """
        return self._NetworkInterfaceDescription

    @NetworkInterfaceDescription.setter
    def NetworkInterfaceDescription(self, NetworkInterfaceDescription):
        self._NetworkInterfaceDescription = NetworkInterfaceDescription

    @property
    def SecondaryPrivateIpAddressCount(self):
        """Number of private IP addresses applied for. The total number of private IP addresses cannot exceed the quota.
        :rtype: int
        """
        return self._SecondaryPrivateIpAddressCount

    @SecondaryPrivateIpAddressCount.setter
    def SecondaryPrivateIpAddressCount(self, SecondaryPrivateIpAddressCount):
        self._SecondaryPrivateIpAddressCount = SecondaryPrivateIpAddressCount

    @property
    def SecurityGroupIds(self):
        """The security group to be bound with, such as ['sg-1dd51d'].
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def PrivateIpAddresses(self):
        """Information of the specified private IPs. You can specify up to 10 IPs at a time.
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Tags(self):
        """List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._NetworkInterfaceName = params.get("NetworkInterfaceName")
        self._SubnetId = params.get("SubnetId")
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self._SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("PrivateIpAddresses") is not None:
            self._PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddresses.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetworkInterfaceResponse(AbstractModel):
    """CreateNetworkInterface response structure.

    """

    def __init__(self):
        r"""
        :param _NetworkInterface: ENI instance.
        :type NetworkInterface: :class:`tencentcloud.ecm.v20190719.models.NetworkInterface`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NetworkInterface = None
        self._RequestId = None

    @property
    def NetworkInterface(self):
        """ENI instance.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.NetworkInterface`
        """
        return self._NetworkInterface

    @NetworkInterface.setter
    def NetworkInterface(self, NetworkInterface):
        self._NetworkInterface = NetworkInterface

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NetworkInterface") is not None:
            self._NetworkInterface = NetworkInterface()
            self._NetworkInterface._deserialize(params.get("NetworkInterface"))
        self._RequestId = params.get("RequestId")


class CreateRouteTableRequest(AbstractModel):
    """CreateRouteTable request structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: ID of the VPC instance to be manipulated, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :type VpcId: str
        :param _RouteTableName: Route table name, which can contain up to 60 bytes.
        :type RouteTableName: str
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        """
        self._VpcId = None
        self._RouteTableName = None
        self._EcmRegion = None

    @property
    def VpcId(self):
        """ID of the VPC instance to be manipulated, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def RouteTableName(self):
        """Route table name, which can contain up to 60 bytes.
        :rtype: str
        """
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._RouteTableName = params.get("RouteTableName")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRouteTableResponse(AbstractModel):
    """CreateRouteTable response structure.

    """

    def __init__(self):
        r"""
        :param _RouteTable: Route table object
        :type RouteTable: :class:`tencentcloud.ecm.v20190719.models.RouteTable`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RouteTable = None
        self._RequestId = None

    @property
    def RouteTable(self):
        """Route table object
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RouteTable`
        """
        return self._RouteTable

    @RouteTable.setter
    def RouteTable(self, RouteTable):
        self._RouteTable = RouteTable

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RouteTable") is not None:
            self._RouteTable = RouteTable()
            self._RouteTable._deserialize(params.get("RouteTable"))
        self._RequestId = params.get("RequestId")


class CreateRoutesRequest(AbstractModel):
    """CreateRoutes request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableId: Route table instance ID.
        :type RouteTableId: str
        :param _Routes: Routing policy object to be created.
        :type Routes: list of Route
        """
        self._RouteTableId = None
        self._Routes = None

    @property
    def RouteTableId(self):
        """Route table instance ID.
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def Routes(self):
        """Routing policy object to be created.
        :rtype: list of Route
        """
        return self._Routes

    @Routes.setter
    def Routes(self, Routes):
        self._Routes = Routes


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self._Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self._Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoutesResponse(AbstractModel):
    """CreateRoutes response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of added instances.
        :type TotalCount: int
        :param _RouteTableSet: Route table object.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RouteTableSet: list of RouteTable
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RouteTableSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of added instances.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RouteTableSet(self):
        """Route table object.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of RouteTable
        """
        return self._RouteTableSet

    @RouteTableSet.setter
    def RouteTableSet(self, RouteTableSet):
        self._RouteTableSet = RouteTableSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self._RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTable()
                obj._deserialize(item)
                self._RouteTableSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateSecurityGroupPoliciesRequest(AbstractModel):
    """CreateSecurityGroupPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :type SecurityGroupId: str
        :param _SecurityGroupPolicySet: Security group policy set.
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        self._SecurityGroupId = None
        self._SecurityGroupPolicySet = None

    @property
    def SecurityGroupId(self):
        """Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupPolicySet(self):
        """Security group policy set.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = SecurityGroupPolicySet()
            self._SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupPoliciesResponse(AbstractModel):
    """CreateSecurityGroupPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: Security group name, which can be customized with up to 60 characters.
        :type GroupName: str
        :param _GroupDescription: Security group remarks, which can contain up to 100 characters.
        :type GroupDescription: str
        :param _Tags: List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self._GroupName = None
        self._GroupDescription = None
        self._Tags = None

    @property
    def GroupName(self):
        """Security group name, which can be customized with up to 60 characters.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupDescription(self):
        """Security group remarks, which can contain up to 100 characters.
        :rtype: str
        """
        return self._GroupDescription

    @GroupDescription.setter
    def GroupDescription(self, GroupDescription):
        self._GroupDescription = GroupDescription

    @property
    def Tags(self):
        """List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupDescription = params.get("GroupDescription")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupResponse(AbstractModel):
    """CreateSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroup: Security group object.
        :type SecurityGroup: :class:`tencentcloud.ecm.v20190719.models.SecurityGroup`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityGroup = None
        self._RequestId = None

    @property
    def SecurityGroup(self):
        """Security group object.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroup`
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self._SecurityGroup = SecurityGroup()
            self._SecurityGroup._deserialize(params.get("SecurityGroup"))
        self._RequestId = params.get("RequestId")


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet request structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: ID of the VPC instance to be manipulated, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :type VpcId: str
        :param _SubnetName: Subnet name, which can contain up to 60 bytes.
        :type SubnetName: str
        :param _CidrBlock: Subnet IP address range. It must be within the VPC IP address range. Subnet IP address ranges cannot overlap with each other within the same VPC.
        :type CidrBlock: str
        :param _Zone: AZ ID of the subnet. You can select different AZs for different subnets for cross-AZ disaster recovery.
        :type Zone: str
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _Tags: List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        """
        self._VpcId = None
        self._SubnetName = None
        self._CidrBlock = None
        self._Zone = None
        self._EcmRegion = None
        self._Tags = None

    @property
    def VpcId(self):
        """ID of the VPC instance to be manipulated, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetName(self):
        """Subnet name, which can contain up to 60 bytes.
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        """Subnet IP address range. It must be within the VPC IP address range. Subnet IP address ranges cannot overlap with each other within the same VPC.
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Zone(self):
        """AZ ID of the subnet. You can select different AZs for different subnets for cross-AZ disaster recovery.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Tags(self):
        """List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetName = params.get("SubnetName")
        self._CidrBlock = params.get("CidrBlock")
        self._Zone = params.get("Zone")
        self._EcmRegion = params.get("EcmRegion")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet response structure.

    """

    def __init__(self):
        r"""
        :param _Subnet: Subnet object.
        :type Subnet: :class:`tencentcloud.ecm.v20190719.models.Subnet`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Subnet = None
        self._RequestId = None

    @property
    def Subnet(self):
        """Subnet object.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Subnet`
        """
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Subnet") is not None:
            self._Subnet = Subnet()
            self._Subnet._deserialize(params.get("Subnet"))
        self._RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc request structure.

    """

    def __init__(self):
        r"""
        :param _VpcName: VPC name, which can contain up to 60 bytes.
        :type VpcName: str
        :param _CidrBlock: VPC CIDR block, which must fall within the following private network IP ranges: 10.*.0.0/16, 172.[16-31].0.0/16, and 192.168.0.0/16.
        :type CidrBlock: str
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _EnableMulticast: Whether multicast is enabled. true: enabled; false: disabled. This parameter is not supported currently
        :type EnableMulticast: str
        :param _DnsServers: DNS address (not supported currently). Up to 4 addresses can be supported.
        :type DnsServers: list of str
        :param _DomainName: Domain name. This parameter is not supported currently
        :type DomainName: str
        :param _Tags: List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :type Tags: list of Tag
        :param _Description: Description
        :type Description: str
        """
        self._VpcName = None
        self._CidrBlock = None
        self._EcmRegion = None
        self._EnableMulticast = None
        self._DnsServers = None
        self._DomainName = None
        self._Tags = None
        self._Description = None

    @property
    def VpcName(self):
        """VPC name, which can contain up to 60 bytes.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def CidrBlock(self):
        """VPC CIDR block, which must fall within the following private network IP ranges: 10.*.0.0/16, 172.[16-31].0.0/16, and 192.168.0.0/16.
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def EnableMulticast(self):
        """Whether multicast is enabled. true: enabled; false: disabled. This parameter is not supported currently
        :rtype: str
        """
        return self._EnableMulticast

    @EnableMulticast.setter
    def EnableMulticast(self, EnableMulticast):
        self._EnableMulticast = EnableMulticast

    @property
    def DnsServers(self):
        """DNS address (not supported currently). Up to 4 addresses can be supported.
        :rtype: list of str
        """
        return self._DnsServers

    @DnsServers.setter
    def DnsServers(self, DnsServers):
        self._DnsServers = DnsServers

    @property
    def DomainName(self):
        """Domain name. This parameter is not supported currently
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Tags(self):
        """List of bound tags, such as [{"Key": "city", "Value": "shanghai"}].
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._VpcName = params.get("VpcName")
        self._CidrBlock = params.get("CidrBlock")
        self._EcmRegion = params.get("EcmRegion")
        self._EnableMulticast = params.get("EnableMulticast")
        self._DnsServers = params.get("DnsServers")
        self._DomainName = params.get("DomainName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcResponse(AbstractModel):
    """CreateVpc response structure.

    """

    def __init__(self):
        r"""
        :param _Vpc: VPC object.
        :type Vpc: :class:`tencentcloud.ecm.v20190719.models.VpcInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Vpc = None
        self._RequestId = None

    @property
    def Vpc(self):
        """VPC object.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.VpcInfo`
        """
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self._Vpc = VpcInfo()
            self._Vpc._deserialize(params.get("Vpc"))
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Data disk information

    """

    def __init__(self):
        r"""
        :param _DiskSize: Data disk size in GB.
        :type DiskSize: int
        :param _DiskType: Data disk type. Valid values:
- LOCAL_BASIC: local disk
- CLOUD_PREMIUM: Premium Cloud Storage

Default value: LOCAL_BASIC.
        :type DiskType: str
        """
        self._DiskSize = None
        self._DiskType = None

    @property
    def DiskSize(self):
        """Data disk size in GB.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        """Data disk type. Valid values:
- LOCAL_BASIC: local disk
- CLOUD_PREMIUM: Premium Cloud Storage

Default value: LOCAL_BASIC.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHaVipRequest(AbstractModel):
    """DeleteHaVip request structure.

    """

    def __init__(self):
        r"""
        :param _HaVipId: Unique HAVIP ID, such as `havip-9o233uri`.
        :type HaVipId: str
        """
        self._HaVipId = None

    @property
    def HaVipId(self):
        """Unique HAVIP ID, such as `havip-9o233uri`.
        :rtype: str
        """
        return self._HaVipId

    @HaVipId.setter
    def HaVipId(self, HaVipId):
        self._HaVipId = HaVipId


    def _deserialize(self, params):
        self._HaVipId = params.get("HaVipId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHaVipResponse(AbstractModel):
    """DeleteHaVip response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteImageRequest(AbstractModel):
    """DeleteImage request structure.

    """

    def __init__(self):
        r"""
        :param _ImageIDSet: List of image IDs.
        :type ImageIDSet: list of str
        """
        self._ImageIDSet = None

    @property
    def ImageIDSet(self):
        """List of image IDs.
        :rtype: list of str
        """
        return self._ImageIDSet

    @ImageIDSet.setter
    def ImageIDSet(self, ImageIDSet):
        self._ImageIDSet = ImageIDSet


    def _deserialize(self, params):
        self._ImageIDSet = params.get("ImageIDSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageResponse(AbstractModel):
    """DeleteImage response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    """DeleteListener request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: ID of the listener to be deleted
        :type ListenerId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        """ID of the listener to be deleted
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    """DeleteListener response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerIds: Array of IDs of the listeners to be deleted. If this parameter is left empty, all listeners of the CLB instance will be deleted
        :type ListenerIds: list of str
        """
        self._LoadBalancerId = None
        self._ListenerIds = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        """Array of IDs of the listeners to be deleted. If this parameter is left empty, all listeners of the CLB instance will be deleted
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerListenersResponse(AbstractModel):
    """DeleteLoadBalancerListeners response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: Array of IDs of the CLB instances to be deleted. Array length limit: 20
        :type LoadBalancerIds: list of str
        """
        self._LoadBalancerIds = None

    @property
    def LoadBalancerIds(self):
        """Array of IDs of the CLB instances to be deleted. Array length limit: 20
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteModuleRequest(AbstractModel):
    """DeleteModule request structure.

    """

    def __init__(self):
        r"""
        :param _ModuleId: Module ID, such as `em-qn46snq8`.
        :type ModuleId: str
        """
        self._ModuleId = None

    @property
    def ModuleId(self):
        """Module ID, such as `em-qn46snq8`.
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModuleResponse(AbstractModel):
    """DeleteModule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteNetworkInterfaceRequest(AbstractModel):
    """DeleteNetworkInterface request structure.

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param _EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        """
        self._NetworkInterfaceId = None
        self._EcmRegion = None

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-m6dyj72l`.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def EcmRegion(self):
        """ECM region, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNetworkInterfaceResponse(AbstractModel):
    """DeleteNetworkInterface response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRouteTableRequest(AbstractModel):
    """DeleteRouteTable request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableId: Route table instance ID, such as `rtb-azd4dt1c`
        :type RouteTableId: str
        """
        self._RouteTableId = None

    @property
    def RouteTableId(self):
        """Route table instance ID, such as `rtb-azd4dt1c`
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteTableResponse(AbstractModel):
    """DeleteRouteTable response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRoutesRequest(AbstractModel):
    """DeleteRoutes request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableId: Unique route table ID.
        :type RouteTableId: str
        :param _Routes: Routing policy object.
        :type Routes: list of Route
        """
        self._RouteTableId = None
        self._Routes = None

    @property
    def RouteTableId(self):
        """Unique route table ID.
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def Routes(self):
        """Routing policy object.
        :rtype: list of Route
        """
        return self._Routes

    @Routes.setter
    def Routes(self, Routes):
        self._Routes = Routes


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self._Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self._Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoutesResponse(AbstractModel):
    """DeleteRoutes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSecurityGroupPoliciesRequest(AbstractModel):
    """DeleteSecurityGroupPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :type SecurityGroupId: str
        :param _SecurityGroupPolicySet: Security group policy set. You can only delete one or more policies in one direction in one request. Both PolicyIndex-matching deletion and security group policy-matching deletion methods are supported. You can use only one matching method in one request.
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        self._SecurityGroupId = None
        self._SecurityGroupPolicySet = None

    @property
    def SecurityGroupId(self):
        """Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupPolicySet(self):
        """Security group policy set. You can only delete one or more policies in one direction in one request. Both PolicyIndex-matching deletion and security group policy-matching deletion methods are supported. You can use only one matching method in one request.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = SecurityGroupPolicySet()
            self._SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupPoliciesResponse(AbstractModel):
    """DeleteSecurityGroupPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :type SecurityGroupId: str
        """
        self._SecurityGroupId = None

    @property
    def SecurityGroupId(self):
        """Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupResponse(AbstractModel):
    """DeleteSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: List of IDs of the snapshots to be deleted, which can be queried through [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :type SnapshotIds: list of str
        :param _DeleteBindImages: Whether to force delete the images associated with the snapshot.
        :type DeleteBindImages: bool
        """
        self._SnapshotIds = None
        self._DeleteBindImages = None

    @property
    def SnapshotIds(self):
        """List of IDs of the snapshots to be deleted, which can be queried through [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :rtype: list of str
        """
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def DeleteBindImages(self):
        """Whether to force delete the images associated with the snapshot.
        :rtype: bool
        """
        return self._DeleteBindImages

    @DeleteBindImages.setter
    def DeleteBindImages(self, DeleteBindImages):
        self._DeleteBindImages = DeleteBindImages


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        self._DeleteBindImages = params.get("DeleteBindImages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet request structure.

    """

    def __init__(self):
        r"""
        :param _SubnetId: Subnet instance ID, which can be obtained from the `SubnetId` field in the returned value of the `DescribeSubnets` API.
        :type SubnetId: str
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        """
        self._SubnetId = None
        self._EcmRegion = None

    @property
    def SubnetId(self):
        """Subnet instance ID, which can be obtained from the `SubnetId` field in the returned value of the `DescribeSubnets` API.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubnetResponse(AbstractModel):
    """DeleteSubnet response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteVpcRequest(AbstractModel):
    """DeleteVpc request structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC instance ID, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :type VpcId: str
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        """
        self._VpcId = None
        self._EcmRegion = None

    @property
    def VpcId(self):
        """VPC instance ID, which can be obtained from the `VpcId` field in the returned value of the `DescribeVpcs` API.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcResponse(AbstractModel):
    """DeleteVpc response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAddressQuotaRequest(AbstractModel):
    """DescribeAddressQuota request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        """
        self._EcmRegion = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressQuotaResponse(AbstractModel):
    """DescribeAddressQuota response structure.

    """

    def __init__(self):
        r"""
        :param _QuotaSet: Quota information of EIPs in the account.
        :type QuotaSet: list of EipQuota
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QuotaSet = None
        self._RequestId = None

    @property
    def QuotaSet(self):
        """Quota information of EIPs in the account.
        :rtype: list of EipQuota
        """
        return self._QuotaSet

    @QuotaSet.setter
    def QuotaSet(self, QuotaSet):
        self._QuotaSet = QuotaSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self._QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = EipQuota()
                obj._deserialize(item)
                self._QuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAddressesRequest(AbstractModel):
    """DescribeAddresses request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _AddressIds: List of unique IDs of EIPs, such as `eip-11112222`. `AddressIds` and `Filters` cannot be specified at the same time.
        :type AddressIds: list of str
        :param _Filters: Each request can contain up to 10 `Filters` and 5 `Filter.Values`. `AddressIds` and `Filters` cannot be specified at the same time. The detailed filters are as follows:
address-id - String - Required: no - (Filter) Filter by unique EIP ID, such as `eip-11112222`.
address-name - String - Required: no - (Filter) Filter by EIP name. Fuzzy filtering is not supported.
address-ip - String - Required: no - (Filter) Filter by EIP IP address.
address-status - String - Required: no - (Filter) Filter by EIP status. Value range: see the list of EIP status.
instance-id - String - Required: no - (Filter) Filter by the ID of the instance bound to the EIP, such as `ins-11112222`.
private-ip-address - String - Required: no - (Filter) Filter by the private IP bound to the EIP.
network-interface-id - String - Required: no - (Filter) Filter by ID of the ENI bound to the EIP, such as `eni-11112222`.
is-arrears - String - Required: no - (Filter) Filter by whether the EIP is overdue (TRUE: the EIP is overdue | FALSE: the billing status of the EIP is normal)
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._EcmRegion = None
        self._AddressIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressIds(self):
        """List of unique IDs of EIPs, such as `eip-11112222`. `AddressIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._AddressIds

    @AddressIds.setter
    def AddressIds(self, AddressIds):
        self._AddressIds = AddressIds

    @property
    def Filters(self):
        """Each request can contain up to 10 `Filters` and 5 `Filter.Values`. `AddressIds` and `Filters` cannot be specified at the same time. The detailed filters are as follows:
address-id - String - Required: no - (Filter) Filter by unique EIP ID, such as `eip-11112222`.
address-name - String - Required: no - (Filter) Filter by EIP name. Fuzzy filtering is not supported.
address-ip - String - Required: no - (Filter) Filter by EIP IP address.
address-status - String - Required: no - (Filter) Filter by EIP status. Value range: see the list of EIP status.
instance-id - String - Required: no - (Filter) Filter by the ID of the instance bound to the EIP, such as `ins-11112222`.
private-ip-address - String - Required: no - (Filter) Filter by the private IP bound to the EIP.
network-interface-id - String - Required: no - (Filter) Filter by ID of the ENI bound to the EIP, such as `eni-11112222`.
is-arrears - String - Required: no - (Filter) Filter by whether the EIP is overdue (TRUE: the EIP is overdue | FALSE: the billing status of the EIP is normal)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressIds = params.get("AddressIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressesResponse(AbstractModel):
    """DescribeAddresses response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible EIPs.
        :type TotalCount: int
        :param _AddressSet: List of EIP details.
        :type AddressSet: list of Address
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AddressSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible EIPs.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AddressSet(self):
        """List of EIP details.
        :rtype: list of Address
        """
        return self._AddressSet

    @AddressSet.setter
    def AddressSet(self, AddressSet):
        self._AddressSet = AddressSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AddressSet") is not None:
            self._AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self._AddressSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBaseOverviewRequest(AbstractModel):
    """DescribeBaseOverview request structure.

    """


class DescribeBaseOverviewResponse(AbstractModel):
    """DescribeBaseOverview response structure.

    """

    def __init__(self):
        r"""
        :param _ModuleNum: Number of modules
        :type ModuleNum: int
        :param _NodeNum: Number of nodes
        :type NodeNum: int
        :param _VcpuNum: Number of CPU cores
        :type VcpuNum: int
        :param _MemoryNum: Memory size in GB
        :type MemoryNum: int
        :param _StorageNum: Disk size in GB
        :type StorageNum: int
        :param _NetworkNum: Yesterday's network peak in Mbps
        :type NetworkNum: int
        :param _InstanceNum: Number of instances
        :type InstanceNum: int
        :param _RunningNum: Number of running instances
        :type RunningNum: int
        :param _IsolationNum: Number of isolated instances
        :type IsolationNum: int
        :param _ExpiredNum: Number of expired instances
        :type ExpiredNum: int
        :param _WillExpireNum: Number of instances about to expire
        :type WillExpireNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ModuleNum = None
        self._NodeNum = None
        self._VcpuNum = None
        self._MemoryNum = None
        self._StorageNum = None
        self._NetworkNum = None
        self._InstanceNum = None
        self._RunningNum = None
        self._IsolationNum = None
        self._ExpiredNum = None
        self._WillExpireNum = None
        self._RequestId = None

    @property
    def ModuleNum(self):
        """Number of modules
        :rtype: int
        """
        return self._ModuleNum

    @ModuleNum.setter
    def ModuleNum(self, ModuleNum):
        self._ModuleNum = ModuleNum

    @property
    def NodeNum(self):
        """Number of nodes
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def VcpuNum(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._VcpuNum

    @VcpuNum.setter
    def VcpuNum(self, VcpuNum):
        self._VcpuNum = VcpuNum

    @property
    def MemoryNum(self):
        """Memory size in GB
        :rtype: int
        """
        return self._MemoryNum

    @MemoryNum.setter
    def MemoryNum(self, MemoryNum):
        self._MemoryNum = MemoryNum

    @property
    def StorageNum(self):
        """Disk size in GB
        :rtype: int
        """
        return self._StorageNum

    @StorageNum.setter
    def StorageNum(self, StorageNum):
        self._StorageNum = StorageNum

    @property
    def NetworkNum(self):
        """Yesterday's network peak in Mbps
        :rtype: int
        """
        return self._NetworkNum

    @NetworkNum.setter
    def NetworkNum(self, NetworkNum):
        self._NetworkNum = NetworkNum

    @property
    def InstanceNum(self):
        """Number of instances
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def RunningNum(self):
        """Number of running instances
        :rtype: int
        """
        return self._RunningNum

    @RunningNum.setter
    def RunningNum(self, RunningNum):
        self._RunningNum = RunningNum

    @property
    def IsolationNum(self):
        """Number of isolated instances
        :rtype: int
        """
        return self._IsolationNum

    @IsolationNum.setter
    def IsolationNum(self, IsolationNum):
        self._IsolationNum = IsolationNum

    @property
    def ExpiredNum(self):
        """Number of expired instances
        :rtype: int
        """
        return self._ExpiredNum

    @ExpiredNum.setter
    def ExpiredNum(self, ExpiredNum):
        self._ExpiredNum = ExpiredNum

    @property
    def WillExpireNum(self):
        """Number of instances about to expire
        :rtype: int
        """
        return self._WillExpireNum

    @WillExpireNum.setter
    def WillExpireNum(self, WillExpireNum):
        self._WillExpireNum = WillExpireNum

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModuleNum = params.get("ModuleNum")
        self._NodeNum = params.get("NodeNum")
        self._VcpuNum = params.get("VcpuNum")
        self._MemoryNum = params.get("MemoryNum")
        self._StorageNum = params.get("StorageNum")
        self._NetworkNum = params.get("NetworkNum")
        self._InstanceNum = params.get("InstanceNum")
        self._RunningNum = params.get("RunningNum")
        self._IsolationNum = params.get("IsolationNum")
        self._ExpiredNum = params.get("ExpiredNum")
        self._WillExpireNum = params.get("WillExpireNum")
        self._RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig request structure.

    """


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig response structure.

    """

    def __init__(self):
        r"""
        :param _NetworkStorageRange: Range of the network bandwidth disk size.
        :type NetworkStorageRange: :class:`tencentcloud.ecm.v20190719.models.NetworkStorageRange`
        :param _ImageWhiteSet: Image OS allowlist.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageWhiteSet: list of str
        :param _InstanceNetworkLimitConfigs: Network quota information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceNetworkLimitConfigs: list of InstanceNetworkLimitConfig
        :param _ImageLimits: Image quota information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageLimits: :class:`tencentcloud.ecm.v20190719.models.ImageLimitConfig`
        :param _DefaultIPDirect: Default IP direct access, used in scenarios with direct access parameters such as module creation and virtual machine purchase.
        :type DefaultIPDirect: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NetworkStorageRange = None
        self._ImageWhiteSet = None
        self._InstanceNetworkLimitConfigs = None
        self._ImageLimits = None
        self._DefaultIPDirect = None
        self._RequestId = None

    @property
    def NetworkStorageRange(self):
        """Range of the network bandwidth disk size.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.NetworkStorageRange`
        """
        return self._NetworkStorageRange

    @NetworkStorageRange.setter
    def NetworkStorageRange(self, NetworkStorageRange):
        self._NetworkStorageRange = NetworkStorageRange

    @property
    def ImageWhiteSet(self):
        """Image OS allowlist.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._ImageWhiteSet

    @ImageWhiteSet.setter
    def ImageWhiteSet(self, ImageWhiteSet):
        self._ImageWhiteSet = ImageWhiteSet

    @property
    def InstanceNetworkLimitConfigs(self):
        """Network quota information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceNetworkLimitConfig
        """
        return self._InstanceNetworkLimitConfigs

    @InstanceNetworkLimitConfigs.setter
    def InstanceNetworkLimitConfigs(self, InstanceNetworkLimitConfigs):
        self._InstanceNetworkLimitConfigs = InstanceNetworkLimitConfigs

    @property
    def ImageLimits(self):
        """Image quota information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ImageLimitConfig`
        """
        return self._ImageLimits

    @ImageLimits.setter
    def ImageLimits(self, ImageLimits):
        self._ImageLimits = ImageLimits

    @property
    def DefaultIPDirect(self):
        """Default IP direct access, used in scenarios with direct access parameters such as module creation and virtual machine purchase.
        :rtype: bool
        """
        return self._DefaultIPDirect

    @DefaultIPDirect.setter
    def DefaultIPDirect(self, DefaultIPDirect):
        self._DefaultIPDirect = DefaultIPDirect

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NetworkStorageRange") is not None:
            self._NetworkStorageRange = NetworkStorageRange()
            self._NetworkStorageRange._deserialize(params.get("NetworkStorageRange"))
        self._ImageWhiteSet = params.get("ImageWhiteSet")
        if params.get("InstanceNetworkLimitConfigs") is not None:
            self._InstanceNetworkLimitConfigs = []
            for item in params.get("InstanceNetworkLimitConfigs"):
                obj = InstanceNetworkLimitConfig()
                obj._deserialize(item)
                self._InstanceNetworkLimitConfigs.append(obj)
        if params.get("ImageLimits") is not None:
            self._ImageLimits = ImageLimitConfig()
            self._ImageLimits._deserialize(params.get("ImageLimits"))
        self._DefaultIPDirect = params.get("DefaultIPDirect")
        self._RequestId = params.get("RequestId")


class DescribeCustomImageTaskRequest(AbstractModel):
    """DescribeCustomImageTask request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Supports querying by key and value.
task-id: async task ID
image-id: image ID
image-name: image name
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """Supports querying by key and value.
task-id: async task ID
image-id: image ID
image-name: image name
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeCustomImageTaskResponse(AbstractModel):
    """DescribeCustomImageTask response structure.

    """

    def __init__(self):
        r"""
        :param _ImageTaskSet: Import task details
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageTaskSet: list of ImageTask
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImageTaskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ImageTaskSet(self):
        """Import task details
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of ImageTask
        """
        return self._ImageTaskSet

    @ImageTaskSet.setter
    def ImageTaskSet(self, ImageTaskSet):
        self._ImageTaskSet = ImageTaskSet

    @property
    def TotalCount(self):
        """Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageTaskSet") is not None:
            self._ImageTaskSet = []
            for item in params.get("ImageTaskSet"):
                obj = ImageTask()
                obj._deserialize(item)
                self._ImageTaskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDefaultSubnetRequest(AbstractModel):
    """DescribeDefaultSubnet request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _Zone: ECM AZ
        :type Zone: str
        """
        self._EcmRegion = None
        self._Zone = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Zone(self):
        """ECM AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultSubnetResponse(AbstractModel):
    """DescribeDefaultSubnet response structure.

    """

    def __init__(self):
        r"""
        :param _Subnet: Default subnet information. If there is no subnet, this parameter will be empty.
        :type Subnet: :class:`tencentcloud.ecm.v20190719.models.Subnet`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Subnet = None
        self._RequestId = None

    @property
    def Subnet(self):
        """Default subnet information. If there is no subnet, this parameter will be empty.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Subnet`
        """
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Subnet") is not None:
            self._Subnet = Subnet()
            self._Subnet._deserialize(params.get("Subnet"))
        self._RequestId = params.get("RequestId")


class DescribeHaVipsRequest(AbstractModel):
    """DescribeHaVips request structure.

    """

    def __init__(self):
        r"""
        :param _HaVipIds: Array of unique HAVIP IDs, such as `havip-9o233uri`.
        :type HaVipIds: list of str
        :param _Filters: Filter. `HaVipIds` and `Filters` cannot be specified at the same time.
havip-id - String - Unique HAVIP ID, such as `havip-9o233uri`.
havip-name - String - HAVIP name.
vpc-id - String - VPC ID of the HAVIP.
subnet-id - String - Subnet ID of the HAVIP.
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _EcmRegion: ECM region. If this parameter is left empty, it will indicate all regions.
        :type EcmRegion: str
        """
        self._HaVipIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._EcmRegion = None

    @property
    def HaVipIds(self):
        """Array of unique HAVIP IDs, such as `havip-9o233uri`.
        :rtype: list of str
        """
        return self._HaVipIds

    @HaVipIds.setter
    def HaVipIds(self, HaVipIds):
        self._HaVipIds = HaVipIds

    @property
    def Filters(self):
        """Filter. `HaVipIds` and `Filters` cannot be specified at the same time.
havip-id - String - Unique HAVIP ID, such as `havip-9o233uri`.
havip-name - String - HAVIP name.
vpc-id - String - VPC ID of the HAVIP.
subnet-id - String - Subnet ID of the HAVIP.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EcmRegion(self):
        """ECM region. If this parameter is left empty, it will indicate all regions.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._HaVipIds = params.get("HaVipIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHaVipsResponse(AbstractModel):
    """DescribeHaVips response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible objects.
        :type TotalCount: int
        :param _HaVipSet: Array of HAVIP objects.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HaVipSet: list of HaVip
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._HaVipSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible objects.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HaVipSet(self):
        """Array of HAVIP objects.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of HaVip
        """
        return self._HaVipSet

    @HaVipSet.setter
    def HaVipSet(self, HaVipSet):
        self._HaVipSet = HaVipSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("HaVipSet") is not None:
            self._HaVipSet = []
            for item in params.get("HaVipSet"):
                obj = HaVip()
                obj._deserialize(item)
                self._HaVipSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImageRequest(AbstractModel):
    """DescribeImage request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter. Each request can contain up to 10 `Filters`. The detailed filters are as follows:
image-id - String - Required: no - (Filter) Filter by image ID.
image-type - String - Required: no - (Filter) Filter by image type. Valid values:
PRIVATE_IMAGE: private image created by the current account 
PUBLIC_IMAGE: public image created by Tencent Cloud
instance-type -String - Required: no - (Filter) Filter supported images by model.
image-name - String - Required: no - (Filter) Fuzzy match by image name. You can provide only one value.
image-os - String - Required: no - (Filter) Fuzzy match by image system name. You can provide only one value.
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API overview.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API overview.
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """Filter. Each request can contain up to 10 `Filters`. The detailed filters are as follows:
image-id - String - Required: no - (Filter) Filter by image ID.
image-type - String - Required: no - (Filter) Filter by image type. Valid values:
PRIVATE_IMAGE: private image created by the current account 
PUBLIC_IMAGE: public image created by Tencent Cloud
instance-type -String - Required: no - (Filter) Filter supported images by model.
image-name - String - Required: no - (Filter) Fuzzy match by image name. You can provide only one value.
image-os - String - Required: no - (Filter) Fuzzy match by image system name. You can provide only one value.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API overview.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API overview.
        :rtype: int
        """
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
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageResponse(AbstractModel):
    """DescribeImage response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of images
        :type TotalCount: int
        :param _ImageSet: Image array
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageSet: list of Image
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ImageSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of images
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ImageSet(self):
        """Image array
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Image
        """
        return self._ImageSet

    @ImageSet.setter
    def ImageSet(self, ImageSet):
        self._ImageSet = ImageSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ImageSet") is not None:
            self._ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self._ImageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImportImageOsRequest(AbstractModel):
    """DescribeImportImageOs request structure.

    """


class DescribeImportImageOsResponse(AbstractModel):
    """DescribeImportImageOs response structure.

    """

    def __init__(self):
        r"""
        :param _ImportImageOsListSupported: Supported OS types of imported images.
        :type ImportImageOsListSupported: :class:`tencentcloud.ecm.v20190719.models.ImageOsList`
        :param _ImportImageOsVersionSet: Supported OS versions of imported images.
        :type ImportImageOsVersionSet: list of OsVersion
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImportImageOsListSupported = None
        self._ImportImageOsVersionSet = None
        self._RequestId = None

    @property
    def ImportImageOsListSupported(self):
        """Supported OS types of imported images.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ImageOsList`
        """
        return self._ImportImageOsListSupported

    @ImportImageOsListSupported.setter
    def ImportImageOsListSupported(self, ImportImageOsListSupported):
        self._ImportImageOsListSupported = ImportImageOsListSupported

    @property
    def ImportImageOsVersionSet(self):
        """Supported OS versions of imported images.
        :rtype: list of OsVersion
        """
        return self._ImportImageOsVersionSet

    @ImportImageOsVersionSet.setter
    def ImportImageOsVersionSet(self, ImportImageOsVersionSet):
        self._ImportImageOsVersionSet = ImportImageOsVersionSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImportImageOsListSupported") is not None:
            self._ImportImageOsListSupported = ImageOsList()
            self._ImportImageOsListSupported._deserialize(params.get("ImportImageOsListSupported"))
        if params.get("ImportImageOsVersionSet") is not None:
            self._ImportImageOsVersionSet = []
            for item in params.get("ImportImageOsVersionSet"):
                obj = OsVersion()
                obj._deserialize(item)
                self._ImportImageOsVersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceTypeConfigRequest(AbstractModel):
    """DescribeInstanceTypeConfig request structure.

    """


class DescribeInstanceTypeConfigResponse(AbstractModel):
    """DescribeInstanceTypeConfig response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _InstanceTypeConfigSet: Model configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceTypeConfigSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceTypeConfigSet(self):
        """Model configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceTypeConfig
        """
        return self._InstanceTypeConfigSet

    @InstanceTypeConfigSet.setter
    def InstanceTypeConfigSet(self, InstanceTypeConfigSet):
        self._InstanceTypeConfigSet = InstanceTypeConfigSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceTypeConfigSet") is not None:
            self._InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self._InstanceTypeConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceVncUrlRequest(AbstractModel):
    """DescribeInstanceVncUrl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which can be obtained from the `InstanceId` field in the returned value of the `DescribeInstances` API.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance ID, which can be obtained from the `InstanceId` field in the returned value of the `DescribeInstances` API.
        :rtype: str
        """
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
        


class DescribeInstanceVncUrlResponse(AbstractModel):
    """DescribeInstanceVncUrl response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceVncUrl: Instance VNC URL.
        :type InstanceVncUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceVncUrl = None
        self._RequestId = None

    @property
    def InstanceVncUrl(self):
        """Instance VNC URL.
        :rtype: str
        """
        return self._InstanceVncUrl

    @InstanceVncUrl.setter
    def InstanceVncUrl(self, InstanceVncUrl):
        self._InstanceVncUrl = InstanceVncUrl

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceVncUrl = params.get("InstanceVncUrl")
        self._RequestId = params.get("RequestId")


class DescribeInstancesDeniedActionsRequest(AbstractModel):
    """DescribeInstancesDeniedActions request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: None
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        """None
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDeniedActionsResponse(AbstractModel):
    """DescribeInstancesDeniedActions response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceOperatorSet: Prohibited operations for the instance
        :type InstanceOperatorSet: list of InstanceOperator
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceOperatorSet = None
        self._RequestId = None

    @property
    def InstanceOperatorSet(self):
        """Prohibited operations for the instance
        :rtype: list of InstanceOperator
        """
        return self._InstanceOperatorSet

    @InstanceOperatorSet.setter
    def InstanceOperatorSet(self, InstanceOperatorSet):
        self._InstanceOperatorSet = InstanceOperatorSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceOperatorSet") is not None:
            self._InstanceOperatorSet = []
            for item in params.get("InstanceOperatorSet"):
                obj = InstanceOperator()
                obj._deserialize(item)
                self._InstanceOperatorSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter.
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
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20 (if the number of query results is greater than or equal to 20). Maximum value: 100.
        :type Limit: int
        :param _OrderByField: Specified sort by field. Currently, valid values are as follows:
timestamp: sort by instance creation time.
Note: you can sort only by creation time currently. More sort criteria may be supported in the future.
If this parameter is not specified, instances will be sorted by creation time by default.
        :type OrderByField: str
        :param _OrderDirection: Sorting order. 0: descending; 1: ascending. If this parameter is not specified, it will be descending by default.
        :type OrderDirection: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderByField = None
        self._OrderDirection = None

    @property
    def Filters(self):
        """Filter.
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
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results. Default value: 20 (if the number of query results is greater than or equal to 20). Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByField(self):
        """Specified sort by field. Currently, valid values are as follows:
timestamp: sort by instance creation time.
Note: you can sort only by creation time currently. More sort criteria may be supported in the future.
If this parameter is not specified, instances will be sorted by creation time by default.
        :rtype: str
        """
        return self._OrderByField

    @OrderByField.setter
    def OrderByField(self, OrderByField):
        self._OrderByField = OrderByField

    @property
    def OrderDirection(self):
        """Sorting order. 0: descending; 1: ascending. If this parameter is not specified, it will be descending by default.
        :rtype: int
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByField = params.get("OrderByField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Length of the list of the returned instance information.
        :type TotalCount: int
        :param _InstanceSet: List of the returned instance information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceSet: list of Instance
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Length of the list of the returned instance information.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        """List of the returned instance information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Instance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerIds: Array of IDs of the CLB listeners to be queried
        :type ListenerIds: list of str
        :param _Protocol: Protocol type of the listener to be queried. Valid values: TCP, UDP.
        :type Protocol: str
        :param _Port: Port of the listener to be queried
        :type Port: int
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._Port = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        """Array of IDs of the CLB listeners to be queried
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Protocol(self):
        """Protocol type of the listener to be queried. Valid values: TCP, UDP.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """Port of the listener to be queried
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners response structure.

    """

    def __init__(self):
        r"""
        :param _Listeners: List of listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :type Listeners: list of Listener
        :param _TotalCount: Total number of listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Listeners = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Listeners(self):
        """List of listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Listener
        """
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def TotalCount(self):
        """Total number of listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
                obj = Listener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalanceTaskStatusRequest(AbstractModel):
    """DescribeLoadBalanceTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Request ID, i.e., the `RequestId` parameter returned by the API
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """Request ID, i.e., the `RequestId` parameter returned by the API
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalanceTaskStatusResponse(AbstractModel):
    """DescribeLoadBalanceTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Current task status. 0: succeeded; 1: failed; 2: in progress.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Current task status. 0: succeeded; 1: failed; 2: in progress.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: Region. If this parameter is not specified, the information of all regions will be queried by default.
        :type EcmRegion: str
        :param _LoadBalancerIds: CLB instance ID.
        :type LoadBalancerIds: list of str
        :param _LoadBalancerName: CLB instance name.
        :type LoadBalancerName: str
        :param _LoadBalancerVips: VIP address of the CLB instance. There can be multiple addresses.
        :type LoadBalancerVips: list of str
        :param _BackendPrivateIps: Private IP of the real server bound to the CLB.
        :type BackendPrivateIps: list of str
        :param _Offset: Data offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned CLB instances. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _WithBackend: Whether the CLB instance is bound to a real server. 0: no; 1: yes; -1: query all. 
If this parameter is not specified, all will be queried by default.
        :type WithBackend: int
        :param _VpcId: Unique VPC ID of the CLB instance, such as `vpc-bhqkbhdx`.
        :type VpcId: str
        :param _Filters: Each request can contain up to 10 `Filters` and 100 `Filter.Values`. The detailed filters are as follows:
tag-key - String - Required: no - (Filter) Filter by tag key.
        :type Filters: list of Filter
        :param _SecurityGroup: Security group.
        :type SecurityGroup: str
        """
        self._EcmRegion = None
        self._LoadBalancerIds = None
        self._LoadBalancerName = None
        self._LoadBalancerVips = None
        self._BackendPrivateIps = None
        self._Offset = None
        self._Limit = None
        self._WithBackend = None
        self._VpcId = None
        self._Filters = None
        self._SecurityGroup = None

    @property
    def EcmRegion(self):
        """Region. If this parameter is not specified, the information of all regions will be queried by default.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def LoadBalancerIds(self):
        """CLB instance ID.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def LoadBalancerName(self):
        """CLB instance name.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerVips(self):
        """VIP address of the CLB instance. There can be multiple addresses.
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def BackendPrivateIps(self):
        """Private IP of the real server bound to the CLB.
        :rtype: list of str
        """
        return self._BackendPrivateIps

    @BackendPrivateIps.setter
    def BackendPrivateIps(self, BackendPrivateIps):
        self._BackendPrivateIps = BackendPrivateIps

    @property
    def Offset(self):
        """Data offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned CLB instances. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def WithBackend(self):
        """Whether the CLB instance is bound to a real server. 0: no; 1: yes; -1: query all. 
If this parameter is not specified, all will be queried by default.
        :rtype: int
        """
        return self._WithBackend

    @WithBackend.setter
    def WithBackend(self, WithBackend):
        self._WithBackend = WithBackend

    @property
    def VpcId(self):
        """Unique VPC ID of the CLB instance, such as `vpc-bhqkbhdx`.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Filters(self):
        """Each request can contain up to 10 `Filters` and 100 `Filter.Values`. The detailed filters are as follows:
tag-key - String - Required: no - (Filter) Filter by tag key.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SecurityGroup(self):
        """Security group.
        :rtype: str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._BackendPrivateIps = params.get("BackendPrivateIps")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._WithBackend = params.get("WithBackend")
        self._VpcId = params.get("VpcId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SecurityGroup = params.get("SecurityGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of eligible CLB instances. This value is independent of the `Limit` in the input parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _LoadBalancerSet: Array of returned CLB instances.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerSet: list of LoadBalancer
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoadBalancerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of eligible CLB instances. This value is independent of the `Limit` in the input parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoadBalancerSet(self):
        """Array of returned CLB instances.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of LoadBalancer
        """
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class DescribeModuleDetailRequest(AbstractModel):
    """DescribeModuleDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ModuleId: Module ID, such as `em-qn46snq8`.
        :type ModuleId: str
        """
        self._ModuleId = None

    @property
    def ModuleId(self):
        """Module ID, such as `em-qn46snq8`.
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModuleDetailResponse(AbstractModel):
    """DescribeModuleDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module details. For more information, see `ModuleInfo` in the data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`
        :param _ModuleCounter: Module statistics. For more information, see `ModuleCounterInfo` in the data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModuleCounter: :class:`tencentcloud.ecm.v20190719.models.ModuleCounter`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Module = None
        self._ModuleCounter = None
        self._RequestId = None

    @property
    def Module(self):
        """Module details. For more information, see `ModuleInfo` in the data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Module`
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ModuleCounter(self):
        """Module statistics. For more information, see `ModuleCounterInfo` in the data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModuleCounter`
        """
        return self._ModuleCounter

    @ModuleCounter.setter
    def ModuleCounter(self, ModuleCounter):
        self._ModuleCounter = ModuleCounter

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Module") is not None:
            self._Module = Module()
            self._Module._deserialize(params.get("Module"))
        if params.get("ModuleCounter") is not None:
            self._ModuleCounter = ModuleCounter()
            self._ModuleCounter._deserialize(params.get("ModuleCounter"))
        self._RequestId = params.get("RequestId")


class DescribeModuleRequest(AbstractModel):
    """DescribeModule request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter.
module-name - string - Required: no - (Filter) Filter by module name.
module-id - string - Required: no - (Filter) Filter by module ID.
image-id      String      Required: no      (Filter) Filter by image ID.
instance-family      String      Required: no      (Filter) Filter by model family.
security-group-id - string Required: no - (Filter) Filter by ID of the security group bound to the module.
Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API overview.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API overview.
        :type Limit: int
        :param _OrderByField: Specified sort by field. Currently, valid values are as follows:
instance-num: sort by the number of instances.
node-num: sort by the number of nodes.
timestamp: sort by instance creation time.
If this parameter is not specified, instances will be sorted by creation time by default.
        :type OrderByField: str
        :param _OrderDirection: Sorting order. 0: descending; 1: ascending. If this parameter is not specified, it will be descending by default.
        :type OrderDirection: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderByField = None
        self._OrderDirection = None

    @property
    def Filters(self):
        """Filter.
module-name - string - Required: no - (Filter) Filter by module name.
module-id - string - Required: no - (Filter) Filter by module ID.
image-id      String      Required: no      (Filter) Filter by image ID.
instance-family      String      Required: no      (Filter) Filter by model family.
security-group-id - string Required: no - (Filter) Filter by ID of the security group bound to the module.
Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API overview.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API overview.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByField(self):
        """Specified sort by field. Currently, valid values are as follows:
instance-num: sort by the number of instances.
node-num: sort by the number of nodes.
timestamp: sort by instance creation time.
If this parameter is not specified, instances will be sorted by creation time by default.
        :rtype: str
        """
        return self._OrderByField

    @OrderByField.setter
    def OrderByField(self, OrderByField):
        self._OrderByField = OrderByField

    @property
    def OrderDirection(self):
        """Sorting order. 0: descending; 1: ascending. If this parameter is not specified, it will be descending by default.
        :rtype: int
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByField = params.get("OrderByField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModuleResponse(AbstractModel):
    """DescribeModule response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible modules.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ModuleItemSet: List of module details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModuleItemSet: list of ModuleItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ModuleItemSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible modules.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ModuleItemSet(self):
        """List of module details.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of ModuleItem
        """
        return self._ModuleItemSet

    @ModuleItemSet.setter
    def ModuleItemSet(self, ModuleItemSet):
        self._ModuleItemSet = ModuleItemSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ModuleItemSet") is not None:
            self._ModuleItemSet = []
            for item in params.get("ModuleItemSet"):
                obj = ModuleItem()
                obj._deserialize(item)
                self._ModuleItemSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMonthPeakNetworkRequest(AbstractModel):
    """DescribeMonthPeakNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _Month: Month (xxxx-xx), such as `2021-03`. Default value: the last month
        :type Month: str
        :param _Filters: Filter
        :type Filters: list of Filter
        """
        self._Month = None
        self._Filters = None

    @property
    def Month(self):
        """Month (xxxx-xx), such as `2021-03`. Default value: the last month
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def Filters(self):
        """Filter
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Month = params.get("Month")
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
        


class DescribeMonthPeakNetworkResponse(AbstractModel):
    """DescribeMonthPeakNetwork response structure.

    """

    def __init__(self):
        r"""
        :param _MonthNetWorkData: None
Note: this field may return null, indicating that no valid values can be obtained.
        :type MonthNetWorkData: list of MonthNetwork
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MonthNetWorkData = None
        self._RequestId = None

    @property
    def MonthNetWorkData(self):
        """None
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of MonthNetwork
        """
        return self._MonthNetWorkData

    @MonthNetWorkData.setter
    def MonthNetWorkData(self, MonthNetWorkData):
        self._MonthNetWorkData = MonthNetWorkData

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MonthNetWorkData") is not None:
            self._MonthNetWorkData = []
            for item in params.get("MonthNetWorkData"):
                obj = MonthNetwork()
                obj._deserialize(item)
                self._MonthNetWorkData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces request structure.

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceIds: Queries the ID of the ENI instance, such as `eni-pxir56ns`. Each request supports a maximum of 100 instances. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.
        :type NetworkInterfaceIds: list of str
        :param _Filters: Filter. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.
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
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        """
        self._NetworkInterfaceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._EcmRegion = None

    @property
    def NetworkInterfaceIds(self):
        """Queries the ID of the ENI instance, such as `eni-pxir56ns`. Each request supports a maximum of 100 instances. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._NetworkInterfaceIds

    @NetworkInterfaceIds.setter
    def NetworkInterfaceIds(self, NetworkInterfaceIds):
        self._NetworkInterfaceIds = NetworkInterfaceIds

    @property
    def Filters(self):
        """Filter. `NetworkInterfaceIds` and `Filters` cannot be specified at the same time.
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
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EcmRegion(self):
        """ECM region, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetworkInterfacesResponse(AbstractModel):
    """DescribeNetworkInterfaces response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _NetworkInterfaceSet: List of instance details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetworkInterfaceSet: list of NetworkInterface
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._NetworkInterfaceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible instances.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NetworkInterfaceSet(self):
        """List of instance details.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of NetworkInterface
        """
        return self._NetworkInterfaceSet

    @NetworkInterfaceSet.setter
    def NetworkInterfaceSet(self, NetworkInterfaceSet):
        self._NetworkInterfaceSet = NetworkInterfaceSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NetworkInterfaceSet") is not None:
            self._NetworkInterfaceSet = []
            for item in params.get("NetworkInterfaceSet"):
                obj = NetworkInterface()
                obj._deserialize(item)
                self._NetworkInterfaceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNodeRequest(AbstractModel):
    """DescribeNode request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter. InstanceFamily: instance family.
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """Filter. InstanceFamily: instance family.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeNodeResponse(AbstractModel):
    """DescribeNode response structure.

    """

    def __init__(self):
        r"""
        :param _NodeSet: List of node details
Note: this field may return null, indicating that no valid values can be obtained.
        :type NodeSet: list of Node
        :param _TotalCount: Total number of nodes.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NodeSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NodeSet(self):
        """List of node details
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Node
        """
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def TotalCount(self):
        """Total number of nodes.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = Node()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePackingQuotaGroupRequest(AbstractModel):
    """DescribePackingQuotaGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter. Zone: AZ; InstanceType: instance type; DataDiskSize: data disk size.
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """Filter. Zone: AZ; InstanceType: instance type; DataDiskSize: data disk size.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribePackingQuotaGroupResponse(AbstractModel):
    """DescribePackingQuotaGroup response structure.

    """

    def __init__(self):
        r"""
        :param _PackingQuotaSet: Set of packing quotas.
        :type PackingQuotaSet: list of PackingQuotaGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PackingQuotaSet = None
        self._RequestId = None

    @property
    def PackingQuotaSet(self):
        """Set of packing quotas.
        :rtype: list of PackingQuotaGroup
        """
        return self._PackingQuotaSet

    @PackingQuotaSet.setter
    def PackingQuotaSet(self, PackingQuotaSet):
        self._PackingQuotaSet = PackingQuotaSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PackingQuotaSet") is not None:
            self._PackingQuotaSet = []
            for item in params.get("PackingQuotaSet"):
                obj = PackingQuotaGroup()
                obj._deserialize(item)
                self._PackingQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePeakBaseOverviewRequest(AbstractModel):
    """DescribePeakBaseOverview request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time (xxxx-xx-xx), such as `2019-08-14`. It is 7 days ago by default and should not be more than 90 days ago.
        :type StartTime: str
        :param _EndTime: End time (xxxx-xx-xx), such as `2019-08-14`. It is yesterday by default and should not be more than 90 days ago. When the time period between the start time and end time is within 30 days, data at the 1-hour granularity will be returned; otherwise, data at the 3-hour granularity will be returned.
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        """Start time (xxxx-xx-xx), such as `2019-08-14`. It is 7 days ago by default and should not be more than 90 days ago.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time (xxxx-xx-xx), such as `2019-08-14`. It is yesterday by default and should not be more than 90 days ago. When the time period between the start time and end time is within 30 days, data at the 1-hour granularity will be returned; otherwise, data at the 3-hour granularity will be returned.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePeakBaseOverviewResponse(AbstractModel):
    """DescribePeakBaseOverview response structure.

    """

    def __init__(self):
        r"""
        :param _PeakFamilyInfoSet: List of basic peaks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeakFamilyInfoSet: list of PeakFamilyInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PeakFamilyInfoSet = None
        self._RequestId = None

    @property
    def PeakFamilyInfoSet(self):
        """List of basic peaks.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of PeakFamilyInfo
        """
        return self._PeakFamilyInfoSet

    @PeakFamilyInfoSet.setter
    def PeakFamilyInfoSet(self, PeakFamilyInfoSet):
        self._PeakFamilyInfoSet = PeakFamilyInfoSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PeakFamilyInfoSet") is not None:
            self._PeakFamilyInfoSet = []
            for item in params.get("PeakFamilyInfoSet"):
                obj = PeakFamilyInfo()
                obj._deserialize(item)
                self._PeakFamilyInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePeakNetworkOverviewRequest(AbstractModel):
    """DescribePeakNetworkOverview request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time (xxxx-xx-xx), such as `2019-08-14`. It is 7 days ago by default and should not be more than 30 days ago.
        :type StartTime: str
        :param _EndTime: End time (xxxx-xx-xx), such as `2019-08-14`. It is yesterday by default and should not be more than 30 days ago. When the time period between the start time and end time is within 1 day, data at the 1-minute granularity will be returned; when the time period is within 7 days, data at the 5-minute granularity will be returned; otherwise, data at the 1-hour granularity will be returned.
        :type EndTime: str
        :param _Filters: Filter.

region    String      Required: no     (Filter) Filter by region. Fuzzy match is not supported. Note: you need to enter the ECM region to be queried before data can be returned.
area       String      Required: no     (Filter) Filter by region. Fuzzy match is not supported. Regions include `china-central`, `china-east`, etc. You can call `DescribeNode` to get the information of all regions. You can also use `ALL_REGION` to indicate all regions.
isp         String      Required: no     (Filter) Filter region traffic by ISP. ISPs include CTCC, CUCC, and CMCC. This parameter must be used together with `area`, and you can specify only one ISP at a time.

You can specify either `region` or `area`.
        :type Filters: list of Filter
        :param _Period: Statistical period in seconds. Valid values: 60, 300.
        :type Period: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._Period = None

    @property
    def StartTime(self):
        """Start time (xxxx-xx-xx), such as `2019-08-14`. It is 7 days ago by default and should not be more than 30 days ago.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time (xxxx-xx-xx), such as `2019-08-14`. It is yesterday by default and should not be more than 30 days ago. When the time period between the start time and end time is within 1 day, data at the 1-minute granularity will be returned; when the time period is within 7 days, data at the 5-minute granularity will be returned; otherwise, data at the 1-hour granularity will be returned.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        """Filter.

region    String      Required: no     (Filter) Filter by region. Fuzzy match is not supported. Note: you need to enter the ECM region to be queried before data can be returned.
area       String      Required: no     (Filter) Filter by region. Fuzzy match is not supported. Regions include `china-central`, `china-east`, etc. You can call `DescribeNode` to get the information of all regions. You can also use `ALL_REGION` to indicate all regions.
isp         String      Required: no     (Filter) Filter region traffic by ISP. ISPs include CTCC, CUCC, and CMCC. This parameter must be used together with `area`, and you can specify only one ISP at a time.

You can specify either `region` or `area`.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Period(self):
        """Statistical period in seconds. Valid values: 60, 300.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePeakNetworkOverviewResponse(AbstractModel):
    """DescribePeakNetworkOverview response structure.

    """

    def __init__(self):
        r"""
        :param _PeakNetworkRegionSet: Array of network peaks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeakNetworkRegionSet: list of PeakNetworkRegionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PeakNetworkRegionSet = None
        self._RequestId = None

    @property
    def PeakNetworkRegionSet(self):
        """Array of network peaks.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of PeakNetworkRegionInfo
        """
        return self._PeakNetworkRegionSet

    @PeakNetworkRegionSet.setter
    def PeakNetworkRegionSet(self, PeakNetworkRegionSet):
        self._PeakNetworkRegionSet = PeakNetworkRegionSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PeakNetworkRegionSet") is not None:
            self._PeakNetworkRegionSet = []
            for item in params.get("PeakNetworkRegionSet"):
                obj = PeakNetworkRegionInfo()
                obj._deserialize(item)
                self._PeakNetworkRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePriceRunInstanceRequest(AbstractModel):
    """DescribePriceRunInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceType: Instance model information
        :type InstanceType: str
        :param _SystemDisk: System disk information
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param _InstanceCount: Number of instances
        :type InstanceCount: int
        :param _DataDisk: Data disk information
        :type DataDisk: list of DataDisk
        :param _InstanceChargeType: Instance billing type. Valid values:
`0`: Bill by daily resource usage peak (CPU, memory, and disk). It applies only to non-GNR models;
`1`: Bill by usage hours of an instance. It applies only to GNR models. It’s available to beta users now. To enable it, submit a ticket;
`2`: Bill by usage month of an instance. It applies only to GNR models.
If this field is left empty, `0` is selected by default for non-GNR models, and `2` is selected by default for GNR models.
        :type InstanceChargeType: int
        """
        self._InstanceType = None
        self._SystemDisk = None
        self._InstanceCount = None
        self._DataDisk = None
        self._InstanceChargeType = None

    @property
    def InstanceType(self):
        """Instance model information
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        """System disk information
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def InstanceCount(self):
        """Number of instances
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def DataDisk(self):
        """Data disk information
        :rtype: list of DataDisk
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def InstanceChargeType(self):
        """Instance billing type. Valid values:
`0`: Bill by daily resource usage peak (CPU, memory, and disk). It applies only to non-GNR models;
`1`: Bill by usage hours of an instance. It applies only to GNR models. It’s available to beta users now. To enable it, submit a ticket;
`2`: Bill by usage month of an instance. It applies only to GNR models.
If this field is left empty, `0` is selected by default for non-GNR models, and `2` is selected by default for GNR models.
        :rtype: int
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._InstanceCount = params.get("InstanceCount")
        if params.get("DataDisk") is not None:
            self._DataDisk = []
            for item in params.get("DataDisk"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisk.append(obj)
        self._InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePriceRunInstanceResponse(AbstractModel):
    """DescribePriceRunInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstancePrice: Instance price information
        :type InstancePrice: :class:`tencentcloud.ecm.v20190719.models.InstancesPrice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstancePrice = None
        self._RequestId = None

    @property
    def InstancePrice(self):
        """Instance price information
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstancesPrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = InstancesPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        self._RequestId = params.get("RequestId")


class DescribeRouteConflictsRequest(AbstractModel):
    """DescribeRouteConflicts request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableId: Route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        :param _DestinationCidrBlocks: List of conflicting destination ports to be checked.
        :type DestinationCidrBlocks: list of str
        """
        self._RouteTableId = None
        self._DestinationCidrBlocks = None

    @property
    def RouteTableId(self):
        """Route table instance ID, such as `rtb-azd4dt1c`.
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def DestinationCidrBlocks(self):
        """List of conflicting destination ports to be checked.
        :rtype: list of str
        """
        return self._DestinationCidrBlocks

    @DestinationCidrBlocks.setter
    def DestinationCidrBlocks(self, DestinationCidrBlocks):
        self._DestinationCidrBlocks = DestinationCidrBlocks


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._DestinationCidrBlocks = params.get("DestinationCidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteConflictsResponse(AbstractModel):
    """DescribeRouteConflicts response structure.

    """

    def __init__(self):
        r"""
        :param _RouteConflictSet: List of routing policy conflicts.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RouteConflictSet: list of RouteConflict
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RouteConflictSet = None
        self._RequestId = None

    @property
    def RouteConflictSet(self):
        """List of routing policy conflicts.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of RouteConflict
        """
        return self._RouteConflictSet

    @RouteConflictSet.setter
    def RouteConflictSet(self, RouteConflictSet):
        self._RouteConflictSet = RouteConflictSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RouteConflictSet") is not None:
            self._RouteConflictSet = []
            for item in params.get("RouteConflictSet"):
                obj = RouteConflict()
                obj._deserialize(item)
                self._RouteConflictSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRouteTablesRequest(AbstractModel):
    """DescribeRouteTables request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableIds: Route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableIds: list of str
        :param _Filters: Filter. `RouteTableIds` and `Filters` cannot be specified at the same time.
route-table-id - String - (Filter) Route table instance ID.
route-table-name - String - (Filter) Route table name.
vpc-id - String - (Filter) VPC instance ID, such as `vpc-f49l6u0z`.
association.main - String - (Filter) Whether it is the main route table.
        :type Filters: list of Filter
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Limit
        :type Limit: int
        :param _EcmRegion: ECM region. If this parameter is left empty or not specified, it will indicate all regions.
        :type EcmRegion: str
        """
        self._RouteTableIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._EcmRegion = None

    @property
    def RouteTableIds(self):
        """Route table instance ID, such as `rtb-azd4dt1c`.
        :rtype: list of str
        """
        return self._RouteTableIds

    @RouteTableIds.setter
    def RouteTableIds(self, RouteTableIds):
        self._RouteTableIds = RouteTableIds

    @property
    def Filters(self):
        """Filter. `RouteTableIds` and `Filters` cannot be specified at the same time.
route-table-id - String - (Filter) Route table instance ID.
route-table-name - String - (Filter) Route table name.
vpc-id - String - (Filter) VPC instance ID, such as `vpc-f49l6u0z`.
association.main - String - (Filter) Whether it is the main route table.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EcmRegion(self):
        """ECM region. If this parameter is left empty or not specified, it will indicate all regions.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._RouteTableIds = params.get("RouteTableIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteTablesResponse(AbstractModel):
    """DescribeRouteTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances
        :type TotalCount: int
        :param _RouteTableSet: List of route tables
Note: this field may return null, indicating that no valid values can be obtained.
        :type RouteTableSet: list of RouteTable
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RouteTableSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RouteTableSet(self):
        """List of route tables
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of RouteTable
        """
        return self._RouteTableSet

    @RouteTableSet.setter
    def RouteTableSet(self, RouteTableSet):
        self._RouteTableSet = RouteTableSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self._RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTable()
                obj._deserialize(item)
                self._RouteTableSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupAssociationStatisticsRequest(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: Security instance ID, such as `esg-33ocnj9n`, which can be obtained through [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/1108/47697?from_cn_redirect=1).
        :type SecurityGroupIds: list of str
        """
        self._SecurityGroupIds = None

    @property
    def SecurityGroupIds(self):
        """Security instance ID, such as `esg-33ocnj9n`, which can be obtained through [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/1108/47697?from_cn_redirect=1).
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupAssociationStatisticsResponse(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupAssociationStatisticsSet: Statistics on the instances associated with the security group.
        :type SecurityGroupAssociationStatisticsSet: list of SecurityGroupAssociationStatistics
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityGroupAssociationStatisticsSet = None
        self._RequestId = None

    @property
    def SecurityGroupAssociationStatisticsSet(self):
        """Statistics on the instances associated with the security group.
        :rtype: list of SecurityGroupAssociationStatistics
        """
        return self._SecurityGroupAssociationStatisticsSet

    @SecurityGroupAssociationStatisticsSet.setter
    def SecurityGroupAssociationStatisticsSet(self, SecurityGroupAssociationStatisticsSet):
        self._SecurityGroupAssociationStatisticsSet = SecurityGroupAssociationStatisticsSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityGroupAssociationStatisticsSet") is not None:
            self._SecurityGroupAssociationStatisticsSet = []
            for item in params.get("SecurityGroupAssociationStatisticsSet"):
                obj = SecurityGroupAssociationStatistics()
                obj._deserialize(item)
                self._SecurityGroupAssociationStatisticsSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupLimitsRequest(AbstractModel):
    """DescribeSecurityGroupLimits request structure.

    """


class DescribeSecurityGroupLimitsResponse(AbstractModel):
    """DescribeSecurityGroupLimits response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupLimitSet: Security group quota limit.
        :type SecurityGroupLimitSet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupLimitSet`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityGroupLimitSet = None
        self._RequestId = None

    @property
    def SecurityGroupLimitSet(self):
        """Security group quota limit.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupLimitSet`
        """
        return self._SecurityGroupLimitSet

    @SecurityGroupLimitSet.setter
    def SecurityGroupLimitSet(self, SecurityGroupLimitSet):
        self._SecurityGroupLimitSet = SecurityGroupLimitSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityGroupLimitSet") is not None:
            self._SecurityGroupLimitSet = SecurityGroupLimitSet()
            self._SecurityGroupLimitSet._deserialize(params.get("SecurityGroupLimitSet"))
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupPoliciesRequest(AbstractModel):
    """DescribeSecurityGroupPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/1108/47697?from_cn_redirect=1).
        :type SecurityGroupId: str
        """
        self._SecurityGroupId = None

    @property
    def SecurityGroupId(self):
        """Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/1108/47697?from_cn_redirect=1).
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupPoliciesResponse(AbstractModel):
    """DescribeSecurityGroupPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupPolicySet: Security group policy set.
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityGroupPolicySet = None
        self._RequestId = None

    @property
    def SecurityGroupPolicySet(self):
        """Security group policy set.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = SecurityGroupPolicySet()
            self._SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupsRequest(AbstractModel):
    """DescribeSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/1108/47697?from_cn_redirect=1). Each request supports a maximum of 100 instances. `SecurityGroupIds` and `Filters` cannot be specified at the same time.
        :type SecurityGroupIds: list of str
        :param _Filters: Filter. `SecurityGroupIds` and `Filters` cannot be specified at the same time.
security-group-id - String - (Filter) Security group ID.
security-group-name - String - (Filter) Security group name.
tag-key - String - Required: no - (Filter) Filter by tag key.
tag:tag-key - String - Required: no - (Filter) Filter by tag key-value pair. Replace `tag-key` with the specific tag key.
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._SecurityGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def SecurityGroupIds(self):
        """Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/1108/47697?from_cn_redirect=1). Each request supports a maximum of 100 instances. `SecurityGroupIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Filters(self):
        """Filter. `SecurityGroupIds` and `Filters` cannot be specified at the same time.
security-group-id - String - (Filter) Security group ID.
security-group-name - String - (Filter) Security group name.
tag-key - String - Required: no - (Filter) Filter by tag key.
tag:tag-key - String - Required: no - (Filter) Filter by tag key-value pair. Replace `tag-key` with the specific tag key.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupsResponse(AbstractModel):
    """DescribeSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _SecurityGroupSet: Security group object.
        :type SecurityGroupSet: list of SecurityGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SecurityGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible instances.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SecurityGroupSet(self):
        """Security group object.
        :rtype: list of SecurityGroup
        """
        return self._SecurityGroupSet

    @SecurityGroupSet.setter
    def SecurityGroupSet(self, SecurityGroupSet):
        self._SecurityGroupSet = SecurityGroupSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SecurityGroupSet") is not None:
            self._SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._SecurityGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: List of IDs of the snapshots to be queried. `SnapshotIds` and `Filters` cannot be specified at the same time.
        :type SnapshotIds: list of str
        :param _Filters: Filter. `SnapshotIds` and `Filters` cannot be specified at the same time.<br><li>snapshot-id - Array of String - Required: no - (Filter) Filter by snapshot ID, such as `snap-11112222`.<br><li>snapshot-name - Array of String - Required: no - (Filter) Filter by snapshot name.<br><li>snapshot-state - Array of String - Required: no - (Filter) Filter by snapshot status. NORMAL: normal; CREATING: creating; ROLLBACKING: rolling back.<br><li>disk-usage - Array of String - Required: no - (Filter) Filter by the type of the cloud disk from which a snapshot is created. SYSTEM_DISK: system disk; DATA_DISK: data disk.<br><li>project-id  - Array of String - Required: no - (Filter) Filter by the project ID of the cloud disk.<br><li>disk-id  - Array of String - Required: no - (Filter) Filter by the ID of the cloud disk from which a snapshot is created.<br><li>zone - Array of String - Required: no - (Filter) Filter by [AZ](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo).<br><li>encrypt - Array of String - Required: no - (Filter) Filter by whether a snapshot is created from an encrypted cloud disk. TRUE: yes; FALSE: no.
<li>snapshot-type- Array of String - Required: no - (Filter) Filter by the snapshot type specified in `snapshot-type`.
(SHARED_SNAPSHOT: shared snapshot | PRIVATE_SNAPSHOT: private snapshot.)
        :type Filters: list of Filter
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param _OrderField: Field by which snapshots are sorted. Valid values:<br><li>CREATE_TIME: sort by snapshot creation time<br>Snapshots are sorted by creation time by default.
        :type OrderField: str
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param _Order: Sorting order of cloud disks. Valid values:<br><li>ASC: ascending<br><li>DESC: descending.
        :type Order: str
        """
        self._SnapshotIds = None
        self._Filters = None
        self._Limit = None
        self._OrderField = None
        self._Offset = None
        self._Order = None

    @property
    def SnapshotIds(self):
        """List of IDs of the snapshots to be queried. `SnapshotIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def Filters(self):
        """Filter. `SnapshotIds` and `Filters` cannot be specified at the same time.<br><li>snapshot-id - Array of String - Required: no - (Filter) Filter by snapshot ID, such as `snap-11112222`.<br><li>snapshot-name - Array of String - Required: no - (Filter) Filter by snapshot name.<br><li>snapshot-state - Array of String - Required: no - (Filter) Filter by snapshot status. NORMAL: normal; CREATING: creating; ROLLBACKING: rolling back.<br><li>disk-usage - Array of String - Required: no - (Filter) Filter by the type of the cloud disk from which a snapshot is created. SYSTEM_DISK: system disk; DATA_DISK: data disk.<br><li>project-id  - Array of String - Required: no - (Filter) Filter by the project ID of the cloud disk.<br><li>disk-id  - Array of String - Required: no - (Filter) Filter by the ID of the cloud disk from which a snapshot is created.<br><li>zone - Array of String - Required: no - (Filter) Filter by [AZ](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo).<br><li>encrypt - Array of String - Required: no - (Filter) Filter by whether a snapshot is created from an encrypted cloud disk. TRUE: yes; FALSE: no.
<li>snapshot-type- Array of String - Required: no - (Filter) Filter by the snapshot type specified in `snapshot-type`.
(SHARED_SNAPSHOT: shared snapshot | PRIVATE_SNAPSHOT: private snapshot.)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        """Field by which snapshots are sorted. Valid values:<br><li>CREATE_TIME: sort by snapshot creation time<br>Snapshots are sorted by creation time by default.
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Offset(self):
        """Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        """Sorting order of cloud disks. Valid values:<br><li>ASC: ascending<br><li>DESC: descending.
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of snapshots.
        :type TotalCount: int
        :param _SnapshotSet: List of snapshot details.
        :type SnapshotSet: list of Snapshot
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SnapshotSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of snapshots.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SnapshotSet(self):
        """List of snapshot details.
        :rtype: list of Snapshot
        """
        return self._SnapshotSet

    @SnapshotSet.setter
    def SnapshotSet(self, SnapshotSet):
        self._SnapshotSet = SnapshotSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SnapshotSet") is not None:
            self._SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self._SnapshotSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets request structure.

    """

    def __init__(self):
        r"""
        :param _SubnetIds: Subnet instance ID, such as `subnet-pxir56ns`. Each request supports a maximum of 100 instances. `SubnetIds` and `Filters` cannot be specified at the same time.
        :type SubnetIds: list of str
        :param _Filters: Filter. `SubnetIds` and `Filters` cannot be specified at the same time.
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
        :param _Offset: Offset
        :type Offset: str
        :param _Limit: Number of returned results.
        :type Limit: str
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _Sort: Sorting method. time: sort in reverse chronological order; default: sort by network planning.
        :type Sort: str
        """
        self._SubnetIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._EcmRegion = None
        self._Sort = None

    @property
    def SubnetIds(self):
        """Subnet instance ID, such as `subnet-pxir56ns`. Each request supports a maximum of 100 instances. `SubnetIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def Filters(self):
        """Filter. `SubnetIds` and `Filters` cannot be specified at the same time.
subnet-id - String - Subnet instance name.
subnet-name - String - Subnet name. Only fuzzy query by a single value is supported.
cidr-block - String - Subnet IP address range, such as `192.168.1.0`. Only fuzzy query by a single value is supported.
vpc-id - String - VPC instance ID, such as `vpc-f49l6u0z`.
vpc-cidr-block  - String - VPC IP address range, such as `192.168.1.0`. Only fuzzy query by a single value is supported.
region - String - ECM region.
zone - String - AZ.
tag-key - String - Required: no - Filter by tag key.
tag:tag-key - String - Required: no - Filter by tag key-value pair.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results.
        :rtype: str
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Sort(self):
        """Sorting method. time: sort in reverse chronological order; default: sort by network planning.
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._SubnetIds = params.get("SubnetIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EcmRegion = params.get("EcmRegion")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetsResponse(AbstractModel):
    """DescribeSubnets response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _SubnetSet: Subnet object.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubnetSet: list of Subnet
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SubnetSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible instances.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SubnetSet(self):
        """Subnet object.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Subnet
        """
        return self._SubnetSet

    @SubnetSet.setter
    def SubnetSet(self, SubnetSet):
        self._SubnetSet = SubnetSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SubnetSet") is not None:
            self._SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self._SubnetSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: List of IDs of CLB instances to be queried.
        :type LoadBalancerIds: list of str
        """
        self._LoadBalancerIds = None

    @property
    def LoadBalancerIds(self):
        """List of IDs of CLB instances to be queried.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancers: List of CLB instances.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancers: list of LoadBalancerHealth
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancers = None
        self._RequestId = None

    @property
    def LoadBalancers(self):
        """List of CLB instances.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of LoadBalancerHealth
        """
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerIds: List of listener IDs.
        :type ListenerIds: list of str
        :param _Protocol: Listener protocol type.
        :type Protocol: int
        :param _Port: Listener port.
        :type Port: int
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._Port = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        """List of listener IDs.
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Protocol(self):
        """Listener protocol type.
        :rtype: int
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """Listener port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets response structure.

    """

    def __init__(self):
        r"""
        :param _Listeners: Information of real servers bound to the listener.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Listeners: list of ListenerBackend
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Listeners = None
        self._RequestId = None

    @property
    def Listeners(self):
        """Information of real servers bound to the listener.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of ListenerBackend
        """
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
                obj = ListenerBackend()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _TaskId: Async task ID.
        :type TaskId: str
        """
        self._EcmRegion = None
        self._TaskId = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def TaskId(self):
        """Async task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID.
        :type TaskId: str
        :param _Result: Execution result. Valid values: SUCCESS; FAILED; RUNNING.
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._Result = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Async task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Result(self):
        """Execution result. Valid values: SUCCESS; FAILED; RUNNING.
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _TaskSet: Task description.
        :type TaskSet: list of TaskInput
        """
        self._TaskSet = None

    @property
    def TaskSet(self):
        """Task description.
        :rtype: list of TaskInput
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskInput()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param _TaskSet: Task description.
        :type TaskSet: list of TaskOutput
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        """Task description.
        :rtype: list of TaskOutput
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskOutput()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs request structure.

    """

    def __init__(self):
        r"""
        :param _VpcIds: VPC instance ID, such as `vpc-f49l6u0z`. Each request supports a maximum of 100 instances. `VpcIds` and `Filters` cannot be specified at the same time.
        :type VpcIds: list of str
        :param _Filters: Filter. `VpcIds` and `Filters` cannot be specified at the same time.
vpc-name - String - VPC instance name. Only fuzzy query by a single value is supported.
vpc-id - String - VPC instance ID, such as `vpc-f49l6u0z`.
cidr-block - String - VPC CIDR. Only fuzzy query by a single value is supported.
region - String - VPC region.
tag-key - String - Required: no - Filter by tag key.
tag:tag-key - String - Required: no - Filter by tag key-value pair.
        :type Filters: list of Filter
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Number of returned results.
        :type Limit: int
        :param _EcmRegion: Region
        :type EcmRegion: str
        :param _Sort: Sorting method. time: sort in reverse chronological order; default: sort by network planning.
        :type Sort: str
        """
        self._VpcIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._EcmRegion = None
        self._Sort = None

    @property
    def VpcIds(self):
        """VPC instance ID, such as `vpc-f49l6u0z`. Each request supports a maximum of 100 instances. `VpcIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def Filters(self):
        """Filter. `VpcIds` and `Filters` cannot be specified at the same time.
vpc-name - String - VPC instance name. Only fuzzy query by a single value is supported.
vpc-id - String - VPC instance ID, such as `vpc-f49l6u0z`.
cidr-block - String - VPC CIDR. Only fuzzy query by a single value is supported.
region - String - VPC region.
tag-key - String - Required: no - Filter by tag key.
tag:tag-key - String - Required: no - Filter by tag key-value pair.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EcmRegion(self):
        """Region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Sort(self):
        """Sorting method. time: sort in reverse chronological order; default: sort by network planning.
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._VpcIds = params.get("VpcIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EcmRegion = params.get("EcmRegion")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcsResponse(AbstractModel):
    """DescribeVpcs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible objects.
        :type TotalCount: int
        :param _VpcSet: VPC object.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcSet: list of VpcInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible objects.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcSet(self):
        """VPC object.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._RequestId = params.get("RequestId")


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface request structure.

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param _InstanceId: Instance ID, such as `ein-hcs7jkg4`.
        :type InstanceId: str
        :param _EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        """
        self._NetworkInterfaceId = None
        self._InstanceId = None
        self._EcmRegion = None

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-m6dyj72l`.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def InstanceId(self):
        """Instance ID, such as `ein-hcs7jkg4`.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EcmRegion(self):
        """ECM region, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._InstanceId = params.get("InstanceId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachNetworkInterfaceResponse(AbstractModel):
    """DetachNetworkInterface response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisableRoutesRequest(AbstractModel):
    """DisableRoutes request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableId: Unique route table ID.
        :type RouteTableId: str
        :param _RouteIds: Routing policy ID.
        :type RouteIds: list of int non-negative
        """
        self._RouteTableId = None
        self._RouteIds = None

    @property
    def RouteTableId(self):
        """Unique route table ID.
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteIds(self):
        """Routing policy ID.
        :rtype: list of int non-negative
        """
        return self._RouteIds

    @RouteIds.setter
    def RouteIds(self, RouteIds):
        self._RouteIds = RouteIds


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRoutesResponse(AbstractModel):
    """DisableRoutes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisassociateAddressRequest(AbstractModel):
    """DisassociateAddress request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _AddressId: Unique EIP ID, such as `eip-11112222`.
        :type AddressId: str
        :param _ReallocateNormalPublicIp: Indicates whether to assign a general public IP after unbinding an EIP. Valid values:
TRUE: yes
FALSE: no.
Default value: FALSE.

You can specify this parameter only under the following conditions:
You can specify this parameter only when you unbind an EIP from the primary private IP of the primary ENI.
An account can reassign a general public IP after unbinding an EIP 10 times a day. More information can be obtained through the `DescribeAddressQuota` API.
        :type ReallocateNormalPublicIp: bool
        """
        self._EcmRegion = None
        self._AddressId = None
        self._ReallocateNormalPublicIp = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressId(self):
        """Unique EIP ID, such as `eip-11112222`.
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def ReallocateNormalPublicIp(self):
        """Indicates whether to assign a general public IP after unbinding an EIP. Valid values:
TRUE: yes
FALSE: no.
Default value: FALSE.

You can specify this parameter only under the following conditions:
You can specify this parameter only when you unbind an EIP from the primary private IP of the primary ENI.
An account can reassign a general public IP after unbinding an EIP 10 times a day. More information can be obtained through the `DescribeAddressQuota` API.
        :rtype: bool
        """
        return self._ReallocateNormalPublicIp

    @ReallocateNormalPublicIp.setter
    def ReallocateNormalPublicIp(self, ReallocateNormalPublicIp):
        self._ReallocateNormalPublicIp = ReallocateNormalPublicIp


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressId = params.get("AddressId")
        self._ReallocateNormalPublicIp = params.get("ReallocateNormalPublicIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateAddressResponse(AbstractModel):
    """DisassociateAddress response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: You can get available instance IDs in the following ways:
Log in to the console to query instance IDs.
Get the instance IDs from the `InstanceId` field in the information returned by the `DescribeInstances` API.
        :type InstanceIds: list of str
        :param _KeyIds: List of key pair IDs. Each request can contain up to 100 key pairs. The key pair ID takes the form of `skey-11112222`.

You can get available key IDs in the following ways:
Log in to the console to query key IDs.
Get the key pair IDs from the `KeyId` field in the information returned by the `DescribeKeyPairs` API.
        :type KeyIds: list of str
        :param _ForceStop: Whether to force shut down the running instance. We recommend you manually shut down the running instance before unbinding the key. Valid values:
TRUE: yes.
FALSE: no.

Default value: FALSE.
        :type ForceStop: bool
        """
        self._InstanceIds = None
        self._KeyIds = None
        self._ForceStop = None

    @property
    def InstanceIds(self):
        """You can get available instance IDs in the following ways:
Log in to the console to query instance IDs.
Get the instance IDs from the `InstanceId` field in the information returned by the `DescribeInstances` API.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def KeyIds(self):
        """List of key pair IDs. Each request can contain up to 100 key pairs. The key pair ID takes the form of `skey-11112222`.

You can get available key IDs in the following ways:
Log in to the console to query key IDs.
Get the key pair IDs from the `KeyId` field in the information returned by the `DescribeKeyPairs` API.
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def ForceStop(self):
        """Whether to force shut down the running instance. We recommend you manually shut down the running instance before unbinding the key. Valid values:
TRUE: yes.
FALSE: no.

Default value: FALSE.
        :rtype: bool
        """
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._KeyIds = params.get("KeyIds")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    """DisassociateInstancesKeyPairs response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: ID of the security group to be unbound, such as `esg-efil73jd`. You can unbind only one security group at a time.
        :type SecurityGroupIds: list of str
        :param _InstanceIds: ID of the instance to be unbound, such as `ein-lesecurk`. You can specify multiple instances.
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        """ID of the security group to be unbound, such as `esg-efil73jd`. You can unbind only one security group at a time.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        """ID of the instance to be unbound, such as `ein-lesecurk`. You can specify multiple instances.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DiskInfo(AbstractModel):
    """Disk information

    """

    def __init__(self):
        r"""
        :param _DiskType: Disk type: LOCAL_BASIC.
        :type DiskType: str
        :param _DiskId: Disk ID
        :type DiskId: str
        :param _DiskSize: Disk size in GB
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskId = None
        self._DiskSize = None

    @property
    def DiskType(self):
        """Disk type: LOCAL_BASIC.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        """Disk ID
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        """Disk size in GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipQuota(AbstractModel):
    """EIP quota information

    """

    def __init__(self):
        r"""
        :param _QuotaId: Quota name. Valid values:
TOTAL_EIP_QUOTA: quota of EIPs in the current region;
DAILY_EIP_APPLY: today's number of applications in the current region;
DAILY_PUBLIC_IP_ASSIGN: number of public IP reassignments in the current region.
        :type QuotaId: str
        :param _QuotaCurrent: Current quantity
        :type QuotaCurrent: int
        :param _QuotaLimit: Quota
        :type QuotaLimit: int
        """
        self._QuotaId = None
        self._QuotaCurrent = None
        self._QuotaLimit = None

    @property
    def QuotaId(self):
        """Quota name. Valid values:
TOTAL_EIP_QUOTA: quota of EIPs in the current region;
DAILY_EIP_APPLY: today's number of applications in the current region;
DAILY_PUBLIC_IP_ASSIGN: number of public IP reassignments in the current region.
        :rtype: str
        """
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def QuotaCurrent(self):
        """Current quantity
        :rtype: int
        """
        return self._QuotaCurrent

    @QuotaCurrent.setter
    def QuotaCurrent(self, QuotaCurrent):
        self._QuotaCurrent = QuotaCurrent

    @property
    def QuotaLimit(self):
        """Quota
        :rtype: int
        """
        return self._QuotaLimit

    @QuotaLimit.setter
    def QuotaLimit(self, QuotaLimit):
        self._QuotaLimit = QuotaLimit


    def _deserialize(self, params):
        self._QuotaId = params.get("QuotaId")
        self._QuotaCurrent = params.get("QuotaCurrent")
        self._QuotaLimit = params.get("QuotaLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRoutesRequest(AbstractModel):
    """EnableRoutes request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableId: Unique route table ID.
        :type RouteTableId: str
        :param _RouteIds: Routing policy ID.
        :type RouteIds: list of int non-negative
        """
        self._RouteTableId = None
        self._RouteIds = None

    @property
    def RouteTableId(self):
        """Unique route table ID.
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteIds(self):
        """Routing policy ID.
        :rtype: list of int non-negative
        """
        return self._RouteIds

    @RouteIds.setter
    def RouteIds(self, RouteIds):
        self._RouteIds = RouteIds


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRoutesResponse(AbstractModel):
    """EnableRoutes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """Enhanced service

    """

    def __init__(self):
        r"""
        :param _SecurityService: Whether to enable CWP.
        :type SecurityService: :class:`tencentcloud.ecm.v20190719.models.RunSecurityServiceEnabled`
        :param _MonitorService: Whether to enable CM.
        :type MonitorService: :class:`tencentcloud.ecm.v20190719.models.RunMonitorServiceEnabled`
        :param _EIPDirectService: Whether to enable IP direct access. If this parameter is not specified, IP direct access will be enabled by default for Linux images and is currently not supported for Windows images.
        :type EIPDirectService: :class:`tencentcloud.ecm.v20190719.models.RunEIPDirectServiceEnabled`
        """
        self._SecurityService = None
        self._MonitorService = None
        self._EIPDirectService = None

    @property
    def SecurityService(self):
        """Whether to enable CWP.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RunSecurityServiceEnabled`
        """
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        """Whether to enable CM.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RunMonitorServiceEnabled`
        """
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def EIPDirectService(self):
        """Whether to enable IP direct access. If this parameter is not specified, IP direct access will be enabled by default for Linux images and is currently not supported for Windows images.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RunEIPDirectServiceEnabled`
        """
        return self._EIPDirectService

    @EIPDirectService.setter
    def EIPDirectService(self, EIPDirectService):
        self._EIPDirectService = EIPDirectService


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self._SecurityService = RunSecurityServiceEnabled()
            self._SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self._MonitorService = RunMonitorServiceEnabled()
            self._MonitorService._deserialize(params.get("MonitorService"))
        if params.get("EIPDirectService") is not None:
            self._EIPDirectService = RunEIPDirectServiceEnabled()
            self._EIPDirectService._deserialize(params.get("EIPDirectService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Key-Value pair filter for conditional filtering queries.

    """

    def __init__(self):
        r"""
        :param _Values: One or more filter values.
        :type Values: list of str
        :param _Name: Filter name.
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        """One or more filter values.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        """Filter name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HaVip(AbstractModel):
    """HAVIP object.

    """

    def __init__(self):
        r"""
        :param _HaVipId: Unique HAVIP ID.
        :type HaVipId: str
        :param _HaVipName: HAVIP name.
        :type HaVipName: str
        :param _Vip: Virtual IP address.
        :type Vip: str
        :param _VpcId: VPC ID of the HAVIP.
        :type VpcId: str
        :param _SubnetId: Subnet ID of the HAVIP.
        :type SubnetId: str
        :param _NetworkInterfaceId: ID of the ENI associated with the HAVIP.
        :type NetworkInterfaceId: str
        :param _InstanceId: ID of the bound instance.
        :type InstanceId: str
        :param _AddressIp: Bound EIP.
        :type AddressIp: str
        :param _State: Status:
AVAILABLE: running.
UNBIND: unbound.
        :type State: str
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _Business: ID of businesses that use HAVIP.
        :type Business: str
        """
        self._HaVipId = None
        self._HaVipName = None
        self._Vip = None
        self._VpcId = None
        self._SubnetId = None
        self._NetworkInterfaceId = None
        self._InstanceId = None
        self._AddressIp = None
        self._State = None
        self._CreatedTime = None
        self._Business = None

    @property
    def HaVipId(self):
        """Unique HAVIP ID.
        :rtype: str
        """
        return self._HaVipId

    @HaVipId.setter
    def HaVipId(self, HaVipId):
        self._HaVipId = HaVipId

    @property
    def HaVipName(self):
        """HAVIP name.
        :rtype: str
        """
        return self._HaVipName

    @HaVipName.setter
    def HaVipName(self, HaVipName):
        self._HaVipName = HaVipName

    @property
    def Vip(self):
        """Virtual IP address.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VpcId(self):
        """VPC ID of the HAVIP.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID of the HAVIP.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def NetworkInterfaceId(self):
        """ID of the ENI associated with the HAVIP.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def InstanceId(self):
        """ID of the bound instance.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AddressIp(self):
        """Bound EIP.
        :rtype: str
        """
        return self._AddressIp

    @AddressIp.setter
    def AddressIp(self, AddressIp):
        self._AddressIp = AddressIp

    @property
    def State(self):
        """Status:
AVAILABLE: running.
UNBIND: unbound.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreatedTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Business(self):
        """ID of businesses that use HAVIP.
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._HaVipId = params.get("HaVipId")
        self._HaVipName = params.get("HaVipName")
        self._Vip = params.get("Vip")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._InstanceId = params.get("InstanceId")
        self._AddressIp = params.get("AddressIp")
        self._State = params.get("State")
        self._CreatedTime = params.get("CreatedTime")
        self._Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheck(AbstractModel):
    """CLB health check

    """

    def __init__(self):
        r"""
        :param _HealthSwitch: Whether to enable health check. Valid values: 1: enable; 0: disable
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthSwitch: int
        :param _TimeOut: Health check response timeout period in seconds. Value range: 2–60. Default value: 2. The value of this parameter should be smaller than the check interval.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeOut: int
        :param _IntervalTime: Health check interval in seconds. Value range: 5–300. Default value: 5.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IntervalTime: int
        :param _HealthNum: Health threshold. Value range: 2–10. Default value: 3, indicating that if a forward is found healthy three consecutive times, it will be considered normal.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthNum: int
        :param _UnHealthyNum: Unhealthy threshold. Value range: 2–10. Default value: 3, indicating that if a forward is found unhealthy three consecutive times, it will be considered exceptional.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UnHealthyNum: int
        :param _CheckPort: Health check port (a custom check parameter), which is the port of the real server by default. Unless you want to specify a port, we recommend you leave it empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CheckPort: int
        :param _ContextType: Health check protocol (a custom check parameter), which is required if the value of `CheckType` is `CUSTOM`. This parameter represents the input format of the health check. Valid values: HEX, TEXT. If the value is `HEX`, the characters of `SendContext` and `RecvContext` can only be selected from `0123456789ABCDEF`, and the length must be an even number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContextType: str
        :param _SendContext: Health check protocol (a custom check parameter), which is required if the value of `CheckType` is `CUSTOM`. This parameter represents the content of the request sent by the health check. It can contain up to 500 visible ASCII characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SendContext: str
        :param _RecvContext: Health check protocol (a custom check parameter), which is required if the value of `CheckType` is `CUSTOM`. This parameter represents the result returned by the health check. It can contain up to 500 visible ASCII characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RecvContext: str
        :param _CheckType: Health check protocol (a custom check parameter). Valid values: TCP, CUSTOM (applicable only to UDP listeners. If custom health check is used, this parameter will be required).
Note: this field may return null, indicating that no valid values can be obtained.
        :type CheckType: str
        """
        self._HealthSwitch = None
        self._TimeOut = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnHealthyNum = None
        self._CheckPort = None
        self._ContextType = None
        self._SendContext = None
        self._RecvContext = None
        self._CheckType = None

    @property
    def HealthSwitch(self):
        """Whether to enable health check. Valid values: 1: enable; 0: disable
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        """Health check response timeout period in seconds. Value range: 2–60. Default value: 2. The value of this parameter should be smaller than the check interval.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        """Health check interval in seconds. Value range: 5–300. Default value: 5.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        """Health threshold. Value range: 2–10. Default value: 3, indicating that if a forward is found healthy three consecutive times, it will be considered normal.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnHealthyNum(self):
        """Unhealthy threshold. Value range: 2–10. Default value: 3, indicating that if a forward is found unhealthy three consecutive times, it will be considered exceptional.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._UnHealthyNum

    @UnHealthyNum.setter
    def UnHealthyNum(self, UnHealthyNum):
        self._UnHealthyNum = UnHealthyNum

    @property
    def CheckPort(self):
        """Health check port (a custom check parameter), which is the port of the real server by default. Unless you want to specify a port, we recommend you leave it empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        """Health check protocol (a custom check parameter), which is required if the value of `CheckType` is `CUSTOM`. This parameter represents the input format of the health check. Valid values: HEX, TEXT. If the value is `HEX`, the characters of `SendContext` and `RecvContext` can only be selected from `0123456789ABCDEF`, and the length must be an even number.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def SendContext(self):
        """Health check protocol (a custom check parameter), which is required if the value of `CheckType` is `CUSTOM`. This parameter represents the content of the request sent by the health check. It can contain up to 500 visible ASCII characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SendContext

    @SendContext.setter
    def SendContext(self, SendContext):
        self._SendContext = SendContext

    @property
    def RecvContext(self):
        """Health check protocol (a custom check parameter), which is required if the value of `CheckType` is `CUSTOM`. This parameter represents the result returned by the health check. It can contain up to 500 visible ASCII characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RecvContext

    @RecvContext.setter
    def RecvContext(self, RecvContext):
        self._RecvContext = RecvContext

    @property
    def CheckType(self):
        """Health check protocol (a custom check parameter). Valid values: TCP, CUSTOM (applicable only to UDP listeners. If custom health check is used, this parameter will be required).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType


    def _deserialize(self, params):
        self._HealthSwitch = params.get("HealthSwitch")
        self._TimeOut = params.get("TimeOut")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnHealthyNum = params.get("UnHealthyNum")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._SendContext = params.get("SendContext")
        self._RecvContext = params.get("RecvContext")
        self._CheckType = params.get("CheckType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISP(AbstractModel):
    """ISP information

    """

    def __init__(self):
        r"""
        :param _ISPId: ISP ID
        :type ISPId: str
        :param _ISPName: ISP name
        :type ISPName: str
        """
        self._ISPId = None
        self._ISPName = None

    @property
    def ISPId(self):
        """ISP ID
        :rtype: str
        """
        return self._ISPId

    @ISPId.setter
    def ISPId(self, ISPId):
        self._ISPId = ISPId

    @property
    def ISPName(self):
        """ISP name
        :rtype: str
        """
        return self._ISPName

    @ISPName.setter
    def ISPName(self, ISPName):
        self._ISPName = ISPName


    def _deserialize(self, params):
        self._ISPId = params.get("ISPId")
        self._ISPName = params.get("ISPName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISPCounter(AbstractModel):
    """ISP statistics

    """

    def __init__(self):
        r"""
        :param _ProviderName: ISP name
        :type ProviderName: str
        :param _ProviderNodeNum: Number of nodes
        :type ProviderNodeNum: int
        :param _ProvederInstanceNum: Number of instances
        :type ProvederInstanceNum: int
        :param _ZoneInstanceInfoSet: Zone instance information structure array
        :type ZoneInstanceInfoSet: list of ZoneInstanceInfo
        """
        self._ProviderName = None
        self._ProviderNodeNum = None
        self._ProvederInstanceNum = None
        self._ZoneInstanceInfoSet = None

    @property
    def ProviderName(self):
        """ISP name
        :rtype: str
        """
        return self._ProviderName

    @ProviderName.setter
    def ProviderName(self, ProviderName):
        self._ProviderName = ProviderName

    @property
    def ProviderNodeNum(self):
        """Number of nodes
        :rtype: int
        """
        return self._ProviderNodeNum

    @ProviderNodeNum.setter
    def ProviderNodeNum(self, ProviderNodeNum):
        self._ProviderNodeNum = ProviderNodeNum

    @property
    def ProvederInstanceNum(self):
        """Number of instances
        :rtype: int
        """
        return self._ProvederInstanceNum

    @ProvederInstanceNum.setter
    def ProvederInstanceNum(self, ProvederInstanceNum):
        self._ProvederInstanceNum = ProvederInstanceNum

    @property
    def ZoneInstanceInfoSet(self):
        """Zone instance information structure array
        :rtype: list of ZoneInstanceInfo
        """
        return self._ZoneInstanceInfoSet

    @ZoneInstanceInfoSet.setter
    def ZoneInstanceInfoSet(self, ZoneInstanceInfoSet):
        self._ZoneInstanceInfoSet = ZoneInstanceInfoSet


    def _deserialize(self, params):
        self._ProviderName = params.get("ProviderName")
        self._ProviderNodeNum = params.get("ProviderNodeNum")
        self._ProvederInstanceNum = params.get("ProvederInstanceNum")
        if params.get("ZoneInstanceInfoSet") is not None:
            self._ZoneInstanceInfoSet = []
            for item in params.get("ZoneInstanceInfoSet"):
                obj = ZoneInstanceInfo()
                obj._deserialize(item)
                self._ZoneInstanceInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    """Image information

    """

    def __init__(self):
        r"""
        :param _ImageId: Image ID
        :type ImageId: str
        :param _ImageName: Image name
        :type ImageName: str
        :param _ImageState: Image status
        :type ImageState: str
        :param _ImageType: Image type
        :type ImageType: str
        :param _ImageOsName: OS name
        :type ImageOsName: str
        :param _ImageDescription: Image description
        :type ImageDescription: str
        :param _ImageCreateTime: Image import time
        :type ImageCreateTime: str
        :param _Architecture: Number of bits of the OS
        :type Architecture: str
        :param _OsType: OS type
        :type OsType: str
        :param _OsVersion: OS version
        :type OsVersion: str
        :param _Platform: OS platform
        :type Platform: str
        :param _ImageOwner: Image owner
        :type ImageOwner: int
        :param _ImageSize: Image size in GB
        :type ImageSize: int
        :param _SrcImage: Image source information
        :type SrcImage: :class:`tencentcloud.ecm.v20190719.models.SrcImage`
        :param _ImageSource: Image source type
        :type ImageSource: str
        :param _TaskId: ID of the task in intermediate or failed status
        :type TaskId: str
        :param _IsSupportCloudInit: Whether cloud-init is supported
        :type IsSupportCloudInit: bool
        """
        self._ImageId = None
        self._ImageName = None
        self._ImageState = None
        self._ImageType = None
        self._ImageOsName = None
        self._ImageDescription = None
        self._ImageCreateTime = None
        self._Architecture = None
        self._OsType = None
        self._OsVersion = None
        self._Platform = None
        self._ImageOwner = None
        self._ImageSize = None
        self._SrcImage = None
        self._ImageSource = None
        self._TaskId = None
        self._IsSupportCloudInit = None

    @property
    def ImageId(self):
        """Image ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        """Image name
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageState(self):
        """Image status
        :rtype: str
        """
        return self._ImageState

    @ImageState.setter
    def ImageState(self, ImageState):
        self._ImageState = ImageState

    @property
    def ImageType(self):
        """Image type
        :rtype: str
        """
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def ImageOsName(self):
        """OS name
        :rtype: str
        """
        return self._ImageOsName

    @ImageOsName.setter
    def ImageOsName(self, ImageOsName):
        self._ImageOsName = ImageOsName

    @property
    def ImageDescription(self):
        """Image description
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def ImageCreateTime(self):
        """Image import time
        :rtype: str
        """
        return self._ImageCreateTime

    @ImageCreateTime.setter
    def ImageCreateTime(self, ImageCreateTime):
        self._ImageCreateTime = ImageCreateTime

    @property
    def Architecture(self):
        """Number of bits of the OS
        :rtype: str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def OsType(self):
        """OS type
        :rtype: str
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OsVersion(self):
        """OS version
        :rtype: str
        """
        return self._OsVersion

    @OsVersion.setter
    def OsVersion(self, OsVersion):
        self._OsVersion = OsVersion

    @property
    def Platform(self):
        """OS platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ImageOwner(self):
        """Image owner
        :rtype: int
        """
        return self._ImageOwner

    @ImageOwner.setter
    def ImageOwner(self, ImageOwner):
        self._ImageOwner = ImageOwner

    @property
    def ImageSize(self):
        """Image size in GB
        :rtype: int
        """
        return self._ImageSize

    @ImageSize.setter
    def ImageSize(self, ImageSize):
        self._ImageSize = ImageSize

    @property
    def SrcImage(self):
        """Image source information
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SrcImage`
        """
        return self._SrcImage

    @SrcImage.setter
    def SrcImage(self, SrcImage):
        self._SrcImage = SrcImage

    @property
    def ImageSource(self):
        """Image source type
        :rtype: str
        """
        return self._ImageSource

    @ImageSource.setter
    def ImageSource(self, ImageSource):
        self._ImageSource = ImageSource

    @property
    def TaskId(self):
        """ID of the task in intermediate or failed status
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def IsSupportCloudInit(self):
        """Whether cloud-init is supported
        :rtype: bool
        """
        return self._IsSupportCloudInit

    @IsSupportCloudInit.setter
    def IsSupportCloudInit(self, IsSupportCloudInit):
        self._IsSupportCloudInit = IsSupportCloudInit


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._ImageState = params.get("ImageState")
        self._ImageType = params.get("ImageType")
        self._ImageOsName = params.get("ImageOsName")
        self._ImageDescription = params.get("ImageDescription")
        self._ImageCreateTime = params.get("ImageCreateTime")
        self._Architecture = params.get("Architecture")
        self._OsType = params.get("OsType")
        self._OsVersion = params.get("OsVersion")
        self._Platform = params.get("Platform")
        self._ImageOwner = params.get("ImageOwner")
        self._ImageSize = params.get("ImageSize")
        if params.get("SrcImage") is not None:
            self._SrcImage = SrcImage()
            self._SrcImage._deserialize(params.get("SrcImage"))
        self._ImageSource = params.get("ImageSource")
        self._TaskId = params.get("TaskId")
        self._IsSupportCloudInit = params.get("IsSupportCloudInit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageLimitConfig(AbstractModel):
    """Image size configuration

    """

    def __init__(self):
        r"""
        :param _MaxImageSize: Supported maximum image size in GB, including custom image size for import and central cloud image size.
        :type MaxImageSize: int
        """
        self._MaxImageSize = None

    @property
    def MaxImageSize(self):
        """Supported maximum image size in GB, including custom image size for import and central cloud image size.
        :rtype: int
        """
        return self._MaxImageSize

    @MaxImageSize.setter
    def MaxImageSize(self, MaxImageSize):
        self._MaxImageSize = MaxImageSize


    def _deserialize(self, params):
        self._MaxImageSize = params.get("MaxImageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOsList(AbstractModel):
    """Supported OS type. Valid values: Windows, Linux.

    """

    def __init__(self):
        r"""
        :param _Windows: Supported Windows OS
Note: this field may return null, indicating that no valid values can be obtained.
        :type Windows: list of str
        :param _Linux: Supported Linux OS
Note: this field may return null, indicating that no valid values can be obtained.
        :type Linux: list of str
        """
        self._Windows = None
        self._Linux = None

    @property
    def Windows(self):
        """Supported Windows OS
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Windows

    @Windows.setter
    def Windows(self, Windows):
        self._Windows = Windows

    @property
    def Linux(self):
        """Supported Linux OS
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Linux

    @Linux.setter
    def Linux(self, Linux):
        self._Linux = Linux


    def _deserialize(self, params):
        self._Windows = params.get("Windows")
        self._Linux = params.get("Linux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTask(AbstractModel):
    """Image task

    """

    def __init__(self):
        r"""
        :param _State: Image import status. Valid values: PENDING, PROCESSING, SUCCESS, FAILED
        :type State: str
        :param _Message: Cause of import failure (FAILED)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _ImageName: Image name
        :type ImageName: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        """
        self._State = None
        self._Message = None
        self._ImageName = None
        self._CreateTime = None

    @property
    def State(self):
        """Image import status. Valid values: PENDING, PROCESSING, SUCCESS, FAILED
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Message(self):
        """Cause of import failure (FAILED)
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ImageName(self):
        """Image name
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._State = params.get("State")
        self._Message = params.get("Message")
        self._ImageName = params.get("ImageName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageRequest(AbstractModel):
    """ImportImage request structure.

    """

    def __init__(self):
        r"""
        :param _ImageId: Image ID.
        :type ImageId: str
        :param _ImageDescription: Image description.
        :type ImageDescription: str
        :param _SourceRegion: Source region
        :type SourceRegion: str
        """
        self._ImageId = None
        self._ImageDescription = None
        self._SourceRegion = None

    @property
    def ImageId(self):
        """Image ID.
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageDescription(self):
        """Image description.
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def SourceRegion(self):
        """Source region
        :rtype: str
        """
        return self._SourceRegion

    @SourceRegion.setter
    def SourceRegion(self, SourceRegion):
        self._SourceRegion = SourceRegion


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageDescription = params.get("ImageDescription")
        self._SourceRegion = params.get("SourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageResponse(AbstractModel):
    """ImportImage response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """Instance information.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceName: Instance name, such as `ens-34241f3s`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _InstanceState: Instance status. Valid values:
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
        :param _Image: Information of the image currently used by the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Image: :class:`tencentcloud.ecm.v20190719.models.Image`
        :param _SimpleModule: Basic information of the current module of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SimpleModule: :class:`tencentcloud.ecm.v20190719.models.SimpleModule`
        :param _Position: Location information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Position: :class:`tencentcloud.ecm.v20190719.models.Position`
        :param _Internet: Network information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Internet: :class:`tencentcloud.ecm.v20190719.models.Internet`
        :param _InstanceTypeConfig: Configuration information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        :param _CreateTime: Instance creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _TagSet: Instance tag information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param _LatestOperation: Last operation on the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestOperation: str
        :param _LatestOperationState: Result of the last operation on the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestOperationState: str
        :param _RestrictState: Instance business status. Valid values:
NORMAL: normal
EXPIRED: expired
PROTECTIVELY_ISOLATED: isolated.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RestrictState: str
        :param _SystemDiskSize: System disk size in GB.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SystemDiskSize: int
        :param _DataDiskSize: Data disk size in GB.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataDiskSize: int
        :param _UUID: Instance UUID
Note: this field may return null, indicating that no valid values can be obtained.
        :type UUID: str
        :param _PayMode: Billing mode.
    0: postpaid.
    1: prepaid.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PayMode: int
        :param _ExpireTime: Expiration time in the format of `yyyy-mm-dd HH:mm:ss`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _IsolatedTime: Isolation time in the format of `yyyy-mm-dd HH:mm:ss`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsolatedTime: str
        :param _RenewFlag: Auto-Renewal flag.
      0: no.
      1: yes.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        :param _ExpireState: Expiration status.
    NORMAL: normal.
    WILL_EXPIRE: about to expire.
    EXPIRED: expired.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireState: str
        :param _SystemDisk: System disk information
Note: this field may return null, indicating that no valid values can be obtained.
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.DiskInfo`
        :param _DataDisks: Data disk information
Note: this field may return null, indicating that no valid values can be obtained.
        :type DataDisks: list of DiskInfo
        :param _NewFlag: New instance flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type NewFlag: int
        :param _SecurityGroupIds: Security group of the instance, which can be obtained from the `sgId` field in the returned value of the `DescribeSecurityGroups` API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecurityGroupIds: list of str
        :param _VirtualPrivateCloud: VPC attribute
Note: this field may return null, indicating that no valid values can be obtained.
        :type VirtualPrivateCloud: :class:`tencentcloud.ecm.v20190719.models.VirtualPrivateCloud`
        :param _ISP: ISP field of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ISP: str
        :param _PhysicalPosition: Physical location information. Note that this field is currently a reserved field and null.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhysicalPosition: :class:`tencentcloud.ecm.v20190719.models.PhysicalPosition`
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceState = None
        self._Image = None
        self._SimpleModule = None
        self._Position = None
        self._Internet = None
        self._InstanceTypeConfig = None
        self._CreateTime = None
        self._TagSet = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._RestrictState = None
        self._SystemDiskSize = None
        self._DataDiskSize = None
        self._UUID = None
        self._PayMode = None
        self._ExpireTime = None
        self._IsolatedTime = None
        self._RenewFlag = None
        self._ExpireState = None
        self._SystemDisk = None
        self._DataDisks = None
        self._NewFlag = None
        self._SecurityGroupIds = None
        self._VirtualPrivateCloud = None
        self._ISP = None
        self._PhysicalPosition = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name, such as `ens-34241f3s`.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceState(self):
        """Instance status. Valid values:
PENDING: creating
LAUNCH_FAILED: failed to create
RUNNING: running
STOPPED: shut down
STARTING: starting
STOPPING: shutting down
REBOOTING: restarting
SHUTDOWN: to be terminated
TERMINATING: terminating.
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def Image(self):
        """Information of the image currently used by the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Image`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def SimpleModule(self):
        """Basic information of the current module of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SimpleModule`
        """
        return self._SimpleModule

    @SimpleModule.setter
    def SimpleModule(self, SimpleModule):
        self._SimpleModule = SimpleModule

    @property
    def Position(self):
        """Location information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Position`
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Internet(self):
        """Network information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Internet`
        """
        return self._Internet

    @Internet.setter
    def Internet(self, Internet):
        self._Internet = Internet

    @property
    def InstanceTypeConfig(self):
        """Configuration information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        """
        return self._InstanceTypeConfig

    @InstanceTypeConfig.setter
    def InstanceTypeConfig(self, InstanceTypeConfig):
        self._InstanceTypeConfig = InstanceTypeConfig

    @property
    def CreateTime(self):
        """Instance creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TagSet(self):
        """Instance tag information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def LatestOperation(self):
        """Last operation on the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        """Result of the last operation on the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def RestrictState(self):
        """Instance business status. Valid values:
NORMAL: normal
EXPIRED: expired
PROTECTIVELY_ISOLATED: isolated.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RestrictState

    @RestrictState.setter
    def RestrictState(self, RestrictState):
        self._RestrictState = RestrictState

    @property
    def SystemDiskSize(self):
        """System disk size in GB.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SystemDiskSize

    @SystemDiskSize.setter
    def SystemDiskSize(self, SystemDiskSize):
        self._SystemDiskSize = SystemDiskSize

    @property
    def DataDiskSize(self):
        """Data disk size in GB.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DataDiskSize

    @DataDiskSize.setter
    def DataDiskSize(self, DataDiskSize):
        self._DataDiskSize = DataDiskSize

    @property
    def UUID(self):
        """Instance UUID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UUID

    @UUID.setter
    def UUID(self, UUID):
        self._UUID = UUID

    @property
    def PayMode(self):
        """Billing mode.
    0: postpaid.
    1: prepaid.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpireTime(self):
        """Expiration time in the format of `yyyy-mm-dd HH:mm:ss`.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def IsolatedTime(self):
        """Isolation time in the format of `yyyy-mm-dd HH:mm:ss`.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def RenewFlag(self):
        """Auto-Renewal flag.
      0: no.
      1: yes.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ExpireState(self):
        """Expiration status.
    NORMAL: normal.
    WILL_EXPIRE: about to expire.
    EXPIRED: expired.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireState

    @ExpireState.setter
    def ExpireState(self, ExpireState):
        self._ExpireState = ExpireState

    @property
    def SystemDisk(self):
        """System disk information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DiskInfo`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """Data disk information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of DiskInfo
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def NewFlag(self):
        """New instance flag
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NewFlag

    @NewFlag.setter
    def NewFlag(self, NewFlag):
        self._NewFlag = NewFlag

    @property
    def SecurityGroupIds(self):
        """Security group of the instance, which can be obtained from the `sgId` field in the returned value of the `DescribeSecurityGroups` API.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def VirtualPrivateCloud(self):
        """VPC attribute
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.VirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ISP(self):
        """ISP field of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def PhysicalPosition(self):
        """Physical location information. Note that this field is currently a reserved field and null.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PhysicalPosition`
        """
        return self._PhysicalPosition

    @PhysicalPosition.setter
    def PhysicalPosition(self, PhysicalPosition):
        self._PhysicalPosition = PhysicalPosition


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceState = params.get("InstanceState")
        if params.get("Image") is not None:
            self._Image = Image()
            self._Image._deserialize(params.get("Image"))
        if params.get("SimpleModule") is not None:
            self._SimpleModule = SimpleModule()
            self._SimpleModule._deserialize(params.get("SimpleModule"))
        if params.get("Position") is not None:
            self._Position = Position()
            self._Position._deserialize(params.get("Position"))
        if params.get("Internet") is not None:
            self._Internet = Internet()
            self._Internet._deserialize(params.get("Internet"))
        if params.get("InstanceTypeConfig") is not None:
            self._InstanceTypeConfig = InstanceTypeConfig()
            self._InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        self._CreateTime = params.get("CreateTime")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._RestrictState = params.get("RestrictState")
        self._SystemDiskSize = params.get("SystemDiskSize")
        self._DataDiskSize = params.get("DataDiskSize")
        self._UUID = params.get("UUID")
        self._PayMode = params.get("PayMode")
        self._ExpireTime = params.get("ExpireTime")
        self._IsolatedTime = params.get("IsolatedTime")
        self._RenewFlag = params.get("RenewFlag")
        self._ExpireState = params.get("ExpireState")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = DiskInfo()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DiskInfo()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._NewFlag = params.get("NewFlag")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ISP = params.get("ISP")
        if params.get("PhysicalPosition") is not None:
            self._PhysicalPosition = PhysicalPosition()
            self._PhysicalPosition._deserialize(params.get("PhysicalPosition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyConfig(AbstractModel):
    """Model family configuration

    """

    def __init__(self):
        r"""
        :param _InstanceFamilyName: Model name
        :type InstanceFamilyName: str
        :param _InstanceFamily: Model ID
        :type InstanceFamily: str
        """
        self._InstanceFamilyName = None
        self._InstanceFamily = None

    @property
    def InstanceFamilyName(self):
        """Model name
        :rtype: str
        """
        return self._InstanceFamilyName

    @InstanceFamilyName.setter
    def InstanceFamilyName(self, InstanceFamilyName):
        self._InstanceFamilyName = InstanceFamilyName

    @property
    def InstanceFamily(self):
        """Model ID
        :rtype: str
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily


    def _deserialize(self, params):
        self._InstanceFamilyName = params.get("InstanceFamilyName")
        self._InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyTypeConfig(AbstractModel):
    """Instance family type configuration

    """

    def __init__(self):
        r"""
        :param _InstanceFamilyType: Instance model family type ID
        :type InstanceFamilyType: str
        :param _InstanceFamilyTypeName: Instance model family type name
        :type InstanceFamilyTypeName: str
        """
        self._InstanceFamilyType = None
        self._InstanceFamilyTypeName = None

    @property
    def InstanceFamilyType(self):
        """Instance model family type ID
        :rtype: str
        """
        return self._InstanceFamilyType

    @InstanceFamilyType.setter
    def InstanceFamilyType(self, InstanceFamilyType):
        self._InstanceFamilyType = InstanceFamilyType

    @property
    def InstanceFamilyTypeName(self):
        """Instance model family type name
        :rtype: str
        """
        return self._InstanceFamilyTypeName

    @InstanceFamilyTypeName.setter
    def InstanceFamilyTypeName(self, InstanceFamilyTypeName):
        self._InstanceFamilyTypeName = InstanceFamilyTypeName


    def _deserialize(self, params):
        self._InstanceFamilyType = params.get("InstanceFamilyType")
        self._InstanceFamilyTypeName = params.get("InstanceFamilyTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNetworkInfo(AbstractModel):
    """Instance ENI IP information array

    """

    def __init__(self):
        r"""
        :param _AddressInfoSet: Private and public IP information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddressInfoSet: list of AddressInfo
        :param _NetworkInterfaceId: ENI ID.
        :type NetworkInterfaceId: str
        :param _NetworkInterfaceName: ENI name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetworkInterfaceName: str
        :param _Primary: Primary ENI attribute. Valid values: true: primary ENI; false: secondary ENI.
        :type Primary: bool
        """
        self._AddressInfoSet = None
        self._NetworkInterfaceId = None
        self._NetworkInterfaceName = None
        self._Primary = None

    @property
    def AddressInfoSet(self):
        """Private and public IP information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of AddressInfo
        """
        return self._AddressInfoSet

    @AddressInfoSet.setter
    def AddressInfoSet(self, AddressInfoSet):
        self._AddressInfoSet = AddressInfoSet

    @property
    def NetworkInterfaceId(self):
        """ENI ID.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def NetworkInterfaceName(self):
        """ENI name.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NetworkInterfaceName

    @NetworkInterfaceName.setter
    def NetworkInterfaceName(self, NetworkInterfaceName):
        self._NetworkInterfaceName = NetworkInterfaceName

    @property
    def Primary(self):
        """Primary ENI attribute. Valid values: true: primary ENI; false: secondary ENI.
        :rtype: bool
        """
        return self._Primary

    @Primary.setter
    def Primary(self, Primary):
        self._Primary = Primary


    def _deserialize(self, params):
        if params.get("AddressInfoSet") is not None:
            self._AddressInfoSet = []
            for item in params.get("AddressInfoSet"):
                obj = AddressInfo()
                obj._deserialize(item)
                self._AddressInfoSet.append(obj)
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._NetworkInterfaceName = params.get("NetworkInterfaceName")
        self._Primary = params.get("Primary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNetworkLimitConfig(AbstractModel):
    """Network resource limit of the instance

    """

    def __init__(self):
        r"""
        :param _CpuNum: Number of CPU cores
        :type CpuNum: int
        :param _NetworkInterfaceLimit: ENI quantity limit
        :type NetworkInterfaceLimit: int
        :param _InnerIpPerNetworkInterface: Private IP quantity limit per ENI
        :type InnerIpPerNetworkInterface: int
        :param _PublicIpPerInstance: Public IP limit per instance
        :type PublicIpPerInstance: int
        """
        self._CpuNum = None
        self._NetworkInterfaceLimit = None
        self._InnerIpPerNetworkInterface = None
        self._PublicIpPerInstance = None

    @property
    def CpuNum(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def NetworkInterfaceLimit(self):
        """ENI quantity limit
        :rtype: int
        """
        return self._NetworkInterfaceLimit

    @NetworkInterfaceLimit.setter
    def NetworkInterfaceLimit(self, NetworkInterfaceLimit):
        self._NetworkInterfaceLimit = NetworkInterfaceLimit

    @property
    def InnerIpPerNetworkInterface(self):
        """Private IP quantity limit per ENI
        :rtype: int
        """
        return self._InnerIpPerNetworkInterface

    @InnerIpPerNetworkInterface.setter
    def InnerIpPerNetworkInterface(self, InnerIpPerNetworkInterface):
        self._InnerIpPerNetworkInterface = InnerIpPerNetworkInterface

    @property
    def PublicIpPerInstance(self):
        """Public IP limit per instance
        :rtype: int
        """
        return self._PublicIpPerInstance

    @PublicIpPerInstance.setter
    def PublicIpPerInstance(self, PublicIpPerInstance):
        self._PublicIpPerInstance = PublicIpPerInstance


    def _deserialize(self, params):
        self._CpuNum = params.get("CpuNum")
        self._NetworkInterfaceLimit = params.get("NetworkInterfaceLimit")
        self._InnerIpPerNetworkInterface = params.get("InnerIpPerNetworkInterface")
        self._PublicIpPerInstance = params.get("PublicIpPerInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceOperator(AbstractModel):
    """Executable operations for the instance

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _DeniedActions: Prohibited operations for the instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeniedActions: list of OperatorAction
        """
        self._InstanceId = None
        self._DeniedActions = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeniedActions(self):
        """Prohibited operations for the instance
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of OperatorAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = OperatorAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancePricesPartDetail(AbstractModel):
    """Instance price information

    """

    def __init__(self):
        r"""
        :param _CpuPrice: CPU price information
        :type CpuPrice: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        :param _MemPrice: Memory price information
        :type MemPrice: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        :param _DisksPrice: Disk price information
        :type DisksPrice: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        """
        self._CpuPrice = None
        self._MemPrice = None
        self._DisksPrice = None

    @property
    def CpuPrice(self):
        """CPU price information
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        """
        return self._CpuPrice

    @CpuPrice.setter
    def CpuPrice(self, CpuPrice):
        self._CpuPrice = CpuPrice

    @property
    def MemPrice(self):
        """Memory price information
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        """
        return self._MemPrice

    @MemPrice.setter
    def MemPrice(self, MemPrice):
        self._MemPrice = MemPrice

    @property
    def DisksPrice(self):
        """Disk price information
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        """
        return self._DisksPrice

    @DisksPrice.setter
    def DisksPrice(self, DisksPrice):
        self._DisksPrice = DisksPrice


    def _deserialize(self, params):
        if params.get("CpuPrice") is not None:
            self._CpuPrice = PriceDetail()
            self._CpuPrice._deserialize(params.get("CpuPrice"))
        if params.get("MemPrice") is not None:
            self._MemPrice = PriceDetail()
            self._MemPrice._deserialize(params.get("MemPrice"))
        if params.get("DisksPrice") is not None:
            self._DisksPrice = PriceDetail()
            self._DisksPrice._deserialize(params.get("DisksPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStatistic(AbstractModel):
    """Instance statistics

    """

    def __init__(self):
        r"""
        :param _InstanceType: Instance type
        :type InstanceType: str
        :param _InstanceCount: Number of instances
        :type InstanceCount: int
        """
        self._InstanceType = None
        self._InstanceCount = None

    @property
    def InstanceType(self):
        """Instance type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceCount(self):
        """Number of instances
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeConfig(AbstractModel):
    """Model configuration

    """

    def __init__(self):
        r"""
        :param _InstanceFamilyConfig: Model family configuration information
        :type InstanceFamilyConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyConfig`
        :param _InstanceType: Model
        :type InstanceType: str
        :param _Vcpu: Number of CPU cores
        :type Vcpu: int
        :param _Memory: Memory size
        :type Memory: int
        :param _Frequency: Clock rate
        :type Frequency: str
        :param _CpuModelName: CPU model
        :type CpuModelName: str
        :param _InstanceFamilyTypeConfig: Instance family type configuration information
        :type InstanceFamilyTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        :param _ExtInfo: Extra model information, which is a JSON string in the format of `{"dataDiskSize":3200,"systemDiskSize":60, "systemDiskSizeShow":"default system disk size:60 GB","dataDiskSizeShow":"local NVMe SSD: 3200 GB"}`. It indicates a special model if it exists
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExtInfo: str
        :param _Vgpu: Number of GPU cards
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vgpu: float
        :param _GpuModelName: GPU model
Note: this field may return null, indicating that no valid values can be obtained.
        :type GpuModelName: str
        """
        self._InstanceFamilyConfig = None
        self._InstanceType = None
        self._Vcpu = None
        self._Memory = None
        self._Frequency = None
        self._CpuModelName = None
        self._InstanceFamilyTypeConfig = None
        self._ExtInfo = None
        self._Vgpu = None
        self._GpuModelName = None

    @property
    def InstanceFamilyConfig(self):
        """Model family configuration information
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyConfig`
        """
        return self._InstanceFamilyConfig

    @InstanceFamilyConfig.setter
    def InstanceFamilyConfig(self, InstanceFamilyConfig):
        self._InstanceFamilyConfig = InstanceFamilyConfig

    @property
    def InstanceType(self):
        """Model
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Vcpu(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._Vcpu

    @Vcpu.setter
    def Vcpu(self, Vcpu):
        self._Vcpu = Vcpu

    @property
    def Memory(self):
        """Memory size
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Frequency(self):
        """Clock rate
        :rtype: str
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def CpuModelName(self):
        """CPU model
        :rtype: str
        """
        return self._CpuModelName

    @CpuModelName.setter
    def CpuModelName(self, CpuModelName):
        self._CpuModelName = CpuModelName

    @property
    def InstanceFamilyTypeConfig(self):
        """Instance family type configuration information
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        """
        return self._InstanceFamilyTypeConfig

    @InstanceFamilyTypeConfig.setter
    def InstanceFamilyTypeConfig(self, InstanceFamilyTypeConfig):
        self._InstanceFamilyTypeConfig = InstanceFamilyTypeConfig

    @property
    def ExtInfo(self):
        """Extra model information, which is a JSON string in the format of `{"dataDiskSize":3200,"systemDiskSize":60, "systemDiskSizeShow":"default system disk size:60 GB","dataDiskSizeShow":"local NVMe SSD: 3200 GB"}`. It indicates a special model if it exists
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExtInfo

    @ExtInfo.setter
    def ExtInfo(self, ExtInfo):
        self._ExtInfo = ExtInfo

    @property
    def Vgpu(self):
        """Number of GPU cards
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Vgpu

    @Vgpu.setter
    def Vgpu(self, Vgpu):
        self._Vgpu = Vgpu

    @property
    def GpuModelName(self):
        """GPU model
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GpuModelName

    @GpuModelName.setter
    def GpuModelName(self, GpuModelName):
        self._GpuModelName = GpuModelName


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfig") is not None:
            self._InstanceFamilyConfig = InstanceFamilyConfig()
            self._InstanceFamilyConfig._deserialize(params.get("InstanceFamilyConfig"))
        self._InstanceType = params.get("InstanceType")
        self._Vcpu = params.get("Vcpu")
        self._Memory = params.get("Memory")
        self._Frequency = params.get("Frequency")
        self._CpuModelName = params.get("CpuModelName")
        if params.get("InstanceFamilyTypeConfig") is not None:
            self._InstanceFamilyTypeConfig = InstanceFamilyTypeConfig()
            self._InstanceFamilyTypeConfig._deserialize(params.get("InstanceFamilyTypeConfig"))
        self._ExtInfo = params.get("ExtInfo")
        self._Vgpu = params.get("Vgpu")
        self._GpuModelName = params.get("GpuModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancesPrice(AbstractModel):
    """Instance price information

    """

    def __init__(self):
        r"""
        :param _InstancePricesPartDetail: Instance price details
        :type InstancePricesPartDetail: :class:`tencentcloud.ecm.v20190719.models.InstancePricesPartDetail`
        :param _Discount: Discount on the total instance price
        :type Discount: int
        :param _DiscountPrice: Discounted price
        :type DiscountPrice: int
        :param _OriginalPrice: Original cost
        :type OriginalPrice: int
        """
        self._InstancePricesPartDetail = None
        self._Discount = None
        self._DiscountPrice = None
        self._OriginalPrice = None

    @property
    def InstancePricesPartDetail(self):
        """Instance price details
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstancePricesPartDetail`
        """
        return self._InstancePricesPartDetail

    @InstancePricesPartDetail.setter
    def InstancePricesPartDetail(self, InstancePricesPartDetail):
        self._InstancePricesPartDetail = InstancePricesPartDetail

    @property
    def Discount(self):
        """Discount on the total instance price
        :rtype: int
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        """Discounted price
        :rtype: int
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def OriginalPrice(self):
        """Original cost
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice


    def _deserialize(self, params):
        if params.get("InstancePricesPartDetail") is not None:
            self._InstancePricesPartDetail = InstancePricesPartDetail()
            self._InstancePricesPartDetail._deserialize(params.get("InstancePricesPartDetail"))
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Internet(AbstractModel):
    """Network information of the instance.

    """

    def __init__(self):
        r"""
        :param _PrivateIPAddressSet: Private network information list of the instance, with the primary ENI followed by secondary ENIs in the order of binding.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIPAddressSet: list of PrivateIPAddressInfo
        :param _PublicIPAddressSet: Public network information list of the instance, with the primary ENI followed by secondary ENIs in the order of binding.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicIPAddressSet: list of PublicIPAddressInfo
        :param _InstanceNetworkInfoSet: Network information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceNetworkInfoSet: list of InstanceNetworkInfo
        """
        self._PrivateIPAddressSet = None
        self._PublicIPAddressSet = None
        self._InstanceNetworkInfoSet = None

    @property
    def PrivateIPAddressSet(self):
        """Private network information list of the instance, with the primary ENI followed by secondary ENIs in the order of binding.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of PrivateIPAddressInfo
        """
        return self._PrivateIPAddressSet

    @PrivateIPAddressSet.setter
    def PrivateIPAddressSet(self, PrivateIPAddressSet):
        self._PrivateIPAddressSet = PrivateIPAddressSet

    @property
    def PublicIPAddressSet(self):
        """Public network information list of the instance, with the primary ENI followed by secondary ENIs in the order of binding.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of PublicIPAddressInfo
        """
        return self._PublicIPAddressSet

    @PublicIPAddressSet.setter
    def PublicIPAddressSet(self, PublicIPAddressSet):
        self._PublicIPAddressSet = PublicIPAddressSet

    @property
    def InstanceNetworkInfoSet(self):
        """Network information of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceNetworkInfo
        """
        return self._InstanceNetworkInfoSet

    @InstanceNetworkInfoSet.setter
    def InstanceNetworkInfoSet(self, InstanceNetworkInfoSet):
        self._InstanceNetworkInfoSet = InstanceNetworkInfoSet


    def _deserialize(self, params):
        if params.get("PrivateIPAddressSet") is not None:
            self._PrivateIPAddressSet = []
            for item in params.get("PrivateIPAddressSet"):
                obj = PrivateIPAddressInfo()
                obj._deserialize(item)
                self._PrivateIPAddressSet.append(obj)
        if params.get("PublicIPAddressSet") is not None:
            self._PublicIPAddressSet = []
            for item in params.get("PublicIPAddressSet"):
                obj = PublicIPAddressInfo()
                obj._deserialize(item)
                self._PublicIPAddressSet.append(obj)
        if params.get("InstanceNetworkInfoSet") is not None:
            self._InstanceNetworkInfoSet = []
            for item in params.get("InstanceNetworkInfoSet"):
                obj = InstanceNetworkInfo()
                obj._deserialize(item)
                self._InstanceNetworkInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Address(AbstractModel):
    """IPv6 address information.

    """

    def __init__(self):
        r"""
        :param _Address: IPv6 address, such as `3402:4e00:20:100:0:8cd9:2a67:71f3`
        :type Address: str
        :param _Primary: Whether it is the primary IP.
        :type Primary: bool
        :param _AddressId: EIP instance ID, such as `eip-hxlqja90`.
        :type AddressId: str
        :param _Description: Description.
        :type Description: str
        :param _IsWanIpBlocked: Whether the public IP is blocked.
        :type IsWanIpBlocked: bool
        :param _State: IPv6 address status:
PENDING: generating
MIGRATING: migrating
DELETING: deleting
AVAILABLE: available
        :type State: str
        """
        self._Address = None
        self._Primary = None
        self._AddressId = None
        self._Description = None
        self._IsWanIpBlocked = None
        self._State = None

    @property
    def Address(self):
        """IPv6 address, such as `3402:4e00:20:100:0:8cd9:2a67:71f3`
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Primary(self):
        """Whether it is the primary IP.
        :rtype: bool
        """
        return self._Primary

    @Primary.setter
    def Primary(self, Primary):
        self._Primary = Primary

    @property
    def AddressId(self):
        """EIP instance ID, such as `eip-hxlqja90`.
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def Description(self):
        """Description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsWanIpBlocked(self):
        """Whether the public IP is blocked.
        :rtype: bool
        """
        return self._IsWanIpBlocked

    @IsWanIpBlocked.setter
    def IsWanIpBlocked(self, IsWanIpBlocked):
        self._IsWanIpBlocked = IsWanIpBlocked

    @property
    def State(self):
        """IPv6 address status:
PENDING: generating
MIGRATING: migrating
DELETING: deleting
AVAILABLE: available
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._Primary = params.get("Primary")
        self._AddressId = params.get("AddressId")
        self._Description = params.get("Description")
        self._IsWanIpBlocked = params.get("IsWanIpBlocked")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyPair(AbstractModel):
    """Key pair information

    """

    def __init__(self):
        r"""
        :param _KeyId: Key pair ID, which is the unique identifier of a key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param _KeyName: Key pair name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyName: str
        :param _ProjectId: Project ID of the key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _Description: Key pair description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _PublicKey: Public key (in plain text) of key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicKey: str
        :param _PrivateKey: Private key (in plaintext) of a key pair. Tencent Cloud do not store private keys. Therefore, keep them secure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateKey: str
        :param _AssociatedInstanceIds: List of IDs of the instances associated with the key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssociatedInstanceIds: list of str
        :param _CreatedTime: Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        """
        self._KeyId = None
        self._KeyName = None
        self._ProjectId = None
        self._Description = None
        self._PublicKey = None
        self._PrivateKey = None
        self._AssociatedInstanceIds = None
        self._CreatedTime = None

    @property
    def KeyId(self):
        """Key pair ID, which is the unique identifier of a key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyName(self):
        """Key pair name.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def ProjectId(self):
        """Project ID of the key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        """Key pair description.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PublicKey(self):
        """Public key (in plain text) of key pair.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def PrivateKey(self):
        """Private key (in plaintext) of a key pair. Tencent Cloud do not store private keys. Therefore, keep them secure.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def AssociatedInstanceIds(self):
        """List of IDs of the instances associated with the key.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AssociatedInstanceIds

    @AssociatedInstanceIds.setter
    def AssociatedInstanceIds(self, AssociatedInstanceIds):
        self._AssociatedInstanceIds = AssociatedInstanceIds

    @property
    def CreatedTime(self):
        """Creation time in the format of YYYY-MM-DDThh:mm:ssZ according to ISO 8601 standard. UTC time is used.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyName = params.get("KeyName")
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        self._PublicKey = params.get("PublicKey")
        self._PrivateKey = params.get("PrivateKey")
        self._AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Listener(AbstractModel):
    """CLB listener

    """

    def __init__(self):
        r"""
        :param _ListenerId: CLB listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param _Protocol: Listener protocol
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Port: Listener port.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _HealthCheck: Health check information of the listener
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        :param _Scheduler: Request scheduling method
Note: this field may return null, indicating that no valid values can be obtained.
        :type Scheduler: str
        :param _SessionExpireTime: Session persistence time
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionExpireTime: int
        :param _ListenerName: Listener name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param _CreateTime: Listener creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _SessionType: Session type of the listener
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionType: str
        :param _EndPort: End port of the port range
Note: this field may return null, indicating that no valid values can be obtained.
        :type EndPort: int
        """
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._HealthCheck = None
        self._Scheduler = None
        self._SessionExpireTime = None
        self._ListenerName = None
        self._CreateTime = None
        self._SessionType = None
        self._EndPort = None

    @property
    def ListenerId(self):
        """CLB listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        """Listener protocol
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """Listener port.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def HealthCheck(self):
        """Health check information of the listener
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Scheduler(self):
        """Request scheduling method
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SessionExpireTime(self):
        """Session persistence time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def ListenerName(self):
        """Listener name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def CreateTime(self):
        """Listener creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SessionType(self):
        """Session type of the listener
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SessionType

    @SessionType.setter
    def SessionType(self, SessionType):
        self._SessionType = SessionType

    @property
    def EndPort(self):
        """End port of the port range
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._Scheduler = params.get("Scheduler")
        self._SessionExpireTime = params.get("SessionExpireTime")
        self._ListenerName = params.get("ListenerName")
        self._CreateTime = params.get("CreateTime")
        self._SessionType = params.get("SessionType")
        self._EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerBackend(AbstractModel):
    """Listener backend

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param _Protocol: Listener protocol
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Port: Listener port
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _Targets: List of real servers bound to the CLB instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type Targets: list of Backend
        """
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._Targets = None

    @property
    def ListenerId(self):
        """Listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        """Listener protocol
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """Listener port
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Targets(self):
        """List of real servers bound to the CLB instance
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Backend
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerHealth(AbstractModel):
    """Listener health status

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param _ListenerName: Listener name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param _Protocol: Listener protocol
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Port: Listener port
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _Rules: List of forwarding rules of the listener
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rules: list of RuleHealth
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._Port = None
        self._Rules = None

    @property
    def ListenerId(self):
        """Listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """Listener name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        """Listener protocol
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """Listener port
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Rules(self):
        """List of forwarding rules of the listener
Note: this field may return null, indicating that no valid values can be obtained.
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
    """CLB instance information

    """

    def __init__(self):
        r"""
        :param _Region: Region.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Position: Location information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Position: :class:`tencentcloud.ecm.v20190719.models.Position`
        :param _LoadBalancerId: CLB instance ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerName: str
        :param _LoadBalancerType: Network type of the CLB instance. Valid values: OPEN: public network
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerType: str
        :param _LoadBalancerVips: List of VIPs of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerVips: list of str
        :param _Status: CLB instance status. Valid values:
 0: creating; 1: running.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _CreateTime: CLB instance creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _StatusTime: Last status change time of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusTime: str
        :param _VpcId: VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _Tags: CLB instance tag information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagInfo
        :param _VipIsp: ISP of the CLB IP address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VipIsp: str
        :param _NetworkAttributes: Network attribute of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NetworkAttributes: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        :param _SecureGroups: Security group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecureGroups: list of str
        :param _LoadBalancerPassToTarget: Whether the real server opens the traffic from ELB to the internet.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerPassToTarget: bool
        :param _AddressIPv6: IPv6 address of a CLB instance
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AddressIPv6: str
        """
        self._Region = None
        self._Position = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerType = None
        self._LoadBalancerVips = None
        self._Status = None
        self._CreateTime = None
        self._StatusTime = None
        self._VpcId = None
        self._Tags = None
        self._VipIsp = None
        self._NetworkAttributes = None
        self._SecureGroups = None
        self._LoadBalancerPassToTarget = None
        self._AddressIPv6 = None

    @property
    def Region(self):
        """Region.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Position(self):
        """Location information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Position`
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def LoadBalancerId(self):
        """CLB instance ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        """CLB instance name.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerType(self):
        """Network type of the CLB instance. Valid values: OPEN: public network
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def LoadBalancerVips(self):
        """List of VIPs of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def Status(self):
        """CLB instance status. Valid values:
 0: creating; 1: running.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """CLB instance creation time.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StatusTime(self):
        """Last status change time of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusTime

    @StatusTime.setter
    def StatusTime(self, StatusTime):
        self._StatusTime = StatusTime

    @property
    def VpcId(self):
        """VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Tags(self):
        """CLB instance tag information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def VipIsp(self):
        """ISP of the CLB IP address.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def NetworkAttributes(self):
        """Network attribute of the CLB instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        """
        return self._NetworkAttributes

    @NetworkAttributes.setter
    def NetworkAttributes(self, NetworkAttributes):
        self._NetworkAttributes = NetworkAttributes

    @property
    def SecureGroups(self):
        """Security group.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SecureGroups

    @SecureGroups.setter
    def SecureGroups(self, SecureGroups):
        self._SecureGroups = SecureGroups

    @property
    def LoadBalancerPassToTarget(self):
        """Whether the real server opens the traffic from ELB to the internet.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def AddressIPv6(self):
        """IPv6 address of a CLB instance
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddressIPv6

    @AddressIPv6.setter
    def AddressIPv6(self, AddressIPv6):
        self._AddressIPv6 = AddressIPv6


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("Position") is not None:
            self._Position = Position()
            self._Position._deserialize(params.get("Position"))
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._StatusTime = params.get("StatusTime")
        self._VpcId = params.get("VpcId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._VipIsp = params.get("VipIsp")
        if params.get("NetworkAttributes") is not None:
            self._NetworkAttributes = LoadBalancerInternetAccessible()
            self._NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        self._SecureGroups = params.get("SecureGroups")
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self._AddressIPv6 = params.get("AddressIPv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerHealth(AbstractModel):
    """CLB health status

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name
Note: this field may return null, indicating that no valid values can be obtained.
        :type LoadBalancerName: str
        :param _Listeners: List of listeners
Note: this field may return null, indicating that no valid values can be obtained.
        :type Listeners: list of ListenerHealth
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Listeners = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        """CLB instance name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Listeners(self):
        """List of listeners
Note: this field may return null, indicating that no valid values can be obtained.
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
        


class LoadBalancerInternetAccessible(AbstractModel):
    """CLB information such as bandwidth limit.

    """

    def __init__(self):
        r"""
        :param _InternetMaxBandwidthOut: Maximum outbound bandwidth in Mbps. Default value: 10.
        :type InternetMaxBandwidthOut: int
        """
        self._InternetMaxBandwidthOut = None

    @property
    def InternetMaxBandwidthOut(self):
        """Maximum outbound bandwidth in Mbps. Default value: 10.
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateNetworkInterfaceRequest(AbstractModel):
    """MigrateNetworkInterface request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param _SourceInstanceId: ID of the ECM instance bound to the ENI, such as `ein-r8hr2upy`.
        :type SourceInstanceId: str
        :param _DestinationInstanceId: ID of the destination ECM instance to be migrated.
        :type DestinationInstanceId: str
        """
        self._EcmRegion = None
        self._NetworkInterfaceId = None
        self._SourceInstanceId = None
        self._DestinationInstanceId = None

    @property
    def EcmRegion(self):
        """ECM region, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-m6dyj72l`.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def SourceInstanceId(self):
        """ID of the ECM instance bound to the ENI, such as `ein-r8hr2upy`.
        :rtype: str
        """
        return self._SourceInstanceId

    @SourceInstanceId.setter
    def SourceInstanceId(self, SourceInstanceId):
        self._SourceInstanceId = SourceInstanceId

    @property
    def DestinationInstanceId(self):
        """ID of the destination ECM instance to be migrated.
        :rtype: str
        """
        return self._DestinationInstanceId

    @DestinationInstanceId.setter
    def DestinationInstanceId(self, DestinationInstanceId):
        self._DestinationInstanceId = DestinationInstanceId


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._SourceInstanceId = params.get("SourceInstanceId")
        self._DestinationInstanceId = params.get("DestinationInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateNetworkInterfaceResponse(AbstractModel):
    """MigrateNetworkInterface response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MigratePrivateIpAddressRequest(AbstractModel):
    """MigratePrivateIpAddress request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param _SourceNetworkInterfaceId: ID of the ENI instance bound to the private IP, such as `eni-11112222`.
        :type SourceNetworkInterfaceId: str
        :param _DestinationNetworkInterfaceId: ID of the destination ENI instance to be migrated.
        :type DestinationNetworkInterfaceId: str
        :param _PrivateIpAddress: Private IP address to be migrated, such as `10.0.0.6`.
        :type PrivateIpAddress: str
        """
        self._EcmRegion = None
        self._SourceNetworkInterfaceId = None
        self._DestinationNetworkInterfaceId = None
        self._PrivateIpAddress = None

    @property
    def EcmRegion(self):
        """ECM region, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def SourceNetworkInterfaceId(self):
        """ID of the ENI instance bound to the private IP, such as `eni-11112222`.
        :rtype: str
        """
        return self._SourceNetworkInterfaceId

    @SourceNetworkInterfaceId.setter
    def SourceNetworkInterfaceId(self, SourceNetworkInterfaceId):
        self._SourceNetworkInterfaceId = SourceNetworkInterfaceId

    @property
    def DestinationNetworkInterfaceId(self):
        """ID of the destination ENI instance to be migrated.
        :rtype: str
        """
        return self._DestinationNetworkInterfaceId

    @DestinationNetworkInterfaceId.setter
    def DestinationNetworkInterfaceId(self, DestinationNetworkInterfaceId):
        self._DestinationNetworkInterfaceId = DestinationNetworkInterfaceId

    @property
    def PrivateIpAddress(self):
        """Private IP address to be migrated, such as `10.0.0.6`.
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._SourceNetworkInterfaceId = params.get("SourceNetworkInterfaceId")
        self._DestinationNetworkInterfaceId = params.get("DestinationNetworkInterfaceId")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigratePrivateIpAddressResponse(AbstractModel):
    """MigratePrivateIpAddress response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAddressAttributeRequest(AbstractModel):
    """ModifyAddressAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _AddressId: Unique EIP ID, such as `eip-11112222`.
        :type AddressId: str
        :param _AddressName: New EIP name, which can contain up to 20 characters.
        :type AddressName: str
        :param _EipDirectConnection: Whether "direct access" is enabled for the EIP. TRUE: yes. FALSE: no. Note that this parameter is available only to users who have activated the EIP direct access feature.
        :type EipDirectConnection: str
        """
        self._EcmRegion = None
        self._AddressId = None
        self._AddressName = None
        self._EipDirectConnection = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressId(self):
        """Unique EIP ID, such as `eip-11112222`.
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def AddressName(self):
        """New EIP name, which can contain up to 20 characters.
        :rtype: str
        """
        return self._AddressName

    @AddressName.setter
    def AddressName(self, AddressName):
        self._AddressName = AddressName

    @property
    def EipDirectConnection(self):
        """Whether "direct access" is enabled for the EIP. TRUE: yes. FALSE: no. Note that this parameter is available only to users who have activated the EIP direct access feature.
        :rtype: str
        """
        return self._EipDirectConnection

    @EipDirectConnection.setter
    def EipDirectConnection(self, EipDirectConnection):
        self._EipDirectConnection = EipDirectConnection


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressId = params.get("AddressId")
        self._AddressName = params.get("AddressName")
        self._EipDirectConnection = params.get("EipDirectConnection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressAttributeResponse(AbstractModel):
    """ModifyAddressAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAddressesBandwidthRequest(AbstractModel):
    """ModifyAddressesBandwidth request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _AddressIds: Unique EIP ID, such as `eip-xxxxxxx`
        :type AddressIds: list of str
        :param _InternetMaxBandwidthOut: Target bandwidth value
        :type InternetMaxBandwidthOut: int
        """
        self._EcmRegion = None
        self._AddressIds = None
        self._InternetMaxBandwidthOut = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressIds(self):
        """Unique EIP ID, such as `eip-xxxxxxx`
        :rtype: list of str
        """
        return self._AddressIds

    @AddressIds.setter
    def AddressIds(self, AddressIds):
        self._AddressIds = AddressIds

    @property
    def InternetMaxBandwidthOut(self):
        """Target bandwidth value
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressIds = params.get("AddressIds")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressesBandwidthResponse(AbstractModel):
    """ModifyAddressesBandwidth response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Async task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyDefaultSubnetRequest(AbstractModel):
    """ModifyDefaultSubnet request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _Zone: ECM AZ
        :type Zone: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        """
        self._EcmRegion = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Zone(self):
        """ECM AZ
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDefaultSubnetResponse(AbstractModel):
    """ModifyDefaultSubnet response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyHaVipAttributeRequest(AbstractModel):
    """ModifyHaVipAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _HaVipId: Unique HAVIP ID, such as `havip-9o233uri`.
        :type HaVipId: str
        :param _HaVipName: HAVIP name, which can be customized with up to 60 characters.
        :type HaVipName: str
        """
        self._HaVipId = None
        self._HaVipName = None

    @property
    def HaVipId(self):
        """Unique HAVIP ID, such as `havip-9o233uri`.
        :rtype: str
        """
        return self._HaVipId

    @HaVipId.setter
    def HaVipId(self, HaVipId):
        self._HaVipId = HaVipId

    @property
    def HaVipName(self):
        """HAVIP name, which can be customized with up to 60 characters.
        :rtype: str
        """
        return self._HaVipName

    @HaVipName.setter
    def HaVipName(self, HaVipName):
        self._HaVipName = HaVipName


    def _deserialize(self, params):
        self._HaVipId = params.get("HaVipId")
        self._HaVipName = params.get("HaVipName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHaVipAttributeResponse(AbstractModel):
    """ModifyHaVipAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ImageId: Image ID, such as `img-gvbnzy6f`
        :type ImageId: str
        :param _ImageName: Image name, which must meet the following requirements:
It can contain up to 20 characters.
- The image name cannot be the same as existing image names.
        :type ImageName: str
        :param _ImageDescription: Image description, which must meet the following requirements:
- It cannot exceed 60 characters.
        :type ImageDescription: str
        """
        self._ImageId = None
        self._ImageName = None
        self._ImageDescription = None

    @property
    def ImageId(self):
        """Image ID, such as `img-gvbnzy6f`
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        """Image name, which must meet the following requirements:
It can contain up to 20 characters.
- The image name cannot be the same as existing image names.
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageDescription(self):
        """Image description, which must meet the following requirements:
- It cannot exceed 60 characters.
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._ImageDescription = params.get("ImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAttributeResponse(AbstractModel):
    """ModifyImageAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of IDs of the instances to be modified. You can request up to 100 instances at a time.
        :type InstanceIdSet: list of str
        :param _InstanceName: Instance name displayed after successful modification, which can contain up to 60 characters. If this parameter is not specified, an empty value will be displayed.
        :type InstanceName: str
        :param _SecurityGroups: List of IDs of the security groups of the instance. The instance will be associated with the specified security groups and will be disassociated from the original security groups. The maximum quantity is 5.
        :type SecurityGroups: list of str
        """
        self._InstanceIdSet = None
        self._InstanceName = None
        self._SecurityGroups = None

    @property
    def InstanceIdSet(self):
        """List of IDs of the instances to be modified. You can request up to 100 instances at a time.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def InstanceName(self):
        """Instance name displayed after successful modification, which can contain up to 60 characters. If this parameter is not specified, an empty value will be displayed.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SecurityGroups(self):
        """List of IDs of the security groups of the instance. The instance will be associated with the specified security groups and will be disassociated from the original security groups. The maximum quantity is 5.
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._InstanceName = params.get("InstanceName")
        self._SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyIpv6AddressesAttributeRequest(AbstractModel):
    """ModifyIpv6AddressesAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param _Ipv6Addresses: Information of the specified IPv6 addresses.
        :type Ipv6Addresses: list of Ipv6Address
        """
        self._EcmRegion = None
        self._NetworkInterfaceId = None
        self._Ipv6Addresses = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-m6dyj72l`.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def Ipv6Addresses(self):
        """Information of the specified IPv6 addresses.
        :rtype: list of Ipv6Address
        """
        return self._Ipv6Addresses

    @Ipv6Addresses.setter
    def Ipv6Addresses(self, Ipv6Addresses):
        self._Ipv6Addresses = Ipv6Addresses


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self._Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6Addresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIpv6AddressesAttributeResponse(AbstractModel):
    """ModifyIpv6AddressesAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyListenerRequest(AbstractModel):
    """ModifyListener request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _ListenerName: New listener name
        :type ListenerName: str
        :param _SessionExpireTime: Session persistence time in seconds. Value range: 30–3600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.
        :type SessionExpireTime: int
        :param _HealthCheck: Health check parameters
        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        :param _Scheduler: Forwarding method of the listener. Valid values: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR.
        :type Scheduler: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._ListenerName = None
        self._SessionExpireTime = None
        self._HealthCheck = None
        self._Scheduler = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        """CLB listener ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """New listener name
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SessionExpireTime(self):
        """Session persistence time in seconds. Value range: 30–3600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners.
        :rtype: int
        """
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def HealthCheck(self):
        """Health check parameters
        :rtype: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Scheduler(self):
        """Forwarding method of the listener. Valid values: WRR, LEAST_CONN.
They represent weighted round robin and least connections, respectively. Default value: WRR.
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._Scheduler = params.get("Scheduler")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerResponse(AbstractModel):
    """ModifyListener response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: Unique CLB ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name
        :type LoadBalancerName: str
        :param _InternetChargeInfo: Network billing and bandwidth parameters
        :type InternetChargeInfo: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        :param _LoadBalancerPassToTarget: Whether to allow ELB traffic to the target group. `true`: allows ELB traffic to the target group and verifies security groups only on ELB; `false`: denies ELB traffic to the target group and verifies security groups on both ELB and backend instances.
        :type LoadBalancerPassToTarget: bool
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._InternetChargeInfo = None
        self._LoadBalancerPassToTarget = None

    @property
    def LoadBalancerId(self):
        """Unique CLB ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        """CLB instance name
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def InternetChargeInfo(self):
        """Network billing and bandwidth parameters
        :rtype: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        """
        return self._InternetChargeInfo

    @InternetChargeInfo.setter
    def InternetChargeInfo(self, InternetChargeInfo):
        self._InternetChargeInfo = InternetChargeInfo

    @property
    def LoadBalancerPassToTarget(self):
        """Whether to allow ELB traffic to the target group. `true`: allows ELB traffic to the target group and verifies security groups only on ELB; `false`: denies ELB traffic to the target group and verifies security groups on both ELB and backend instances.
        :rtype: bool
        """
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("InternetChargeInfo") is not None:
            self._InternetChargeInfo = LoadBalancerInternetAccessible()
            self._InternetChargeInfo._deserialize(params.get("InternetChargeInfo"))
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyModuleConfigRequest(AbstractModel):
    """ModifyModuleConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ModuleId: Module ID.
        :type ModuleId: str
        :param _InstanceType: Model ID.
        :type InstanceType: str
        :param _DefaultDataDiskSize: Default data disk size in GB. It cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :type DefaultDataDiskSize: int
        :param _DefaultSystemDiskSize: Default system disk size in GB. It cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :type DefaultSystemDiskSize: int
        :param _SystemDisk: System disk
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param _DataDisks: Data disk
        :type DataDisks: list of DataDisk
        """
        self._ModuleId = None
        self._InstanceType = None
        self._DefaultDataDiskSize = None
        self._DefaultSystemDiskSize = None
        self._SystemDisk = None
        self._DataDisks = None

    @property
    def ModuleId(self):
        """Module ID.
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def InstanceType(self):
        """Model ID.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DefaultDataDiskSize(self):
        """Default data disk size in GB. It cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :rtype: int
        """
        return self._DefaultDataDiskSize

    @DefaultDataDiskSize.setter
    def DefaultDataDiskSize(self, DefaultDataDiskSize):
        self._DefaultDataDiskSize = DefaultDataDiskSize

    @property
    def DefaultSystemDiskSize(self):
        """Default system disk size in GB. It cannot exceed the system disk size range. For more information, see `DescribeConfig`.
        :rtype: int
        """
        return self._DefaultSystemDiskSize

    @DefaultSystemDiskSize.setter
    def DefaultSystemDiskSize(self, DefaultSystemDiskSize):
        self._DefaultSystemDiskSize = DefaultSystemDiskSize

    @property
    def SystemDisk(self):
        """System disk
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """Data disk
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._InstanceType = params.get("InstanceType")
        self._DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        self._DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleConfigResponse(AbstractModel):
    """ModifyModuleConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyModuleDisableWanIpRequest(AbstractModel):
    """ModifyModuleDisableWanIp request structure.

    """

    def __init__(self):
        r"""
        :param _ModuleId: Module ID
        :type ModuleId: str
        :param _DisableWanIp: Whether to prohibit public IP assignment. Valid values: true: no; false: yes.
        :type DisableWanIp: bool
        """
        self._ModuleId = None
        self._DisableWanIp = None

    @property
    def ModuleId(self):
        """Module ID
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def DisableWanIp(self):
        """Whether to prohibit public IP assignment. Valid values: true: no; false: yes.
        :rtype: bool
        """
        return self._DisableWanIp

    @DisableWanIp.setter
    def DisableWanIp(self, DisableWanIp):
        self._DisableWanIp = DisableWanIp


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._DisableWanIp = params.get("DisableWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleDisableWanIpResponse(AbstractModel):
    """ModifyModuleDisableWanIp response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyModuleImageRequest(AbstractModel):
    """ModifyModuleImage request structure.

    """

    def __init__(self):
        r"""
        :param _DefaultImageId: Default image ID
        :type DefaultImageId: str
        :param _ModuleId: Module ID
        :type ModuleId: str
        """
        self._DefaultImageId = None
        self._ModuleId = None

    @property
    def DefaultImageId(self):
        """Default image ID
        :rtype: str
        """
        return self._DefaultImageId

    @DefaultImageId.setter
    def DefaultImageId(self, DefaultImageId):
        self._DefaultImageId = DefaultImageId

    @property
    def ModuleId(self):
        """Module ID
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId


    def _deserialize(self, params):
        self._DefaultImageId = params.get("DefaultImageId")
        self._ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleImageResponse(AbstractModel):
    """ModifyModuleImage response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyModuleIpDirectRequest(AbstractModel):
    """ModifyModuleIpDirect request structure.

    """

    def __init__(self):
        r"""
        :param _ModuleId: Module ID.
        :type ModuleId: str
        :param _CloseIpDirect: Whether to disable IP direct access. Valid values:
true: yes
false: no
        :type CloseIpDirect: bool
        """
        self._ModuleId = None
        self._CloseIpDirect = None

    @property
    def ModuleId(self):
        """Module ID.
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def CloseIpDirect(self):
        """Whether to disable IP direct access. Valid values:
true: yes
false: no
        :rtype: bool
        """
        return self._CloseIpDirect

    @CloseIpDirect.setter
    def CloseIpDirect(self, CloseIpDirect):
        self._CloseIpDirect = CloseIpDirect


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._CloseIpDirect = params.get("CloseIpDirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleIpDirectResponse(AbstractModel):
    """ModifyModuleIpDirect response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyModuleNameRequest(AbstractModel):
    """ModifyModuleName request structure.

    """

    def __init__(self):
        r"""
        :param _ModuleId: Module ID.
        :type ModuleId: str
        :param _ModuleName: Module name.
        :type ModuleName: str
        """
        self._ModuleId = None
        self._ModuleName = None

    @property
    def ModuleId(self):
        """Module ID.
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def ModuleName(self):
        """Module name.
        :rtype: str
        """
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleNameResponse(AbstractModel):
    """ModifyModuleName response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyModuleNetworkRequest(AbstractModel):
    """ModifyModuleNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _ModuleId: Module ID
        :type ModuleId: str
        :param _DefaultBandwidth: Default outbound bandwidth cap
        :type DefaultBandwidth: int
        :param _DefaultBandwidthIn: Default inbound bandwidth cap
        :type DefaultBandwidthIn: int
        """
        self._ModuleId = None
        self._DefaultBandwidth = None
        self._DefaultBandwidthIn = None

    @property
    def ModuleId(self):
        """Module ID
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def DefaultBandwidth(self):
        """Default outbound bandwidth cap
        :rtype: int
        """
        return self._DefaultBandwidth

    @DefaultBandwidth.setter
    def DefaultBandwidth(self, DefaultBandwidth):
        self._DefaultBandwidth = DefaultBandwidth

    @property
    def DefaultBandwidthIn(self):
        """Default inbound bandwidth cap
        :rtype: int
        """
        return self._DefaultBandwidthIn

    @DefaultBandwidthIn.setter
    def DefaultBandwidthIn(self, DefaultBandwidthIn):
        self._DefaultBandwidthIn = DefaultBandwidthIn


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._DefaultBandwidth = params.get("DefaultBandwidth")
        self._DefaultBandwidthIn = params.get("DefaultBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleNetworkResponse(AbstractModel):
    """ModifyModuleNetwork response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyModuleSecurityGroupsRequest(AbstractModel):
    """ModifyModuleSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIdSet: List of up to 5 security groups.
        :type SecurityGroupIdSet: list of str
        :param _ModuleId: Module ID.
        :type ModuleId: str
        """
        self._SecurityGroupIdSet = None
        self._ModuleId = None

    @property
    def SecurityGroupIdSet(self):
        """List of up to 5 security groups.
        :rtype: list of str
        """
        return self._SecurityGroupIdSet

    @SecurityGroupIdSet.setter
    def SecurityGroupIdSet(self, SecurityGroupIdSet):
        self._SecurityGroupIdSet = SecurityGroupIdSet

    @property
    def ModuleId(self):
        """Module ID.
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId


    def _deserialize(self, params):
        self._SecurityGroupIdSet = params.get("SecurityGroupIdSet")
        self._ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleSecurityGroupsResponse(AbstractModel):
    """ModifyModuleSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPrivateIpAddressesAttributeRequest(AbstractModel):
    """ModifyPrivateIpAddressesAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param _PrivateIpAddresses: Information of the specified private IP addresses.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param _EcmRegion: Region information of the ECM node, such as `ap-xian-ecm`.
        :type EcmRegion: str
        """
        self._NetworkInterfaceId = None
        self._PrivateIpAddresses = None
        self._EcmRegion = None

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-m6dyj72l`.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def PrivateIpAddresses(self):
        """Information of the specified private IP addresses.
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def EcmRegion(self):
        """Region information of the ECM node, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self._PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddresses.append(obj)
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateIpAddressesAttributeResponse(AbstractModel):
    """ModifyPrivateIpAddressesAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRouteTableAttributeRequest(AbstractModel):
    """ModifyRouteTableAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableId: Route table instance ID, such as `rtb-azd4dt1c`
        :type RouteTableId: str
        :param _RouteTableName: Route table name
        :type RouteTableName: str
        """
        self._RouteTableId = None
        self._RouteTableName = None

    @property
    def RouteTableId(self):
        """Route table instance ID, such as `rtb-azd4dt1c`
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteTableName(self):
        """Route table name
        :rtype: str
        """
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._RouteTableName = params.get("RouteTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRouteTableAttributeResponse(AbstractModel):
    """ModifyRouteTableAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySecurityGroupAttributeRequest(AbstractModel):
    """ModifySecurityGroupAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :type SecurityGroupId: str
        :param _GroupName: Security group name, which can be customized with up to 60 characters.
        :type GroupName: str
        :param _GroupDescription: Security group remarks, which can contain up to 100 characters.
        :type GroupDescription: str
        """
        self._SecurityGroupId = None
        self._GroupName = None
        self._GroupDescription = None

    @property
    def SecurityGroupId(self):
        """Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def GroupName(self):
        """Security group name, which can be customized with up to 60 characters.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupDescription(self):
        """Security group remarks, which can contain up to 100 characters.
        :rtype: str
        """
        return self._GroupDescription

    @GroupDescription.setter
    def GroupDescription(self, GroupDescription):
        self._GroupDescription = GroupDescription


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._GroupName = params.get("GroupName")
        self._GroupDescription = params.get("GroupDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupAttributeResponse(AbstractModel):
    """ModifySecurityGroupAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySecurityGroupPoliciesRequest(AbstractModel):
    """ModifySecurityGroupPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :type SecurityGroupId: str
        :param _SecurityGroupPolicySet: Security group policy set. You must specify both new egress and ingress policies for the `SecurityGroupPolicySet` object. You cannot customize the index (PolicyIndex) of the `SecurityGroupPolicy` object.
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        :param _SortPolicys: Whether security group sorting is supported. `True` indicates yes. If `SortPolicys` doesn't exist or is set to `False`, the security group policy can be modified.
        :type SortPolicys: bool
        """
        self._SecurityGroupId = None
        self._SecurityGroupPolicySet = None
        self._SortPolicys = None

    @property
    def SecurityGroupId(self):
        """Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupPolicySet(self):
        """Security group policy set. You must specify both new egress and ingress policies for the `SecurityGroupPolicySet` object. You cannot customize the index (PolicyIndex) of the `SecurityGroupPolicy` object.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet

    @property
    def SortPolicys(self):
        """Whether security group sorting is supported. `True` indicates yes. If `SortPolicys` doesn't exist or is set to `False`, the security group policy can be modified.
        :rtype: bool
        """
        return self._SortPolicys

    @SortPolicys.setter
    def SortPolicys(self, SortPolicys):
        self._SortPolicys = SortPolicys


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = SecurityGroupPolicySet()
            self._SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self._SortPolicys = params.get("SortPolicys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupPoliciesResponse(AbstractModel):
    """ModifySecurityGroupPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubnetAttributeRequest(AbstractModel):
    """ModifySubnetAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _SubnetId: Subnet instance ID, such as `subnet-pxir56ns`.
        :type SubnetId: str
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _SubnetName: Subnet name, which can contain up to 60 bytes.
        :type SubnetName: str
        :param _EnableBroadcast: Whether to enable broadcast for the subnet.
        :type EnableBroadcast: str
        :param _Tags: Tag key value of the subnet
        :type Tags: list of Tag
        """
        self._SubnetId = None
        self._EcmRegion = None
        self._SubnetName = None
        self._EnableBroadcast = None
        self._Tags = None

    @property
    def SubnetId(self):
        """Subnet instance ID, such as `subnet-pxir56ns`.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def SubnetName(self):
        """Subnet name, which can contain up to 60 bytes.
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def EnableBroadcast(self):
        """Whether to enable broadcast for the subnet.
        :rtype: str
        """
        return self._EnableBroadcast

    @EnableBroadcast.setter
    def EnableBroadcast(self, EnableBroadcast):
        self._EnableBroadcast = EnableBroadcast

    @property
    def Tags(self):
        """Tag key value of the subnet
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._EcmRegion = params.get("EcmRegion")
        self._SubnetName = params.get("SubnetName")
        self._EnableBroadcast = params.get("EnableBroadcast")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubnetAttributeResponse(AbstractModel):
    """ModifySubnetAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _Targets: List of real servers for which to modify the ports
        :type Targets: list of Target
        :param _NewPort: New port of the real server bound to the listener or forwarding rule
        :type NewPort: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Targets = None
        self._NewPort = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        """CLB listener ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        """List of real servers for which to modify the ports
        :rtype: list of Target
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def NewPort(self):
        """New port of the real server bound to the listener or forwarding rule
        :rtype: int
        """
        return self._NewPort

    @NewPort.setter
    def NewPort(self, NewPort):
        self._NewPort = NewPort


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._NewPort = params.get("NewPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetPortResponse(AbstractModel):
    """ModifyTargetPort response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _ListenerId: CLB listener ID
        :type ListenerId: str
        :param _Targets: List of real servers for which to modify the weights
        :type Targets: list of Target
        :param _Weight: New forwarding weight of the real server. Value range: 0-100. Default value: 10. This parameter will not take effect if the `Targets.Weight` parameter is set.
        :type Weight: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Targets = None
        self._Weight = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        """CLB listener ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        """List of real servers for which to modify the weights
        :rtype: list of Target
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def Weight(self):
        """New forwarding weight of the real server. Value range: 0-100. Default value: 10. This parameter will not take effect if the `Targets.Weight` parameter is set.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetWeightResponse(AbstractModel):
    """ModifyTargetWeight response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyVpcAttributeRequest(AbstractModel):
    """ModifyVpcAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC instance ID, such as `vpc-f49l6u0z`.
        :type VpcId: str
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _VpcName: VPC name, which can be customized with up to 60 characters.
        :type VpcName: str
        :param _Tags: Tags
        :type Tags: list of Tag
        :param _Description: VPC description
        :type Description: str
        """
        self._VpcId = None
        self._EcmRegion = None
        self._VpcName = None
        self._Tags = None
        self._Description = None

    @property
    def VpcId(self):
        """VPC instance ID, such as `vpc-f49l6u0z`.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def VpcName(self):
        """VPC name, which can be customized with up to 60 characters.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tags(self):
        """Tags
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Description(self):
        """VPC description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._EcmRegion = params.get("EcmRegion")
        self._VpcName = params.get("VpcName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcAttributeResponse(AbstractModel):
    """ModifyVpcAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Module(AbstractModel):
    """Module information

    """

    def __init__(self):
        r"""
        :param _ModuleId: Module ID.
        :type ModuleId: str
        :param _ModuleName: Module name.
        :type ModuleName: str
        :param _ModuleState: Module status. Valid values:
NORMAL: normal.
DELETING: deleting 
DELETEFAILED: failed to delete.
        :type ModuleState: str
        :param _DefaultSystemDiskSize: Default system disk size.
        :type DefaultSystemDiskSize: int
        :param _DefaultDataDiskSize: Default data disk size.
        :type DefaultDataDiskSize: int
        :param _InstanceTypeConfig: Default model.
        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        :param _DefaultImage: Default image.
        :type DefaultImage: :class:`tencentcloud.ecm.v20190719.models.Image`
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _DefaultBandwidth: Default outbound bandwidth.
        :type DefaultBandwidth: int
        :param _TagSet: Tag set.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param _CloseIpDirect: Whether to disable IP direct access.
        :type CloseIpDirect: int
        :param _SecurityGroupIds: List of default security group IDs.
        :type SecurityGroupIds: list of str
        :param _DefaultBandwidthIn: Default inbound bandwidth.
        :type DefaultBandwidthIn: int
        :param _UserData: Custom script data
        :type UserData: str
        :param _SystemDisk: System disk information.
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param _DataDisks: Data disk information.
        :type DataDisks: list of DataDisk
        """
        self._ModuleId = None
        self._ModuleName = None
        self._ModuleState = None
        self._DefaultSystemDiskSize = None
        self._DefaultDataDiskSize = None
        self._InstanceTypeConfig = None
        self._DefaultImage = None
        self._CreateTime = None
        self._DefaultBandwidth = None
        self._TagSet = None
        self._CloseIpDirect = None
        self._SecurityGroupIds = None
        self._DefaultBandwidthIn = None
        self._UserData = None
        self._SystemDisk = None
        self._DataDisks = None

    @property
    def ModuleId(self):
        """Module ID.
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def ModuleName(self):
        """Module name.
        :rtype: str
        """
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName

    @property
    def ModuleState(self):
        """Module status. Valid values:
NORMAL: normal.
DELETING: deleting 
DELETEFAILED: failed to delete.
        :rtype: str
        """
        return self._ModuleState

    @ModuleState.setter
    def ModuleState(self, ModuleState):
        self._ModuleState = ModuleState

    @property
    def DefaultSystemDiskSize(self):
        """Default system disk size.
        :rtype: int
        """
        return self._DefaultSystemDiskSize

    @DefaultSystemDiskSize.setter
    def DefaultSystemDiskSize(self, DefaultSystemDiskSize):
        self._DefaultSystemDiskSize = DefaultSystemDiskSize

    @property
    def DefaultDataDiskSize(self):
        """Default data disk size.
        :rtype: int
        """
        return self._DefaultDataDiskSize

    @DefaultDataDiskSize.setter
    def DefaultDataDiskSize(self, DefaultDataDiskSize):
        self._DefaultDataDiskSize = DefaultDataDiskSize

    @property
    def InstanceTypeConfig(self):
        """Default model.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        """
        return self._InstanceTypeConfig

    @InstanceTypeConfig.setter
    def InstanceTypeConfig(self, InstanceTypeConfig):
        self._InstanceTypeConfig = InstanceTypeConfig

    @property
    def DefaultImage(self):
        """Default image.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Image`
        """
        return self._DefaultImage

    @DefaultImage.setter
    def DefaultImage(self, DefaultImage):
        self._DefaultImage = DefaultImage

    @property
    def CreateTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DefaultBandwidth(self):
        """Default outbound bandwidth.
        :rtype: int
        """
        return self._DefaultBandwidth

    @DefaultBandwidth.setter
    def DefaultBandwidth(self, DefaultBandwidth):
        self._DefaultBandwidth = DefaultBandwidth

    @property
    def TagSet(self):
        """Tag set.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def CloseIpDirect(self):
        """Whether to disable IP direct access.
        :rtype: int
        """
        return self._CloseIpDirect

    @CloseIpDirect.setter
    def CloseIpDirect(self, CloseIpDirect):
        self._CloseIpDirect = CloseIpDirect

    @property
    def SecurityGroupIds(self):
        """List of default security group IDs.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def DefaultBandwidthIn(self):
        """Default inbound bandwidth.
        :rtype: int
        """
        return self._DefaultBandwidthIn

    @DefaultBandwidthIn.setter
    def DefaultBandwidthIn(self, DefaultBandwidthIn):
        self._DefaultBandwidthIn = DefaultBandwidthIn

    @property
    def UserData(self):
        """Custom script data
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def SystemDisk(self):
        """System disk information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """Data disk information.
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._ModuleName = params.get("ModuleName")
        self._ModuleState = params.get("ModuleState")
        self._DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self._DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        if params.get("InstanceTypeConfig") is not None:
            self._InstanceTypeConfig = InstanceTypeConfig()
            self._InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        if params.get("DefaultImage") is not None:
            self._DefaultImage = Image()
            self._DefaultImage._deserialize(params.get("DefaultImage"))
        self._CreateTime = params.get("CreateTime")
        self._DefaultBandwidth = params.get("DefaultBandwidth")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._CloseIpDirect = params.get("CloseIpDirect")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._DefaultBandwidthIn = params.get("DefaultBandwidthIn")
        self._UserData = params.get("UserData")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModuleCounter(AbstractModel):
    """Node statistics

    """

    def __init__(self):
        r"""
        :param _ISPCounterSet: ISP statistics list
        :type ISPCounterSet: list of ISPCounter
        :param _ProvinceNum: Number of provinces/states
        :type ProvinceNum: int
        :param _CityNum: Number of cities
        :type CityNum: int
        :param _NodeNum: Number of nodes
        :type NodeNum: int
        :param _InstanceNum: Number of instances
        :type InstanceNum: int
        """
        self._ISPCounterSet = None
        self._ProvinceNum = None
        self._CityNum = None
        self._NodeNum = None
        self._InstanceNum = None

    @property
    def ISPCounterSet(self):
        """ISP statistics list
        :rtype: list of ISPCounter
        """
        return self._ISPCounterSet

    @ISPCounterSet.setter
    def ISPCounterSet(self, ISPCounterSet):
        self._ISPCounterSet = ISPCounterSet

    @property
    def ProvinceNum(self):
        """Number of provinces/states
        :rtype: int
        """
        return self._ProvinceNum

    @ProvinceNum.setter
    def ProvinceNum(self, ProvinceNum):
        self._ProvinceNum = ProvinceNum

    @property
    def CityNum(self):
        """Number of cities
        :rtype: int
        """
        return self._CityNum

    @CityNum.setter
    def CityNum(self, CityNum):
        self._CityNum = CityNum

    @property
    def NodeNum(self):
        """Number of nodes
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def InstanceNum(self):
        """Number of instances
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum


    def _deserialize(self, params):
        if params.get("ISPCounterSet") is not None:
            self._ISPCounterSet = []
            for item in params.get("ISPCounterSet"):
                obj = ISPCounter()
                obj._deserialize(item)
                self._ISPCounterSet.append(obj)
        self._ProvinceNum = params.get("ProvinceNum")
        self._CityNum = params.get("CityNum")
        self._NodeNum = params.get("NodeNum")
        self._InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModuleItem(AbstractModel):
    """Item information of the module list

    """

    def __init__(self):
        r"""
        :param _NodeInstanceNum: Instance statistics of the node
        :type NodeInstanceNum: :class:`tencentcloud.ecm.v20190719.models.NodeInstanceNum`
        :param _Module: Module information
        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`
        """
        self._NodeInstanceNum = None
        self._Module = None

    @property
    def NodeInstanceNum(self):
        """Instance statistics of the node
        :rtype: :class:`tencentcloud.ecm.v20190719.models.NodeInstanceNum`
        """
        return self._NodeInstanceNum

    @NodeInstanceNum.setter
    def NodeInstanceNum(self, NodeInstanceNum):
        self._NodeInstanceNum = NodeInstanceNum

    @property
    def Module(self):
        """Module information
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Module`
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module


    def _deserialize(self, params):
        if params.get("NodeInstanceNum") is not None:
            self._NodeInstanceNum = NodeInstanceNum()
            self._NodeInstanceNum._deserialize(params.get("NodeInstanceNum"))
        if params.get("Module") is not None:
            self._Module = Module()
            self._Module._deserialize(params.get("Module"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonthNetwork(AbstractModel):
    """Bandwidth information of the corresponding month

    """

    def __init__(self):
        r"""
        :param _ZoneInfo: Zone information of the node
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param _Month: Bandwidth month, such as `202103`
        :type Month: str
        :param _BandwidthPkgId: Bandwidth package ID format, such as `bwp-xxxxxxxx`
        :type BandwidthPkgId: str
        :param _Isp: ISP abbreviation. Valid values: CUCC, CTCC, CMCC
        :type Isp: str
        :param _TrafficMaxIn: Inbound bandwidth package peak. Value range: 0.0–xxx.xxx
        :type TrafficMaxIn: float
        :param _TrafficMaxOut: Outbound bandwidth package peak. Value range: 0.0–xxx.xxx
        :type TrafficMaxOut: float
        :param _FeeTraffic: Billable bandwidth. Value range: 0.0–xxx.xxx
        :type FeeTraffic: float
        :param _StartTime: Start time of the monthly billable bandwidth in the format of `yyyy-mm-dd HH:mm:ss`
        :type StartTime: str
        :param _EndTime: End time of the monthly billable bandwidth in the format of `yyyy-mm-dd HH:mm:ss`
        :type EndTime: str
        :param _EffectiveDays: Number of actual valid days for the monthly billable bandwidth, which must be an integer greater than or equal to 0
        :type EffectiveDays: int
        :param _MonthDays: Actual number of days in the specified month, such as 30
        :type MonthDays: int
        :param _EffectiveDaysRate: Proportion of the number of valid days, accurate to four decimal places, such as `0.2134`
        :type EffectiveDaysRate: float
        :param _BandwidthPkgType: Billable bandwidth package type. Valid values: Address, LoadBalance, AddressIpv6
        :type BandwidthPkgType: str
        """
        self._ZoneInfo = None
        self._Month = None
        self._BandwidthPkgId = None
        self._Isp = None
        self._TrafficMaxIn = None
        self._TrafficMaxOut = None
        self._FeeTraffic = None
        self._StartTime = None
        self._EndTime = None
        self._EffectiveDays = None
        self._MonthDays = None
        self._EffectiveDaysRate = None
        self._BandwidthPkgType = None

    @property
    def ZoneInfo(self):
        """Zone information of the node
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        """
        return self._ZoneInfo

    @ZoneInfo.setter
    def ZoneInfo(self, ZoneInfo):
        self._ZoneInfo = ZoneInfo

    @property
    def Month(self):
        """Bandwidth month, such as `202103`
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def BandwidthPkgId(self):
        """Bandwidth package ID format, such as `bwp-xxxxxxxx`
        :rtype: str
        """
        return self._BandwidthPkgId

    @BandwidthPkgId.setter
    def BandwidthPkgId(self, BandwidthPkgId):
        self._BandwidthPkgId = BandwidthPkgId

    @property
    def Isp(self):
        """ISP abbreviation. Valid values: CUCC, CTCC, CMCC
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def TrafficMaxIn(self):
        """Inbound bandwidth package peak. Value range: 0.0–xxx.xxx
        :rtype: float
        """
        return self._TrafficMaxIn

    @TrafficMaxIn.setter
    def TrafficMaxIn(self, TrafficMaxIn):
        self._TrafficMaxIn = TrafficMaxIn

    @property
    def TrafficMaxOut(self):
        """Outbound bandwidth package peak. Value range: 0.0–xxx.xxx
        :rtype: float
        """
        return self._TrafficMaxOut

    @TrafficMaxOut.setter
    def TrafficMaxOut(self, TrafficMaxOut):
        self._TrafficMaxOut = TrafficMaxOut

    @property
    def FeeTraffic(self):
        """Billable bandwidth. Value range: 0.0–xxx.xxx
        :rtype: float
        """
        return self._FeeTraffic

    @FeeTraffic.setter
    def FeeTraffic(self, FeeTraffic):
        self._FeeTraffic = FeeTraffic

    @property
    def StartTime(self):
        """Start time of the monthly billable bandwidth in the format of `yyyy-mm-dd HH:mm:ss`
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the monthly billable bandwidth in the format of `yyyy-mm-dd HH:mm:ss`
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def EffectiveDays(self):
        """Number of actual valid days for the monthly billable bandwidth, which must be an integer greater than or equal to 0
        :rtype: int
        """
        return self._EffectiveDays

    @EffectiveDays.setter
    def EffectiveDays(self, EffectiveDays):
        self._EffectiveDays = EffectiveDays

    @property
    def MonthDays(self):
        """Actual number of days in the specified month, such as 30
        :rtype: int
        """
        return self._MonthDays

    @MonthDays.setter
    def MonthDays(self, MonthDays):
        self._MonthDays = MonthDays

    @property
    def EffectiveDaysRate(self):
        """Proportion of the number of valid days, accurate to four decimal places, such as `0.2134`
        :rtype: float
        """
        return self._EffectiveDaysRate

    @EffectiveDaysRate.setter
    def EffectiveDaysRate(self, EffectiveDaysRate):
        self._EffectiveDaysRate = EffectiveDaysRate

    @property
    def BandwidthPkgType(self):
        """Billable bandwidth package type. Valid values: Address, LoadBalance, AddressIpv6
        :rtype: str
        """
        return self._BandwidthPkgType

    @BandwidthPkgType.setter
    def BandwidthPkgType(self, BandwidthPkgType):
        self._BandwidthPkgType = BandwidthPkgType


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self._ZoneInfo = ZoneInfo()
            self._ZoneInfo._deserialize(params.get("ZoneInfo"))
        self._Month = params.get("Month")
        self._BandwidthPkgId = params.get("BandwidthPkgId")
        self._Isp = params.get("Isp")
        self._TrafficMaxIn = params.get("TrafficMaxIn")
        self._TrafficMaxOut = params.get("TrafficMaxOut")
        self._FeeTraffic = params.get("FeeTraffic")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._EffectiveDays = params.get("EffectiveDays")
        self._MonthDays = params.get("MonthDays")
        self._EffectiveDaysRate = params.get("EffectiveDaysRate")
        self._BandwidthPkgType = params.get("BandwidthPkgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkInterface(AbstractModel):
    """ENI

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-f1xjkw1b`.
        :type NetworkInterfaceId: str
        :param _NetworkInterfaceName: ENI name.
        :type NetworkInterfaceName: str
        :param _NetworkInterfaceDescription: ENI description.
        :type NetworkInterfaceDescription: str
        :param _SubnetId: Subnet instance ID.
        :type SubnetId: str
        :param _VpcId: VPC instance ID.
        :type VpcId: str
        :param _GroupSet: Bound security groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupSet: list of str
        :param _Primary: Whether it is the primary ENI.
        :type Primary: bool
        :param _MacAddress: MAC address.
        :type MacAddress: str
        :param _State: ENI status:
PENDING: creating
AVAILABLE: available
ATTACHING: binding
DETACHING: unbinding
DELETING: deleting
        :type State: str
        :param _PrivateIpAddressSet: Private IP information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param _Attachment: Bound CVM object.
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Attachment: :class:`tencentcloud.ecm.v20190719.models.NetworkInterfaceAttachment`
        :param _Zone: AZ.
        :type Zone: str
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _Ipv6AddressSet: List of IPv6 addresses.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ipv6AddressSet: list of Ipv6Address
        :param _TagSet: Tag key-value pairs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param _EniType: ENI type. Valid values: 0: ENI; 1: EVM ENI.
        :type EniType: int
        :param _EcmRegion: ECM region (EcmRegion)
        :type EcmRegion: str
        :param _Business: Type of the resource bound with an ENI. Valid values: `cvm` and `eks`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Business: str
        """
        self._NetworkInterfaceId = None
        self._NetworkInterfaceName = None
        self._NetworkInterfaceDescription = None
        self._SubnetId = None
        self._VpcId = None
        self._GroupSet = None
        self._Primary = None
        self._MacAddress = None
        self._State = None
        self._PrivateIpAddressSet = None
        self._Attachment = None
        self._Zone = None
        self._CreatedTime = None
        self._Ipv6AddressSet = None
        self._TagSet = None
        self._EniType = None
        self._EcmRegion = None
        self._Business = None

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-f1xjkw1b`.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def NetworkInterfaceName(self):
        """ENI name.
        :rtype: str
        """
        return self._NetworkInterfaceName

    @NetworkInterfaceName.setter
    def NetworkInterfaceName(self, NetworkInterfaceName):
        self._NetworkInterfaceName = NetworkInterfaceName

    @property
    def NetworkInterfaceDescription(self):
        """ENI description.
        :rtype: str
        """
        return self._NetworkInterfaceDescription

    @NetworkInterfaceDescription.setter
    def NetworkInterfaceDescription(self, NetworkInterfaceDescription):
        self._NetworkInterfaceDescription = NetworkInterfaceDescription

    @property
    def SubnetId(self):
        """Subnet instance ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        """VPC instance ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def GroupSet(self):
        """Bound security groups.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

    @property
    def Primary(self):
        """Whether it is the primary ENI.
        :rtype: bool
        """
        return self._Primary

    @Primary.setter
    def Primary(self, Primary):
        self._Primary = Primary

    @property
    def MacAddress(self):
        """MAC address.
        :rtype: str
        """
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def State(self):
        """ENI status:
PENDING: creating
AVAILABLE: available
ATTACHING: binding
DETACHING: unbinding
DELETING: deleting
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def PrivateIpAddressSet(self):
        """Private IP information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddressSet

    @PrivateIpAddressSet.setter
    def PrivateIpAddressSet(self, PrivateIpAddressSet):
        self._PrivateIpAddressSet = PrivateIpAddressSet

    @property
    def Attachment(self):
        """Bound CVM object.
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.NetworkInterfaceAttachment`
        """
        return self._Attachment

    @Attachment.setter
    def Attachment(self, Attachment):
        self._Attachment = Attachment

    @property
    def Zone(self):
        """AZ.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CreatedTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Ipv6AddressSet(self):
        """List of IPv6 addresses.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Ipv6Address
        """
        return self._Ipv6AddressSet

    @Ipv6AddressSet.setter
    def Ipv6AddressSet(self, Ipv6AddressSet):
        self._Ipv6AddressSet = Ipv6AddressSet

    @property
    def TagSet(self):
        """Tag key-value pairs.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def EniType(self):
        """ENI type. Valid values: 0: ENI; 1: EVM ENI.
        :rtype: int
        """
        return self._EniType

    @EniType.setter
    def EniType(self, EniType):
        self._EniType = EniType

    @property
    def EcmRegion(self):
        """ECM region (EcmRegion)
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Business(self):
        """Type of the resource bound with an ENI. Valid values: `cvm` and `eks`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._NetworkInterfaceName = params.get("NetworkInterfaceName")
        self._NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._GroupSet = params.get("GroupSet")
        self._Primary = params.get("Primary")
        self._MacAddress = params.get("MacAddress")
        self._State = params.get("State")
        if params.get("PrivateIpAddressSet") is not None:
            self._PrivateIpAddressSet = []
            for item in params.get("PrivateIpAddressSet"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddressSet.append(obj)
        if params.get("Attachment") is not None:
            self._Attachment = NetworkInterfaceAttachment()
            self._Attachment._deserialize(params.get("Attachment"))
        self._Zone = params.get("Zone")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("Ipv6AddressSet") is not None:
            self._Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6AddressSet.append(obj)
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._EniType = params.get("EniType")
        self._EcmRegion = params.get("EcmRegion")
        self._Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkInterfaceAttachment(AbstractModel):
    """Binding relationship of the ENI

    """

    def __init__(self):
        r"""
        :param _InstanceId: CVM instance ID.
        :type InstanceId: str
        :param _DeviceIndex: Serial number of the ENI in the CVM instance.
        :type DeviceIndex: int
        :param _InstanceAccountId: Account information of the CVM instance owner.
        :type InstanceAccountId: str
        :param _AttachTime: Binding time.
        :type AttachTime: str
        """
        self._InstanceId = None
        self._DeviceIndex = None
        self._InstanceAccountId = None
        self._AttachTime = None

    @property
    def InstanceId(self):
        """CVM instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceIndex(self):
        """Serial number of the ENI in the CVM instance.
        :rtype: int
        """
        return self._DeviceIndex

    @DeviceIndex.setter
    def DeviceIndex(self, DeviceIndex):
        self._DeviceIndex = DeviceIndex

    @property
    def InstanceAccountId(self):
        """Account information of the CVM instance owner.
        :rtype: str
        """
        return self._InstanceAccountId

    @InstanceAccountId.setter
    def InstanceAccountId(self, InstanceAccountId):
        self._InstanceAccountId = InstanceAccountId

    @property
    def AttachTime(self):
        """Binding time.
        :rtype: str
        """
        return self._AttachTime

    @AttachTime.setter
    def AttachTime(self, AttachTime):
        self._AttachTime = AttachTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DeviceIndex = params.get("DeviceIndex")
        self._InstanceAccountId = params.get("InstanceAccountId")
        self._AttachTime = params.get("AttachTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkStorageRange(AbstractModel):
    """Upper and lower limits of the disk

    """

    def __init__(self):
        r"""
        :param _MaxBandwidth: Network bandwidth cap
        :type MaxBandwidth: int
        :param _MaxSystemDiskSize: Upper limit of the data disk size
        :type MaxSystemDiskSize: int
        :param _MinBandwidth: Lower limit of the network bandwidth
        :type MinBandwidth: int
        :param _MinSystemDiskSize: Lower limit of the data disk size
        :type MinSystemDiskSize: int
        :param _MaxDataDiskSize: Maximum data disk size
        :type MaxDataDiskSize: int
        :param _MinDataDiskSize: Minimum data disk size
        :type MinDataDiskSize: int
        :param _SuggestBandwidth: Suggested bandwidth
        :type SuggestBandwidth: int
        :param _SuggestDataDiskSize: Suggested disk size
        :type SuggestDataDiskSize: int
        :param _SuggestSystemDiskSize: Suggested system disk size
        :type SuggestSystemDiskSize: int
        :param _MaxVcpu: Peak number of CPU cores
        :type MaxVcpu: int
        :param _MinVcpu: Minimum number of CPU cores
        :type MinVcpu: int
        :param _MaxVcpuPerReq: Maximum number of CPU cores per request
        :type MaxVcpuPerReq: int
        :param _PerBandwidth: Bandwidth increment
        :type PerBandwidth: int
        :param _PerDataDisk: Data disk increment
        :type PerDataDisk: int
        :param _MaxModuleNum: Total number of modules
        :type MaxModuleNum: int
        """
        self._MaxBandwidth = None
        self._MaxSystemDiskSize = None
        self._MinBandwidth = None
        self._MinSystemDiskSize = None
        self._MaxDataDiskSize = None
        self._MinDataDiskSize = None
        self._SuggestBandwidth = None
        self._SuggestDataDiskSize = None
        self._SuggestSystemDiskSize = None
        self._MaxVcpu = None
        self._MinVcpu = None
        self._MaxVcpuPerReq = None
        self._PerBandwidth = None
        self._PerDataDisk = None
        self._MaxModuleNum = None

    @property
    def MaxBandwidth(self):
        """Network bandwidth cap
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def MaxSystemDiskSize(self):
        """Upper limit of the data disk size
        :rtype: int
        """
        return self._MaxSystemDiskSize

    @MaxSystemDiskSize.setter
    def MaxSystemDiskSize(self, MaxSystemDiskSize):
        self._MaxSystemDiskSize = MaxSystemDiskSize

    @property
    def MinBandwidth(self):
        """Lower limit of the network bandwidth
        :rtype: int
        """
        return self._MinBandwidth

    @MinBandwidth.setter
    def MinBandwidth(self, MinBandwidth):
        self._MinBandwidth = MinBandwidth

    @property
    def MinSystemDiskSize(self):
        """Lower limit of the data disk size
        :rtype: int
        """
        return self._MinSystemDiskSize

    @MinSystemDiskSize.setter
    def MinSystemDiskSize(self, MinSystemDiskSize):
        self._MinSystemDiskSize = MinSystemDiskSize

    @property
    def MaxDataDiskSize(self):
        """Maximum data disk size
        :rtype: int
        """
        return self._MaxDataDiskSize

    @MaxDataDiskSize.setter
    def MaxDataDiskSize(self, MaxDataDiskSize):
        self._MaxDataDiskSize = MaxDataDiskSize

    @property
    def MinDataDiskSize(self):
        """Minimum data disk size
        :rtype: int
        """
        return self._MinDataDiskSize

    @MinDataDiskSize.setter
    def MinDataDiskSize(self, MinDataDiskSize):
        self._MinDataDiskSize = MinDataDiskSize

    @property
    def SuggestBandwidth(self):
        """Suggested bandwidth
        :rtype: int
        """
        return self._SuggestBandwidth

    @SuggestBandwidth.setter
    def SuggestBandwidth(self, SuggestBandwidth):
        self._SuggestBandwidth = SuggestBandwidth

    @property
    def SuggestDataDiskSize(self):
        """Suggested disk size
        :rtype: int
        """
        return self._SuggestDataDiskSize

    @SuggestDataDiskSize.setter
    def SuggestDataDiskSize(self, SuggestDataDiskSize):
        self._SuggestDataDiskSize = SuggestDataDiskSize

    @property
    def SuggestSystemDiskSize(self):
        """Suggested system disk size
        :rtype: int
        """
        return self._SuggestSystemDiskSize

    @SuggestSystemDiskSize.setter
    def SuggestSystemDiskSize(self, SuggestSystemDiskSize):
        self._SuggestSystemDiskSize = SuggestSystemDiskSize

    @property
    def MaxVcpu(self):
        """Peak number of CPU cores
        :rtype: int
        """
        return self._MaxVcpu

    @MaxVcpu.setter
    def MaxVcpu(self, MaxVcpu):
        self._MaxVcpu = MaxVcpu

    @property
    def MinVcpu(self):
        """Minimum number of CPU cores
        :rtype: int
        """
        return self._MinVcpu

    @MinVcpu.setter
    def MinVcpu(self, MinVcpu):
        self._MinVcpu = MinVcpu

    @property
    def MaxVcpuPerReq(self):
        """Maximum number of CPU cores per request
        :rtype: int
        """
        return self._MaxVcpuPerReq

    @MaxVcpuPerReq.setter
    def MaxVcpuPerReq(self, MaxVcpuPerReq):
        self._MaxVcpuPerReq = MaxVcpuPerReq

    @property
    def PerBandwidth(self):
        """Bandwidth increment
        :rtype: int
        """
        return self._PerBandwidth

    @PerBandwidth.setter
    def PerBandwidth(self, PerBandwidth):
        self._PerBandwidth = PerBandwidth

    @property
    def PerDataDisk(self):
        """Data disk increment
        :rtype: int
        """
        return self._PerDataDisk

    @PerDataDisk.setter
    def PerDataDisk(self, PerDataDisk):
        self._PerDataDisk = PerDataDisk

    @property
    def MaxModuleNum(self):
        """Total number of modules
        :rtype: int
        """
        return self._MaxModuleNum

    @MaxModuleNum.setter
    def MaxModuleNum(self, MaxModuleNum):
        self._MaxModuleNum = MaxModuleNum


    def _deserialize(self, params):
        self._MaxBandwidth = params.get("MaxBandwidth")
        self._MaxSystemDiskSize = params.get("MaxSystemDiskSize")
        self._MinBandwidth = params.get("MinBandwidth")
        self._MinSystemDiskSize = params.get("MinSystemDiskSize")
        self._MaxDataDiskSize = params.get("MaxDataDiskSize")
        self._MinDataDiskSize = params.get("MinDataDiskSize")
        self._SuggestBandwidth = params.get("SuggestBandwidth")
        self._SuggestDataDiskSize = params.get("SuggestDataDiskSize")
        self._SuggestSystemDiskSize = params.get("SuggestSystemDiskSize")
        self._MaxVcpu = params.get("MaxVcpu")
        self._MinVcpu = params.get("MinVcpu")
        self._MaxVcpuPerReq = params.get("MaxVcpuPerReq")
        self._PerBandwidth = params.get("PerBandwidth")
        self._PerDataDisk = params.get("PerDataDisk")
        self._MaxModuleNum = params.get("MaxModuleNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Node(AbstractModel):
    """Node information

    """

    def __init__(self):
        r"""
        :param _ZoneInfo: Zone information.
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param _Country: Country/Region information.
        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`
        :param _Area: Region information.
        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`
        :param _Province: Province/State information.
        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`
        :param _City: City information.
        :type City: :class:`tencentcloud.ecm.v20190719.models.City`
        :param _RegionInfo: Region information.
        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        :param _ISPSet: List of ISPs.
        :type ISPSet: list of ISP
        :param _ISPNum: Number of ISPs.
        :type ISPNum: int
        """
        self._ZoneInfo = None
        self._Country = None
        self._Area = None
        self._Province = None
        self._City = None
        self._RegionInfo = None
        self._ISPSet = None
        self._ISPNum = None

    @property
    def ZoneInfo(self):
        """Zone information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        """
        return self._ZoneInfo

    @ZoneInfo.setter
    def ZoneInfo(self, ZoneInfo):
        self._ZoneInfo = ZoneInfo

    @property
    def Country(self):
        """Country/Region information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Country`
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Area(self):
        """Region information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Area`
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Province(self):
        """Province/State information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Province`
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """City information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.City`
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def RegionInfo(self):
        """Region information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        """
        return self._RegionInfo

    @RegionInfo.setter
    def RegionInfo(self, RegionInfo):
        self._RegionInfo = RegionInfo

    @property
    def ISPSet(self):
        """List of ISPs.
        :rtype: list of ISP
        """
        return self._ISPSet

    @ISPSet.setter
    def ISPSet(self, ISPSet):
        self._ISPSet = ISPSet

    @property
    def ISPNum(self):
        """Number of ISPs.
        :rtype: int
        """
        return self._ISPNum

    @ISPNum.setter
    def ISPNum(self, ISPNum):
        self._ISPNum = ISPNum


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self._ZoneInfo = ZoneInfo()
            self._ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self._Country = Country()
            self._Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self._Area = Area()
            self._Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self._Province = Province()
            self._Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self._City = City()
            self._City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self._RegionInfo = RegionInfo()
            self._RegionInfo._deserialize(params.get("RegionInfo"))
        if params.get("ISPSet") is not None:
            self._ISPSet = []
            for item in params.get("ISPSet"):
                obj = ISP()
                obj._deserialize(item)
                self._ISPSet.append(obj)
        self._ISPNum = params.get("ISPNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInstanceNum(AbstractModel):
    """Instance number of the node

    """

    def __init__(self):
        r"""
        :param _NodeNum: Number of nodes
        :type NodeNum: int
        :param _InstanceNum: Number of instances
        :type InstanceNum: int
        """
        self._NodeNum = None
        self._InstanceNum = None

    @property
    def NodeNum(self):
        """Number of nodes
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def InstanceNum(self):
        """Number of instances
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum


    def _deserialize(self, params):
        self._NodeNum = params.get("NodeNum")
        self._InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperatorAction(AbstractModel):
    """Operation (action)

    """

    def __init__(self):
        r"""
        :param _Action: Executable operation
        :type Action: str
        :param _Code: Code
Note: this field may return null, indicating that no valid values can be obtained.
        :type Code: str
        :param _Message: Specific information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Message: str
        """
        self._Action = None
        self._Code = None
        self._Message = None

    @property
    def Action(self):
        """Executable operation
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Code(self):
        """Code
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """Specific information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsVersion(AbstractModel):
    """Supported OS types.

    """

    def __init__(self):
        r"""
        :param _OsName: OS type
        :type OsName: str
        :param _OsVersions: Supported OS versions
Note: this field may return null, indicating that no valid values can be obtained.
        :type OsVersions: list of str
        :param _Architecture: Supported OS architecture
Note: this field may return null, indicating that no valid values can be obtained.
        :type Architecture: list of str
        """
        self._OsName = None
        self._OsVersions = None
        self._Architecture = None

    @property
    def OsName(self):
        """OS type
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def OsVersions(self):
        """Supported OS versions
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._OsVersions

    @OsVersions.setter
    def OsVersions(self, OsVersions):
        self._OsVersions = OsVersions

    @property
    def Architecture(self):
        """Supported OS architecture
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture


    def _deserialize(self, params):
        self._OsName = params.get("OsName")
        self._OsVersions = params.get("OsVersions")
        self._Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackingQuotaGroup(AbstractModel):
    """A set of correlated packing quotas sorted by instance type priority

    """

    def __init__(self):
        r"""
        :param _Zone: AZ
        :type Zone: str
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _ISPId: ISP id
        :type ISPId: str
        :param _PackingQuotaInfos: A set of correlated packing quotas
        :type PackingQuotaInfos: list of PackingQuotaInfo
        """
        self._Zone = None
        self._ZoneId = None
        self._ISPId = None
        self._PackingQuotaInfos = None

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
    def ZoneId(self):
        """AZ ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ISPId(self):
        """ISP id
        :rtype: str
        """
        return self._ISPId

    @ISPId.setter
    def ISPId(self, ISPId):
        self._ISPId = ISPId

    @property
    def PackingQuotaInfos(self):
        """A set of correlated packing quotas
        :rtype: list of PackingQuotaInfo
        """
        return self._PackingQuotaInfos

    @PackingQuotaInfos.setter
    def PackingQuotaInfos(self, PackingQuotaInfos):
        self._PackingQuotaInfos = PackingQuotaInfos


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ISPId = params.get("ISPId")
        if params.get("PackingQuotaInfos") is not None:
            self._PackingQuotaInfos = []
            for item in params.get("PackingQuotaInfos"):
                obj = PackingQuotaInfo()
                obj._deserialize(item)
                self._PackingQuotaInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackingQuotaInfo(AbstractModel):
    """The information of a set of correlated packing quotas

    """

    def __init__(self):
        r"""
        :param _InstanceType: Instance type
        :type InstanceType: str
        :param _PackingQuota: Packing quota
        :type PackingQuota: int
        """
        self._InstanceType = None
        self._PackingQuota = None

    @property
    def InstanceType(self):
        """Instance type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PackingQuota(self):
        """Packing quota
        :rtype: int
        """
        return self._PackingQuota

    @PackingQuota.setter
    def PackingQuota(self, PackingQuota):
        self._PackingQuota = PackingQuota


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._PackingQuota = params.get("PackingQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakBase(AbstractModel):
    """Peak information

    """

    def __init__(self):
        r"""
        :param _PeakCpuNum: Peak CPU
        :type PeakCpuNum: int
        :param _PeakMemoryNum: Peak memory
        :type PeakMemoryNum: int
        :param _PeakStorageNum: Peak disk
        :type PeakStorageNum: int
        :param _RecordTime: Recording time
        :type RecordTime: str
        """
        self._PeakCpuNum = None
        self._PeakMemoryNum = None
        self._PeakStorageNum = None
        self._RecordTime = None

    @property
    def PeakCpuNum(self):
        """Peak CPU
        :rtype: int
        """
        return self._PeakCpuNum

    @PeakCpuNum.setter
    def PeakCpuNum(self, PeakCpuNum):
        self._PeakCpuNum = PeakCpuNum

    @property
    def PeakMemoryNum(self):
        """Peak memory
        :rtype: int
        """
        return self._PeakMemoryNum

    @PeakMemoryNum.setter
    def PeakMemoryNum(self, PeakMemoryNum):
        self._PeakMemoryNum = PeakMemoryNum

    @property
    def PeakStorageNum(self):
        """Peak disk
        :rtype: int
        """
        return self._PeakStorageNum

    @PeakStorageNum.setter
    def PeakStorageNum(self, PeakStorageNum):
        self._PeakStorageNum = PeakStorageNum

    @property
    def RecordTime(self):
        """Recording time
        :rtype: str
        """
        return self._RecordTime

    @RecordTime.setter
    def RecordTime(self, RecordTime):
        self._RecordTime = RecordTime


    def _deserialize(self, params):
        self._PeakCpuNum = params.get("PeakCpuNum")
        self._PeakMemoryNum = params.get("PeakMemoryNum")
        self._PeakStorageNum = params.get("PeakStorageNum")
        self._RecordTime = params.get("RecordTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakFamilyInfo(AbstractModel):
    """PeakFamilyInfo: peak information of data such as CPU by model type

    """

    def __init__(self):
        r"""
        :param _InstanceFamily: Model type information.
        :type InstanceFamily: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        :param _PeakBaseSet: Peak information of basic data.
        :type PeakBaseSet: list of PeakBase
        """
        self._InstanceFamily = None
        self._PeakBaseSet = None

    @property
    def InstanceFamily(self):
        """Model type information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def PeakBaseSet(self):
        """Peak information of basic data.
        :rtype: list of PeakBase
        """
        return self._PeakBaseSet

    @PeakBaseSet.setter
    def PeakBaseSet(self, PeakBaseSet):
        self._PeakBaseSet = PeakBaseSet


    def _deserialize(self, params):
        if params.get("InstanceFamily") is not None:
            self._InstanceFamily = InstanceFamilyTypeConfig()
            self._InstanceFamily._deserialize(params.get("InstanceFamily"))
        if params.get("PeakBaseSet") is not None:
            self._PeakBaseSet = []
            for item in params.get("PeakBaseSet"):
                obj = PeakBase()
                obj._deserialize(item)
                self._PeakBaseSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakNetwork(AbstractModel):
    """Peak network data

    """

    def __init__(self):
        r"""
        :param _RecordTime: Recording time.
        :type RecordTime: str
        :param _PeakInNetwork: Inbound bandwidth data.
        :type PeakInNetwork: str
        :param _PeakOutNetwork: Outbound bandwidth data.
        :type PeakOutNetwork: str
        :param _ChargeNetwork: Billable bandwidth in bps
        :type ChargeNetwork: str
        """
        self._RecordTime = None
        self._PeakInNetwork = None
        self._PeakOutNetwork = None
        self._ChargeNetwork = None

    @property
    def RecordTime(self):
        """Recording time.
        :rtype: str
        """
        return self._RecordTime

    @RecordTime.setter
    def RecordTime(self, RecordTime):
        self._RecordTime = RecordTime

    @property
    def PeakInNetwork(self):
        """Inbound bandwidth data.
        :rtype: str
        """
        return self._PeakInNetwork

    @PeakInNetwork.setter
    def PeakInNetwork(self, PeakInNetwork):
        self._PeakInNetwork = PeakInNetwork

    @property
    def PeakOutNetwork(self):
        """Outbound bandwidth data.
        :rtype: str
        """
        return self._PeakOutNetwork

    @PeakOutNetwork.setter
    def PeakOutNetwork(self, PeakOutNetwork):
        self._PeakOutNetwork = PeakOutNetwork

    @property
    def ChargeNetwork(self):
        """Billable bandwidth in bps
        :rtype: str
        """
        return self._ChargeNetwork

    @ChargeNetwork.setter
    def ChargeNetwork(self, ChargeNetwork):
        self._ChargeNetwork = ChargeNetwork


    def _deserialize(self, params):
        self._RecordTime = params.get("RecordTime")
        self._PeakInNetwork = params.get("PeakInNetwork")
        self._PeakOutNetwork = params.get("PeakOutNetwork")
        self._ChargeNetwork = params.get("ChargeNetwork")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakNetworkRegionInfo(AbstractModel):
    """Peak network information by region

    """

    def __init__(self):
        r"""
        :param _Region: Region information
        :type Region: str
        :param _PeakNetworkSet: Peak network set
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeakNetworkSet: list of PeakNetwork
        """
        self._Region = None
        self._PeakNetworkSet = None

    @property
    def Region(self):
        """Region information
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PeakNetworkSet(self):
        """Peak network set
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of PeakNetwork
        """
        return self._PeakNetworkSet

    @PeakNetworkSet.setter
    def PeakNetworkSet(self, PeakNetworkSet):
        self._PeakNetworkSet = PeakNetworkSet


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("PeakNetworkSet") is not None:
            self._PeakNetworkSet = []
            for item in params.get("PeakNetworkSet"):
                obj = PeakNetwork()
                obj._deserialize(item)
                self._PeakNetworkSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhysicalPosition(AbstractModel):
    """Physical location information

    """

    def __init__(self):
        r"""
        :param _PosId: Rack unit
Note: this field may return null, indicating that no valid values can be obtained.
        :type PosId: str
        :param _RackId: Rack
Note: this field may return null, indicating that no valid values can be obtained.
        :type RackId: str
        :param _SwitchId: Switch
Note: this field may return null, indicating that no valid values can be obtained.
        :type SwitchId: str
        """
        self._PosId = None
        self._RackId = None
        self._SwitchId = None

    @property
    def PosId(self):
        """Rack unit
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PosId

    @PosId.setter
    def PosId(self, PosId):
        self._PosId = PosId

    @property
    def RackId(self):
        """Rack
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RackId

    @RackId.setter
    def RackId(self, RackId):
        self._RackId = RackId

    @property
    def SwitchId(self):
        """Switch
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SwitchId

    @SwitchId.setter
    def SwitchId(self, SwitchId):
        self._SwitchId = SwitchId


    def _deserialize(self, params):
        self._PosId = params.get("PosId")
        self._RackId = params.get("RackId")
        self._SwitchId = params.get("SwitchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """Abstract location of the instance, including its AZ, project, and dedicated cluster ID and name.

    """

    def __init__(self):
        r"""
        :param _Zone: [AZ ID](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) of the cloud disk, which can be obtained from the `Zone` field in the returned value of the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1) API.
        :type Zone: str
        :param _CageId: Cage ID. When it is used as an input parameter, it indicates to manipulate the resources in the cage with the specified `CageId` and can be left empty. When it is used as an output parameter, it represents the cage ID of the resource and can be left empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CageId: str
        :param _ProjectId: Project ID of the instance, which can be obtained from the `projectId` field in the returned value of the [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1) API. If this parameter is not specified, the default project ID will be used.
        :type ProjectId: int
        :param _CdcName: Name of the dedicated cluster. When it is used as an input parameter, it is ignored. When it is used as an output parameter, it represents the name of the dedicated cluster to which the cloud disk belongs, and it can be left empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CdcName: str
        :param _CdcId: Dedicated cluster ID of the instance. When it is used as an input parameter, it indicates to manipulate the resources in the dedicated cluster with the specified `CdcId` and can be left empty. When it is used as an output parameter, it represents the dedicated cluster ID of the resource and can be left empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CdcId: str
        """
        self._Zone = None
        self._CageId = None
        self._ProjectId = None
        self._CdcName = None
        self._CdcId = None

    @property
    def Zone(self):
        """[AZ ID](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) of the cloud disk, which can be obtained from the `Zone` field in the returned value of the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CageId(self):
        """Cage ID. When it is used as an input parameter, it indicates to manipulate the resources in the cage with the specified `CageId` and can be left empty. When it is used as an output parameter, it represents the cage ID of the resource and can be left empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ProjectId(self):
        """Project ID of the instance, which can be obtained from the `projectId` field in the returned value of the [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1) API. If this parameter is not specified, the default project ID will be used.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CdcName(self):
        """Name of the dedicated cluster. When it is used as an input parameter, it is ignored. When it is used as an output parameter, it represents the name of the dedicated cluster to which the cloud disk belongs, and it can be left empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CdcName

    @CdcName.setter
    def CdcName(self, CdcName):
        self._CdcName = CdcName

    @property
    def CdcId(self):
        """Dedicated cluster ID of the instance. When it is used as an input parameter, it indicates to manipulate the resources in the dedicated cluster with the specified `CdcId` and can be left empty. When it is used as an output parameter, it represents the dedicated cluster ID of the resource and can be left empty.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._CageId = params.get("CageId")
        self._ProjectId = params.get("ProjectId")
        self._CdcName = params.get("CdcName")
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Position(AbstractModel):
    """Location information of the instance.

    """

    def __init__(self):
        r"""
        :param _ZoneInfo: Zone information of the instance.
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param _Country: Country/Region information of the instance.
        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`
        :param _Area: Area information of the instance.
        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`
        :param _Province: Province/State information of the instance.
        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`
        :param _City: City information of the instance.
        :type City: :class:`tencentcloud.ecm.v20190719.models.City`
        :param _RegionInfo: Region information of the instance.
        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        """
        self._ZoneInfo = None
        self._Country = None
        self._Area = None
        self._Province = None
        self._City = None
        self._RegionInfo = None

    @property
    def ZoneInfo(self):
        """Zone information of the instance.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        """
        return self._ZoneInfo

    @ZoneInfo.setter
    def ZoneInfo(self, ZoneInfo):
        self._ZoneInfo = ZoneInfo

    @property
    def Country(self):
        """Country/Region information of the instance.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Country`
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Area(self):
        """Area information of the instance.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Area`
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Province(self):
        """Province/State information of the instance.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Province`
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """City information of the instance.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.City`
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def RegionInfo(self):
        """Region information of the instance.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        """
        return self._RegionInfo

    @RegionInfo.setter
    def RegionInfo(self, RegionInfo):
        self._RegionInfo = RegionInfo


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self._ZoneInfo = ZoneInfo()
            self._ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self._Country = Country()
            self._Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self._Area = Area()
            self._Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self._Province = Province()
            self._Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self._City = City()
            self._City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self._RegionInfo = RegionInfo()
            self._RegionInfo._deserialize(params.get("RegionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceDetail(AbstractModel):
    """Prices of CPU, memory, and other resources

    """

    def __init__(self):
        r"""
        :param _Discount: Discount, such as `20`, which represents 80% off
        :type Discount: int
        :param _DiscountPrice: Discounted price in cents
        :type DiscountPrice: int
        :param _OriginalPrice: Original price in cents
        :type OriginalPrice: int
        """
        self._Discount = None
        self._DiscountPrice = None
        self._OriginalPrice = None

    @property
    def Discount(self):
        """Discount, such as `20`, which represents 80% off
        :rtype: int
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        """Discounted price in cents
        :rtype: int
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def OriginalPrice(self):
        """Original price in cents
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice


    def _deserialize(self, params):
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateIPAddressInfo(AbstractModel):
    """Private IP information of the instance.

    """

    def __init__(self):
        r"""
        :param _PrivateIPAddress: Private IP of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateIPAddress: str
        """
        self._PrivateIPAddress = None

    @property
    def PrivateIPAddress(self):
        """Private IP of the instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateIPAddress

    @PrivateIPAddress.setter
    def PrivateIPAddress(self, PrivateIPAddress):
        self._PrivateIPAddress = PrivateIPAddress


    def _deserialize(self, params):
        self._PrivateIPAddress = params.get("PrivateIPAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateIpAddressSpecification(AbstractModel):
    """Private IP information

    """

    def __init__(self):
        r"""
        :param _PrivateIpAddress: Private IP address.
        :type PrivateIpAddress: str
        :param _Primary: Whether it is the primary IP.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Primary: bool
        :param _PublicIpAddress: Public IP address.
        :type PublicIpAddress: str
        :param _AddressId: EIP instance ID, such as `eip-11112222`.
        :type AddressId: str
        :param _Description: Private IP description.
        :type Description: str
        :param _IsWanIpBlocked: Whether the public IP is blocked.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsWanIpBlocked: bool
        :param _State: IP status:
PENDING: generating
MIGRATING: migrating
DELETING: deleting
AVAILABLE: available
        :type State: str
        """
        self._PrivateIpAddress = None
        self._Primary = None
        self._PublicIpAddress = None
        self._AddressId = None
        self._Description = None
        self._IsWanIpBlocked = None
        self._State = None

    @property
    def PrivateIpAddress(self):
        """Private IP address.
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress

    @property
    def Primary(self):
        """Whether it is the primary IP.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Primary

    @Primary.setter
    def Primary(self, Primary):
        self._Primary = Primary

    @property
    def PublicIpAddress(self):
        """Public IP address.
        :rtype: str
        """
        return self._PublicIpAddress

    @PublicIpAddress.setter
    def PublicIpAddress(self, PublicIpAddress):
        self._PublicIpAddress = PublicIpAddress

    @property
    def AddressId(self):
        """EIP instance ID, such as `eip-11112222`.
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def Description(self):
        """Private IP description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsWanIpBlocked(self):
        """Whether the public IP is blocked.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsWanIpBlocked

    @IsWanIpBlocked.setter
    def IsWanIpBlocked(self, IsWanIpBlocked):
        self._IsWanIpBlocked = IsWanIpBlocked

    @property
    def State(self):
        """IP status:
PENDING: generating
MIGRATING: migrating
DELETING: deleting
AVAILABLE: available
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        self._Primary = params.get("Primary")
        self._PublicIpAddress = params.get("PublicIpAddress")
        self._AddressId = params.get("AddressId")
        self._Description = params.get("Description")
        self._IsWanIpBlocked = params.get("IsWanIpBlocked")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Province(AbstractModel):
    """Province/State information

    """

    def __init__(self):
        r"""
        :param _ProvinceId: Province/State ID
        :type ProvinceId: str
        :param _ProvinceName: Province/State name
        :type ProvinceName: str
        """
        self._ProvinceId = None
        self._ProvinceName = None

    @property
    def ProvinceId(self):
        """Province/State ID
        :rtype: str
        """
        return self._ProvinceId

    @ProvinceId.setter
    def ProvinceId(self, ProvinceId):
        self._ProvinceId = ProvinceId

    @property
    def ProvinceName(self):
        """Province/State name
        :rtype: str
        """
        return self._ProvinceName

    @ProvinceName.setter
    def ProvinceName(self, ProvinceName):
        self._ProvinceName = ProvinceName


    def _deserialize(self, params):
        self._ProvinceId = params.get("ProvinceId")
        self._ProvinceName = params.get("ProvinceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicIPAddressInfo(AbstractModel):
    """Public IP information of the instance.

    """

    def __init__(self):
        r"""
        :param _ChargeMode: Billing mode.
        :type ChargeMode: str
        :param _PublicIPAddress: Public IP of the instance.
        :type PublicIPAddress: str
        :param _ISP: Public IP ISP of the instance.
        :type ISP: :class:`tencentcloud.ecm.v20190719.models.ISP`
        :param _MaxBandwidthOut: Outbound bandwidth cap of the instance in Mbps.
        :type MaxBandwidthOut: int
        :param _MaxBandwidthIn: Inbound bandwidth cap of the instance in Mbps.
        :type MaxBandwidthIn: int
        """
        self._ChargeMode = None
        self._PublicIPAddress = None
        self._ISP = None
        self._MaxBandwidthOut = None
        self._MaxBandwidthIn = None

    @property
    def ChargeMode(self):
        """Billing mode.
        :rtype: str
        """
        return self._ChargeMode

    @ChargeMode.setter
    def ChargeMode(self, ChargeMode):
        self._ChargeMode = ChargeMode

    @property
    def PublicIPAddress(self):
        """Public IP of the instance.
        :rtype: str
        """
        return self._PublicIPAddress

    @PublicIPAddress.setter
    def PublicIPAddress(self, PublicIPAddress):
        self._PublicIPAddress = PublicIPAddress

    @property
    def ISP(self):
        """Public IP ISP of the instance.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ISP`
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def MaxBandwidthOut(self):
        """Outbound bandwidth cap of the instance in Mbps.
        :rtype: int
        """
        return self._MaxBandwidthOut

    @MaxBandwidthOut.setter
    def MaxBandwidthOut(self, MaxBandwidthOut):
        self._MaxBandwidthOut = MaxBandwidthOut

    @property
    def MaxBandwidthIn(self):
        """Inbound bandwidth cap of the instance in Mbps.
        :rtype: int
        """
        return self._MaxBandwidthIn

    @MaxBandwidthIn.setter
    def MaxBandwidthIn(self, MaxBandwidthIn):
        self._MaxBandwidthIn = MaxBandwidthIn


    def _deserialize(self, params):
        self._ChargeMode = params.get("ChargeMode")
        self._PublicIPAddress = params.get("PublicIPAddress")
        if params.get("ISP") is not None:
            self._ISP = ISP()
            self._ISP._deserialize(params.get("ISP"))
        self._MaxBandwidthOut = params.get("MaxBandwidthOut")
        self._MaxBandwidthIn = params.get("MaxBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesRequest(AbstractModel):
    """RebootInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of IDs of the instances to be restarted. You can request up to 100 instances in a region at a time.
        :type InstanceIdSet: list of str
        :param _ForceReboot: Whether to force restart the instance after it failed to be restarted normally. Valid values:
TRUE: yes;
FALSE: no;
Default value: FALSE.
        :type ForceReboot: bool
        :param _StopType: Shutdown type. Valid values:
SOFT: soft shutdown
HARD: hard shutdown
SOFT_FIRST: perform a soft shutdown first; if it fails, perform a hard shutdown

Default value: SOFT.
        :type StopType: str
        """
        self._InstanceIdSet = None
        self._ForceReboot = None
        self._StopType = None

    @property
    def InstanceIdSet(self):
        """List of IDs of the instances to be restarted. You can request up to 100 instances in a region at a time.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def ForceReboot(self):
        """Whether to force restart the instance after it failed to be restarted normally. Valid values:
TRUE: yes;
FALSE: no;
Default value: FALSE.
        :rtype: bool
        """
        return self._ForceReboot

    @ForceReboot.setter
    def ForceReboot(self, ForceReboot):
        self._ForceReboot = ForceReboot

    @property
    def StopType(self):
        """Shutdown type. Valid values:
SOFT: soft shutdown
HARD: hard shutdown
SOFT_FIRST: perform a soft shutdown first; if it fails, perform a hard shutdown

Default value: SOFT.
        :rtype: str
        """
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._ForceReboot = params.get("ForceReboot")
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    """RebootInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Region and region name (RegionName)

    """

    def __init__(self):
        r"""
        :param _Region: Region
        :type Region: str
        :param _RegionName: Region name
        :type RegionName: str
        :param _RegionId: RegionID
        :type RegionId: int
        """
        self._Region = None
        self._RegionName = None
        self._RegionId = None

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        """Region name
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        """RegionID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseAddressesRequest(AbstractModel):
    """ReleaseAddresses request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _AddressIds: List of unique IDs of EIPs.
        :type AddressIds: list of str
        """
        self._EcmRegion = None
        self._AddressIds = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressIds(self):
        """List of unique IDs of EIPs.
        :rtype: list of str
        """
        return self._AddressIds

    @AddressIds.setter
    def AddressIds(self, AddressIds):
        self._AddressIds = AddressIds


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressIds = params.get("AddressIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseAddressesResponse(AbstractModel):
    """ReleaseAddresses response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Async task ID (TaskId). You can use the `DescribeTaskResult` API to query the task status.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ReleaseIpv6AddressesRequest(AbstractModel):
    """ReleaseIpv6Addresses request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-m6dyj72l`.
        :type NetworkInterfaceId: str
        :param _Ipv6Addresses: List of the specified IPv6 addresses. You can specify up to 10 IPv6 addresses at a time.
        :type Ipv6Addresses: list of Ipv6Address
        """
        self._EcmRegion = None
        self._NetworkInterfaceId = None
        self._Ipv6Addresses = None

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-m6dyj72l`.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def Ipv6Addresses(self):
        """List of the specified IPv6 addresses. You can specify up to 10 IPv6 addresses at a time.
        :rtype: list of Ipv6Address
        """
        return self._Ipv6Addresses

    @Ipv6Addresses.setter
    def Ipv6Addresses(self, Ipv6Addresses):
        self._Ipv6Addresses = Ipv6Addresses


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self._Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6Addresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIpv6AddressesResponse(AbstractModel):
    """ReleaseIpv6Addresses response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID. You can use the `DescribeTaskResult` API to query the task status
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Task ID. You can use the `DescribeTaskResult` API to query the task status
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class RemovePrivateIpAddressesRequest(AbstractModel):
    """RemovePrivateIpAddresses request structure.

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM region, such as `ap-xian-ecm`.
        :type EcmRegion: str
        :param _NetworkInterfaceId: ENI instance ID, such as `eni-11112222`.
        :type NetworkInterfaceId: str
        :param _PrivateIpAddresses: Information of the specified private IPs. You can specify up to 10 IPs at a time.
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self._EcmRegion = None
        self._NetworkInterfaceId = None
        self._PrivateIpAddresses = None

    @property
    def EcmRegion(self):
        """ECM region, such as `ap-xian-ecm`.
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceId(self):
        """ENI instance ID, such as `eni-11112222`.
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def PrivateIpAddresses(self):
        """Information of the specified private IPs. You can specify up to 10 IPs at a time.
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self._PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemovePrivateIpAddressesResponse(AbstractModel):
    """RemovePrivateIpAddresses response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReplaceRouteTableAssociationRequest(AbstractModel):
    """ReplaceRouteTableAssociation request structure.

    """

    def __init__(self):
        r"""
        :param _SubnetId: Subnet instance ID, such as `subnet-3x5lf5q0`, which can be queried through the `DescribeSubnets` API.
        :type SubnetId: str
        :param _RouteTableId: Route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        :param _EcmRegion: ECM region
        :type EcmRegion: str
        """
        self._SubnetId = None
        self._RouteTableId = None
        self._EcmRegion = None

    @property
    def SubnetId(self):
        """Subnet instance ID, such as `subnet-3x5lf5q0`, which can be queried through the `DescribeSubnets` API.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def RouteTableId(self):
        """Route table instance ID, such as `rtb-azd4dt1c`.
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def EcmRegion(self):
        """ECM region
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._RouteTableId = params.get("RouteTableId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceRouteTableAssociationResponse(AbstractModel):
    """ReplaceRouteTableAssociation response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReplaceRoutesRequest(AbstractModel):
    """ReplaceRoutes request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableId: Route table instance ID.
        :type RouteTableId: str
        :param _Routes: Routing policy object.
        :type Routes: list of Route
        """
        self._RouteTableId = None
        self._Routes = None

    @property
    def RouteTableId(self):
        """Route table instance ID.
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def Routes(self):
        """Routing policy object.
        :rtype: list of Route
        """
        return self._Routes

    @Routes.setter
    def Routes(self, Routes):
        self._Routes = Routes


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self._Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self._Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceRoutesResponse(AbstractModel):
    """ReplaceRoutes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReplaceSecurityGroupPolicyRequest(AbstractModel):
    """ReplaceSecurityGroupPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API
        :type SecurityGroupId: str
        :param _SecurityGroupPolicySet: Security group policy set object.
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        self._SecurityGroupId = None
        self._SecurityGroupPolicySet = None

    @property
    def SecurityGroupId(self):
        """Security group instance ID, such as `esg-33ocnj9n`, which can be obtained through the `DescribeSecurityGroups` API
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupPolicySet(self):
        """Security group policy set object.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = SecurityGroupPolicySet()
            self._SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceSecurityGroupPolicyResponse(AbstractModel):
    """ReplaceSecurityGroupPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResetInstancesMaxBandwidthRequest(AbstractModel):
    """ResetInstancesMaxBandwidth request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of IDs of the instances for which to reset the bandwidth cap. You can request up to 100 instances in a region at a time.
        :type InstanceIdSet: list of str
        :param _MaxBandwidthOut: Modified outbound bandwidth cap.
        :type MaxBandwidthOut: int
        :param _MaxBandwidthIn: Modified inbound bandwidth cap.
        :type MaxBandwidthIn: int
        """
        self._InstanceIdSet = None
        self._MaxBandwidthOut = None
        self._MaxBandwidthIn = None

    @property
    def InstanceIdSet(self):
        """List of IDs of the instances for which to reset the bandwidth cap. You can request up to 100 instances in a region at a time.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def MaxBandwidthOut(self):
        """Modified outbound bandwidth cap.
        :rtype: int
        """
        return self._MaxBandwidthOut

    @MaxBandwidthOut.setter
    def MaxBandwidthOut(self, MaxBandwidthOut):
        self._MaxBandwidthOut = MaxBandwidthOut

    @property
    def MaxBandwidthIn(self):
        """Modified inbound bandwidth cap.
        :rtype: int
        """
        return self._MaxBandwidthIn

    @MaxBandwidthIn.setter
    def MaxBandwidthIn(self, MaxBandwidthIn):
        self._MaxBandwidthIn = MaxBandwidthIn


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._MaxBandwidthOut = params.get("MaxBandwidthOut")
        self._MaxBandwidthIn = params.get("MaxBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesMaxBandwidthResponse(AbstractModel):
    """ResetInstancesMaxBandwidth response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of IDs of the instances for which to set the password. You can request up to 100 instances in a region at a time.
        :type InstanceIdSet: list of str
        :param _Password: New password. The password of a Linux instance must contain 8–16 characters in at least two of the following character types: letters, digits, and special symbols [( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /] and cannot start with `/`.
The password of a Windows instance must contain 12–16 characters in at least three of the following character types: letters, digits, and special symbols [( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /] and cannot start with `/`.
If the instances include both Linux instances and Windows instances, the password complexity limit for Windows instances will apply.
        :type Password: str
        :param _ForceStop: Whether to force shut down. Default value: false.
        :type ForceStop: bool
        :param _UserName: Username of the instance for which to reset the password, which can contain up to 64 characters. If this parameter is not specified, the password of the root user will be reset by default for Linux, and the password of the admin will be reset by default for Windows.
        :type UserName: str
        """
        self._InstanceIdSet = None
        self._Password = None
        self._ForceStop = None
        self._UserName = None

    @property
    def InstanceIdSet(self):
        """List of IDs of the instances for which to set the password. You can request up to 100 instances in a region at a time.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def Password(self):
        """New password. The password of a Linux instance must contain 8–16 characters in at least two of the following character types: letters, digits, and special symbols [( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /] and cannot start with `/`.
The password of a Windows instance must contain 12–16 characters in at least three of the following character types: letters, digits, and special symbols [( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /] and cannot start with `/`.
If the instances include both Linux instances and Windows instances, the password complexity limit for Windows instances will apply.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ForceStop(self):
        """Whether to force shut down. Default value: false.
        :rtype: bool
        """
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop

    @property
    def UserName(self):
        """Username of the instance for which to reset the password, which can contain up to 64 characters. If this parameter is not specified, the password of the root user will be reset by default for Linux, and the password of the admin will be reset by default for Windows.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._Password = params.get("Password")
        self._ForceStop = params.get("ForceStop")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResetInstancesRequest(AbstractModel):
    """ResetInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of IDs of the instances to be reinstalled.
        :type InstanceIdSet: list of str
        :param _ImageId: ID of the image from which to install the instance. If this parameter is not specified, the current image of the instance will be used.
        :type ImageId: str
        :param _Password: Password. If this parameter is not specified, the password will be subsequently displayed in the Message Center.
        :type Password: str
        :param _EnhancedService: Whether to enable CM and CWP. If this parameter is not specified, they will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        :param _KeepData: Whether to retain the data on the data disk. Valid values: true, false. Default value: true
        :type KeepData: str
        :param _KeepImageLogin: Whether to keep the original settings for the image. You cannot specify this parameter if `Password` or `KeyIds.N` is specified. You can specify this parameter as `TRUE` only when you create an instance by using a custom image, shared image, or image imported from an external resource. Valid values:
TRUE: yes
FALSE: no

Default value: FALSE.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeepImageLogin: str
        """
        self._InstanceIdSet = None
        self._ImageId = None
        self._Password = None
        self._EnhancedService = None
        self._KeepData = None
        self._KeepImageLogin = None

    @property
    def InstanceIdSet(self):
        """List of IDs of the instances to be reinstalled.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def ImageId(self):
        """ID of the image from which to install the instance. If this parameter is not specified, the current image of the instance will be used.
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Password(self):
        """Password. If this parameter is not specified, the password will be subsequently displayed in the Message Center.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EnhancedService(self):
        """Whether to enable CM and CWP. If this parameter is not specified, they will be enabled by default.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def KeepData(self):
        """Whether to retain the data on the data disk. Valid values: true, false. Default value: true
        :rtype: str
        """
        return self._KeepData

    @KeepData.setter
    def KeepData(self, KeepData):
        self._KeepData = KeepData

    @property
    def KeepImageLogin(self):
        """Whether to keep the original settings for the image. You cannot specify this parameter if `Password` or `KeyIds.N` is specified. You can specify this parameter as `TRUE` only when you create an instance by using a custom image, shared image, or image imported from an external resource. Valid values:
TRUE: yes
FALSE: no

Default value: FALSE.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeepImageLogin

    @KeepImageLogin.setter
    def KeepImageLogin(self, KeepImageLogin):
        self._KeepImageLogin = KeepImageLogin


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._ImageId = params.get("ImageId")
        self._Password = params.get("Password")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._KeepData = params.get("KeepData")
        self._KeepImageLogin = params.get("KeepImageLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesResponse(AbstractModel):
    """ResetInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResetRoutesRequest(AbstractModel):
    """ResetRoutes request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableId: Route table instance ID, such as `rtb-azd4dt1c`.
        :type RouteTableId: str
        :param _RouteTableName: Route table name, which can contain up to 60 bytes.
        :type RouteTableName: str
        :param _Routes: Routing policy.
        :type Routes: list of Route
        """
        self._RouteTableId = None
        self._RouteTableName = None
        self._Routes = None

    @property
    def RouteTableId(self):
        """Route table instance ID, such as `rtb-azd4dt1c`.
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteTableName(self):
        """Route table name, which can contain up to 60 bytes.
        :rtype: str
        """
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def Routes(self):
        """Routing policy.
        :rtype: list of Route
        """
        return self._Routes

    @Routes.setter
    def Routes(self, Routes):
        self._Routes = Routes


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._RouteTableName = params.get("RouteTableName")
        if params.get("Routes") is not None:
            self._Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self._Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetRoutesResponse(AbstractModel):
    """ResetRoutes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Route(AbstractModel):
    """Routing policy

    """

    def __init__(self):
        r"""
        :param _DestinationCidrBlock: Destination IPv4 IP range
        :type DestinationCidrBlock: str
        :param _GatewayType: Next hop type
NORMAL_CVM: general CVM;
        :type GatewayType: str
        :param _GatewayId: Next hop address
You simply need to specify the gateway ID of a different next hop type, and the system will automatically match the next hop address
When `GatewayType` is `EIP`, the value of `GatewayId` will be fixed at `0`
        :type GatewayId: str
        :param _RouteItemId: Unique routing policy ID
        :type RouteItemId: str
        :param _RouteDescription: Routing policy description
        :type RouteDescription: str
        :param _Enabled: Whether to enable
        :type Enabled: bool
        :param _RouteType: Route type. Valid values:
USER: user route;
NETD: network probe route, which will be delivered by the system by default when you create a network probe instance and cannot be edited or deleted;
CCN: CCN route, which will be delivered by the system by default and cannot be edited or deleted.
You can only add and manipulate routes of `USER` type.
        :type RouteType: str
        :param _RouteId: Routing policy ID. The IPv4 routing policy will have a meaningful value, while the IPv6 routing policy is always 0. We recommend you use the unique ID `RouteItemId` for the routing policy
        :type RouteId: int
        """
        self._DestinationCidrBlock = None
        self._GatewayType = None
        self._GatewayId = None
        self._RouteItemId = None
        self._RouteDescription = None
        self._Enabled = None
        self._RouteType = None
        self._RouteId = None

    @property
    def DestinationCidrBlock(self):
        """Destination IPv4 IP range
        :rtype: str
        """
        return self._DestinationCidrBlock

    @DestinationCidrBlock.setter
    def DestinationCidrBlock(self, DestinationCidrBlock):
        self._DestinationCidrBlock = DestinationCidrBlock

    @property
    def GatewayType(self):
        """Next hop type
NORMAL_CVM: general CVM;
        :rtype: str
        """
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType

    @property
    def GatewayId(self):
        """Next hop address
You simply need to specify the gateway ID of a different next hop type, and the system will automatically match the next hop address
When `GatewayType` is `EIP`, the value of `GatewayId` will be fixed at `0`
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def RouteItemId(self):
        """Unique routing policy ID
        :rtype: str
        """
        return self._RouteItemId

    @RouteItemId.setter
    def RouteItemId(self, RouteItemId):
        self._RouteItemId = RouteItemId

    @property
    def RouteDescription(self):
        """Routing policy description
        :rtype: str
        """
        return self._RouteDescription

    @RouteDescription.setter
    def RouteDescription(self, RouteDescription):
        self._RouteDescription = RouteDescription

    @property
    def Enabled(self):
        """Whether to enable
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def RouteType(self):
        """Route type. Valid values:
USER: user route;
NETD: network probe route, which will be delivered by the system by default when you create a network probe instance and cannot be edited or deleted;
CCN: CCN route, which will be delivered by the system by default and cannot be edited or deleted.
You can only add and manipulate routes of `USER` type.
        :rtype: str
        """
        return self._RouteType

    @RouteType.setter
    def RouteType(self, RouteType):
        self._RouteType = RouteType

    @property
    def RouteId(self):
        """Routing policy ID. The IPv4 routing policy will have a meaningful value, while the IPv6 routing policy is always 0. We recommend you use the unique ID `RouteItemId` for the routing policy
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId


    def _deserialize(self, params):
        self._DestinationCidrBlock = params.get("DestinationCidrBlock")
        self._GatewayType = params.get("GatewayType")
        self._GatewayId = params.get("GatewayId")
        self._RouteItemId = params.get("RouteItemId")
        self._RouteDescription = params.get("RouteDescription")
        self._Enabled = params.get("Enabled")
        self._RouteType = params.get("RouteType")
        self._RouteId = params.get("RouteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteConflict(AbstractModel):
    """Route conflict object

    """

    def __init__(self):
        r"""
        :param _RouteTableId: Route table instance ID
        :type RouteTableId: str
        :param _DestinationCidrBlock: The conflicting destination ports to be checked
        :type DestinationCidrBlock: str
        :param _ConflictSet: List of conflicting routing policies
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConflictSet: list of Route
        """
        self._RouteTableId = None
        self._DestinationCidrBlock = None
        self._ConflictSet = None

    @property
    def RouteTableId(self):
        """Route table instance ID
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def DestinationCidrBlock(self):
        """The conflicting destination ports to be checked
        :rtype: str
        """
        return self._DestinationCidrBlock

    @DestinationCidrBlock.setter
    def DestinationCidrBlock(self, DestinationCidrBlock):
        self._DestinationCidrBlock = DestinationCidrBlock

    @property
    def ConflictSet(self):
        """List of conflicting routing policies
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Route
        """
        return self._ConflictSet

    @ConflictSet.setter
    def ConflictSet(self, ConflictSet):
        self._ConflictSet = ConflictSet


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._DestinationCidrBlock = params.get("DestinationCidrBlock")
        if params.get("ConflictSet") is not None:
            self._ConflictSet = []
            for item in params.get("ConflictSet"):
                obj = Route()
                obj._deserialize(item)
                self._ConflictSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTable(AbstractModel):
    """Route table

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC instance ID
        :type VpcId: str
        :param _RouteTableId: Route table instance ID
        :type RouteTableId: str
        :param _RouteTableName: Route table name
        :type RouteTableName: str
        :param _AssociationSet: Association relationships of the route table
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssociationSet: list of RouteTableAssociation
        :param _RouteSet: IPv4 routing policy set
Note: this field may return null, indicating that no valid values can be obtained.
        :type RouteSet: list of Route
        :param _Main: Whether it is the default route table
        :type Main: bool
        :param _CreatedTime: Creation time
        :type CreatedTime: str
        """
        self._VpcId = None
        self._RouteTableId = None
        self._RouteTableName = None
        self._AssociationSet = None
        self._RouteSet = None
        self._Main = None
        self._CreatedTime = None

    @property
    def VpcId(self):
        """VPC instance ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def RouteTableId(self):
        """Route table instance ID
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteTableName(self):
        """Route table name
        :rtype: str
        """
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def AssociationSet(self):
        """Association relationships of the route table
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of RouteTableAssociation
        """
        return self._AssociationSet

    @AssociationSet.setter
    def AssociationSet(self, AssociationSet):
        self._AssociationSet = AssociationSet

    @property
    def RouteSet(self):
        """IPv4 routing policy set
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Route
        """
        return self._RouteSet

    @RouteSet.setter
    def RouteSet(self, RouteSet):
        self._RouteSet = RouteSet

    @property
    def Main(self):
        """Whether it is the default route table
        :rtype: bool
        """
        return self._Main

    @Main.setter
    def Main(self, Main):
        self._Main = Main

    @property
    def CreatedTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._RouteTableId = params.get("RouteTableId")
        self._RouteTableName = params.get("RouteTableName")
        if params.get("AssociationSet") is not None:
            self._AssociationSet = []
            for item in params.get("AssociationSet"):
                obj = RouteTableAssociation()
                obj._deserialize(item)
                self._AssociationSet.append(obj)
        if params.get("RouteSet") is not None:
            self._RouteSet = []
            for item in params.get("RouteSet"):
                obj = Route()
                obj._deserialize(item)
                self._RouteSet.append(obj)
        self._Main = params.get("Main")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableAssociation(AbstractModel):
    """Association relationships of the route table

    """

    def __init__(self):
        r"""
        :param _SubnetId: Subnet instance ID
        :type SubnetId: str
        :param _RouteTableId: Route table instance ID
        :type RouteTableId: str
        """
        self._SubnetId = None
        self._RouteTableId = None

    @property
    def SubnetId(self):
        """Subnet instance ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def RouteTableId(self):
        """Route table instance ID
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleHealth(AbstractModel):
    """List of forwarding rules and health status

    """

    def __init__(self):
        r"""
        :param _Targets: Health check status of the real server bound to the rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type Targets: list of TargetHealth
        """
        self._Targets = None

    @property
    def Targets(self):
        """Health check status of the real server bound to the rule
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of TargetHealth
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
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
        


class RunEIPDirectServiceEnabled(AbstractModel):
    """IP direct access information

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable IP direct access. Valid values:
TRUE: yes
FALSE: no
Default value: TRUE.
Currently, Windows images do not support IP direct access.
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        """Whether to enable IP direct access. Valid values:
TRUE: yes
FALSE: no
Default value: TRUE.
Currently, Windows images do not support IP direct access.
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesRequest(AbstractModel):
    """RunInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneInstanceCountISPSet: List of AZs in which to create instances, the number of instances to be created, and the ISPs. You can create up to 100 instances in a region at a time.
        :type ZoneInstanceCountISPSet: list of ZoneInstanceCountISP
        :param _Password: Instance login password. Different OS types have different limits on password complexity as detailed below:
The password of a Linux instance must contain 8–30 characters in at least two of the following character types: letters, digits, and special symbols [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? / ]. The password of a Windows instance must contain 12–30 characters in at least three of the following character types: letters, digits, and special symbols [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? /].
        :type Password: str
        :param _InternetMaxBandwidthOut: Public network outbound bandwidth cap in Mbps.
1. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used.
2. If you don't specify this parameter or specify it as `0` without specifying the module, the value of `InternetMaxBandwidthIn` will be used
        :type InternetMaxBandwidthOut: int
        :param _ModuleId: Module ID. If you don't specify this parameter, you must specify the `ImageId`, `InstanceType`, `DataDiskSize`, and `InternetMaxBandwidthOut` parameters
        :type ModuleId: str
        :param _ImageId: Image ID. If you don't specify this parameter or specify it as null, the default value under the corresponding module will be used.
        :type ImageId: str
        :param _InstanceName: Instance display name.
If this parameter is not specified, `Not named` will be displayed by default.
If you purchase multiple instances and specify the pattern string `{R:x}`, display names will be generated based on `[x, x+n-1]`, where `n` is the number of the purchased instances. For example, if you specify `server\_{R:3}` and purchase 1 instance, the display name will be `server\_3`, and if you purchase 2 instances, the display names will be `server\_3` and `server\_4` respectively.
You can specify multiple pattern strings `{R:x}`.
If you purchase multiple instances and don't specify the pattern string, the instance display names will be suffixed with 1, 2...n, where `n` indicates the number of the purchased instances. For example, if you specify `server_` and purchase 2 instances, the instance display names will be `server\_1` and `server\_2` respectively.
If the purchased instances belong to different regions or ISPs, the above rules will apply to each region and ISP independently.
It can contain up to 60 characters (including pattern string).
        :type InstanceName: str
        :param _HostName: Server name
`HostName` cannot start or end with a dot or hyphen and cannot contain consecutive dots or hyphens.
Windows instance: the name can contain 2–15 letters, digits, and hyphens but not dots or only digits.
Other types (such as Linux) of instances: the name should be a combination of 2 to 60 characters, supporting multiple dots. A string between two dots can contain letters, digits, and hyphens.
        :type HostName: str
        :param _ClientToken: The string used to ensure the idempotency of the request. Currently, it is a reserved parameter; therefore, do not use it.
        :type ClientToken: str
        :param _EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled for public images by default.
        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        :param _TagSpecification: Tag list
        :type TagSpecification: list of TagSpecification
        :param _UserData: The user data provided to the instance, which needs to be Base64-encoded with a maximum size of 16 KB
        :type UserData: str
        :param _InstanceType: Model. If you don't specify this parameter or specify it as null, the default value under the corresponding module will be used.
        :type InstanceType: str
        :param _DataDiskSize: Data disk size in GB. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used
        :type DataDiskSize: int
        :param _SecurityGroupIds: Security group of the instance, which can be obtained from the `sgId` field in the returned value of the `DescribeSecurityGroups` API. If this parameter is not specified, the default security group will be bound by default.
        :type SecurityGroupIds: list of str
        :param _SystemDiskSize: System disk size in GB. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used
        :type SystemDiskSize: int
        :param _InternetMaxBandwidthIn: Public network inbound bandwidth cap in Mbps.
1. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used.
2. If you don't specify this parameter or specify it as `0` without specifying the module, the value of `InternetMaxBandwidthOut` will be used
        :type InternetMaxBandwidthIn: int
        :param _InstanceChargeType: Instance billing type. Valid values:
0: postpaid by resource usage, where the daily peak usage of the CPU, memory, and disk will be calculated. This billing mode applies only to non-GNR models;
1: hourly postpaid at the unit price of xx USD/instance/hour. This billing mode applies only to GNR models. To enable it, submit a ticket for application;
2: monthly postpaid at the unit price of xx USD/instance/month. This billing mode applies only to GNR models;
If this field is left empty, `0` will be selected by default for non-GNR models, and `2` will be selected by default for GNR models.
        :type InstanceChargeType: int
        :param _KeyIds: Key pair.
        :type KeyIds: list of str
        :param _KeepImageLogin: Whether to keep the original settings for the image. You cannot specify this parameter if `Password` or `KeyIds.N` is specified. You can specify this parameter as `TRUE` only when you create an instance by using a custom image, shared image, or image imported from an external resource. Valid values:
TRUE: yes
FALSE: no

Default value: FALSE.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeepImageLogin: str
        :param _SystemDisk: System disk information.
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param _DataDisks: Data disk information.
        :type DataDisks: list of DataDisk
        """
        self._ZoneInstanceCountISPSet = None
        self._Password = None
        self._InternetMaxBandwidthOut = None
        self._ModuleId = None
        self._ImageId = None
        self._InstanceName = None
        self._HostName = None
        self._ClientToken = None
        self._EnhancedService = None
        self._TagSpecification = None
        self._UserData = None
        self._InstanceType = None
        self._DataDiskSize = None
        self._SecurityGroupIds = None
        self._SystemDiskSize = None
        self._InternetMaxBandwidthIn = None
        self._InstanceChargeType = None
        self._KeyIds = None
        self._KeepImageLogin = None
        self._SystemDisk = None
        self._DataDisks = None

    @property
    def ZoneInstanceCountISPSet(self):
        """List of AZs in which to create instances, the number of instances to be created, and the ISPs. You can create up to 100 instances in a region at a time.
        :rtype: list of ZoneInstanceCountISP
        """
        return self._ZoneInstanceCountISPSet

    @ZoneInstanceCountISPSet.setter
    def ZoneInstanceCountISPSet(self, ZoneInstanceCountISPSet):
        self._ZoneInstanceCountISPSet = ZoneInstanceCountISPSet

    @property
    def Password(self):
        """Instance login password. Different OS types have different limits on password complexity as detailed below:
The password of a Linux instance must contain 8–30 characters in at least two of the following character types: letters, digits, and special symbols [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? / ]. The password of a Windows instance must contain 12–30 characters in at least three of the following character types: letters, digits, and special symbols [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? /].
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def InternetMaxBandwidthOut(self):
        """Public network outbound bandwidth cap in Mbps.
1. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used.
2. If you don't specify this parameter or specify it as `0` without specifying the module, the value of `InternetMaxBandwidthIn` will be used
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def ModuleId(self):
        """Module ID. If you don't specify this parameter, you must specify the `ImageId`, `InstanceType`, `DataDiskSize`, and `InternetMaxBandwidthOut` parameters
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def ImageId(self):
        """Image ID. If you don't specify this parameter or specify it as null, the default value under the corresponding module will be used.
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceName(self):
        """Instance display name.
If this parameter is not specified, `Not named` will be displayed by default.
If you purchase multiple instances and specify the pattern string `{R:x}`, display names will be generated based on `[x, x+n-1]`, where `n` is the number of the purchased instances. For example, if you specify `server\_{R:3}` and purchase 1 instance, the display name will be `server\_3`, and if you purchase 2 instances, the display names will be `server\_3` and `server\_4` respectively.
You can specify multiple pattern strings `{R:x}`.
If you purchase multiple instances and don't specify the pattern string, the instance display names will be suffixed with 1, 2...n, where `n` indicates the number of the purchased instances. For example, if you specify `server_` and purchase 2 instances, the instance display names will be `server\_1` and `server\_2` respectively.
If the purchased instances belong to different regions or ISPs, the above rules will apply to each region and ISP independently.
It can contain up to 60 characters (including pattern string).
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def HostName(self):
        """Server name
`HostName` cannot start or end with a dot or hyphen and cannot contain consecutive dots or hyphens.
Windows instance: the name can contain 2–15 letters, digits, and hyphens but not dots or only digits.
Other types (such as Linux) of instances: the name should be a combination of 2 to 60 characters, supporting multiple dots. A string between two dots can contain letters, digits, and hyphens.
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def ClientToken(self):
        """The string used to ensure the idempotency of the request. Currently, it is a reserved parameter; therefore, do not use it.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def EnhancedService(self):
        """Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled for public images by default.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def TagSpecification(self):
        """Tag list
        :rtype: list of TagSpecification
        """
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def UserData(self):
        """The user data provided to the instance, which needs to be Base64-encoded with a maximum size of 16 KB
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def InstanceType(self):
        """Model. If you don't specify this parameter or specify it as null, the default value under the corresponding module will be used.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DataDiskSize(self):
        """Data disk size in GB. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used
        :rtype: int
        """
        return self._DataDiskSize

    @DataDiskSize.setter
    def DataDiskSize(self, DataDiskSize):
        self._DataDiskSize = DataDiskSize

    @property
    def SecurityGroupIds(self):
        """Security group of the instance, which can be obtained from the `sgId` field in the returned value of the `DescribeSecurityGroups` API. If this parameter is not specified, the default security group will be bound by default.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def SystemDiskSize(self):
        """System disk size in GB. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used
        :rtype: int
        """
        return self._SystemDiskSize

    @SystemDiskSize.setter
    def SystemDiskSize(self, SystemDiskSize):
        self._SystemDiskSize = SystemDiskSize

    @property
    def InternetMaxBandwidthIn(self):
        """Public network inbound bandwidth cap in Mbps.
1. If you don't specify this parameter or specify it as `0`, the default value under the corresponding module will be used.
2. If you don't specify this parameter or specify it as `0` without specifying the module, the value of `InternetMaxBandwidthOut` will be used
        :rtype: int
        """
        return self._InternetMaxBandwidthIn

    @InternetMaxBandwidthIn.setter
    def InternetMaxBandwidthIn(self, InternetMaxBandwidthIn):
        self._InternetMaxBandwidthIn = InternetMaxBandwidthIn

    @property
    def InstanceChargeType(self):
        """Instance billing type. Valid values:
0: postpaid by resource usage, where the daily peak usage of the CPU, memory, and disk will be calculated. This billing mode applies only to non-GNR models;
1: hourly postpaid at the unit price of xx USD/instance/hour. This billing mode applies only to GNR models. To enable it, submit a ticket for application;
2: monthly postpaid at the unit price of xx USD/instance/month. This billing mode applies only to GNR models;
If this field is left empty, `0` will be selected by default for non-GNR models, and `2` will be selected by default for GNR models.
        :rtype: int
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def KeyIds(self):
        """Key pair.
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
        """Whether to keep the original settings for the image. You cannot specify this parameter if `Password` or `KeyIds.N` is specified. You can specify this parameter as `TRUE` only when you create an instance by using a custom image, shared image, or image imported from an external resource. Valid values:
TRUE: yes
FALSE: no

Default value: FALSE.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeepImageLogin

    @KeepImageLogin.setter
    def KeepImageLogin(self, KeepImageLogin):
        self._KeepImageLogin = KeepImageLogin

    @property
    def SystemDisk(self):
        """System disk information.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """Data disk information.
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks


    def _deserialize(self, params):
        if params.get("ZoneInstanceCountISPSet") is not None:
            self._ZoneInstanceCountISPSet = []
            for item in params.get("ZoneInstanceCountISPSet"):
                obj = ZoneInstanceCountISP()
                obj._deserialize(item)
                self._ZoneInstanceCountISPSet.append(obj)
        self._Password = params.get("Password")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._ModuleId = params.get("ModuleId")
        self._ImageId = params.get("ImageId")
        self._InstanceName = params.get("InstanceName")
        self._HostName = params.get("HostName")
        self._ClientToken = params.get("ClientToken")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._UserData = params.get("UserData")
        self._InstanceType = params.get("InstanceType")
        self._DataDiskSize = params.get("DataDiskSize")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._SystemDiskSize = params.get("SystemDiskSize")
        self._InternetMaxBandwidthIn = params.get("InternetMaxBandwidthIn")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._KeyIds = params.get("KeyIds")
        self._KeepImageLogin = params.get("KeepImageLogin")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesResponse(AbstractModel):
    """RunInstances response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of IDs of the instances being created
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        """List of IDs of the instances being created
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """CM

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable.
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        """Whether to enable.
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """CWP;

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable.
        :type Enabled: bool
        :param _Version: CWP edition. Valid values: 0: Basic Edition; 1: Pro Edition. Currently, only Basic Edition is supported
        :type Version: int
        """
        self._Enabled = None
        self._Version = None

    @property
    def Enabled(self):
        """Whether to enable.
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Version(self):
        """CWP edition. Valid values: 0: Basic Edition; 1: Pro Edition. Currently, only Basic Edition is supported
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """Security group object

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group instance ID, such as `esg-ohuuioma`.
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name, which can be customized with up to 60 characters.
        :type SecurityGroupName: str
        :param _SecurityGroupDesc: Security group remarks, which can contain up to 100 characters.
        :type SecurityGroupDesc: str
        :param _IsDefault: Whether it is the default security group (which cannot be deleted).
        :type IsDefault: bool
        :param _CreatedTime: Security group creation time.
        :type CreatedTime: str
        :param _TagSet: Tag key-value pairs.
        :type TagSet: list of Tag
        """
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupDesc = None
        self._IsDefault = None
        self._CreatedTime = None
        self._TagSet = None

    @property
    def SecurityGroupId(self):
        """Security group instance ID, such as `esg-ohuuioma`.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        """Security group name, which can be customized with up to 60 characters.
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupDesc(self):
        """Security group remarks, which can contain up to 100 characters.
        :rtype: str
        """
        return self._SecurityGroupDesc

    @SecurityGroupDesc.setter
    def SecurityGroupDesc(self, SecurityGroupDesc):
        self._SecurityGroupDesc = SecurityGroupDesc

    @property
    def IsDefault(self):
        """Whether it is the default security group (which cannot be deleted).
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def CreatedTime(self):
        """Security group creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def TagSet(self):
        """Tag key-value pairs.
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupDesc = params.get("SecurityGroupDesc")
        self._IsDefault = params.get("IsDefault")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupAssociationStatistics(AbstractModel):
    """Statistics on the resources associated with the security group

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group instance ID.
        :type SecurityGroupId: str
        :param _ECM: Number of ECM instances.
        :type ECM: int
        :param _Module: Number of ECM modules.
        :type Module: int
        :param _ENI: Number of ENI instances.
        :type ENI: int
        :param _SG: Number of times the security group is referenced by other security groups.
        :type SG: int
        :param _CLB: Number of CLB instances.
        :type CLB: int
        :param _InstanceStatistics: Binding statistics of all instances.
        :type InstanceStatistics: list of InstanceStatistic
        :param _TotalCount: Total number of all resources (excluding resources referenced by security groups).
        :type TotalCount: int
        """
        self._SecurityGroupId = None
        self._ECM = None
        self._Module = None
        self._ENI = None
        self._SG = None
        self._CLB = None
        self._InstanceStatistics = None
        self._TotalCount = None

    @property
    def SecurityGroupId(self):
        """Security group instance ID.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def ECM(self):
        """Number of ECM instances.
        :rtype: int
        """
        return self._ECM

    @ECM.setter
    def ECM(self, ECM):
        self._ECM = ECM

    @property
    def Module(self):
        """Number of ECM modules.
        :rtype: int
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ENI(self):
        """Number of ENI instances.
        :rtype: int
        """
        return self._ENI

    @ENI.setter
    def ENI(self, ENI):
        self._ENI = ENI

    @property
    def SG(self):
        """Number of times the security group is referenced by other security groups.
        :rtype: int
        """
        return self._SG

    @SG.setter
    def SG(self, SG):
        self._SG = SG

    @property
    def CLB(self):
        """Number of CLB instances.
        :rtype: int
        """
        return self._CLB

    @CLB.setter
    def CLB(self, CLB):
        self._CLB = CLB

    @property
    def InstanceStatistics(self):
        """Binding statistics of all instances.
        :rtype: list of InstanceStatistic
        """
        return self._InstanceStatistics

    @InstanceStatistics.setter
    def InstanceStatistics(self, InstanceStatistics):
        self._InstanceStatistics = InstanceStatistics

    @property
    def TotalCount(self):
        """Total number of all resources (excluding resources referenced by security groups).
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._ECM = params.get("ECM")
        self._Module = params.get("Module")
        self._ENI = params.get("ENI")
        self._SG = params.get("SG")
        self._CLB = params.get("CLB")
        if params.get("InstanceStatistics") is not None:
            self._InstanceStatistics = []
            for item in params.get("InstanceStatistics"):
                obj = InstanceStatistic()
                obj._deserialize(item)
                self._InstanceStatistics.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupLimitSet(AbstractModel):
    """Security group quota limit

    """

    def __init__(self):
        r"""
        :param _SecurityGroupLimit: Total number of security groups that can be created
        :type SecurityGroupLimit: int
        :param _SecurityGroupPolicyLimit: Maximum number of rules under the security group
        :type SecurityGroupPolicyLimit: int
        :param _ReferedSecurityGroupLimit: Number of nested security group rules under the security group
        :type ReferedSecurityGroupLimit: int
        :param _SecurityGroupInstanceLimit: Number of instances associated with the security group
        :type SecurityGroupInstanceLimit: int
        :param _InstanceSecurityGroupLimit: Number of security groups associated with the instance
        :type InstanceSecurityGroupLimit: int
        :param _SecurityGroupModuleLimit: Number of modules associated with the security group
        :type SecurityGroupModuleLimit: int
        :param _ModuleSecurityGroupLimit: Number of security groups associated with the module
        :type ModuleSecurityGroupLimit: int
        """
        self._SecurityGroupLimit = None
        self._SecurityGroupPolicyLimit = None
        self._ReferedSecurityGroupLimit = None
        self._SecurityGroupInstanceLimit = None
        self._InstanceSecurityGroupLimit = None
        self._SecurityGroupModuleLimit = None
        self._ModuleSecurityGroupLimit = None

    @property
    def SecurityGroupLimit(self):
        """Total number of security groups that can be created
        :rtype: int
        """
        return self._SecurityGroupLimit

    @SecurityGroupLimit.setter
    def SecurityGroupLimit(self, SecurityGroupLimit):
        self._SecurityGroupLimit = SecurityGroupLimit

    @property
    def SecurityGroupPolicyLimit(self):
        """Maximum number of rules under the security group
        :rtype: int
        """
        return self._SecurityGroupPolicyLimit

    @SecurityGroupPolicyLimit.setter
    def SecurityGroupPolicyLimit(self, SecurityGroupPolicyLimit):
        self._SecurityGroupPolicyLimit = SecurityGroupPolicyLimit

    @property
    def ReferedSecurityGroupLimit(self):
        """Number of nested security group rules under the security group
        :rtype: int
        """
        return self._ReferedSecurityGroupLimit

    @ReferedSecurityGroupLimit.setter
    def ReferedSecurityGroupLimit(self, ReferedSecurityGroupLimit):
        self._ReferedSecurityGroupLimit = ReferedSecurityGroupLimit

    @property
    def SecurityGroupInstanceLimit(self):
        """Number of instances associated with the security group
        :rtype: int
        """
        return self._SecurityGroupInstanceLimit

    @SecurityGroupInstanceLimit.setter
    def SecurityGroupInstanceLimit(self, SecurityGroupInstanceLimit):
        self._SecurityGroupInstanceLimit = SecurityGroupInstanceLimit

    @property
    def InstanceSecurityGroupLimit(self):
        """Number of security groups associated with the instance
        :rtype: int
        """
        return self._InstanceSecurityGroupLimit

    @InstanceSecurityGroupLimit.setter
    def InstanceSecurityGroupLimit(self, InstanceSecurityGroupLimit):
        self._InstanceSecurityGroupLimit = InstanceSecurityGroupLimit

    @property
    def SecurityGroupModuleLimit(self):
        """Number of modules associated with the security group
        :rtype: int
        """
        return self._SecurityGroupModuleLimit

    @SecurityGroupModuleLimit.setter
    def SecurityGroupModuleLimit(self, SecurityGroupModuleLimit):
        self._SecurityGroupModuleLimit = SecurityGroupModuleLimit

    @property
    def ModuleSecurityGroupLimit(self):
        """Number of security groups associated with the module
        :rtype: int
        """
        return self._ModuleSecurityGroupLimit

    @ModuleSecurityGroupLimit.setter
    def ModuleSecurityGroupLimit(self, ModuleSecurityGroupLimit):
        self._ModuleSecurityGroupLimit = ModuleSecurityGroupLimit


    def _deserialize(self, params):
        self._SecurityGroupLimit = params.get("SecurityGroupLimit")
        self._SecurityGroupPolicyLimit = params.get("SecurityGroupPolicyLimit")
        self._ReferedSecurityGroupLimit = params.get("ReferedSecurityGroupLimit")
        self._SecurityGroupInstanceLimit = params.get("SecurityGroupInstanceLimit")
        self._InstanceSecurityGroupLimit = params.get("InstanceSecurityGroupLimit")
        self._SecurityGroupModuleLimit = params.get("SecurityGroupModuleLimit")
        self._ModuleSecurityGroupLimit = params.get("ModuleSecurityGroupLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicy(AbstractModel):
    """Security group policy object

    """

    def __init__(self):
        r"""
        :param _PolicyIndex: Security group policy index number
        :type PolicyIndex: int
        :param _Protocol: Protocol. Valid values: TCP, UDP, ICMP.
        :type Protocol: str
        :param _Port: Port. Valid values: all, discrete port, range.
        :type Port: str
        :param _ServiceTemplate: Protocol port ID or protocol port group ID. `ServiceTemplate` and `Protocol+Port` are mutually exclusive.
        :type ServiceTemplate: :class:`tencentcloud.ecm.v20190719.models.ServiceTemplateSpecification`
        :param _CidrBlock: IP range or IP address (mutually exclusive).
        :type CidrBlock: str
        :param _SecurityGroupId: Security group instance ID, such as `esg-ohuuioma`.
        :type SecurityGroupId: str
        :param _AddressTemplate: IP address ID or IP address group ID.
        :type AddressTemplate: :class:`tencentcloud.ecm.v20190719.models.AddressTemplateSpecification`
        :param _Action: `ACCEPT` or `DROP`.
        :type Action: str
        :param _PolicyDescription: Security group policy description.
        :type PolicyDescription: str
        :param _ModifyTime: Modification time, such as `2020-07-22 19:27:23`
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModifyTime: str
        :param _Ipv6CidrBlock: IP range or IPv6 address (mutually exclusive).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ipv6CidrBlock: str
        """
        self._PolicyIndex = None
        self._Protocol = None
        self._Port = None
        self._ServiceTemplate = None
        self._CidrBlock = None
        self._SecurityGroupId = None
        self._AddressTemplate = None
        self._Action = None
        self._PolicyDescription = None
        self._ModifyTime = None
        self._Ipv6CidrBlock = None

    @property
    def PolicyIndex(self):
        """Security group policy index number
        :rtype: int
        """
        return self._PolicyIndex

    @PolicyIndex.setter
    def PolicyIndex(self, PolicyIndex):
        self._PolicyIndex = PolicyIndex

    @property
    def Protocol(self):
        """Protocol. Valid values: TCP, UDP, ICMP.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """Port. Valid values: all, discrete port, range.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceTemplate(self):
        """Protocol port ID or protocol port group ID. `ServiceTemplate` and `Protocol+Port` are mutually exclusive.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ServiceTemplateSpecification`
        """
        return self._ServiceTemplate

    @ServiceTemplate.setter
    def ServiceTemplate(self, ServiceTemplate):
        self._ServiceTemplate = ServiceTemplate

    @property
    def CidrBlock(self):
        """IP range or IP address (mutually exclusive).
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def SecurityGroupId(self):
        """Security group instance ID, such as `esg-ohuuioma`.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def AddressTemplate(self):
        """IP address ID or IP address group ID.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AddressTemplateSpecification`
        """
        return self._AddressTemplate

    @AddressTemplate.setter
    def AddressTemplate(self, AddressTemplate):
        self._AddressTemplate = AddressTemplate

    @property
    def Action(self):
        """`ACCEPT` or `DROP`.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PolicyDescription(self):
        """Security group policy description.
        :rtype: str
        """
        return self._PolicyDescription

    @PolicyDescription.setter
    def PolicyDescription(self, PolicyDescription):
        self._PolicyDescription = PolicyDescription

    @property
    def ModifyTime(self):
        """Modification time, such as `2020-07-22 19:27:23`
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Ipv6CidrBlock(self):
        """IP range or IPv6 address (mutually exclusive).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock


    def _deserialize(self, params):
        self._PolicyIndex = params.get("PolicyIndex")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("ServiceTemplate") is not None:
            self._ServiceTemplate = ServiceTemplateSpecification()
            self._ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self._CidrBlock = params.get("CidrBlock")
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("AddressTemplate") is not None:
            self._AddressTemplate = AddressTemplateSpecification()
            self._AddressTemplate._deserialize(params.get("AddressTemplate"))
        self._Action = params.get("Action")
        self._PolicyDescription = params.get("PolicyDescription")
        self._ModifyTime = params.get("ModifyTime")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicySet(AbstractModel):
    """Security group policy set

    """

    def __init__(self):
        r"""
        :param _Version: The version number of the security group policy, which will automatically increase by one each time you update the security group policy, so as to prevent expiration of the updated routing policies. If it is left empty, any conflicts will be ignored.
        :type Version: str
        :param _Egress: Outbound rule. You must select either an outbound rule or inbound rule.
        :type Egress: list of SecurityGroupPolicy
        :param _Ingress: Inbound rule. You must select either outbound rule or inbound rule.
        :type Ingress: list of SecurityGroupPolicy
        """
        self._Version = None
        self._Egress = None
        self._Ingress = None

    @property
    def Version(self):
        """The version number of the security group policy, which will automatically increase by one each time you update the security group policy, so as to prevent expiration of the updated routing policies. If it is left empty, any conflicts will be ignored.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Egress(self):
        """Outbound rule. You must select either an outbound rule or inbound rule.
        :rtype: list of SecurityGroupPolicy
        """
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress

    @property
    def Ingress(self):
        """Inbound rule. You must select either outbound rule or inbound rule.
        :rtype: list of SecurityGroupPolicy
        """
        return self._Ingress

    @Ingress.setter
    def Ingress(self, Ingress):
        self._Ingress = Ingress


    def _deserialize(self, params):
        self._Version = params.get("Version")
        if params.get("Egress") is not None:
            self._Egress = []
            for item in params.get("Egress"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self._Egress.append(obj)
        if params.get("Ingress") is not None:
            self._Ingress = []
            for item in params.get("Ingress"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self._Ingress.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceTemplateSpecification(AbstractModel):
    """Protocol port template

    """

    def __init__(self):
        r"""
        :param _ServiceId: Protocol port ID, such as `eppm-f5n1f8da`.
        :type ServiceId: str
        :param _ServiceGroupId: Protocol port group ID, such as `eppmg-f5n1f8da`.
        :type ServiceGroupId: str
        """
        self._ServiceId = None
        self._ServiceGroupId = None

    @property
    def ServiceId(self):
        """Protocol port ID, such as `eppm-f5n1f8da`.
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceGroupId(self):
        """Protocol port group ID, such as `eppmg-f5n1f8da`.
        :rtype: str
        """
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceGroupId = params.get("ServiceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID
        :type LoadBalancerId: str
        :param _SecurityGroups: Array of security group IDs. You can bind up to 5 security groups to a CLB instance. If you want to unbind all security groups, leave this parameter empty or pass in an empty array
        :type SecurityGroups: list of str
        """
        self._LoadBalancerId = None
        self._SecurityGroups = None

    @property
    def LoadBalancerId(self):
        """CLB instance ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SecurityGroups(self):
        """Array of security group IDs. You can bind up to 5 security groups to a CLB instance. If you want to unbind all security groups, leave this parameter empty or pass in an empty array
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    """SetLoadBalancerSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: Array of CLB instance IDs
        :type LoadBalancerIds: list of str
        :param _SecurityGroup: Security group ID, such as `esg-12345678`
        :type SecurityGroup: str
        :param _OperationType: ADD: bind security group;
DEL: unbind security group
        :type OperationType: str
        """
        self._LoadBalancerIds = None
        self._SecurityGroup = None
        self._OperationType = None

    @property
    def LoadBalancerIds(self):
        """Array of CLB instance IDs
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def SecurityGroup(self):
        """Security group ID, such as `esg-12345678`
        :rtype: str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def OperationType(self):
        """ADD: bind security group;
DEL: unbind security group
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._SecurityGroup = params.get("SecurityGroup")
        self._OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetSecurityGroupForLoadbalancersResponse(AbstractModel):
    """SetSecurityGroupForLoadbalancers response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SimpleModule(AbstractModel):
    """Basic information of the module

    """

    def __init__(self):
        r"""
        :param _ModuleId: Module ID
        :type ModuleId: str
        :param _ModuleName: Module name
        :type ModuleName: str
        """
        self._ModuleId = None
        self._ModuleName = None

    @property
    def ModuleId(self):
        """Module ID
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def ModuleName(self):
        """Module name
        :rtype: str
        """
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """Snapshot details

    """

    def __init__(self):
        r"""
        :param _Placement: Snapshot location.
        :type Placement: :class:`tencentcloud.ecm.v20190719.models.Placement`
        :param _CopyFromRemote: Whether the snapshot is replicated across regions. Valid values:<br><li>true: yes;<br><li>false: no.
        :type CopyFromRemote: bool
        :param _IsPermanent: Whether the snapshot is a permanent snapshot. Valid values:<br><li>true: yes<br><li>false: no.
        :type IsPermanent: bool
        :param _SnapshotName: Snapshot name, i.e., the user-defined snapshot alias. You can call [ModifySnapshotAttribute](https://intl.cloud.tencent.com/document/product/362/15650?from_cn_redirect=1) to modify this field.
        :type SnapshotName: str
        :param _Percent: Snapshot creation progress in percentage. This field will always be `100` once the snapshot is created successfully.
        :type Percent: int
        :param _Images: List of images associated with the snapshot.
        :type Images: list of Image
        :param _ShareReference: Number of snapshots currently shared.
        :type ShareReference: int
        :param _SnapshotType: Snapshot type. Valid values: PRIVATE_SNAPSHOT, SHARED_SNAPSHOT
        :type SnapshotType: str
        :param _DiskSize: Size in GB of the cloud disk for which the snapshot is created.
        :type DiskSize: int
        :param _DiskId: ID of the cloud disk for which the snapshot is created.
        :type DiskId: str
        :param _CopyingToRegions: Destination region to which the snapshot is being replicated. Default value: [].
        :type CopyingToRegions: list of str
        :param _SnapshotId: Snapshot ID.
        :type SnapshotId: str
        :param _DiskUsage: Type of the cloud disk for which the snapshot is created. Valid values:<br><li>SYSTEM_DISK: system disk<br><li>DATA_DISK: data disk.
        :type DiskUsage: str
        :param _Encrypt: Whether the snapshot is created from an encrypted disk. Valid values:<br><li>true: yes<br><li>false: no.
        :type Encrypt: bool
        :param _CreateTime: Snapshot creation time.
        :type CreateTime: str
        :param _ImageCount: Number of images associated with the snapshot.
        :type ImageCount: int
        :param _SnapshotState: Snapshot status. Valid values:<br><li>NORMAL: normal<br><li>CREATING: creating<br><li>ROLLBACKING: rolling back<br><li>COPYING_FROM_REMOTE: cross-region replicating<br><li>CHECKING_COPIED: verifying the cross-region replicated data<br><li>TORECYCLE: to be repossessed.
        :type SnapshotState: str
        :param _DeadlineTime: Snapshot expiration time.
        :type DeadlineTime: str
        :param _TimeStartShare: Time when snapshot sharing starts.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeStartShare: str
        """
        self._Placement = None
        self._CopyFromRemote = None
        self._IsPermanent = None
        self._SnapshotName = None
        self._Percent = None
        self._Images = None
        self._ShareReference = None
        self._SnapshotType = None
        self._DiskSize = None
        self._DiskId = None
        self._CopyingToRegions = None
        self._SnapshotId = None
        self._DiskUsage = None
        self._Encrypt = None
        self._CreateTime = None
        self._ImageCount = None
        self._SnapshotState = None
        self._DeadlineTime = None
        self._TimeStartShare = None

    @property
    def Placement(self):
        """Snapshot location.
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CopyFromRemote(self):
        """Whether the snapshot is replicated across regions. Valid values:<br><li>true: yes;<br><li>false: no.
        :rtype: bool
        """
        return self._CopyFromRemote

    @CopyFromRemote.setter
    def CopyFromRemote(self, CopyFromRemote):
        self._CopyFromRemote = CopyFromRemote

    @property
    def IsPermanent(self):
        """Whether the snapshot is a permanent snapshot. Valid values:<br><li>true: yes<br><li>false: no.
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def SnapshotName(self):
        """Snapshot name, i.e., the user-defined snapshot alias. You can call [ModifySnapshotAttribute](https://intl.cloud.tencent.com/document/product/362/15650?from_cn_redirect=1) to modify this field.
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Percent(self):
        """Snapshot creation progress in percentage. This field will always be `100` once the snapshot is created successfully.
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Images(self):
        """List of images associated with the snapshot.
        :rtype: list of Image
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def ShareReference(self):
        """Number of snapshots currently shared.
        :rtype: int
        """
        return self._ShareReference

    @ShareReference.setter
    def ShareReference(self, ShareReference):
        self._ShareReference = ShareReference

    @property
    def SnapshotType(self):
        """Snapshot type. Valid values: PRIVATE_SNAPSHOT, SHARED_SNAPSHOT
        :rtype: str
        """
        return self._SnapshotType

    @SnapshotType.setter
    def SnapshotType(self, SnapshotType):
        self._SnapshotType = SnapshotType

    @property
    def DiskSize(self):
        """Size in GB of the cloud disk for which the snapshot is created.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        """ID of the cloud disk for which the snapshot is created.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def CopyingToRegions(self):
        """Destination region to which the snapshot is being replicated. Default value: [].
        :rtype: list of str
        """
        return self._CopyingToRegions

    @CopyingToRegions.setter
    def CopyingToRegions(self, CopyingToRegions):
        self._CopyingToRegions = CopyingToRegions

    @property
    def SnapshotId(self):
        """Snapshot ID.
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskUsage(self):
        """Type of the cloud disk for which the snapshot is created. Valid values:<br><li>SYSTEM_DISK: system disk<br><li>DATA_DISK: data disk.
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def Encrypt(self):
        """Whether the snapshot is created from an encrypted disk. Valid values:<br><li>true: yes<br><li>false: no.
        :rtype: bool
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def CreateTime(self):
        """Snapshot creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ImageCount(self):
        """Number of images associated with the snapshot.
        :rtype: int
        """
        return self._ImageCount

    @ImageCount.setter
    def ImageCount(self, ImageCount):
        self._ImageCount = ImageCount

    @property
    def SnapshotState(self):
        """Snapshot status. Valid values:<br><li>NORMAL: normal<br><li>CREATING: creating<br><li>ROLLBACKING: rolling back<br><li>COPYING_FROM_REMOTE: cross-region replicating<br><li>CHECKING_COPIED: verifying the cross-region replicated data<br><li>TORECYCLE: to be repossessed.
        :rtype: str
        """
        return self._SnapshotState

    @SnapshotState.setter
    def SnapshotState(self, SnapshotState):
        self._SnapshotState = SnapshotState

    @property
    def DeadlineTime(self):
        """Snapshot expiration time.
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def TimeStartShare(self):
        """Time when snapshot sharing starts.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TimeStartShare

    @TimeStartShare.setter
    def TimeStartShare(self, TimeStartShare):
        self._TimeStartShare = TimeStartShare


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CopyFromRemote = params.get("CopyFromRemote")
        self._IsPermanent = params.get("IsPermanent")
        self._SnapshotName = params.get("SnapshotName")
        self._Percent = params.get("Percent")
        if params.get("Images") is not None:
            self._Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self._Images.append(obj)
        self._ShareReference = params.get("ShareReference")
        self._SnapshotType = params.get("SnapshotType")
        self._DiskSize = params.get("DiskSize")
        self._DiskId = params.get("DiskId")
        self._CopyingToRegions = params.get("CopyingToRegions")
        self._SnapshotId = params.get("SnapshotId")
        self._DiskUsage = params.get("DiskUsage")
        self._Encrypt = params.get("Encrypt")
        self._CreateTime = params.get("CreateTime")
        self._ImageCount = params.get("ImageCount")
        self._SnapshotState = params.get("SnapshotState")
        self._DeadlineTime = params.get("DeadlineTime")
        self._TimeStartShare = params.get("TimeStartShare")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SrcImage(AbstractModel):
    """Image source information

    """

    def __init__(self):
        r"""
        :param _ImageId: Image ID
        :type ImageId: str
        :param _ImageName: Image name
        :type ImageName: str
        :param _ImageOsName: System name
        :type ImageOsName: str
        :param _ImageDescription: Image description
        :type ImageDescription: str
        :param _Region: Region
        :type Region: str
        :param _RegionID: Region ID
        :type RegionID: int
        :param _RegionName: Region name
        :type RegionName: str
        :param _InstanceName: Source instance name
        :type InstanceName: str
        :param _InstanceId: Source instance ID
        :type InstanceId: str
        :param _ImageType: Source image type
        :type ImageType: str
        """
        self._ImageId = None
        self._ImageName = None
        self._ImageOsName = None
        self._ImageDescription = None
        self._Region = None
        self._RegionID = None
        self._RegionName = None
        self._InstanceName = None
        self._InstanceId = None
        self._ImageType = None

    @property
    def ImageId(self):
        """Image ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        """Image name
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageOsName(self):
        """System name
        :rtype: str
        """
        return self._ImageOsName

    @ImageOsName.setter
    def ImageOsName(self, ImageOsName):
        self._ImageOsName = ImageOsName

    @property
    def ImageDescription(self):
        """Image description
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionID(self):
        """Region ID
        :rtype: int
        """
        return self._RegionID

    @RegionID.setter
    def RegionID(self, RegionID):
        self._RegionID = RegionID

    @property
    def RegionName(self):
        """Region name
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def InstanceName(self):
        """Source instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        """Source instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageType(self):
        """Source image type
        :rtype: str
        """
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._ImageOsName = params.get("ImageOsName")
        self._ImageDescription = params.get("ImageDescription")
        self._Region = params.get("Region")
        self._RegionID = params.get("RegionID")
        self._RegionName = params.get("RegionName")
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._ImageType = params.get("ImageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesRequest(AbstractModel):
    """StartInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of IDs of the instances to be started. You can request up to 100 instances in a region at a time.
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        """List of IDs of the instances to be started. You can request up to 100 instances in a region at a time.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesResponse(AbstractModel):
    """StartInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopInstancesRequest(AbstractModel):
    """StopInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of IDs of the instances to be shut down. You can request up to 100 instances in a region at a time.
        :type InstanceIdSet: list of str
        :param _ForceStop: Whether to force shut down the instance after it failed to be shut down normally. Default value: false: no.
        :type ForceStop: bool
        :param _StopType: Instance shutdown mode. Valid values:
SOFT_FIRST: perform a forced shutdown in case of a failure of the normal shutdown;
HARD: forced shutdown;
SOFT: Soft shutdown;
Default value: SOFT.
        :type StopType: str
        """
        self._InstanceIdSet = None
        self._ForceStop = None
        self._StopType = None

    @property
    def InstanceIdSet(self):
        """List of IDs of the instances to be shut down. You can request up to 100 instances in a region at a time.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def ForceStop(self):
        """Whether to force shut down the instance after it failed to be shut down normally. Default value: false: no.
        :rtype: bool
        """
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop

    @property
    def StopType(self):
        """Instance shutdown mode. Valid values:
SOFT_FIRST: perform a forced shutdown in case of a failure of the normal shutdown;
HARD: forced shutdown;
SOFT: Soft shutdown;
Default value: SOFT.
        :rtype: str
        """
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._ForceStop = params.get("ForceStop")
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    """StopInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Subnet(AbstractModel):
    """Subnet object

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC instance ID.
        :type VpcId: str
        :param _SubnetId: Subnet instance ID, such as `subnet-bthucmmy`.
        :type SubnetId: str
        :param _SubnetName: Subnet name.
        :type SubnetName: str
        :param _CidrBlock: IPv4 CIDR block of the subnet.
        :type CidrBlock: str
        :param _IsDefault: Whether it is the default subnet.
        :type IsDefault: bool
        :param _EnableBroadcast: Whether to enable broadcast.
        :type EnableBroadcast: bool
        :param _RouteTableId: Route table instance ID, such as `rtb-l2h8d7c2`.
        :type RouteTableId: str
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _AvailableIpAddressCount: Number of available IPs.
        :type AvailableIpAddressCount: int
        :param _Ipv6CidrBlock: IPv6 CIDR block of the subnet.
        :type Ipv6CidrBlock: str
        :param _NetworkAclId: Associated ACLID
        :type NetworkAclId: str
        :param _IsRemoteVpcSnat: Whether it is an SNAT address pool subnet.
        :type IsRemoteVpcSnat: bool
        :param _TagSet: Tag key-value pairs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param _Zone: Region
        :type Zone: str
        :param _ZoneName: AZ name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneName: str
        :param _InstanceCount: Number of instances
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceCount: int
        :param _VpcCidrBlock: IPv4 CIDR block of the VPC.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcCidrBlock: str
        :param _VpcIpv6CidrBlock: IPv6 CIDR block of the VPC.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcIpv6CidrBlock: str
        :param _Region: Region
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._SubnetName = None
        self._CidrBlock = None
        self._IsDefault = None
        self._EnableBroadcast = None
        self._RouteTableId = None
        self._CreatedTime = None
        self._AvailableIpAddressCount = None
        self._Ipv6CidrBlock = None
        self._NetworkAclId = None
        self._IsRemoteVpcSnat = None
        self._TagSet = None
        self._Zone = None
        self._ZoneName = None
        self._InstanceCount = None
        self._VpcCidrBlock = None
        self._VpcIpv6CidrBlock = None
        self._Region = None

    @property
    def VpcId(self):
        """VPC instance ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet instance ID, such as `subnet-bthucmmy`.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        """Subnet name.
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        """IPv4 CIDR block of the subnet.
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def IsDefault(self):
        """Whether it is the default subnet.
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def EnableBroadcast(self):
        """Whether to enable broadcast.
        :rtype: bool
        """
        return self._EnableBroadcast

    @EnableBroadcast.setter
    def EnableBroadcast(self, EnableBroadcast):
        self._EnableBroadcast = EnableBroadcast

    @property
    def RouteTableId(self):
        """Route table instance ID, such as `rtb-l2h8d7c2`.
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def CreatedTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def AvailableIpAddressCount(self):
        """Number of available IPs.
        :rtype: int
        """
        return self._AvailableIpAddressCount

    @AvailableIpAddressCount.setter
    def AvailableIpAddressCount(self, AvailableIpAddressCount):
        self._AvailableIpAddressCount = AvailableIpAddressCount

    @property
    def Ipv6CidrBlock(self):
        """IPv6 CIDR block of the subnet.
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock

    @property
    def NetworkAclId(self):
        """Associated ACLID
        :rtype: str
        """
        return self._NetworkAclId

    @NetworkAclId.setter
    def NetworkAclId(self, NetworkAclId):
        self._NetworkAclId = NetworkAclId

    @property
    def IsRemoteVpcSnat(self):
        """Whether it is an SNAT address pool subnet.
        :rtype: bool
        """
        return self._IsRemoteVpcSnat

    @IsRemoteVpcSnat.setter
    def IsRemoteVpcSnat(self, IsRemoteVpcSnat):
        self._IsRemoteVpcSnat = IsRemoteVpcSnat

    @property
    def TagSet(self):
        """Tag key-value pairs.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Zone(self):
        """Region
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        """AZ name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceCount(self):
        """Number of instances
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def VpcCidrBlock(self):
        """IPv4 CIDR block of the VPC.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def VpcIpv6CidrBlock(self):
        """IPv6 CIDR block of the VPC.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcIpv6CidrBlock

    @VpcIpv6CidrBlock.setter
    def VpcIpv6CidrBlock(self, VpcIpv6CidrBlock):
        self._VpcIpv6CidrBlock = VpcIpv6CidrBlock

    @property
    def Region(self):
        """Region
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._CidrBlock = params.get("CidrBlock")
        self._IsDefault = params.get("IsDefault")
        self._EnableBroadcast = params.get("EnableBroadcast")
        self._RouteTableId = params.get("RouteTableId")
        self._CreatedTime = params.get("CreatedTime")
        self._AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self._NetworkAclId = params.get("NetworkAclId")
        self._IsRemoteVpcSnat = params.get("IsRemoteVpcSnat")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._InstanceCount = params.get("InstanceCount")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._VpcIpv6CidrBlock = params.get("VpcIpv6CidrBlock")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemDisk(AbstractModel):
    """System disk description.

    """

    def __init__(self):
        r"""
        :param _DiskType: Disk type. Valid values:
- LOCAL_BASIC: local disk;
- CLOUD_PREMIUM: Premium Cloud Storage;
Default value: CLOUD_BASIC.
        :type DiskType: str
        :param _DiskId: Disk ID. This parameter is temporarily unavailable.
        :type DiskId: str
        :param _DiskSize: Disk size in GB.
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskId = None
        self._DiskSize = None

    @property
    def DiskType(self):
        """Disk type. Valid values:
- LOCAL_BASIC: local disk;
- CLOUD_PREMIUM: Premium Cloud Storage;
Default value: CLOUD_BASIC.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        """Disk ID. This parameter is temporarily unavailable.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        """Disk size in GB.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag information.

    """

    def __init__(self):
        r"""
        :param _Key: Tag key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: Tag value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Tag key.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Tag value.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        


class TagInfo(AbstractModel):
    """Tag information.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value.
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
        


class TagSpecification(AbstractModel):
    """Resource type tag

    """

    def __init__(self):
        r"""
        :param _ResourceType: Resource type. Valid values: instance, module
        :type ResourceType: str
        :param _Tags: Tag list
        :type Tags: list of Tag
        """
        self._ResourceType = None
        self._Tags = None

    @property
    def ResourceType(self):
        """Resource type. Valid values: instance, module
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Tags(self):
        """Tag list
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Target(AbstractModel):
    """CLB backend target

    """

    def __init__(self):
        r"""
        :param _Port: Listening port of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _InstanceId: CVM instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Weight: Forwarding weight of the real server. Value range: [0, 100]. Default value: 10.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param _EniIp: You need to pass in this parameter when binding an ENI. It represents the IP address of the ENI. You must bind an ENI to a CVM instance first before you can bind it to a CLB instance. Note: you must pass in either `InstanceId` or `EniIp`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EniIp: str
        """
        self._Port = None
        self._InstanceId = None
        self._Weight = None
        self._EniIp = None

    @property
    def Port(self):
        """Listening port of the real server
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        """CVM instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        """Forwarding weight of the real server. Value range: [0, 100]. Default value: 10.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def EniIp(self):
        """You need to pass in this parameter when binding an ENI. It represents the IP address of the ENI. You must bind an ENI to a CVM instance first before you can bind it to a CLB instance. Note: you must pass in either `InstanceId` or `EniIp`.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp


    def _deserialize(self, params):
        self._Port = params.get("Port")
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
    """Health check status of the backend

    """

    def __init__(self):
        r"""
        :param _IP: Private IP of the target
Note: this field may return null, indicating that no valid values can be obtained.
        :type IP: str
        :param _Port: Port bound to the target
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _HealthStatus: Current health status. Valid values: true: healthy; false: unhealthy (e.g., check not started, checking, or exceptional status). CLB instance will route traffic to only healthy real servers whose weights are greater than 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthStatus: bool
        :param _TargetId: Instance ID of the target
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetId: str
        :param _HealthStatusDetail: Detailed information of the current health status. Valid values: Alive: healthy; Dead: exceptional; Unknown: check not started/checking/unknown status; Close: health check not configured.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthStatusDetail: str
        """
        self._IP = None
        self._Port = None
        self._HealthStatus = None
        self._TargetId = None
        self._HealthStatusDetail = None

    @property
    def IP(self):
        """Private IP of the target
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Port(self):
        """Port bound to the target
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def HealthStatus(self):
        """Current health status. Valid values: true: healthy; false: unhealthy (e.g., check not started, checking, or exceptional status). CLB instance will route traffic to only healthy real servers whose weights are greater than 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def TargetId(self):
        """Instance ID of the target
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def HealthStatusDetail(self):
        """Detailed information of the current health status. Valid values: Alive: healthy; Dead: exceptional; Unknown: check not started/checking/unknown status; Close: health check not configured.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HealthStatusDetail

    @HealthStatusDetail.setter
    def HealthStatusDetail(self, HealthStatusDetail):
        self._HealthStatusDetail = HealthStatusDetail


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Port = params.get("Port")
        self._HealthStatus = params.get("HealthStatus")
        self._TargetId = params.get("TargetId")
        self._HealthStatusDetail = params.get("HealthStatusDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetsWeightRule(AbstractModel):
    """Description of targets and their weights

    """

    def __init__(self):
        r"""
        :param _ListenerId: CLB listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param _Targets: List of real servers for which to modify the weights
Note: this field may return null, indicating that no valid values can be obtained.
        :type Targets: list of Target
        :param _Weight: New forwarding weight of the real server. Value range: 0–100.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        """
        self._ListenerId = None
        self._Targets = None
        self._Weight = None

    @property
    def ListenerId(self):
        """CLB listener ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        """List of real servers for which to modify the weights
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Target
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def Weight(self):
        """New forwarding weight of the real server. Value range: 0–100.
Note: this field may return null, indicating that no valid values can be obtained.
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
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInput(AbstractModel):
    """Task query

    """

    def __init__(self):
        r"""
        :param _Operation: Operation name, i.e., API name, such as `CreateImage`
        :type Operation: str
        :param _TaskId: Task ID
        :type TaskId: str
        """
        self._Operation = None
        self._TaskId = None

    @property
    def Operation(self):
        """Operation name, i.e., API name, such as `CreateImage`
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def TaskId(self):
        """Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOutput(AbstractModel):
    """Output parameter of the task query

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _Message: Status description
        :type Message: str
        :param _Status: Status value. Valid values: SUCCESS, FAILED, OPERATING
        :type Status: str
        :param _AddTime: Task submission time
        :type AddTime: str
        :param _EndTime: Task end time
        :type EndTime: str
        :param _Operation: Operation name
        :type Operation: str
        """
        self._TaskId = None
        self._Message = None
        self._Status = None
        self._AddTime = None
        self._EndTime = None
        self._Operation = None

    @property
    def TaskId(self):
        """Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Message(self):
        """Status description
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Status(self):
        """Status value. Valid values: SUCCESS, FAILED, OPERATING
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTime(self):
        """Task submission time
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def EndTime(self):
        """Task end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Operation(self):
        """Operation name
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Message = params.get("Message")
        self._Status = params.get("Status")
        self._AddTime = params.get("AddTime")
        self._EndTime = params.get("EndTime")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: List of IDs of the instances to be terminated.
        :type InstanceIdSet: list of str
        :param _TerminateDelay: Whether to enable scheduled termination. Default value: no.
        :type TerminateDelay: bool
        :param _TerminateTime: Scheduled termination time, such as `2019-08-05 12:01:30`. If you don't enable scheduled termination, you can ignore this parameter.
        :type TerminateTime: str
        :param _AssociatedResourceDestroy: Whether to delete the bound ENI and EIP. Default value: true.
true: the ENI and EIP will also be deleted;
false: only the server will be terminated, while the ENI and EIP will be retained.
        :type AssociatedResourceDestroy: bool
        """
        self._InstanceIdSet = None
        self._TerminateDelay = None
        self._TerminateTime = None
        self._AssociatedResourceDestroy = None

    @property
    def InstanceIdSet(self):
        """List of IDs of the instances to be terminated.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def TerminateDelay(self):
        """Whether to enable scheduled termination. Default value: no.
        :rtype: bool
        """
        return self._TerminateDelay

    @TerminateDelay.setter
    def TerminateDelay(self, TerminateDelay):
        self._TerminateDelay = TerminateDelay

    @property
    def TerminateTime(self):
        """Scheduled termination time, such as `2019-08-05 12:01:30`. If you don't enable scheduled termination, you can ignore this parameter.
        :rtype: str
        """
        return self._TerminateTime

    @TerminateTime.setter
    def TerminateTime(self, TerminateTime):
        self._TerminateTime = TerminateTime

    @property
    def AssociatedResourceDestroy(self):
        """Whether to delete the bound ENI and EIP. Default value: true.
true: the ENI and EIP will also be deleted;
false: only the server will be terminated, while the ENI and EIP will be retained.
        :rtype: bool
        """
        return self._AssociatedResourceDestroy

    @AssociatedResourceDestroy.setter
    def AssociatedResourceDestroy(self, AssociatedResourceDestroy):
        self._AssociatedResourceDestroy = AssociatedResourceDestroy


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._TerminateDelay = params.get("TerminateDelay")
        self._TerminateTime = params.get("TerminateTime")
        self._AssociatedResourceDestroy = params.get("AssociatedResourceDestroy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class VirtualPrivateCloud(AbstractModel):
    """VPC information configuration.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID, such as `vpc-xxx`.
        :type VpcId: str
        :param _SubnetId: Subnet ID of the VPC, such as `subnet-xxx`.
        :type SubnetId: str
        :param _AsVpcGateway: Whether it is used as a public gateway. The public gateway can be used only when the instance has a public IP and resides in a VPC. Valid values:
TRUE: yes
FALSE: no

Default value: FALSE.
        :type AsVpcGateway: bool
        :param _PrivateIpAddresses: Array of VPC subnet IPs. This parameter can be used to create instances or modify the VPC attributes of instances.
        :type PrivateIpAddresses: list of str
        :param _Ipv6AddressCount: Number of the IPv6 addresses to be randomly generated for the ENI.
        :type Ipv6AddressCount: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._AsVpcGateway = None
        self._PrivateIpAddresses = None
        self._Ipv6AddressCount = None

    @property
    def VpcId(self):
        """VPC ID, such as `vpc-xxx`.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID of the VPC, such as `subnet-xxx`.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AsVpcGateway(self):
        """Whether it is used as a public gateway. The public gateway can be used only when the instance has a public IP and resides in a VPC. Valid values:
TRUE: yes
FALSE: no

Default value: FALSE.
        :rtype: bool
        """
        return self._AsVpcGateway

    @AsVpcGateway.setter
    def AsVpcGateway(self, AsVpcGateway):
        self._AsVpcGateway = AsVpcGateway

    @property
    def PrivateIpAddresses(self):
        """Array of VPC subnet IPs. This parameter can be used to create instances or modify the VPC attributes of instances.
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Ipv6AddressCount(self):
        """Number of the IPv6 addresses to be randomly generated for the ENI.
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AsVpcGateway = params.get("AsVpcGateway")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """VPC object.

    """

    def __init__(self):
        r"""
        :param _VpcName: VPC name.
        :type VpcName: str
        :param _VpcId: VPC instance ID, such as `vpc-azd4dt1c`.
        :type VpcId: str
        :param _CidrBlock: IPv4 CIDR block of the VPC.
        :type CidrBlock: str
        :param _IsDefault: Whether it is the default VPC.
        :type IsDefault: bool
        :param _EnableMulticast: Whether to enable multicast.
        :type EnableMulticast: bool
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _DnsServerSet: List of DNS servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DnsServerSet: list of str
        :param _DomainName: DHCP domain option value.
        :type DomainName: str
        :param _DhcpOptionsId: DHCP option set ID.
        :type DhcpOptionsId: str
        :param _EnableDhcp: Whether to enable DHCP.
        :type EnableDhcp: bool
        :param _Ipv6CidrBlock: IPv6 CIDR block of the VPC.
        :type Ipv6CidrBlock: str
        :param _TagSet: Tag key-value pair
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagSet: list of Tag
        :param _AssistantCidrSet: Secondary CIDR block
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssistantCidrSet: list of AssistantCidr
        :param _Region: Region
        :type Region: str
        :param _Description: Description
        :type Description: str
        :param _RegionName: Region name
        :type RegionName: str
        :param _SubnetCount: Number of included subnets
        :type SubnetCount: int
        :param _InstanceCount: Number of included instances
        :type InstanceCount: int
        """
        self._VpcName = None
        self._VpcId = None
        self._CidrBlock = None
        self._IsDefault = None
        self._EnableMulticast = None
        self._CreatedTime = None
        self._DnsServerSet = None
        self._DomainName = None
        self._DhcpOptionsId = None
        self._EnableDhcp = None
        self._Ipv6CidrBlock = None
        self._TagSet = None
        self._AssistantCidrSet = None
        self._Region = None
        self._Description = None
        self._RegionName = None
        self._SubnetCount = None
        self._InstanceCount = None

    @property
    def VpcName(self):
        """VPC name.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcId(self):
        """VPC instance ID, such as `vpc-azd4dt1c`.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def CidrBlock(self):
        """IPv4 CIDR block of the VPC.
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def IsDefault(self):
        """Whether it is the default VPC.
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def EnableMulticast(self):
        """Whether to enable multicast.
        :rtype: bool
        """
        return self._EnableMulticast

    @EnableMulticast.setter
    def EnableMulticast(self, EnableMulticast):
        self._EnableMulticast = EnableMulticast

    @property
    def CreatedTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DnsServerSet(self):
        """List of DNS servers.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DnsServerSet

    @DnsServerSet.setter
    def DnsServerSet(self, DnsServerSet):
        self._DnsServerSet = DnsServerSet

    @property
    def DomainName(self):
        """DHCP domain option value.
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def DhcpOptionsId(self):
        """DHCP option set ID.
        :rtype: str
        """
        return self._DhcpOptionsId

    @DhcpOptionsId.setter
    def DhcpOptionsId(self, DhcpOptionsId):
        self._DhcpOptionsId = DhcpOptionsId

    @property
    def EnableDhcp(self):
        """Whether to enable DHCP.
        :rtype: bool
        """
        return self._EnableDhcp

    @EnableDhcp.setter
    def EnableDhcp(self, EnableDhcp):
        self._EnableDhcp = EnableDhcp

    @property
    def Ipv6CidrBlock(self):
        """IPv6 CIDR block of the VPC.
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock

    @property
    def TagSet(self):
        """Tag key-value pair
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def AssistantCidrSet(self):
        """Secondary CIDR block
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of AssistantCidr
        """
        return self._AssistantCidrSet

    @AssistantCidrSet.setter
    def AssistantCidrSet(self, AssistantCidrSet):
        self._AssistantCidrSet = AssistantCidrSet

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RegionName(self):
        """Region name
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def SubnetCount(self):
        """Number of included subnets
        :rtype: int
        """
        return self._SubnetCount

    @SubnetCount.setter
    def SubnetCount(self, SubnetCount):
        self._SubnetCount = SubnetCount

    @property
    def InstanceCount(self):
        """Number of included instances
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount


    def _deserialize(self, params):
        self._VpcName = params.get("VpcName")
        self._VpcId = params.get("VpcId")
        self._CidrBlock = params.get("CidrBlock")
        self._IsDefault = params.get("IsDefault")
        self._EnableMulticast = params.get("EnableMulticast")
        self._CreatedTime = params.get("CreatedTime")
        self._DnsServerSet = params.get("DnsServerSet")
        self._DomainName = params.get("DomainName")
        self._DhcpOptionsId = params.get("DhcpOptionsId")
        self._EnableDhcp = params.get("EnableDhcp")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        if params.get("AssistantCidrSet") is not None:
            self._AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self._AssistantCidrSet.append(obj)
        self._Region = params.get("Region")
        self._Description = params.get("Description")
        self._RegionName = params.get("RegionName")
        self._SubnetCount = params.get("SubnetCount")
        self._InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """Zone information

    """

    def __init__(self):
        r"""
        :param _ZoneId: ZoneId
        :type ZoneId: int
        :param _ZoneName: ZoneName
        :type ZoneName: str
        :param _Zone: Zone
        :type Zone: str
        """
        self._ZoneId = None
        self._ZoneName = None
        self._Zone = None

    @property
    def ZoneId(self):
        """ZoneId
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """ZoneName
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Zone(self):
        """Zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInstanceCountISP(AbstractModel):
    """Combination of the instance AZ, number of instances to be created, and ISP;

    """

    def __init__(self):
        r"""
        :param _Zone: The AZ in which to create an instance.
        :type Zone: str
        :param _InstanceCount: Number of instances to be created in the current AZ.
        :type InstanceCount: int
        :param _ISP: ISP name. Valid values:
CTCC: China Telecom
CUCC: China Unicom
CMCC: China Mobile
If there are multiple ISP names, you need to separate them by semicolons, such as `CMCC;CUCC;CTCC`. To use multiple ISPs, contact Tencent Cloud customer service for assistance.
        :type ISP: str
        :param _VpcId: ID of the specified VPC. You must specify both `SubnetId` and `VpcId` or neither
        :type VpcId: str
        :param _SubnetId: ID of the specified subnet. You must specify both `SubnetId` and `VpcId` or neither
        :type SubnetId: str
        :param _PrivateIpAddresses: Private IP of the specified primary ENI. You must specify both `SubnetId` and `VpcId` at the same time. The number of IP addresses must be the same as `InstanceCount`. You can get the private IP of the secondary ENI of a multi-IP server through DHCP in the same subnet.
        :type PrivateIpAddresses: list of str
        :param _Ipv6AddressCount: Number of the IPv6 addresses to be randomly generated for the ENI, which cannot be greater than 1.
        :type Ipv6AddressCount: int
        """
        self._Zone = None
        self._InstanceCount = None
        self._ISP = None
        self._VpcId = None
        self._SubnetId = None
        self._PrivateIpAddresses = None
        self._Ipv6AddressCount = None

    @property
    def Zone(self):
        """The AZ in which to create an instance.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceCount(self):
        """Number of instances to be created in the current AZ.
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def ISP(self):
        """ISP name. Valid values:
CTCC: China Telecom
CUCC: China Unicom
CMCC: China Mobile
If there are multiple ISP names, you need to separate them by semicolons, such as `CMCC;CUCC;CTCC`. To use multiple ISPs, contact Tencent Cloud customer service for assistance.
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def VpcId(self):
        """ID of the specified VPC. You must specify both `SubnetId` and `VpcId` or neither
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """ID of the specified subnet. You must specify both `SubnetId` and `VpcId` or neither
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PrivateIpAddresses(self):
        """Private IP of the specified primary ENI. You must specify both `SubnetId` and `VpcId` at the same time. The number of IP addresses must be the same as `InstanceCount`. You can get the private IP of the secondary ENI of a multi-IP server through DHCP in the same subnet.
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Ipv6AddressCount(self):
        """Number of the IPv6 addresses to be randomly generated for the ENI, which cannot be greater than 1.
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceCount = params.get("InstanceCount")
        self._ISP = params.get("ISP")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInstanceInfo(AbstractModel):
    """Instance information of the zone

    """

    def __init__(self):
        r"""
        :param _ZoneName: Zone name
        :type ZoneName: str
        :param _InstanceNum: Number of instances
        :type InstanceNum: int
        """
        self._ZoneName = None
        self._InstanceNum = None

    @property
    def ZoneName(self):
        """Zone name
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceNum(self):
        """Number of instances
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        self._InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        