# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
    r"""Retention policy for scheduled snapshots. All four parameters are required.

    """

    def __init__(self):
        r"""
        :param _Days: Retains the latest snapshot of each day within the specified number of Days. value range: [0, 100].
        :type Days: int
        :param _Weeks: Reserve the latest snapshot of each week for Weeks. value range: [0, 100].
        :type Weeks: int
        :param _Months: Reserve the latest snapshot of each month within Months Months. value range: [0, 100].
        :type Months: int
        :param _Years: Reserve the latest snapshot of each year within Years Years. value range: [0, 100].
        :type Years: int
        """
        self._Days = None
        self._Weeks = None
        self._Months = None
        self._Years = None

    @property
    def Days(self):
        r"""Retains the latest snapshot of each day within the specified number of Days. value range: [0, 100].
        :rtype: int
        """
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Weeks(self):
        r"""Reserve the latest snapshot of each week for Weeks. value range: [0, 100].
        :rtype: int
        """
        return self._Weeks

    @Weeks.setter
    def Weeks(self, Weeks):
        self._Weeks = Weeks

    @property
    def Months(self):
        r"""Reserve the latest snapshot of each month within Months Months. value range: [0, 100].
        :rtype: int
        """
        return self._Months

    @Months.setter
    def Months(self, Months):
        self._Months = Months

    @property
    def Years(self):
        r"""Reserve the latest snapshot of each year within Years Years. value range: [0, 100].
        :rtype: int
        """
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
        


class ApplyDisk(AbstractModel):
    r"""This parameter is used for the snapshot group rollback API input, representing the cloud disks and snapshot list to be rolled back.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Specifies the snapshot ID associated with the snapshot group.
        :type SnapshotId: str
        :param _DiskId: Specifies the original cloud disk ID of the snapshot associated with the snapshot group.
        :type DiskId: str
        """
        self._SnapshotId = None
        self._DiskId = None

    @property
    def SnapshotId(self):
        r"""Specifies the snapshot ID associated with the snapshot group.
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskId(self):
        r"""Specifies the original cloud disk ID of the snapshot associated with the snapshot group.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyDiskBackupRequest(AbstractModel):
    r"""ApplyDiskBackup request structure.

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: Cloud disk backup point ID. can be queried through the [DescribeDiskBackups](https://www.tencentcloud.com/document/product/362/80278?from_cn_redirect=1) api.
        :type DiskBackupId: str
        :param _DiskId: Original cloud disk ID of the backup point. can be queried through the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api.
        :type DiskId: str
        :param _AutoStopInstance: Specifies whether to enable automatic shutdown before rolling back the CBS backup point. defaults to FALSE, which means no automatic shutdown.
        :type AutoStopInstance: bool
        :param _AutoStartInstance: Whether to automatically start after rolling back the cloud disk backup point, default to FALSE, means do not auto boot. the AutoStartInstance parameter can only be set to true when AutoStopInstance is true.
        :type AutoStartInstance: bool
        """
        self._DiskBackupId = None
        self._DiskId = None
        self._AutoStopInstance = None
        self._AutoStartInstance = None

    @property
    def DiskBackupId(self):
        r"""Cloud disk backup point ID. can be queried through the [DescribeDiskBackups](https://www.tencentcloud.com/document/product/362/80278?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def DiskId(self):
        r"""Original cloud disk ID of the backup point. can be queried through the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def AutoStopInstance(self):
        r"""Specifies whether to enable automatic shutdown before rolling back the CBS backup point. defaults to FALSE, which means no automatic shutdown.
        :rtype: bool
        """
        return self._AutoStopInstance

    @AutoStopInstance.setter
    def AutoStopInstance(self, AutoStopInstance):
        self._AutoStopInstance = AutoStopInstance

    @property
    def AutoStartInstance(self):
        r"""Whether to automatically start after rolling back the cloud disk backup point, default to FALSE, means do not auto boot. the AutoStartInstance parameter can only be set to true when AutoStopInstance is true.
        :rtype: bool
        """
        return self._AutoStartInstance

    @AutoStartInstance.setter
    def AutoStartInstance(self, AutoStartInstance):
        self._AutoStartInstance = AutoStartInstance


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
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
        


class ApplyDiskBackupResponse(AbstractModel):
    r"""ApplyDiskBackup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ApplySnapshotGroupRequest(AbstractModel):
    r"""ApplySnapshotGroup request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotGroupId: Specifies the snapshot group ID rolled back.
        :type SnapshotGroupId: str
        :param _ApplyDisks: Specifies the snapshot ID associated with the rollback snapshot group and the original cloud disk ID list of the corresponding snapshot.
        :type ApplyDisks: list of ApplyDisk
        :param _AutoStopInstance: Specifies whether to perform automatic shutdown before rollback.
        :type AutoStopInstance: bool
        :param _AutoStartInstance: Specifies whether to automatically start after completion.
        :type AutoStartInstance: bool
        """
        self._SnapshotGroupId = None
        self._ApplyDisks = None
        self._AutoStopInstance = None
        self._AutoStartInstance = None

    @property
    def SnapshotGroupId(self):
        r"""Specifies the snapshot group ID rolled back.
        :rtype: str
        """
        return self._SnapshotGroupId

    @SnapshotGroupId.setter
    def SnapshotGroupId(self, SnapshotGroupId):
        self._SnapshotGroupId = SnapshotGroupId

    @property
    def ApplyDisks(self):
        r"""Specifies the snapshot ID associated with the rollback snapshot group and the original cloud disk ID list of the corresponding snapshot.
        :rtype: list of ApplyDisk
        """
        return self._ApplyDisks

    @ApplyDisks.setter
    def ApplyDisks(self, ApplyDisks):
        self._ApplyDisks = ApplyDisks

    @property
    def AutoStopInstance(self):
        r"""Specifies whether to perform automatic shutdown before rollback.
        :rtype: bool
        """
        return self._AutoStopInstance

    @AutoStopInstance.setter
    def AutoStopInstance(self, AutoStopInstance):
        self._AutoStopInstance = AutoStopInstance

    @property
    def AutoStartInstance(self):
        r"""Specifies whether to automatically start after completion.
        :rtype: bool
        """
        return self._AutoStartInstance

    @AutoStartInstance.setter
    def AutoStartInstance(self, AutoStartInstance):
        self._AutoStartInstance = AutoStartInstance


    def _deserialize(self, params):
        self._SnapshotGroupId = params.get("SnapshotGroupId")
        if params.get("ApplyDisks") is not None:
            self._ApplyDisks = []
            for item in params.get("ApplyDisks"):
                obj = ApplyDisk()
                obj._deserialize(item)
                self._ApplyDisks.append(obj)
        self._AutoStopInstance = params.get("AutoStopInstance")
        self._AutoStartInstance = params.get("AutoStartInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplySnapshotGroupResponse(AbstractModel):
    r"""ApplySnapshotGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ApplySnapshotRequest(AbstractModel):
    r"""ApplySnapshot request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot ID, which can be queried via [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :type SnapshotId: str
        :param _DiskId: ID of the original cloud disk corresponding to the snapshot, which can be queried via the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1).
        :type DiskId: str
        :param _AutoStopInstance: Specifies whether to perform automatic shutdown before rolling back. only supports rolling back snapshots to mounted cbs.
Specifies whether AutoStartInstance can be set to true when this parameter is true.
        :type AutoStopInstance: bool
        :param _AutoStartInstance: Specifies whether to automatically start after completion. only supports rolling back snapshots to mounted cbs. this parameter requires simultaneous parameter passing of AutoStopInstance.
        :type AutoStartInstance: bool
        """
        self._SnapshotId = None
        self._DiskId = None
        self._AutoStopInstance = None
        self._AutoStartInstance = None

    @property
    def SnapshotId(self):
        r"""Snapshot ID, which can be queried via [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskId(self):
        r"""ID of the original cloud disk corresponding to the snapshot, which can be queried via the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1).
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def AutoStopInstance(self):
        r"""Specifies whether to perform automatic shutdown before rolling back. only supports rolling back snapshots to mounted cbs.
Specifies whether AutoStartInstance can be set to true when this parameter is true.
        :rtype: bool
        """
        return self._AutoStopInstance

    @AutoStopInstance.setter
    def AutoStopInstance(self, AutoStopInstance):
        self._AutoStopInstance = AutoStopInstance

    @property
    def AutoStartInstance(self):
        r"""Specifies whether to automatically start after completion. only supports rolling back snapshots to mounted cbs. this parameter requires simultaneous parameter passing of AutoStopInstance.
        :rtype: bool
        """
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
    r"""ApplySnapshot response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AttachDetail(AbstractModel):
    r"""This describes the number of mounted and mountable data disks of an instance.

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
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AttachedDiskCount(self):
        r"""The number of instances mounted to data disk.
        :rtype: int
        """
        return self._AttachedDiskCount

    @AttachedDiskCount.setter
    def AttachedDiskCount(self, AttachedDiskCount):
        self._AttachedDiskCount = AttachedDiskCount

    @property
    def MaxAttachCount(self):
        r"""The maximum number of instances that can be mounted to data disk.
        :rtype: int
        """
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
    r"""AttachDisks request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the CVM instance on which the cloud disk will be mounted. It can be queried via the API [DescribeInstances](https://intl.cloud.tencent.com/document/product/213/15728?from_cn_redirect=1).
        :type InstanceId: str
        :param _DiskIds: ID of the elastic cloud disk to be mounted, which can be queried through the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1). A maximum of 10 elastic cloud disks can be mounted in a single request.
        :type DiskIds: list of str
        :param _DeleteWithInstance: Optional parameter. If this is not passed only the mount operation is executed. If `True` is passed, the cloud disk will be configured to be terminated when the server it is mounted to is terminated. This is only valid for pay-as-you-go cloud disks.
        :type DeleteWithInstance: bool
        :param _AttachMode: Optional parameter, used to control the mount mode used in cloud disk mounting, currently only applicable to blackstone bare metal model. valid values: <br><li>PF</li><br><li>VF</li>.
        :type AttachMode: str
        """
        self._InstanceId = None
        self._DiskIds = None
        self._DeleteWithInstance = None
        self._AttachMode = None

    @property
    def InstanceId(self):
        r"""ID of the CVM instance on which the cloud disk will be mounted. It can be queried via the API [DescribeInstances](https://intl.cloud.tencent.com/document/product/213/15728?from_cn_redirect=1).
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskIds(self):
        r"""ID of the elastic cloud disk to be mounted, which can be queried through the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1). A maximum of 10 elastic cloud disks can be mounted in a single request.
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DeleteWithInstance(self):
        r"""Optional parameter. If this is not passed only the mount operation is executed. If `True` is passed, the cloud disk will be configured to be terminated when the server it is mounted to is terminated. This is only valid for pay-as-you-go cloud disks.
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def AttachMode(self):
        r"""Optional parameter, used to control the mount mode used in cloud disk mounting, currently only applicable to blackstone bare metal model. valid values: <br><li>PF</li><br><li>VF</li>.
        :rtype: str
        """
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
    r"""AttachDisks response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AutoMountConfiguration(AbstractModel):
    r"""Describes how a newly purchased cloud disk is initialized and attached to a CVM instance.

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
        r"""ID of the instance to which the cloud disk is attached.
        :rtype: list of str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MountPoint(self):
        r"""Mount point in the instance.
        :rtype: list of str
        """
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def FileSystemType(self):
        r"""File system type. Valid values: `ext4`, `xfs`.
        :rtype: str
        """
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
    r"""This describes the detailed information of the scheduled snapshot policy.

    """

    def __init__(self):
        r"""
        :param _DiskIdSet: It lists IDs of cloud disks that have been bound to the current regular snapshot policy.

In the scenario of DescribeDiskAssociatedAutoSnapshotPolicy, this field returns empty.
        :type DiskIdSet: list of str
        :param _IsActivated: Whether scheduled snapshot policy is activated.
        :type IsActivated: bool
        :param _AutoSnapshotPolicyState: Status of regular snapshot policy. valid values:.
<ul>
<Li>NORMAL: specifies the scaling group is in normal state.</li>.
<Li>ISOLATED: specifies the instance is isolated.</li>.
</ul>
        :type AutoSnapshotPolicyState: str
        :param _IsCopyToRemote: Whether it is a cross-account snapshot replication. valid values: 1 (yes), 0 (no).
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
        :param _InstanceIdSet: Lists instance ids that are bound to the current periodic snapshot policy.
        :type InstanceIdSet: list of str
        :param _RetentionMonths: Specifies the number of months snapshot can be retained.
        :type RetentionMonths: int
        :param _RetentionAmount: Specifies the maximum retention number of snapshots created by scheduled snapshot.
        :type RetentionAmount: int
        :param _AdvancedRetentionPolicy: Retention policy for scheduled snapshots.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AdvancedRetentionPolicy: :class:`tencentcloud.cbs.v20170312.models.AdvancedRetentionPolicy`
        :param _CopyFromAccountUin: Source account ID of the copied snapshot policy
Note: This field may return null, indicating that no valid values can be obtained.
        :type CopyFromAccountUin: str
        :param _Tags: Tag.
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
        r"""It lists IDs of cloud disks that have been bound to the current regular snapshot policy.

In the scenario of DescribeDiskAssociatedAutoSnapshotPolicy, this field returns empty.
        :rtype: list of str
        """
        return self._DiskIdSet

    @DiskIdSet.setter
    def DiskIdSet(self, DiskIdSet):
        self._DiskIdSet = DiskIdSet

    @property
    def IsActivated(self):
        r"""Whether scheduled snapshot policy is activated.
        :rtype: bool
        """
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def AutoSnapshotPolicyState(self):
        r"""Status of regular snapshot policy. valid values:.
<ul>
<Li>NORMAL: specifies the scaling group is in normal state.</li>.
<Li>ISOLATED: specifies the instance is isolated.</li>.
</ul>
        :rtype: str
        """
        return self._AutoSnapshotPolicyState

    @AutoSnapshotPolicyState.setter
    def AutoSnapshotPolicyState(self, AutoSnapshotPolicyState):
        self._AutoSnapshotPolicyState = AutoSnapshotPolicyState

    @property
    def IsCopyToRemote(self):
        r"""Whether it is a cross-account snapshot replication. valid values: 1 (yes), 0 (no).
        :rtype: int
        """
        return self._IsCopyToRemote

    @IsCopyToRemote.setter
    def IsCopyToRemote(self, IsCopyToRemote):
        self._IsCopyToRemote = IsCopyToRemote

    @property
    def IsPermanent(self):
        r"""Whether the snapshot created by this scheduled snapshot policy is retained permanently.
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def NextTriggerTime(self):
        r"""The time the scheduled snapshot will be triggered again.
        :rtype: str
        """
        return self._NextTriggerTime

    @NextTriggerTime.setter
    def NextTriggerTime(self, NextTriggerTime):
        self._NextTriggerTime = NextTriggerTime

    @property
    def AutoSnapshotPolicyName(self):
        r"""Scheduled snapshot policy name.
        :rtype: str
        """
        return self._AutoSnapshotPolicyName

    @AutoSnapshotPolicyName.setter
    def AutoSnapshotPolicyName(self, AutoSnapshotPolicyName):
        self._AutoSnapshotPolicyName = AutoSnapshotPolicyName

    @property
    def AutoSnapshotPolicyId(self):
        r"""Scheduled snapshot policy ID.
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def Policy(self):
        r"""The policy for executing the scheduled snapshot.
        :rtype: list of Policy
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def CreateTime(self):
        r"""The time the scheduled snapshot policy was created.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RetentionDays(self):
        r"""Number of days the snapshot created by this scheduled snapshot policy is retained.
        :rtype: int
        """
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays

    @property
    def CopyToAccountUin(self):
        r"""ID of the replication target account
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CopyToAccountUin

    @CopyToAccountUin.setter
    def CopyToAccountUin(self, CopyToAccountUin):
        self._CopyToAccountUin = CopyToAccountUin

    @property
    def InstanceIdSet(self):
        r"""Lists instance ids that are bound to the current periodic snapshot policy.
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RetentionMonths(self):
        r"""Specifies the number of months snapshot can be retained.
        :rtype: int
        """
        return self._RetentionMonths

    @RetentionMonths.setter
    def RetentionMonths(self, RetentionMonths):
        self._RetentionMonths = RetentionMonths

    @property
    def RetentionAmount(self):
        r"""Specifies the maximum retention number of snapshots created by scheduled snapshot.
        :rtype: int
        """
        return self._RetentionAmount

    @RetentionAmount.setter
    def RetentionAmount(self, RetentionAmount):
        self._RetentionAmount = RetentionAmount

    @property
    def AdvancedRetentionPolicy(self):
        r"""Retention policy for scheduled snapshots.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.AdvancedRetentionPolicy`
        """
        return self._AdvancedRetentionPolicy

    @AdvancedRetentionPolicy.setter
    def AdvancedRetentionPolicy(self, AdvancedRetentionPolicy):
        self._AdvancedRetentionPolicy = AdvancedRetentionPolicy

    @property
    def CopyFromAccountUin(self):
        r"""Source account ID of the copied snapshot policy
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CopyFromAccountUin

    @CopyFromAccountUin.setter
    def CopyFromAccountUin(self, CopyFromAccountUin):
        self._CopyFromAccountUin = CopyFromAccountUin

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of Tag
        """
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
    r"""BindAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Specifies the ID of the regular snapshot policy to bind. query via the DescribeAutoSnapshotPolicies api (https://www.tencentcloud.com/document/api/362/33556?from_cn_redirect=1).
        :type AutoSnapshotPolicyId: str
        :param _DiskIds: List of cloud disk IDs to be bound. Maximum of 80 cloud disks can be bound per request.
        :type DiskIds: list of str
        """
        self._AutoSnapshotPolicyId = None
        self._DiskIds = None

    @property
    def AutoSnapshotPolicyId(self):
        r"""Specifies the ID of the regular snapshot policy to bind. query via the DescribeAutoSnapshotPolicies api (https://www.tencentcloud.com/document/api/362/33556?from_cn_redirect=1).
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def DiskIds(self):
        r"""List of cloud disk IDs to be bound. Maximum of 80 cloud disks can be bound per request.
        :rtype: list of str
        """
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
    r"""BindAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Cdc(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _CageId: 
        :type CageId: str
        :param _CdcState: Exclusive cluster status. value ranges from:<br><li>NORMAL: NORMAL;</li><br><li>CLOSED: CLOSED. at this time, the exclusive cluster will be unavailable to create new cloud disks;</li><br><li>FAULT: abnormal exclusive cluster status. at this point, the exclusive cluster will be inoperable, and the tencent cloud ops team will promptly fix the cluster;</li><br><li>ISOLATED: the exclusive cluster is ISOLATED due to not renewed timely. at this moment, the exclusive cluster will be unavailable to create new cloud disks, and the corresponding cloud disks will also be inoperable.</li>.
        :type CdcState: str
        :param _Zone: Specifies the AZ ID of the exclusive cluster.
        :type Zone: str
        :param _CdcName: 
        :type CdcName: str
        :param _CdcResource: Specifies the capacity size of the dedicated cluster.
        :type CdcResource: :class:`tencentcloud.cbs.v20170312.models.CdcSize`
        :param _CdcId: 
        :type CdcId: str
        :param _DiskType: Exclusive cluster type. valid values: <br><li>CLOUD_BASIC: BASIC CLOUD disk cluster</li><br><li>CLOUD_PREMIUM: high-performance CLOUD block storage cluster</li><br><li>CLOUD_SSD: SSD CLOUD disk cluster.</li>.
        :type DiskType: str
        :param _ExpiredTime: Expiry time of the dedicated cloud disk cluster.
        :type ExpiredTime: str
        :param _CreatedTime: Creation time of the resource pool.
        :type CreatedTime: str
        :param _DiskNumber: Number of cloud disks created in the current cluster.
        :type DiskNumber: int
        """
        self._CageId = None
        self._CdcState = None
        self._Zone = None
        self._CdcName = None
        self._CdcResource = None
        self._CdcId = None
        self._DiskType = None
        self._ExpiredTime = None
        self._CreatedTime = None
        self._DiskNumber = None

    @property
    def CageId(self):
        r"""
        :rtype: str
        """
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def CdcState(self):
        r"""Exclusive cluster status. value ranges from:<br><li>NORMAL: NORMAL;</li><br><li>CLOSED: CLOSED. at this time, the exclusive cluster will be unavailable to create new cloud disks;</li><br><li>FAULT: abnormal exclusive cluster status. at this point, the exclusive cluster will be inoperable, and the tencent cloud ops team will promptly fix the cluster;</li><br><li>ISOLATED: the exclusive cluster is ISOLATED due to not renewed timely. at this moment, the exclusive cluster will be unavailable to create new cloud disks, and the corresponding cloud disks will also be inoperable.</li>.
        :rtype: str
        """
        return self._CdcState

    @CdcState.setter
    def CdcState(self, CdcState):
        self._CdcState = CdcState

    @property
    def Zone(self):
        r"""Specifies the AZ ID of the exclusive cluster.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CdcName(self):
        r"""
        :rtype: str
        """
        return self._CdcName

    @CdcName.setter
    def CdcName(self, CdcName):
        self._CdcName = CdcName

    @property
    def CdcResource(self):
        r"""Specifies the capacity size of the dedicated cluster.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.CdcSize`
        """
        return self._CdcResource

    @CdcResource.setter
    def CdcResource(self, CdcResource):
        self._CdcResource = CdcResource

    @property
    def CdcId(self):
        r"""
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def DiskType(self):
        r"""Exclusive cluster type. valid values: <br><li>CLOUD_BASIC: BASIC CLOUD disk cluster</li><br><li>CLOUD_PREMIUM: high-performance CLOUD block storage cluster</li><br><li>CLOUD_SSD: SSD CLOUD disk cluster.</li>.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def ExpiredTime(self):
        r"""Expiry time of the dedicated cloud disk cluster.
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def CreatedTime(self):
        r"""Creation time of the resource pool.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DiskNumber(self):
        r"""Number of cloud disks created in the current cluster.
        :rtype: int
        """
        return self._DiskNumber

    @DiskNumber.setter
    def DiskNumber(self, DiskNumber):
        self._DiskNumber = DiskNumber


    def _deserialize(self, params):
        self._CageId = params.get("CageId")
        self._CdcState = params.get("CdcState")
        self._Zone = params.get("Zone")
        self._CdcName = params.get("CdcName")
        if params.get("CdcResource") is not None:
            self._CdcResource = CdcSize()
            self._CdcResource._deserialize(params.get("CdcResource"))
        self._CdcId = params.get("CdcId")
        self._DiskType = params.get("DiskType")
        self._ExpiredTime = params.get("ExpiredTime")
        self._CreatedTime = params.get("CreatedTime")
        self._DiskNumber = params.get("DiskNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdcSize(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _DiskTotal: 
        :type DiskTotal: int
        :param _DiskAvailable: Specifies the available capacity size of the dedicated cluster in GiB.
        :type DiskAvailable: int
        """
        self._DiskTotal = None
        self._DiskAvailable = None

    @property
    def DiskTotal(self):
        r"""
        :rtype: int
        """
        return self._DiskTotal

    @DiskTotal.setter
    def DiskTotal(self, DiskTotal):
        self._DiskTotal = DiskTotal

    @property
    def DiskAvailable(self):
        r"""Specifies the available capacity size of the dedicated cluster in GiB.
        :rtype: int
        """
        return self._DiskAvailable

    @DiskAvailable.setter
    def DiskAvailable(self, DiskAvailable):
        self._DiskAvailable = DiskAvailable


    def _deserialize(self, params):
        self._DiskTotal = params.get("DiskTotal")
        self._DiskAvailable = params.get("DiskAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopySnapshotCrossRegionsRequest(AbstractModel):
    r"""CopySnapshotCrossRegions request structure.

    """

    def __init__(self):
        r"""
        :param _DestinationRegions: Destination regions of the replication task. You can query the value of regions by calling [DescribeRegions](https://www.tencentcloud.com/document/product/1271/71925) API. Note that you can only specify regions that support snapshots.
        :type DestinationRegions: list of str
        :param _SnapshotId: Snapshot ID, which can be queried via the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API.
        :type SnapshotId: str
        :param _SnapshotName: Name of the snapshot replica. If it is not specified, it defaults to Copied [source snapshot ID from [region name]
        :type SnapshotName: str
        """
        self._DestinationRegions = None
        self._SnapshotId = None
        self._SnapshotName = None

    @property
    def DestinationRegions(self):
        r"""Destination regions of the replication task. You can query the value of regions by calling [DescribeRegions](https://www.tencentcloud.com/document/product/1271/71925) API. Note that you can only specify regions that support snapshots.
        :rtype: list of str
        """
        return self._DestinationRegions

    @DestinationRegions.setter
    def DestinationRegions(self, DestinationRegions):
        self._DestinationRegions = DestinationRegions

    @property
    def SnapshotId(self):
        r"""Snapshot ID, which can be queried via the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def SnapshotName(self):
        r"""Name of the snapshot replica. If it is not specified, it defaults to Copied [source snapshot ID from [region name]
        :rtype: str
        """
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
    r"""CopySnapshotCrossRegions response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotCopyResultSet: Result of the cross-region replication task. The ID of the new snapshot replica is returned if the request succeeds. Otherwise `Error` is returned.
        :type SnapshotCopyResultSet: list of SnapshotCopyResult
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotCopyResultSet = None
        self._RequestId = None

    @property
    def SnapshotCopyResultSet(self):
        r"""Result of the cross-region replication task. The ID of the new snapshot replica is returned if the request succeeds. Otherwise `Error` is returned.
        :rtype: list of SnapshotCopyResult
        """
        return self._SnapshotCopyResultSet

    @SnapshotCopyResultSet.setter
    def SnapshotCopyResultSet(self, SnapshotCopyResultSet):
        self._SnapshotCopyResultSet = SnapshotCopyResultSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""CreateAutoSnapshotPolicy request structure.

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
        r"""The policy for executing the scheduled snapshot.
        :rtype: list of Policy
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def AutoSnapshotPolicyName(self):
        r"""The name of the scheduled snapshot policy to be created. If it is left empty, the default is 'Not named'. The maximum length cannot exceed 60 bytes.
        :rtype: str
        """
        return self._AutoSnapshotPolicyName

    @AutoSnapshotPolicyName.setter
    def AutoSnapshotPolicyName(self, AutoSnapshotPolicyName):
        self._AutoSnapshotPolicyName = AutoSnapshotPolicyName

    @property
    def IsActivated(self):
        r"""Whether or not the scheduled snapshot policy is activated. FALSE: Not activated. TRUE: Activated. The default value is TRUE.
        :rtype: bool
        """
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def IsPermanent(self):
        r"""Whether the snapshot created by this scheduled snapshot policy is retained permanently. FALSE: Not retained permanently. TRUE: Retained permanently. The default value is FALSE.
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def RetentionDays(self):
        r"""The number of days that a snapshot created by this scheduled snapshot policy is retained. The default value is 7. If this parameter is specified, the IsPermanent input parameter can not be TRUE, otherwise a conflict will occur.
        :rtype: int
        """
        return self._RetentionDays

    @RetentionDays.setter
    def RetentionDays(self, RetentionDays):
        self._RetentionDays = RetentionDays

    @property
    def DryRun(self):
        r"""Whether to create an execution policy for the scheduled snapshot. TRUE: Only the time of the initial backup needs to be obtained, and no scheduled snapshot policy is actually created. FALSE: Create. The default value is FALSE.
        :rtype: bool
        """
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
    r"""CreateAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: The ID of the newly created scheduled snapshot policy.
        :type AutoSnapshotPolicyId: str
        :param _NextTriggerTime: The time that initial backup will start.
        :type NextTriggerTime: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoSnapshotPolicyId = None
        self._NextTriggerTime = None
        self._RequestId = None

    @property
    def AutoSnapshotPolicyId(self):
        r"""The ID of the newly created scheduled snapshot policy.
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def NextTriggerTime(self):
        r"""The time that initial backup will start.
        :rtype: str
        """
        return self._NextTriggerTime

    @NextTriggerTime.setter
    def NextTriggerTime(self, NextTriggerTime):
        self._NextTriggerTime = NextTriggerTime

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._NextTriggerTime = params.get("NextTriggerTime")
        self._RequestId = params.get("RequestId")


class CreateDiskBackupRequest(AbstractModel):
    r"""CreateDiskBackup request structure.

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
        r"""Name of the cloud disk for which to create a backup point.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupName(self):
        r"""Name of the cloud disk backup point, which can contain up to 100 characters.
        :rtype: str
        """
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
    r"""CreateDiskBackup response structure.

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: ID of the cloud disk backup point.
        :type DiskBackupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskBackupId = None
        self._RequestId = None

    @property
    def DiskBackupId(self):
        r"""ID of the cloud disk backup point.
        :rtype: str
        """
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiskBackupId = params.get("DiskBackupId")
        self._RequestId = params.get("RequestId")


class CreateDisksRequest(AbstractModel):
    r"""CreateDisks request structure.

    """

    def __init__(self):
        r"""
        :param _Placement: Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone and project. If no project is specified, the default project will be used.
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param _DiskChargeType: Cloud disk billing mode. POSTPAID_BY_HOUR: Pay-as-you-go by hour<br><li>CDCPAID: Billed together with the bound dedicated cluster<br>For more information on the pricing in each mode, see [Pricing Overview](https://intl.cloud.tencent.com/document/product/362/2413?from_cn_redirect=1).
        :type DiskChargeType: str
        :param _DiskType: Hard disk media type. valid values:<br><li>CLOUD_PREMIUM: indicates high-performance CLOUD block storage</li><br><li>CLOUD_BSSD: indicates universal type SSD CLOUD disk</li><br><li>CLOUD_SSD: indicates SSD CLOUD disk</li><br><li>CLOUD_HSSD: indicates enhanced SSD CLOUD disk</li><br><li>CLOUD_TSSD: indicates ultra-fast SSD cbs.</li>ultra-fast SSD CBS (CLOUD_TSSD) is only supported when purchased with some instances and not currently supported for separate creation.
        :type DiskType: str
        :param _DiskName: Cloud disk name. If it is not specified, "Unnamed" will be used by default. The maximum length is 60 bytes.
        :type DiskName: str
        :param _Tags: Tags bound to the cloud disk.
        :type Tags: list of Tag
        :param _SnapshotId: Snapshot ID. If this parameter is specified, the cloud disk will be created based on the snapshot. The snapshot must be a data disk snapshot. To query the type of a snapshot, call the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API and see the `DiskUsage` field in the response.
        :type SnapshotId: str
        :param _DiskCount: Number of cloud disks to be created. If it is not specified, `1` will be used by default. There is an upper limit on the maximum number of cloud disks that can be created in a single request. For more information, see [Use Limits](https://intl.cloud.tencent.com/doc/product/362/5145?from_cn_redirect=1).
        :type DiskCount: int
        :param _ThroughputPerformance: Use this parameter to purchase additional performance for CLOUD disk in MB/s.<br>currently, only extreme CBS (CLOUD_TSSD) and enhanced SSD CLOUD disk (CLOUD_HSSD) are supported.
        :type ThroughputPerformance: int
        :param _KmsKeyId: Custom key for purchasing encrypted disks. when this parameter is input, the Encrypt parameter cannot be empty.
        :type KmsKeyId: str
        :param _DiskSize: Cloud disk size in GiB. <li>if `SnapshotId` is input, `DiskSize` can be omitted. at this point, the new cloud disk size will be the snapshot size.</li> <li>if both `SnapshotId` and `DiskSize` are input, the cloud disk size must be greater than or equal to the snapshot size.</li> <li>for the cloud disk size range, please refer to the [product type](https://www.tencentcloud.com/document/product/362/2353?from_cn_redirect=1) of cloud block storage.</li>.
        :type DiskSize: int
        :param _Shareable: When True is entered, the cloud disk will be created as a shared cloud disk. default is False. since shared cloud disk does not support encryption, this parameter cannot be imported simultaneously with the Encrypt parameter.
        :type Shareable: bool
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        :param _Encrypt: This parameter is used to create an encrypted cloud disk, with the value fixed as ENCRYPT. since shared cloud disk does not support encryption, this parameter cannot be imported simultaneously with the Shareable parameter.
        :type Encrypt: str
        :param _DiskChargePrepaid: Prepaid mode, that is, the settings for the monthly subscription-related parameters. through this parameter, you can specify the purchase duration of the monthly subscribed cloud disk, whether to enable auto-renewal, and other attributes. this parameter is required for creating a prepaid cloud disk, but no need to specify it when creating an hourly postpaid cloud disk.
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param _DeleteSnapshot: Delete associated non-permanently retained snapshots when destroying the cloud disk. 0 means non-permanent snapshots are not deleted with cloud disk destruction, 1 means non-permanent snapshots are deleted with cloud disk destruction. default value is 0. whether a snapshot is permanently retained can be determined through the IsPermanent field in the snapshot description returned by the [DescribeSnapshots](https://www.tencentcloud.com/document/api/362/15647?from_cn_redirect=1) api. True represents a permanent snapshot, False represents a non-permanent snapshot.
        :type DeleteSnapshot: int
        :param _AutoMountConfiguration: Specifies auto mount and initialization of the data disk when creating a cloud disk. this parameter cannot be imported simultaneously with the Encrypt parameter because encrypted disks do not support auto mount or initialization.
        :type AutoMountConfiguration: :class:`tencentcloud.cbs.v20170312.models.AutoMountConfiguration`
        :param _DiskBackupQuota: Specifies the cloud disk backup point quota.
        :type DiskBackupQuota: int
        :param _BurstPerformance: Specifies whether to enable burst performance when creating a CLOUD disk. currently only supports extreme cbs (CLOUD_TSSD) and enhanced SSD CLOUD disk (CLOUD_HSSD) with CLOUD disk size greater than or equal to 460GiB.
        :type BurstPerformance: bool
        :param _EncryptType: Specifies the CBS encryption type. valid values are ENCRYPT_V1 and ENCRYPT_V2, representing first generation and second generation encryption technology respectively. the two encryption technologies are incompatible. it is recommended to prioritize using second generation encryption technology ENCRYPT_V2. first generation encryption is only supported on some outdated models. this parameter is valid only when creating an encrypted cloud disk.
        :type EncryptType: str
        """
        self._Placement = None
        self._DiskChargeType = None
        self._DiskType = None
        self._DiskName = None
        self._Tags = None
        self._SnapshotId = None
        self._DiskCount = None
        self._ThroughputPerformance = None
        self._KmsKeyId = None
        self._DiskSize = None
        self._Shareable = None
        self._ClientToken = None
        self._Encrypt = None
        self._DiskChargePrepaid = None
        self._DeleteSnapshot = None
        self._AutoMountConfiguration = None
        self._DiskBackupQuota = None
        self._BurstPerformance = None
        self._EncryptType = None

    @property
    def Placement(self):
        r"""Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone and project. If no project is specified, the default project will be used.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def DiskChargeType(self):
        r"""Cloud disk billing mode. POSTPAID_BY_HOUR: Pay-as-you-go by hour<br><li>CDCPAID: Billed together with the bound dedicated cluster<br>For more information on the pricing in each mode, see [Pricing Overview](https://intl.cloud.tencent.com/document/product/362/2413?from_cn_redirect=1).
        :rtype: str
        """
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def DiskType(self):
        r"""Hard disk media type. valid values:<br><li>CLOUD_PREMIUM: indicates high-performance CLOUD block storage</li><br><li>CLOUD_BSSD: indicates universal type SSD CLOUD disk</li><br><li>CLOUD_SSD: indicates SSD CLOUD disk</li><br><li>CLOUD_HSSD: indicates enhanced SSD CLOUD disk</li><br><li>CLOUD_TSSD: indicates ultra-fast SSD cbs.</li>ultra-fast SSD CBS (CLOUD_TSSD) is only supported when purchased with some instances and not currently supported for separate creation.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskName(self):
        r"""Cloud disk name. If it is not specified, "Unnamed" will be used by default. The maximum length is 60 bytes.
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def Tags(self):
        r"""Tags bound to the cloud disk.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SnapshotId(self):
        r"""Snapshot ID. If this parameter is specified, the cloud disk will be created based on the snapshot. The snapshot must be a data disk snapshot. To query the type of a snapshot, call the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API and see the `DiskUsage` field in the response.
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskCount(self):
        r"""Number of cloud disks to be created. If it is not specified, `1` will be used by default. There is an upper limit on the maximum number of cloud disks that can be created in a single request. For more information, see [Use Limits](https://intl.cloud.tencent.com/doc/product/362/5145?from_cn_redirect=1).
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def ThroughputPerformance(self):
        r"""Use this parameter to purchase additional performance for CLOUD disk in MB/s.<br>currently, only extreme CBS (CLOUD_TSSD) and enhanced SSD CLOUD disk (CLOUD_HSSD) are supported.
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def KmsKeyId(self):
        r"""Custom key for purchasing encrypted disks. when this parameter is input, the Encrypt parameter cannot be empty.
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def DiskSize(self):
        r"""Cloud disk size in GiB. <li>if `SnapshotId` is input, `DiskSize` can be omitted. at this point, the new cloud disk size will be the snapshot size.</li> <li>if both `SnapshotId` and `DiskSize` are input, the cloud disk size must be greater than or equal to the snapshot size.</li> <li>for the cloud disk size range, please refer to the [product type](https://www.tencentcloud.com/document/product/362/2353?from_cn_redirect=1) of cloud block storage.</li>.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Shareable(self):
        r"""When True is entered, the cloud disk will be created as a shared cloud disk. default is False. since shared cloud disk does not support encryption, this parameter cannot be imported simultaneously with the Encrypt parameter.
        :rtype: bool
        """
        return self._Shareable

    @Shareable.setter
    def Shareable(self, Shareable):
        self._Shareable = Shareable

    @property
    def ClientToken(self):
        r"""A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Encrypt(self):
        r"""This parameter is used to create an encrypted cloud disk, with the value fixed as ENCRYPT. since shared cloud disk does not support encryption, this parameter cannot be imported simultaneously with the Shareable parameter.
        :rtype: str
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def DiskChargePrepaid(self):
        r"""Prepaid mode, that is, the settings for the monthly subscription-related parameters. through this parameter, you can specify the purchase duration of the monthly subscribed cloud disk, whether to enable auto-renewal, and other attributes. this parameter is required for creating a prepaid cloud disk, but no need to specify it when creating an hourly postpaid cloud disk.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        """
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DeleteSnapshot(self):
        r"""Delete associated non-permanently retained snapshots when destroying the cloud disk. 0 means non-permanent snapshots are not deleted with cloud disk destruction, 1 means non-permanent snapshots are deleted with cloud disk destruction. default value is 0. whether a snapshot is permanently retained can be determined through the IsPermanent field in the snapshot description returned by the [DescribeSnapshots](https://www.tencentcloud.com/document/api/362/15647?from_cn_redirect=1) api. True represents a permanent snapshot, False represents a non-permanent snapshot.
        :rtype: int
        """
        return self._DeleteSnapshot

    @DeleteSnapshot.setter
    def DeleteSnapshot(self, DeleteSnapshot):
        self._DeleteSnapshot = DeleteSnapshot

    @property
    def AutoMountConfiguration(self):
        r"""Specifies auto mount and initialization of the data disk when creating a cloud disk. this parameter cannot be imported simultaneously with the Encrypt parameter because encrypted disks do not support auto mount or initialization.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.AutoMountConfiguration`
        """
        return self._AutoMountConfiguration

    @AutoMountConfiguration.setter
    def AutoMountConfiguration(self, AutoMountConfiguration):
        self._AutoMountConfiguration = AutoMountConfiguration

    @property
    def DiskBackupQuota(self):
        r"""Specifies the cloud disk backup point quota.
        :rtype: int
        """
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota

    @property
    def BurstPerformance(self):
        r"""Specifies whether to enable burst performance when creating a CLOUD disk. currently only supports extreme cbs (CLOUD_TSSD) and enhanced SSD CLOUD disk (CLOUD_HSSD) with CLOUD disk size greater than or equal to 460GiB.
        :rtype: bool
        """
        return self._BurstPerformance

    @BurstPerformance.setter
    def BurstPerformance(self, BurstPerformance):
        self._BurstPerformance = BurstPerformance

    @property
    def EncryptType(self):
        r"""Specifies the CBS encryption type. valid values are ENCRYPT_V1 and ENCRYPT_V2, representing first generation and second generation encryption technology respectively. the two encryption technologies are incompatible. it is recommended to prioritize using second generation encryption technology ENCRYPT_V2. first generation encryption is only supported on some outdated models. this parameter is valid only when creating an encrypted cloud disk.
        :rtype: str
        """
        return self._EncryptType

    @EncryptType.setter
    def EncryptType(self, EncryptType):
        self._EncryptType = EncryptType


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
        self._KmsKeyId = params.get("KmsKeyId")
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
        self._EncryptType = params.get("EncryptType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisksResponse(AbstractModel):
    r"""CreateDisks response structure.

    """

    def __init__(self):
        r"""
        :param _DiskIdSet: ID list of the created cloud disks. Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskIdSet: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskIdSet = None
        self._RequestId = None

    @property
    def DiskIdSet(self):
        r"""ID list of the created cloud disks. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DiskIdSet

    @DiskIdSet.setter
    def DiskIdSet(self, DiskIdSet):
        self._DiskIdSet = DiskIdSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiskIdSet = params.get("DiskIdSet")
        self._RequestId = params.get("RequestId")


class CreateSnapshotGroupRequest(AbstractModel):
    r"""CreateSnapshotGroup request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: Specifies the cloud disk ID list for creating snapshot groups. disks mounted on the same instance must be selected.
        :type DiskIds: list of str
        :param _SnapshotGroupName: Snapshot group name. snapshots associated with the snapshot group inherit the snapshot group name. example: if the snapshot group name is testSnapshotGroup and the snapshot group is associated with two snapshots, the snapshot names are testSnapshotGroup_0 and testSnapshotGroup_1 respectively.
        :type SnapshotGroupName: str
        :param _Tags: Specifies the Tag list that should be bound to the snapshot group.
        :type Tags: list of Tag
        """
        self._DiskIds = None
        self._SnapshotGroupName = None
        self._Tags = None

    @property
    def DiskIds(self):
        r"""Specifies the cloud disk ID list for creating snapshot groups. disks mounted on the same instance must be selected.
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def SnapshotGroupName(self):
        r"""Snapshot group name. snapshots associated with the snapshot group inherit the snapshot group name. example: if the snapshot group name is testSnapshotGroup and the snapshot group is associated with two snapshots, the snapshot names are testSnapshotGroup_0 and testSnapshotGroup_1 respectively.
        :rtype: str
        """
        return self._SnapshotGroupName

    @SnapshotGroupName.setter
    def SnapshotGroupName(self, SnapshotGroupName):
        self._SnapshotGroupName = SnapshotGroupName

    @property
    def Tags(self):
        r"""Specifies the Tag list that should be bound to the snapshot group.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._SnapshotGroupName = params.get("SnapshotGroupName")
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
        


class CreateSnapshotGroupResponse(AbstractModel):
    r"""CreateSnapshotGroup response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotGroupId: Specifies the snapshot group ID created successfully.
        :type SnapshotGroupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotGroupId = None
        self._RequestId = None

    @property
    def SnapshotGroupId(self):
        r"""Specifies the snapshot group ID created successfully.
        :rtype: str
        """
        return self._SnapshotGroupId

    @SnapshotGroupId.setter
    def SnapshotGroupId(self, SnapshotGroupId):
        self._SnapshotGroupId = SnapshotGroupId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotGroupId = params.get("SnapshotGroupId")
        self._RequestId = params.get("RequestId")


class CreateSnapshotRequest(AbstractModel):
    r"""CreateSnapshot request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: ID of the cloud disk for which to create a snapshot, which can be queried through the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskId: str
        :param _SnapshotName: Snapshot name. If it is not specified, "Unnamed" will be used by default.
        :type SnapshotName: str
        :param _Deadline: Expiration time of the snapshot. It must be in UTC ISO-8601 format, eg. 2022-01-08T09:47:55+00:00. The snapshot will be automatically deleted when it expires.
        :type Deadline: str
        :param _DiskBackupId: Backup point ID of the cbs. when input this parameter, a snapshot will be created through the backup point. the backup point ID can be obtained through the [DescribeDiskBackups](https://www.tencentcloud.com/document/product/362/80278?from_cn_redirect=1) API query.
        :type DiskBackupId: str
        :param _Tags: Tags bound to the snapshot.
        :type Tags: list of Tag
        :param _DiskUsage: Snapshot association cloud DISK type. valid values: SYSTEM_DISK (SYSTEM DISK), DATA_DISK (DATA DISK). optional. if left empty, the snapshot type remains consistent with the cloud DISK type. this parameter is based on some scenes where users need to create a DATA DISK snapshot from a SYSTEM DISK for shared usage.
        :type DiskUsage: str
        """
        self._DiskId = None
        self._SnapshotName = None
        self._Deadline = None
        self._DiskBackupId = None
        self._Tags = None
        self._DiskUsage = None

    @property
    def DiskId(self):
        r"""ID of the cloud disk for which to create a snapshot, which can be queried through the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def SnapshotName(self):
        r"""Snapshot name. If it is not specified, "Unnamed" will be used by default.
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Deadline(self):
        r"""Expiration time of the snapshot. It must be in UTC ISO-8601 format, eg. 2022-01-08T09:47:55+00:00. The snapshot will be automatically deleted when it expires.
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def DiskBackupId(self):
        r"""Backup point ID of the cbs. when input this parameter, a snapshot will be created through the backup point. the backup point ID can be obtained through the [DescribeDiskBackups](https://www.tencentcloud.com/document/product/362/80278?from_cn_redirect=1) API query.
        :rtype: str
        """
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def Tags(self):
        r"""Tags bound to the snapshot.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DiskUsage(self):
        r"""Snapshot association cloud DISK type. valid values: SYSTEM_DISK (SYSTEM DISK), DATA_DISK (DATA DISK). optional. if left empty, the snapshot type remains consistent with the cloud DISK type. this parameter is based on some scenes where users need to create a DATA DISK snapshot from a SYSTEM DISK for shared usage.
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage


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
        self._DiskUsage = params.get("DiskUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotResponse(AbstractModel):
    r"""CreateSnapshot response structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: ID of the created snapshot <br/>Note: This field may return null, indicating that no valid values can be obtained.
        :type SnapshotId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SnapshotId = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        r"""ID of the created snapshot <br/>Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._RequestId = params.get("RequestId")


class DeleteAutoSnapshotPoliciesRequest(AbstractModel):
    r"""DeleteAutoSnapshotPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyIds: Specifies the ID list of the regular snapshot policies to delete. query via the DescribeAutoSnapshotPolicies api (https://www.tencentcloud.com/document/api/362/33556?from_cn_redirect=1).
        :type AutoSnapshotPolicyIds: list of str
        """
        self._AutoSnapshotPolicyIds = None

    @property
    def AutoSnapshotPolicyIds(self):
        r"""Specifies the ID list of the regular snapshot policies to delete. query via the DescribeAutoSnapshotPolicies api (https://www.tencentcloud.com/document/api/362/33556?from_cn_redirect=1).
        :rtype: list of str
        """
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
    r"""DeleteAutoSnapshotPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDiskBackupsRequest(AbstractModel):
    r"""DeleteDiskBackups request structure.

    """

    def __init__(self):
        r"""
        :param _DiskBackupIds: Cloud disk backup point ID to be deleted. can be queried through the [DescribeDiskBackups](https://www.tencentcloud.com/document/product/362/80278?from_cn_redirect=1) api.
        :type DiskBackupIds: list of str
        """
        self._DiskBackupIds = None

    @property
    def DiskBackupIds(self):
        r"""Cloud disk backup point ID to be deleted. can be queried through the [DescribeDiskBackups](https://www.tencentcloud.com/document/product/362/80278?from_cn_redirect=1) api.
        :rtype: list of str
        """
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
    r"""DeleteDiskBackups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSnapshotGroupRequest(AbstractModel):
    r"""DeleteSnapshotGroup request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotGroupId: Specifies the snapshot group ID.
        :type SnapshotGroupId: str
        :param _SnapshotGroupIds: List of snapshot group ids. this parameter and the snapshot group ID must provide at least one. if both are provided, they will be merged with the snapshot group ID.
        :type SnapshotGroupIds: list of str
        :param _DeleteBindImages: Specifies whether to delete the image associated with the snapshot group at the same time. valid values: set to false (not delete the image bound to the snapshot group; at this point, if the snapshot group has bound images, deletion will fail) or set to true (delete the image bound to the snapshot group simultaneously). default value is false.
        :type DeleteBindImages: bool
        """
        self._SnapshotGroupId = None
        self._SnapshotGroupIds = None
        self._DeleteBindImages = None

    @property
    def SnapshotGroupId(self):
        r"""Specifies the snapshot group ID.
        :rtype: str
        """
        return self._SnapshotGroupId

    @SnapshotGroupId.setter
    def SnapshotGroupId(self, SnapshotGroupId):
        self._SnapshotGroupId = SnapshotGroupId

    @property
    def SnapshotGroupIds(self):
        r"""List of snapshot group ids. this parameter and the snapshot group ID must provide at least one. if both are provided, they will be merged with the snapshot group ID.
        :rtype: list of str
        """
        return self._SnapshotGroupIds

    @SnapshotGroupIds.setter
    def SnapshotGroupIds(self, SnapshotGroupIds):
        self._SnapshotGroupIds = SnapshotGroupIds

    @property
    def DeleteBindImages(self):
        r"""Specifies whether to delete the image associated with the snapshot group at the same time. valid values: set to false (not delete the image bound to the snapshot group; at this point, if the snapshot group has bound images, deletion will fail) or set to true (delete the image bound to the snapshot group simultaneously). default value is false.
        :rtype: bool
        """
        return self._DeleteBindImages

    @DeleteBindImages.setter
    def DeleteBindImages(self, DeleteBindImages):
        self._DeleteBindImages = DeleteBindImages


    def _deserialize(self, params):
        self._SnapshotGroupId = params.get("SnapshotGroupId")
        self._SnapshotGroupIds = params.get("SnapshotGroupIds")
        self._DeleteBindImages = params.get("DeleteBindImages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotGroupResponse(AbstractModel):
    r"""DeleteSnapshotGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSnapshotsRequest(AbstractModel):
    r"""DeleteSnapshots request structure.

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
        r"""List of IDs of snapshots to be deleted, which can be queried via [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :rtype: list of str
        """
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def DeleteBindImages(self):
        r"""Whether to forcibly delete the image associated with the snapshot
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
    r"""DeleteSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAutoSnapshotPoliciesRequest(AbstractModel):
    r"""DescribeAutoSnapshotPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyIds: List of scheduled snapshot policy IDs to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`.
        :type AutoSnapshotPolicyIds: list of str
        :param _Filters: Filter criteria. AutoSnapshotPolicyIds and Filters cannot be specified at the same time.
<li>auto-snapshot-policy-id - Array of String - required: no - (filter condition) filter by regular snapshot policy id. regular snapshot policy id such as: `asp-3stvwfxx`.</li>.
<li>AutoSnapshotPolicyState - Array of String - required: no - (filter condition) filters by the status of the regular snapshot policy. regular snapshot policy ID format: `asp-3stvwfxx`. (NORMAL: NORMAL | ISOLATED: ISOLATED).</li>.
<li>AutoSnapshotPolicyName - Array of String - required: no - (filter condition) filters by the name of the regular snapshot policy.</li>.
        :type Filters: list of Filter
        :param _Limit: Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param _Order: Specifies the output order of the regular snapshot list. valid values: <br><li>ASC: ascending order<br></li><li>DESC: descending order.</li>.
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
        r"""List of scheduled snapshot policy IDs to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`.
        :rtype: list of str
        """
        return self._AutoSnapshotPolicyIds

    @AutoSnapshotPolicyIds.setter
    def AutoSnapshotPolicyIds(self, AutoSnapshotPolicyIds):
        self._AutoSnapshotPolicyIds = AutoSnapshotPolicyIds

    @property
    def Filters(self):
        r"""Filter criteria. AutoSnapshotPolicyIds and Filters cannot be specified at the same time.
<li>auto-snapshot-policy-id - Array of String - required: no - (filter condition) filter by regular snapshot policy id. regular snapshot policy id such as: `asp-3stvwfxx`.</li>.
<li>AutoSnapshotPolicyState - Array of String - required: no - (filter condition) filters by the status of the regular snapshot policy. regular snapshot policy ID format: `asp-3stvwfxx`. (NORMAL: NORMAL | ISOLATED: ISOLATED).</li>.
<li>AutoSnapshotPolicyName - Array of String - required: no - (filter condition) filters by the name of the regular snapshot policy.</li>.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""Specifies the output order of the regular snapshot list. valid values: <br><li>ASC: ascending order<br></li><li>DESC: descending order.</li>.
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""The sorting filter applied to the scheduled snapshot list. Value range: <Sort by creation time of scheduled snapshot. By default, this is sorted by creation time.
        :rtype: str
        """
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
    r"""DescribeAutoSnapshotPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The quantity of valid scheduled snapshot policies.
        :type TotalCount: int
        :param _AutoSnapshotPolicySet: List of scheduled snapshot policies.
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoSnapshotPolicySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""The quantity of valid scheduled snapshot policies.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoSnapshotPolicySet(self):
        r"""List of scheduled snapshot policies.
        :rtype: list of AutoSnapshotPolicy
        """
        return self._AutoSnapshotPolicySet

    @AutoSnapshotPolicySet.setter
    def AutoSnapshotPolicySet(self, AutoSnapshotPolicySet):
        self._AutoSnapshotPolicySet = AutoSnapshotPolicySet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""DescribeDiskAssociatedAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: Specifies the cloud disk ID to query. can be queried via the [DescribeDisks](https://www.tencentcloud.com/document/api/362/16315?from_cn_redirect=1) api.
        :type DiskId: str
        """
        self._DiskId = None

    @property
    def DiskId(self):
        r"""Specifies the cloud disk ID to query. can be queried via the [DescribeDisks](https://www.tencentcloud.com/document/api/362/16315?from_cn_redirect=1) api.
        :rtype: str
        """
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
    r"""DescribeDiskAssociatedAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The quantity of scheduled snapshots binded to cloud disk.
        :type TotalCount: int
        :param _AutoSnapshotPolicySet: List of scheduled snapshots bound to cloud disk.
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoSnapshotPolicySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""The quantity of scheduled snapshots binded to cloud disk.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoSnapshotPolicySet(self):
        r"""List of scheduled snapshots bound to cloud disk.
        :rtype: list of AutoSnapshotPolicy
        """
        return self._AutoSnapshotPolicySet

    @AutoSnapshotPolicySet.setter
    def AutoSnapshotPolicySet(self, AutoSnapshotPolicySet):
        self._AutoSnapshotPolicySet = AutoSnapshotPolicySet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""DescribeDiskBackups request structure.

    """

    def __init__(self):
        r"""
        :param _DiskBackupIds: List of IDs of the backup points to be queried. `DiskBackupIds` and `Filters` cannot be specified at the same time.
        :type DiskBackupIds: list of str
        :param _Filters: Filter criteria. parameters must not be specified simultaneously for DiskBackupIds and Filters. filter conditions:<br><li>disk-backup-id - Array of String - required: no - (filter condition) Filters by backup point id. backup point id format: dbp-11112222.</li><br><li>disk-id - Array of String - required: no - (filter condition) Filters by cloud disk id where the backup point was created. cloud disk id format: disk-srftydert.</li><br><li>disk-usage - Array of String - required: no - (filter condition) Filters by cloud disk type (SYSTEM_disk: represents SYSTEM disk | DATA_disk: represents DATA disk).</li>.
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param _Order: Specifies the sorting order of the CBS backup point list. default: ASC. valid values: <br><li>ASC: ascending order</li><br><li>DESC: descending order.</li>.
        :type Order: str
        :param _OrderField: Field on which the list of cloud disk backup points is sorted. valid values: <br><li>CREATE_TIME: sort by creation TIME of the cloud disk backup point</li><br>sort by creation TIME by default.
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
        r"""List of IDs of the backup points to be queried. `DiskBackupIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._DiskBackupIds

    @DiskBackupIds.setter
    def DiskBackupIds(self, DiskBackupIds):
        self._DiskBackupIds = DiskBackupIds

    @property
    def Filters(self):
        r"""Filter criteria. parameters must not be specified simultaneously for DiskBackupIds and Filters. filter conditions:<br><li>disk-backup-id - Array of String - required: no - (filter condition) Filters by backup point id. backup point id format: dbp-11112222.</li><br><li>disk-id - Array of String - required: no - (filter condition) Filters by cloud disk id where the backup point was created. cloud disk id format: disk-srftydert.</li><br><li>disk-usage - Array of String - required: no - (filter condition) Filters by cloud disk type (SYSTEM_disk: represents SYSTEM disk | DATA_disk: represents DATA disk).</li>.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""Specifies the sorting order of the CBS backup point list. default: ASC. valid values: <br><li>ASC: ascending order</li><br><li>DESC: descending order.</li>.
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""Field on which the list of cloud disk backup points is sorted. valid values: <br><li>CREATE_TIME: sort by creation TIME of the cloud disk backup point</li><br>sort by creation TIME by default.
        :rtype: str
        """
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
    r"""DescribeDiskBackups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible cloud disk backup points.
        :type TotalCount: int
        :param _DiskBackupSet: List of details of cloud disk backup points.
        :type DiskBackupSet: list of DiskBackup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DiskBackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of eligible cloud disk backup points.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DiskBackupSet(self):
        r"""List of details of cloud disk backup points.
        :rtype: list of DiskBackup
        """
        return self._DiskBackupSet

    @DiskBackupSet.setter
    def DiskBackupSet(self, DiskBackupSet):
        self._DiskBackupSet = DiskBackupSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""DescribeDiskConfigQuota request structure.

    """

    def __init__(self):
        r"""
        :param _InquiryType: INQUIRY type. valid values:<br>INQUIRY_CBS_CONFIG: query the cloud disk configuration list<br>INQUIRY_CVM_CONFIG: query the configuration list of cloud disks with instances.
        :type InquiryType: str
        :param _DiskChargeType: Billing mode. Value range: <br><li>POSTPAID_BY_HOUR: postpaid.
        :type DiskChargeType: str
        :param _InstanceFamilies: Filter by the instance model series, such as S1, I1 and M1. For more information, please see [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1)
        :type InstanceFamilies: list of str
        :param _DiskTypes: Hard disk media type. valid values: <br> CLOUD_BASIC: BASIC CLOUD disk <br> CLOUD_PREMIUM: high-performance CLOUD block storage <br> CLOUD_SSD: SSD CLOUD disk <br> CLOUD_HSSD: enhanced SSD CLOUD disk.
        :type DiskTypes: list of str
        :param _Zones: Query configuration under one or more [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo).
        :type Zones: list of str
        :param _Memory: Instance memory size in GB.
        :type Memory: int
        :param _DiskUsage: SYSTEM DISK or DATA DISK. valid values:<br>SYSTEM_DISK: SYSTEM DISK<br>DATA_DISK: DATA DISK.
        :type DiskUsage: str
        :param _CPU: Instance CPU cores.
        :type CPU: int
        :param _DedicatedClusterId: Dedicated cluster ID.
        :type DedicatedClusterId: str
        """
        self._InquiryType = None
        self._DiskChargeType = None
        self._InstanceFamilies = None
        self._DiskTypes = None
        self._Zones = None
        self._Memory = None
        self._DiskUsage = None
        self._CPU = None
        self._DedicatedClusterId = None

    @property
    def InquiryType(self):
        r"""INQUIRY type. valid values:<br>INQUIRY_CBS_CONFIG: query the cloud disk configuration list<br>INQUIRY_CVM_CONFIG: query the configuration list of cloud disks with instances.
        :rtype: str
        """
        return self._InquiryType

    @InquiryType.setter
    def InquiryType(self, InquiryType):
        self._InquiryType = InquiryType

    @property
    def DiskChargeType(self):
        r"""Billing mode. Value range: <br><li>POSTPAID_BY_HOUR: postpaid.
        :rtype: str
        """
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def InstanceFamilies(self):
        r"""Filter by the instance model series, such as S1, I1 and M1. For more information, please see [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1)
        :rtype: list of str
        """
        return self._InstanceFamilies

    @InstanceFamilies.setter
    def InstanceFamilies(self, InstanceFamilies):
        self._InstanceFamilies = InstanceFamilies

    @property
    def DiskTypes(self):
        r"""Hard disk media type. valid values: <br> CLOUD_BASIC: BASIC CLOUD disk <br> CLOUD_PREMIUM: high-performance CLOUD block storage <br> CLOUD_SSD: SSD CLOUD disk <br> CLOUD_HSSD: enhanced SSD CLOUD disk.
        :rtype: list of str
        """
        return self._DiskTypes

    @DiskTypes.setter
    def DiskTypes(self, DiskTypes):
        self._DiskTypes = DiskTypes

    @property
    def Zones(self):
        r"""Query configuration under one or more [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo).
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Memory(self):
        r"""Instance memory size in GB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DiskUsage(self):
        r"""SYSTEM DISK or DATA DISK. valid values:<br>SYSTEM_DISK: SYSTEM DISK<br>DATA_DISK: DATA DISK.
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def CPU(self):
        r"""Instance CPU cores.
        :rtype: int
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def DedicatedClusterId(self):
        r"""Dedicated cluster ID.
        :rtype: str
        """
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId


    def _deserialize(self, params):
        self._InquiryType = params.get("InquiryType")
        self._DiskChargeType = params.get("DiskChargeType")
        self._InstanceFamilies = params.get("InstanceFamilies")
        self._DiskTypes = params.get("DiskTypes")
        self._Zones = params.get("Zones")
        self._Memory = params.get("Memory")
        self._DiskUsage = params.get("DiskUsage")
        self._CPU = params.get("CPU")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskConfigQuotaResponse(AbstractModel):
    r"""DescribeDiskConfigQuota response structure.

    """

    def __init__(self):
        r"""
        :param _DiskConfigSet: List of cloud disk configurations.
        :type DiskConfigSet: list of DiskConfig
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskConfigSet = None
        self._RequestId = None

    @property
    def DiskConfigSet(self):
        r"""List of cloud disk configurations.
        :rtype: list of DiskConfig
        """
        return self._DiskConfigSet

    @DiskConfigSet.setter
    def DiskConfigSet(self, DiskConfigSet):
        self._DiskConfigSet = DiskConfigSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeDiskStoragePoolRequest(AbstractModel):
    r"""DescribeDiskStoragePool request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of returned results, defaults to 20 with a maximum value of 100. For further introduction about `Limit`, see relevant sections in the API [overview](/document/product/362/15633).
        :type Limit: int
        :param _CdcIds: Specify the exclusive cluster ID list you want to query. This parameter cannot be used with Filters.

        :type CdcIds: list of str
        :param _Filters: Filter conditions. `CdcIds` and `Filters` cannot be specified at the same time. <br><li>cdc-id - Array of String - Optional - Filter by the cluster ID. <br><li>zone - Array of String - Optional - Filter by the [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) where the cluster resides. <br><li>cage-id - Array of String - Optional - Filter by the ID of the cage where the cluster resides. <br><li>disk-type - Array of string - Optional - Filter by the media type of cloud disks (`CLOUD_BASIC`: HDD cloud disk | `CLOUD_PREMIUM`: Premium cloud disk. | `CLOUD_SSD`: SSD cloud disk.)
        :type Filters: list of Filter
        :param _Offset: Offset, defaults to 0. For further introduction about `Offset`, see the relevant sections in the API [overview](/document/product/362/15633).
        :type Offset: int
        """
        self._Limit = None
        self._CdcIds = None
        self._Filters = None
        self._Offset = None

    @property
    def Limit(self):
        r"""Number of returned results, defaults to 20 with a maximum value of 100. For further introduction about `Limit`, see relevant sections in the API [overview](/document/product/362/15633).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CdcIds(self):
        r"""Specify the exclusive cluster ID list you want to query. This parameter cannot be used with Filters.

        :rtype: list of str
        """
        return self._CdcIds

    @CdcIds.setter
    def CdcIds(self, CdcIds):
        self._CdcIds = CdcIds

    @property
    def Filters(self):
        r"""Filter conditions. `CdcIds` and `Filters` cannot be specified at the same time. <br><li>cdc-id - Array of String - Optional - Filter by the cluster ID. <br><li>zone - Array of String - Optional - Filter by the [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) where the cluster resides. <br><li>cage-id - Array of String - Optional - Filter by the ID of the cage where the cluster resides. <br><li>disk-type - Array of string - Optional - Filter by the media type of cloud disks (`CLOUD_BASIC`: HDD cloud disk | `CLOUD_PREMIUM`: Premium cloud disk. | `CLOUD_SSD`: SSD cloud disk.)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""Offset, defaults to 0. For further introduction about `Offset`, see the relevant sections in the API [overview](/document/product/362/15633).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._CdcIds = params.get("CdcIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskStoragePoolResponse(AbstractModel):
    r"""DescribeDiskStoragePool response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: the number of eligible dedicated clusters.
        :type TotalCount: int
        :param _CdcSet: Details of the dedicated cluster.
        :type CdcSet: list of Cdc
        :param _DiskStoragePoolSet: Exclusive cluster details list.
        :type DiskStoragePoolSet: list of Cdc
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._CdcSet = None
        self._DiskStoragePoolSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""the number of eligible dedicated clusters.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CdcSet(self):
        r"""Details of the dedicated cluster.
        :rtype: list of Cdc
        """
        return self._CdcSet

    @CdcSet.setter
    def CdcSet(self, CdcSet):
        self._CdcSet = CdcSet

    @property
    def DiskStoragePoolSet(self):
        r"""Exclusive cluster details list.
        :rtype: list of Cdc
        """
        return self._DiskStoragePoolSet

    @DiskStoragePoolSet.setter
    def DiskStoragePoolSet(self, DiskStoragePoolSet):
        self._DiskStoragePoolSet = DiskStoragePoolSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CdcSet") is not None:
            self._CdcSet = []
            for item in params.get("CdcSet"):
                obj = Cdc()
                obj._deserialize(item)
                self._CdcSet.append(obj)
        if params.get("DiskStoragePoolSet") is not None:
            self._DiskStoragePoolSet = []
            for item in params.get("DiskStoragePoolSet"):
                obj = Cdc()
                obj._deserialize(item)
                self._DiskStoragePoolSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    r"""DescribeDisks request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filters. You cannot specify `DiskIds` and `Filters` at the same time. <br><li>disk-usage - Array of String - Optional - Filters by cloud disk type. (SYSTEM_DISK: system disk | DATA_DISK: data disk) <br><li>disk-charge-type - Array of String - Optional - Filters by cloud disk billing method. (POSTPAID_BY_HOUR: pay-as-you-go) <br><li>portable - Array of String- Optional - Filters by whether the cloud disk is elastic or not. (TRUE: elastic | FALSE: non-elastic) <br><li>project-id - Array of Integer - Optional - Filters by the ID of the project to which a cloud disk belongs. <br><li>disk-id - Array of String - Optional - Filters by cloud disk ID, such as `disk-11112222`. <br><li>disk-name - Array of String - Optional - Filters by cloud disk name. <br><li>disk-type - Array of String - Optional - Filters by cloud disk media type (CLOUD_BASIC: HDD cloud disk | CLOUD_PREMIUM: Premium Cloud Storage | CLOUD_SSD: SSD cloud disk.) <br><li>disk-state - Array of String - Optional - Filters by cloud disk state. (UNATTACHED: not mounted | ATTACHING: being mounted | ATTACHED: mounted | DETACHING: being unmounted | EXPANDING: being expanded | ROLLBACKING: being rolled back | TORECYCLE: to be repossessed.) <br><li>instance-id - Array of String - Optional - Filters by the ID of the CVM instance on which a cloud disk is mounted. You can use this parameter to query the cloud disks mounted on specific CVMs. <br><li>zone - Array of String - Optional - Filters by [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) <br><li>instance-ip-address - Array of String - Optional - Filters by the private or public IP of the CVM on which a cloud disk is mounted. <br><li>instance-name - Array of String - Optional - Filters by the name of the instance on which a cloud disk is mounted. <br><li>tag-key - Array of String - Optional - Filters by tag key. <br><li>tag-value - Array of String - Optional - Filters by tag value. <br><li>tag:tag-key - Array of String - Optional - Filters by tag key-value pair. Please replace `tag-key` with a specific tag key.
        :type Filters: list of Filter
        :param _Limit: Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param _OrderField: Field on which the list of cloud disks is sorted. valid values: <br><li>CREATE_TIME: sort by creation TIME of the cloud disk</li><br><li>DEADLINE: sort by expiration TIME of the cloud disk</li><br>sort by creation TIME by default.
        :type OrderField: str
        :param _Offset: Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param _ReturnBindAutoSnapshotPolicy: Whether the ID of the periodic snapshot policy bound to the cloud disk needs to be returned in the cloud disk details. TRUE: return; FALSE: do not return.
        :type ReturnBindAutoSnapshotPolicy: bool
        :param _DiskIds: Query by one or more cloud disk IDs, such as `disk-11112222`. For the format of this parameter, please see the ids.N section of the API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1). This parameter does not support specifying both `DiskIds` and `Filters`.
        :type DiskIds: list of str
        :param _Order: Specifies the sorting order of the cloud disk list. valid values: <br><li>ASC: ascending order</li><br><li>DESC: descending order.</li>.
        :type Order: str
        """
        self._Filters = None
        self._Limit = None
        self._OrderField = None
        self._Offset = None
        self._ReturnBindAutoSnapshotPolicy = None
        self._DiskIds = None
        self._Order = None

    @property
    def Filters(self):
        r"""Filters. You cannot specify `DiskIds` and `Filters` at the same time. <br><li>disk-usage - Array of String - Optional - Filters by cloud disk type. (SYSTEM_DISK: system disk | DATA_DISK: data disk) <br><li>disk-charge-type - Array of String - Optional - Filters by cloud disk billing method. (POSTPAID_BY_HOUR: pay-as-you-go) <br><li>portable - Array of String- Optional - Filters by whether the cloud disk is elastic or not. (TRUE: elastic | FALSE: non-elastic) <br><li>project-id - Array of Integer - Optional - Filters by the ID of the project to which a cloud disk belongs. <br><li>disk-id - Array of String - Optional - Filters by cloud disk ID, such as `disk-11112222`. <br><li>disk-name - Array of String - Optional - Filters by cloud disk name. <br><li>disk-type - Array of String - Optional - Filters by cloud disk media type (CLOUD_BASIC: HDD cloud disk | CLOUD_PREMIUM: Premium Cloud Storage | CLOUD_SSD: SSD cloud disk.) <br><li>disk-state - Array of String - Optional - Filters by cloud disk state. (UNATTACHED: not mounted | ATTACHING: being mounted | ATTACHED: mounted | DETACHING: being unmounted | EXPANDING: being expanded | ROLLBACKING: being rolled back | TORECYCLE: to be repossessed.) <br><li>instance-id - Array of String - Optional - Filters by the ID of the CVM instance on which a cloud disk is mounted. You can use this parameter to query the cloud disks mounted on specific CVMs. <br><li>zone - Array of String - Optional - Filters by [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) <br><li>instance-ip-address - Array of String - Optional - Filters by the private or public IP of the CVM on which a cloud disk is mounted. <br><li>instance-name - Array of String - Optional - Filters by the name of the instance on which a cloud disk is mounted. <br><li>tag-key - Array of String - Optional - Filters by tag key. <br><li>tag-value - Array of String - Optional - Filters by tag value. <br><li>tag:tag-key - Array of String - Optional - Filters by tag key-value pair. Please replace `tag-key` with a specific tag key.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        r"""Field on which the list of cloud disks is sorted. valid values: <br><li>CREATE_TIME: sort by creation TIME of the cloud disk</li><br><li>DEADLINE: sort by expiration TIME of the cloud disk</li><br>sort by creation TIME by default.
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Offset(self):
        r"""Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ReturnBindAutoSnapshotPolicy(self):
        r"""Whether the ID of the periodic snapshot policy bound to the cloud disk needs to be returned in the cloud disk details. TRUE: return; FALSE: do not return.
        :rtype: bool
        """
        return self._ReturnBindAutoSnapshotPolicy

    @ReturnBindAutoSnapshotPolicy.setter
    def ReturnBindAutoSnapshotPolicy(self, ReturnBindAutoSnapshotPolicy):
        self._ReturnBindAutoSnapshotPolicy = ReturnBindAutoSnapshotPolicy

    @property
    def DiskIds(self):
        r"""Query by one or more cloud disk IDs, such as `disk-11112222`. For the format of this parameter, please see the ids.N section of the API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1). This parameter does not support specifying both `DiskIds` and `Filters`.
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Order(self):
        r"""Specifies the sorting order of the cloud disk list. valid values: <br><li>ASC: ascending order</li><br><li>DESC: descending order.</li>.
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Offset = params.get("Offset")
        self._ReturnBindAutoSnapshotPolicy = params.get("ReturnBindAutoSnapshotPolicy")
        self._DiskIds = params.get("DiskIds")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksResponse(AbstractModel):
    r"""DescribeDisks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The quantity of cloud disks meeting the conditions.
        :type TotalCount: int
        :param _DiskSet: List of cloud disk details.
        :type DiskSet: list of Disk
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DiskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""The quantity of cloud disks meeting the conditions.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DiskSet(self):
        r"""List of cloud disk details.
        :rtype: list of Disk
        """
        return self._DiskSet

    @DiskSet.setter
    def DiskSet(self, DiskSet):
        self._DiskSet = DiskSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""DescribeInstancesDiskNum request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: ID of the CVM instance can be queried via the API [DescribeInstances](https://intl.cloud.tencent.com/document/product/213/15728?from_cn_redirect=1).
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""ID of the CVM instance can be queried via the API [DescribeInstances](https://intl.cloud.tencent.com/document/product/213/15728?from_cn_redirect=1).
        :rtype: list of str
        """
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
    r"""DescribeInstancesDiskNum response structure.

    """

    def __init__(self):
        r"""
        :param _AttachDetail: The quantity of mounted and mountable elastic cloud disks for each cloud virtual machine
        :type AttachDetail: list of AttachDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AttachDetail = None
        self._RequestId = None

    @property
    def AttachDetail(self):
        r"""The quantity of mounted and mountable elastic cloud disks for each cloud virtual machine
        :rtype: list of AttachDetail
        """
        return self._AttachDetail

    @AttachDetail.setter
    def AttachDetail(self, AttachDetail):
        self._AttachDetail = AttachDetail

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeSnapshotGroupsRequest(AbstractModel):
    r"""DescribeSnapshotGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter criteria.<br><li>snapshot-group-id - Array of String - Required: No - (Filter criteria) Filter by snapshot group ID.<br><li>snapshot-group-state - Array of String - Required: No - (Filter criteria) Filter by snapshot group state. (NORMAL: Normal | CREATING: Creating | ROLLBACKING: Rolling back)<br><li>snapshot-group-name - Array of String - Required: No - (Filter criteria) Filter by snapshot group name.<br><li>snapshot-id - Array of String - Required: No - (Filter criteria) Filter by snapshot ID within the snapshot group.
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returns, with a default value of 20, and a maximum value of 100.
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        r"""Filter criteria.<br><li>snapshot-group-id - Array of String - Required: No - (Filter criteria) Filter by snapshot group ID.<br><li>snapshot-group-state - Array of String - Required: No - (Filter criteria) Filter by snapshot group state. (NORMAL: Normal | CREATING: Creating | ROLLBACKING: Rolling back)<br><li>snapshot-group-name - Array of String - Required: No - (Filter criteria) Filter by snapshot group name.<br><li>snapshot-id - Array of String - Required: No - (Filter criteria) Filter by snapshot ID within the snapshot group.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returns, with a default value of 20, and a maximum value of 100.
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
        


class DescribeSnapshotGroupsResponse(AbstractModel):
    r"""DescribeSnapshotGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of eligible items.
        :type TotalCount: int
        :param _SnapshotGroupSet: Specifies the snapshot group list details.
        :type SnapshotGroupSet: list of SnapshotGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SnapshotGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of eligible items.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SnapshotGroupSet(self):
        r"""Specifies the snapshot group list details.
        :rtype: list of SnapshotGroup
        """
        return self._SnapshotGroupSet

    @SnapshotGroupSet.setter
    def SnapshotGroupSet(self, SnapshotGroupSet):
        self._SnapshotGroupSet = SnapshotGroupSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SnapshotGroupSet") is not None:
            self._SnapshotGroupSet = []
            for item in params.get("SnapshotGroupSet"):
                obj = SnapshotGroup()
                obj._deserialize(item)
                self._SnapshotGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotOverviewRequest(AbstractModel):
    r"""DescribeSnapshotOverview request structure.

    """


class DescribeSnapshotOverviewResponse(AbstractModel):
    r"""DescribeSnapshotOverview response structure.

    """

    def __init__(self):
        r"""
        :param _TotalNums: Current number of valid snapshots.
        :type TotalNums: int
        :param _TotalSize: Total used snapshot capacity. unit: GiB.
        :type TotalSize: float
        :param _FreeQuota: Snapshot free quota size in GiB.
        :type FreeQuota: float
        :param _RealTradeSize: Snapshot actual cost of total capacity in GiB.
        :type RealTradeSize: float
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalNums = None
        self._TotalSize = None
        self._FreeQuota = None
        self._RealTradeSize = None
        self._RequestId = None

    @property
    def TotalNums(self):
        r"""Current number of valid snapshots.
        :rtype: int
        """
        return self._TotalNums

    @TotalNums.setter
    def TotalNums(self, TotalNums):
        self._TotalNums = TotalNums

    @property
    def TotalSize(self):
        r"""Total used snapshot capacity. unit: GiB.
        :rtype: float
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def FreeQuota(self):
        r"""Snapshot free quota size in GiB.
        :rtype: float
        """
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def RealTradeSize(self):
        r"""Snapshot actual cost of total capacity in GiB.
        :rtype: float
        """
        return self._RealTradeSize

    @RealTradeSize.setter
    def RealTradeSize(self, RealTradeSize):
        self._RealTradeSize = RealTradeSize

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNums = params.get("TotalNums")
        self._TotalSize = params.get("TotalSize")
        self._FreeQuota = params.get("FreeQuota")
        self._RealTradeSize = params.get("RealTradeSize")
        self._RequestId = params.get("RequestId")


class DescribeSnapshotSharePermissionRequest(AbstractModel):
    r"""DescribeSnapshotSharePermission request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: The ID of the snapshot to be queried. You can obtain this by using [DescribeSnapshots](https://intl.cloud.tencent.com/document/api/362/15647?from_cn_redirect=1).
        :type SnapshotId: str
        """
        self._SnapshotId = None

    @property
    def SnapshotId(self):
        r"""The ID of the snapshot to be queried. You can obtain this by using [DescribeSnapshots](https://intl.cloud.tencent.com/document/api/362/15647?from_cn_redirect=1).
        :rtype: str
        """
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
    r"""DescribeSnapshotSharePermission response structure.

    """

    def __init__(self):
        r"""
        :param _SharePermissionSet: The set of snapshot sharing information
        :type SharePermissionSet: list of SharePermission
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SharePermissionSet = None
        self._RequestId = None

    @property
    def SharePermissionSet(self):
        r"""The set of snapshot sharing information
        :rtype: list of SharePermission
        """
        return self._SharePermissionSet

    @SharePermissionSet.setter
    def SharePermissionSet(self, SharePermissionSet):
        self._SharePermissionSet = SharePermissionSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""DescribeSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: List of snapshot IDs to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`.
        :type SnapshotIds: list of str
        :param _Filters: Filter criteria. parameters `SnapshotIds` and `Filters` cannot be specified at the same time.<br><ul><li>snapshot-id<ul><li>filter by cloud disk snapshot id</li><li>type: String</li><li>required: no</li></ul></li><li>snapshot-name<ul><li>filter by cloud disk snapshot name</li><li>type: String</li><li>required: no</li></ul></li><li>snapshot-state<ul><li>filter by cloud disk snapshot status</li><li>type: String</li><li>required: no</li><li>value ranges FROM:<ul><li><code>NORMAL</code>: NORMAL</li><li><code>CREATING</code>: CREATING</li><li><code>ROLLBACKING</code>: rolling back</li><li><code>COPYING_FROM_REMOTE</code>: cross geo-replication in progress</li><li><code>CHECKING_COPIED</code>: COPYING check in progress</li><li><code>TORECYCLE</code>: pending recycling</li></ul></li></ul></li><li>disk-usage<ul><li>filter by cloud disk usage purpose</li><li>type: String</li><li>required: no</li><li>value ranges FROM:<ul><li><code>SYSTEM_disk</code>: represent SYSTEM disk</li><li><code>DATA_disk</code>: represent DATA disk</li></ul></li></ul></li><li>project-id<ul><li>filter by cloud disk project id</li><li>type: String</li><li>required: no</li></ul></li><li>disk-id<ul><li>filter by cloud disk id. up to 10 values can be specified</li><li>type: String</li><li>required: no</li></ul></li><li>encrypt<ul><li>filter by whether encrypted or not</li><li>type: String</li><li>required: no</li></ul></li><li>snapshot-type<ul><li>query by snapshot ownership type</li><li>type: String</li><li>required: no</li><li>value ranges FROM:<ul><li><code>SHARED_snapshot</code>: refer to SHARED snapshot</li><li><code>PRIVATE_snapshot</code>: refer to own PRIVATE snapshot</li></ul></li></ul></li></ul>.
        :type Filters: list of Filter
        :param _Limit: Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param _OrderField: Field based on which the snapshot list is sorted. valid values:.
<ul>
<Li>CREATE_TIME: specifies to sort by snapshot creation time.</li>.
<Li>Sort by creation time by default.</li>.
</ul>
        :type OrderField: str
        :param _Offset: Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param _Order: Outputs the sorting order of the cloud disk list. valid values:.
<ul>
<Li>ASC: specifies ascending order.</li>.
<Li>DESC: specifies sorting in descending order.</li>.
</ul>

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
        r"""List of snapshot IDs to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`.
        :rtype: list of str
        """
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def Filters(self):
        r"""Filter criteria. parameters `SnapshotIds` and `Filters` cannot be specified at the same time.<br><ul><li>snapshot-id<ul><li>filter by cloud disk snapshot id</li><li>type: String</li><li>required: no</li></ul></li><li>snapshot-name<ul><li>filter by cloud disk snapshot name</li><li>type: String</li><li>required: no</li></ul></li><li>snapshot-state<ul><li>filter by cloud disk snapshot status</li><li>type: String</li><li>required: no</li><li>value ranges FROM:<ul><li><code>NORMAL</code>: NORMAL</li><li><code>CREATING</code>: CREATING</li><li><code>ROLLBACKING</code>: rolling back</li><li><code>COPYING_FROM_REMOTE</code>: cross geo-replication in progress</li><li><code>CHECKING_COPIED</code>: COPYING check in progress</li><li><code>TORECYCLE</code>: pending recycling</li></ul></li></ul></li><li>disk-usage<ul><li>filter by cloud disk usage purpose</li><li>type: String</li><li>required: no</li><li>value ranges FROM:<ul><li><code>SYSTEM_disk</code>: represent SYSTEM disk</li><li><code>DATA_disk</code>: represent DATA disk</li></ul></li></ul></li><li>project-id<ul><li>filter by cloud disk project id</li><li>type: String</li><li>required: no</li></ul></li><li>disk-id<ul><li>filter by cloud disk id. up to 10 values can be specified</li><li>type: String</li><li>required: no</li></ul></li><li>encrypt<ul><li>filter by whether encrypted or not</li><li>type: String</li><li>required: no</li></ul></li><li>snapshot-type<ul><li>query by snapshot ownership type</li><li>type: String</li><li>required: no</li><li>value ranges FROM:<ul><li><code>SHARED_snapshot</code>: refer to SHARED snapshot</li><li><code>PRIVATE_snapshot</code>: refer to own PRIVATE snapshot</li></ul></li></ul></li></ul>.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        r"""Field based on which the snapshot list is sorted. valid values:.
<ul>
<Li>CREATE_TIME: specifies to sort by snapshot creation time.</li>.
<Li>Sort by creation time by default.</li>.
</ul>
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Offset(self):
        r"""Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""Outputs the sorting order of the cloud disk list. valid values:.
<ul>
<Li>ASC: specifies ascending order.</li>.
<Li>DESC: specifies sorting in descending order.</li>.
</ul>

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
    r"""DescribeSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of snapshots.
        :type TotalCount: int
        :param _SnapshotSet: List of snapshot details.
        :type SnapshotSet: list of Snapshot
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SnapshotSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of snapshots.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SnapshotSet(self):
        r"""List of snapshot details.
        :rtype: list of Snapshot
        """
        return self._SnapshotSet

    @SnapshotSet.setter
    def SnapshotSet(self, SnapshotSet):
        self._SnapshotSet = SnapshotSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DetachDisksRequest(AbstractModel):
    r"""DetachDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: IDs of the cloud disks to be unmounted, which can be queried via the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API. Up to 10 elastic cloud disks can be unmounted in a single request.
        :type DiskIds: list of str
        :param _InstanceId: For non-shared cloud disks, this parameter validates whether it matches the actual mounted instance. for shared cloud disks, this parameter indicates from which CVM instance to unmount the cloud disk.
        :type InstanceId: str
        """
        self._DiskIds = None
        self._InstanceId = None

    @property
    def DiskIds(self):
        r"""IDs of the cloud disks to be unmounted, which can be queried via the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API. Up to 10 elastic cloud disks can be unmounted in a single request.
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def InstanceId(self):
        r"""For non-shared cloud disks, this parameter validates whether it matches the actual mounted instance. for shared cloud disks, this parameter indicates from which CVM instance to unmount the cloud disk.
        :rtype: str
        """
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
    r"""DetachDisks response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DetailPrice(AbstractModel):
    r"""Pricing details for the cloud disk.

    """

    def __init__(self):
        r"""
        :param _PriceTitle: Name of a billable item.
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
        r"""Name of a billable item.
        :rtype: str
        """
        return self._PriceTitle

    @PriceTitle.setter
    def PriceTitle(self, PriceTitle):
        self._PriceTitle = PriceTitle

    @property
    def PriceName(self):
        r"""Name of the billable item displayed in the console.
        :rtype: str
        """
        return self._PriceName

    @PriceName.setter
    def PriceName(self, PriceName):
        self._PriceName = PriceName

    @property
    def OriginalPrice(self):
        r"""Original price of a monthly subscribed cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        r"""Discounted price of a monthly subscribed cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def UnitPrice(self):
        r"""Original unit price of a pay-as-you-go cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        r"""Discount unit price of a pay-as-you-go cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def ChargeUnit(self):
        r"""Billing unit for pay-as-you-go cloud disks. Valid value: `HOUR` (billed hourly).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def OriginalPriceHigh(self):
        r"""Original highly-precise price of a monthly subscribed cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OriginalPriceHigh

    @OriginalPriceHigh.setter
    def OriginalPriceHigh(self, OriginalPriceHigh):
        self._OriginalPriceHigh = OriginalPriceHigh

    @property
    def DiscountPriceHigh(self):
        r"""Discounted highly-precise price of a monthly subscribed cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiscountPriceHigh

    @DiscountPriceHigh.setter
    def DiscountPriceHigh(self, DiscountPriceHigh):
        self._DiscountPriceHigh = DiscountPriceHigh

    @property
    def UnitPriceHigh(self):
        r"""Original highly-precise unit price of a pay-as-you-go cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UnitPriceHigh

    @UnitPriceHigh.setter
    def UnitPriceHigh(self, UnitPriceHigh):
        self._UnitPriceHigh = UnitPriceHigh

    @property
    def UnitPriceDiscountHigh(self):
        r"""Discounted highly-precise unit price of a pay-as-you-go cloud disk, in USD.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
    r"""The details of a cloud disk

    """

    def __init__(self):
        r"""
        :param _DeleteWithInstance: Specifies whether the cloud disk is destroyed along with the mounted instance.<br><li>true: destroy the cloud disk along with the instance. only hourly postpaid cloud disk is supported.</li><li>false: destroying instance without destroying cloud disk.</li>.
        :type DeleteWithInstance: bool
        :param _RenewFlag: AUTO renewal flag. supported values:<br><li>NOTIFY_AND_AUTO_RENEW: NOTIFY expiry AND RENEW automatically</li><li>NOTIFY_AND_MANUAL_RENEW: NOTIFY expiry but not RENEW automatically</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither NOTIFY expiry nor RENEW automatically.</li>.
        :type RenewFlag: str
        :param _DiskType: Hard disk media type. valid values:<br><li>CLOUD_BASIC: BASIC CLOUD disk</li><li>CLOUD_PREMIUM: high-performance CLOUD block storage</li><li>CLOUD_BSSD: universal type SSD CLOUD disk</li><li>CLOUD_SSD: SSD CLOUD disk</li><li>CLOUD_HSSD: enhanced SSD CLOUD disk</li><li>CLOUD_TSSD: ultra-fast SSD cbs.</li>.
        :type DiskType: str
        :param _DiskState: Cloud disk state. valid values:<br><li>UNATTACHED: unmounted</li><li>ATTACHING: mounting</li><li>ATTACHED: mounted</li><li>DETACHING: unmounting</li><li>EXPANDING: EXPANDING</li><li>ROLLBACKING: rolling back</li><li>TORECYCLE: to be recycled</li><li>DUMPING: copying hard drive.</li>.
        :type DiskState: str
        :param _SnapshotCount: The total number of snapshots of the cloud disk.
        :type SnapshotCount: int
        :param _AutoRenewFlagError: Cloud disk mounted to child machine, and both child machine and cloud disk are on a monthly subscription basis.<br><li>true: auto renewal flag is set for child machine, but cloud disk not set</li><li>false: cloud disk auto-renewal flag normal</li>.
        :type AutoRenewFlagError: bool
        :param _Rollbacking: Indicates if the cloud disk is in snapshot rollback status. valid values: <br><li>false: means not in snapshot rollback status</li><li>true: means in snapshot rollback status.</li>.
        :type Rollbacking: bool
        :param _InstanceIdList: For non-shareable cloud disks, this parameter is null. For shareable cloud disks, this parameters indicates this cloud disk's Instance IDs currently mounted to the CVM.
        :type InstanceIdList: list of str
        :param _Encrypt: Indicates whether the cloud disk is encrypted. valid values:<br><li>false: non-encrypted disk</li><li>true: encrypted disk</li>.
        :type Encrypt: bool
        :param _DiskName: Cloud disk name.
        :type DiskName: str
        :param _BackupDisk: Specifies whether to create a snapshot when the cloud disk is terminated due to overdue payment or expiration. `true`: create snapshot; `false`: do not create snapshot.
        :type BackupDisk: bool
        :param _Tags: It indicates the tag bound to the cloud disk. If the cloud disk is not bound to any tag, the value is empty.
        :type Tags: list of Tag
        :param _InstanceId: ID of the CVM to which the cloud disk is mounted.
        :type InstanceId: str
        :param _AttachMode: The mount type of the cloud disk. valid values: <br><li>PF: PF mount</li><li>VF: VF mount</li>.
        :type AttachMode: str
        :param _AutoSnapshotPolicyIds: Regular snapshot ID associated with the cloud disk. return this parameter only when calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API with ReturnBindAutoSnapshotPolicy set to TRUE.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoSnapshotPolicyIds: list of str
        :param _ThroughputPerformance: Specifies the additional performance value of the CBS in MiB/s.
        :type ThroughputPerformance: int
        :param _Migrating: Indicates if the cloud disk is in type change. valid values: <br><li>false: means the cloud disk is not in type change</li><li>true: means the cloud disk has initiated type change and is migrating.</li>.
        :type Migrating: bool
        :param _DiskId: Cloud disk ID.
        :type DiskId: str
        :param _SnapshotSize: Total snapshot capacity of the cloud disk. unit: MiB.
        :type SnapshotSize: int
        :param _Placement: Location of the cloud disk.
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param _IsReturnable: Determines if a prepaid cloud disk supports proactive return.<br><li>true: supports proactive return</li><li>false: does not support proactive return.</li>.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsReturnable: bool
        :param _DeadlineTime: Expiration time of the cloud disk.
        :type DeadlineTime: str
        :param _Attached: Indicates whether the cloud disk is mounted to the cvm. valid values: <br><li>false: means not mounted</li><li>true: means mounted.</li>.
        :type Attached: bool
        :param _DiskSize: Specifies the disk capacity in GiB.
        :type DiskSize: int
        :param _MigratePercent: It indicates the migration progress of cloud disk type change. The value range is 0 to 100.
        :type MigratePercent: int
        :param _DiskUsage: Cloud DISK type. valid values:<br><li>SYSTEM_DISK: SYSTEM DISK</li><li>DATA_DISK: DATA DISK.</li>.
        :type DiskUsage: str
        :param _DiskChargeType: Payment mode. valid values: <br><li>PREPAID: PREPAID, i.e. monthly subscription</li><li>POSTPAID_BY_HOUR: POSTPAID, i.e. pay-as-you-go.</li>.
        :type DiskChargeType: str
        :param _Portable: Whether it is an elastic cloud disk. false: Non-elastic cloud disk; true: Elastic cloud disk.
        :type Portable: bool
        :param _SnapshotAbility: Specifies whether the cloud disk has the capability to create snapshots. valid values:<br><li>false: cannot create snapshots</li><li>true: can create snapshots.</li>.
        :type SnapshotAbility: bool
        :param _DeadlineError: Indicates whether the cloud disk expiration time is earlier than that of the instance. this field is valid only when the cloud disk is mounted to the instance and both the instance and the cloud disk are on a monthly subscription basis.<br><li>true: the expiration time of the cloud disk is earlier than that of the instance.</li><li>false: cloud disk expiration time later than instance.</li>.
        :type DeadlineError: bool
        :param _RollbackPercent: Rollback progress of a cloud disk snapshot.
        :type RollbackPercent: int
        :param _DifferDaysOfDeadline: The number of days from the current time to disk expiration (only applicable to prepaid cbs).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DifferDaysOfDeadline: int
        :param _ReturnFailCode: For prepaid cloud disks that do not support proactive return, this parameter indicates the specific reason for not supporting refund. value range: <br><li>1: the cloud disk has already been returned.</li><li>2: the cloud disk has expired.</li><li>3: the cloud disk does not support return.</li><li>8: the maximum returnable quantity is exceeded.</li><li>10: non-elastic cloud disks, system disks, and pay-as-you-go cloud disks do not support return.</li>.
        :type ReturnFailCode: int
        :param _Shareable: Whether or not cloud disk is shareable cloud disk.
        :type Shareable: bool
        :param _CreateTime: Creation time of the cloud disk.
        :type CreateTime: str
        :param _DeleteSnapshot: Specifies whether to delete associated non-permanently retained snapshots when destroying the cloud disk. 0 indicates non-permanent snapshots are not deleted with cloud disk destruction, 1 indicates non-permanent snapshots are deleted with cloud disk destruction. default value: 0. whether a snapshot is permanently retained can be determined through the IsPermanent field in the snapshot description returned by the DescribeSnapshots API (https://www.tencentcloud.com/document/product/362/15647?from_cn_redirect=1). true indicates permanent snapshot, false indicates non-permanent snapshot.
        :type DeleteSnapshot: int
        :param _DiskBackupQuota: Quota of cloud disk backup points, i.e., the maximum number of backup points that a cloud disk can have.
        :type DiskBackupQuota: int
        :param _DiskBackupCount: Number of used cloud disk backups.
        :type DiskBackupCount: int
        :param _InstanceType: The type of the CBS mounting instance. valid values: <br><li>CVM</li><li>EKS</li>.
        :type InstanceType: str
        :param _LastAttachInsId: ID of the last instance to which the cloud disk is attached
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastAttachInsId: str
        :param _ErrorPrompt: Error prompt for the last operation on cbs.
        :type ErrorPrompt: str
        :param _BurstPerformance: Whether performance burst is enabled for the cloud disk.
        :type BurstPerformance: bool
        :param _EncryptType: Encryption type of cbs. valid values: ENCRYPT_V1 and ENCRYPT_V2, which indicate first generation and second generation encryption technology respectively. the two kinds are incompatible.
        :type EncryptType: str
        :param _KmsKeyId: Key ID of the encrypted disk.
        :type KmsKeyId: str
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
        self._EncryptType = None
        self._KmsKeyId = None

    @property
    def DeleteWithInstance(self):
        r"""Specifies whether the cloud disk is destroyed along with the mounted instance.<br><li>true: destroy the cloud disk along with the instance. only hourly postpaid cloud disk is supported.</li><li>false: destroying instance without destroying cloud disk.</li>.
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def RenewFlag(self):
        r"""AUTO renewal flag. supported values:<br><li>NOTIFY_AND_AUTO_RENEW: NOTIFY expiry AND RENEW automatically</li><li>NOTIFY_AND_MANUAL_RENEW: NOTIFY expiry but not RENEW automatically</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither NOTIFY expiry nor RENEW automatically.</li>.
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def DiskType(self):
        r"""Hard disk media type. valid values:<br><li>CLOUD_BASIC: BASIC CLOUD disk</li><li>CLOUD_PREMIUM: high-performance CLOUD block storage</li><li>CLOUD_BSSD: universal type SSD CLOUD disk</li><li>CLOUD_SSD: SSD CLOUD disk</li><li>CLOUD_HSSD: enhanced SSD CLOUD disk</li><li>CLOUD_TSSD: ultra-fast SSD cbs.</li>.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskState(self):
        r"""Cloud disk state. valid values:<br><li>UNATTACHED: unmounted</li><li>ATTACHING: mounting</li><li>ATTACHED: mounted</li><li>DETACHING: unmounting</li><li>EXPANDING: EXPANDING</li><li>ROLLBACKING: rolling back</li><li>TORECYCLE: to be recycled</li><li>DUMPING: copying hard drive.</li>.
        :rtype: str
        """
        return self._DiskState

    @DiskState.setter
    def DiskState(self, DiskState):
        self._DiskState = DiskState

    @property
    def SnapshotCount(self):
        r"""The total number of snapshots of the cloud disk.
        :rtype: int
        """
        return self._SnapshotCount

    @SnapshotCount.setter
    def SnapshotCount(self, SnapshotCount):
        self._SnapshotCount = SnapshotCount

    @property
    def AutoRenewFlagError(self):
        r"""Cloud disk mounted to child machine, and both child machine and cloud disk are on a monthly subscription basis.<br><li>true: auto renewal flag is set for child machine, but cloud disk not set</li><li>false: cloud disk auto-renewal flag normal</li>.
        :rtype: bool
        """
        return self._AutoRenewFlagError

    @AutoRenewFlagError.setter
    def AutoRenewFlagError(self, AutoRenewFlagError):
        self._AutoRenewFlagError = AutoRenewFlagError

    @property
    def Rollbacking(self):
        r"""Indicates if the cloud disk is in snapshot rollback status. valid values: <br><li>false: means not in snapshot rollback status</li><li>true: means in snapshot rollback status.</li>.
        :rtype: bool
        """
        return self._Rollbacking

    @Rollbacking.setter
    def Rollbacking(self, Rollbacking):
        self._Rollbacking = Rollbacking

    @property
    def InstanceIdList(self):
        r"""For non-shareable cloud disks, this parameter is null. For shareable cloud disks, this parameters indicates this cloud disk's Instance IDs currently mounted to the CVM.
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def Encrypt(self):
        r"""Indicates whether the cloud disk is encrypted. valid values:<br><li>false: non-encrypted disk</li><li>true: encrypted disk</li>.
        :rtype: bool
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def DiskName(self):
        r"""Cloud disk name.
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def BackupDisk(self):
        r"""Specifies whether to create a snapshot when the cloud disk is terminated due to overdue payment or expiration. `true`: create snapshot; `false`: do not create snapshot.
        :rtype: bool
        """
        return self._BackupDisk

    @BackupDisk.setter
    def BackupDisk(self, BackupDisk):
        self._BackupDisk = BackupDisk

    @property
    def Tags(self):
        r"""It indicates the tag bound to the cloud disk. If the cloud disk is not bound to any tag, the value is empty.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        r"""ID of the CVM to which the cloud disk is mounted.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AttachMode(self):
        r"""The mount type of the cloud disk. valid values: <br><li>PF: PF mount</li><li>VF: VF mount</li>.
        :rtype: str
        """
        return self._AttachMode

    @AttachMode.setter
    def AttachMode(self, AttachMode):
        self._AttachMode = AttachMode

    @property
    def AutoSnapshotPolicyIds(self):
        r"""Regular snapshot ID associated with the cloud disk. return this parameter only when calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API with ReturnBindAutoSnapshotPolicy set to TRUE.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AutoSnapshotPolicyIds

    @AutoSnapshotPolicyIds.setter
    def AutoSnapshotPolicyIds(self, AutoSnapshotPolicyIds):
        self._AutoSnapshotPolicyIds = AutoSnapshotPolicyIds

    @property
    def ThroughputPerformance(self):
        r"""Specifies the additional performance value of the CBS in MiB/s.
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def Migrating(self):
        r"""Indicates if the cloud disk is in type change. valid values: <br><li>false: means the cloud disk is not in type change</li><li>true: means the cloud disk has initiated type change and is migrating.</li>.
        :rtype: bool
        """
        return self._Migrating

    @Migrating.setter
    def Migrating(self, Migrating):
        self._Migrating = Migrating

    @property
    def DiskId(self):
        r"""Cloud disk ID.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def SnapshotSize(self):
        r"""Total snapshot capacity of the cloud disk. unit: MiB.
        :rtype: int
        """
        return self._SnapshotSize

    @SnapshotSize.setter
    def SnapshotSize(self, SnapshotSize):
        self._SnapshotSize = SnapshotSize

    @property
    def Placement(self):
        r"""Location of the cloud disk.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def IsReturnable(self):
        r"""Determines if a prepaid cloud disk supports proactive return.<br><li>true: supports proactive return</li><li>false: does not support proactive return.</li>.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsReturnable

    @IsReturnable.setter
    def IsReturnable(self, IsReturnable):
        self._IsReturnable = IsReturnable

    @property
    def DeadlineTime(self):
        r"""Expiration time of the cloud disk.
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Attached(self):
        r"""Indicates whether the cloud disk is mounted to the cvm. valid values: <br><li>false: means not mounted</li><li>true: means mounted.</li>.
        :rtype: bool
        """
        return self._Attached

    @Attached.setter
    def Attached(self, Attached):
        self._Attached = Attached

    @property
    def DiskSize(self):
        r"""Specifies the disk capacity in GiB.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MigratePercent(self):
        r"""It indicates the migration progress of cloud disk type change. The value range is 0 to 100.
        :rtype: int
        """
        return self._MigratePercent

    @MigratePercent.setter
    def MigratePercent(self, MigratePercent):
        self._MigratePercent = MigratePercent

    @property
    def DiskUsage(self):
        r"""Cloud DISK type. valid values:<br><li>SYSTEM_DISK: SYSTEM DISK</li><li>DATA_DISK: DATA DISK.</li>.
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskChargeType(self):
        r"""Payment mode. valid values: <br><li>PREPAID: PREPAID, i.e. monthly subscription</li><li>POSTPAID_BY_HOUR: POSTPAID, i.e. pay-as-you-go.</li>.
        :rtype: str
        """
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def Portable(self):
        r"""Whether it is an elastic cloud disk. false: Non-elastic cloud disk; true: Elastic cloud disk.
        :rtype: bool
        """
        return self._Portable

    @Portable.setter
    def Portable(self, Portable):
        self._Portable = Portable

    @property
    def SnapshotAbility(self):
        r"""Specifies whether the cloud disk has the capability to create snapshots. valid values:<br><li>false: cannot create snapshots</li><li>true: can create snapshots.</li>.
        :rtype: bool
        """
        return self._SnapshotAbility

    @SnapshotAbility.setter
    def SnapshotAbility(self, SnapshotAbility):
        self._SnapshotAbility = SnapshotAbility

    @property
    def DeadlineError(self):
        r"""Indicates whether the cloud disk expiration time is earlier than that of the instance. this field is valid only when the cloud disk is mounted to the instance and both the instance and the cloud disk are on a monthly subscription basis.<br><li>true: the expiration time of the cloud disk is earlier than that of the instance.</li><li>false: cloud disk expiration time later than instance.</li>.
        :rtype: bool
        """
        return self._DeadlineError

    @DeadlineError.setter
    def DeadlineError(self, DeadlineError):
        self._DeadlineError = DeadlineError

    @property
    def RollbackPercent(self):
        r"""Rollback progress of a cloud disk snapshot.
        :rtype: int
        """
        return self._RollbackPercent

    @RollbackPercent.setter
    def RollbackPercent(self, RollbackPercent):
        self._RollbackPercent = RollbackPercent

    @property
    def DifferDaysOfDeadline(self):
        r"""The number of days from the current time to disk expiration (only applicable to prepaid cbs).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DifferDaysOfDeadline

    @DifferDaysOfDeadline.setter
    def DifferDaysOfDeadline(self, DifferDaysOfDeadline):
        self._DifferDaysOfDeadline = DifferDaysOfDeadline

    @property
    def ReturnFailCode(self):
        r"""For prepaid cloud disks that do not support proactive return, this parameter indicates the specific reason for not supporting refund. value range: <br><li>1: the cloud disk has already been returned.</li><li>2: the cloud disk has expired.</li><li>3: the cloud disk does not support return.</li><li>8: the maximum returnable quantity is exceeded.</li><li>10: non-elastic cloud disks, system disks, and pay-as-you-go cloud disks do not support return.</li>.
        :rtype: int
        """
        return self._ReturnFailCode

    @ReturnFailCode.setter
    def ReturnFailCode(self, ReturnFailCode):
        self._ReturnFailCode = ReturnFailCode

    @property
    def Shareable(self):
        r"""Whether or not cloud disk is shareable cloud disk.
        :rtype: bool
        """
        return self._Shareable

    @Shareable.setter
    def Shareable(self, Shareable):
        self._Shareable = Shareable

    @property
    def CreateTime(self):
        r"""Creation time of the cloud disk.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeleteSnapshot(self):
        r"""Specifies whether to delete associated non-permanently retained snapshots when destroying the cloud disk. 0 indicates non-permanent snapshots are not deleted with cloud disk destruction, 1 indicates non-permanent snapshots are deleted with cloud disk destruction. default value: 0. whether a snapshot is permanently retained can be determined through the IsPermanent field in the snapshot description returned by the DescribeSnapshots API (https://www.tencentcloud.com/document/product/362/15647?from_cn_redirect=1). true indicates permanent snapshot, false indicates non-permanent snapshot.
        :rtype: int
        """
        return self._DeleteSnapshot

    @DeleteSnapshot.setter
    def DeleteSnapshot(self, DeleteSnapshot):
        self._DeleteSnapshot = DeleteSnapshot

    @property
    def DiskBackupQuota(self):
        r"""Quota of cloud disk backup points, i.e., the maximum number of backup points that a cloud disk can have.
        :rtype: int
        """
        return self._DiskBackupQuota

    @DiskBackupQuota.setter
    def DiskBackupQuota(self, DiskBackupQuota):
        self._DiskBackupQuota = DiskBackupQuota

    @property
    def DiskBackupCount(self):
        r"""Number of used cloud disk backups.
        :rtype: int
        """
        return self._DiskBackupCount

    @DiskBackupCount.setter
    def DiskBackupCount(self, DiskBackupCount):
        self._DiskBackupCount = DiskBackupCount

    @property
    def InstanceType(self):
        r"""The type of the CBS mounting instance. valid values: <br><li>CVM</li><li>EKS</li>.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def LastAttachInsId(self):
        r"""ID of the last instance to which the cloud disk is attached
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastAttachInsId

    @LastAttachInsId.setter
    def LastAttachInsId(self, LastAttachInsId):
        self._LastAttachInsId = LastAttachInsId

    @property
    def ErrorPrompt(self):
        r"""Error prompt for the last operation on cbs.
        :rtype: str
        """
        return self._ErrorPrompt

    @ErrorPrompt.setter
    def ErrorPrompt(self, ErrorPrompt):
        self._ErrorPrompt = ErrorPrompt

    @property
    def BurstPerformance(self):
        r"""Whether performance burst is enabled for the cloud disk.
        :rtype: bool
        """
        return self._BurstPerformance

    @BurstPerformance.setter
    def BurstPerformance(self, BurstPerformance):
        self._BurstPerformance = BurstPerformance

    @property
    def EncryptType(self):
        r"""Encryption type of cbs. valid values: ENCRYPT_V1 and ENCRYPT_V2, which indicate first generation and second generation encryption technology respectively. the two kinds are incompatible.
        :rtype: str
        """
        return self._EncryptType

    @EncryptType.setter
    def EncryptType(self, EncryptType):
        self._EncryptType = EncryptType

    @property
    def KmsKeyId(self):
        r"""Key ID of the encrypted disk.
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId


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
        self._EncryptType = params.get("EncryptType")
        self._KmsKeyId = params.get("KmsKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskBackup(AbstractModel):
    r"""Cloud disk backup point.

    """

    def __init__(self):
        r"""
        :param _DiskBackupId: Cloud disk backup point ID.
        :type DiskBackupId: str
        :param _DiskId: ID of the cloud disk with which the backup point is associated.
        :type DiskId: str
        :param _DiskSize: Specifies the disk capacity in GiB.
        :type DiskSize: int
        :param _DiskUsage: Cloud disk type. value ranges from...to...<br>.
<Li>SYSTEM_DISK: specifies the system disk.</li>.
<Li>DATA_DISK: specifies the data disk.</li>.
        :type DiskUsage: str
        :param _DiskBackupName: Backup point name.
        :type DiskBackupName: str
        :param _DiskBackupState: <P>Specifies the status of the cloud disk backup point. valid values:</p>.
<ul>
<Li>NORMAL: specifies the scaling group is in normal state.</li>.
<Li>CREATING: creating.</li>.
<Li>ROLLBACKING: indicates the rollback is in progress.</li>.
</ul>
        :type DiskBackupState: str
        :param _Percent: Specifies the creation percentage of the cloud disk backup point.
        :type Percent: int
        :param _CreateTime: Creation time of the cloud disk backup point.
        :type CreateTime: str
        :param _Encrypt: Indicates whether the cloud disk is encrypted. valid values:<br><li>false: non-encrypted disk</li><li>true: encrypted disk</li>.
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
        r"""Cloud disk backup point ID.
        :rtype: str
        """
        return self._DiskBackupId

    @DiskBackupId.setter
    def DiskBackupId(self, DiskBackupId):
        self._DiskBackupId = DiskBackupId

    @property
    def DiskId(self):
        r"""ID of the cloud disk with which the backup point is associated.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        r"""Specifies the disk capacity in GiB.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskUsage(self):
        r"""Cloud disk type. value ranges from...to...<br>.
<Li>SYSTEM_DISK: specifies the system disk.</li>.
<Li>DATA_DISK: specifies the data disk.</li>.
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskBackupName(self):
        r"""Backup point name.
        :rtype: str
        """
        return self._DiskBackupName

    @DiskBackupName.setter
    def DiskBackupName(self, DiskBackupName):
        self._DiskBackupName = DiskBackupName

    @property
    def DiskBackupState(self):
        r"""<P>Specifies the status of the cloud disk backup point. valid values:</p>.
<ul>
<Li>NORMAL: specifies the scaling group is in normal state.</li>.
<Li>CREATING: creating.</li>.
<Li>ROLLBACKING: indicates the rollback is in progress.</li>.
</ul>
        :rtype: str
        """
        return self._DiskBackupState

    @DiskBackupState.setter
    def DiskBackupState(self, DiskBackupState):
        self._DiskBackupState = DiskBackupState

    @property
    def Percent(self):
        r"""Specifies the creation percentage of the cloud disk backup point.
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def CreateTime(self):
        r"""Creation time of the cloud disk backup point.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Encrypt(self):
        r"""Indicates whether the cloud disk is encrypted. valid values:<br><li>false: non-encrypted disk</li><li>true: encrypted disk</li>.
        :rtype: bool
        """
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
    r"""Billing mode of the instance

    """

    def __init__(self):
        r"""
        :param _Period: Specifies the duration for purchasing cloud block storage (cbs) in months. default unit: month. valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param _RenewFlag: Automatic renewal flag. valid values:.
<ul>
<Li>NOTIFY_AND_AUTO_RENEW: notifies expiry and renews automatically.</li>.
<Li>NOTIFY_AND_MANUAL_RENEW: notifies expiry but does not renew automatically.</li>.
<Li>DISABLE_NOTIFY_AND_MANUAL_RENEW: no notification is sent upon expiration, and the instance is not renewed automatically.</li>.
</ul>
Default value: NOTIFY_AND_MANUAL_RENEW.
        :type RenewFlag: str
        :param _CurInstanceDeadline: Specifies the current expiration time of the child machine when the expiration time of the cloud block storage needs to align with the mounted child machine. you can input this parameter. if Period is input at this time, it indicates the duration of child machine renewal. the cloud disk will automatically renew according to the expiration time after the child machine is renewed.
        :type CurInstanceDeadline: str
        """
        self._Period = None
        self._RenewFlag = None
        self._CurInstanceDeadline = None

    @property
    def Period(self):
        r"""Specifies the duration for purchasing cloud block storage (cbs) in months. default unit: month. valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        r"""Automatic renewal flag. valid values:.
<ul>
<Li>NOTIFY_AND_AUTO_RENEW: notifies expiry and renews automatically.</li>.
<Li>NOTIFY_AND_MANUAL_RENEW: notifies expiry but does not renew automatically.</li>.
<Li>DISABLE_NOTIFY_AND_MANUAL_RENEW: no notification is sent upon expiration, and the instance is not renewed automatically.</li>.
</ul>
Default value: NOTIFY_AND_MANUAL_RENEW.
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def CurInstanceDeadline(self):
        r"""Specifies the current expiration time of the child machine when the expiration time of the cloud block storage needs to align with the mounted child machine. you can input this parameter. if Period is input at this time, it indicates the duration of child machine renewal. the cloud disk will automatically renew according to the expiration time after the child machine is renewed.
        :rtype: str
        """
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
    r"""Cloud disk configuration.

    """

    def __init__(self):
        r"""
        :param _Available: Whether the configuration is available.
        :type Available: bool
        :param _DiskChargeType: Payment mode. valid values: <br><li>PREPAID: PREPAID, i.e. monthly subscription</li><br><li>POSTPAID_BY_HOUR: POSTPAID, i.e. pay-as-you-go.</li>.
        :type DiskChargeType: str
        :param _Zone: The [Availability Region](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) of the cloud drive.
        :type Zone: str
        :param _InstanceFamily: Instance model series. For more information, please see [Instance Models](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1)
Note: This field may return null, indicating that no valid value was found.
        :type InstanceFamily: str
        :param _DiskType: Cloud disk media type. valid values: <br>.
CLOUD_BASIC: specifies the BASIC CLOUD disk.
CLOUD_PREMIUM: indicates high-performance CLOUD block storage.
CLOUD_BSSD: indicates a universal type SSD CLOUD disk.
CLOUD_SSD: indicates SSD CLOUD disk.
CLOUD_HSSD: indicates the enhanced SSD CLOUD disk.
CLOUD_TSSD: indicates ultra-fast ssd cbs.
        :type DiskType: str
        :param _StepSize: Specifies the minimum step size for disk size change in GiB.
        :type StepSize: int
        :param _ExtraPerformanceRange: Additional performance range.
Note: This field might return null, indicating that no valid values can be obtained.
        :type ExtraPerformanceRange: list of int
        :param _DeviceClass: Instance model.
Note: This field may return null, indicating that no valid value was found.
        :type DeviceClass: str
        :param _DiskUsage: Cloud DISK type. valid values:<br><li>SYSTEM_DISK: SYSTEM DISK</li><br><li>DATA_DISK: DATA DISK.</li>.
        :type DiskUsage: str
        :param _MinDiskSize: Specifies the minimum configurable cloud disk size in GiB.
        :type MinDiskSize: int
        :param _MaxDiskSize: Specifies the maximum configurable cloud disk size in GiB.
        :type MaxDiskSize: int
        :param _Price: Price of a prepaid or postpaid cloud disk.
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
        r"""Whether the configuration is available.
        :rtype: bool
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def DiskChargeType(self):
        r"""Payment mode. valid values: <br><li>PREPAID: PREPAID, i.e. monthly subscription</li><br><li>POSTPAID_BY_HOUR: POSTPAID, i.e. pay-as-you-go.</li>.
        :rtype: str
        """
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def Zone(self):
        r"""The [Availability Region](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) of the cloud drive.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceFamily(self):
        r"""Instance model series. For more information, please see [Instance Models](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1)
Note: This field may return null, indicating that no valid value was found.
        :rtype: str
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def DiskType(self):
        r"""Cloud disk media type. valid values: <br>.
CLOUD_BASIC: specifies the BASIC CLOUD disk.
CLOUD_PREMIUM: indicates high-performance CLOUD block storage.
CLOUD_BSSD: indicates a universal type SSD CLOUD disk.
CLOUD_SSD: indicates SSD CLOUD disk.
CLOUD_HSSD: indicates the enhanced SSD CLOUD disk.
CLOUD_TSSD: indicates ultra-fast ssd cbs.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def StepSize(self):
        r"""Specifies the minimum step size for disk size change in GiB.
        :rtype: int
        """
        return self._StepSize

    @StepSize.setter
    def StepSize(self, StepSize):
        self._StepSize = StepSize

    @property
    def ExtraPerformanceRange(self):
        r"""Additional performance range.
Note: This field might return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._ExtraPerformanceRange

    @ExtraPerformanceRange.setter
    def ExtraPerformanceRange(self, ExtraPerformanceRange):
        self._ExtraPerformanceRange = ExtraPerformanceRange

    @property
    def DeviceClass(self):
        r"""Instance model.
Note: This field may return null, indicating that no valid value was found.
        :rtype: str
        """
        return self._DeviceClass

    @DeviceClass.setter
    def DeviceClass(self, DeviceClass):
        self._DeviceClass = DeviceClass

    @property
    def DiskUsage(self):
        r"""Cloud DISK type. valid values:<br><li>SYSTEM_DISK: SYSTEM DISK</li><br><li>DATA_DISK: DATA DISK.</li>.
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def MinDiskSize(self):
        r"""Specifies the minimum configurable cloud disk size in GiB.
        :rtype: int
        """
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def MaxDiskSize(self):
        r"""Specifies the maximum configurable cloud disk size in GiB.
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def Price(self):
        r"""Price of a prepaid or postpaid cloud disk.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.Price`
        """
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
        


class Filter(AbstractModel):
    r"""Filter criteria

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
        r"""Name of filter key.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""One or more filter values.
        :rtype: list of str
        """
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
    r"""GetSnapOverview request structure.

    """


class GetSnapOverviewResponse(AbstractModel):
    r"""GetSnapOverview response structure.

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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalSize = None
        self._RealTradeSize = None
        self._FreeQuota = None
        self._TotalNums = None
        self._RequestId = None

    @property
    def TotalSize(self):
        r"""The total snapshot size of the user
        :rtype: float
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def RealTradeSize(self):
        r"""The total billed snapshot size of the user
        :rtype: float
        """
        return self._RealTradeSize

    @RealTradeSize.setter
    def RealTradeSize(self, RealTradeSize):
        self._RealTradeSize = RealTradeSize

    @property
    def FreeQuota(self):
        r"""Free tier of snapshot
        :rtype: float
        """
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def TotalNums(self):
        r"""Total number of snapshots
        :rtype: int
        """
        return self._TotalNums

    @TotalNums.setter
    def TotalNums(self, TotalNums):
        self._TotalNums = TotalNums

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""Image

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
        r"""Image instance ID.
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        r"""Image name.
        :rtype: str
        """
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
    r"""InitializeDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk ids to be reinitialized. can be accessed through the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. the initialization is limited to not exceeding 20 disks.
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        r"""List of cloud disk ids to be reinitialized. can be accessed through the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. the initialization is limited to not exceeding 20 disks.
        :rtype: list of str
        """
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
    r"""InitializeDisks response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class InquirePriceModifyDiskBackupQuotaRequest(AbstractModel):
    r"""InquirePriceModifyDiskBackupQuota request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: Cloud disk ID, which can be queried by calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskId: str
        :param _DiskBackupQuota: Cloud disk backup point quota after the modification, i.e., the number of backup points that a cloud disk can have.
        :type DiskBackupQuota: int
        """
        self._DiskId = None
        self._DiskBackupQuota = None

    @property
    def DiskId(self):
        r"""Cloud disk ID, which can be queried by calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupQuota(self):
        r"""Cloud disk backup point quota after the modification, i.e., the number of backup points that a cloud disk can have.
        :rtype: int
        """
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
    r"""InquirePriceModifyDiskBackupQuota response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: Price of the cloud disk after its backup point quota is modified.
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        r"""Price of the cloud disk after its backup point quota is modified.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.Price`
        """
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""InquirePriceModifyDiskExtraPerformance request structure.

    """

    def __init__(self):
        r"""
        :param _ThroughputPerformance: Specifies the additional performance value of the CBS disk in MiB/s. extra performance is only supported for enhanced SSD (CLOUD_HSSD) and ultra-fast SSD (CLOUD_TSSD) CBS disks exceeding 460GiB in size.
        :type ThroughputPerformance: int
        :param _DiskId: Cloud disk ID, which can be queried via the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskId: str
        """
        self._ThroughputPerformance = None
        self._DiskId = None

    @property
    def ThroughputPerformance(self):
        r"""Specifies the additional performance value of the CBS disk in MiB/s. extra performance is only supported for enhanced SSD (CLOUD_HSSD) and ultra-fast SSD (CLOUD_TSSD) CBS disks exceeding 460GiB in size.
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def DiskId(self):
        r"""Cloud disk ID, which can be queried via the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDiskExtraPerformanceResponse(AbstractModel):
    r"""InquirePriceModifyDiskExtraPerformance response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: Price for purchasing the extra performance
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        r"""Price for purchasing the extra performance
        :rtype: :class:`tencentcloud.cbs.v20170312.models.Price`
        """
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""InquiryPriceCreateDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskChargeType: Cloud disk billing mode. <br>
<li>PREPAID: Prepaid by month.</li>
<li>POSTPAID_BY_HOUR: Hourly pay-as-you-go.</li>
        :type DiskChargeType: str
        :param _DiskType: Hard disk media type. valid values: <ul> <li>CLOUD_PREMIUM: high-performance CLOUD block storage</li> <li>CLOUD_SSD: SSD CLOUD disk</li> <li>CLOUD_HSSD: enhanced SSD CLOUD disk</li> <li>CLOUD_TSSD: ultra-fast SSD cbs</li> </ul>.
        :type DiskType: str
        :param _DiskSize: Specifies the disk capacity in GiB. for the cloud disk size range, please refer to the product type of cloud block storage (https://www.tencentcloud.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        :param _ProjectId: cloud disk project ID. obtain this parameter by calling the projectId field in the return value of [DescribeProject](https://www.tencentcloud.com/document/api/651/78725?from_cn_redirect=1). default to the default project.
        :type ProjectId: int
        :param _DiskCount: Specifies the number of cloud block storage (cbs) disks to purchase. defaults to 1 if left blank.
        :type DiskCount: int
        :param _ThroughputPerformance: Specifies the additional performance value of the CBS disk in MiB/s. extra performance is only supported for enhanced SSD (CLOUD_HSSD) and ultra-fast SSD (CLOUD_TSSD) CBS disks exceeding 460GiB in size.
        :type ThroughputPerformance: int
        :param _DiskChargePrepaid: Prepaid mode, that is, the settings for the monthly subscription-related parameters. through this parameter, you can specify the purchase duration of the monthly subscribed cloud disk, whether to enable auto-renewal, and other attributes. this parameter is required for creating a prepaid cloud disk, but no need to specify it when creating an hourly postpaid cloud disk.
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
        r"""Cloud disk billing mode. <br>
<li>PREPAID: Prepaid by month.</li>
<li>POSTPAID_BY_HOUR: Hourly pay-as-you-go.</li>
        :rtype: str
        """
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def DiskType(self):
        r"""Hard disk media type. valid values: <ul> <li>CLOUD_PREMIUM: high-performance CLOUD block storage</li> <li>CLOUD_SSD: SSD CLOUD disk</li> <li>CLOUD_HSSD: enhanced SSD CLOUD disk</li> <li>CLOUD_TSSD: ultra-fast SSD cbs</li> </ul>.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""Specifies the disk capacity in GiB. for the cloud disk size range, please refer to the product type of cloud block storage (https://www.tencentcloud.com/document/product/362/2353?from_cn_redirect=1).
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ProjectId(self):
        r"""cloud disk project ID. obtain this parameter by calling the projectId field in the return value of [DescribeProject](https://www.tencentcloud.com/document/api/651/78725?from_cn_redirect=1). default to the default project.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DiskCount(self):
        r"""Specifies the number of cloud block storage (cbs) disks to purchase. defaults to 1 if left blank.
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def ThroughputPerformance(self):
        r"""Specifies the additional performance value of the CBS disk in MiB/s. extra performance is only supported for enhanced SSD (CLOUD_HSSD) and ultra-fast SSD (CLOUD_TSSD) CBS disks exceeding 460GiB in size.
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def DiskChargePrepaid(self):
        r"""Prepaid mode, that is, the settings for the monthly subscription-related parameters. through this parameter, you can specify the purchase duration of the monthly subscribed cloud disk, whether to enable auto-renewal, and other attributes. this parameter is required for creating a prepaid cloud disk, but no need to specify it when creating an hourly postpaid cloud disk.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        """
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DiskBackupQuota(self):
        r"""Specifies the cloud disk backup point quota.
        :rtype: int
        """
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
    r"""InquiryPriceCreateDisks response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: Describes the price of newly purchased cloud disks.
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        r"""Describes the price of newly purchased cloud disks.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.Price`
        """
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = Price()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewDisksRequest(AbstractModel):
    r"""InquiryPriceRenewDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: Cloud disk ID, which can be queried by calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskIds: list of str
        :param _DiskChargePrepaids: Prepaid mode, that is, settings related to the monthly subscription. Through this parameter, you can specify the purchase duration of the monthly subscribed cloud disk. If CurInstanceDeadline is specified in this parameter, it will be renewed in aligned with the sub-machine expiration time. If it is a batch renewal inquiry, this parameter corresponds one-to-one with the Disks parameter, and the number of Element (XML) must be consistent.
        :type DiskChargePrepaids: list of DiskChargePrepaid
        :param _NewDeadline: Specifies the new expiry time of the CBS in the format such as 2017-12-17 00:00:00. parameter `NewDeadline` and `DiskChargePrepaids` are two ways to specify inquiry duration. one of them must be input.
        :type NewDeadline: str
        :param _ProjectId: cloud disk project ID. obtain this parameter by calling the projectId field in the return value of [DescribeProject](https://www.tencentcloud.com/document/api/651/78725?from_cn_redirect=1). if input, it is only for authentication.
        :type ProjectId: int
        """
        self._DiskIds = None
        self._DiskChargePrepaids = None
        self._NewDeadline = None
        self._ProjectId = None

    @property
    def DiskIds(self):
        r"""Cloud disk ID, which can be queried by calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API.
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskChargePrepaids(self):
        r"""Prepaid mode, that is, settings related to the monthly subscription. Through this parameter, you can specify the purchase duration of the monthly subscribed cloud disk. If CurInstanceDeadline is specified in this parameter, it will be renewed in aligned with the sub-machine expiration time. If it is a batch renewal inquiry, this parameter corresponds one-to-one with the Disks parameter, and the number of Element (XML) must be consistent.
        :rtype: list of DiskChargePrepaid
        """
        return self._DiskChargePrepaids

    @DiskChargePrepaids.setter
    def DiskChargePrepaids(self, DiskChargePrepaids):
        self._DiskChargePrepaids = DiskChargePrepaids

    @property
    def NewDeadline(self):
        r"""Specifies the new expiry time of the CBS in the format such as 2017-12-17 00:00:00. parameter `NewDeadline` and `DiskChargePrepaids` are two ways to specify inquiry duration. one of them must be input.
        :rtype: str
        """
        return self._NewDeadline

    @NewDeadline.setter
    def NewDeadline(self, NewDeadline):
        self._NewDeadline = NewDeadline

    @property
    def ProjectId(self):
        r"""cloud disk project ID. obtain this parameter by calling the projectId field in the return value of [DescribeProject](https://www.tencentcloud.com/document/api/651/78725?from_cn_redirect=1). if input, it is only for authentication.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        if params.get("DiskChargePrepaids") is not None:
            self._DiskChargePrepaids = []
            for item in params.get("DiskChargePrepaids"):
                obj = DiskChargePrepaid()
                obj._deserialize(item)
                self._DiskChargePrepaids.append(obj)
        self._NewDeadline = params.get("NewDeadline")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewDisksResponse(AbstractModel):
    r"""InquiryPriceRenewDisks response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: It describes the price of renewing cloud disks.
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        r"""It describes the price of renewing cloud disks.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        """
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self._DiskPrice = PrepayPrice()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResizeDiskRequest(AbstractModel):
    r"""InquiryPriceResizeDisk request structure.

    """

    def __init__(self):
        r"""
        :param _DiskSize: Specifies the size after expanding the cloud disk in GiB, which should not be less than the current disk size. for the cloud disk size range, please refer to the product type of CBS (https://www.tencentcloud.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        :param _DiskId: Cloud disk ID. can be queried via the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. mutually exclusive with the DiskIds parameter.
        :type DiskId: str
        :param _ProjectId: cloud disk project ID. obtain this parameter by calling the projectId field in the return value of [DescribeProject](https://www.tencentcloud.com/document/api/651/78725?from_cn_redirect=1). if input, it is only for authentication.
        :type ProjectId: int
        :param _DiskIds: Cloud disk ID list. queried via the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. mutually exclusive with the DiskId parameter.
        :type DiskIds: list of str
        """
        self._DiskSize = None
        self._DiskId = None
        self._ProjectId = None
        self._DiskIds = None

    @property
    def DiskSize(self):
        r"""Specifies the size after expanding the cloud disk in GiB, which should not be less than the current disk size. for the cloud disk size range, please refer to the product type of CBS (https://www.tencentcloud.com/document/product/362/2353?from_cn_redirect=1).
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        r"""Cloud disk ID. can be queried via the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. mutually exclusive with the DiskIds parameter.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def ProjectId(self):
        r"""cloud disk project ID. obtain this parameter by calling the projectId field in the return value of [DescribeProject](https://www.tencentcloud.com/document/api/651/78725?from_cn_redirect=1). if input, it is only for authentication.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DiskIds(self):
        r"""Cloud disk ID list. queried via the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. mutually exclusive with the DiskId parameter.
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskId = params.get("DiskId")
        self._ProjectId = params.get("ProjectId")
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResizeDiskResponse(AbstractModel):
    r"""InquiryPriceResizeDisk response structure.

    """

    def __init__(self):
        r"""
        :param _DiskPrice: Describes the price of expanding the cloud disk.
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DiskPrice = None
        self._RequestId = None

    @property
    def DiskPrice(self):
        r"""Describes the price of expanding the cloud disk.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        """
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""ModifyAutoSnapshotPolicyAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: Specifies the scheduled snapshot policy ID. query via the describeautosnapshotpolicies API (https://www.tencentcloud.com/document/product/362/33556?from_cn_redirect=1).
        :type AutoSnapshotPolicyId: str
        :param _IsActivated: Whether the periodic snapshot policy is activated. `false` means inactive, `true` means active. defaults to `true`.
        :type IsActivated: bool
        :param _IsPermanent: Indicates whether snapshots created by the regular snapshot policy are retained permanently. `false` means the snapshots are not retained permanently, `true` means permanent retention. defaults to `false`.
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
        r"""Specifies the scheduled snapshot policy ID. query via the describeautosnapshotpolicies API (https://www.tencentcloud.com/document/product/362/33556?from_cn_redirect=1).
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def IsActivated(self):
        r"""Whether the periodic snapshot policy is activated. `false` means inactive, `true` means active. defaults to `true`.
        :rtype: bool
        """
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def IsPermanent(self):
        r"""Indicates whether snapshots created by the regular snapshot policy are retained permanently. `false` means the snapshots are not retained permanently, `true` means permanent retention. defaults to `false`.
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def AutoSnapshotPolicyName(self):
        r"""The name of the scheduled snapshot policy to be created. If it is left empty, the default is 'Not named'. The maximum length cannot exceed 60 bytes.
        :rtype: str
        """
        return self._AutoSnapshotPolicyName

    @AutoSnapshotPolicyName.setter
    def AutoSnapshotPolicyName(self, AutoSnapshotPolicyName):
        self._AutoSnapshotPolicyName = AutoSnapshotPolicyName

    @property
    def Policy(self):
        r"""The policy for executing the scheduled snapshot.
        :rtype: list of Policy
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def RetentionDays(self):
        r"""Number of days to retain the snapshots created according to this scheduled snapshot policy. If this parameter is specified, `IsPermanent` cannot be specified as `TRUE`; otherwise, they will conflict with each other.
        :rtype: int
        """
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
    r"""ModifyAutoSnapshotPolicyAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDiskAttributesRequest(AbstractModel):
    r"""ModifyDiskAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: One or more cloud disk ids to be operated, which can be queried through the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. if multiple cloud disk ids are passed in, only modifying all cloud disks to the same attribute is supported.

        :type DiskIds: list of str
        :param _DiskName: Name of new cloud disk.
        :type DiskName: str
        :param _Portable: Whether it is an elastic cloud disk. FALSE: non-elastic cloud disk; TRUE: elastic cloud disk. You can only modify non-elastic cloud disks to elastic cloud disks.
        :type Portable: bool
        :param _ProjectId: The new project ID of the cloud disk. Only the project ID of elastic cloud disk can be modified. The available projects and their IDs can be queried via the API [DescribeProject](https://www.tencentcloud.com/document/api/651/54679).
        :type ProjectId: int
        :param _DeleteWithInstance: Whether the cloud disk is terminated with the CVM after it has been successfully mounted. `TRUE` indicates that it is terminated with the CVM. `FALSE` indicates that it is not terminated with the CVM. This is only supported for cloud disks and data disks that are pay-as-you-go.
        :type DeleteWithInstance: bool
        :param _DiskType: When changing the CLOUD disk type, you can input this parameter to indicate the target type. valid values:<br><li>CLOUD_PREMIUM: refers to high-performance CLOUD block storage</li><li>CLOUD_SSD: refers to SSD CLOUD disk.</li>batch type change is not supported. when inputting DiskType, DiskIds only supports entering one CLOUD disk id.<br>changing the CLOUD disk type does not support changing other attributes at the same time.
For details, see [adjust cloud disk type](https://www.tencentcloud.com/document/product/362/32540?from_cn_redirect=1).
        :type DiskType: str
        :param _BurstPerformanceOperation: Enable/Disable cloud disk performance burst feature. valid values:. 
CREATE: enable.
Specifies to CANCEL and close.
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
        r"""One or more cloud disk ids to be operated, which can be queried through the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. if multiple cloud disk ids are passed in, only modifying all cloud disks to the same attribute is supported.

        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DiskName(self):
        r"""Name of new cloud disk.
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def Portable(self):
        r"""Whether it is an elastic cloud disk. FALSE: non-elastic cloud disk; TRUE: elastic cloud disk. You can only modify non-elastic cloud disks to elastic cloud disks.
        :rtype: bool
        """
        return self._Portable

    @Portable.setter
    def Portable(self, Portable):
        self._Portable = Portable

    @property
    def ProjectId(self):
        r"""The new project ID of the cloud disk. Only the project ID of elastic cloud disk can be modified. The available projects and their IDs can be queried via the API [DescribeProject](https://www.tencentcloud.com/document/api/651/54679).
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeleteWithInstance(self):
        r"""Whether the cloud disk is terminated with the CVM after it has been successfully mounted. `TRUE` indicates that it is terminated with the CVM. `FALSE` indicates that it is not terminated with the CVM. This is only supported for cloud disks and data disks that are pay-as-you-go.
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def DiskType(self):
        r"""When changing the CLOUD disk type, you can input this parameter to indicate the target type. valid values:<br><li>CLOUD_PREMIUM: refers to high-performance CLOUD block storage</li><li>CLOUD_SSD: refers to SSD CLOUD disk.</li>batch type change is not supported. when inputting DiskType, DiskIds only supports entering one CLOUD disk id.<br>changing the CLOUD disk type does not support changing other attributes at the same time.
For details, see [adjust cloud disk type](https://www.tencentcloud.com/document/product/362/32540?from_cn_redirect=1).
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def BurstPerformanceOperation(self):
        r"""Enable/Disable cloud disk performance burst feature. valid values:. 
CREATE: enable.
Specifies to CANCEL and close.
        :rtype: str
        """
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
    r"""ModifyDiskAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDiskBackupQuotaRequest(AbstractModel):
    r"""ModifyDiskBackupQuota request structure.

    """

    def __init__(self):
        r"""
        :param _DiskId: Cloud disk ID. can be queried via the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api.
        :type DiskId: str
        :param _DiskBackupQuota: Adjusted cloud disk backup point quota. value range: 1-1024.
        :type DiskBackupQuota: int
        """
        self._DiskId = None
        self._DiskBackupQuota = None

    @property
    def DiskId(self):
        r"""Cloud disk ID. can be queried via the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskBackupQuota(self):
        r"""Adjusted cloud disk backup point quota. value range: 1-1024.
        :rtype: int
        """
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
    r"""ModifyDiskBackupQuota response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDiskExtraPerformanceRequest(AbstractModel):
    r"""ModifyDiskExtraPerformance request structure.

    """

    def __init__(self):
        r"""
        :param _ThroughputPerformance: Specifies the hard disk performance of the additional CBS purchase in MiB/s.
        :type ThroughputPerformance: int
        :param _DiskId: The CLOUD disk ID for which extra performance needs to be purchased. it can be queried via the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. extra performance is only supported for enhanced SSD (CLOUD_HSSD) and ultra-fast SSD (CLOUD_TSSD) CBS disks exceeding 460GiB in size.
        :type DiskId: str
        """
        self._ThroughputPerformance = None
        self._DiskId = None

    @property
    def ThroughputPerformance(self):
        r"""Specifies the hard disk performance of the additional CBS purchase in MiB/s.
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def DiskId(self):
        r"""The CLOUD disk ID for which extra performance needs to be purchased. it can be queried via the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. extra performance is only supported for enhanced SSD (CLOUD_HSSD) and ultra-fast SSD (CLOUD_TSSD) CBS disks exceeding 460GiB in size.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskExtraPerformanceResponse(AbstractModel):
    r"""ModifyDiskExtraPerformance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySnapshotAttributeRequest(AbstractModel):
    r"""ModifySnapshotAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotId: Snapshot ID. can be queried via DescribeSnapshots (https://www.tencentcloud.com/document/api/362/15647?from_cn_redirect=1).
        :type SnapshotId: str
        :param _IsPermanent: Snapshot retention mode. Valid values: `FALSE`: non-permanent retention; `TRUE`: permanent retention.
        :type IsPermanent: bool
        :param _SnapshotName: Name of new snapshot. Maximum length is 60 bytes.
        :type SnapshotName: str
        :param _Deadline: Specifies the snapshot expiration time. the snapshot will be simultaneously set to the non-permanent retention method. snapshots exceeding the expiry time will be automatically deleted. note: this parameter is valid only when IsPermanent is False.
        :type Deadline: str
        """
        self._SnapshotId = None
        self._IsPermanent = None
        self._SnapshotName = None
        self._Deadline = None

    @property
    def SnapshotId(self):
        r"""Snapshot ID. can be queried via DescribeSnapshots (https://www.tencentcloud.com/document/api/362/15647?from_cn_redirect=1).
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def IsPermanent(self):
        r"""Snapshot retention mode. Valid values: `FALSE`: non-permanent retention; `TRUE`: permanent retention.
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def SnapshotName(self):
        r"""Name of new snapshot. Maximum length is 60 bytes.
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Deadline(self):
        r"""Specifies the snapshot expiration time. the snapshot will be simultaneously set to the non-permanent retention method. snapshots exceeding the expiry time will be automatically deleted. note: this parameter is valid only when IsPermanent is False.
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._IsPermanent = params.get("IsPermanent")
        self._SnapshotName = params.get("SnapshotName")
        self._Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotAttributeResponse(AbstractModel):
    r"""ModifySnapshotAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySnapshotsSharePermissionRequest(AbstractModel):
    r"""ModifySnapshotsSharePermission request structure.

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: The ID of the snapshot. You can obtain this by using [DescribeSnapshots](https://intl.cloud.tencent.com/document/api/362/15647?from_cn_redirect=1).
        :type SnapshotIds: list of str
        :param _AccountIds: Account Id list for receiving shared snapshots. the format of array-type parameters can be found in the API overview (https://www.tencentcloud.com/document/API/213/568?from_cn_redirect=1). the account Id is different from a QQ number. to query a user account Id, view the account Id column in the account information (https://console.cloud.tencent.com/developer).
        :type AccountIds: list of str
        :param _Permission: Operations. Valid values: `SHARE`, sharing an image; `CANCEL`, cancelling the sharing of an image.
        :type Permission: str
        """
        self._SnapshotIds = None
        self._AccountIds = None
        self._Permission = None

    @property
    def SnapshotIds(self):
        r"""The ID of the snapshot. You can obtain this by using [DescribeSnapshots](https://intl.cloud.tencent.com/document/api/362/15647?from_cn_redirect=1).
        :rtype: list of str
        """
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def AccountIds(self):
        r"""Account Id list for receiving shared snapshots. the format of array-type parameters can be found in the API overview (https://www.tencentcloud.com/document/API/213/568?from_cn_redirect=1). the account Id is different from a QQ number. to query a user account Id, view the account Id column in the account information (https://console.cloud.tencent.com/developer).
        :rtype: list of str
        """
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds

    @property
    def Permission(self):
        r"""Operations. Valid values: `SHARE`, sharing an image; `CANCEL`, cancelling the sharing of an image.
        :rtype: str
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        self._AccountIds = params.get("AccountIds")
        self._Permission = params.get("Permission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotsSharePermissionResponse(AbstractModel):
    r"""ModifySnapshotsSharePermission response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Placement(AbstractModel):
    r"""This describes the abstract location of the instance, including the availability zone in which it is located, the projects to which it belongs, and the ID and name of the dedicated clusters to which it belongs.

    """

    def __init__(self):
        r"""
        :param _Zone: The ID of the [Availability Zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) to which the cloud disk belongs. This parameter can be obtained from the Zone field in the returned values of [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1).
        :type Zone: str
        :param _CageId: CageId, which can be obtained via [DescribeDiskStoragePool](https://www.tencentcloud.com/document/api/362/62143?from_cn_redirect=1). as an input parameter, it operates on resources of the specified cage Id and can be empty. as an output parameter, it indicates the cage Id to which the resource belongs and can be empty.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CageId: str
        :param _ProjectId: Instance'S project ID, which can be obtained by DescribeProject. by default if left blank, it is 0, indicating the default project.
        :type ProjectId: int
        :param _ProjectName: Project to which instance belongs. search via [DescribeProject](https://www.tencentcloud.com/document/api/651/78725?from_cn_redirect=1).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param _CdcName: Dedicated cluster name. When it is an input parameter, it is ignored.  When it is an output parameter, it is the name of the dedicated cluster the cloud disk belongs to, and it can be left blank.
Note: This field may return null, indicating that no valid value was found.
        :type CdcName: str
        :param _CdcId: The exclusive cluster ID of the instance. can be obtained via [DescribeDiskStoragePool](https://www.tencentcloud.com/document/api/362/62143?from_cn_redirect=1). as an input parameter, it indicates operations on resources belonging to the designated CdcId exclusive cluster and can be empty. as an output parameter, it indicates the exclusive cluster ID of the resource and can be empty.
Note: This field may return null, indicating that no valid values can be obtained.
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
        r"""The ID of the [Availability Zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) to which the cloud disk belongs. This parameter can be obtained from the Zone field in the returned values of [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1).
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CageId(self):
        r"""CageId, which can be obtained via [DescribeDiskStoragePool](https://www.tencentcloud.com/document/api/362/62143?from_cn_redirect=1). as an input parameter, it operates on resources of the specified cage Id and can be empty. as an output parameter, it indicates the cage Id to which the resource belongs and can be empty.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ProjectId(self):
        r"""Instance'S project ID, which can be obtained by DescribeProject. by default if left blank, it is 0, indicating the default project.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project to which instance belongs. search via [DescribeProject](https://www.tencentcloud.com/document/api/651/78725?from_cn_redirect=1).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def CdcName(self):
        r"""Dedicated cluster name. When it is an input parameter, it is ignored.  When it is an output parameter, it is the name of the dedicated cluster the cloud disk belongs to, and it can be left blank.
Note: This field may return null, indicating that no valid value was found.
        :rtype: str
        """
        return self._CdcName

    @CdcName.setter
    def CdcName(self, CdcName):
        self._CdcName = CdcName

    @property
    def CdcId(self):
        r"""The exclusive cluster ID of the instance. can be obtained via [DescribeDiskStoragePool](https://www.tencentcloud.com/document/api/362/62143?from_cn_redirect=1). as an input parameter, it indicates operations on resources belonging to the designated CdcId exclusive cluster and can be empty. as an output parameter, it indicates the exclusive cluster ID of the resource and can be empty.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def DedicatedClusterId(self):
        r"""Dedicated cluster ID
        :rtype: str
        """
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
    r"""Describes the execution strategy of regular snapshots. it can be understood as executing this scheduled snapshot policy at the moment specified by Hour on the days designated by DayOfWeek/DayOfMonth or at the interval set by IntervalDays. note: DayOfWeek/DayOfMonth/IntervalDays are mutual exclusion rules, required and only one policy rule can be set. if mutual exclusion rules are imported at the same time, only one takes effect, with priority following the sequence listed in the previous context: for example, if all three rules are set, only DayOfWeek comes into effect.

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
        r"""Specifies the time that that the scheduled snapshot policy will be triggered. The unit is hour. The value range is [0-23]. 00:00-23:00 is a total of 24 time points that can be selected. 1 indicates 01:00, and so on.
        :rtype: list of int non-negative
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def DayOfWeek(self):
        r"""Specifies the days of the week, from Monday to Sunday, on which a scheduled snapshot will be triggered. Value range: [0, 6]. 0 indicates triggering on Sunday, 1-6 indicate triggering on Monday-Saturday.
        :rtype: list of int non-negative
        """
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def DayOfMonth(self):
        r"""Specifies the dates of the month on which a scheduled snapshot will be triggered. Value range: [1, 31]. `1` to `31` indicate the specific dates of the month; for example, `5` indicates the 5th day of the month. Note: If you set a date that does not exist in some months such as 29, 30, and 31, these months will be skipped for scheduled snapshot creation.
        :rtype: list of int non-negative
        """
        return self._DayOfMonth

    @DayOfMonth.setter
    def DayOfMonth(self, DayOfMonth):
        self._DayOfMonth = DayOfMonth

    @property
    def IntervalDays(self):
        r"""Specifies the interval for creating scheduled snapshots in days. Value range: [1, 365]. For example, if it is set to `5`, scheduled snapshots will be created every 5 days. Note: If you choose to back up by day, the time for the first backup is theoretically the day when the backup policy is created. If the backup policy creation time on the current day is later than the set backup time, the first backup will be performed in the second backup cycle.
        :rtype: int
        """
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
    r"""The cost of a prepaid order.

    """

    def __init__(self):
        r"""
        :param _DiscountPrice: Discounted price of a monthly-subscribed cloud disk or a snapshot, in USD.
        :type DiscountPrice: float
        :param _ChargeUnit: Billing unit for postpaid cloud disk. valid values:<br><li>HOUR: the billing unit for postpaid cloud disk is calculated hourly.</li>.
Note: This field may return null, indicating that no valid values can be obtained.
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
        :param _DetailPrices: Details list of billable items.
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
        r"""Discounted price of a monthly-subscribed cloud disk or a snapshot, in USD.
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def ChargeUnit(self):
        r"""Billing unit for postpaid cloud disk. valid values:<br><li>HOUR: the billing unit for postpaid cloud disk is calculated hourly.</li>.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def UnitPriceHigh(self):
        r"""Original unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UnitPriceHigh

    @UnitPriceHigh.setter
    def UnitPriceHigh(self, UnitPriceHigh):
        self._UnitPriceHigh = UnitPriceHigh

    @property
    def OriginalPriceHigh(self):
        r"""Original payment of a monthly-subscribed cloud disk or a snapshot, in USD, with six decimal places.
        :rtype: str
        """
        return self._OriginalPriceHigh

    @OriginalPriceHigh.setter
    def OriginalPriceHigh(self, OriginalPriceHigh):
        self._OriginalPriceHigh = OriginalPriceHigh

    @property
    def OriginalPrice(self):
        r"""Original payment of a monthly-subscribed cloud disk or a snapshot, in USD.
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def UnitPriceDiscount(self):
        r"""Discount unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def UnitPriceDiscountHigh(self):
        r"""Discounted unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UnitPriceDiscountHigh

    @UnitPriceDiscountHigh.setter
    def UnitPriceDiscountHigh(self, UnitPriceDiscountHigh):
        self._UnitPriceDiscountHigh = UnitPriceDiscountHigh

    @property
    def DiscountPriceHigh(self):
        r"""Discounted price of a monthly-subscribed cloud disk or a snapshot, in USD, with six decimal places.
        :rtype: str
        """
        return self._DiscountPriceHigh

    @DiscountPriceHigh.setter
    def DiscountPriceHigh(self, DiscountPriceHigh):
        self._DiscountPriceHigh = DiscountPriceHigh

    @property
    def UnitPrice(self):
        r"""Original unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def DetailPrices(self):
        r"""Details list of billable items.
        :rtype: list of DetailPrice
        """
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
    r"""Describes the prepaid or postpaid price for the cloud disk.

    """

    def __init__(self):
        r"""
        :param _UnitPriceDiscount: Discount unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: float
        :param _DiscountPrice: Discounted price of a monthly-subscribed cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiscountPrice: float
        :param _UnitPrice: Original unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param _UnitPriceHigh: Original unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceHigh: str
        :param _OriginalPriceHigh: Original payment of a monthly-subscribed cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginalPriceHigh: str
        :param _OriginalPrice: Original price of a monthly-subscribed cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginalPrice: float
        :param _DiscountPriceHigh: Discounted payment price of a monthly-subscribed cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiscountPriceHigh: str
        :param _UnitPriceDiscountHigh: Discounted unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceDiscountHigh: str
        :param _ChargeUnit: Billing unit for postpaid cloud disk. valid values:<br><li>HOUR: the billing unit for postpaid cloud disk is calculated hourly.</li>.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeUnit: str
        """
        self._UnitPriceDiscount = None
        self._DiscountPrice = None
        self._UnitPrice = None
        self._UnitPriceHigh = None
        self._OriginalPriceHigh = None
        self._OriginalPrice = None
        self._DiscountPriceHigh = None
        self._UnitPriceDiscountHigh = None
        self._ChargeUnit = None

    @property
    def UnitPriceDiscount(self):
        r"""Discount unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def DiscountPrice(self):
        r"""Discounted price of a monthly-subscribed cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def UnitPrice(self):
        r"""Original unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceHigh(self):
        r"""Original unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UnitPriceHigh

    @UnitPriceHigh.setter
    def UnitPriceHigh(self, UnitPriceHigh):
        self._UnitPriceHigh = UnitPriceHigh

    @property
    def OriginalPriceHigh(self):
        r"""Original payment of a monthly-subscribed cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OriginalPriceHigh

    @OriginalPriceHigh.setter
    def OriginalPriceHigh(self, OriginalPriceHigh):
        self._OriginalPriceHigh = OriginalPriceHigh

    @property
    def OriginalPrice(self):
        r"""Original price of a monthly-subscribed cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPriceHigh(self):
        r"""Discounted payment price of a monthly-subscribed cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiscountPriceHigh

    @DiscountPriceHigh.setter
    def DiscountPriceHigh(self, DiscountPriceHigh):
        self._DiscountPriceHigh = DiscountPriceHigh

    @property
    def UnitPriceDiscountHigh(self):
        r"""Discounted unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UnitPriceDiscountHigh

    @UnitPriceDiscountHigh.setter
    def UnitPriceDiscountHigh(self, UnitPriceDiscountHigh):
        self._UnitPriceDiscountHigh = UnitPriceDiscountHigh

    @property
    def ChargeUnit(self):
        r"""Billing unit for postpaid cloud disk. valid values:<br><li>HOUR: the billing unit for postpaid cloud disk is calculated hourly.</li>.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit


    def _deserialize(self, params):
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._DiscountPrice = params.get("DiscountPrice")
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceHigh = params.get("UnitPriceHigh")
        self._OriginalPriceHigh = params.get("OriginalPriceHigh")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPriceHigh = params.get("DiscountPriceHigh")
        self._UnitPriceDiscountHigh = params.get("UnitPriceDiscountHigh")
        self._ChargeUnit = params.get("ChargeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDiskRequest(AbstractModel):
    r"""RenewDisk request structure.

    """

    def __init__(self):
        r"""
        :param _DiskChargePrepaid: Specifies the parameter CurInstanceDeadline in the scenario where the cloud disk and mounted instance renew together. at this point, the cloud disk renewal aligns with the instance renewal expiry date.
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param _DiskId: Cloud disk ID, which can be queried by calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskId: str
        """
        self._DiskChargePrepaid = None
        self._DiskId = None

    @property
    def DiskChargePrepaid(self):
        r"""Specifies the parameter CurInstanceDeadline in the scenario where the cloud disk and mounted instance renew together. at this point, the cloud disk renewal aligns with the instance renewal expiry date.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        """
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DiskId(self):
        r"""Cloud disk ID, which can be queried by calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDiskResponse(AbstractModel):
    r"""RenewDisk response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResizeDiskRequest(AbstractModel):
    r"""ResizeDisk request structure.

    """

    def __init__(self):
        r"""
        :param _DiskSize: Cloud disk size after scale out (in GB). This must be larger than the current size of the cloud disk. For the value range of the cloud disk sizes, see cloud disk [Product Types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        :param _DiskId: Cloud disk ID, which can be queried by calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. this field is only required when expanding a single cloud disk.
        :type DiskId: str
        """
        self._DiskSize = None
        self._DiskId = None

    @property
    def DiskSize(self):
        r"""Cloud disk size after scale out (in GB). This must be larger than the current size of the cloud disk. For the value range of the cloud disk sizes, see cloud disk [Product Types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1).
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        r"""Cloud disk ID, which can be queried by calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api. this field is only required when expanding a single cloud disk.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskResponse(AbstractModel):
    r"""ResizeDisk response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SharePermission(AbstractModel):
    r"""Snapshot sharing information set

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
        r"""Snapshot sharing time
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def AccountId(self):
        r"""ID of the shared account
        :rtype: str
        """
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
    r"""The details of a snapshot

    """

    def __init__(self):
        r"""
        :param _Placement: Location of the snapshot.
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param _CopyFromRemote: Specifies whether the snapshot is for cross-region replication. value range:.
<ul>
<li>true: indicates a snapshot for cross-region replication.</li>.
<li>false: snapshot of the local region.</li>.
</ul>
        :type CopyFromRemote: bool
        :param _SnapshotState: Snapshot status. valid values:.
<ul>
<Li>NORMAL: specifies the scaling group is normal.</li>.
<Li>CREATING: creating</li>.
<Li>ROLLBACKING: indicates the rollback is in progress.</li>.
<Li>COPYING_FROM_REMOTE: cross geo-replication in progress.</li>.
<Li>CHECKING_COPIED: copying check in progress.</li>.
<Li>TORECYCLE: to be recycled.</li>.
</ul>
        :type SnapshotState: str
        :param _IsPermanent: Whether it is a permanent snapshot. valid values:.
<ul>
<li>true: permanent snapshot.</li>.
<li>false: non-permanent snapshot.</li>.
</ul>
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
        :param _SnapshotType: Specifies the SNAPSHOT type. valid values: `PRIVATE_SNAPSHOT` (PRIVATE SNAPSHOT) or `SHARED_SNAPSHOT` (SHARED SNAPSHOT).
        :type SnapshotType: str
        :param _DiskSize: Specifies the disk capacity of the CBS for creating this snapshot, in GiB.
        :type DiskSize: int
        :param _DiskId: ID of the cloud disk used to create this snapshot.
        :type DiskId: str
        :param _CopyingToRegions: Destination region of the snapshot currently under cross region replication. if not, return `[]`.
        :type CopyingToRegions: list of str
        :param _Encrypt: Indicates whether the snapshot is created for an encrypted disk. valid values:.
<ul>
<li>true: specifies the snapshot is created by encrypted disks.</li>.
<li>false: snapshot created for non-encrypted disk.</li>.
</ul>
        :type Encrypt: bool
        :param _CreateTime: Creation time of the snapshot.
        :type CreateTime: str
        :param _ImageCount: Number of images associated with snapshot.
        :type ImageCount: int
        :param _DiskUsage: Specifies the cloud disk type of the CBS for creating this snapshot. valid values:.
<ul>
<Li>SYSTEM_DISK: system disk</li>.
<Li>DATA_DISK: specifies the data disk.</li>.
</ul>

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
        r"""Location of the snapshot.
        :rtype: :class:`tencentcloud.cbs.v20170312.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CopyFromRemote(self):
        r"""Specifies whether the snapshot is for cross-region replication. value range:.
<ul>
<li>true: indicates a snapshot for cross-region replication.</li>.
<li>false: snapshot of the local region.</li>.
</ul>
        :rtype: bool
        """
        return self._CopyFromRemote

    @CopyFromRemote.setter
    def CopyFromRemote(self, CopyFromRemote):
        self._CopyFromRemote = CopyFromRemote

    @property
    def SnapshotState(self):
        r"""Snapshot status. valid values:.
<ul>
<Li>NORMAL: specifies the scaling group is normal.</li>.
<Li>CREATING: creating</li>.
<Li>ROLLBACKING: indicates the rollback is in progress.</li>.
<Li>COPYING_FROM_REMOTE: cross geo-replication in progress.</li>.
<Li>CHECKING_COPIED: copying check in progress.</li>.
<Li>TORECYCLE: to be recycled.</li>.
</ul>
        :rtype: str
        """
        return self._SnapshotState

    @SnapshotState.setter
    def SnapshotState(self, SnapshotState):
        self._SnapshotState = SnapshotState

    @property
    def IsPermanent(self):
        r"""Whether it is a permanent snapshot. valid values:.
<ul>
<li>true: permanent snapshot.</li>.
<li>false: non-permanent snapshot.</li>.
</ul>
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def SnapshotName(self):
        r"""Snapshot name, the user-defined snapshot alias. Call [ModifySnapshotAttribute](https://intl.cloud.tencent.com/document/product/362/15650?from_cn_redirect=1) to modify this field.
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def DeadlineTime(self):
        r"""The expiration time of the snapshot. If the snapshot is permanently retained, this field is blank.
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Percent(self):
        r"""The progress percentage for snapshot creation. This field is always 100 after the snapshot is created successfully.
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Images(self):
        r"""List of images associated with snapshot.
        :rtype: list of Image
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def ShareReference(self):
        r"""Number of snapshots currently shared
        :rtype: int
        """
        return self._ShareReference

    @ShareReference.setter
    def ShareReference(self, ShareReference):
        self._ShareReference = ShareReference

    @property
    def SnapshotType(self):
        r"""Specifies the SNAPSHOT type. valid values: `PRIVATE_SNAPSHOT` (PRIVATE SNAPSHOT) or `SHARED_SNAPSHOT` (SHARED SNAPSHOT).
        :rtype: str
        """
        return self._SnapshotType

    @SnapshotType.setter
    def SnapshotType(self, SnapshotType):
        self._SnapshotType = SnapshotType

    @property
    def DiskSize(self):
        r"""Specifies the disk capacity of the CBS for creating this snapshot, in GiB.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        r"""ID of the cloud disk used to create this snapshot.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def CopyingToRegions(self):
        r"""Destination region of the snapshot currently under cross region replication. if not, return `[]`.
        :rtype: list of str
        """
        return self._CopyingToRegions

    @CopyingToRegions.setter
    def CopyingToRegions(self, CopyingToRegions):
        self._CopyingToRegions = CopyingToRegions

    @property
    def Encrypt(self):
        r"""Indicates whether the snapshot is created for an encrypted disk. valid values:.
<ul>
<li>true: specifies the snapshot is created by encrypted disks.</li>.
<li>false: snapshot created for non-encrypted disk.</li>.
</ul>
        :rtype: bool
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def CreateTime(self):
        r"""Creation time of the snapshot.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ImageCount(self):
        r"""Number of images associated with snapshot.
        :rtype: int
        """
        return self._ImageCount

    @ImageCount.setter
    def ImageCount(self, ImageCount):
        self._ImageCount = ImageCount

    @property
    def DiskUsage(self):
        r"""Specifies the cloud disk type of the CBS for creating this snapshot. valid values:.
<ul>
<Li>SYSTEM_DISK: system disk</li>.
<Li>DATA_DISK: specifies the data disk.</li>.
</ul>

        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def SnapshotId(self):
        r"""Snapshot ID.
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def TimeStartShare(self):
        r"""The time when the snapshot sharing starts
        :rtype: str
        """
        return self._TimeStartShare

    @TimeStartShare.setter
    def TimeStartShare(self, TimeStartShare):
        self._TimeStartShare = TimeStartShare

    @property
    def Tags(self):
        r"""List of tags associated with the snapshot.
        :rtype: list of Tag
        """
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
    r"""Result of the cross-region replication task

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
        r"""ID of the snapshot replica
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Message(self):
        r"""Error message. It’s null if the request succeeds.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        r"""Error code. It’s `Success` if the request succeeds.
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def DestinationRegion(self):
        r"""Destination region of the replication task
        :rtype: str
        """
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
        


class SnapshotGroup(AbstractModel):
    r"""It describes the snapshot group details.

    """

    def __init__(self):
        r"""
        :param _SnapshotGroupId: Specifies the snapshot group ID.
        :type SnapshotGroupId: str
        :param _SnapshotGroupType: Snapshot group type. NORMAL: common snapshot group, non-consistent snapshot.
        :type SnapshotGroupType: str
        :param _ContainRootSnapshot: Specifies whether the snapshot group contains a system disk snapshot.
        :type ContainRootSnapshot: bool
        :param _SnapshotIdSet: Specifies the snapshot ID list included in the snapshot group.
        :type SnapshotIdSet: list of str
        :param _SnapshotGroupState: <ul>
<Li>NORMAL: specifies the scaling group is in normal state.</li>.
<Li>CREATING: creating.</li>.
<Li>ROLLBACKING: indicates the rollback is in progress.</li>.
</ul>
        :type SnapshotGroupState: str
        :param _Percent: Specifies the snapshot group creation progress.
        :type Percent: int
        :param _CreateTime: Specifies the snapshot group creation time.
        :type CreateTime: str
        :param _ModifyTime: Latest modification time of the snapshot group.
        :type ModifyTime: str
        :param _Images: Specifies the image list associated with the snapshot group.
        :type Images: list of Image
        :param _SnapshotGroupName: Specifies the snapshot group name.
        :type SnapshotGroupName: str
        :param _ImageCount: Number of images associated with the snapshot group.
        :type ImageCount: int
        :param _IsPermanent: Specifies whether the snapshot group has permanent retention.
        :type IsPermanent: bool
        :param _DeadlineTime: Specifies the snapshot group expiration time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeadlineTime: str
        :param _AutoSnapshotPolicyId: Source automatic snapshot policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoSnapshotPolicyId: str
        """
        self._SnapshotGroupId = None
        self._SnapshotGroupType = None
        self._ContainRootSnapshot = None
        self._SnapshotIdSet = None
        self._SnapshotGroupState = None
        self._Percent = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Images = None
        self._SnapshotGroupName = None
        self._ImageCount = None
        self._IsPermanent = None
        self._DeadlineTime = None
        self._AutoSnapshotPolicyId = None

    @property
    def SnapshotGroupId(self):
        r"""Specifies the snapshot group ID.
        :rtype: str
        """
        return self._SnapshotGroupId

    @SnapshotGroupId.setter
    def SnapshotGroupId(self, SnapshotGroupId):
        self._SnapshotGroupId = SnapshotGroupId

    @property
    def SnapshotGroupType(self):
        r"""Snapshot group type. NORMAL: common snapshot group, non-consistent snapshot.
        :rtype: str
        """
        return self._SnapshotGroupType

    @SnapshotGroupType.setter
    def SnapshotGroupType(self, SnapshotGroupType):
        self._SnapshotGroupType = SnapshotGroupType

    @property
    def ContainRootSnapshot(self):
        r"""Specifies whether the snapshot group contains a system disk snapshot.
        :rtype: bool
        """
        return self._ContainRootSnapshot

    @ContainRootSnapshot.setter
    def ContainRootSnapshot(self, ContainRootSnapshot):
        self._ContainRootSnapshot = ContainRootSnapshot

    @property
    def SnapshotIdSet(self):
        r"""Specifies the snapshot ID list included in the snapshot group.
        :rtype: list of str
        """
        return self._SnapshotIdSet

    @SnapshotIdSet.setter
    def SnapshotIdSet(self, SnapshotIdSet):
        self._SnapshotIdSet = SnapshotIdSet

    @property
    def SnapshotGroupState(self):
        r"""<ul>
<Li>NORMAL: specifies the scaling group is in normal state.</li>.
<Li>CREATING: creating.</li>.
<Li>ROLLBACKING: indicates the rollback is in progress.</li>.
</ul>
        :rtype: str
        """
        return self._SnapshotGroupState

    @SnapshotGroupState.setter
    def SnapshotGroupState(self, SnapshotGroupState):
        self._SnapshotGroupState = SnapshotGroupState

    @property
    def Percent(self):
        r"""Specifies the snapshot group creation progress.
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def CreateTime(self):
        r"""Specifies the snapshot group creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""Latest modification time of the snapshot group.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Images(self):
        r"""Specifies the image list associated with the snapshot group.
        :rtype: list of Image
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def SnapshotGroupName(self):
        r"""Specifies the snapshot group name.
        :rtype: str
        """
        return self._SnapshotGroupName

    @SnapshotGroupName.setter
    def SnapshotGroupName(self, SnapshotGroupName):
        self._SnapshotGroupName = SnapshotGroupName

    @property
    def ImageCount(self):
        r"""Number of images associated with the snapshot group.
        :rtype: int
        """
        return self._ImageCount

    @ImageCount.setter
    def ImageCount(self, ImageCount):
        self._ImageCount = ImageCount

    @property
    def IsPermanent(self):
        r"""Specifies whether the snapshot group has permanent retention.
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def DeadlineTime(self):
        r"""Specifies the snapshot group expiration time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def AutoSnapshotPolicyId(self):
        r"""Source automatic snapshot policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId


    def _deserialize(self, params):
        self._SnapshotGroupId = params.get("SnapshotGroupId")
        self._SnapshotGroupType = params.get("SnapshotGroupType")
        self._ContainRootSnapshot = params.get("ContainRootSnapshot")
        self._SnapshotIdSet = params.get("SnapshotIdSet")
        self._SnapshotGroupState = params.get("SnapshotGroupState")
        self._Percent = params.get("Percent")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        if params.get("Images") is not None:
            self._Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self._Images.append(obj)
        self._SnapshotGroupName = params.get("SnapshotGroupName")
        self._ImageCount = params.get("ImageCount")
        self._IsPermanent = params.get("IsPermanent")
        self._DeadlineTime = params.get("DeadlineTime")
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""Tag.

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
        r"""Tag key.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Tag value.
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
        


class TerminateDisksRequest(AbstractModel):
    r"""TerminateDisks request structure.

    """

    def __init__(self):
        r"""
        :param _DiskIds: List of cloud disk ids to be returned, which can be queried by calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api.
        :type DiskIds: list of str
        :param _DeleteSnapshot: Delete the associated non-permanently reserved snapshots upon deletion of the source cloud disk. `0`: No (default). `1`: Yes. To check whether a snapshot is permanently reserved, refer to the `IsPermanent` field returned by the `DescribeSnapshots` API. 
        :type DeleteSnapshot: int
        """
        self._DiskIds = None
        self._DeleteSnapshot = None

    @property
    def DiskIds(self):
        r"""List of cloud disk ids to be returned, which can be queried by calling the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) api.
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DeleteSnapshot(self):
        r"""Delete the associated non-permanently reserved snapshots upon deletion of the source cloud disk. `0`: No (default). `1`: Yes. To check whether a snapshot is permanently reserved, refer to the `IsPermanent` field returned by the `DescribeSnapshots` API. 
        :rtype: int
        """
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
    r"""TerminateDisks response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UnbindAutoSnapshotPolicyRequest(AbstractModel):
    r"""UnbindAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _AutoSnapshotPolicyId: ID of scheduled snapshot policy to be unbound.
        :type AutoSnapshotPolicyId: str
        :param _DiskIds: ID list of cloud disks from which the regular snapshot policy is unbound. specifies this parameter or the InstanceIds parameter. a minimum of one is required.
        :type DiskIds: list of str
        :param _InstanceIds: Instance ID list to unbind the periodic snapshot policy. this parameter or the DiskIds parameter requires a minimum of one input.
        :type InstanceIds: list of str
        """
        self._AutoSnapshotPolicyId = None
        self._DiskIds = None
        self._InstanceIds = None

    @property
    def AutoSnapshotPolicyId(self):
        r"""ID of scheduled snapshot policy to be unbound.
        :rtype: str
        """
        return self._AutoSnapshotPolicyId

    @AutoSnapshotPolicyId.setter
    def AutoSnapshotPolicyId(self, AutoSnapshotPolicyId):
        self._AutoSnapshotPolicyId = AutoSnapshotPolicyId

    @property
    def DiskIds(self):
        r"""ID list of cloud disks from which the regular snapshot policy is unbound. specifies this parameter or the InstanceIds parameter. a minimum of one is required.
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def InstanceIds(self):
        r"""Instance ID list to unbind the periodic snapshot policy. this parameter or the DiskIds parameter requires a minimum of one input.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self._DiskIds = params.get("DiskIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoSnapshotPolicyResponse(AbstractModel):
    r"""UnbindAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")