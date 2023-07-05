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


class AutoSnapshotPolicyInfo(AbstractModel):
    """Snapshot policy information

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Snapshot policy ID
        :type AutoSnapshotPolicyId: str
        :param _PolicyName: Snapshot policy name
        :type PolicyName: str
        :param _CreationTime: Snapshot policy creation time
        :type CreationTime: str
        :param _FileSystemNums: Number of bound file systems
        :type FileSystemNums: int
        :param _DayOfWeek: The specific day of the week on which to create a snapshot. This parameter is mutually exclusive with `DayOfMonth` and `IntervalDays`.
        :type DayOfWeek: str
        :param _Hour: The hour of a day at which to regularly back up the snapshot
        :type Hour: str
        :param _IsActivated: Whether to activate the scheduled snapshot feature
        :type IsActivated: int
        :param _NextActiveTime: Next time to trigger snapshot
        :type NextActiveTime: str
        :param _Status: Snapshot policy status
        :type Status: str
        :param _AppId: Account ID
        :type AppId: int
        :param _AliveDays: Retention period
        :type AliveDays: int
        :param _RegionName: Region
        :type RegionName: str
        :param _FileSystems: File system information
        :type FileSystems: list of FileSystemByPolicy
        :param _DayOfMonth: The specific day of the month on which to create a snapshot. This parameter is mutually exclusive with `DayOfWeek` and `IntervalDays`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DayOfMonth: str
        :param _IntervalDays: The snapshot interval (1 to 365 days). This parameter is mutually exclusive with `DayOfWeek` and `DayOfMonth`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntervalDays: int
        """
        self._AutoSnapshotPolicyId = None
        self._PolicyName = None
        self._CreationTime = None
        self._FileSystemNums = None
        self._DayOfWeek = None
        self._Hour = None
        self._IsActivated = None
        self._NextActiveTime = None
        self._Status = None
        self._AppId = None
        self._AliveDays = None
        self._RegionName = None
        self._FileSystems = None
        self._DayOfMonth = None
        self._IntervalDays = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def FileSystemNums(self):
        return self._FileSystemNums

    @FileSystemNums.setter
    def FileSystemNums(self, FileSystemNums):
        self._FileSystemNums = FileSystemNums

    @property
    def DayOfWeek(self):
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def NextActiveTime(self):
        return self._NextActiveTime

    @NextActiveTime.setter
    def NextActiveTime(self, NextActiveTime):
        self._NextActiveTime = NextActiveTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AliveDays(self):
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def FileSystems(self):
        return self._FileSystems

    @FileSystems.setter
    def FileSystems(self, FileSystems):
        self._FileSystems = FileSystems

    @property
    def DayOfMonth(self):
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        return self._IntervalDays

    @IntervalDays.setter
    def IntervalDays(self, IntervalDays):
        self._IntervalDays = IntervalDays


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._PolicyName = params.get("PolicyName")
        self._CreationTime = params.get("CreationTime")
        self._FileSystemNums = params.get("FileSystemNums")
        self._DayOfWeek = params.get("DayOfWeek")
        self._Hour = params.get("Hour")
        self._IsActivated = params.get("IsActivated")
        self._NextActiveTime = params.get("NextActiveTime")
        self._Status = params.get("Status")
        self._AppId = params.get("AppId")
        self._AliveDays = params.get("AliveDays")
        self._RegionName = params.get("RegionName")
        if params.get("FileSystems") is not None:
            self._FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystemByPolicy()
                obj._deserialize(item)
                self._FileSystems.append(obj)
        self._DayOfMonth = params.get("DayOfMonth")
        self._IntervalDays = params.get("IntervalDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableProtoStatus(AbstractModel):
    """Versioning - protocol details

    """

    def __init__(self):
        r"""
        :param _SaleStatus: Sale status. Valid values: sale_out (sold out), saling (purchasable), no_saling (non-purchasable)
        :type SaleStatus: str
        :param _Protocol: Protocol type. Valid values: NFS, CIFS
        :type Protocol: str
        """
        self._SaleStatus = None
        self._Protocol = None

    @property
    def SaleStatus(self):
        return self._SaleStatus

    @SaleStatus.setter
    def SaleStatus(self, SaleStatus):
        self._SaleStatus = SaleStatus

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._SaleStatus = params.get("SaleStatus")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableRegion(AbstractModel):
    """Versioning - array of regions

    """

    def __init__(self):
        r"""
        :param _Region: Region name, such as "ap-beijing"
        :type Region: str
        :param _RegionName: Region name, such as "bj"
        :type RegionName: str
        :param _RegionStatus: Region availability. If a region has at least one AZ where resources are purchasable, this value will be `AVAILABLE`; otherwise, it will be `UNAVAILABLE`
        :type RegionStatus: str
        :param _Zones: Array of AZs
        :type Zones: list of AvailableZone
        :param _RegionCnName: Region name, such as "Guangzhou"
        :type RegionCnName: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionStatus = None
        self._Zones = None
        self._RegionCnName = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionStatus(self):
        return self._RegionStatus

    @RegionStatus.setter
    def RegionStatus(self, RegionStatus):
        self._RegionStatus = RegionStatus

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RegionCnName(self):
        return self._RegionCnName

    @RegionCnName.setter
    def RegionCnName(self, RegionCnName):
        self._RegionCnName = RegionCnName


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionStatus = params.get("RegionStatus")
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = AvailableZone()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._RegionCnName = params.get("RegionCnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableType(AbstractModel):
    """Versioning - array of classes

    """

    def __init__(self):
        r"""
        :param _Protocols: Protocol and sale details
        :type Protocols: list of AvailableProtoStatus
        :param _Type: Storage class. Valid values: `SD` (standard storage) and `HP` (high-performance storage)
        :type Type: str
        :param _Prepayment: Indicates whether prepaid is supported. `true`: yes; `false`: no
        :type Prepayment: bool
        """
        self._Protocols = None
        self._Type = None
        self._Prepayment = None

    @property
    def Protocols(self):
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Prepayment(self):
        return self._Prepayment

    @Prepayment.setter
    def Prepayment(self, Prepayment):
        self._Prepayment = Prepayment


    def _deserialize(self, params):
        if params.get("Protocols") is not None:
            self._Protocols = []
            for item in params.get("Protocols"):
                obj = AvailableProtoStatus()
                obj._deserialize(item)
                self._Protocols.append(obj)
        self._Type = params.get("Type")
        self._Prepayment = params.get("Prepayment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableZone(AbstractModel):
    """Versioning - array of AZs

    """

    def __init__(self):
        r"""
        :param _Zone: AZ name
        :type Zone: str
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _ZoneCnName: Chinese name of an AZ
        :type ZoneCnName: str
        :param _Types: Array of classes
        :type Types: list of AvailableType
        :param _ZoneName: Chinese and English names of an AZ
        :type ZoneName: str
        """
        self._Zone = None
        self._ZoneId = None
        self._ZoneCnName = None
        self._Types = None
        self._ZoneName = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneCnName(self):
        return self._ZoneCnName

    @ZoneCnName.setter
    def ZoneCnName(self, ZoneCnName):
        self._ZoneCnName = ZoneCnName

    @property
    def Types(self):
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneCnName = params.get("ZoneCnName")
        if params.get("Types") is not None:
            self._Types = []
            for item in params.get("Types"):
                obj = AvailableType()
                obj._deserialize(item)
                self._Types.append(obj)
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoSnapshotPolicyRequest(AbstractModel):
    """BindAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Snapshot policy ID
        :type AutoSnapshotPolicyId: str
        :param _FileSystemIds: List of file systems
        :type FileSystemIds: str
        """
        self._AutoSnapshotPolicyId = None
        self._FileSystemIds = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def FileSystemIds(self):
        return self._FileSystemIds

    @FileSystemIds.setter
    def FileSystemIds(self, FileSystemIds):
        self._FileSystemIds = FileSystemIds


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._FileSystemIds = params.get("FileSystemIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoSnapshotPolicyResponse(AbstractModel):
    """BindAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Snapshot policy ID
        :type AutoSnapshotPolicyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class BucketInfo(AbstractModel):
    """Bucket information

    """

    def __init__(self):
        r"""
        :param _Name: Bucket name
        :type Name: str
        :param _Region: Bucket region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        """
        self._Name = None
        self._Region = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoSnapshotPolicyRequest(AbstractModel):
    """CreateAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Hour: The time point when to repeat the snapshot operation
        :type Hour: str
        :param _PolicyName: Policy name
        :type PolicyName: str
        :param _DayOfWeek: The day of the week on which to repeat the snapshot operation
        :type DayOfWeek: str
        :param _AliveDays: Snapshot retention period
        :type AliveDays: int
        :param _DayOfMonth: The specific day (day 1 to day 31) of the month on which to automatically create a snapshot.
        :type DayOfMonth: str
        :param _IntervalDays: The snapshot interval, in days.
        :type IntervalDays: int
        """
        self._Hour = None
        self._PolicyName = None
        self._DayOfWeek = None
        self._AliveDays = None
        self._DayOfMonth = None
        self._IntervalDays = None

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def DayOfWeek(self):
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def AliveDays(self):
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays

    @property
    def DayOfMonth(self):
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        return self._IntervalDays

    @IntervalDays.setter
    def IntervalDays(self, IntervalDays):
        self._IntervalDays = IntervalDays


    def _deserialize(self, params):
        self._Hour = params.get("Hour")
        self._PolicyName = params.get("PolicyName")
        self._DayOfWeek = params.get("DayOfWeek")
        self._AliveDays = params.get("AliveDays")
        self._DayOfMonth = params.get("DayOfMonth")
        self._IntervalDays = params.get("IntervalDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoSnapshotPolicyResponse(AbstractModel):
    """CreateAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Snapshot policy ID
        :type AutoSnapshotPolicyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class CreateCfsFileSystemRequest(AbstractModel):
    """CreateCfsFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ name, such as "ap-beijing-1". For the list of regions and AZs, please see [Overview](https://intl.cloud.tencent.com/document/product/582/13225?from_cn_redirect=1)
        :type Zone: str
        :param _NetInterface: Network type. Valid values: `VPC` and `CCN`. Select `VPC` for a Standard or High-Performance file system, and `CCN` for a Standard Turbo or High-Performance Turbo one.
        :type NetInterface: str
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _Protocol: File system protocol. Valid values: `NFS`, `CIFS`, `TURBO`. If this parameter is left empty, `NFS` is used by default. For the Turbo series, you must set this parameter to `TURBO`.
        :type Protocol: str
        :param _StorageType: Storage type of the file system. Valid values: `SD` (Standard), `HP` (High-Performance), `TB` (Standard Turbo), and `TP` (High-Performance Turbo). Default value: `SD`.
        :type StorageType: str
        :param _VpcId: VPC ID. This field is required if network type is VPC.
        :type VpcId: str
        :param _SubnetId: Subnet ID. This field is required if network type is VPC.
        :type SubnetId: str
        :param _MountIP: IP address (this parameter supports only the VPC network type, and the Turbo series is not supported). If this parameter is left empty, a random IP in the subnet will be assigned.
        :type MountIP: str
        :param _FsName: Custom file system name
        :type FsName: str
        :param _ResourceTags: File system tag
        :type ResourceTags: list of TagInfo
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed. This string is valid for 2 hours.
        :type ClientToken: str
        :param _CcnId: CCN instance ID (required if the network type is CCN)
        :type CcnId: str
        :param _CidrBlock: CCN IP range used by the CFS (required if the network type is CCN), which cannot conflict with other IP ranges bound in CCN
        :type CidrBlock: str
        :param _Capacity: File system capacity, in GiB (required for the Turbo series). For Standard Turbo, the minimum purchase required is 40,960 GiB (40 TiB) and the expansion increment is 20,480 GiB (20 TiB). For High-Performance Turbo, the minimum purchase required is 20,480 GiB (20 TiB) and the expansion increment is 10,240 GiB (10 TiB).
        :type Capacity: int
        """
        self._Zone = None
        self._NetInterface = None
        self._PGroupId = None
        self._Protocol = None
        self._StorageType = None
        self._VpcId = None
        self._SubnetId = None
        self._MountIP = None
        self._FsName = None
        self._ResourceTags = None
        self._ClientToken = None
        self._CcnId = None
        self._CidrBlock = None
        self._Capacity = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NetInterface(self):
        return self._NetInterface

    @NetInterface.setter
    def NetInterface(self, NetInterface):
        self._NetInterface = NetInterface

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def MountIP(self):
        return self._MountIP

    @MountIP.setter
    def MountIP(self, MountIP):
        self._MountIP = MountIP

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def CcnId(self):
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Capacity(self):
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._NetInterface = params.get("NetInterface")
        self._PGroupId = params.get("PGroupId")
        self._Protocol = params.get("Protocol")
        self._StorageType = params.get("StorageType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._MountIP = params.get("MountIP")
        self._FsName = params.get("FsName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._ClientToken = params.get("ClientToken")
        self._CcnId = params.get("CcnId")
        self._CidrBlock = params.get("CidrBlock")
        self._Capacity = params.get("Capacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsFileSystemResponse(AbstractModel):
    """CreateCfsFileSystem response structure.

    """

    def __init__(self):
        r"""
        :param _CreationTime: File system creation time
        :type CreationTime: str
        :param _CreationToken: Custom file system name
        :type CreationToken: str
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _LifeCycleState: File system status. Valid values: `creating`, `create_failed`, `available`, `unserviced`, `upgrading`, `deleting`
        :type LifeCycleState: str
        :param _SizeByte: Storage used by the file system, in bytes
        :type SizeByte: int
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _FsName: Custom file system name
        :type FsName: str
        :param _Encrypted: Whether a file system is encrypted
        :type Encrypted: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CreationTime = None
        self._CreationToken = None
        self._FileSystemId = None
        self._LifeCycleState = None
        self._SizeByte = None
        self._ZoneId = None
        self._FsName = None
        self._Encrypted = None
        self._RequestId = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def CreationToken(self):
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def LifeCycleState(self):
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def SizeByte(self):
        return self._SizeByte

    @SizeByte.setter
    def SizeByte(self, SizeByte):
        self._SizeByte = SizeByte

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def Encrypted(self):
        return self._Encrypted

    @Encrypted.setter
    def Encrypted(self, Encrypted):
        self._Encrypted = Encrypted

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._CreationToken = params.get("CreationToken")
        self._FileSystemId = params.get("FileSystemId")
        self._LifeCycleState = params.get("LifeCycleState")
        self._SizeByte = params.get("SizeByte")
        self._ZoneId = params.get("ZoneId")
        self._FsName = params.get("FsName")
        self._Encrypted = params.get("Encrypted")
        self._RequestId = params.get("RequestId")


class CreateCfsPGroupRequest(AbstractModel):
    """CreateCfsPGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Permission group name, which can contain 1-64 Chinese characters, letters, numbers, underscores, or dashes
        :type Name: str
        :param _DescInfo: Permission group description, which can contain 1-255 characters
        :type DescInfo: str
        """
        self._Name = None
        self._DescInfo = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsPGroupResponse(AbstractModel):
    """CreateCfsPGroup response structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _Name: Permission group name
        :type Name: str
        :param _DescInfo: Permission group description
        :type DescInfo: str
        :param _BindCfsNum: The number of file systems bound to this permission group
        :type BindCfsNum: int
        :param _CDate: Permission group creation time
        :type CDate: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PGroupId = None
        self._Name = None
        self._DescInfo = None
        self._BindCfsNum = None
        self._CDate = None
        self._RequestId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo

    @property
    def BindCfsNum(self):
        return self._BindCfsNum

    @BindCfsNum.setter
    def BindCfsNum(self, BindCfsNum):
        self._BindCfsNum = BindCfsNum

    @property
    def CDate(self):
        return self._CDate

    @CDate.setter
    def CDate(self, CDate):
        self._CDate = CDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        self._BindCfsNum = params.get("BindCfsNum")
        self._CDate = params.get("CDate")
        self._RequestId = params.get("RequestId")


class CreateCfsRuleRequest(AbstractModel):
    """CreateCfsRule request structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _AuthClientIp: You can enter a single IP or IP range, such as 10.1.10.11 or 10.10.1.0/24. The default visiting address is `*`, indicating that all IPs are allowed. Please note that you need to enter the CVM instance's private IP here.
        :type AuthClientIp: str
        :param _Priority: Rule priority. Value range: 1-100. 1 represents the highest priority, while 100 the lowest
        :type Priority: int
        :param _RWPermission: Read/write permission. Valid values: RO (read-only), RW (read & write). Default value: RO
        :type RWPermission: str
        :param _UserPermission: User permission. Valid values: all_squash, no_all_squash, root_squash, no_root_squash. Specifically, all_squash: any visiting user will be mapped to an anonymous user or user group; no_all_squash: a visiting user will be first matched with a local user, and if the match fails, it will be mapped to an anonymous user or user group; root_squash: a visiting root user will be mapped to an anonymous user or user group; no_root_squash: a visiting root user will be allowed to maintain root account permissions. Default value: root_squash.
        :type UserPermission: str
        """
        self._PGroupId = None
        self._AuthClientIp = None
        self._Priority = None
        self._RWPermission = None
        self._UserPermission = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def AuthClientIp(self):
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RWPermission(self):
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._Priority = params.get("Priority")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsRuleResponse(AbstractModel):
    """CreateCfsRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _AuthClientIp: Client IP
        :type AuthClientIp: str
        :param _RWPermission: Read & write permissions
        :type RWPermission: str
        :param _UserPermission: User permission
        :type UserPermission: str
        :param _Priority: Priority
        :type Priority: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._PGroupId = None
        self._AuthClientIp = None
        self._RWPermission = None
        self._UserPermission = None
        self._Priority = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def AuthClientIp(self):
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._PGroupId = params.get("PGroupId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        self._Priority = params.get("Priority")
        self._RequestId = params.get("RequestId")


class CreateCfsSnapshotRequest(AbstractModel):
    """CreateCfsSnapshot request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _SnapshotName: Snapshot name
        :type SnapshotName: str
        :param _ResourceTags: Snapshot tag
        :type ResourceTags: list of TagInfo
        """
        self._FileSystemId = None
        self._SnapshotName = None
        self._ResourceTags = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._SnapshotName = params.get("SnapshotName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCfsSnapshotResponse(AbstractModel):
    """CreateCfsSnapshot response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: File system snapshot ID
        :type SnapshotId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotId = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class CreateMigrationTaskRequest(AbstractModel):
    """CreateMigrationTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskName: Migration task name
        :type TaskName: str
        :param _MigrationType: Migration type. Valid values: `0` (bucket) and `1` (list). Default value: `0`.
        :type MigrationType: int
        :param _MigrationMode: Migration mode. Default value: `0` (full migration).
        :type MigrationMode: int
        :param _SrcSecretId: SecretId of the data source account
        :type SrcSecretId: str
        :param _SrcSecretKey: SecretKey of the data source account
        :type SrcSecretKey: str
        :param _FileSystemId: File system instance ID
        :type FileSystemId: str
        :param _FsPath: File system path
        :type FsPath: str
        :param _CoverType: Overwrite policy for files with the same name. Valid values: `0` (retain the file with the latest modified time), `1` (overwrite); and `2` (not overwrite). Default value: `0`.
        :type CoverType: int
        :param _SrcService: Data source service provider. Valid values: `COS` (Tencent Cloud COS), `OSS` (Alibaba Cloud OSS), and `OBS` (Huawei Cloud OBS).
        :type SrcService: str
        :param _BucketName: Data source bucket name. Specify at least one of the bucket name or address.
        :type BucketName: str
        :param _BucketRegion: Data source bucket region
        :type BucketRegion: str
        :param _BucketAddress: Data source bucket address. Specify at least one of the bucket name or address.
        :type BucketAddress: str
        :param _ListAddress: List address. This parameter is required if `MigrationType` is set to `1` (list).
        :type ListAddress: str
        :param _FsName: Target file system name
        :type FsName: str
        :param _BucketPath: Source bucket path, which defaults to `/`
        :type BucketPath: str
        """
        self._TaskName = None
        self._MigrationType = None
        self._MigrationMode = None
        self._SrcSecretId = None
        self._SrcSecretKey = None
        self._FileSystemId = None
        self._FsPath = None
        self._CoverType = None
        self._SrcService = None
        self._BucketName = None
        self._BucketRegion = None
        self._BucketAddress = None
        self._ListAddress = None
        self._FsName = None
        self._BucketPath = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def MigrationType(self):
        return self._MigrationType

    @MigrationType.setter
    def MigrationType(self, MigrationType):
        self._MigrationType = MigrationType

    @property
    def MigrationMode(self):
        return self._MigrationMode

    @MigrationMode.setter
    def MigrationMode(self, MigrationMode):
        self._MigrationMode = MigrationMode

    @property
    def SrcSecretId(self):
        return self._SrcSecretId

    @SrcSecretId.setter
    def SrcSecretId(self, SrcSecretId):
        self._SrcSecretId = SrcSecretId

    @property
    def SrcSecretKey(self):
        return self._SrcSecretKey

    @SrcSecretKey.setter
    def SrcSecretKey(self, SrcSecretKey):
        self._SrcSecretKey = SrcSecretKey

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsPath(self):
        return self._FsPath

    @FsPath.setter
    def FsPath(self, FsPath):
        self._FsPath = FsPath

    @property
    def CoverType(self):
        return self._CoverType

    @CoverType.setter
    def CoverType(self, CoverType):
        self._CoverType = CoverType

    @property
    def SrcService(self):
        return self._SrcService

    @SrcService.setter
    def SrcService(self, SrcService):
        self._SrcService = SrcService

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketRegion(self):
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def BucketAddress(self):
        return self._BucketAddress

    @BucketAddress.setter
    def BucketAddress(self, BucketAddress):
        self._BucketAddress = BucketAddress

    @property
    def ListAddress(self):
        return self._ListAddress

    @ListAddress.setter
    def ListAddress(self, ListAddress):
        self._ListAddress = ListAddress

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def BucketPath(self):
        return self._BucketPath

    @BucketPath.setter
    def BucketPath(self, BucketPath):
        self._BucketPath = BucketPath


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._MigrationType = params.get("MigrationType")
        self._MigrationMode = params.get("MigrationMode")
        self._SrcSecretId = params.get("SrcSecretId")
        self._SrcSecretKey = params.get("SrcSecretKey")
        self._FileSystemId = params.get("FileSystemId")
        self._FsPath = params.get("FsPath")
        self._CoverType = params.get("CoverType")
        self._SrcService = params.get("SrcService")
        self._BucketName = params.get("BucketName")
        self._BucketRegion = params.get("BucketRegion")
        self._BucketAddress = params.get("BucketAddress")
        self._ListAddress = params.get("ListAddress")
        self._FsName = params.get("FsName")
        self._BucketPath = params.get("BucketPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrationTaskResponse(AbstractModel):
    """CreateMigrationTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Migration task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteAutoSnapshotPolicyRequest(AbstractModel):
    """DeleteAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Snapshot policy ID
        :type AutoSnapshotPolicyId: str
        """
        self._AutoSnapshotPolicyId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoSnapshotPolicyResponse(AbstractModel):
    """DeleteAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Snapshot policy ID
        :type AutoSnapshotPolicyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class DeleteCfsFileSystemRequest(AbstractModel):
    """DeleteCfsFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID. Note: please call the `DeleteMountTarget` API to delete the mount target first before deleting a file system; otherwise, the delete operation will fail.
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsFileSystemResponse(AbstractModel):
    """DeleteCfsFileSystem response structure.

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


class DeleteCfsPGroupRequest(AbstractModel):
    """DeleteCfsPGroup request structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        """
        self._PGroupId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsPGroupResponse(AbstractModel):
    """DeleteCfsPGroup response structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _AppId: User ID
        :type AppId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PGroupId = None
        self._AppId = None
        self._RequestId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._AppId = params.get("AppId")
        self._RequestId = params.get("RequestId")


class DeleteCfsRuleRequest(AbstractModel):
    """DeleteCfsRule request structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _RuleId: Rule ID
        :type RuleId: str
        """
        self._PGroupId = None
        self._RuleId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsRuleResponse(AbstractModel):
    """DeleteCfsRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._PGroupId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._PGroupId = params.get("PGroupId")
        self._RequestId = params.get("RequestId")


class DeleteCfsSnapshotRequest(AbstractModel):
    """DeleteCfsSnapshot request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: File system snapshot ID
        :type SnapshotId: str
        :param _SnapshotIds: The list of the IDs of the file system snapshots to be deleted. At least one of `SnapshotId` and `SnapshotIds` must be specified.
        :type SnapshotIds: list of str
        """
        self._SnapshotId = None
        self._SnapshotIds = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._SnapshotIds = params.get("SnapshotIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCfsSnapshotResponse(AbstractModel):
    """DeleteCfsSnapshot response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: File system ID
        :type SnapshotId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotId = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class DeleteMigrationTaskRequest(AbstractModel):
    """DeleteMigrationTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Migration task ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        


class DeleteMigrationTaskResponse(AbstractModel):
    """DeleteMigrationTask response structure.

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


class DeleteMountTargetRequest(AbstractModel):
    """DeleteMountTarget request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _MountTargetId: Mount target ID
        :type MountTargetId: str
        """
        self._FileSystemId = None
        self._MountTargetId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def MountTargetId(self):
        return self._MountTargetId

    @MountTargetId.setter
    def MountTargetId(self, MountTargetId):
        self._MountTargetId = MountTargetId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._MountTargetId = params.get("MountTargetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMountTargetResponse(AbstractModel):
    """DeleteMountTarget response structure.

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


class DescribeAutoSnapshotPoliciesRequest(AbstractModel):
    """DescribeAutoSnapshotPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Snapshot policy ID
        :type AutoSnapshotPolicyId: str
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Page length
        :type Limit: int
        :param _Filters: Filters
        :type Filters: list of Filter
        :param _Order: Ascending or descending order
        :type Order: str
        :param _OrderField: Sorting field
        :type OrderField: str
        """
        self._AutoSnapshotPolicyId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Order = None
        self._OrderField = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

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

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoSnapshotPoliciesResponse(AbstractModel):
    """DescribeAutoSnapshotPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of snapshot policies
        :type TotalCount: int
        :param _AutoSnapshotPolicies: Snapshot policy information
        :type AutoSnapshotPolicies: list of AutoSnapshotPolicyInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoSnapshotPolicies = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoSnapshotPolicies(self):
        return self._AutoSnapshotPolicies

    @AutoSnapshotPolicies.setter
    def AutoSnapshotPolicies(self, AutoSnapshotPolicies):
        self._AutoSnapshotPolicies = AutoSnapshotPolicies

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicies") is not None:
            self._AutoSnapshotPolicies = []
            for item in params.get("AutoSnapshotPolicies"):
                obj = AutoSnapshotPolicyInfo()
                obj._deserialize(item)
                self._AutoSnapshotPolicies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAvailableZoneInfoRequest(AbstractModel):
    """DescribeAvailableZoneInfo request structure.

    """


class DescribeAvailableZoneInfoResponse(AbstractModel):
    """DescribeAvailableZoneInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RegionZones: Information such as resource availability in each AZ and the supported storage classes and protocols
        :type RegionZones: list of AvailableRegion
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegionZones = None
        self._RequestId = None

    @property
    def RegionZones(self):
        return self._RegionZones

    @RegionZones.setter
    def RegionZones(self, RegionZones):
        self._RegionZones = RegionZones

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionZones") is not None:
            self._RegionZones = []
            for item in params.get("RegionZones"):
                obj = AvailableRegion()
                obj._deserialize(item)
                self._RegionZones.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBucketListRequest(AbstractModel):
    """DescribeBucketList request structure.

    """

    def __init__(self):
        r"""
        :param _SrcService: Data source service provider. Valid values: `COS` (Tencent Cloud COS), `OSS` (Alibaba Cloud OSS), and `OBS` (Huawei Cloud OBS).
        :type SrcService: str
        :param _SrcSecretId: SecretId of the data source account

        :type SrcSecretId: str
        :param _SrcSecretKey: SecretKey of the data source account
        :type SrcSecretKey: str
        """
        self._SrcService = None
        self._SrcSecretId = None
        self._SrcSecretKey = None

    @property
    def SrcService(self):
        return self._SrcService

    @SrcService.setter
    def SrcService(self, SrcService):
        self._SrcService = SrcService

    @property
    def SrcSecretId(self):
        return self._SrcSecretId

    @SrcSecretId.setter
    def SrcSecretId(self, SrcSecretId):
        self._SrcSecretId = SrcSecretId

    @property
    def SrcSecretKey(self):
        return self._SrcSecretKey

    @SrcSecretKey.setter
    def SrcSecretKey(self, SrcSecretKey):
        self._SrcSecretKey = SrcSecretKey


    def _deserialize(self, params):
        self._SrcService = params.get("SrcService")
        self._SrcSecretId = params.get("SrcSecretId")
        self._SrcSecretKey = params.get("SrcSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBucketListResponse(AbstractModel):
    """DescribeBucketList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of buckets
        :type TotalCount: int
        :param _BucketList: Bucket list
        :type BucketList: list of BucketInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BucketList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BucketList(self):
        return self._BucketList

    @BucketList.setter
    def BucketList(self, BucketList):
        self._BucketList = BucketList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BucketList") is not None:
            self._BucketList = []
            for item in params.get("BucketList"):
                obj = BucketInfo()
                obj._deserialize(item)
                self._BucketList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsFileSystemClientsRequest(AbstractModel):
    """DescribeCfsFileSystemClients request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsFileSystemClientsResponse(AbstractModel):
    """DescribeCfsFileSystemClients response structure.

    """

    def __init__(self):
        r"""
        :param _ClientList: Client list
        :type ClientList: list of FileSystemClient
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClientList = None
        self._RequestId = None

    @property
    def ClientList(self):
        return self._ClientList

    @ClientList.setter
    def ClientList(self, ClientList):
        self._ClientList = ClientList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClientList") is not None:
            self._ClientList = []
            for item in params.get("ClientList"):
                obj = FileSystemClient()
                obj._deserialize(item)
                self._ClientList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsFileSystemsRequest(AbstractModel):
    """DescribeCfsFileSystems request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        """
        self._FileSystemId = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsFileSystemsResponse(AbstractModel):
    """DescribeCfsFileSystems response structure.

    """

    def __init__(self):
        r"""
        :param _FileSystems: File system information
        :type FileSystems: list of FileSystemInfo
        :param _TotalCount: Total number of file systems
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileSystems = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FileSystems(self):
        return self._FileSystems

    @FileSystems.setter
    def FileSystems(self, FileSystems):
        self._FileSystems = FileSystems

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
        if params.get("FileSystems") is not None:
            self._FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystemInfo()
                obj._deserialize(item)
                self._FileSystems.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCfsPGroupsRequest(AbstractModel):
    """DescribeCfsPGroups request structure.

    """


class DescribeCfsPGroupsResponse(AbstractModel):
    """DescribeCfsPGroups response structure.

    """

    def __init__(self):
        r"""
        :param _PGroupList: Permission group information list
        :type PGroupList: list of PGroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PGroupList = None
        self._RequestId = None

    @property
    def PGroupList(self):
        return self._PGroupList

    @PGroupList.setter
    def PGroupList(self, PGroupList):
        self._PGroupList = PGroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PGroupList") is not None:
            self._PGroupList = []
            for item in params.get("PGroupList"):
                obj = PGroupInfo()
                obj._deserialize(item)
                self._PGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsRulesRequest(AbstractModel):
    """DescribeCfsRules request structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        """
        self._PGroupId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsRulesResponse(AbstractModel):
    """DescribeCfsRules response structure.

    """

    def __init__(self):
        r"""
        :param _RuleList: List of permission group rules
        :type RuleList: list of PGroupRuleInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleList = None
        self._RequestId = None

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = PGroupRuleInfo()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsServiceStatusRequest(AbstractModel):
    """DescribeCfsServiceStatus request structure.

    """


class DescribeCfsServiceStatusResponse(AbstractModel):
    """DescribeCfsServiceStatus response structure.

    """

    def __init__(self):
        r"""
        :param _CfsServiceStatus: Current status of the CFS service for this user. Valid values: none (not activated), creating (activating), created (activated)
        :type CfsServiceStatus: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CfsServiceStatus = None
        self._RequestId = None

    @property
    def CfsServiceStatus(self):
        return self._CfsServiceStatus

    @CfsServiceStatus.setter
    def CfsServiceStatus(self, CfsServiceStatus):
        self._CfsServiceStatus = CfsServiceStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CfsServiceStatus = params.get("CfsServiceStatus")
        self._RequestId = params.get("RequestId")


class DescribeCfsSnapshotOverviewRequest(AbstractModel):
    """DescribeCfsSnapshotOverview request structure.

    """


class DescribeCfsSnapshotOverviewResponse(AbstractModel):
    """DescribeCfsSnapshotOverview response structure.

    """

    def __init__(self):
        r"""
        :param _StatisticsList: Statistics
        :type StatisticsList: list of SnapshotStatistics
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StatisticsList = None
        self._RequestId = None

    @property
    def StatisticsList(self):
        return self._StatisticsList

    @StatisticsList.setter
    def StatisticsList(self, StatisticsList):
        self._StatisticsList = StatisticsList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StatisticsList") is not None:
            self._StatisticsList = []
            for item in params.get("StatisticsList"):
                obj = SnapshotStatistics()
                obj._deserialize(item)
                self._StatisticsList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfsSnapshotsRequest(AbstractModel):
    """DescribeCfsSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _SnapshotId: Snapshot ID
        :type SnapshotId: str
        :param _Offset: The starting position of paging
        :type Offset: int
        :param _Limit: Page length
        :type Limit: int
        :param _Filters: Filters
        :type Filters: list of Filter
        :param _OrderField: Order field
        :type OrderField: str
        :param _Order: Sorting order (ascending or descending)
        :type Order: str
        """
        self._FileSystemId = None
        self._SnapshotId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._OrderField = None
        self._Order = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

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

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._SnapshotId = params.get("SnapshotId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfsSnapshotsResponse(AbstractModel):
    """DescribeCfsSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _Snapshots: Snapshot information description
        :type Snapshots: list of SnapshotInfo
        :param _TotalSize: Total size of snapshots
        :type TotalSize: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Snapshots = None
        self._TotalSize = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Snapshots(self):
        return self._Snapshots

    @Snapshots.setter
    def Snapshots(self, Snapshots):
        self._Snapshots = Snapshots

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Snapshots") is not None:
            self._Snapshots = []
            for item in params.get("Snapshots"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self._Snapshots.append(obj)
        self._TotalSize = params.get("TotalSize")
        self._RequestId = params.get("RequestId")


class DescribeMigrationTasksRequest(AbstractModel):
    """DescribeMigrationTasks request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: The pagination offset. Default value: 0.
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Filters: <br><li> taskId

Filter by **migration task ID**
Type: String

Required: No

<br><li> taskName

Fuzzy filter by **migration task name**
Type: String

Required: No

Each request can have up to 10 `Filters` and 100 `Filter.Values`.
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
        


class DescribeMigrationTasksResponse(AbstractModel):
    """DescribeMigrationTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of migration tasks
        :type TotalCount: int
        :param _MigrationTasks: Migration task details
        :type MigrationTasks: list of MigrationTaskInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._MigrationTasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MigrationTasks(self):
        return self._MigrationTasks

    @MigrationTasks.setter
    def MigrationTasks(self, MigrationTasks):
        self._MigrationTasks = MigrationTasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("MigrationTasks") is not None:
            self._MigrationTasks = []
            for item in params.get("MigrationTasks"):
                obj = MigrationTaskInfo()
                obj._deserialize(item)
                self._MigrationTasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMountTargetsRequest(AbstractModel):
    """DescribeMountTargets request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountTargetsResponse(AbstractModel):
    """DescribeMountTargets response structure.

    """

    def __init__(self):
        r"""
        :param _MountTargets: Mount target details
        :type MountTargets: list of MountInfo
        :param _NumberOfMountTargets: The number of mount targets
        :type NumberOfMountTargets: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MountTargets = None
        self._NumberOfMountTargets = None
        self._RequestId = None

    @property
    def MountTargets(self):
        return self._MountTargets

    @MountTargets.setter
    def MountTargets(self, MountTargets):
        self._MountTargets = MountTargets

    @property
    def NumberOfMountTargets(self):
        return self._NumberOfMountTargets

    @NumberOfMountTargets.setter
    def NumberOfMountTargets(self, NumberOfMountTargets):
        self._NumberOfMountTargets = NumberOfMountTargets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MountTargets") is not None:
            self._MountTargets = []
            for item in params.get("MountTargets"):
                obj = MountInfo()
                obj._deserialize(item)
                self._MountTargets.append(obj)
        self._NumberOfMountTargets = params.get("NumberOfMountTargets")
        self._RequestId = params.get("RequestId")


class DescribeSnapshotOperationLogsRequest(AbstractModel):
    """DescribeSnapshotOperationLogs request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: File system snapshot ID
        :type SnapshotId: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        """
        self._SnapshotId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

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


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotOperationLogsResponse(AbstractModel):
    """DescribeSnapshotOperationLogs response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot ID
        :type SnapshotId: str
        :param _SnapshotOperates: Operation log
        :type SnapshotOperates: list of SnapshotOperateLog
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotId = None
        self._SnapshotOperates = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotOperates(self):
        return self._SnapshotOperates

    @SnapshotOperates.setter
    def SnapshotOperates(self, SnapshotOperates):
        self._SnapshotOperates = SnapshotOperates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        if params.get("SnapshotOperates") is not None:
            self._SnapshotOperates = []
            for item in params.get("SnapshotOperates"):
                obj = SnapshotOperateLog()
                obj._deserialize(item)
                self._SnapshotOperates.append(obj)
        self._RequestId = params.get("RequestId")


class FileSystemByPolicy(AbstractModel):
    """Information of the file system bound to the snapshot policy

    """

    def __init__(self):
        r"""
        :param _CreationToken: File system name
        :type CreationToken: str
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _SizeByte: File system size
        :type SizeByte: int
        :param _StorageType: Storage class
        :type StorageType: str
        :param _TotalSnapshotSize: Total snapshot size
        :type TotalSnapshotSize: int
        :param _CreationTime: File system creation time
        :type CreationTime: str
        :param _ZoneId: Region ID of the file system
        :type ZoneId: int
        """
        self._CreationToken = None
        self._FileSystemId = None
        self._SizeByte = None
        self._StorageType = None
        self._TotalSnapshotSize = None
        self._CreationTime = None
        self._ZoneId = None

    @property
    def CreationToken(self):
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SizeByte(self):
        return self._SizeByte

    @SizeByte.setter
    def SizeByte(self, SizeByte):
        self._SizeByte = SizeByte

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def TotalSnapshotSize(self):
        return self._TotalSnapshotSize

    @TotalSnapshotSize.setter
    def TotalSnapshotSize(self, TotalSnapshotSize):
        self._TotalSnapshotSize = TotalSnapshotSize

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._CreationToken = params.get("CreationToken")
        self._FileSystemId = params.get("FileSystemId")
        self._SizeByte = params.get("SizeByte")
        self._StorageType = params.get("StorageType")
        self._TotalSnapshotSize = params.get("TotalSnapshotSize")
        self._CreationTime = params.get("CreationTime")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSystemClient(AbstractModel):
    """Information on the file system client

    """

    def __init__(self):
        r"""
        :param _CfsVip: IP address of the file system
        :type CfsVip: str
        :param _ClientIp: Client IP
        :type ClientIp: str
        :param _VpcId: File system VPCID
        :type VpcId: str
        :param _Zone: Name of the availability zone, e.g. ap-beijing-1. For more information, see regions and availability zones in the Overview document
        :type Zone: str
        :param _ZoneName: AZ name
        :type ZoneName: str
        :param _MountDirectory: Path in which the file system is mounted to the client
        :type MountDirectory: str
        """
        self._CfsVip = None
        self._ClientIp = None
        self._VpcId = None
        self._Zone = None
        self._ZoneName = None
        self._MountDirectory = None

    @property
    def CfsVip(self):
        return self._CfsVip

    @CfsVip.setter
    def CfsVip(self, CfsVip):
        self._CfsVip = CfsVip

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def MountDirectory(self):
        return self._MountDirectory

    @MountDirectory.setter
    def MountDirectory(self, MountDirectory):
        self._MountDirectory = MountDirectory


    def _deserialize(self, params):
        self._CfsVip = params.get("CfsVip")
        self._ClientIp = params.get("ClientIp")
        self._VpcId = params.get("VpcId")
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._MountDirectory = params.get("MountDirectory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSystemInfo(AbstractModel):
    """Basic information of a file system

    """

    def __init__(self):
        r"""
        :param _CreationTime: Creation time
        :type CreationTime: str
        :param _CreationToken: Custom name
        :type CreationToken: str
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _LifeCycleState: File system status. Valid values:
- creating
- mounting
- create_failed
- available
- unserviced
- upgrading
        :type LifeCycleState: str
        :param _SizeByte: Used file system capacity
        :type SizeByte: int
        :param _SizeLimit: Maximum storage limit of a file system
        :type SizeLimit: int
        :param _ZoneId: Region ID
        :type ZoneId: int
        :param _Zone: Region name
        :type Zone: str
        :param _Protocol: File system protocol type
        :type Protocol: str
        :param _StorageType: File system storage class
        :type StorageType: str
        :param _StorageResourcePkg: Prepaid storage pack bound with the file system
        :type StorageResourcePkg: str
        :param _BandwidthResourcePkg: Prepaid bandwidth pack bound to a file system (not supported currently)
        :type BandwidthResourcePkg: str
        :param _PGroup: Information of permission groups bound to a file system
        :type PGroup: :class:`tencentcloud.cfs.v20190719.models.PGroup`
        :param _FsName: Custom name
        :type FsName: str
        :param _Encrypted: Whether a file system is encrypted
        :type Encrypted: bool
        :param _KmsKeyId: Key used for encryption, which can be the key ID or ARN
        :type KmsKeyId: str
        :param _AppId: Application ID
        :type AppId: int
        :param _BandwidthLimit: The upper limit on the file system’s throughput, which is determined based on its current usage, and bound resource packs for both storage and throughput
        :type BandwidthLimit: float
        :param _Capacity: Total capacity of the file system
        :type Capacity: int
        :param _Tags: File system tag list
        :type Tags: list of TagInfo
        :param _TieringState: The lifecycle management status of a file system.
        :type TieringState: str
        :param _TieringDetail: The details about tiered storage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TieringDetail: :class:`tencentcloud.cfs.v20190719.models.TieringDetailInfo`
        """
        self._CreationTime = None
        self._CreationToken = None
        self._FileSystemId = None
        self._LifeCycleState = None
        self._SizeByte = None
        self._SizeLimit = None
        self._ZoneId = None
        self._Zone = None
        self._Protocol = None
        self._StorageType = None
        self._StorageResourcePkg = None
        self._BandwidthResourcePkg = None
        self._PGroup = None
        self._FsName = None
        self._Encrypted = None
        self._KmsKeyId = None
        self._AppId = None
        self._BandwidthLimit = None
        self._Capacity = None
        self._Tags = None
        self._TieringState = None
        self._TieringDetail = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def CreationToken(self):
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def LifeCycleState(self):
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def SizeByte(self):
        return self._SizeByte

    @SizeByte.setter
    def SizeByte(self, SizeByte):
        self._SizeByte = SizeByte

    @property
    def SizeLimit(self):
        return self._SizeLimit

    @SizeLimit.setter
    def SizeLimit(self, SizeLimit):
        self._SizeLimit = SizeLimit

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StorageResourcePkg(self):
        return self._StorageResourcePkg

    @StorageResourcePkg.setter
    def StorageResourcePkg(self, StorageResourcePkg):
        self._StorageResourcePkg = StorageResourcePkg

    @property
    def BandwidthResourcePkg(self):
        return self._BandwidthResourcePkg

    @BandwidthResourcePkg.setter
    def BandwidthResourcePkg(self, BandwidthResourcePkg):
        self._BandwidthResourcePkg = BandwidthResourcePkg

    @property
    def PGroup(self):
        return self._PGroup

    @PGroup.setter
    def PGroup(self, PGroup):
        self._PGroup = PGroup

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def Encrypted(self):
        return self._Encrypted

    @Encrypted.setter
    def Encrypted(self, Encrypted):
        self._Encrypted = Encrypted

    @property
    def KmsKeyId(self):
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def BandwidthLimit(self):
        return self._BandwidthLimit

    @BandwidthLimit.setter
    def BandwidthLimit(self, BandwidthLimit):
        self._BandwidthLimit = BandwidthLimit

    @property
    def Capacity(self):
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TieringState(self):
        return self._TieringState

    @TieringState.setter
    def TieringState(self, TieringState):
        self._TieringState = TieringState

    @property
    def TieringDetail(self):
        return self._TieringDetail

    @TieringDetail.setter
    def TieringDetail(self, TieringDetail):
        self._TieringDetail = TieringDetail


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._CreationToken = params.get("CreationToken")
        self._FileSystemId = params.get("FileSystemId")
        self._LifeCycleState = params.get("LifeCycleState")
        self._SizeByte = params.get("SizeByte")
        self._SizeLimit = params.get("SizeLimit")
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._Protocol = params.get("Protocol")
        self._StorageType = params.get("StorageType")
        self._StorageResourcePkg = params.get("StorageResourcePkg")
        self._BandwidthResourcePkg = params.get("BandwidthResourcePkg")
        if params.get("PGroup") is not None:
            self._PGroup = PGroup()
            self._PGroup._deserialize(params.get("PGroup"))
        self._FsName = params.get("FsName")
        self._Encrypted = params.get("Encrypted")
        self._KmsKeyId = params.get("KmsKeyId")
        self._AppId = params.get("AppId")
        self._BandwidthLimit = params.get("BandwidthLimit")
        self._Capacity = params.get("Capacity")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TieringState = params.get("TieringState")
        if params.get("TieringDetail") is not None:
            self._TieringDetail = TieringDetailInfo()
            self._TieringDetail._deserialize(params.get("TieringDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Conditional filter

    """

    def __init__(self):
        r"""
        :param _Values: Value
        :type Values: list of str
        :param _Name: Name
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
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
        


class MigrationTaskInfo(AbstractModel):
    """Information of a CFS data migration task

    """

    def __init__(self):
        r"""
        :param _TaskName: Migration task name
        :type TaskName: str
        :param _TaskId: Migration task ID
        :type TaskId: str
        :param _MigrationType: Migration type. Valid values: `0` (bucket) and `1` (list). Default value: `0`.
        :type MigrationType: int
        :param _MigrationMode: Migration mode. Default value: `0` (full migration).
        :type MigrationMode: int
        :param _BucketName: Data source bucket name
Note: This field may return null, indicating that no valid values can be obtained.
        :type BucketName: str
        :param _BucketRegion: Data source bucket region
Note: This field may return null, indicating that no valid values can be obtained.
        :type BucketRegion: str
        :param _BucketAddress: Data source bucket address
Note: This field may return null, indicating that no valid values can be obtained.
        :type BucketAddress: str
        :param _ListAddress: List address
Note: This field may return null, indicating that no valid values can be obtained.
        :type ListAddress: str
        :param _FsName: File system instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FsName: str
        :param _FileSystemId: File system instance ID
        :type FileSystemId: str
        :param _FsPath: File system path
        :type FsPath: str
        :param _CoverType: Overwrite policy for files with the same name. Valid values: `0` (retain the file with the latest modified time), `1` (overwrite); and `2` (not overwrite). Default value: `0`.
        :type CoverType: int
        :param _CreateTime: Creation time
        :type CreateTime: int
        :param _EndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: int
        :param _Status: Migration status. Valid values: `0` (completed), `1` (in progress), and `2` (stopped).
        :type Status: int
        :param _FileTotalCount: Number of files
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileTotalCount: int
        :param _FileMigratedCount: Number of migrated files
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileMigratedCount: int
        :param _FileFailedCount: Number of files that failed to be migrated
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileFailedCount: int
        :param _FileTotalSize: File size, in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileTotalSize: int
        :param _FileMigratedSize: Size of migrated files, in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileMigratedSize: int
        :param _FileFailedSize: Size of files that failed to be migrated, in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileFailedSize: int
        :param _FileTotalList: List of all files
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileTotalList: str
        :param _FileCompletedList: List of migrated files
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileCompletedList: str
        :param _FileFailedList: List of files that failed to be migrated
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileFailedList: str
        :param _BucketPath: Source bucket path
Note: This field may return null, indicating that no valid values can be obtained.
        :type BucketPath: str
        """
        self._TaskName = None
        self._TaskId = None
        self._MigrationType = None
        self._MigrationMode = None
        self._BucketName = None
        self._BucketRegion = None
        self._BucketAddress = None
        self._ListAddress = None
        self._FsName = None
        self._FileSystemId = None
        self._FsPath = None
        self._CoverType = None
        self._CreateTime = None
        self._EndTime = None
        self._Status = None
        self._FileTotalCount = None
        self._FileMigratedCount = None
        self._FileFailedCount = None
        self._FileTotalSize = None
        self._FileMigratedSize = None
        self._FileFailedSize = None
        self._FileTotalList = None
        self._FileCompletedList = None
        self._FileFailedList = None
        self._BucketPath = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MigrationType(self):
        return self._MigrationType

    @MigrationType.setter
    def MigrationType(self, MigrationType):
        self._MigrationType = MigrationType

    @property
    def MigrationMode(self):
        return self._MigrationMode

    @MigrationMode.setter
    def MigrationMode(self, MigrationMode):
        self._MigrationMode = MigrationMode

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketRegion(self):
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def BucketAddress(self):
        return self._BucketAddress

    @BucketAddress.setter
    def BucketAddress(self, BucketAddress):
        self._BucketAddress = BucketAddress

    @property
    def ListAddress(self):
        return self._ListAddress

    @ListAddress.setter
    def ListAddress(self, ListAddress):
        self._ListAddress = ListAddress

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsPath(self):
        return self._FsPath

    @FsPath.setter
    def FsPath(self, FsPath):
        self._FsPath = FsPath

    @property
    def CoverType(self):
        return self._CoverType

    @CoverType.setter
    def CoverType(self, CoverType):
        self._CoverType = CoverType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FileTotalCount(self):
        return self._FileTotalCount

    @FileTotalCount.setter
    def FileTotalCount(self, FileTotalCount):
        self._FileTotalCount = FileTotalCount

    @property
    def FileMigratedCount(self):
        return self._FileMigratedCount

    @FileMigratedCount.setter
    def FileMigratedCount(self, FileMigratedCount):
        self._FileMigratedCount = FileMigratedCount

    @property
    def FileFailedCount(self):
        return self._FileFailedCount

    @FileFailedCount.setter
    def FileFailedCount(self, FileFailedCount):
        self._FileFailedCount = FileFailedCount

    @property
    def FileTotalSize(self):
        return self._FileTotalSize

    @FileTotalSize.setter
    def FileTotalSize(self, FileTotalSize):
        self._FileTotalSize = FileTotalSize

    @property
    def FileMigratedSize(self):
        return self._FileMigratedSize

    @FileMigratedSize.setter
    def FileMigratedSize(self, FileMigratedSize):
        self._FileMigratedSize = FileMigratedSize

    @property
    def FileFailedSize(self):
        return self._FileFailedSize

    @FileFailedSize.setter
    def FileFailedSize(self, FileFailedSize):
        self._FileFailedSize = FileFailedSize

    @property
    def FileTotalList(self):
        return self._FileTotalList

    @FileTotalList.setter
    def FileTotalList(self, FileTotalList):
        self._FileTotalList = FileTotalList

    @property
    def FileCompletedList(self):
        return self._FileCompletedList

    @FileCompletedList.setter
    def FileCompletedList(self, FileCompletedList):
        self._FileCompletedList = FileCompletedList

    @property
    def FileFailedList(self):
        return self._FileFailedList

    @FileFailedList.setter
    def FileFailedList(self, FileFailedList):
        self._FileFailedList = FileFailedList

    @property
    def BucketPath(self):
        return self._BucketPath

    @BucketPath.setter
    def BucketPath(self, BucketPath):
        self._BucketPath = BucketPath


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskId = params.get("TaskId")
        self._MigrationType = params.get("MigrationType")
        self._MigrationMode = params.get("MigrationMode")
        self._BucketName = params.get("BucketName")
        self._BucketRegion = params.get("BucketRegion")
        self._BucketAddress = params.get("BucketAddress")
        self._ListAddress = params.get("ListAddress")
        self._FsName = params.get("FsName")
        self._FileSystemId = params.get("FileSystemId")
        self._FsPath = params.get("FsPath")
        self._CoverType = params.get("CoverType")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._FileTotalCount = params.get("FileTotalCount")
        self._FileMigratedCount = params.get("FileMigratedCount")
        self._FileFailedCount = params.get("FileFailedCount")
        self._FileTotalSize = params.get("FileTotalSize")
        self._FileMigratedSize = params.get("FileMigratedSize")
        self._FileFailedSize = params.get("FileFailedSize")
        self._FileTotalList = params.get("FileTotalList")
        self._FileCompletedList = params.get("FileCompletedList")
        self._FileFailedList = params.get("FileFailedList")
        self._BucketPath = params.get("BucketPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileSystemAutoScaleUpRuleRequest(AbstractModel):
    """ModifyFileSystemAutoScaleUpRule request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _ScaleUpThreshold: Threshold for triggering scaling. Value range: 10-90
        :type ScaleUpThreshold: int
        :param _TargetThreshold: Target threshold after scaling. Value range: 10-90. The value of this parameter must be smaller than that of `ScaleUpThreshold`.
        :type TargetThreshold: int
        :param _Status: Rule status. Valid values: `0` (disabled) and `1` (enabled).

        :type Status: int
        """
        self._FileSystemId = None
        self._ScaleUpThreshold = None
        self._TargetThreshold = None
        self._Status = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def ScaleUpThreshold(self):
        return self._ScaleUpThreshold

    @ScaleUpThreshold.setter
    def ScaleUpThreshold(self, ScaleUpThreshold):
        self._ScaleUpThreshold = ScaleUpThreshold

    @property
    def TargetThreshold(self):
        return self._TargetThreshold

    @TargetThreshold.setter
    def TargetThreshold(self, TargetThreshold):
        self._TargetThreshold = TargetThreshold

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._ScaleUpThreshold = params.get("ScaleUpThreshold")
        self._TargetThreshold = params.get("TargetThreshold")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileSystemAutoScaleUpRuleResponse(AbstractModel):
    """ModifyFileSystemAutoScaleUpRule response structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _Status: Rule status. Valid values: `0` (disabled) and `1` (enabled).
        :type Status: int
        :param _ScaleUpThreshold: Threshold for triggering scaling. Value range: 10-90
        :type ScaleUpThreshold: int
        :param _TargetThreshold: Target threshold after scaling. Value range: 10-90
        :type TargetThreshold: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileSystemId = None
        self._Status = None
        self._ScaleUpThreshold = None
        self._TargetThreshold = None
        self._RequestId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ScaleUpThreshold(self):
        return self._ScaleUpThreshold

    @ScaleUpThreshold.setter
    def ScaleUpThreshold(self, ScaleUpThreshold):
        self._ScaleUpThreshold = ScaleUpThreshold

    @property
    def TargetThreshold(self):
        return self._TargetThreshold

    @TargetThreshold.setter
    def TargetThreshold(self, TargetThreshold):
        self._TargetThreshold = TargetThreshold

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._Status = params.get("Status")
        self._ScaleUpThreshold = params.get("ScaleUpThreshold")
        self._TargetThreshold = params.get("TargetThreshold")
        self._RequestId = params.get("RequestId")


class MountInfo(AbstractModel):
    """Mount target information

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _MountTargetId: Mount target ID
        :type MountTargetId: str
        :param _IpAddress: Mount target IP
        :type IpAddress: str
        :param _FSID: Mount root-directory
        :type FSID: str
        :param _LifeCycleState: Mount target status
        :type LifeCycleState: str
        :param _NetworkInterface: Network type
        :type NetworkInterface: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _VpcName: VPC name
        :type VpcName: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _SubnetName: Subnet name
        :type SubnetName: str
        :param _CcnID: CCN instance ID used by CFS Turbo
        :type CcnID: str
        :param _CidrBlock: CCN IP range used by CFS Turbo
        :type CidrBlock: str
        """
        self._FileSystemId = None
        self._MountTargetId = None
        self._IpAddress = None
        self._FSID = None
        self._LifeCycleState = None
        self._NetworkInterface = None
        self._VpcId = None
        self._VpcName = None
        self._SubnetId = None
        self._SubnetName = None
        self._CcnID = None
        self._CidrBlock = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def MountTargetId(self):
        return self._MountTargetId

    @MountTargetId.setter
    def MountTargetId(self, MountTargetId):
        self._MountTargetId = MountTargetId

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def FSID(self):
        return self._FSID

    @FSID.setter
    def FSID(self, FSID):
        self._FSID = FSID

    @property
    def LifeCycleState(self):
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def NetworkInterface(self):
        return self._NetworkInterface

    @NetworkInterface.setter
    def NetworkInterface(self, NetworkInterface):
        self._NetworkInterface = NetworkInterface

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CcnID(self):
        return self._CcnID

    @CcnID.setter
    def CcnID(self, CcnID):
        self._CcnID = CcnID

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._MountTargetId = params.get("MountTargetId")
        self._IpAddress = params.get("IpAddress")
        self._FSID = params.get("FSID")
        self._LifeCycleState = params.get("LifeCycleState")
        self._NetworkInterface = params.get("NetworkInterface")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._CcnID = params.get("CcnID")
        self._CidrBlock = params.get("CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroup(AbstractModel):
    """Information of permission groups bound to a file system

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _Name: Permission group name
        :type Name: str
        """
        self._PGroupId = None
        self._Name = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroupInfo(AbstractModel):
    """Array of permission groups

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _Name: Permission group name
        :type Name: str
        :param _DescInfo: Description
        :type DescInfo: str
        :param _CDate: Creation time
        :type CDate: str
        :param _BindCfsNum: The number of bound file system
        :type BindCfsNum: int
        """
        self._PGroupId = None
        self._Name = None
        self._DescInfo = None
        self._CDate = None
        self._BindCfsNum = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo

    @property
    def CDate(self):
        return self._CDate

    @CDate.setter
    def CDate(self, CDate):
        self._CDate = CDate

    @property
    def BindCfsNum(self):
        return self._BindCfsNum

    @BindCfsNum.setter
    def BindCfsNum(self, BindCfsNum):
        self._BindCfsNum = BindCfsNum


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        self._CDate = params.get("CDate")
        self._BindCfsNum = params.get("BindCfsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PGroupRuleInfo(AbstractModel):
    """List of permission group rules

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _AuthClientIp: Client IP allowed for access
        :type AuthClientIp: str
        :param _RWPermission: Read/write permission. ro: read-only; rw: read & write
        :type RWPermission: str
        :param _UserPermission: User permission. all_squash: any visiting user will be mapped to an anonymous user or user group; no_all_squash: a visiting user will be first matched with a local user, and if the match fails, it will be mapped to an anonymous user or user group; root_squash: a visiting root user will be mapped to an anonymous user or user group; no_root_squash: a visiting root user will be allowed to maintain root account permissions.
        :type UserPermission: str
        :param _Priority: Rule priority. Value range: 1-100. 1 represents the highest priority, while 100 the lowest
        :type Priority: int
        """
        self._RuleId = None
        self._AuthClientIp = None
        self._RWPermission = None
        self._UserPermission = None
        self._Priority = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AuthClientIp(self):
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpFileSystemRequest(AbstractModel):
    """ScaleUpFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _TargetCapacity: Target capacity after scaling
        :type TargetCapacity: int
        """
        self._FileSystemId = None
        self._TargetCapacity = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def TargetCapacity(self):
        return self._TargetCapacity

    @TargetCapacity.setter
    def TargetCapacity(self, TargetCapacity):
        self._TargetCapacity = TargetCapacity


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._TargetCapacity = params.get("TargetCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpFileSystemResponse(AbstractModel):
    """ScaleUpFileSystem response structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _TargetCapacity: Target capacity after scaling
        :type TargetCapacity: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileSystemId = None
        self._TargetCapacity = None
        self._RequestId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def TargetCapacity(self):
        return self._TargetCapacity

    @TargetCapacity.setter
    def TargetCapacity(self, TargetCapacity):
        self._TargetCapacity = TargetCapacity

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._TargetCapacity = params.get("TargetCapacity")
        self._RequestId = params.get("RequestId")


class SignUpCfsServiceRequest(AbstractModel):
    """SignUpCfsService request structure.

    """


class SignUpCfsServiceResponse(AbstractModel):
    """SignUpCfsService response structure.

    """

    def __init__(self):
        r"""
        :param _CfsServiceStatus: Current status of the CFS service for this user. Valid values: `creating` (activating); `created` (activated)
        :type CfsServiceStatus: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CfsServiceStatus = None
        self._RequestId = None

    @property
    def CfsServiceStatus(self):
        return self._CfsServiceStatus

    @CfsServiceStatus.setter
    def CfsServiceStatus(self, CfsServiceStatus):
        self._CfsServiceStatus = CfsServiceStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CfsServiceStatus = params.get("CfsServiceStatus")
        self._RequestId = params.get("RequestId")


class SnapshotInfo(AbstractModel):
    """Snapshot information

    """

    def __init__(self):
        r"""
        :param _CreationTime: Snapshot creation time
        :type CreationTime: str
        :param _SnapshotName: Snapshot name
        :type SnapshotName: str
        :param _SnapshotId: Snapshot ID
        :type SnapshotId: str
        :param _Status: Snapshot status
        :type Status: str
        :param _RegionName: Region name
        :type RegionName: str
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _Size: Snapshot size
        :type Size: int
        :param _AliveDay: Retention period in days
        :type AliveDay: int
        :param _Percent: Snapshot progress
        :type Percent: int
        :param _AppId: Account ID
        :type AppId: int
        :param _DeleteTime: Snapshot deletion time
        :type DeleteTime: str
        :param _FsName: File system name
        :type FsName: str
        :param _Tags: Snapshot tag
        :type Tags: list of TagInfo
        :param _SnapshotType: Snapshot type
Note: This field may return null, indicating that no valid values can be obtained.
        :type SnapshotType: str
        """
        self._CreationTime = None
        self._SnapshotName = None
        self._SnapshotId = None
        self._Status = None
        self._RegionName = None
        self._FileSystemId = None
        self._Size = None
        self._AliveDay = None
        self._Percent = None
        self._AppId = None
        self._DeleteTime = None
        self._FsName = None
        self._Tags = None
        self._SnapshotType = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def AliveDay(self):
        return self._AliveDay

    @AliveDay.setter
    def AliveDay(self, AliveDay):
        self._AliveDay = AliveDay

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def DeleteTime(self):
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SnapshotType(self):
        return self._SnapshotType

    @SnapshotType.setter
    def SnapshotType(self, SnapshotType):
        self._SnapshotType = SnapshotType


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._SnapshotName = params.get("SnapshotName")
        self._SnapshotId = params.get("SnapshotId")
        self._Status = params.get("Status")
        self._RegionName = params.get("RegionName")
        self._FileSystemId = params.get("FileSystemId")
        self._Size = params.get("Size")
        self._AliveDay = params.get("AliveDay")
        self._Percent = params.get("Percent")
        self._AppId = params.get("AppId")
        self._DeleteTime = params.get("DeleteTime")
        self._FsName = params.get("FsName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SnapshotType = params.get("SnapshotType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotOperateLog(AbstractModel):
    """Snapshot operation log

    """

    def __init__(self):
        r"""
        :param _Action: Operation type
        :type Action: str
        :param _ActionTime: Operation time
        :type ActionTime: str
        :param _ActionName: Operation name
        :type ActionName: str
        :param _Operator: Operator
        :type Operator: str
        :param _Result: Result
        :type Result: int
        """
        self._Action = None
        self._ActionTime = None
        self._ActionName = None
        self._Operator = None
        self._Result = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionTime(self):
        return self._ActionTime

    @ActionTime.setter
    def ActionTime(self, ActionTime):
        self._ActionTime = ActionTime

    @property
    def ActionName(self):
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._ActionTime = params.get("ActionTime")
        self._ActionName = params.get("ActionName")
        self._Operator = params.get("Operator")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotStatistics(AbstractModel):
    """File system snapshot statistics

    """

    def __init__(self):
        r"""
        :param _Region: Region
        :type Region: str
        :param _SnapshotNumber: Total number of snapshots
        :type SnapshotNumber: int
        :param _SnapshotSize: Total snapshot size
        :type SnapshotSize: int
        """
        self._Region = None
        self._SnapshotNumber = None
        self._SnapshotSize = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SnapshotNumber(self):
        return self._SnapshotNumber

    @SnapshotNumber.setter
    def SnapshotNumber(self, SnapshotNumber):
        self._SnapshotNumber = SnapshotNumber

    @property
    def SnapshotSize(self):
        return self._SnapshotSize

    @SnapshotSize.setter
    def SnapshotSize(self, SnapshotSize):
        self._SnapshotSize = SnapshotSize


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._SnapshotNumber = params.get("SnapshotNumber")
        self._SnapshotSize = params.get("SnapshotSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrationTaskRequest(AbstractModel):
    """StopMigrationTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Migration task name
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        


class StopMigrationTaskResponse(AbstractModel):
    """StopMigrationTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Migration task ID
        :type TaskId: str
        :param _Status: Migration status. Valid values: `0` (completed), `1` (in progress), and `2` (stopped).
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """Tag information unit

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
        


class TieringDetailInfo(AbstractModel):
    """The details about tiered storage.

    """

    def __init__(self):
        r"""
        :param _TieringSizeInBytes: STANDARD_IA storage usage
Note: This field may return null, indicating that no valid values can be obtained.
        :type TieringSizeInBytes: int
        """
        self._TieringSizeInBytes = None

    @property
    def TieringSizeInBytes(self):
        return self._TieringSizeInBytes

    @TieringSizeInBytes.setter
    def TieringSizeInBytes(self, TieringSizeInBytes):
        self._TieringSizeInBytes = TieringSizeInBytes


    def _deserialize(self, params):
        self._TieringSizeInBytes = params.get("TieringSizeInBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoSnapshotPolicyRequest(AbstractModel):
    """UnbindAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemIds: List of IDs of the file systems to be unbound, separated by comma
        :type FileSystemIds: str
        :param _AutoSnapshotPolicyId: ID of the snapshot to be unbound
        :type AutoSnapshotPolicyId: str
        """
        self._FileSystemIds = None
        self._AutoSnapshotPolicyId = None

    @property
    def FileSystemIds(self):
        return self._FileSystemIds

    @FileSystemIds.setter
    def FileSystemIds(self, FileSystemIds):
        self._FileSystemIds = FileSystemIds

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId


    def _deserialize(self, params):
        self._FileSystemIds = params.get("FileSystemIds")
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoSnapshotPolicyResponse(AbstractModel):
    """UnbindAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Snapshot policy ID
        :type AutoSnapshotPolicyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class UpdateAutoSnapshotPolicyRequest(AbstractModel):
    """UpdateAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Snapshot policy ID
        :type AutoSnapshotPolicyId: str
        :param _PolicyName: Snapshot policy name
        :type PolicyName: str
        :param _DayOfWeek: The day of the week on which to regularly back up the snapshot
        :type DayOfWeek: str
        :param _Hour: The hour of a day at which to regularly back up the snapshot
        :type Hour: str
        :param _AliveDays: Snapshot retention period
        :type AliveDays: int
        :param _IsActivated: Whether to activate the scheduled snapshot feature
        :type IsActivated: int
        :param _DayOfMonth: The specific day of the month on which to create a snapshot. This parameter is mutually exclusive with `DayOfWeek`.
        :type DayOfMonth: str
        :param _IntervalDays: The snapshot interval. This parameter is mutually exclusive with `DayOfWeek` and `DayOfMonth`.
        :type IntervalDays: int
        """
        self._AutoSnapshotPolicyId = None
        self._PolicyName = None
        self._DayOfWeek = None
        self._Hour = None
        self._AliveDays = None
        self._IsActivated = None
        self._DayOfMonth = None
        self._IntervalDays = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def DayOfWeek(self):
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def AliveDays(self):
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def DayOfMonth(self):
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        return self._IntervalDays

    @IntervalDays.setter
    def IntervalDays(self, IntervalDays):
        self._IntervalDays = IntervalDays


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._PolicyName = params.get("PolicyName")
        self._DayOfWeek = params.get("DayOfWeek")
        self._Hour = params.get("Hour")
        self._AliveDays = params.get("AliveDays")
        self._IsActivated = params.get("IsActivated")
        self._DayOfMonth = params.get("DayOfMonth")
        self._IntervalDays = params.get("IntervalDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAutoSnapshotPolicyResponse(AbstractModel):
    """UpdateAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Snapshot policy ID
        :type AutoSnapshotPolicyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._RequestId = params.get("RequestId")


class UpdateCfsFileSystemNameRequest(AbstractModel):
    """UpdateCfsFileSystemName request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _FsName: Custom file system name
        :type FsName: str
        """
        self._FileSystemId = None
        self._FsName = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._FsName = params.get("FsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemNameResponse(AbstractModel):
    """UpdateCfsFileSystemName response structure.

    """

    def __init__(self):
        r"""
        :param _CreationToken: Custom file system name
        :type CreationToken: str
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _FsName: Custom file system name
        :type FsName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CreationToken = None
        self._FileSystemId = None
        self._FsName = None
        self._RequestId = None

    @property
    def CreationToken(self):
        return self._CreationToken

    @CreationToken.setter
    def CreationToken(self, CreationToken):
        self._CreationToken = CreationToken

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsName(self):
        return self._FsName

    @FsName.setter
    def FsName(self, FsName):
        self._FsName = FsName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CreationToken = params.get("CreationToken")
        self._FileSystemId = params.get("FileSystemId")
        self._FsName = params.get("FsName")
        self._RequestId = params.get("RequestId")


class UpdateCfsFileSystemPGroupRequest(AbstractModel):
    """UpdateCfsFileSystemPGroup request structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        """
        self._PGroupId = None
        self._FileSystemId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemPGroupResponse(AbstractModel):
    """UpdateCfsFileSystemPGroup response structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PGroupId = None
        self._FileSystemId = None
        self._RequestId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._FileSystemId = params.get("FileSystemId")
        self._RequestId = params.get("RequestId")


class UpdateCfsFileSystemSizeLimitRequest(AbstractModel):
    """UpdateCfsFileSystemSizeLimit request structure.

    """

    def __init__(self):
        r"""
        :param _FsLimit: File system capacity limit in GB. Value range: 0-1,073,741,824. If 0 is entered, no limit will be imposed on the file system capacity.
        :type FsLimit: int
        :param _FileSystemId: File system ID. Currently, only Standard file systems are supported.
        :type FileSystemId: str
        """
        self._FsLimit = None
        self._FileSystemId = None

    @property
    def FsLimit(self):
        return self._FsLimit

    @FsLimit.setter
    def FsLimit(self, FsLimit):
        self._FsLimit = FsLimit

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FsLimit = params.get("FsLimit")
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsFileSystemSizeLimitResponse(AbstractModel):
    """UpdateCfsFileSystemSizeLimit response structure.

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


class UpdateCfsPGroupRequest(AbstractModel):
    """UpdateCfsPGroup request structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _Name: Permission group name, which can contain 1-64 Chinese characters, letters, numbers, underscores, or dashes
        :type Name: str
        :param _DescInfo: Permission group description, which can contain 1-255 characters
        :type DescInfo: str
        """
        self._PGroupId = None
        self._Name = None
        self._DescInfo = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsPGroupResponse(AbstractModel):
    """UpdateCfsPGroup response structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _Name: Permission group name
        :type Name: str
        :param _DescInfo: Description
        :type DescInfo: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PGroupId = None
        self._Name = None
        self._DescInfo = None
        self._RequestId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescInfo(self):
        return self._DescInfo

    @DescInfo.setter
    def DescInfo(self, DescInfo):
        self._DescInfo = DescInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._Name = params.get("Name")
        self._DescInfo = params.get("DescInfo")
        self._RequestId = params.get("RequestId")


class UpdateCfsRuleRequest(AbstractModel):
    """UpdateCfsRule request structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _AuthClientIp: You can enter a single IP or IP range, such as 10.1.10.11 or 10.10.1.0/24. The default visiting address is `*`, indicating that all IPs are allowed. Please note that you need to enter the CVM instance's private IP here.
        :type AuthClientIp: str
        :param _RWPermission: Read/write permission. Valid values: RO (read-only), RW (read & write). Default value: RO
        :type RWPermission: str
        :param _UserPermission: User permission. Valid values: all_squash, no_all_squash, root_squash, no_root_squash. Specifically, all_squash: any visiting user will be mapped to an anonymous user or user group; no_all_squash: a visiting user will be first matched with a local user, and if the match fails, it will be mapped to an anonymous user or user group; root_squash: a visiting root user will be mapped to an anonymous user or user group; no_root_squash: a visiting root user will be allowed to maintain root account permissions. Default value: root_squash.
        :type UserPermission: str
        :param _Priority: Rule priority. Value range: 1-100. 1 represents the highest priority, while 100 the lowest
        :type Priority: int
        """
        self._PGroupId = None
        self._RuleId = None
        self._AuthClientIp = None
        self._RWPermission = None
        self._UserPermission = None
        self._Priority = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AuthClientIp(self):
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._RuleId = params.get("RuleId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsRuleResponse(AbstractModel):
    """UpdateCfsRule response structure.

    """

    def __init__(self):
        r"""
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _AuthClientIp: Client IP or IP range allowed for access
        :type AuthClientIp: str
        :param _RWPermission: Read & write permission
        :type RWPermission: str
        :param _UserPermission: User permission
        :type UserPermission: str
        :param _Priority: Priority
        :type Priority: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PGroupId = None
        self._RuleId = None
        self._AuthClientIp = None
        self._RWPermission = None
        self._UserPermission = None
        self._Priority = None
        self._RequestId = None

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AuthClientIp(self):
        return self._AuthClientIp

    @AuthClientIp.setter
    def AuthClientIp(self, AuthClientIp):
        self._AuthClientIp = AuthClientIp

    @property
    def RWPermission(self):
        return self._RWPermission

    @RWPermission.setter
    def RWPermission(self, RWPermission):
        self._RWPermission = RWPermission

    @property
    def UserPermission(self):
        return self._UserPermission

    @UserPermission.setter
    def UserPermission(self, UserPermission):
        self._UserPermission = UserPermission

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PGroupId = params.get("PGroupId")
        self._RuleId = params.get("RuleId")
        self._AuthClientIp = params.get("AuthClientIp")
        self._RWPermission = params.get("RWPermission")
        self._UserPermission = params.get("UserPermission")
        self._Priority = params.get("Priority")
        self._RequestId = params.get("RequestId")


class UpdateCfsSnapshotAttributeRequest(AbstractModel):
    """UpdateCfsSnapshotAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: File system snapshot ID
        :type SnapshotId: str
        :param _SnapshotName: File system snapshot name
        :type SnapshotName: str
        :param _AliveDays: File system snapshot retention period in days
        :type AliveDays: int
        """
        self._SnapshotId = None
        self._SnapshotName = None
        self._AliveDays = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def AliveDays(self):
        return self._AliveDays

    @AliveDays.setter
    def AliveDays(self, AliveDays):
        self._AliveDays = AliveDays


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._SnapshotName = params.get("SnapshotName")
        self._AliveDays = params.get("AliveDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCfsSnapshotAttributeResponse(AbstractModel):
    """UpdateCfsSnapshotAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: File system snapshot ID
        :type SnapshotId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotId = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")