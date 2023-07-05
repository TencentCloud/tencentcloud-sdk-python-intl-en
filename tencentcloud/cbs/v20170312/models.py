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


class AdvancedRetentionPolicy(AbstractModel):
    """Retention policy for scheduled snapshots. All four parameters are required.

    """

    def __init__(self):
        r"""
        :param _Days: Retains one latest snapshot each day within `Days` days. Value range: [0, 100].
Note: This field may return null, indicating that no valid values can be obtained.
        :type Days: int
        :param _Weeks: Retains one latest snapshot each week within `Weeks` weeks. Value range: [0, 100].
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weeks: int
        :param _Months: Retains one latest snapshot each month within `Months` months. Value range: [0, 100].
Note: This field may return null, indicating that no valid values can be obtained.
        :type Months: int
        :param _Years: Retains one latest snapshot each year within `Years` years. Value range: [0, 100].
Note: This field may return null, indicating that no valid values can be obtained.
        :type Years: int
        """
        self._Days = None
        self._Weeks = None
        self._Months = None
        self._Years = None

    @property
    def Days(self):
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Weeks(self):
        return self._Weeks

    @Weeks.setter
    def Weeks(self, Weeks):
        self._Weeks = Weeks

    @property
    def Months(self):
        return self._Months

    @Months.setter
    def Months(self, Months):
        self._Months = Months

    @property
    def Years(self):
        return self._Years

    @Years.setter
    def Years(self, Years):
        self._Years = Years


    def _deserialize(self, params):
        self._Days = params.get("Days")
        self._Weeks = params.get("Weeks")
        self._Months = params.get("Months")
        self._Years = params.get("Years")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyDiskBackupRequest(AbstractModel):
    """ApplyDiskBackup request structure.

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: ID of the cloud disk backup point, which can be queried through the `DescribeDiskBackups` API.
        :type DiskBackupId: str
        :param _DiskId: ID of the original cloud disk of the backup point, which can be queried through the `DescribeDisks` API.
        :type DiskId: str
        """
        self._DiskBackupId = None
        self._DiskId = None

    @property
    def DiskBackupId(self):
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyDiskBackupResponse(AbstractModel):
    """ApplyDiskBackup response structure.

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


class ApplySnapshotRequest(AbstractModel):
    """ApplySnapshot request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot ID, which can be queried via [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :type SnapshotId: str
        :param _DiskId: ID of the original cloud disk corresponding to the snapshot, which can be queried via the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1).
        :type DiskId: str
        :param _AutoStopInstance: Specifies whether to shut down a CVM automatically before a rollback
        :type AutoStopInstance: bool
        :param _AutoStartInstance: Specifies whether to start up a CVM automatically after a rollback
        :type AutoStartInstance: bool
        """
        self._SnapshotId = None
        self._DiskId = None
        self._AutoStopInstance = None
        self._AutoStartInstance = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def AutoStopInstance(self):
        return self._AutoStopInstance

    @AutoStopInstance.setter
    def AutoStopInstance(self, AutoStopInstance):
        self._AutoStopInstance = AutoStopInstance

    @property
    def AutoStartInstance(self):
        return self._AutoStartInstance

    @AutoStartInstance.setter
    def AutoStartInstance(self, AutoStartInstance):
        self._AutoStartInstance = AutoStartInstance


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._DiskId = params.get("DiskId")
        self._AutoStopInstance = params.get("AutoStopInstance")
        self._AutoStartInstance = params.get("AutoStartInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplySnapshotResponse(AbstractModel):
    """ApplySnapshot response structure.

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


class AttachDetail(AbstractModel):
    """This describes the number of mounted and mountable data disks of an instance.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AttachedDiskCount: The number of instances mounted to data disk.
        :type AttachedDiskCount: int
        :param _MaxAttachCount: The maximum number of instances that can be mounted to data disk.
        :type MaxAttachCount: int
        """
        self._InstanceId = None
        self._AttachedDiskCount = None
        self._MaxAttachCount = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AttachedDiskCount(self):
        return self._AttachedDiskCount

    @AttachedDiskCount.setter
    def AttachedDiskCount(self, AttachedDiskCount):
        self._AttachedDiskCount = AttachedDiskCount

    @property
    def MaxAttachCount(self):
        return self._MaxAttachCount

    @MaxAttachCount.setter
    def MaxAttachCount(self, MaxAttachCount):
        self._MaxAttachCount = MaxAttachCount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AttachedDiskCount = params.get("AttachedDiskCount")
        self._MaxAttachCount = params.get("MaxAttachCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksRequest(AbstractModel):
    """AttachDisks request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the CVM instance on which the cloud disk will be mounted. It can be queried via the API [DescribeInstances](https://intl.cloud.tencent.com/document/product/213/15728?from_cn_redirect=1).
        :type InstanceId: str
        :param _DiskIds: ID of the elastic cloud disk to be mounted, which can be queried through the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1). A maximum of 10 elastic cloud disks can be mounted in a single request.
        :type DiskIds: list of str
        :param _DeleteWithInstance: Optional parameter. If this is not passed only the mount operation is executed. If `True` is passed, the cloud disk will be configured to be terminated when the server it is mounted to is terminated. This is only valid for pay-as-you-go cloud disks.
        :type DeleteWithInstance: bool
        :param _AttachMode: (Optional) Specifies the cloud disk mounting method. It’s only valid for BM models. Valid values: <br><li>PF<br><li>VF
        :type AttachMode: str
        """
        self._InstanceId = None
        self._DiskIds = None
        self._DeleteWithInstance = None
        self._AttachMode = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def AttachMode(self):
        return self._AttachMode

    @AttachMode.setter
    def AttachMode(self, AttachMode):
        self._AttachMode = AttachMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DiskIds = params.get("DiskIds")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._AttachMode = params.get("AttachMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksResponse(AbstractModel):
    """AttachDisks response structure.

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


class AutoMountConfiguration(AbstractModel):
    """Describes how a newly purchased cloud disk is initialized and attached to a CVM instance.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance to which the cloud disk is attached.
        :type InstanceId: list of str
        :param _MountPoint: Mount point in the instance.
        :type MountPoint: list of str
        :param _FileSystemType: File system type. Valid values: `ext4`, `xfs`.
        :type FileSystemType: str
        """
        self._InstanceId = None
        self._MountPoint = None
        self._FileSystemType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MountPoint(self):
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def FileSystemType(self):
        return self._FileSystemType

    @FileSystemType.setter
    def FileSystemType(self, FileSystemType):
        self._FileSystemType = FileSystemType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MountPoint = params.get("MountPoint")
        self._FileSystemType = params.get("FileSystemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoSnapshotPolicy(AbstractModel):
    """This describes the detailed information of the scheduled snapshot policy.

    """

    def __init__(self):
        r"""
        :param _DiskIdSet: The list of cloud disk IDs that the current scheduled snapshot policy is bound to.
        :type DiskIdSet: list of str
        :param _IsActivated: Whether scheduled snapshot policy is activated.
        :type IsActivated: bool
        :param _AutoSnapshotPolicyState: Scheduled snapshot policy state. Value range:<br><li>NORMAL: Normal<br><li>ISOLATED: Isolated.
        :type AutoSnapshotPolicyState: str
        :param _IsCopyToRemote: Whether it is to replicate a snapshot across accounts. `1`: yes, `0`: no.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsCopyToRemote: int
        :param _IsPermanent: Whether the snapshot created by this scheduled snapshot policy is retained permanently.
        :type IsPermanent: bool
        :param _NextTriggerTime: The time the scheduled snapshot will be triggered again.
        :type NextTriggerTime: str
        :param _AutoSnapshotPolicyName: Scheduled snapshot policy name.
        :type AutoSnapshotPolicyName: str
        :param _AutoSnapshotPolicyId: Scheduled snapshot policy ID.
        :type AutoSnapshotPolicyId: str
        :param _Policy: The policy for executing the scheduled snapshot.
        :type Policy: list of Policy
        :param _CreateTime: The time the scheduled snapshot policy was created.
        :type CreateTime: str
        :param _RetentionDays: Number of days the snapshot created by this scheduled snapshot policy is retained.
        :type RetentionDays: int
        :param _CopyToAccountUin: ID of the replication target account
Note: This field may return null, indicating that no valid values can be obtained.
        :type CopyToAccountUin: str
        :param _InstanceIdSet: List of IDs of the instances associated with the scheduled snapshot policy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceIdSet: list of str
        :param _RetentionMonths: The number of months for which the snapshots created by this scheduled snapshot policy can be retained.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RetentionMonths: int
        :param _RetentionAmount: The maximum number of snapshots created by this scheduled snapshot policy that can be retained.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RetentionAmount: int
        :param _AdvancedRetentionPolicy: Retention policy for scheduled snapshots.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AdvancedRetentionPolicy: :class:`tencentcloud.cbs.v20170312.models.AdvancedRetentionPolicy`
        :param _CopyFromAccountUin: Source account ID of the copied snapshot policy
Note: This field may return null, indicating that no valid values can be obtained.
        :type CopyFromAccountUin: str
        :param _Tags: Tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
        self._DiskIdSet = None
        self._IsActivated = None
        self._AutoSnapshotPolicyState = None
        self._IsCopyToRemote = None
        self._IsPermanent = None
        self._NextTriggerTime = None
        self._AutoSnapshotPolicyName = None
        self._AutoSnapshotPolicyId = None
        self._Policy = None
        self._CreateTime = None
        self._RetentionDays = None
        self._CopyToAccountUin = None
        self._InstanceIdSet = None
        self._RetentionMonths = None
        self._RetentionAmount = None
        self._AdvancedRetentionPolicy = None
        self._CopyFromAccountUin = None
        self._Tags = None

    @property
    def DiskIdSet(self):
        return self._DiskIdSet

    @DiskIdSet.setter
    def DiskIdSet(self, DiskIdSet):
        self._DiskIdSet = DiskIdSet

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def AutoSnapshotPolicyState(self):
        return self._AutoSnapshotPolicyState

    @AutoSnapshotPolicyState.setter
    def AutoSnapshotPolicyState(self, AutoSnapshotPolicyState):
        self._AutoSnapshotPolicyState = AutoSnapshotPolicyState

    @property
    def IsCopyToRemote(self):
        return self._IsCopyToRemote

    @IsCopyToRemote.setter
    def IsCopyToRemote(self, IsCopyToRemote):
        self._IsCopyToRemote = IsCopyToRemote

    @property
    def IsPermanent(self):
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def NextTriggerTime(self):
        return self._NextTriggerTime

    @NextTriggerTime.setter
    def NextTriggerTime(self, NextTriggerTime):
        self._NextTriggerTime = NextTriggerTime

    @property
    def AutoSnapshotPolicyName(self):
        return self._AutoSnapshotPolicyName

    @AutoSnapshotPolicyName.setter
    def AutoSnapshotPolicyName(self, AutoSnapshotPolicyName):
        self._AutoSnapshotPolicyName = AutoSnapshotPolicyName

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RetentionDays(self):
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays

    @property
    def CopyToAccountUin(self):
        return self._CopyToAccountUin

    @CopyToAccountUin.setter
    def CopyToAccountUin(self, CopyToAccountUin):
        self._CopyToAccountUin = CopyToAccountUin

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RetentionMonths(self):
        return self._RetentionMonths

    @RetentionMonths.setter
    def RetentionMonths(self, RetentionMonths):
        self._RetentionMonths = RetentionMonths

    @property
    def RetentionAmount(self):
        return self._RetentionAmount

    @RetentionAmount.setter
    def RetentionAmount(self, RetentionAmount):
        self._RetentionAmount = RetentionAmount

    @property
    def AdvancedRetentionPolicy(self):
        return self._AdvancedRetentionPolicy

    @AdvancedRetentionPolicy.setter
    def AdvancedRetentionPolicy(self, AdvancedRetentionPolicy):
        self._AdvancedRetentionPolicy = AdvancedRetentionPolicy

    @property
    def CopyFromAccountUin(self):
        return self._CopyFromAccountUin

    @CopyFromAccountUin.setter
    def CopyFromAccountUin(self, CopyFromAccountUin):
        self._CopyFromAccountUin = CopyFromAccountUin

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DiskIdSet = params.get("DiskIdSet")
        self._IsActivated = params.get("IsActivated")
        self._AutoSnapshotPolicyState = params.get("AutoSnapshotPolicyState")
        self._IsCopyToRemote = params.get("IsCopyToRemote")
        self._IsPermanent = params.get("IsPermanent")
        self._NextTriggerTime = params.get("NextTriggerTime")
        self._AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self._Policy.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._RetentionDays = params.get("RetentionDays")
        self._CopyToAccountUin = params.get("CopyToAccountUin")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RetentionMonths = params.get("RetentionMonths")
        self._RetentionAmount = params.get("RetentionAmount")
        if params.get("AdvancedRetentionPolicy") is not None:
            self._AdvancedRetentionPolicy = AdvancedRetentionPolicy()
            self._AdvancedRetentionPolicy._deserialize(params.get("AdvancedRetentionPolicy"))
        self._CopyFromAccountUin = params.get("CopyFromAccountUin")
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
        


class BindAutoSnapshotPolicyRequest(AbstractModel):
    """BindAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: ID of scheduled snapshot policy to be bound.
        :type AutoSnapshotPolicyId: str
        :param _DiskIds: List of cloud disk IDs to be bound. Maximum of 80 cloud disks can be bound per request.
        :type DiskIds: list of str
        """
        self._AutoSnapshotPolicyId = None
        self._DiskIds = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._DiskIds = params.get("DiskIds")
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


class CopySnapshotCrossRegionsRequest(AbstractModel):
    """CopySnapshotCrossRegions request structure.

    """

    def __init__(self):
        r"""
        :param _DestinationRegions: Destination regions of the replication task. You can query the value of regions by calling [DescribeRegions](https://intl.cloud.tencent.com/document/product/213/9456?from_cn_redirect=1) API. Note that you can only specify regions that support snapshots.
        :type DestinationRegions: list of str
        :param _SnapshotId: Snapshot ID, which can be queried via the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API.
        :type SnapshotId: str
        :param _SnapshotName: Name of the snapshot replica. If it’s not specified, it defaults to “Copied [source snapshot ID from [region name]”
        :type SnapshotName: str
        """
        self._DestinationRegions = None
        self._SnapshotId = None
        self._SnapshotName = None

    @property
    def DestinationRegions(self):
        return self._DestinationRegions

    @DestinationRegions.setter
    def DestinationRegions(self, DestinationRegions):
        self._DestinationRegions = DestinationRegions

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


    def _deserialize(self, params):
        self._DestinationRegions = params.get("DestinationRegions")
        self._SnapshotId = params.get("SnapshotId")
        self._SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopySnapshotCrossRegionsResponse(AbstractModel):
    """CopySnapshotCrossRegions response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotCopyResultSet: Result of the cross-region replication task. The ID of the new snapshot replica is returned if the request succeeds. Otherwise `Error` is returned.
        :type SnapshotCopyResultSet: list of SnapshotCopyResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotCopyResultSet = None
        self._RequestId = None

    @property
    def SnapshotCopyResultSet(self):
        return self._SnapshotCopyResultSet

    @SnapshotCopyResultSet.setter
    def SnapshotCopyResultSet(self, SnapshotCopyResultSet):
        self._SnapshotCopyResultSet = SnapshotCopyResultSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SnapshotCopyResultSet") is not None:
            self._SnapshotCopyResultSet = []
            for item in params.get("SnapshotCopyResultSet"):
                obj = SnapshotCopyResult()
                obj._deserialize(item)
                self._SnapshotCopyResultSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateAutoSnapshotPolicyRequest(AbstractModel):
    """CreateAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Policy: The policy for executing the scheduled snapshot.
        :type Policy: list of Policy
        :param _AutoSnapshotPolicyName: The name of the scheduled snapshot policy to be created. If it is left empty, the default is 'Not named'. The maximum length cannot exceed 60 bytes.
        :type AutoSnapshotPolicyName: str
        :param _IsActivated: Whether or not the scheduled snapshot policy is activated. FALSE: Not activated. TRUE: Activated. The default value is TRUE.
        :type IsActivated: bool
        :param _IsPermanent: Whether the snapshot created by this scheduled snapshot policy is retained permanently. FALSE: Not retained permanently. TRUE: Retained permanently. The default value is FALSE.
        :type IsPermanent: bool
        :param _RetentionDays: The number of days that a snapshot created by this scheduled snapshot policy is retained. The default value is 7. If this parameter is specified, the IsPermanent input parameter can not be TRUE, otherwise a conflict will occur.
        :type RetentionDays: int
        :param _DryRun: Whether to create an execution policy for the scheduled snapshot. TRUE: Only the time of the initial backup needs to be obtained, and no scheduled snapshot policy is actually created. FALSE: Create. The default value is FALSE.
        :type DryRun: bool
        """
        self._Policy = None
        self._AutoSnapshotPolicyName = None
        self._IsActivated = None
        self._IsPermanent = None
        self._RetentionDays = None
        self._DryRun = None

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def AutoSnapshotPolicyName(self):
        return self._AutoSnapshotPolicyName

    @AutoSnapshotPolicyName.setter
    def AutoSnapshotPolicyName(self, AutoSnapshotPolicyName):
        self._AutoSnapshotPolicyName = AutoSnapshotPolicyName

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def IsPermanent(self):
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def RetentionDays(self):
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self._Policy.append(obj)
        self._AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self._IsActivated = params.get("IsActivated")
        self._IsPermanent = params.get("IsPermanent")
        self._RetentionDays = params.get("RetentionDays")
        self._DryRun = params.get("DryRun")
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
        :param _AutoSnapshotPolicyId: The ID of the newly created scheduled snapshot policy.
        :type AutoSnapshotPolicyId: str
        :param _NextTriggerTime: The time that initial backup will start.
        :type NextTriggerTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._NextTriggerTime = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def NextTriggerTime(self):
        return self._NextTriggerTime

    @NextTriggerTime.setter
    def NextTriggerTime(self, NextTriggerTime):
        self._NextTriggerTime = NextTriggerTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._NextTriggerTime = params.get("NextTriggerTime")
        self._RequestId = params.get("RequestId")


class CreateDiskBackupRequest(AbstractModel):
    """CreateDiskBackup request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: Name of the cloud disk for which to create a backup point.
        :type DiskId: str
        :param _DiskBackupName: Name of the cloud disk backup point, which can contain up to 100 characters.
        :type DiskBackupName: str
        """
        self._DiskId = None
        self._DiskBackupName = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupName(self):
        return self._DiskBackupName

    @DiskBackupName.setter
    def DiskBackupName(self, DiskBackupName):
        self._DiskBackupName = DiskBackupName


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._DiskBackupName = params.get("DiskBackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDiskBackupResponse(AbstractModel):
    """CreateDiskBackup response structure.

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: ID of the cloud disk backup point.
        :type DiskBackupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskBackupId = None
        self._RequestId = None

    @property
    def DiskBackupId(self):
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
        self._RequestId = params.get("RequestId")


class CreateDisksRequest(AbstractModel):
    """CreateDisks request structure.

    """

    def __init__(self):
        r"""
        :param _Placement: Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone and project. If no project is specified, the default project will be used.
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param _DiskChargeType: Cloud disk billing mode. POSTPAID_BY_HOUR: Pay-as-you-go by hour<br><li>CDCPAID: Billed together with the bound dedicated cluster<br>For more information on the pricing in each mode, see [Pricing Overview](https://intl.cloud.tencent.com/document/product/362/2413?from_cn_redirect=1).
        :type DiskChargeType: str
        :param _DiskType: Cloud disk media type. Valid values: <br><li>CLOUD_BASIC: HDD Cloud Storage<br><li>CLOUD_PREMIUM: Premium Cloud Disk<br><li>CLOUD_BSSD: Balanced SSD<br><li>CLOUD_SSD: SSD<br><li>CLOUD_HSSD: Enhanced SSD<br><li>CLOUD_TSSD: ulTra SSD.
        :type DiskType: str
        :param _DiskName: Cloud disk name. If it is not specified, "Unnamed" will be used by default. The maximum length is 60 bytes.
        :type DiskName: str
        :param _Tags: Tags bound to the cloud disk.
        :type Tags: list of Tag
        :param _SnapshotId: Snapshot ID. If this parameter is specified, the cloud disk will be created based on the snapshot. The snapshot must be a data disk snapshot. To query the type of a snapshot, call the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API and see the `DiskUsage` field in the response.
        :type SnapshotId: str
        :param _DiskCount: Number of cloud disks to be created. If it is not specified, `1` will be used by default. There is an upper limit on the maximum number of cloud disks that can be created in a single request. For more information, see [Use Limits](https://intl.cloud.tencent.com/doc/product/362/5145?from_cn_redirect=1).
        :type DiskCount: int
        :param _ThroughputPerformance: Extra performance purchased for a cloud disk.<br>This optional parameter is only valid for ulTra SSD (CLOUD_TSSD) and Enhanced SSD (CLOUD_HSSD).
        :type ThroughputPerformance: int
        :param _DiskSize: Cloud disk size in GB. <br><li>`DiskSize` is not required if `SnapshotId` is specified. In this case, the size of the cloud disk will be equal to that of the snapshot. <br><li>If you specify both `SnapshotId` and `DiskSize`, the specified disk size cannot be smaller than the snapshot size. <br><li>For the value range of cloud disk size, see [Cloud Disk Types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        :param _Shareable: Optional parameter. Default value: `False`. If `True` is specified, the new cloud disk will be shared.
        :type Shareable: bool
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        :param _Encrypt: This parameter is used to create encrypted cloud disks. It is fixed at `ENCRYPT`.
        :type Encrypt: str
        :param _DiskChargePrepaid: Relevant parameter settings for the prepaid mode (i.e., monthly subscription). The monthly subscription cloud disk purchase attributes such as usage period and whether or not auto-renewal is set up can be specified using this parameter. <br>This parameter is required when creating a prepaid cloud disk. This parameter is not required when creating an hourly postpaid cloud disk. 
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param _DeleteSnapshot: Whether to delete the associated non-permanently reserved snapshots upon deletion of the source cloud disk. `0`: No (default value). `1`: Yes. To check whether a snapshot is permanently reserved, see the `IsPermanent` field returned by the `DescribeSnapshots` API.
        :type DeleteSnapshot: int
        :param _AutoMountConfiguration: Specifies whether to automatically attach and initialize the newly created data disk.
        :type AutoMountConfiguration: :class:`tencentcloud.cbs.v20170312.models.AutoMountConfiguration`
        :param _DiskBackupQuota: Specifies the cloud disk backup point quota.
        :type DiskBackupQuota: int
        :param _BurstPerformance: Specifies whether to enable disk bursting.
        :type BurstPerformance: bool
        """
        self._Placement = None
        self._DiskChargeType = None
        self._DiskType = None
        self._DiskName = None
        self._Tags = None
        self._SnapshotId = None
        self._DiskCount = None
        self._ThroughputPerformance = None
        self._DiskSize = None
        self._Shareable = None
        self._ClientToken = None
        self._Encrypt = None
        self._DiskChargePrepaid = None
        self._DeleteSnapshot = None
        self._AutoMountConfiguration = None
        self._DiskBackupQuota = None
        self._BurstPerformance = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskName(self):
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskCount(self):
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Shareable(self):
        return self._Shareable

    @Shareable.setter
    def Shareable(self, Shareable):
        self._Shareable = Shareable

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def DiskChargePrepaid(self):
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DeleteSnapshot(self):
        return self._DeleteSnapshot

    @DeleteSnapshot.setter
    def DeleteSnapshot(self, DeleteSnapshot):
        self._DeleteSnapshot = DeleteSnapshot

    @property
    def AutoMountConfiguration(self):
        return self._AutoMountConfiguration

    @AutoMountConfiguration.setter
    def AutoMountConfiguration(self, AutoMountConfiguration):
        self._AutoMountConfiguration = AutoMountConfiguration

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota

    @property
    def BurstPerformance(self):
        return self._BurstPerformance

    @BurstPerformance.setter
    def BurstPerformance(self, BurstPerformance):
        self._BurstPerformance = BurstPerformance


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._DiskChargeType = params.get("DiskChargeType")
        self._DiskType = params.get("DiskType")
        self._DiskName = params.get("DiskName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SnapshotId = params.get("SnapshotId")
        self._DiskCount = params.get("DiskCount")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._DiskSize = params.get("DiskSize")
        self._Shareable = params.get("Shareable")
        self._ClientToken = params.get("ClientToken")
        self._Encrypt = params.get("Encrypt")
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DeleteSnapshot = params.get("DeleteSnapshot")
        if params.get("AutoMountConfiguration") is not None:
            self._AutoMountConfiguration = AutoMountConfiguration()
            self._AutoMountConfiguration._deserialize(params.get("AutoMountConfiguration"))
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        self._BurstPerformance = params.get("BurstPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisksResponse(AbstractModel):
    """CreateDisks response structure.

    """

    def __init__(self):
        r"""
        :param _DiskIdSet: ID list of the created cloud disks. Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskIdSet = None
        self._RequestId = None

    @property
    def DiskIdSet(self):
        return self._DiskIdSet

    @DiskIdSet.setter
    def DiskIdSet(self, DiskIdSet):
        self._DiskIdSet = DiskIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiskIdSet = params.get("DiskIdSet")
        self._RequestId = params.get("RequestId")


class CreateSnapshotRequest(AbstractModel):
    """CreateSnapshot request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: ID of the cloud disk for which to create a snapshot, which can be queried through the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskId: str
        :param _SnapshotName: Snapshot name. If it is not specified, "Unnamed" will be used by default.
        :type SnapshotName: str
        :param _Deadline: Expiration time of the snapshot. It must be in UTC ISO-8601 format, eg. 2022-01-08T09:47:55+00:00. The snapshot will be automatically deleted when it expires.
        :type Deadline: str
        :param _DiskBackupId: ID of the cloud disk backup point. When this parameter is specified, the snapshot will be created from the backup point.
        :type DiskBackupId: str
        :param _Tags: Tags bound to the snapshot.
        :type Tags: list of Tag
        """
        self._DiskId = None
        self._SnapshotName = None
        self._Deadline = None
        self._DiskBackupId = None
        self._Tags = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def DiskBackupId(self):
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._SnapshotName = params.get("SnapshotName")
        self._Deadline = params.get("Deadline")
        self._DiskBackupId = params.get("DiskBackupId")
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
        


class CreateSnapshotResponse(AbstractModel):
    """CreateSnapshot response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: ID of the created snapshot <br/>Note: This field may return null, indicating that no valid values can be obtained.
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


class DeleteAutoSnapshotPoliciesRequest(AbstractModel):
    """DeleteAutoSnapshotPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyIds: List of scheduled snapshot policy IDs to be deleted.
        :type AutoSnapshotPolicyIds: list of str
        """
        self._AutoSnapshotPolicyIds = None

    @property
    def AutoSnapshotPolicyIds(self):
        return self._AutoSnapshotPolicyIds

    @AutoSnapshotPolicyIds.setter
    def AutoSnapshotPolicyIds(self, AutoSnapshotPolicyIds):
        self._AutoSnapshotPolicyIds = AutoSnapshotPolicyIds


    def _deserialize(self, params):
        self._AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoSnapshotPoliciesResponse(AbstractModel):
    """DeleteAutoSnapshotPolicies response structure.

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


class DeleteDiskBackupsRequest(AbstractModel):
    """DeleteDiskBackups request structure.

    """

    def __init__(self):
        r"""
        :param _DiskBackupIds: ID of the cloud disk backup point to be deleted.
        :type DiskBackupIds: list of str
        """
        self._DiskBackupIds = None

    @property
    def DiskBackupIds(self):
        return self._DiskBackupIds

    @DiskBackupIds.setter
    def DiskBackupIds(self, DiskBackupIds):
        self._DiskBackupIds = DiskBackupIds


    def _deserialize(self, params):
        self._DiskBackupIds = params.get("DiskBackupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDiskBackupsResponse(AbstractModel):
    """DeleteDiskBackups response structure.

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


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: List of IDs of snapshots to be deleted, which can be queried via [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :type SnapshotIds: list of str
        :param _DeleteBindImages: Whether to forcibly delete the image associated with the snapshot
        :type DeleteBindImages: bool
        """
        self._SnapshotIds = None
        self._DeleteBindImages = None

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def DeleteBindImages(self):
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
        :param _AutoSnapshotPolicyIds: List of scheduled snapshot policy IDs to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`.
        :type AutoSnapshotPolicyIds: list of str
        :param _Filters: Filter conditions. Specification of both the `AutoSnapshotPolicyIds` and `Filters` parameters is not supported.<br><li>auto-snapshot-policy-id - Array of String - Required or not: No - (Filter condition) Filters according to the scheduled snapshot policy ID. The format of the scheduled snapshot policy ID is as follows: `asp-11112222`. <br><li>auto-snapshot-policy-state - Array of String - Required or not: No - (Filter condition) Filters according to the status of the scheduled snapshot policy. The format of the scheduled snapshot policy ID is as follows: `asp-11112222`. (NORMAL: normal | ISOLATED: isolated)<br><li>auto-snapshot-policy-name - Array of String - Required or not: No - (Filter condition) Filters according to the name of the scheduled snapshot policy.
        :type Filters: list of Filter
        :param _Limit: Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param _Order: Outputs the ordering of the scheduled snapshot lists. Value range: <br><li>ASC: Ascending order <br><li>DESC: Descending order.
        :type Order: str
        :param _OrderField: The sorting filter applied to the scheduled snapshot list. Value range: <Sort by creation time of scheduled snapshot. By default, this is sorted by creation time.
        :type OrderField: str
        """
        self._AutoSnapshotPolicyIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._OrderField = None

    @property
    def AutoSnapshotPolicyIds(self):
        return self._AutoSnapshotPolicyIds

    @AutoSnapshotPolicyIds.setter
    def AutoSnapshotPolicyIds(self, AutoSnapshotPolicyIds):
        self._AutoSnapshotPolicyIds = AutoSnapshotPolicyIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

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
        self._AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        :param _TotalCount: The quantity of valid scheduled snapshot policies.
        :type TotalCount: int
        :param _AutoSnapshotPolicySet: List of scheduled snapshot policies.
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoSnapshotPolicySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoSnapshotPolicySet(self):
        return self._AutoSnapshotPolicySet

    @AutoSnapshotPolicySet.setter
    def AutoSnapshotPolicySet(self, AutoSnapshotPolicySet):
        self._AutoSnapshotPolicySet = AutoSnapshotPolicySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicySet") is not None:
            self._AutoSnapshotPolicySet = []
            for item in params.get("AutoSnapshotPolicySet"):
                obj = AutoSnapshotPolicy()
                obj._deserialize(item)
                self._AutoSnapshotPolicySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskAssociatedAutoSnapshotPolicyRequest(AbstractModel):
    """DescribeDiskAssociatedAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: The ID of the queried cloud disk.
        :type DiskId: str
        """
        self._DiskId = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskAssociatedAutoSnapshotPolicyResponse(AbstractModel):
    """DescribeDiskAssociatedAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The quantity of scheduled snapshots binded to cloud disk.
        :type TotalCount: int
        :param _AutoSnapshotPolicySet: List of scheduled snapshots bound to cloud disk.
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoSnapshotPolicySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoSnapshotPolicySet(self):
        return self._AutoSnapshotPolicySet

    @AutoSnapshotPolicySet.setter
    def AutoSnapshotPolicySet(self, AutoSnapshotPolicySet):
        self._AutoSnapshotPolicySet = AutoSnapshotPolicySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicySet") is not None:
            self._AutoSnapshotPolicySet = []
            for item in params.get("AutoSnapshotPolicySet"):
                obj = AutoSnapshotPolicy()
                obj._deserialize(item)
                self._AutoSnapshotPolicySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskBackupsRequest(AbstractModel):
    """DescribeDiskBackups request structure.

    """

    def __init__(self):
        r"""
        :param _DiskBackupIds: List of IDs of the backup points to be queried. `DiskBackupIds` and `Filters` cannot be specified at the same time.
        :type DiskBackupIds: list of str
        :param _Filters: Filter. `DiskBackupIds` and `Filters` cannot be specified at the same time. Valid values: <br><li>disk-backup-id - Array of String - Required: No - (Filter) Filter by backup point ID in the format of `dbp-11112222`.
<br><li>disk-id - Array of String - Required: No - (Filter) Filter by ID of the cloud disk for which backup points are created.
<br><li>disk-usage - Array of String - Required: No - (Filter) Filter by type of the cloud disk for which backup points are created. (SYSTEM_DISK: System disk | DATA_DISK: Data disk)
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param _Order: Sorting order of cloud disk backup points. Valid values:<br><li>ASC: Ascending<br><li>DESC: Descending
        :type Order: str
        :param _OrderField: The field by which cloud disk backup points are sorted. Valid values:<br><li>CREATE_TIME: Sort by creation time<br>Backup points are sorted by creation time by default.
        :type OrderField: str
        """
        self._DiskBackupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def DiskBackupIds(self):
        return self._DiskBackupIds

    @DiskBackupIds.setter
    def DiskBackupIds(self, DiskBackupIds):
        self._DiskBackupIds = DiskBackupIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._DiskBackupIds = params.get("DiskBackupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskBackupsResponse(AbstractModel):
    """DescribeDiskBackups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible cloud disk backup points.
        :type TotalCount: int
        :param _DiskBackupSet: List of details of cloud disk backup points.
        :type DiskBackupSet: list of DiskBackup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DiskBackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DiskBackupSet(self):
        return self._DiskBackupSet

    @DiskBackupSet.setter
    def DiskBackupSet(self, DiskBackupSet):
        self._DiskBackupSet = DiskBackupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DiskBackupSet") is not None:
            self._DiskBackupSet = []
            for item in params.get("DiskBackupSet"):
                obj = DiskBackup()
                obj._deserialize(item)
                self._DiskBackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskConfigQuotaRequest(AbstractModel):
    """DescribeDiskConfigQuota request structure.

    """

    def __init__(self):
        r"""
        :param _InquiryType: Inquiry type. Value range: INQUIRY_CBS_CONFIG: query the configuration list of cloud disks <br><li>INQUIRY_CVM_CONFIG: query the configuration list of cloud disks and instances.
        :type InquiryType: str
        :param _Zones: Query configuration under one or more [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo).
        :type Zones: list of str
        :param _DiskChargeType: Billing mode. Value range: <br><li>POSTPAID_BY_HOUR: postpaid.
        :type DiskChargeType: str
        :param _DiskTypes: Cloud disk media type. Valid values: <br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium Cloud Storage<br><li>CLOUD_SSD: SSD<br><li>CLOUD_HSSD: Enhanced SSD
        :type DiskTypes: list of str
        :param _DiskUsage: The system disk or data disk. Value range: <br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk.
        :type DiskUsage: str
        :param _InstanceFamilies: Filter by the instance model series, such as S1, I1 and M1. For more information, please see [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1)
        :type InstanceFamilies: list of str
        :param _CPU: Instance CPU cores.
        :type CPU: int
        :param _Memory: Instance memory size.
        :type Memory: int
        """
        self._InquiryType = None
        self._Zones = None
        self._DiskChargeType = None
        self._DiskTypes = None
        self._DiskUsage = None
        self._InstanceFamilies = None
        self._CPU = None
        self._Memory = None

    @property
    def InquiryType(self):
        return self._InquiryType

    @InquiryType.setter
    def InquiryType(self, InquiryType):
        self._InquiryType = InquiryType

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def DiskTypes(self):
        return self._DiskTypes

    @DiskTypes.setter
    def DiskTypes(self, DiskTypes):
        self._DiskTypes = DiskTypes

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def InstanceFamilies(self):
        return self._InstanceFamilies

    @InstanceFamilies.setter
    def InstanceFamilies(self, InstanceFamilies):
        self._InstanceFamilies = InstanceFamilies

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory


    def _deserialize(self, params):
        self._InquiryType = params.get("InquiryType")
        self._Zones = params.get("Zones")
        self._DiskChargeType = params.get("DiskChargeType")
        self._DiskTypes = params.get("DiskTypes")
        self._DiskUsage = params.get("DiskUsage")
        self._InstanceFamilies = params.get("InstanceFamilies")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskConfigQuotaResponse(AbstractModel):
    """DescribeDiskConfigQuota response structure.

    """

    def __init__(self):
        r"""
        :param _DiskConfigSet: List of cloud disk configurations.
        :type DiskConfigSet: list of DiskConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskConfigSet = None
        self._RequestId = None

    @property
    def DiskConfigSet(self):
        return self._DiskConfigSet

    @DiskConfigSet.setter
    def DiskConfigSet(self, DiskConfigSet):
        self._DiskConfigSet = DiskConfigSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskConfigSet") is not None:
            self._DiskConfigSet = []
            for item in params.get("DiskConfigSet"):
                obj = DiskConfig()
                obj._deserialize(item)
                self._DiskConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiskOperationLogsRequest(AbstractModel):
    """DescribeDiskOperationLogs request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter conditions. The following conditions are supported:
<li>disk-id - Array of String - Required or not: Yes - Filter by cloud disk ID, with maximum of 10 cloud disk IDs able to be specified per request.
        :type Filters: list of Filter
        :param _BeginTime: The start time of the operation logs to be queried, for example: '2019-11-22 00:00:00"
        :type BeginTime: str
        :param _EndTime: The end time of the operation logs to be queried, for example: '2019-11-22 23:59:59"
        :type EndTime: str
        """
        self._Filters = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskOperationLogsResponse(AbstractModel):
    """DescribeDiskOperationLogs response structure.

    """

    def __init__(self):
        r"""
        :param _DiskOperationLogSet: List of cloud disk operation logs.
        :type DiskOperationLogSet: list of DiskOperationLog
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskOperationLogSet = None
        self._RequestId = None

    @property
    def DiskOperationLogSet(self):
        return self._DiskOperationLogSet

    @DiskOperationLogSet.setter
    def DiskOperationLogSet(self, DiskOperationLogSet):
        self._DiskOperationLogSet = DiskOperationLogSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskOperationLogSet") is not None:
            self._DiskOperationLogSet = []
            for item in params.get("DiskOperationLogSet"):
                obj = DiskOperationLog()
                obj._deserialize(item)
                self._DiskOperationLogSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    """DescribeDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: Query by one or more cloud disk IDs, such as `disk-11112222`. For the format of this parameter, please see the ids.N section of the API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1). This parameter does not support specifying both `DiskIds` and `Filters`.
        :type DiskIds: list of str
        :param _Filters: Filters. You cannot specify `DiskIds` and `Filters` at the same time. <br><li>disk-usage - Array of String - Optional - Filters by cloud disk type. (SYSTEM_DISK: system disk | DATA_DISK: data disk) <br><li>disk-charge-type - Array of String - Optional - Filters by cloud disk billing method. (POSTPAID_BY_HOUR: pay-as-you-go) <br><li>portable - Array of String- Optional - Filters by whether the cloud disk is elastic or not. (TRUE: elastic | FALSE: non-elastic) <br><li>project-id - Array of Integer - Optional - Filters by the ID of the project to which a cloud disk belongs. <br><li>disk-id - Array of String - Optional - Filters by cloud disk ID, such as `disk-11112222`. <br><li>disk-name - Array of String - Optional - Filters by cloud disk name. <br><li>disk-type - Array of String - Optional - Filters by cloud disk media type (CLOUD_BASIC: HDD cloud disk | CLOUD_PREMIUM: Premium Cloud Storage | CLOUD_SSD: SSD cloud disk.) <br><li>disk-state - Array of String - Optional - Filters by cloud disk state. (UNATTACHED: not mounted | ATTACHING: being mounted | ATTACHED: mounted | DETACHING: being unmounted | EXPANDING: being expanded | ROLLBACKING: being rolled back | TORECYCLE: to be repossessed.) <br><li>instance-id - Array of String - Optional - Filters by the ID of the CVM instance on which a cloud disk is mounted. You can use this parameter to query the cloud disks mounted on specific CVMs. <br><li>zone - Array of String - Optional - Filters by [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) <br><li>instance-ip-address - Array of String - Optional - Filters by the private or public IP of the CVM on which a cloud disk is mounted. <br><li>instance-name - Array of String - Optional - Filters by the name of the instance on which a cloud disk is mounted. <br><li>tag-key - Array of String - Optional - Filters by tag key. <br><li>tag-value - Array of String - Optional - Filters by tag value. <br><li>tag:tag-key - Array of String - Optional - Filters by tag key-value pair. Please replace `tag-key` with a specific tag key.
        :type Filters: list of Filter
        :param _Offset: Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param _Order: Outputs the ordering of the cloud disk list. Value range: <br><li>ASC: Ascending order <br><li>DESC: Descending order.
        :type Order: str
        :param _OrderField: The field by which the cloud disk list is sorted. Value range: <br><li>CREATE_TIME: sorted by the creation time of cloud disks <br><li>DEADLINE: sorted by the expiration time of cloud disks<br>By default, the cloud disk list is sorted by the creation time of cloud disks.
        :type OrderField: str
        :param _ReturnBindAutoSnapshotPolicy: Whether the ID of the periodic snapshot policy bound to the cloud disk needs to be returned in the cloud disk details. TRUE: return; FALSE: do not return.
        :type ReturnBindAutoSnapshotPolicy: bool
        """
        self._DiskIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None
        self._ReturnBindAutoSnapshotPolicy = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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

    @property
    def ReturnBindAutoSnapshotPolicy(self):
        return self._ReturnBindAutoSnapshotPolicy

    @ReturnBindAutoSnapshotPolicy.setter
    def ReturnBindAutoSnapshotPolicy(self, ReturnBindAutoSnapshotPolicy):
        self._ReturnBindAutoSnapshotPolicy = ReturnBindAutoSnapshotPolicy


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        self._ReturnBindAutoSnapshotPolicy = params.get("ReturnBindAutoSnapshotPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksResponse(AbstractModel):
    """DescribeDisks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The quantity of cloud disks meeting the conditions.
        :type TotalCount: int
        :param _DiskSet: List of cloud disk details.
        :type DiskSet: list of Disk
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DiskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DiskSet(self):
        return self._DiskSet

    @DiskSet.setter
    def DiskSet(self, DiskSet):
        self._DiskSet = DiskSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DiskSet") is not None:
            self._DiskSet = []
            for item in params.get("DiskSet"):
                obj = Disk()
                obj._deserialize(item)
                self._DiskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesDiskNumRequest(AbstractModel):
    """DescribeInstancesDiskNum request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: ID of the CVM instance can be queried via the API [DescribeInstances](https://intl.cloud.tencent.com/document/product/213/15728?from_cn_redirect=1).
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDiskNumResponse(AbstractModel):
    """DescribeInstancesDiskNum response structure.

    """

    def __init__(self):
        r"""
        :param _AttachDetail: The quantity of mounted and mountable elastic cloud disks for each cloud virtual machine
        :type AttachDetail: list of AttachDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AttachDetail = None
        self._RequestId = None

    @property
    def AttachDetail(self):
        return self._AttachDetail

    @AttachDetail.setter
    def AttachDetail(self, AttachDetail):
        self._AttachDetail = AttachDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AttachDetail") is not None:
            self._AttachDetail = []
            for item in params.get("AttachDetail"):
                obj = AttachDetail()
                obj._deserialize(item)
                self._AttachDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotOperationLogsRequest(AbstractModel):
    """DescribeSnapshotOperationLogs request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter conditions. The following conditions are supported:
<li>snapshot-id - Array of String - Required or not: Yes - Filter by snapshot ID, with maximum of 10 snapshot IDs able to be specified per request.
        :type Filters: list of Filter
        :param _BeginTime: The start time of the operation logs to be queried, for example: '2019-11-22 00:00:00"
        :type BeginTime: str
        :param _EndTime: The end time of the operation logs to be queried, for example: '2019-11-22 23:59:59"
        :type EndTime: str
        """
        self._Filters = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._BeginTime = params.get("BeginTime")
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
        :param _SnapshotOperationLogSet: List of snapshot operation logs.
        :type SnapshotOperationLogSet: list of SnapshotOperationLog
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotOperationLogSet = None
        self._RequestId = None

    @property
    def SnapshotOperationLogSet(self):
        return self._SnapshotOperationLogSet

    @SnapshotOperationLogSet.setter
    def SnapshotOperationLogSet(self, SnapshotOperationLogSet):
        self._SnapshotOperationLogSet = SnapshotOperationLogSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SnapshotOperationLogSet") is not None:
            self._SnapshotOperationLogSet = []
            for item in params.get("SnapshotOperationLogSet"):
                obj = SnapshotOperationLog()
                obj._deserialize(item)
                self._SnapshotOperationLogSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotSharePermissionRequest(AbstractModel):
    """DescribeSnapshotSharePermission request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: The ID of the snapshot to be queried. You can obtain this by using [DescribeSnapshots](https://intl.cloud.tencent.com/document/api/362/15647?from_cn_redirect=1).
        :type SnapshotId: str
        """
        self._SnapshotId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotSharePermissionResponse(AbstractModel):
    """DescribeSnapshotSharePermission response structure.

    """

    def __init__(self):
        r"""
        :param _SharePermissionSet: The set of snapshot sharing information
        :type SharePermissionSet: list of SharePermission
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SharePermissionSet = None
        self._RequestId = None

    @property
    def SharePermissionSet(self):
        return self._SharePermissionSet

    @SharePermissionSet.setter
    def SharePermissionSet(self, SharePermissionSet):
        self._SharePermissionSet = SharePermissionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SharePermissionSet") is not None:
            self._SharePermissionSet = []
            for item in params.get("SharePermissionSet"):
                obj = SharePermission()
                obj._deserialize(item)
                self._SharePermissionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: List of snapshot IDs to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`.
        :type SnapshotIds: list of str
        :param _Filters: Filters. It cannot be specified together with `SnapshotIds`.<br><li>snapshot-id - Array of String - Optional - Filters by snapshot ID, such as `snap-11112222`.<br><li>snapshot-name - Array of String - Optional - Filters by snapshot name. <br><li>snapshot-state - Array of String - Optional - Filters by snapshot state (NORMAL: normal | CREATING: creating | ROLLBACKING: rolling back). <br><li>disk-usage - Array of String - Optional - Filters by the type of the cloud disk from which a snapshot is created (SYSTEM_DISK: system disk | DATA_DISK: data disk).<br><li>project-id - Array of String - Optional - Filters by the ID of the project to which a cloud disk belongs. <br><li>disk-id - Array of String - Optional - Filters by the ID of the cloud disk from which a snapshot is created.<br><li>zone - Array of String - Optional - Filters by [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo).<br><li>encrypt - Array of String - Optional - Filters by whether a snapshot is created from an encrypted cloud disk. (TRUE: a snapshot of an encrypted cloud disk | FALSE: not a snapshot of an encrypted cloud disk.)
<li>snapshot-type- Array of String - Optional - Filters by the snapshot type specified in `snapshot-type`.
(SHARED_SNAPSHOT: a shared snapshot | PRIVATE_SNAPSHOT: a private snapshot.)
        :type Filters: list of Filter
        :param _Offset: Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param _Order: Outputs the ordering of the cloud disk list. Value range: <br><li>ASC: Ascending order <br><li>DESC: Descending order.
        :type Order: str
        :param _OrderField: The field by which the snapshot list is sorted. Value range: <br><li>CREATE_TIME: sorted by the creation time of the snapshots <br>By default, the snapshot list is sorted by the creation time of snapshots.
        :type OrderField: str
        """
        self._SnapshotIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._SnapshotIds = params.get("SnapshotIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
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
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SnapshotSet(self):
        return self._SnapshotSet

    @SnapshotSet.setter
    def SnapshotSet(self, SnapshotSet):
        self._SnapshotSet = SnapshotSet

    @property
    def RequestId(self):
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


class DetachDisksRequest(AbstractModel):
    """DetachDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: IDs of the cloud disks to be unmounted, which can be queried via the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API. Up to 10 elastic cloud disks can be unmounted in a single request.
        :type DiskIds: list of str
        :param _InstanceId: Indicates the CVM from which you want to unmount the disks. This parameter is only available for shared cloud disks.
        :type InstanceId: str
        """
        self._DiskIds = None
        self._InstanceId = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachDisksResponse(AbstractModel):
    """DetachDisks response structure.

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


class DetailPrice(AbstractModel):
    """Pricing details for the cloud disk.

    """

    def __init__(self):
        r"""
        :param _PriceTitle: Name of the billable item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PriceTitle: str
        :param _PriceName: Name of the billable item displayed in the console.
        :type PriceName: str
        :param _OriginalPrice: Original price of a monthly subscribed cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalPrice: float
        :param _DiscountPrice: Discounted price of a monthly subscribed cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiscountPrice: float
        :param _UnitPrice: Original unit price of a pay-as-you-go cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param _UnitPriceDiscount: Discount unit price of a pay-as-you-go cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: float
        :param _ChargeUnit: Billing unit for pay-as-you-go cloud disks. Valid value: `HOUR` (billed hourly).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeUnit: str
        :param _OriginalPriceHigh: Original highly-precise price of a monthly subscribed cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalPriceHigh: str
        :param _DiscountPriceHigh: Discounted highly-precise price of a monthly subscribed cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiscountPriceHigh: str
        :param _UnitPriceHigh: Original highly-precise unit price of a pay-as-you-go cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPriceHigh: str
        :param _UnitPriceDiscountHigh: Discounted highly-precise unit price of a pay-as-you-go cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnitPriceDiscountHigh: str
        """
        self._PriceTitle = None
        self._PriceName = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._UnitPrice = None
        self._UnitPriceDiscount = None
        self._ChargeUnit = None
        self._OriginalPriceHigh = None
        self._DiscountPriceHigh = None
        self._UnitPriceHigh = None
        self._UnitPriceDiscountHigh = None

    @property
    def PriceTitle(self):
        return self._PriceTitle

    @PriceTitle.setter
    def PriceTitle(self, PriceTitle):
        self._PriceTitle = PriceTitle

    @property
    def PriceName(self):
        return self._PriceName

    @PriceName.setter
    def PriceName(self, PriceName):
        self._PriceName = PriceName

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def OriginalPriceHigh(self):
        return self._OriginalPriceHigh

    @OriginalPriceHigh.setter
    def OriginalPriceHigh(self, OriginalPriceHigh):
        self._OriginalPriceHigh = OriginalPriceHigh

    @property
    def DiscountPriceHigh(self):
        return self._DiscountPriceHigh

    @DiscountPriceHigh.setter
    def DiscountPriceHigh(self, DiscountPriceHigh):
        self._DiscountPriceHigh = DiscountPriceHigh

    @property
    def UnitPriceHigh(self):
        return self._UnitPriceHigh

    @UnitPriceHigh.setter
    def UnitPriceHigh(self, UnitPriceHigh):
        self._UnitPriceHigh = UnitPriceHigh

    @property
    def UnitPriceDiscountHigh(self):
        return self._UnitPriceDiscountHigh

    @UnitPriceDiscountHigh.setter
    def UnitPriceDiscountHigh(self, UnitPriceDiscountHigh):
        self._UnitPriceDiscountHigh = UnitPriceDiscountHigh


    def _deserialize(self, params):
        self._PriceTitle = params.get("PriceTitle")
        self._PriceName = params.get("PriceName")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._ChargeUnit = params.get("ChargeUnit")
        self._OriginalPriceHigh = params.get("OriginalPriceHigh")
        self._DiscountPriceHigh = params.get("DiscountPriceHigh")
        self._UnitPriceHigh = params.get("UnitPriceHigh")
        self._UnitPriceDiscountHigh = params.get("UnitPriceDiscountHigh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Disk(AbstractModel):
    """The details of a cloud disk

    """

    def __init__(self):
        r"""
        :param _DeleteWithInstance: Whether the cloud disk terminates along with the instance mounted to it. <br><li>true: Cloud disk will also be terminated when instance terminates, so only hourly postpaid cloud disk are supported.<br><li>false: Cloud disk does not terminate when instance terminates.
Note: This field may return null, indicating that no valid value was found.
        :type DeleteWithInstance: bool
        :param _RenewFlag: Auto renewal flag. Supported values:<br><li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically<br><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically.
Note: This field may return null, indicating that no valid value was found.
        :type RenewFlag: str
        :param _DiskType: Cloud disk types. Valid values: <br><li>CLOUD_BASIC: HDD cloud disk <br><li>CLOUD_PREMIUM: Premium Cloud Disk <br><li>CLOUD_BSSD: General Purpose SSD <br><li>CLOUD_SSD: SSD <br><li>CLOUD_HSSD: Enhanced SSD <br><li>CLOUD_TSSD: Tremendous SSD
        :type DiskType: str
        :param _DiskState: The state of the cloud disk. Value range: <br><li>UNATTACHED: Not mounted <br><li>ATTACHING: Mounting <br><li>ATTACHED: Mounted <br><li>DETACHING: Un-mounting <br><li>EXPANDING: Expanding <br><li>ROLLBACKING: Rolling back <br><li>TORECYCE: Pending recycling. <br><li>DUMPING: Copying the hard drive.
        :type DiskState: str
        :param _SnapshotCount: The total number of snapshots of the cloud disk.
        :type SnapshotCount: int
        :param _AutoRenewFlagError: Cloud disk already mounted to CVM, and both CVM and cloud disk use monthly subscription.<br><li>true: CVM has auto-renewal flag set up, but cloud disk does not.<br><li>false: Cloud disk auto-renewal flag set up normally.
Note: This field may return null, indicating that no valid value was found.
        :type AutoRenewFlagError: bool
        :param _Rollbacking: Whether the cloud disk is in the status of snapshot rollback. Value range: <br><li>false: No <br><li>true: Yes
        :type Rollbacking: bool
        :param _InstanceIdList: For non-shareable cloud disks, this parameter is null. For shareable cloud disks, this parameters indicates this cloud disk's Instance IDs currently mounted to the CVM.
        :type InstanceIdList: list of str
        :param _Encrypt: Whether the cloud disk is encrypted. Value range: <br><li>false: Not encrypted <br><li>true: Encrypted.
        :type Encrypt: bool
        :param _DiskName: Cloud disk name.
        :type DiskName: str
        :param _BackupDisk: Specifies whether to create a snapshot when the cloud disk is terminated due to overdue payment or expiration. `true`: create snapshot; `false`: do not create snapshot.
        :type BackupDisk: bool
        :param _Tags: The tag bound to the cloud disk. The value Null is used when no tag is bound to the cloud disk.
Note: This field may return null, indicating that no valid value was found.
        :type Tags: list of Tag
        :param _InstanceId: ID of the CVM to which the cloud disk is mounted.
        :type InstanceId: str
        :param _AttachMode: Cloud disk mount method. Valid values: <br><li>PF: mount as a PF (Physical Function)<br><li>VF: mount as a VF (Virtual Function)
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AttachMode: str
        :param _AutoSnapshotPolicyIds: ID of the periodic snapshot associated to the cloud disk. This parameter is returned only if the value of parameter ReturnBindAutoSnapshotPolicy is TRUE when the API DescribeDisks is called.
Note: This field may return null, indicating that no valid value was found.
        :type AutoSnapshotPolicyIds: list of str
        :param _ThroughputPerformance: Extra performance for a cloud disk, in MB/sec.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ThroughputPerformance: int
        :param _Migrating: Whether cloud disk is in process of type change. Value range: <br><li>false: Cloud disk not in process of type change. <br><li>true: Cloud disk type change has been launched, and migration is in process.
Note: This field may return null, indicating that no valid value was found.
        :type Migrating: bool
        :param _DiskId: Cloud disk ID.
        :type DiskId: str
        :param _SnapshotSize: The total capacity of the snapshots of the cloud disk. Unit: MB.
        :type SnapshotSize: int
        :param _Placement: Location of the cloud disk.
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param _IsReturnable: Determines whether or not prepaid cloud disk supports active return. <br><li>true: Active return supported.<br><li>false: Active return not supported.
Note: This field may return null, indicating that no valid value was found.
        :type IsReturnable: bool
        :param _DeadlineTime: Expiration time of the cloud disk.
        :type DeadlineTime: str
        :param _Attached: Whether the cloud disk is mounted to the CVM. Value range: <br><li>false: Unmounted <br><li>true: Mounted.
        :type Attached: bool
        :param _DiskSize: Cloud disk size (in GB).
        :type DiskSize: int
        :param _MigratePercent: Migration progress of cloud disk type change, from 0 to 100.
Note: This field may return null, indicating that no valid value was found.
        :type MigratePercent: int
        :param _DiskUsage: Cloud disk type. Value range:<br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk.
        :type DiskUsage: str
        :param _DiskChargeType: Billing method. Value range: <br><li>PREPAID: Prepaid, that is, monthly subscription<br><li>POSTPAID_BY_HOUR: Postpaid, that is, pay as you go.
        :type DiskChargeType: str
        :param _Portable: Whether it is an elastic cloud disk. false: Non-elastic cloud disk; true: Elastic cloud disk.
        :type Portable: bool
        :param _SnapshotAbility: Whether the cloud disk has the capability to create snapshots. Value range: <br><li>false: Cannot create snapshots. true: Can create snapshots.
        :type SnapshotAbility: bool
        :param _DeadlineError: This field is only applicable when the instance is already mounted to the cloud disk, and both the instance and the cloud disk use monthly subscription. <br><li>true: Expiration time of cloud disk is earlier than that of the instance.<br><li>false:Expiration time of cloud disk is later than that of the instance.
Note: This field may return null, indicating that no valid value was found.
        :type DeadlineError: bool
        :param _RollbackPercent: Rollback progress of a cloud disk snapshot.
        :type RollbackPercent: int
        :param _DifferDaysOfDeadline: Number of days from current time until disk expiration (only applicable for prepaid disks).
Note: This field may return null, indicating that no valid value was found.
        :type DifferDaysOfDeadline: int
        :param _ReturnFailCode: In circumstances where the prepaid cloud disk does not support active return, this parameter indicates the reason that return is not supported. Value range: <br><li>1: The cloud disk has already been returned. <br><li>2: The cloud disk has already expired. <br><li>3: The cloud disk does not support return. <br><li> 8: The limit on the number of returns is exceeded.
Note: This field may return null, indicating that no valid value was found.
        :type ReturnFailCode: int
        :param _Shareable: Whether or not cloud disk is shareable cloud disk.
        :type Shareable: bool
        :param _CreateTime: Creation time of the cloud disk.
        :type CreateTime: str
        :param _DeleteSnapshot: Delete the associated non-permanently reserved snapshots upon deletion of the source cloud disk. `0`: No (default). `1`: Yes. To check whether a snapshot is permanently reserved, refer to the `IsPermanent` field returned by the `DescribeSnapshots` API. 
        :type DeleteSnapshot: int
        :param _DiskBackupQuota: Quota of cloud disk backup points, i.e., the maximum number of backup points that a cloud disk can have.
        :type DiskBackupQuota: int
        :param _DiskBackupCount: Number of used cloud disk backups.
        :type DiskBackupCount: int
        :param _InstanceType: Type of the instance mounted to the cloud disk. Valid values: <br><li>CVM<br><li>EKS
        :type InstanceType: str
        :param _LastAttachInsId: ID of the last instance to which the cloud disk is attached
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastAttachInsId: str
        :param _ErrorPrompt: Error message for the last operation of the cloud disk
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorPrompt: str
        :param _BurstPerformance: Whether the cloud disk has enabled disk bursting. Note: This field may return null, indicating that no valid values can be obtained.
        :type BurstPerformance: bool
        """
        self._DeleteWithInstance = None
        self._RenewFlag = None
        self._DiskType = None
        self._DiskState = None
        self._SnapshotCount = None
        self._AutoRenewFlagError = None
        self._Rollbacking = None
        self._InstanceIdList = None
        self._Encrypt = None
        self._DiskName = None
        self._BackupDisk = None
        self._Tags = None
        self._InstanceId = None
        self._AttachMode = None
        self._AutoSnapshotPolicyIds = None
        self._ThroughputPerformance = None
        self._Migrating = None
        self._DiskId = None
        self._SnapshotSize = None
        self._Placement = None
        self._IsReturnable = None
        self._DeadlineTime = None
        self._Attached = None
        self._DiskSize = None
        self._MigratePercent = None
        self._DiskUsage = None
        self._DiskChargeType = None
        self._Portable = None
        self._SnapshotAbility = None
        self._DeadlineError = None
        self._RollbackPercent = None
        self._DifferDaysOfDeadline = None
        self._ReturnFailCode = None
        self._Shareable = None
        self._CreateTime = None
        self._DeleteSnapshot = None
        self._DiskBackupQuota = None
        self._DiskBackupCount = None
        self._InstanceType = None
        self._LastAttachInsId = None
        self._ErrorPrompt = None
        self._BurstPerformance = None

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskState(self):
        return self._DiskState

    @DiskState.setter
    def DiskState(self, DiskState):
        self._DiskState = DiskState

    @property
    def SnapshotCount(self):
        return self._SnapshotCount

    @SnapshotCount.setter
    def SnapshotCount(self, SnapshotCount):
        self._SnapshotCount = SnapshotCount

    @property
    def AutoRenewFlagError(self):
        return self._AutoRenewFlagError

    @AutoRenewFlagError.setter
    def AutoRenewFlagError(self, AutoRenewFlagError):
        self._AutoRenewFlagError = AutoRenewFlagError

    @property
    def Rollbacking(self):
        return self._Rollbacking

    @Rollbacking.setter
    def Rollbacking(self, Rollbacking):
        self._Rollbacking = Rollbacking

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def DiskName(self):
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def BackupDisk(self):
        return self._BackupDisk

    @BackupDisk.setter
    def BackupDisk(self, BackupDisk):
        self._BackupDisk = BackupDisk

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AttachMode(self):
        return self._AttachMode

    @AttachMode.setter
    def AttachMode(self, AttachMode):
        self._AttachMode = AttachMode

    @property
    def AutoSnapshotPolicyIds(self):
        return self._AutoSnapshotPolicyIds

    @AutoSnapshotPolicyIds.setter
    def AutoSnapshotPolicyIds(self, AutoSnapshotPolicyIds):
        self._AutoSnapshotPolicyIds = AutoSnapshotPolicyIds

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def Migrating(self):
        return self._Migrating

    @Migrating.setter
    def Migrating(self, Migrating):
        self._Migrating = Migrating

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def SnapshotSize(self):
        return self._SnapshotSize

    @SnapshotSize.setter
    def SnapshotSize(self, SnapshotSize):
        self._SnapshotSize = SnapshotSize

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def IsReturnable(self):
        return self._IsReturnable

    @IsReturnable.setter
    def IsReturnable(self, IsReturnable):
        self._IsReturnable = IsReturnable

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Attached(self):
        return self._Attached

    @Attached.setter
    def Attached(self, Attached):
        self._Attached = Attached

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MigratePercent(self):
        return self._MigratePercent

    @MigratePercent.setter
    def MigratePercent(self, MigratePercent):
        self._MigratePercent = MigratePercent

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def Portable(self):
        return self._Portable

    @Portable.setter
    def Portable(self, Portable):
        self._Portable = Portable

    @property
    def SnapshotAbility(self):
        return self._SnapshotAbility

    @SnapshotAbility.setter
    def SnapshotAbility(self, SnapshotAbility):
        self._SnapshotAbility = SnapshotAbility

    @property
    def DeadlineError(self):
        return self._DeadlineError

    @DeadlineError.setter
    def DeadlineError(self, DeadlineError):
        self._DeadlineError = DeadlineError

    @property
    def RollbackPercent(self):
        return self._RollbackPercent

    @RollbackPercent.setter
    def RollbackPercent(self, RollbackPercent):
        self._RollbackPercent = RollbackPercent

    @property
    def DifferDaysOfDeadline(self):
        return self._DifferDaysOfDeadline

    @DifferDaysOfDeadline.setter
    def DifferDaysOfDeadline(self, DifferDaysOfDeadline):
        self._DifferDaysOfDeadline = DifferDaysOfDeadline

    @property
    def ReturnFailCode(self):
        return self._ReturnFailCode

    @ReturnFailCode.setter
    def ReturnFailCode(self, ReturnFailCode):
        self._ReturnFailCode = ReturnFailCode

    @property
    def Shareable(self):
        return self._Shareable

    @Shareable.setter
    def Shareable(self, Shareable):
        self._Shareable = Shareable

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeleteSnapshot(self):
        return self._DeleteSnapshot

    @DeleteSnapshot.setter
    def DeleteSnapshot(self, DeleteSnapshot):
        self._DeleteSnapshot = DeleteSnapshot

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota

    @property
    def DiskBackupCount(self):
        return self._DiskBackupCount

    @DiskBackupCount.setter
    def DiskBackupCount(self, DiskBackupCount):
        self._DiskBackupCount = DiskBackupCount

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def LastAttachInsId(self):
        return self._LastAttachInsId

    @LastAttachInsId.setter
    def LastAttachInsId(self, LastAttachInsId):
        self._LastAttachInsId = LastAttachInsId

    @property
    def ErrorPrompt(self):
        return self._ErrorPrompt

    @ErrorPrompt.setter
    def ErrorPrompt(self, ErrorPrompt):
        self._ErrorPrompt = ErrorPrompt

    @property
    def BurstPerformance(self):
        return self._BurstPerformance

    @BurstPerformance.setter
    def BurstPerformance(self, BurstPerformance):
        self._BurstPerformance = BurstPerformance


    def _deserialize(self, params):
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._RenewFlag = params.get("RenewFlag")
        self._DiskType = params.get("DiskType")
        self._DiskState = params.get("DiskState")
        self._SnapshotCount = params.get("SnapshotCount")
        self._AutoRenewFlagError = params.get("AutoRenewFlagError")
        self._Rollbacking = params.get("Rollbacking")
        self._InstanceIdList = params.get("InstanceIdList")
        self._Encrypt = params.get("Encrypt")
        self._DiskName = params.get("DiskName")
        self._BackupDisk = params.get("BackupDisk")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._AttachMode = params.get("AttachMode")
        self._AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._Migrating = params.get("Migrating")
        self._DiskId = params.get("DiskId")
        self._SnapshotSize = params.get("SnapshotSize")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._IsReturnable = params.get("IsReturnable")
        self._DeadlineTime = params.get("DeadlineTime")
        self._Attached = params.get("Attached")
        self._DiskSize = params.get("DiskSize")
        self._MigratePercent = params.get("MigratePercent")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskChargeType = params.get("DiskChargeType")
        self._Portable = params.get("Portable")
        self._SnapshotAbility = params.get("SnapshotAbility")
        self._DeadlineError = params.get("DeadlineError")
        self._RollbackPercent = params.get("RollbackPercent")
        self._DifferDaysOfDeadline = params.get("DifferDaysOfDeadline")
        self._ReturnFailCode = params.get("ReturnFailCode")
        self._Shareable = params.get("Shareable")
        self._CreateTime = params.get("CreateTime")
        self._DeleteSnapshot = params.get("DeleteSnapshot")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        self._DiskBackupCount = params.get("DiskBackupCount")
        self._InstanceType = params.get("InstanceType")
        self._LastAttachInsId = params.get("LastAttachInsId")
        self._ErrorPrompt = params.get("ErrorPrompt")
        self._BurstPerformance = params.get("BurstPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskBackup(AbstractModel):
    """Cloud disk backup point.

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: Cloud disk backup point ID.
        :type DiskBackupId: str
        :param _DiskId: ID of the cloud disk with which the backup point is associated.
        :type DiskId: str
        :param _DiskSize: Cloud disk size in GB.
        :type DiskSize: int
        :param _DiskUsage: Cloud disk type. Valid values:<br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk
        :type DiskUsage: str
        :param _DiskBackupName: Backup point name.
        :type DiskBackupName: str
        :param _DiskBackupState: Cloud disk backup point status. Valid values:<br><li>NORMAL: Normal<br><li>CREATING: Creating<br><li>ROLLBACKING: Rolling back
        :type DiskBackupState: str
        :param _Percent: Cloud disk creation progress in percentage.
        :type Percent: int
        :param _CreateTime: Creation time of the cloud disk backup point.
        :type CreateTime: str
        :param _Encrypt: Whether the cloud disk is encrypted. Valid values: <br><li>false: Not encrypted <br><li>true: Encrypted
        :type Encrypt: bool
        """
        self._DiskBackupId = None
        self._DiskId = None
        self._DiskSize = None
        self._DiskUsage = None
        self._DiskBackupName = None
        self._DiskBackupState = None
        self._Percent = None
        self._CreateTime = None
        self._Encrypt = None

    @property
    def DiskBackupId(self):
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskBackupName(self):
        return self._DiskBackupName

    @DiskBackupName.setter
    def DiskBackupName(self, DiskBackupName):
        self._DiskBackupName = DiskBackupName

    @property
    def DiskBackupState(self):
        return self._DiskBackupState

    @DiskBackupState.setter
    def DiskBackupState(self, DiskBackupState):
        self._DiskBackupState = DiskBackupState

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskBackupName = params.get("DiskBackupName")
        self._DiskBackupState = params.get("DiskBackupState")
        self._Percent = params.get("Percent")
        self._CreateTime = params.get("CreateTime")
        self._Encrypt = params.get("Encrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskChargePrepaid(AbstractModel):
    """Billing mode of the instance

    """

    def __init__(self):
        r"""
        :param _Period: Subscription period of the cloud disk in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param _RenewFlag: Auto-renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: Notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: Notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify upon expiration nor renew automatically <br><br>Default value: NOTIFY_AND_MANUAL_RENEW.
        :type RenewFlag: str
        :param _CurInstanceDeadline: You can specify this parameter when you need to ensure that a cloud disk and the CVM instance to which it is attached have the same expiration time. This parameter represents the current expiration time of the instance. In this case, if you specify `Period`, `Period` will represent how long you want to renew the instance, and the cloud disk will be renewed based on the new expiration time of the instance. For example, the value of this parameter can be `2018-03-30 20:15:03`.
        :type CurInstanceDeadline: str
        """
        self._Period = None
        self._RenewFlag = None
        self._CurInstanceDeadline = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def CurInstanceDeadline(self):
        return self._CurInstanceDeadline

    @CurInstanceDeadline.setter
    def CurInstanceDeadline(self, CurInstanceDeadline):
        self._CurInstanceDeadline = CurInstanceDeadline


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        self._CurInstanceDeadline = params.get("CurInstanceDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskConfig(AbstractModel):
    """Cloud disk configuration.

    """

    def __init__(self):
        r"""
        :param _Available: Whether the configuration is available.
        :type Available: bool
        :param _DiskChargeType: Billing method. Value range: <br><li>PREPAID: Prepaid, that is, monthly subscription<br><li>POSTPAID_BY_HOUR: Postpaid, that is, pay as you go.
        :type DiskChargeType: str
        :param _Zone: The [Availability Region](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) of the cloud drive.
        :type Zone: str
        :param _InstanceFamily: Instance model series. For more information, please see [Instance Models](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1)
Note: This field may return null, indicating that no valid value was found.
        :type InstanceFamily: str
        :param _DiskType: Type of cloud disk medium. Value range: <br><li>CLOUD_BASIC: Ordinary cloud disk <br><li>CLOUD_PREMIUM: Premium cloud storage <br><li>CLOUD_SSD: SSD cloud disk.
        :type DiskType: str
        :param _StepSize: Minimum increment of cloud disk size adjustment in GB.
Note: This field might return null, indicating that no valid values can be obtained.
        :type StepSize: int
        :param _ExtraPerformanceRange: Additional performance range.
Note: This field might return null, indicating that no valid values can be obtained.
        :type ExtraPerformanceRange: list of int
        :param _DeviceClass: Instance model.
Note: This field may return null, indicating that no valid value was found.
        :type DeviceClass: str
        :param _DiskUsage: Cloud disk type. Value range: <br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk.
        :type DiskUsage: str
        :param _MinDiskSize: The minimum configurable cloud disk size (in GB).
        :type MinDiskSize: int
        :param _MaxDiskSize: The maximum configurable cloud disk size (in GB).
        :type MaxDiskSize: int
        :param _Price: Price of a monthly subscribed or pay-as-you-go cloud disk.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Price: :class:`tencentcloud.cbs.v20170312.models.Price`
        """
        self._Available = None
        self._DiskChargeType = None
        self._Zone = None
        self._InstanceFamily = None
        self._DiskType = None
        self._StepSize = None
        self._ExtraPerformanceRange = None
        self._DeviceClass = None
        self._DiskUsage = None
        self._MinDiskSize = None
        self._MaxDiskSize = None
        self._Price = None

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def StepSize(self):
        return self._StepSize

    @StepSize.setter
    def StepSize(self, StepSize):
        self._StepSize = StepSize

    @property
    def ExtraPerformanceRange(self):
        return self._ExtraPerformanceRange

    @ExtraPerformanceRange.setter
    def ExtraPerformanceRange(self, ExtraPerformanceRange):
        self._ExtraPerformanceRange = ExtraPerformanceRange

    @property
    def DeviceClass(self):
        return self._DeviceClass

    @DeviceClass.setter
    def DeviceClass(self, DeviceClass):
        self._DeviceClass = DeviceClass

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def MinDiskSize(self):
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def MaxDiskSize(self):
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price


    def _deserialize(self, params):
        self._Available = params.get("Available")
        self._DiskChargeType = params.get("DiskChargeType")
        self._Zone = params.get("Zone")
        self._InstanceFamily = params.get("InstanceFamily")
        self._DiskType = params.get("DiskType")
        self._StepSize = params.get("StepSize")
        self._ExtraPerformanceRange = params.get("ExtraPerformanceRange")
        self._DeviceClass = params.get("DeviceClass")
        self._DiskUsage = params.get("DiskUsage")
        self._MinDiskSize = params.get("MinDiskSize")
        self._MaxDiskSize = params.get("MaxDiskSize")
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskOperationLog(AbstractModel):
    """The operation log of the cloud disk.

    """

    def __init__(self):
        r"""
        :param _Operator: UIN of operator.
        :type Operator: str
        :param _Operation: Operation type. Value range:
CBS_OPERATION_ATTACH: Mount cloud disk
CBS_OPERATION_DETACH: Unmount cloud disk
CBS_OPERATION_RENEW: Renew
CBS_OPERATION_EXPAND: Expand
CBS_OPERATION_CREATE: Create
CBS_OPERATION_ISOLATE: Isolate
CBS_OPERATION_MODIFY: Modify cloud disk attributes
ASP_OPERATION_BIND: Associate scheduled snapshot policy
ASP_OPERATION_UNBIND: Cancel associated scheduled snapshot policy
        :type Operation: str
        :param _DiskId: Cloud disk ID of operation.
        :type DiskId: str
        :param _OperationState: Status of operation. Value range:
SUCCESS: Operation successful 
FAILED: Operation failed 
PROCESSING: Operation in process
        :type OperationState: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        """
        self._Operator = None
        self._Operation = None
        self._DiskId = None
        self._OperationState = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def OperationState(self):
        return self._OperationState

    @OperationState.setter
    def OperationState(self, OperationState):
        self._OperationState = OperationState

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
        self._Operator = params.get("Operator")
        self._Operation = params.get("Operation")
        self._DiskId = params.get("DiskId")
        self._OperationState = params.get("OperationState")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Key-value pair filters for conditional filtering queries.

    """

    def __init__(self):
        r"""
        :param _Name: Name of filter key.
        :type Name: str
        :param _Values: One or more filter values.
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
        


class GetSnapOverviewRequest(AbstractModel):
    """GetSnapOverview request structure.

    """


class GetSnapOverviewResponse(AbstractModel):
    """GetSnapOverview response structure.

    """

    def __init__(self):
        r"""
        :param _TotalSize: The total snapshot size of the user
        :type TotalSize: float
        :param _RealTradeSize: The total billed snapshot size of the user
        :type RealTradeSize: float
        :param _FreeQuota: Free tier of snapshot
        :type FreeQuota: float
        :param _TotalNums: Total number of snapshots
        :type TotalNums: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalSize = None
        self._RealTradeSize = None
        self._FreeQuota = None
        self._TotalNums = None
        self._RequestId = None

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def RealTradeSize(self):
        return self._RealTradeSize

    @RealTradeSize.setter
    def RealTradeSize(self, RealTradeSize):
        self._RealTradeSize = RealTradeSize

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def TotalNums(self):
        return self._TotalNums

    @TotalNums.setter
    def TotalNums(self, TotalNums):
        self._TotalNums = TotalNums

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalSize = params.get("TotalSize")
        self._RealTradeSize = params.get("RealTradeSize")
        self._FreeQuota = params.get("FreeQuota")
        self._TotalNums = params.get("TotalNums")
        self._RequestId = params.get("RequestId")


class Image(AbstractModel):
    """Image

    """

    def __init__(self):
        r"""
        :param _ImageId: Image instance ID.
        :type ImageId: str
        :param _ImageName: Image name.
        :type ImageName: str
        """
        self._ImageId = None
        self._ImageName = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitializeDisksRequest(AbstractModel):
    """InitializeDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: ID list of the cloud disks to be reinitialized. Up to 20 disks can be reinitialized at a time.
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitializeDisksResponse(AbstractModel):
    """InitializeDisks response structure.

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


class InquirePriceModifyDiskBackupQuotaRequest(AbstractModel):
    """InquirePriceModifyDiskBackupQuota request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: Cloud disk ID, which can be queried through the `DescribeDisks` API.
        :type DiskId: str
        :param _DiskBackupQuota: Cloud disk backup point quota after the modification, i.e., the number of backup points that a cloud disk can have.
        :type DiskBackupQuota: int
        """
        self._DiskId = None
        self._DiskBackupQuota = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDiskBackupQuotaResponse(AbstractModel):
    """InquirePriceModifyDiskBackupQuota response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: Price of the cloud disk after its backup point quota is modified.
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = Price()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceModifyDiskExtraPerformanceRequest(AbstractModel):
    """InquirePriceModifyDiskExtraPerformance request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: Cloud disk ID, which can be queried via the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskId: str
        :param _ThroughputPerformance: The extra throughput to purchase, in MB/s
        :type ThroughputPerformance: int
        """
        self._DiskId = None
        self._ThroughputPerformance = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDiskExtraPerformanceResponse(AbstractModel):
    """InquirePriceModifyDiskExtraPerformance response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: Price for purchasing the extra performance
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = Price()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquiryPriceCreateDisksRequest(AbstractModel):
    """InquiryPriceCreateDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskChargeType: Cloud disk billing mode. <br><li>POSTPAID_BY_HOUR: Hourly pay-as-you-go.
        :type DiskChargeType: str
        :param _DiskType: Cloud disk media type. Valid values: <br><li>CLOUD_BASIC: HDD Cloud Storage<br><li>CLOUD_PREMIUM: Premium Cloud Disk<br><li>CLOUD_SSD: SSD<br><li>CLOUD_HSSD: Enhanced SSD<br><li>CLOUD_TSSD: ulTra SSD.
        :type DiskType: str
        :param _DiskSize: Cloud disk size in GB. For the value range, see [Cloud Disk Types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        :param _ProjectId: ID of the project to which the cloud disk belongs.
        :type ProjectId: int
        :param _DiskCount: Number of cloud disks to be purchased. If it is not specified, `1` will be used by default.
        :type DiskCount: int
        :param _ThroughputPerformance: Extra performance in MB/s purchased for a cloud disk.<br>This parameter is only valid for Enhanced SSD (CLOUD_HSSD) and ulTra SSD (CLOUD_TSSD).
        :type ThroughputPerformance: int
        :param _DiskChargePrepaid: Relevant parameter settings for the prepaid mode (i.e., monthly subscription). The monthly subscription cloud disk purchase attributes such as usage period and whether or not auto-renewal is set up can be specified using this parameter. <br>This parameter is required when creating a prepaid cloud disk. This parameter is not required when creating an hourly postpaid cloud disk.
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param _DiskBackupQuota: Specifies the cloud disk backup point quota.
        :type DiskBackupQuota: int
        """
        self._DiskChargeType = None
        self._DiskType = None
        self._DiskSize = None
        self._ProjectId = None
        self._DiskCount = None
        self._ThroughputPerformance = None
        self._DiskChargePrepaid = None
        self._DiskBackupQuota = None

    @property
    def DiskChargeType(self):
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DiskCount(self):
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def DiskChargePrepaid(self):
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskChargeType = params.get("DiskChargeType")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._ProjectId = params.get("ProjectId")
        self._DiskCount = params.get("DiskCount")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDisksResponse(AbstractModel):
    """InquiryPriceCreateDisks response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: Describes the price of newly purchased cloud disks.
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = Price()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResizeDiskRequest(AbstractModel):
    """InquiryPriceResizeDisk request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: ID of the cloud disk, which can be queried via the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1).
        :type DiskId: str
        :param _DiskSize: Cloud disk size after scale out (in GB). This cannot be smaller than the current size of the cloud disk. For the value range of the cloud disk sizes, see cloud disk [Product Types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        :param _ProjectId: ID of project the cloud disk belongs to. If selected, it can only be used for authentication.
        :type ProjectId: int
        """
        self._DiskId = None
        self._DiskSize = None
        self._ProjectId = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResizeDiskResponse(AbstractModel):
    """InquiryPriceResizeDisk response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: Describes the price of expanding the cloud disk.
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = PrepayPrice()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class ModifyAutoSnapshotPolicyAttributeRequest(AbstractModel):
    """ModifyAutoSnapshotPolicyAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Scheduled snapshot policy ID.
        :type AutoSnapshotPolicyId: str
        :param _IsActivated: Whether or not the scheduled snapshot policy is activated. FALSE: Not activated. TRUE: Activated. The default value is TRUE.
        :type IsActivated: bool
        :param _IsPermanent: Whether the snapshot created by this scheduled snapshot policy is retained permanently. FALSE: Not retained permanently. TRUE: Retained permanently. The default value is FALSE.
        :type IsPermanent: bool
        :param _AutoSnapshotPolicyName: The name of the scheduled snapshot policy to be created. If it is left empty, the default is 'Not named'. The maximum length cannot exceed 60 bytes.
        :type AutoSnapshotPolicyName: str
        :param _Policy: The policy for executing the scheduled snapshot.
        :type Policy: list of Policy
        :param _RetentionDays: Number of days to retain the snapshots created according to this scheduled snapshot policy. If this parameter is specified, `IsPermanent` cannot be specified as `TRUE`; otherwise, they will conflict with each other.
        :type RetentionDays: int
        """
        self._AutoSnapshotPolicyId = None
        self._IsActivated = None
        self._IsPermanent = None
        self._AutoSnapshotPolicyName = None
        self._Policy = None
        self._RetentionDays = None

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def IsPermanent(self):
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def AutoSnapshotPolicyName(self):
        return self._AutoSnapshotPolicyName

    @AutoSnapshotPolicyName.setter
    def AutoSnapshotPolicyName(self, AutoSnapshotPolicyName):
        self._AutoSnapshotPolicyName = AutoSnapshotPolicyName

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def RetentionDays(self):
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._IsActivated = params.get("IsActivated")
        self._IsPermanent = params.get("IsPermanent")
        self._AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self._Policy.append(obj)
        self._RetentionDays = params.get("RetentionDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoSnapshotPolicyAttributeResponse(AbstractModel):
    """ModifyAutoSnapshotPolicyAttribute response structure.

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


class ModifyDiskAttributesRequest(AbstractModel):
    """ModifyDiskAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: IDs of one or more cloud disks to be operated. If multiple cloud disk IDs are selected, it only supports modifying all cloud disks with the same attributes.
        :type DiskIds: list of str
        :param _DiskName: Name of new cloud disk.
        :type DiskName: str
        :param _Portable: Whether it is an elastic cloud disk. FALSE: non-elastic cloud disk; TRUE: elastic cloud disk. You can only modify non-elastic cloud disks to elastic cloud disks.
        :type Portable: bool
        :param _ProjectId: The new project ID of the cloud disk. Only the project ID of elastic cloud disk can be modified. The available projects and their IDs can be queried via the API [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1).
        :type ProjectId: int
        :param _DeleteWithInstance: Whether the cloud disk is terminated with the CVM after it has been successfully mounted. `TRUE` indicates that it is terminated with the CVM. `FALSE` indicates that it is not terminated with the CVM. This is only supported for cloud disks and data disks that are pay-as-you-go.
        :type DeleteWithInstance: bool
        :param _DiskType: When changing the type of a cloud disk, this parameter can be passed to indicate the desired cloud disk type. Value range: <br><li>CLOUD_PREMIUM: Premium cloud storage.  <br><li>CLOUD_SSD: SSD cloud disk. <br>Currently, batch operations are not supported for changing type. That is, when `DiskType` is passed, only one cloud disk can be passed through `DiskIds`. <br>When the cloud disk type is changed, the changing of other attributes is not supported concurrently.
        :type DiskType: str
        :param _BurstPerformanceOperation: Enable/disable disk bursting.
        :type BurstPerformanceOperation: str
        """
        self._DiskIds = None
        self._DiskName = None
        self._Portable = None
        self._ProjectId = None
        self._DeleteWithInstance = None
        self._DiskType = None
        self._BurstPerformanceOperation = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskName(self):
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def Portable(self):
        return self._Portable

    @Portable.setter
    def Portable(self, Portable):
        self._Portable = Portable

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def BurstPerformanceOperation(self):
        return self._BurstPerformanceOperation

    @BurstPerformanceOperation.setter
    def BurstPerformanceOperation(self, BurstPerformanceOperation):
        self._BurstPerformanceOperation = BurstPerformanceOperation


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._DiskName = params.get("DiskName")
        self._Portable = params.get("Portable")
        self._ProjectId = params.get("ProjectId")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._DiskType = params.get("DiskType")
        self._BurstPerformanceOperation = params.get("BurstPerformanceOperation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskAttributesResponse(AbstractModel):
    """ModifyDiskAttributes response structure.

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


class ModifyDiskBackupQuotaRequest(AbstractModel):
    """ModifyDiskBackupQuota request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: Cloud disk ID.
        :type DiskId: str
        :param _DiskBackupQuota: Cloud disk backup point quota after the adjustment
        :type DiskBackupQuota: int
        """
        self._DiskId = None
        self._DiskBackupQuota = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupQuota(self):
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskBackupQuotaResponse(AbstractModel):
    """ModifyDiskBackupQuota response structure.

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


class ModifyDiskExtraPerformanceRequest(AbstractModel):
    """ModifyDiskExtraPerformance request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: ID of the cloud disk to create a snapshot, which can be obtained via the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskId: str
        :param _ThroughputPerformance: The extra throughput to purchase, in MB/s
        :type ThroughputPerformance: int
        """
        self._DiskId = None
        self._ThroughputPerformance = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskExtraPerformanceResponse(AbstractModel):
    """ModifyDiskExtraPerformance response structure.

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


class ModifySnapshotAttributeRequest(AbstractModel):
    """ModifySnapshotAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot ID, which can be queried via [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :type SnapshotId: str
        :param _SnapshotName: Name of new snapshot. Maximum length is 60 bytes.
        :type SnapshotName: str
        :param _IsPermanent: Snapshot retention mode. Valid values: `FALSE`: non-permanent retention; `TRUE`: permanent retention.
        :type IsPermanent: bool
        :param _Deadline: Expiration time of the snapshot. Setting this parameter will set the snapshot retention mode to `FALSE` (non-permanent retention) and the snapshot will be automatically deleted upon expiration.
        :type Deadline: str
        """
        self._SnapshotId = None
        self._SnapshotName = None
        self._IsPermanent = None
        self._Deadline = None

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
    def IsPermanent(self):
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._SnapshotName = params.get("SnapshotName")
        self._IsPermanent = params.get("IsPermanent")
        self._Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotAttributeResponse(AbstractModel):
    """ModifySnapshotAttribute response structure.

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


class ModifySnapshotsSharePermissionRequest(AbstractModel):
    """ModifySnapshotsSharePermission request structure.

    """

    def __init__(self):
        r"""
        :param _AccountIds: List of account IDs with which a snapshot is shared. For the format of array-type parameters, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/568?from_cn_redirect=1). You can find the account ID in [Account Information](https://console.cloud.tencent.com/developer).
        :type AccountIds: list of str
        :param _Permission: Operations. Valid values: `SHARE`, sharing an image; `CANCEL`, cancelling the sharing of an image.
        :type Permission: str
        :param _SnapshotIds: The ID of the snapshot. You can obtain this by using [DescribeSnapshots](https://intl.cloud.tencent.com/document/api/362/15647?from_cn_redirect=1).
        :type SnapshotIds: list of str
        """
        self._AccountIds = None
        self._Permission = None
        self._SnapshotIds = None

    @property
    def AccountIds(self):
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds


    def _deserialize(self, params):
        self._AccountIds = params.get("AccountIds")
        self._Permission = params.get("Permission")
        self._SnapshotIds = params.get("SnapshotIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotsSharePermissionResponse(AbstractModel):
    """ModifySnapshotsSharePermission response structure.

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


class Placement(AbstractModel):
    """This describes the abstract location of the instance, including the availability zone in which it is located, the projects to which it belongs, and the ID and name of the dedicated clusters to which it belongs.

    """

    def __init__(self):
        r"""
        :param _Zone: The ID of the [Availability Zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) to which the cloud disk belongs. This parameter can be obtained from the Zone field in the returned values of [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1).
        :type Zone: str
        :param _CageId: Cage ID. When it is an input parameter, the specified CageID resource is operated, and it can be left blank. When it is an output parameter, it is the ID of the cage the resource belongs to, and it can be left blank.
Note: This field may return null, indicating that no valid value was found.
        :type CageId: str
        :param _ProjectId: ID of the project to which the instance belongs. This parameter can be obtained from the projectId field in the returned values of [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1). If this is left empty, default project is used.
        :type ProjectId: int
        :param _ProjectName: Project name of the instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param _CdcName: Dedicated cluster name. When it is an input parameter, it is ignored.  When it is an output parameter, it is the name of the dedicated cluster the cloud disk belongs to, and it can be left blank.
Note: This field may return null, indicating that no valid value was found.
        :type CdcName: str
        :param _CdcId: ID of dedicated cluster which the instance belongs to. When it is an input parameter, the specified CdcId dedicated cluster resource is operated, and it can be left blank. When it is an output parameter, it is the ID of the dedicated cluster which the resource belongs to, and it can be left blank.
Note: This field may return null, indicating that no valid value was found.
        :type CdcId: str
        :param _DedicatedClusterId: Dedicated cluster ID
        :type DedicatedClusterId: str
        """
        self._Zone = None
        self._CageId = None
        self._ProjectId = None
        self._ProjectName = None
        self._CdcName = None
        self._CdcId = None
        self._DedicatedClusterId = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def CdcName(self):
        return self._CdcName

    @CdcName.setter
    def CdcName(self, CdcName):
        self._CdcName = CdcName

    @property
    def CdcId(self):
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def DedicatedClusterId(self):
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._CageId = params.get("CageId")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._CdcName = params.get("CdcName")
        self._CdcId = params.get("CdcId")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Policy(AbstractModel):
    """Execution policy for scheduled snapshot. It indicates that a scheduled snapshot policy is executed at the specified `Hour` in the days specified by `DayOfWeek` or `DayOfMonth` or once every `IntervalDays` days. Note: `DayOfWeek`, `DayOfMonth`, and `IntervalDays` are mutually exclusive, and only one policy rule can be set.

    """

    def __init__(self):
        r"""
        :param _Hour: Specifies the time that that the scheduled snapshot policy will be triggered. The unit is hour. The value range is [0-23]. 00:00-23:00 is a total of 24 time points that can be selected. 1 indicates 01:00, and so on.
        :type Hour: list of int non-negative
        :param _DayOfWeek: Specifies the days of the week, from Monday to Sunday, on which a scheduled snapshot will be triggered. Value range: [0, 6]. 0 indicates triggering on Sunday, 1-6 indicate triggering on Monday-Saturday.
        :type DayOfWeek: list of int non-negative
        :param _DayOfMonth: Specifies the dates of the month on which a scheduled snapshot will be triggered. Value range: [1, 31]. `1` to `31` indicate the specific dates of the month; for example, `5` indicates the 5th day of the month. Note: If you set a date that does not exist in some months such as 29, 30, and 31, these months will be skipped for scheduled snapshot creation.
        :type DayOfMonth: list of int non-negative
        :param _IntervalDays: Specifies the interval for creating scheduled snapshots in days. Value range: [1, 365]. For example, if it is set to `5`, scheduled snapshots will be created every 5 days. Note: If you choose to back up by day, the time for the first backup is theoretically the day when the backup policy is created. If the backup policy creation time on the current day is later than the set backup time, the first backup will be performed in the second backup cycle.
        :type IntervalDays: int
        """
        self._Hour = None
        self._DayOfWeek = None
        self._DayOfMonth = None
        self._IntervalDays = None

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def DayOfWeek(self):
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

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
        self._DayOfWeek = params.get("DayOfWeek")
        self._DayOfMonth = params.get("DayOfMonth")
        self._IntervalDays = params.get("IntervalDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrepayPrice(AbstractModel):
    """The cost of a prepaid order.

    """

    def __init__(self):
        r"""
        :param _DiscountPrice: Discounted price of a monthly-subscribed cloud disk or a snapshot, in USD.
        :type DiscountPrice: float
        :param _ChargeUnit: Billing unit for pay-as-you-go cloud disks. Valid value: <br><li>HOUR: billed hourly.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ChargeUnit: str
        :param _UnitPriceHigh: Original unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceHigh: str
        :param _OriginalPriceHigh: Original payment of a monthly-subscribed cloud disk or a snapshot, in USD, with six decimal places.
        :type OriginalPriceHigh: str
        :param _OriginalPrice: Original payment of a monthly-subscribed cloud disk or a snapshot, in USD.
        :type OriginalPrice: float
        :param _UnitPriceDiscount: Discount unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: float
        :param _UnitPriceDiscountHigh: Discounted unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceDiscountHigh: str
        :param _DiscountPriceHigh: Discounted price of a monthly-subscribed cloud disk or a snapshot, in USD, with six decimal places.
        :type DiscountPriceHigh: str
        :param _UnitPrice: Original unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param _DetailPrices: Detailed billing items
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetailPrices: list of DetailPrice
        """
        self._DiscountPrice = None
        self._ChargeUnit = None
        self._UnitPriceHigh = None
        self._OriginalPriceHigh = None
        self._OriginalPrice = None
        self._UnitPriceDiscount = None
        self._UnitPriceDiscountHigh = None
        self._DiscountPriceHigh = None
        self._UnitPrice = None
        self._DetailPrices = None

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def UnitPriceHigh(self):
        return self._UnitPriceHigh

    @UnitPriceHigh.setter
    def UnitPriceHigh(self, UnitPriceHigh):
        self._UnitPriceHigh = UnitPriceHigh

    @property
    def OriginalPriceHigh(self):
        return self._OriginalPriceHigh

    @OriginalPriceHigh.setter
    def OriginalPriceHigh(self, OriginalPriceHigh):
        self._OriginalPriceHigh = OriginalPriceHigh

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def UnitPriceDiscountHigh(self):
        return self._UnitPriceDiscountHigh

    @UnitPriceDiscountHigh.setter
    def UnitPriceDiscountHigh(self, UnitPriceDiscountHigh):
        self._UnitPriceDiscountHigh = UnitPriceDiscountHigh

    @property
    def DiscountPriceHigh(self):
        return self._DiscountPriceHigh

    @DiscountPriceHigh.setter
    def DiscountPriceHigh(self, DiscountPriceHigh):
        self._DiscountPriceHigh = DiscountPriceHigh

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def DetailPrices(self):
        return self._DetailPrices

    @DetailPrices.setter
    def DetailPrices(self, DetailPrices):
        self._DetailPrices = DetailPrices


    def _deserialize(self, params):
        self._DiscountPrice = params.get("DiscountPrice")
        self._ChargeUnit = params.get("ChargeUnit")
        self._UnitPriceHigh = params.get("UnitPriceHigh")
        self._OriginalPriceHigh = params.get("OriginalPriceHigh")
        self._OriginalPrice = params.get("OriginalPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._UnitPriceDiscountHigh = params.get("UnitPriceDiscountHigh")
        self._DiscountPriceHigh = params.get("DiscountPriceHigh")
        self._UnitPrice = params.get("UnitPrice")
        if params.get("DetailPrices") is not None:
            self._DetailPrices = []
            for item in params.get("DetailPrices"):
                obj = DetailPrice()
                obj._deserialize(item)
                self._DetailPrices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """Describes the prepaid or postpaid price for the cloud disk.

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: Original price of a monthly-subscribed cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginalPrice: float
        :param _DiscountPrice: Discounted price of a monthly-subscribed cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiscountPrice: float
        :param _UnitPrice: Original unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param _ChargeUnit: Billing unit of a postpaid cloud disk. Value range: <br><li>HOUR: Billed by hour.
Note: This field may return null, indicating that no valid value was found.
        :type ChargeUnit: str
        :param _UnitPriceDiscount: Discount unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: float
        :param _OriginalPriceHigh: Original payment of a monthly-subscribed cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginalPriceHigh: str
        :param _DiscountPriceHigh: Discounted payment price of a monthly-subscribed cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiscountPriceHigh: str
        :param _UnitPriceHigh: Original unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceHigh: str
        :param _UnitPriceDiscountHigh: Discounted unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceDiscountHigh: str
        """
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._UnitPrice = None
        self._ChargeUnit = None
        self._UnitPriceDiscount = None
        self._OriginalPriceHigh = None
        self._DiscountPriceHigh = None
        self._UnitPriceHigh = None
        self._UnitPriceDiscountHigh = None

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def OriginalPriceHigh(self):
        return self._OriginalPriceHigh

    @OriginalPriceHigh.setter
    def OriginalPriceHigh(self, OriginalPriceHigh):
        self._OriginalPriceHigh = OriginalPriceHigh

    @property
    def DiscountPriceHigh(self):
        return self._DiscountPriceHigh

    @DiscountPriceHigh.setter
    def DiscountPriceHigh(self, DiscountPriceHigh):
        self._DiscountPriceHigh = DiscountPriceHigh

    @property
    def UnitPriceHigh(self):
        return self._UnitPriceHigh

    @UnitPriceHigh.setter
    def UnitPriceHigh(self, UnitPriceHigh):
        self._UnitPriceHigh = UnitPriceHigh

    @property
    def UnitPriceDiscountHigh(self):
        return self._UnitPriceDiscountHigh

    @UnitPriceDiscountHigh.setter
    def UnitPriceDiscountHigh(self, UnitPriceDiscountHigh):
        self._UnitPriceDiscountHigh = UnitPriceDiscountHigh


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._UnitPrice = params.get("UnitPrice")
        self._ChargeUnit = params.get("ChargeUnit")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._OriginalPriceHigh = params.get("OriginalPriceHigh")
        self._DiscountPriceHigh = params.get("DiscountPriceHigh")
        self._UnitPriceHigh = params.get("UnitPriceHigh")
        self._UnitPriceDiscountHigh = params.get("UnitPriceDiscountHigh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskRequest(AbstractModel):
    """ResizeDisk request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: ID of the cloud disk, which can be queried via the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1).
        :type DiskId: str
        :param _DiskSize: Cloud disk size after scale out (in GB). This must be larger than the current size of the cloud disk. For the value range of the cloud disk sizes, see cloud disk [Product Types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        """
        self._DiskId = None
        self._DiskSize = None

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskResponse(AbstractModel):
    """ResizeDisk response structure.

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


class SharePermission(AbstractModel):
    """Snapshot sharing information set

    """

    def __init__(self):
        r"""
        :param _CreatedTime: Snapshot sharing time
        :type CreatedTime: str
        :param _AccountId: ID of the shared account
        :type AccountId: str
        """
        self._CreatedTime = None
        self._AccountId = None

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId


    def _deserialize(self, params):
        self._CreatedTime = params.get("CreatedTime")
        self._AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """The details of a snapshot

    """

    def __init__(self):
        r"""
        :param _Placement: Location of the snapshot.
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param _CopyFromRemote: Whether the snapshot is replicated across regions. Value range: <br><li>true: Indicates that the snapshot is replicated across regions. <br><li>false: Indicates that the snapshot belongs to the local region.
        :type CopyFromRemote: bool
        :param _SnapshotState: Snapshot status. Valid values: <br><li>NORMAL: normal <br><li>CREATING: creating<br><li>ROLLBACKING: rolling back<br><li>COPYING_FROM_REMOTE: cross-region replicating<li>CHECKING_COPIED: verifying the cross-region replicated data<br><li>TORECYCLE: to be repossessed.
        :type SnapshotState: str
        :param _IsPermanent: Whether it is a permanent snapshot. Value range: <br><li>true: Permanent snapshot <br><li>false: Non-permanent snapshot.
        :type IsPermanent: bool
        :param _SnapshotName: Snapshot name, the user-defined snapshot alias. Call [ModifySnapshotAttribute](https://intl.cloud.tencent.com/document/product/362/15650?from_cn_redirect=1) to modify this field.
        :type SnapshotName: str
        :param _DeadlineTime: The expiration time of the snapshot. If the snapshot is permanently retained, this field is blank.
        :type DeadlineTime: str
        :param _Percent: The progress percentage for snapshot creation. This field is always 100 after the snapshot is created successfully.
        :type Percent: int
        :param _Images: List of images associated with snapshot.
        :type Images: list of Image
        :param _ShareReference: Number of snapshots currently shared
        :type ShareReference: int
        :param _SnapshotType: Snapshot type. This value can currently be either PRIVATE_SNAPSHOT or SHARED_SNAPSHOT.
        :type SnapshotType: str
        :param _DiskSize: Size of the cloud disk used to create this snapshot (in GB).
        :type DiskSize: int
        :param _DiskId: ID of the cloud disk used to create this snapshot.
        :type DiskId: str
        :param _CopyingToRegions: The destination region to which the snapshot is being replicated. Default value is [ ].
        :type CopyingToRegions: list of str
        :param _Encrypt: Whether the snapshot is created from an encrypted disk. Value range: <br><li>true: Yes <br><li>false: No.
        :type Encrypt: bool
        :param _CreateTime: Creation time of the snapshot.
        :type CreateTime: str
        :param _ImageCount: Number of images associated with snapshot.
        :type ImageCount: int
        :param _DiskUsage: The type of the cloud disk used to create the snapshot. Value range: <br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk.
        :type DiskUsage: str
        :param _SnapshotId: Snapshot ID.
        :type SnapshotId: str
        :param _TimeStartShare: The time when the snapshot sharing starts
        :type TimeStartShare: str
        :param _Tags: List of tags associated with the snapshot.
        :type Tags: list of Tag
        """
        self._Placement = None
        self._CopyFromRemote = None
        self._SnapshotState = None
        self._IsPermanent = None
        self._SnapshotName = None
        self._DeadlineTime = None
        self._Percent = None
        self._Images = None
        self._ShareReference = None
        self._SnapshotType = None
        self._DiskSize = None
        self._DiskId = None
        self._CopyingToRegions = None
        self._Encrypt = None
        self._CreateTime = None
        self._ImageCount = None
        self._DiskUsage = None
        self._SnapshotId = None
        self._TimeStartShare = None
        self._Tags = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CopyFromRemote(self):
        return self._CopyFromRemote

    @CopyFromRemote.setter
    def CopyFromRemote(self, CopyFromRemote):
        self._CopyFromRemote = CopyFromRemote

    @property
    def SnapshotState(self):
        return self._SnapshotState

    @SnapshotState.setter
    def SnapshotState(self, SnapshotState):
        self._SnapshotState = SnapshotState

    @property
    def IsPermanent(self):
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Images(self):
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def ShareReference(self):
        return self._ShareReference

    @ShareReference.setter
    def ShareReference(self, ShareReference):
        self._ShareReference = ShareReference

    @property
    def SnapshotType(self):
        return self._SnapshotType

    @SnapshotType.setter
    def SnapshotType(self, SnapshotType):
        self._SnapshotType = SnapshotType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def CopyingToRegions(self):
        return self._CopyingToRegions

    @CopyingToRegions.setter
    def CopyingToRegions(self, CopyingToRegions):
        self._CopyingToRegions = CopyingToRegions

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ImageCount(self):
        return self._ImageCount

    @ImageCount.setter
    def ImageCount(self, ImageCount):
        self._ImageCount = ImageCount

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def TimeStartShare(self):
        return self._TimeStartShare

    @TimeStartShare.setter
    def TimeStartShare(self, TimeStartShare):
        self._TimeStartShare = TimeStartShare

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CopyFromRemote = params.get("CopyFromRemote")
        self._SnapshotState = params.get("SnapshotState")
        self._IsPermanent = params.get("IsPermanent")
        self._SnapshotName = params.get("SnapshotName")
        self._DeadlineTime = params.get("DeadlineTime")
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
        self._Encrypt = params.get("Encrypt")
        self._CreateTime = params.get("CreateTime")
        self._ImageCount = params.get("ImageCount")
        self._DiskUsage = params.get("DiskUsage")
        self._SnapshotId = params.get("SnapshotId")
        self._TimeStartShare = params.get("TimeStartShare")
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
        


class SnapshotCopyResult(AbstractModel):
    """Result of the cross-region replication task

    """

    def __init__(self):
        r"""
        :param _SnapshotId: ID of the snapshot replica
        :type SnapshotId: str
        :param _Message: Error message. It’s null if the request succeeds.
        :type Message: str
        :param _Code: Error code. It’s `Success` if the request succeeds.
        :type Code: str
        :param _DestinationRegion: Destination region of the replication task
        :type DestinationRegion: str
        """
        self._SnapshotId = None
        self._Message = None
        self._Code = None
        self._DestinationRegion = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def DestinationRegion(self):
        return self._DestinationRegion

    @DestinationRegion.setter
    def DestinationRegion(self, DestinationRegion):
        self._DestinationRegion = DestinationRegion


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        self._DestinationRegion = params.get("DestinationRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotOperationLog(AbstractModel):
    """Snapshot operation log (disused).

    """

    def __init__(self):
        r"""
        :param _OperationState: Status of operation. Value range:
SUCCESS: Operation successful 
FAILED: Operation failed 
PROCESSING: Operation in process
        :type OperationState: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _Operator: UIN of operator.
Note: This field may return null, indicating that no valid value was found.
        :type Operator: str
        :param _SnapshotId: ID of snapshot being operated.
        :type SnapshotId: str
        :param _Operation: Operation type. Value range:
SNAP_OPERATION_DELETE: Delete snapshot
SNAP_OPERATION_ROLLBACK: Roll back snapshot
SNAP_OPERATION_MODIFY: Modify snapshot attributes
SNAP_OPERATION_CREATE: Create snapshot
SNAP_OPERATION_COPY: Cross-region replication of snapshot
ASP_OPERATION_CREATE_SNAP: Create snapshot with scheduled snapshot policy
ASP_OPERATION_DELETE_SNAP: Delete snapshot from scheduled snapshot policy
        :type Operation: str
        :param _EndTime: End time
        :type EndTime: str
        """
        self._OperationState = None
        self._StartTime = None
        self._Operator = None
        self._SnapshotId = None
        self._Operation = None
        self._EndTime = None

    @property
    def OperationState(self):
        return self._OperationState

    @OperationState.setter
    def OperationState(self, OperationState):
        self._OperationState = OperationState

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._OperationState = params.get("OperationState")
        self._StartTime = params.get("StartTime")
        self._Operator = params.get("Operator")
        self._SnapshotId = params.get("SnapshotId")
        self._Operation = params.get("Operation")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag.

    """

    def __init__(self):
        r"""
        :param _Key: Tag key.
        :type Key: str
        :param _Value: Tag value.
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
        


class TerminateDisksRequest(AbstractModel):
    """TerminateDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs required to be returned.
        :type DiskIds: list of str
        :param _DeleteSnapshot: Delete the associated non-permanently reserved snapshots upon deletion of the source cloud disk. `0`: No (default). `1`: Yes. To check whether a snapshot is permanently reserved, refer to the `IsPermanent` field returned by the `DescribeSnapshots` API. 
        :type DeleteSnapshot: int
        """
        self._DiskIds = None
        self._DeleteSnapshot = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DeleteSnapshot(self):
        return self._DeleteSnapshot

    @DeleteSnapshot.setter
    def DeleteSnapshot(self, DeleteSnapshot):
        self._DeleteSnapshot = DeleteSnapshot


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._DeleteSnapshot = params.get("DeleteSnapshot")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDisksResponse(AbstractModel):
    """TerminateDisks response structure.

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


class UnbindAutoSnapshotPolicyRequest(AbstractModel):
    """UnbindAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk IDs scheduled snapshot policy to be unbound from.
        :type DiskIds: list of str
        :param _AutoSnapshotPolicyId: ID of scheduled snapshot policy to be unbound.
        :type AutoSnapshotPolicyId: str
        """
        self._DiskIds = None
        self._AutoSnapshotPolicyId = None

    @property
    def DiskIds(self):
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def AutoSnapshotPolicyId(self):
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
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