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


class AvailableProtoStatus(AbstractModel):
    """Versioning - protocol details

    """

    def __init__(self):
        r"""
        :param SaleStatus: Sale status. Valid values: sale_out (sold out), saling (purchasable), no_saling (non-purchasable)
        :type SaleStatus: str
        :param Protocol: Protocol type. Valid values: NFS, CIFS
        :type Protocol: str
        """
        self.SaleStatus = None
        self.Protocol = None


    def _deserialize(self, params):
        self.SaleStatus = params.get("SaleStatus")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableRegion(AbstractModel):
    """Versioning - array of regions

    """

    def __init__(self):
        r"""
        :param Region: Region name, such as "ap-beijing"
        :type Region: str
        :param RegionName: Region name, such as "bj"
        :type RegionName: str
        :param RegionStatus: Region availability. If a region has at least one AZ where resources are purchasable, this value will be `AVAILABLE`; otherwise, it will be `UNAVAILABLE`
        :type RegionStatus: str
        :param Zones: Array of AZs
        :type Zones: list of AvailableZone
        :param RegionCnName: Region name, such as "Guangzhou"
        :type RegionCnName: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionStatus = None
        self.Zones = None
        self.RegionCnName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionStatus = params.get("RegionStatus")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = AvailableZone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RegionCnName = params.get("RegionCnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableType(AbstractModel):
    """Versioning - array of classes

    """

    def __init__(self):
        r"""
        :param Protocols: Protocol and sale details
        :type Protocols: list of AvailableProtoStatus
        :param Type: Storage class. Valid values: `SD` (standard storage) and `HP` (high-performance storage)
        :type Type: str
        :param Prepayment: Indicates whether prepaid is supported. `true`: yes; `false`: no
        :type Prepayment: bool
        """
        self.Protocols = None
        self.Type = None
        self.Prepayment = None


    def _deserialize(self, params):
        if params.get("Protocols") is not None:
            self.Protocols = []
            for item in params.get("Protocols"):
                obj = AvailableProtoStatus()
                obj._deserialize(item)
                self.Protocols.append(obj)
        self.Type = params.get("Type")
        self.Prepayment = params.get("Prepayment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableZone(AbstractModel):
    """Versioning - array of AZs

    """

    def __init__(self):
        r"""
        :param Zone: AZ name
        :type Zone: str
        :param ZoneId: AZ ID
        :type ZoneId: int
        :param ZoneCnName: Chinese name of an AZ
        :type ZoneCnName: str
        :param Types: Array of classes
        :type Types: list of AvailableType
        :param ZoneName: Chinese and English names of an AZ
        :type ZoneName: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneCnName = None
        self.Types = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneCnName = params.get("ZoneCnName")
        if params.get("Types") is not None:
            self.Types = []
            for item in params.get("Types"):
                obj = AvailableType()
                obj._deserialize(item)
                self.Types.append(obj)
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsFileSystemRequest(AbstractModel):
    """CreateCfsFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param Zone: AZ name, such as "ap-beijing-1". For the list of regions and AZs, please see [Overview](https://intl.cloud.tencent.com/document/product/582/13225?from_cn_redirect=1)
        :type Zone: str
        :param NetInterface: Network type. Valid values: `VPC` (private network), `BASIC` (classic network), `CCN` (Cloud Connect Network). You must set this parameter to `CCN` if you use the Turbo series. Classic network will be phased out and is not recommended.
        :type NetInterface: str
        :param PGroupId: Permission group ID (required for Standard and High-Performance). For the Turbo series, set it to `pgroupbasic`.
        :type PGroupId: str
        :param Protocol: File system protocol. Valid values: `NFS`, `CIFS`, `TURBO`. If this parameter is left empty, `NFS` is used by default. For the Turbo series, you must set this parameter to `TURBO`.
        :type Protocol: str
        :param StorageType: Storage class of the file system. Valid values: `SD` (Standard), `HP` (High-Performance), `TB` (Standard Turbo), `TP` (High-Performance Turbo)
        :type StorageType: str
        :param VpcId: VPC ID. This field is required if network type is VPC.
        :type VpcId: str
        :param SubnetId: Subnet ID. This field is required if network type is VPC.
        :type SubnetId: str
        :param MountIP: IP address (this parameter supports only the VPC network type, and the Turbo series is not supported). If this parameter is left empty, a random IP in the subnet will be assigned.
        :type MountIP: str
        :param FsName: Custom file system name
        :type FsName: str
        :param ResourceTags: File system tag
        :type ResourceTags: list of TagInfo
        :param ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed. This string is valid for 2 hours.
        :type ClientToken: str
        :param CcnId: CCN instance ID (required if the network type is CCN)
        :type CcnId: str
        :param CidrBlock: CCN IP range used by the CFS (required if the network type is CCN), which cannot conflict with other IP ranges bound in CCN
        :type CidrBlock: str
        :param Capacity: File system capacity, in GiB (required for the Turbo series). For Standard Turbo, the minimum purchase required is 40,960 GiB (40 TiB) and the expansion increment is 20,480 GiB (20 TiB). For High-Performance Turbo, the minimum purchase required is 20,480 GiB (20 TiB) and the expansion increment is 10,240 GiB (10 TiB).
        :type Capacity: int
        """
        self.Zone = None
        self.NetInterface = None
        self.PGroupId = None
        self.Protocol = None
        self.StorageType = None
        self.VpcId = None
        self.SubnetId = None
        self.MountIP = None
        self.FsName = None
        self.ResourceTags = None
        self.ClientToken = None
        self.CcnId = None
        self.CidrBlock = None
        self.Capacity = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NetInterface = params.get("NetInterface")
        self.PGroupId = params.get("PGroupId")
        self.Protocol = params.get("Protocol")
        self.StorageType = params.get("StorageType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.MountIP = params.get("MountIP")
        self.FsName = params.get("FsName")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.ClientToken = params.get("ClientToken")
        self.CcnId = params.get("CcnId")
        self.CidrBlock = params.get("CidrBlock")
        self.Capacity = params.get("Capacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsFileSystemResponse(AbstractModel):
    """CreateCfsFileSystem response structure.

    """

    def __init__(self):
        r"""
        :param CreationTime: File system creation time
        :type CreationTime: str
        :param CreationToken: Custom file system name
        :type CreationToken: str
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param LifeCycleState: File system status. Valid values: `creating`, `create_failed`, `available`, `unserviced`, `upgrading`, `deleting`
        :type LifeCycleState: str
        :param SizeByte: Storage used by the file system, in bytes
        :type SizeByte: int
        :param ZoneId: AZ ID
        :type ZoneId: int
        :param FsName: Custom file system name
        :type FsName: str
        :param Encrypted: Whether a file system is encrypted
        :type Encrypted: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CreationTime = None
        self.CreationToken = None
        self.FileSystemId = None
        self.LifeCycleState = None
        self.SizeByte = None
        self.ZoneId = None
        self.FsName = None
        self.Encrypted = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.LifeCycleState = params.get("LifeCycleState")
        self.SizeByte = params.get("SizeByte")
        self.ZoneId = params.get("ZoneId")
        self.FsName = params.get("FsName")
        self.Encrypted = params.get("Encrypted")
        self.RequestId = params.get("RequestId")


class CreateCfsPGroupRequest(AbstractModel):
    """CreateCfsPGroup request structure.

    """

    def __init__(self):
        r"""
        :param Name: Permission group name, which can contain 1-64 Chinese characters, letters, numbers, underscores, or dashes
        :type Name: str
        :param DescInfo: Permission group description, which can contain 1-255 characters
        :type DescInfo: str
        """
        self.Name = None
        self.DescInfo = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsPGroupResponse(AbstractModel):
    """CreateCfsPGroup response structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param Name: Permission group name
        :type Name: str
        :param DescInfo: Permission group description
        :type DescInfo: str
        :param BindCfsNum: The number of file systems bound to this permission group
        :type BindCfsNum: int
        :param CDate: Permission group creation time
        :type CDate: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.BindCfsNum = None
        self.CDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.BindCfsNum = params.get("BindCfsNum")
        self.CDate = params.get("CDate")
        self.RequestId = params.get("RequestId")


class CreateCfsRuleRequest(AbstractModel):
    """CreateCfsRule request structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param AuthClientIp: You can enter a single IP or IP range, such as 10.1.10.11 or 10.10.1.0/24. The default visiting address is `*`, indicating that all IPs are allowed. Please note that you need to enter the CVM instance's private IP here.
        :type AuthClientIp: str
        :param Priority: Rule priority. Value range: 1-100. 1 represents the highest priority, while 100 the lowest
        :type Priority: int
        :param RWPermission: Read/write permission. Valid values: RO (read-only), RW (read & write). Default value: RO
        :type RWPermission: str
        :param UserPermission: User permission. Valid values: all_squash, no_all_squash, root_squash, no_root_squash. Specifically, all_squash: any visiting user will be mapped to an anonymous user or user group; no_all_squash: a visiting user will be first matched with a local user, and if the match fails, it will be mapped to an anonymous user or user group; root_squash: a visiting root user will be mapped to an anonymous user or user group; no_root_squash: a visiting root user will be allowed to maintain root account permissions. Default value: root_squash.
        :type UserPermission: str
        """
        self.PGroupId = None
        self.AuthClientIp = None
        self.Priority = None
        self.RWPermission = None
        self.UserPermission = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.Priority = params.get("Priority")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsRuleResponse(AbstractModel):
    """CreateCfsRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
        :type RuleId: str
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param AuthClientIp: Client IP
        :type AuthClientIp: str
        :param RWPermission: Read & write permissions
        :type RWPermission: str
        :param UserPermission: User permission
        :type UserPermission: str
        :param Priority: Priority
        :type Priority: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.PGroupId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.PGroupId = params.get("PGroupId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")


class DeleteCfsFileSystemRequest(AbstractModel):
    """DeleteCfsFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID. Note: please call the `DeleteMountTarget` API to delete the mount target first before deleting a file system; otherwise, the delete operation will fail.
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsFileSystemResponse(AbstractModel):
    """DeleteCfsFileSystem response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCfsPGroupRequest(AbstractModel):
    """DeleteCfsPGroup request structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        """
        self.PGroupId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsPGroupResponse(AbstractModel):
    """DeleteCfsPGroup response structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param AppId: User ID
        :type AppId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PGroupId = None
        self.AppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.AppId = params.get("AppId")
        self.RequestId = params.get("RequestId")


class DeleteCfsRuleRequest(AbstractModel):
    """DeleteCfsRule request structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param RuleId: Rule ID
        :type RuleId: str
        """
        self.PGroupId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsRuleResponse(AbstractModel):
    """DeleteCfsRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
        :type RuleId: str
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.PGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.PGroupId = params.get("PGroupId")
        self.RequestId = params.get("RequestId")


class DeleteMountTargetRequest(AbstractModel):
    """DeleteMountTarget request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param MountTargetId: Mount target ID
        :type MountTargetId: str
        """
        self.FileSystemId = None
        self.MountTargetId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.MountTargetId = params.get("MountTargetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMountTargetResponse(AbstractModel):
    """DeleteMountTarget response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAvailableZoneInfoRequest(AbstractModel):
    """DescribeAvailableZoneInfo request structure.

    """


class DescribeAvailableZoneInfoResponse(AbstractModel):
    """DescribeAvailableZoneInfo response structure.

    """

    def __init__(self):
        r"""
        :param RegionZones: Information such as resource availability in each AZ and the supported storage classes and protocols
        :type RegionZones: list of AvailableRegion
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegionZones = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionZones") is not None:
            self.RegionZones = []
            for item in params.get("RegionZones"):
                obj = AvailableRegion()
                obj._deserialize(item)
                self.RegionZones.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsFileSystemClientsRequest(AbstractModel):
    """DescribeCfsFileSystemClients request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsFileSystemClientsResponse(AbstractModel):
    """DescribeCfsFileSystemClients response structure.

    """

    def __init__(self):
        r"""
        :param ClientList: Client list
        :type ClientList: list of FileSystemClient
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClientList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClientList") is not None:
            self.ClientList = []
            for item in params.get("ClientList"):
                obj = FileSystemClient()
                obj._deserialize(item)
                self.ClientList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsFileSystemsRequest(AbstractModel):
    """DescribeCfsFileSystems request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        """
        self.FileSystemId = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsFileSystemsResponse(AbstractModel):
    """DescribeCfsFileSystems response structure.

    """

    def __init__(self):
        r"""
        :param FileSystems: File system information
        :type FileSystems: list of FileSystemInfo
        :param TotalCount: Total number of file systems
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FileSystems = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystems") is not None:
            self.FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystemInfo()
                obj._deserialize(item)
                self.FileSystems.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCfsPGroupsRequest(AbstractModel):
    """DescribeCfsPGroups request structure.

    """


class DescribeCfsPGroupsResponse(AbstractModel):
    """DescribeCfsPGroups response structure.

    """

    def __init__(self):
        r"""
        :param PGroupList: Permission group information list
        :type PGroupList: list of PGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PGroupList") is not None:
            self.PGroupList = []
            for item in params.get("PGroupList"):
                obj = PGroupInfo()
                obj._deserialize(item)
                self.PGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsRulesRequest(AbstractModel):
    """DescribeCfsRules request structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        """
        self.PGroupId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsRulesResponse(AbstractModel):
    """DescribeCfsRules response structure.

    """

    def __init__(self):
        r"""
        :param RuleList: List of permission group rules
        :type RuleList: list of PGroupRuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = PGroupRuleInfo()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsServiceStatusRequest(AbstractModel):
    """DescribeCfsServiceStatus request structure.

    """


class DescribeCfsServiceStatusResponse(AbstractModel):
    """DescribeCfsServiceStatus response structure.

    """

    def __init__(self):
        r"""
        :param CfsServiceStatus: Current status of the CFS service for this user. Valid values: none (not activated), creating (activating), created (activated)
        :type CfsServiceStatus: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CfsServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CfsServiceStatus = params.get("CfsServiceStatus")
        self.RequestId = params.get("RequestId")


class DescribeMountTargetsRequest(AbstractModel):
    """DescribeMountTargets request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountTargetsResponse(AbstractModel):
    """DescribeMountTargets response structure.

    """

    def __init__(self):
        r"""
        :param MountTargets: Mount target details
        :type MountTargets: list of MountInfo
        :param NumberOfMountTargets: The number of mount targets
        :type NumberOfMountTargets: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MountTargets = None
        self.NumberOfMountTargets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountTargets") is not None:
            self.MountTargets = []
            for item in params.get("MountTargets"):
                obj = MountInfo()
                obj._deserialize(item)
                self.MountTargets.append(obj)
        self.NumberOfMountTargets = params.get("NumberOfMountTargets")
        self.RequestId = params.get("RequestId")


class FileSystemClient(AbstractModel):
    """Information on the file system client

    """

    def __init__(self):
        r"""
        :param CfsVip: IP address of the file system
        :type CfsVip: str
        :param ClientIp: Client IP
        :type ClientIp: str
        :param VpcId: File system VPCID
        :type VpcId: str
        :param Zone: Name of the availability zone, e.g. ap-beijing-1. For more information, see regions and availability zones in the Overview document
        :type Zone: str
        :param ZoneName: AZ name
        :type ZoneName: str
        :param MountDirectory: Path in which the file system is mounted to the client
        :type MountDirectory: str
        """
        self.CfsVip = None
        self.ClientIp = None
        self.VpcId = None
        self.Zone = None
        self.ZoneName = None
        self.MountDirectory = None


    def _deserialize(self, params):
        self.CfsVip = params.get("CfsVip")
        self.ClientIp = params.get("ClientIp")
        self.VpcId = params.get("VpcId")
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.MountDirectory = params.get("MountDirectory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSystemInfo(AbstractModel):
    """Basic information of a file system

    """

    def __init__(self):
        r"""
        :param CreationTime: Creation time
        :type CreationTime: str
        :param CreationToken: Custom name
        :type CreationToken: str
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param LifeCycleState: File system status
        :type LifeCycleState: str
        :param SizeByte: Used file system capacity
        :type SizeByte: int
        :param SizeLimit: Maximum storage limit of a file system
        :type SizeLimit: int
        :param ZoneId: Region ID
        :type ZoneId: int
        :param Zone: Region name
        :type Zone: str
        :param Protocol: File system protocol type
        :type Protocol: str
        :param StorageType: File system storage class
        :type StorageType: str
        :param StorageResourcePkg: Prepaid storage pack bound with the file system
        :type StorageResourcePkg: str
        :param BandwidthResourcePkg: Prepaid bandwidth pack bound to a file system (not supported currently)
        :type BandwidthResourcePkg: str
        :param PGroup: Information of permission groups bound to a file system
        :type PGroup: :class:`tencentcloud.cfs.v20190719.models.PGroup`
        :param FsName: Custom name
        :type FsName: str
        :param Encrypted: Whether a file system is encrypted
        :type Encrypted: bool
        :param KmsKeyId: Key used for encryption, which can be the key ID or ARN
        :type KmsKeyId: str
        :param AppId: Application ID
        :type AppId: int
        :param BandwidthLimit: The upper limit on the file system’s throughput, which is determined based on its current usage, and bound resource packs for both storage and throughput
        :type BandwidthLimit: float
        :param Capacity: Total capacity of the file system
        :type Capacity: int
        :param Tags: File system tag list
        :type Tags: list of TagInfo
        """
        self.CreationTime = None
        self.CreationToken = None
        self.FileSystemId = None
        self.LifeCycleState = None
        self.SizeByte = None
        self.SizeLimit = None
        self.ZoneId = None
        self.Zone = None
        self.Protocol = None
        self.StorageType = None
        self.StorageResourcePkg = None
        self.BandwidthResourcePkg = None
        self.PGroup = None
        self.FsName = None
        self.Encrypted = None
        self.KmsKeyId = None
        self.AppId = None
        self.BandwidthLimit = None
        self.Capacity = None
        self.Tags = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.LifeCycleState = params.get("LifeCycleState")
        self.SizeByte = params.get("SizeByte")
        self.SizeLimit = params.get("SizeLimit")
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.Protocol = params.get("Protocol")
        self.StorageType = params.get("StorageType")
        self.StorageResourcePkg = params.get("StorageResourcePkg")
        self.BandwidthResourcePkg = params.get("BandwidthResourcePkg")
        if params.get("PGroup") is not None:
            self.PGroup = PGroup()
            self.PGroup._deserialize(params.get("PGroup"))
        self.FsName = params.get("FsName")
        self.Encrypted = params.get("Encrypted")
        self.KmsKeyId = params.get("KmsKeyId")
        self.AppId = params.get("AppId")
        self.BandwidthLimit = params.get("BandwidthLimit")
        self.Capacity = params.get("Capacity")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MountInfo(AbstractModel):
    """Mount target information

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param MountTargetId: Mount target ID
        :type MountTargetId: str
        :param IpAddress: Mount target IP
        :type IpAddress: str
        :param FSID: Mount root-directory
        :type FSID: str
        :param LifeCycleState: Mount target status
        :type LifeCycleState: str
        :param NetworkInterface: Network type
        :type NetworkInterface: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param VpcName: VPC name
        :type VpcName: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param SubnetName: Subnet name
        :type SubnetName: str
        :param CcnID: CCN instance ID used by CFS Turbo
        :type CcnID: str
        :param CidrBlock: CCN IP range used by CFS Turbo
        :type CidrBlock: str
        """
        self.FileSystemId = None
        self.MountTargetId = None
        self.IpAddress = None
        self.FSID = None
        self.LifeCycleState = None
        self.NetworkInterface = None
        self.VpcId = None
        self.VpcName = None
        self.SubnetId = None
        self.SubnetName = None
        self.CcnID = None
        self.CidrBlock = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.MountTargetId = params.get("MountTargetId")
        self.IpAddress = params.get("IpAddress")
        self.FSID = params.get("FSID")
        self.LifeCycleState = params.get("LifeCycleState")
        self.NetworkInterface = params.get("NetworkInterface")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CcnID = params.get("CcnID")
        self.CidrBlock = params.get("CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroup(AbstractModel):
    """Information of permission groups bound to a file system

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param Name: Permission group name
        :type Name: str
        """
        self.PGroupId = None
        self.Name = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroupInfo(AbstractModel):
    """Array of permission groups

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param Name: Permission group name
        :type Name: str
        :param DescInfo: Description
        :type DescInfo: str
        :param CDate: Creation time
        :type CDate: str
        :param BindCfsNum: The number of bound file system
        :type BindCfsNum: int
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.CDate = None
        self.BindCfsNum = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.CDate = params.get("CDate")
        self.BindCfsNum = params.get("BindCfsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroupRuleInfo(AbstractModel):
    """List of permission group rules

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
        :type RuleId: str
        :param AuthClientIp: Client IP allowed for access
        :type AuthClientIp: str
        :param RWPermission: Read/write permission. ro: read-only; rw: read & write
        :type RWPermission: str
        :param UserPermission: User permission. all_squash: any visiting user will be mapped to an anonymous user or user group; no_all_squash: a visiting user will be first matched with a local user, and if the match fails, it will be mapped to an anonymous user or user group; root_squash: a visiting root user will be mapped to an anonymous user or user group; no_root_squash: a visiting root user will be allowed to maintain root account permissions.
        :type UserPermission: str
        :param Priority: Rule priority. Value range: 1-100. 1 represents the highest priority, while 100 the lowest
        :type Priority: int
        """
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignUpCfsServiceRequest(AbstractModel):
    """SignUpCfsService request structure.

    """


class SignUpCfsServiceResponse(AbstractModel):
    """SignUpCfsService response structure.

    """

    def __init__(self):
        r"""
        :param CfsServiceStatus: Current status of the CFS service for this user. Valid values: none (not activated), creating (activating), created (activated)
        :type CfsServiceStatus: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CfsServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CfsServiceStatus = params.get("CfsServiceStatus")
        self.RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """Tag information unit

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
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
        


class UpdateCfsFileSystemNameRequest(AbstractModel):
    """UpdateCfsFileSystemName request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param FsName: Custom file system name
        :type FsName: str
        """
        self.FileSystemId = None
        self.FsName = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.FsName = params.get("FsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemNameResponse(AbstractModel):
    """UpdateCfsFileSystemName response structure.

    """

    def __init__(self):
        r"""
        :param CreationToken: Custom file system name
        :type CreationToken: str
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param FsName: Custom file system name
        :type FsName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CreationToken = None
        self.FileSystemId = None
        self.FsName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.FsName = params.get("FsName")
        self.RequestId = params.get("RequestId")


class UpdateCfsFileSystemPGroupRequest(AbstractModel):
    """UpdateCfsFileSystemPGroup request structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param FileSystemId: File system ID
        :type FileSystemId: str
        """
        self.PGroupId = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemPGroupResponse(AbstractModel):
    """UpdateCfsFileSystemPGroup response structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PGroupId = None
        self.FileSystemId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.FileSystemId = params.get("FileSystemId")
        self.RequestId = params.get("RequestId")


class UpdateCfsFileSystemSizeLimitRequest(AbstractModel):
    """UpdateCfsFileSystemSizeLimit request structure.

    """

    def __init__(self):
        r"""
        :param FsLimit: File system capacity limit in GB. Value range: 0-1,073,741,824. If 0 is entered, no limit will be imposed on the file system capacity.
        :type FsLimit: int
        :param FileSystemId: File system ID. Currently, only Standard file systems are supported.
        :type FileSystemId: str
        """
        self.FsLimit = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FsLimit = params.get("FsLimit")
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemSizeLimitResponse(AbstractModel):
    """UpdateCfsFileSystemSizeLimit response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateCfsPGroupRequest(AbstractModel):
    """UpdateCfsPGroup request structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param Name: Permission group name, which can contain 1-64 Chinese characters, letters, numbers, underscores, or dashes
        :type Name: str
        :param DescInfo: Permission group description, which can contain 1-255 characters
        :type DescInfo: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsPGroupResponse(AbstractModel):
    """UpdateCfsPGroup response structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param Name: Permission group name
        :type Name: str
        :param DescInfo: Description
        :type DescInfo: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.RequestId = params.get("RequestId")


class UpdateCfsRuleRequest(AbstractModel):
    """UpdateCfsRule request structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param AuthClientIp: You can enter a single IP or IP range, such as 10.1.10.11 or 10.10.1.0/24. The default visiting address is `*`, indicating that all IPs are allowed. Please note that you need to enter the CVM instance's private IP here.
        :type AuthClientIp: str
        :param RWPermission: Read/write permission. Valid values: RO (read-only), RW (read & write). Default value: RO
        :type RWPermission: str
        :param UserPermission: User permission. Valid values: all_squash, no_all_squash, root_squash, no_root_squash. Specifically, all_squash: any visiting user will be mapped to an anonymous user or user group; no_all_squash: a visiting user will be first matched with a local user, and if the match fails, it will be mapped to an anonymous user or user group; root_squash: a visiting root user will be mapped to an anonymous user or user group; no_root_squash: a visiting root user will be allowed to maintain root account permissions. Default value: root_squash.
        :type UserPermission: str
        :param Priority: Rule priority. Value range: 1-100. 1 represents the highest priority, while 100 the lowest
        :type Priority: int
        """
        self.PGroupId = None
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsRuleResponse(AbstractModel):
    """UpdateCfsRule response structure.

    """

    def __init__(self):
        r"""
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param AuthClientIp: Client IP or IP range allowed for access
        :type AuthClientIp: str
        :param RWPermission: Read & write permission
        :type RWPermission: str
        :param UserPermission: User permission
        :type UserPermission: str
        :param Priority: Priority
        :type Priority: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PGroupId = None
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")