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


class ApplyDiskBackupRequest(AbstractModel):
    """ApplyDiskBackup request structure.

    """

    def __init__(self):
        r"""
        :param DiskBackupId: ID of the cloud disk backup point, which can be queried through the `DescribeDiskBackups` API.
        :type DiskBackupId: str
        :param DiskId: ID of the original cloud disk of the backup point, which can be queried through the `DescribeDisks` API.
        :type DiskId: str
        """
        self.DiskBackupId = None
        self.DiskId = None


    def _deserialize(self, params):
        self.DiskBackupId = params.get("DiskBackupId")
        self.DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyDiskBackupResponse(AbstractModel):
    """ApplyDiskBackup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ApplySnapshotRequest(AbstractModel):
    """ApplySnapshot request structure.

    """

    def __init__(self):
        r"""
        :param SnapshotId: Snapshot ID, which can be queried via [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :type SnapshotId: str
        :param DiskId: ID of the original cloud disk corresponding to the snapshot, which can be queried via the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1).
        :type DiskId: str
        :param AutoStopInstance: Specifies whether to shut down a CVM automatically before a rollback
        :type AutoStopInstance: bool
        :param AutoStartInstance: Specifies whether to start up a CVM automatically after a rollback
        :type AutoStartInstance: bool
        """
        self.SnapshotId = None
        self.DiskId = None
        self.AutoStopInstance = None
        self.AutoStartInstance = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.DiskId = params.get("DiskId")
        self.AutoStopInstance = params.get("AutoStopInstance")
        self.AutoStartInstance = params.get("AutoStartInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplySnapshotResponse(AbstractModel):
    """ApplySnapshot response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachDetail(AbstractModel):
    """This describes the number of mounted and mountable data disks of an instance.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param AttachedDiskCount: The number of instances mounted to data disk.
        :type AttachedDiskCount: int
        :param MaxAttachCount: The maximum number of instances that can be mounted to data disk.
        :type MaxAttachCount: int
        """
        self.InstanceId = None
        self.AttachedDiskCount = None
        self.MaxAttachCount = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AttachedDiskCount = params.get("AttachedDiskCount")
        self.MaxAttachCount = params.get("MaxAttachCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksRequest(AbstractModel):
    """AttachDisks request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ID of the CVM instance on which the cloud disk will be mounted. It can be queried via the API [DescribeInstances](https://intl.cloud.tencent.com/document/product/213/15728?from_cn_redirect=1).
        :type InstanceId: str
        :param DiskIds: ID of the elastic cloud disk to be mounted, which can be queried through the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1). A maximum of 10 elastic cloud disks can be mounted in a single request.
        :type DiskIds: list of str
        :param DeleteWithInstance: Optional parameter. If this is not passed only the mount operation is executed. If `True` is passed, the cloud disk will be configured to be terminated when the server it is mounted to is terminated. This is only valid for pay-as-you-go cloud disks.
        :type DeleteWithInstance: bool
        :param AttachMode: (Optional) Specifies the cloud disk mounting method. It’s only valid for BM models. Valid values: <br><li>PF<br><li>VF
        :type AttachMode: str
        """
        self.InstanceId = None
        self.DiskIds = None
        self.DeleteWithInstance = None
        self.AttachMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DiskIds = params.get("DiskIds")
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.AttachMode = params.get("AttachMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksResponse(AbstractModel):
    """AttachDisks response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AutoMountConfiguration(AbstractModel):
    """Describes how a newly purchased cloud disk is initialized and attached to a CVM instance.

    """

    def __init__(self):
        r"""
        :param InstanceId: ID of the instance to which the cloud disk is attached.
        :type InstanceId: list of str
        :param MountPoint: Mount point in the instance.
        :type MountPoint: list of str
        :param FileSystemType: File system type. Valid values: `ext4`, `xfs`.
        :type FileSystemType: str
        """
        self.InstanceId = None
        self.MountPoint = None
        self.FileSystemType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MountPoint = params.get("MountPoint")
        self.FileSystemType = params.get("FileSystemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoSnapshotPolicy(AbstractModel):
    """This describes the detailed information of the scheduled snapshot policy.

    """

    def __init__(self):
        r"""
        :param DiskIdSet: The list of cloud disk IDs that the current scheduled snapshot policy is bound to.
        :type DiskIdSet: list of str
        :param IsActivated: Whether scheduled snapshot policy is activated.
        :type IsActivated: bool
        :param AutoSnapshotPolicyState: Scheduled snapshot policy state. Value range:<br><li>NORMAL: Normal<br><li>ISOLATED: Isolated.
        :type AutoSnapshotPolicyState: str
        :param IsCopyToRemote: Whether it is to replicate a snapshot across accounts. `1`: yes, `0`: no.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsCopyToRemote: int
        :param IsPermanent: Whether the snapshot created by this scheduled snapshot policy is retained permanently.
        :type IsPermanent: bool
        :param NextTriggerTime: The time the scheduled snapshot will be triggered again.
        :type NextTriggerTime: str
        :param AutoSnapshotPolicyName: Scheduled snapshot policy name.
        :type AutoSnapshotPolicyName: str
        :param AutoSnapshotPolicyId: Scheduled snapshot policy ID.
        :type AutoSnapshotPolicyId: str
        :param Policy: The policy for executing the scheduled snapshot.
        :type Policy: list of Policy
        :param CreateTime: The time the scheduled snapshot policy was created.
        :type CreateTime: str
        :param RetentionDays: Number of days the snapshot created by this scheduled snapshot policy is retained.
        :type RetentionDays: int
        :param CopyToAccountUin: ID of the replication target account
Note: This field may return null, indicating that no valid values can be obtained.
        :type CopyToAccountUin: str
        :param InstanceIdSet: List of IDs of the instances associated with the scheduled snapshot policy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceIdSet: list of str
        """
        self.DiskIdSet = None
        self.IsActivated = None
        self.AutoSnapshotPolicyState = None
        self.IsCopyToRemote = None
        self.IsPermanent = None
        self.NextTriggerTime = None
        self.AutoSnapshotPolicyName = None
        self.AutoSnapshotPolicyId = None
        self.Policy = None
        self.CreateTime = None
        self.RetentionDays = None
        self.CopyToAccountUin = None
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.DiskIdSet = params.get("DiskIdSet")
        self.IsActivated = params.get("IsActivated")
        self.AutoSnapshotPolicyState = params.get("AutoSnapshotPolicyState")
        self.IsCopyToRemote = params.get("IsCopyToRemote")
        self.IsPermanent = params.get("IsPermanent")
        self.NextTriggerTime = params.get("NextTriggerTime")
        self.AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        if params.get("Policy") is not None:
            self.Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self.Policy.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.RetentionDays = params.get("RetentionDays")
        self.CopyToAccountUin = params.get("CopyToAccountUin")
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoSnapshotPolicyRequest(AbstractModel):
    """BindAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: ID of scheduled snapshot policy to be bound.
        :type AutoSnapshotPolicyId: str
        :param DiskIds: List of cloud disk IDs to be bound. Maximum of 80 cloud disks can be bound per request.
        :type DiskIds: list of str
        """
        self.AutoSnapshotPolicyId = None
        self.DiskIds = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoSnapshotPolicyResponse(AbstractModel):
    """BindAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CopySnapshotCrossRegionsRequest(AbstractModel):
    """CopySnapshotCrossRegions request structure.

    """

    def __init__(self):
        r"""
        :param DestinationRegions: Destination regions of the replication task. You can query the value of regions by calling [DescribeRegions](https://intl.cloud.tencent.com/document/product/213/9456?from_cn_redirect=1) API. Note that you can only specify regions that support snapshots.
        :type DestinationRegions: list of str
        :param SnapshotId: Snapshot ID, which can be queried via the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API.
        :type SnapshotId: str
        :param SnapshotName: Name of the snapshot replica. If it’s not specified, it defaults to “Copied [source snapshot ID from [region name]”
        :type SnapshotName: str
        """
        self.DestinationRegions = None
        self.SnapshotId = None
        self.SnapshotName = None


    def _deserialize(self, params):
        self.DestinationRegions = params.get("DestinationRegions")
        self.SnapshotId = params.get("SnapshotId")
        self.SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopySnapshotCrossRegionsResponse(AbstractModel):
    """CopySnapshotCrossRegions response structure.

    """

    def __init__(self):
        r"""
        :param SnapshotCopyResultSet: Result of the cross-region replication task. The ID of the new snapshot replica is returned if the request succeeds. Otherwise `Error` is returned.
        :type SnapshotCopyResultSet: list of SnapshotCopyResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SnapshotCopyResultSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SnapshotCopyResultSet") is not None:
            self.SnapshotCopyResultSet = []
            for item in params.get("SnapshotCopyResultSet"):
                obj = SnapshotCopyResult()
                obj._deserialize(item)
                self.SnapshotCopyResultSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateAutoSnapshotPolicyRequest(AbstractModel):
    """CreateAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param Policy: The policy for executing the scheduled snapshot.
        :type Policy: list of Policy
        :param AutoSnapshotPolicyName: The name of the scheduled snapshot policy to be created. If it is left empty, the default is 'Not named'. The maximum length cannot exceed 60 bytes.
        :type AutoSnapshotPolicyName: str
        :param IsActivated: Whether or not the scheduled snapshot policy is activated. FALSE: Not activated. TRUE: Activated. The default value is TRUE.
        :type IsActivated: bool
        :param IsPermanent: Whether the snapshot created by this scheduled snapshot policy is retained permanently. FALSE: Not retained permanently. TRUE: Retained permanently. The default value is FALSE.
        :type IsPermanent: bool
        :param RetentionDays: The number of days that a snapshot created by this scheduled snapshot policy is retained. The default value is 7. If this parameter is specified, the IsPermanent input parameter can not be TRUE, otherwise a conflict will occur.
        :type RetentionDays: int
        :param DryRun: Whether to create an execution policy for the scheduled snapshot. TRUE: Only the time of the initial backup needs to be obtained, and no scheduled snapshot policy is actually created. FALSE: Create. The default value is FALSE.
        :type DryRun: bool
        """
        self.Policy = None
        self.AutoSnapshotPolicyName = None
        self.IsActivated = None
        self.IsPermanent = None
        self.RetentionDays = None
        self.DryRun = None


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self.Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self.Policy.append(obj)
        self.AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self.IsActivated = params.get("IsActivated")
        self.IsPermanent = params.get("IsPermanent")
        self.RetentionDays = params.get("RetentionDays")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoSnapshotPolicyResponse(AbstractModel):
    """CreateAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: The ID of the newly created scheduled snapshot policy.
        :type AutoSnapshotPolicyId: str
        :param NextTriggerTime: The time that initial backup will start.
        :type NextTriggerTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AutoSnapshotPolicyId = None
        self.NextTriggerTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.NextTriggerTime = params.get("NextTriggerTime")
        self.RequestId = params.get("RequestId")


class CreateDisksRequest(AbstractModel):
    """CreateDisks request structure.

    """

    def __init__(self):
        r"""
        :param Placement: Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone and project. If no project is specified, the default project will be used.
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param DiskChargeType: Cloud disk billing mode. POSTPAID_BY_HOUR: Pay-as-you-go by hour<br><li>CDCPAID: Billed together with the bound dedicated cluster<br>For more information on the pricing in each mode, see [Pricing Overview](https://intl.cloud.tencent.com/document/product/362/2413?from_cn_redirect=1).
        :type DiskChargeType: str
        :param DiskType: Cloud disk media type. Valid values: <br><li>CLOUD_BASIC: HDD Cloud Storage<br><li>CLOUD_PREMIUM: Premium Cloud Disk<br><li>CLOUD_BSSD: Balanced SSD<br><li>CLOUD_SSD: SSD<br><li>CLOUD_HSSD: Enhanced SSD<br><li>CLOUD_TSSD: ulTra SSD.
        :type DiskType: str
        :param DiskName: Cloud disk name. If it is not specified, "Unnamed" will be used by default. The maximum length is 60 bytes.
        :type DiskName: str
        :param Tags: Tags bound to the cloud disk.
        :type Tags: list of Tag
        :param SnapshotId: Snapshot ID. If this parameter is specified, the cloud disk will be created based on the snapshot. The snapshot must be a data disk snapshot. To query the type of a snapshot, call the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API and see the `DiskUsage` field in the response.
        :type SnapshotId: str
        :param DiskCount: Number of cloud disks to be created. If it is not specified, `1` will be used by default. There is an upper limit on the maximum number of cloud disks that can be created in a single request. For more information, see [Use Limits](https://intl.cloud.tencent.com/doc/product/362/5145?from_cn_redirect=1).
        :type DiskCount: int
        :param ThroughputPerformance: Extra performance purchased for a cloud disk.<br>This optional parameter is only valid for ulTra SSD (CLOUD_TSSD) and Enhanced SSD (CLOUD_HSSD).
        :type ThroughputPerformance: int
        :param DiskSize: Cloud disk size in GB. <br><li>`DiskSize` is not required if `SnapshotId` is specified. In this case, the size of the cloud disk will be equal to that of the snapshot. <br><li>If you specify both `SnapshotId` and `DiskSize`, the specified disk size cannot be smaller than the snapshot size. <br><li>For the value range of cloud disk size, see [Cloud Disk Types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        :param Shareable: Optional parameter. Default value: `False`. If `True` is specified, the new cloud disk will be shared.
        :type Shareable: bool
        :param ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        :param Encrypt: This parameter is used to create encrypted cloud disks. It is fixed at `ENCRYPT`.
        :type Encrypt: str
        :param DiskChargePrepaid: Relevant parameter settings for the prepaid mode (i.e., monthly subscription). The monthly subscription cloud disk purchase attributes such as usage period and whether or not auto-renewal is set up can be specified using this parameter. <br>This parameter is required when creating a prepaid cloud disk. This parameter is not required when creating an hourly postpaid cloud disk. 
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param DeleteSnapshot: Whether to delete the associated non-permanently reserved snapshots upon deletion of the source cloud disk. `0`: No (default value). `1`: Yes. To check whether a snapshot is permanently reserved, see the `IsPermanent` field returned by the `DescribeSnapshots` API.
        :type DeleteSnapshot: int
        :param AutoMountConfiguration: Specifies whether to automatically attach and initialize the newly created data disk.
        :type AutoMountConfiguration: :class:`tencentcloud.cbs.v20170312.models.AutoMountConfiguration`
        :param DiskBackupQuota: Specifies the cloud disk backup point quota.
        :type DiskBackupQuota: int
        """
        self.Placement = None
        self.DiskChargeType = None
        self.DiskType = None
        self.DiskName = None
        self.Tags = None
        self.SnapshotId = None
        self.DiskCount = None
        self.ThroughputPerformance = None
        self.DiskSize = None
        self.Shareable = None
        self.ClientToken = None
        self.Encrypt = None
        self.DiskChargePrepaid = None
        self.DeleteSnapshot = None
        self.AutoMountConfiguration = None
        self.DiskBackupQuota = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.DiskChargeType = params.get("DiskChargeType")
        self.DiskType = params.get("DiskType")
        self.DiskName = params.get("DiskName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SnapshotId = params.get("SnapshotId")
        self.DiskCount = params.get("DiskCount")
        self.ThroughputPerformance = params.get("ThroughputPerformance")
        self.DiskSize = params.get("DiskSize")
        self.Shareable = params.get("Shareable")
        self.ClientToken = params.get("ClientToken")
        self.Encrypt = params.get("Encrypt")
        if params.get("DiskChargePrepaid") is not None:
            self.DiskChargePrepaid = DiskChargePrepaid()
            self.DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self.DeleteSnapshot = params.get("DeleteSnapshot")
        if params.get("AutoMountConfiguration") is not None:
            self.AutoMountConfiguration = AutoMountConfiguration()
            self.AutoMountConfiguration._deserialize(params.get("AutoMountConfiguration"))
        self.DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisksResponse(AbstractModel):
    """CreateDisks response structure.

    """

    def __init__(self):
        r"""
        :param DiskIdSet: List of IDs of the created cloud disks.
        :type DiskIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DiskIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DiskIdSet = params.get("DiskIdSet")
        self.RequestId = params.get("RequestId")


class CreateSnapshotRequest(AbstractModel):
    """CreateSnapshot request structure.

    """

    def __init__(self):
        r"""
        :param DiskId: ID of the cloud disk for which to create a snapshot, which can be queried through the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskId: str
        :param SnapshotName: Snapshot name. If it is not specified, "Unnamed" will be used by default.
        :type SnapshotName: str
        :param Deadline: Expiration time of the snapshot. It must be in UTC ISO-8601 format, such as 2022-01-08T09:47:55+00:00. The snapshot will be automatically deleted when it expires.
        :type Deadline: str
        :param DiskBackupId: ID of the cloud disk backup point. When this parameter is specified, the snapshot will be created from the backup point.
        :type DiskBackupId: str
        :param Tags: Tags bound to the snapshot.
        :type Tags: list of Tag
        """
        self.DiskId = None
        self.SnapshotName = None
        self.Deadline = None
        self.DiskBackupId = None
        self.Tags = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.SnapshotName = params.get("SnapshotName")
        self.Deadline = params.get("Deadline")
        self.DiskBackupId = params.get("DiskBackupId")
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
        


class CreateSnapshotResponse(AbstractModel):
    """CreateSnapshot response structure.

    """

    def __init__(self):
        r"""
        :param SnapshotId: ID of the new snapshot.
        :type SnapshotId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SnapshotId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.RequestId = params.get("RequestId")


class DeleteAutoSnapshotPoliciesRequest(AbstractModel):
    """DeleteAutoSnapshotPolicies request structure.

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyIds: List of scheduled snapshot policy IDs to be deleted.
        :type AutoSnapshotPolicyIds: list of str
        """
        self.AutoSnapshotPolicyIds = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoSnapshotPoliciesResponse(AbstractModel):
    """DeleteAutoSnapshotPolicies response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDiskBackupsRequest(AbstractModel):
    """DeleteDiskBackups request structure.

    """

    def __init__(self):
        r"""
        :param DiskBackupIds: ID of the cloud disk backup point to be deleted.
        :type DiskBackupIds: list of str
        """
        self.DiskBackupIds = None


    def _deserialize(self, params):
        self.DiskBackupIds = params.get("DiskBackupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDiskBackupsResponse(AbstractModel):
    """DeleteDiskBackups response structure.

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
        :param SnapshotIds: List of IDs of snapshots to be deleted, which can be queried via [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :type SnapshotIds: list of str
        :param DeleteBindImages: Whether to forcibly delete the image associated with the snapshot
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


class DescribeAutoSnapshotPoliciesRequest(AbstractModel):
    """DescribeAutoSnapshotPolicies request structure.

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyIds: List of scheduled snapshot policy IDs to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`.
        :type AutoSnapshotPolicyIds: list of str
        :param Filters: Filter conditions. Specification of both the `AutoSnapshotPolicyIds` and `Filters` parameters is not supported.<br><li>auto-snapshot-policy-id - Array of String - Required or not: No - (Filter condition) Filters according to the scheduled snapshot policy ID. The format of the scheduled snapshot policy ID is as follows: `asp-11112222`. <br><li>auto-snapshot-policy-state - Array of String - Required or not: No - (Filter condition) Filters according to the status of the scheduled snapshot policy. The format of the scheduled snapshot policy ID is as follows: `asp-11112222`. (NORMAL: normal | ISOLATED: isolated)<br><li>auto-snapshot-policy-name - Array of String - Required or not: No - (Filter condition) Filters according to the name of the scheduled snapshot policy.
        :type Filters: list of Filter
        :param Limit: Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param Offset: Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param Order: Outputs the ordering of the scheduled snapshot lists. Value range: <br><li>ASC: Ascending order <br><li>DESC: Descending order.
        :type Order: str
        :param OrderField: The sorting filter applied to the scheduled snapshot list. Value range: <Sort by creation time of scheduled snapshot. By default, this is sorted by creation time.
        :type OrderField: str
        """
        self.AutoSnapshotPolicyIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoSnapshotPoliciesResponse(AbstractModel):
    """DescribeAutoSnapshotPolicies response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The quantity of valid scheduled snapshot policies.
        :type TotalCount: int
        :param AutoSnapshotPolicySet: List of scheduled snapshot policies.
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AutoSnapshotPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicySet") is not None:
            self.AutoSnapshotPolicySet = []
            for item in params.get("AutoSnapshotPolicySet"):
                obj = AutoSnapshotPolicy()
                obj._deserialize(item)
                self.AutoSnapshotPolicySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskAssociatedAutoSnapshotPolicyRequest(AbstractModel):
    """DescribeDiskAssociatedAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param DiskId: The ID of the queried cloud disk.
        :type DiskId: str
        """
        self.DiskId = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskAssociatedAutoSnapshotPolicyResponse(AbstractModel):
    """DescribeDiskAssociatedAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The quantity of scheduled snapshots binded to cloud disk.
        :type TotalCount: int
        :param AutoSnapshotPolicySet: List of scheduled snapshots bound to cloud disk.
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AutoSnapshotPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicySet") is not None:
            self.AutoSnapshotPolicySet = []
            for item in params.get("AutoSnapshotPolicySet"):
                obj = AutoSnapshotPolicy()
                obj._deserialize(item)
                self.AutoSnapshotPolicySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskBackupsRequest(AbstractModel):
    """DescribeDiskBackups request structure.

    """

    def __init__(self):
        r"""
        :param DiskBackupIds: List of IDs of the backup points to be queried. `DiskBackupIds` and `Filters` cannot be specified at the same time.
        :type DiskBackupIds: list of str
        :param Filters: Filter. `DiskBackupIds` and `Filters` cannot be specified at the same time. Valid values: <br><li>disk-backup-id - Array of String - Required: No - (Filter) Filter by backup point ID in the format of `dbp-11112222`.
<br><li>disk-id - Array of String - Required: No - (Filter) Filter by ID of the cloud disk for which backup points are created.
<br><li>disk-usage - Array of String - Required: No - (Filter) Filter by type of the cloud disk for which backup points are created. (SYSTEM_DISK: System disk | DATA_DISK: Data disk)
        :type Filters: list of Filter
        :param Offset: Offset. Default value: 0. For more information on `Offset`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant section of the API [Overview](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param Order: Sorting order of cloud disk backup points. Valid values:<br><li>ASC: Ascending<br><li>DESC: Descending
        :type Order: str
        :param OrderField: The field by which cloud disk backup points are sorted. Valid values:<br><li>CREATE_TIME: Sort by creation time<br>Backup points are sorted by creation time by default.
        :type OrderField: str
        """
        self.DiskBackupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        self.DiskBackupIds = params.get("DiskBackupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskBackupsResponse(AbstractModel):
    """DescribeDiskBackups response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible cloud disk backup points.
        :type TotalCount: int
        :param DiskBackupSet: List of details of cloud disk backup points.
        :type DiskBackupSet: list of DiskBackup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DiskBackupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DiskBackupSet") is not None:
            self.DiskBackupSet = []
            for item in params.get("DiskBackupSet"):
                obj = DiskBackup()
                obj._deserialize(item)
                self.DiskBackupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskConfigQuotaRequest(AbstractModel):
    """DescribeDiskConfigQuota request structure.

    """

    def __init__(self):
        r"""
        :param InquiryType: Inquiry type. Value range: INQUIRY_CBS_CONFIG: query the configuration list of cloud disks <br><li>INQUIRY_CVM_CONFIG: query the configuration list of cloud disks and instances.
        :type InquiryType: str
        :param Zones: Query configuration under one or more [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo).
        :type Zones: list of str
        :param DiskChargeType: Billing mode. Value range: <br><li>POSTPAID_BY_HOUR: postpaid.
        :type DiskChargeType: str
        :param DiskTypes: Cloud disk media type. Valid values: <br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium Cloud Storage<br><li>CLOUD_SSD: SSD<br><li>CLOUD_HSSD: Enhanced SSD
        :type DiskTypes: list of str
        :param DiskUsage: The system disk or data disk. Value range: <br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk.
        :type DiskUsage: str
        :param InstanceFamilies: Filter by the instance model series, such as S1, I1 and M1. For more information, please see [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1)
        :type InstanceFamilies: list of str
        :param CPU: Instance CPU cores.
        :type CPU: int
        :param Memory: Instance memory size.
        :type Memory: int
        """
        self.InquiryType = None
        self.Zones = None
        self.DiskChargeType = None
        self.DiskTypes = None
        self.DiskUsage = None
        self.InstanceFamilies = None
        self.CPU = None
        self.Memory = None


    def _deserialize(self, params):
        self.InquiryType = params.get("InquiryType")
        self.Zones = params.get("Zones")
        self.DiskChargeType = params.get("DiskChargeType")
        self.DiskTypes = params.get("DiskTypes")
        self.DiskUsage = params.get("DiskUsage")
        self.InstanceFamilies = params.get("InstanceFamilies")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskConfigQuotaResponse(AbstractModel):
    """DescribeDiskConfigQuota response structure.

    """

    def __init__(self):
        r"""
        :param DiskConfigSet: List of cloud disk configurations.
        :type DiskConfigSet: list of DiskConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DiskConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskConfigSet") is not None:
            self.DiskConfigSet = []
            for item in params.get("DiskConfigSet"):
                obj = DiskConfig()
                obj._deserialize(item)
                self.DiskConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskOperationLogsRequest(AbstractModel):
    """DescribeDiskOperationLogs request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter conditions. The following conditions are supported:
<li>disk-id - Array of String - Required or not: Yes - Filter by cloud disk ID, with maximum of 10 cloud disk IDs able to be specified per request.
        :type Filters: list of Filter
        :param BeginTime: The start time of the operation logs to be queried, for example: '2019-11-22 00:00:00"
        :type BeginTime: str
        :param EndTime: The end time of the operation logs to be queried, for example: '2019-11-22 23:59:59"
        :type EndTime: str
        """
        self.Filters = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskOperationLogsResponse(AbstractModel):
    """DescribeDiskOperationLogs response structure.

    """

    def __init__(self):
        r"""
        :param DiskOperationLogSet: List of cloud disk operation logs.
        :type DiskOperationLogSet: list of DiskOperationLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DiskOperationLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskOperationLogSet") is not None:
            self.DiskOperationLogSet = []
            for item in params.get("DiskOperationLogSet"):
                obj = DiskOperationLog()
                obj._deserialize(item)
                self.DiskOperationLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    """DescribeDisks request structure.

    """

    def __init__(self):
        r"""
        :param DiskIds: Query by one or more cloud disk IDs, such as `disk-11112222`. For the format of this parameter, please see the ids.N section of the API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1). This parameter does not support specifying both `DiskIds` and `Filters`.
        :type DiskIds: list of str
        :param Filters: Filters. You cannot specify `DiskIds` and `Filters` at the same time. <br><li>disk-usage - Array of String - Optional - Filters by cloud disk type. (SYSTEM_DISK: system disk | DATA_DISK: data disk) <br><li>disk-charge-type - Array of String - Optional - Filters by cloud disk billing method. (POSTPAID_BY_HOUR: pay-as-you-go) <br><li>portable - Array of String- Optional - Filters by whether the cloud disk is elastic or not. (TRUE: elastic | FALSE: non-elastic) <br><li>project-id - Array of Integer - Optional - Filters by the ID of the project to which a cloud disk belongs. <br><li>disk-id - Array of String - Optional - Filters by cloud disk ID, such as `disk-11112222`. <br><li>disk-name - Array of String - Optional - Filters by cloud disk name. <br><li>disk-type - Array of String - Optional - Filters by cloud disk media type (CLOUD_BASIC: HDD cloud disk | CLOUD_PREMIUM: Premium Cloud Storage | CLOUD_SSD: SSD cloud disk.) <br><li>disk-state - Array of String - Optional - Filters by cloud disk state. (UNATTACHED: not mounted | ATTACHING: being mounted | ATTACHED: mounted | DETACHING: being unmounted | EXPANDING: being expanded | ROLLBACKING: being rolled back | TORECYCLE: to be repossessed.) <br><li>instance-id - Array of String - Optional - Filters by the ID of the CVM instance on which a cloud disk is mounted. You can use this parameter to query the cloud disks mounted on specific CVMs. <br><li>zone - Array of String - Optional - Filters by [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) <br><li>instance-ip-address - Array of String - Optional - Filters by the private or public IP of the CVM on which a cloud disk is mounted. <br><li>instance-name - Array of String - Optional - Filters by the name of the instance on which a cloud disk is mounted. <br><li>tag-key - Array of String - Optional - Filters by tag key. <br><li>tag-value - Array of String - Optional - Filters by tag value. <br><li>tag:tag-key - Array of String - Optional - Filters by tag key-value pair. Please replace `tag-key` with a specific tag key.
        :type Filters: list of Filter
        :param Offset: Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param Limit: Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param Order: Outputs the ordering of the cloud disk list. Value range: <br><li>ASC: Ascending order <br><li>DESC: Descending order.
        :type Order: str
        :param OrderField: The field by which the cloud disk list is sorted. Value range: <br><li>CREATE_TIME: sorted by the creation time of cloud disks <br><li>DEADLINE: sorted by the expiration time of cloud disks<br>By default, the cloud disk list is sorted by the creation time of cloud disks.
        :type OrderField: str
        :param ReturnBindAutoSnapshotPolicy: Whether the ID of the periodic snapshot policy bound to the cloud disk needs to be returned in the cloud disk details. TRUE: return; FALSE: do not return.
        :type ReturnBindAutoSnapshotPolicy: bool
        """
        self.DiskIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.ReturnBindAutoSnapshotPolicy = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        self.ReturnBindAutoSnapshotPolicy = params.get("ReturnBindAutoSnapshotPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksResponse(AbstractModel):
    """DescribeDisks response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The quantity of cloud disks meeting the conditions.
        :type TotalCount: int
        :param DiskSet: List of cloud disk details.
        :type DiskSet: list of Disk
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DiskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DiskSet") is not None:
            self.DiskSet = []
            for item in params.get("DiskSet"):
                obj = Disk()
                obj._deserialize(item)
                self.DiskSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesDiskNumRequest(AbstractModel):
    """DescribeInstancesDiskNum request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: ID of the CVM instance can be queried via the API [DescribeInstances](https://intl.cloud.tencent.com/document/product/213/15728?from_cn_redirect=1).
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDiskNumResponse(AbstractModel):
    """DescribeInstancesDiskNum response structure.

    """

    def __init__(self):
        r"""
        :param AttachDetail: The quantity of mounted and mountable elastic cloud disks for each cloud virtual machine
        :type AttachDetail: list of AttachDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AttachDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AttachDetail") is not None:
            self.AttachDetail = []
            for item in params.get("AttachDetail"):
                obj = AttachDetail()
                obj._deserialize(item)
                self.AttachDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotOperationLogsRequest(AbstractModel):
    """DescribeSnapshotOperationLogs request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter conditions. The following conditions are supported:
<li>snapshot-id - Array of String - Required or not: Yes - Filter by snapshot ID, with maximum of 10 snapshot IDs able to be specified per request.
        :type Filters: list of Filter
        :param BeginTime: The start time of the operation logs to be queried, for example: '2019-11-22 00:00:00"
        :type BeginTime: str
        :param EndTime: The end time of the operation logs to be queried, for example: '2019-11-22 23:59:59"
        :type EndTime: str
        """
        self.Filters = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotOperationLogsResponse(AbstractModel):
    """DescribeSnapshotOperationLogs response structure.

    """

    def __init__(self):
        r"""
        :param SnapshotOperationLogSet: List of snapshot operation logs.
        :type SnapshotOperationLogSet: list of SnapshotOperationLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SnapshotOperationLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SnapshotOperationLogSet") is not None:
            self.SnapshotOperationLogSet = []
            for item in params.get("SnapshotOperationLogSet"):
                obj = SnapshotOperationLog()
                obj._deserialize(item)
                self.SnapshotOperationLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotSharePermissionRequest(AbstractModel):
    """DescribeSnapshotSharePermission request structure.

    """

    def __init__(self):
        r"""
        :param SnapshotId: The ID of the snapshot to be queried. You can obtain this by using [DescribeSnapshots](https://intl.cloud.tencent.com/document/api/362/15647?from_cn_redirect=1).
        :type SnapshotId: str
        """
        self.SnapshotId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotSharePermissionResponse(AbstractModel):
    """DescribeSnapshotSharePermission response structure.

    """

    def __init__(self):
        r"""
        :param SharePermissionSet: The set of snapshot sharing information
        :type SharePermissionSet: list of SharePermission
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SharePermissionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SharePermissionSet") is not None:
            self.SharePermissionSet = []
            for item in params.get("SharePermissionSet"):
                obj = SharePermission()
                obj._deserialize(item)
                self.SharePermissionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param SnapshotIds: List of snapshot IDs to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`.
        :type SnapshotIds: list of str
        :param Filters: Filters. It cannot be specified together with `SnapshotIds`.<br><li>snapshot-id - Array of String - Optional - Filters by snapshot ID, such as `snap-11112222`.<br><li>snapshot-name - Array of String - Optional - Filters by snapshot name. <br><li>snapshot-state - Array of String - Optional - Filters by snapshot state (NORMAL: normal | CREATING: creating | ROLLBACKING: rolling back). <br><li>disk-usage - Array of String - Optional - Filters by the type of the cloud disk from which a snapshot is created (SYSTEM_DISK: system disk | DATA_DISK: data disk).<br><li>project-id - Array of String - Optional - Filters by the ID of the project to which a cloud disk belongs. <br><li>disk-id - Array of String - Optional - Filters by the ID of the cloud disk from which a snapshot is created.<br><li>zone - Array of String - Optional - Filters by [availability zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo).<br><li>encrypt - Array of String - Optional - Filters by whether a snapshot is created from an encrypted cloud disk. (TRUE: a snapshot of an encrypted cloud disk | FALSE: not a snapshot of an encrypted cloud disk.)
<li>snapshot-type- Array of String - Optional - Filters by the snapshot type specified in `snapshot-type`.
(SHARED_SNAPSHOT: a shared snapshot | PRIVATE_SNAPSHOT: a private snapshot.)
        :type Filters: list of Filter
        :param Offset: Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Offset: int
        :param Limit: Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/product/362/15633?from_cn_redirect=1).
        :type Limit: int
        :param Order: Outputs the ordering of the cloud disk list. Value range: <br><li>ASC: Ascending order <br><li>DESC: Descending order.
        :type Order: str
        :param OrderField: The field by which the snapshot list is sorted. Value range: <br><li>CREATE_TIME: sorted by the creation time of the snapshots <br>By default, the snapshot list is sorted by the creation time of snapshots.
        :type OrderField: str
        """
        self.SnapshotIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        self.SnapshotIds = params.get("SnapshotIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
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


class DetachDisksRequest(AbstractModel):
    """DetachDisks request structure.

    """

    def __init__(self):
        r"""
        :param DiskIds: IDs of the cloud disks to be unmounted, which can be queried via the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API. Up to 10 elastic cloud disks can be unmounted in a single request.
        :type DiskIds: list of str
        :param InstanceId: Indicates the CVM from which you want to unmount the disks. This parameter is only available for shared cloud disks.
        :type InstanceId: str
        """
        self.DiskIds = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachDisksResponse(AbstractModel):
    """DetachDisks response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Disk(AbstractModel):
    """The details of a cloud disk

    """

    def __init__(self):
        r"""
        :param DeleteWithInstance: Whether the cloud disk terminates along with the instance mounted to it. <br><li>true: Cloud disk will also be terminated when instance terminates, so only hourly postpaid cloud disk are supported.<br><li>false: Cloud disk does not terminate when instance terminates.
Note: This field may return null, indicating that no valid value was found.
        :type DeleteWithInstance: bool
        :param RenewFlag: Auto renewal flag. Supported values:<br><li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically<br><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically.
Note: This field may return null, indicating that no valid value was found.
        :type RenewFlag: str
        :param DiskType: Cloud disk types. Valid values: <br><li>CLOUD_BASIC: HDD cloud disk <br><li>CLOUD_PREMIUM: Premium Cloud Disk <br><li>CLOUD_BSSD: General Purpose SSD <br><li>CLOUD_SSD: SSD <br><li>CLOUD_HSSD: Enhanced SSD <br><li>CLOUD_TSSD: Tremendous SSD
        :type DiskType: str
        :param DiskState: The state of the cloud disk. Value range: <br><li>UNATTACHED: Not mounted <br><li>ATTACHING: Mounting <br><li>ATTACHED: Mounted <br><li>DETACHING: Un-mounting <br><li>EXPANDING: Expanding <br><li>ROLLBACKING: Rolling back <br><li>TORECYCE: Pending recycling. <br><li>DUMPING: Copying the hard drive.
        :type DiskState: str
        :param SnapshotCount: The total number of snapshots of the cloud disk.
        :type SnapshotCount: int
        :param AutoRenewFlagError: Cloud disk already mounted to CVM, and both CVM and cloud disk use monthly subscription.<br><li>true: CVM has auto-renewal flag set up, but cloud disk does not.<br><li>false: Cloud disk auto-renewal flag set up normally.
Note: This field may return null, indicating that no valid value was found.
        :type AutoRenewFlagError: bool
        :param Rollbacking: Whether the cloud disk is in the status of snapshot rollback. Value range: <br><li>false: No <br><li>true: Yes
        :type Rollbacking: bool
        :param InstanceIdList: For non-shareable cloud disks, this parameter is null. For shareable cloud disks, this parameters indicates this cloud disk's Instance IDs currently mounted to the CVM.
        :type InstanceIdList: list of str
        :param Encrypt: Whether the cloud disk is encrypted. Value range: <br><li>false: Not encrypted <br><li>true: Encrypted.
        :type Encrypt: bool
        :param DiskName: Cloud disk name.
        :type DiskName: str
        :param BackupDisk: Specifies whether to create a snapshot when the cloud disk is terminated due to overdue payment or expiration. `true`: create snapshot; `false`: do not create snapshot.
        :type BackupDisk: bool
        :param Tags: The tag bound to the cloud disk. The value Null is used when no tag is bound to the cloud disk.
Note: This field may return null, indicating that no valid value was found.
        :type Tags: list of Tag
        :param InstanceId: ID of the CVM to which the cloud disk is mounted.
        :type InstanceId: str
        :param AttachMode: Cloud disk mount method. Valid values: <br><li>PF: mount as a PF (Physical Function)<br><li>VF: mount as a VF (Virtual Function)
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AttachMode: str
        :param AutoSnapshotPolicyIds: ID of the periodic snapshot associated to the cloud disk. This parameter is returned only if the value of parameter ReturnBindAutoSnapshotPolicy is TRUE when the API DescribeDisks is called.
Note: This field may return null, indicating that no valid value was found.
        :type AutoSnapshotPolicyIds: list of str
        :param ThroughputPerformance: Extra performance for a cloud disk, in MB/sec.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ThroughputPerformance: int
        :param Migrating: Whether cloud disk is in process of type change. Value range: <br><li>false: Cloud disk not in process of type change. <br><li>true: Cloud disk type change has been launched, and migration is in process.
Note: This field may return null, indicating that no valid value was found.
        :type Migrating: bool
        :param DiskId: Cloud disk ID.
        :type DiskId: str
        :param SnapshotSize: The total capacity of the snapshots of the cloud disk. Unit: MB.
        :type SnapshotSize: int
        :param Placement: Location of the cloud disk.
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param IsReturnable: Determines whether or not prepaid cloud disk supports active return. <br><li>true: Active return supported.<br><li>false: Active return not supported.
Note: This field may return null, indicating that no valid value was found.
        :type IsReturnable: bool
        :param DeadlineTime: Expiration time of the cloud disk.
        :type DeadlineTime: str
        :param Attached: Whether the cloud disk is mounted to the CVM. Value range: <br><li>false: Unmounted <br><li>true: Mounted.
        :type Attached: bool
        :param DiskSize: Cloud disk size (in GB).
        :type DiskSize: int
        :param MigratePercent: Migration progress of cloud disk type change, from 0 to 100.
Note: This field may return null, indicating that no valid value was found.
        :type MigratePercent: int
        :param DiskUsage: Cloud disk type. Value range:<br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk.
        :type DiskUsage: str
        :param DiskChargeType: Billing method. Value range: <br><li>PREPAID: Prepaid, that is, monthly subscription<br><li>POSTPAID_BY_HOUR: Postpaid, that is, pay as you go.
        :type DiskChargeType: str
        :param Portable: Whether it is an elastic cloud disk. false: Non-elastic cloud disk; true: Elastic cloud disk.
        :type Portable: bool
        :param SnapshotAbility: Whether the cloud disk has the capability to create snapshots. Value range: <br><li>false: Cannot create snapshots. true: Can create snapshots.
        :type SnapshotAbility: bool
        :param DeadlineError: This field is only applicable when the instance is already mounted to the cloud disk, and both the instance and the cloud disk use monthly subscription. <br><li>true: Expiration time of cloud disk is earlier than that of the instance.<br><li>false:Expiration time of cloud disk is later than that of the instance.
Note: This field may return null, indicating that no valid value was found.
        :type DeadlineError: bool
        :param RollbackPercent: Rollback progress of a cloud disk snapshot.
        :type RollbackPercent: int
        :param DifferDaysOfDeadline: Number of days from current time until disk expiration (only applicable for prepaid disks).
Note: This field may return null, indicating that no valid value was found.
        :type DifferDaysOfDeadline: int
        :param ReturnFailCode: In circumstances where the prepaid cloud disk does not support active return, this parameter indicates the reason that return is not supported. Value range: <br><li>1: The cloud disk has already been returned. <br><li>2: The cloud disk has already expired. <br><li>3: The cloud disk does not support return. <br><li> 8: The limit on the number of returns is exceeded.
Note: This field may return null, indicating that no valid value was found.
        :type ReturnFailCode: int
        :param Shareable: Whether or not cloud disk is shareable cloud disk.
        :type Shareable: bool
        :param CreateTime: Creation time of the cloud disk.
        :type CreateTime: str
        :param DeleteSnapshot: Delete the associated non-permanently reserved snapshots upon deletion of the source cloud disk. `0`: No (default). `1`: Yes. To check whether a snapshot is permanently reserved, refer to the `IsPermanent` field returned by the `DescribeSnapshots` API. 
        :type DeleteSnapshot: int
        :param DiskBackupCount: Number of used cloud disk backups.
        :type DiskBackupCount: int
        :param InstanceType: Type of the instance mounted to the cloud disk. Valid values: <br><li>CVM<br><li>EKS
        :type InstanceType: str
        """
        self.DeleteWithInstance = None
        self.RenewFlag = None
        self.DiskType = None
        self.DiskState = None
        self.SnapshotCount = None
        self.AutoRenewFlagError = None
        self.Rollbacking = None
        self.InstanceIdList = None
        self.Encrypt = None
        self.DiskName = None
        self.BackupDisk = None
        self.Tags = None
        self.InstanceId = None
        self.AttachMode = None
        self.AutoSnapshotPolicyIds = None
        self.ThroughputPerformance = None
        self.Migrating = None
        self.DiskId = None
        self.SnapshotSize = None
        self.Placement = None
        self.IsReturnable = None
        self.DeadlineTime = None
        self.Attached = None
        self.DiskSize = None
        self.MigratePercent = None
        self.DiskUsage = None
        self.DiskChargeType = None
        self.Portable = None
        self.SnapshotAbility = None
        self.DeadlineError = None
        self.RollbackPercent = None
        self.DifferDaysOfDeadline = None
        self.ReturnFailCode = None
        self.Shareable = None
        self.CreateTime = None
        self.DeleteSnapshot = None
        self.DiskBackupCount = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.RenewFlag = params.get("RenewFlag")
        self.DiskType = params.get("DiskType")
        self.DiskState = params.get("DiskState")
        self.SnapshotCount = params.get("SnapshotCount")
        self.AutoRenewFlagError = params.get("AutoRenewFlagError")
        self.Rollbacking = params.get("Rollbacking")
        self.InstanceIdList = params.get("InstanceIdList")
        self.Encrypt = params.get("Encrypt")
        self.DiskName = params.get("DiskName")
        self.BackupDisk = params.get("BackupDisk")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.AttachMode = params.get("AttachMode")
        self.AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        self.ThroughputPerformance = params.get("ThroughputPerformance")
        self.Migrating = params.get("Migrating")
        self.DiskId = params.get("DiskId")
        self.SnapshotSize = params.get("SnapshotSize")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.IsReturnable = params.get("IsReturnable")
        self.DeadlineTime = params.get("DeadlineTime")
        self.Attached = params.get("Attached")
        self.DiskSize = params.get("DiskSize")
        self.MigratePercent = params.get("MigratePercent")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskChargeType = params.get("DiskChargeType")
        self.Portable = params.get("Portable")
        self.SnapshotAbility = params.get("SnapshotAbility")
        self.DeadlineError = params.get("DeadlineError")
        self.RollbackPercent = params.get("RollbackPercent")
        self.DifferDaysOfDeadline = params.get("DifferDaysOfDeadline")
        self.ReturnFailCode = params.get("ReturnFailCode")
        self.Shareable = params.get("Shareable")
        self.CreateTime = params.get("CreateTime")
        self.DeleteSnapshot = params.get("DeleteSnapshot")
        self.DiskBackupCount = params.get("DiskBackupCount")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskBackup(AbstractModel):
    """Cloud disk backup point.

    """

    def __init__(self):
        r"""
        :param DiskBackupId: Cloud disk backup point ID.
        :type DiskBackupId: str
        :param DiskId: ID of the cloud disk with which the backup point is associated.
        :type DiskId: str
        :param DiskSize: Cloud disk size in GB.
        :type DiskSize: int
        :param DiskUsage: Cloud disk type. Valid values:<br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk
        :type DiskUsage: str
        :param DiskBackupName: Backup point name.
        :type DiskBackupName: str
        :param DiskBackupState: Cloud disk backup point status. Valid values:<br><li>NORMAL: Normal<br><li>CREATING: Creating<br><li>ROLLBACKING: Rolling back
        :type DiskBackupState: str
        :param Percent: Cloud disk creation progress in percentage.
        :type Percent: int
        :param CreateTime: Creation time of the cloud disk backup point.
        :type CreateTime: str
        :param Encrypt: Whether the cloud disk is encrypted. Valid values: <br><li>false: Not encrypted <br><li>true: Encrypted
        :type Encrypt: bool
        """
        self.DiskBackupId = None
        self.DiskId = None
        self.DiskSize = None
        self.DiskUsage = None
        self.DiskBackupName = None
        self.DiskBackupState = None
        self.Percent = None
        self.CreateTime = None
        self.Encrypt = None


    def _deserialize(self, params):
        self.DiskBackupId = params.get("DiskBackupId")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskBackupName = params.get("DiskBackupName")
        self.DiskBackupState = params.get("DiskBackupState")
        self.Percent = params.get("Percent")
        self.CreateTime = params.get("CreateTime")
        self.Encrypt = params.get("Encrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskChargePrepaid(AbstractModel):
    """Billing mode of the instance

    """

    def __init__(self):
        r"""
        :param Period: Subscription period of the cloud disk in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param RenewFlag: Auto-renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: Notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: Notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify upon expiration nor renew automatically <br><br>Default value: NOTIFY_AND_MANUAL_RENEW.
        :type RenewFlag: str
        :param CurInstanceDeadline: You can specify this parameter when you need to ensure that a cloud disk and the CVM instance to which it is attached have the same expiration time. This parameter represents the current expiration time of the instance. In this case, if you specify `Period`, `Period` will represent how long you want to renew the instance, and the cloud disk will be renewed based on the new expiration time of the instance. For example, the value of this parameter can be `2018-03-30 20:15:03`.
        :type CurInstanceDeadline: str
        """
        self.Period = None
        self.RenewFlag = None
        self.CurInstanceDeadline = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        self.CurInstanceDeadline = params.get("CurInstanceDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskConfig(AbstractModel):
    """Cloud disk configuration.

    """

    def __init__(self):
        r"""
        :param Available: Whether the configuration is available.
        :type Available: bool
        :param DiskChargeType: Billing method. Value range: <br><li>PREPAID: Prepaid, that is, monthly subscription<br><li>POSTPAID_BY_HOUR: Postpaid, that is, pay as you go.
        :type DiskChargeType: str
        :param Zone: The [Availability Region](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) of the cloud drive.
        :type Zone: str
        :param InstanceFamily: Instance model series. For more information, please see [Instance Models](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1)
Note: This field may return null, indicating that no valid value was found.
        :type InstanceFamily: str
        :param DiskType: Type of cloud disk medium. Value range: <br><li>CLOUD_BASIC: Ordinary cloud disk <br><li>CLOUD_PREMIUM: Premium cloud storage <br><li>CLOUD_SSD: SSD cloud disk.
        :type DiskType: str
        :param StepSize: Minimum increment of cloud disk size adjustment in GB.
Note: This field might return null, indicating that no valid values can be obtained.
        :type StepSize: int
        :param ExtraPerformanceRange: Additional performance range.
Note: This field might return null, indicating that no valid values can be obtained.
        :type ExtraPerformanceRange: list of int
        :param DeviceClass: Instance model.
Note: This field may return null, indicating that no valid value was found.
        :type DeviceClass: str
        :param DiskUsage: Cloud disk type. Value range: <br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk.
        :type DiskUsage: str
        :param MinDiskSize: The minimum configurable cloud disk size (in GB).
        :type MinDiskSize: int
        :param MaxDiskSize: The maximum configurable cloud disk size (in GB).
        :type MaxDiskSize: int
        """
        self.Available = None
        self.DiskChargeType = None
        self.Zone = None
        self.InstanceFamily = None
        self.DiskType = None
        self.StepSize = None
        self.ExtraPerformanceRange = None
        self.DeviceClass = None
        self.DiskUsage = None
        self.MinDiskSize = None
        self.MaxDiskSize = None


    def _deserialize(self, params):
        self.Available = params.get("Available")
        self.DiskChargeType = params.get("DiskChargeType")
        self.Zone = params.get("Zone")
        self.InstanceFamily = params.get("InstanceFamily")
        self.DiskType = params.get("DiskType")
        self.StepSize = params.get("StepSize")
        self.ExtraPerformanceRange = params.get("ExtraPerformanceRange")
        self.DeviceClass = params.get("DeviceClass")
        self.DiskUsage = params.get("DiskUsage")
        self.MinDiskSize = params.get("MinDiskSize")
        self.MaxDiskSize = params.get("MaxDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskOperationLog(AbstractModel):
    """The operation log of the cloud disk.

    """

    def __init__(self):
        r"""
        :param Operator: UIN of operator.
        :type Operator: str
        :param Operation: Operation type. Value range:
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
        :param DiskId: Cloud disk ID of operation.
        :type DiskId: str
        :param OperationState: Status of operation. Value range:
SUCCESS: Operation successful 
FAILED: Operation failed 
PROCESSING: Operation in process
        :type OperationState: str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        """
        self.Operator = None
        self.Operation = None
        self.DiskId = None
        self.OperationState = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Operation = params.get("Operation")
        self.DiskId = params.get("DiskId")
        self.OperationState = params.get("OperationState")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Key-value pair filters for conditional filtering queries.

    """

    def __init__(self):
        r"""
        :param Name: Name of filter key.
        :type Name: str
        :param Values: One or more filter values.
        :type Values: list of str
        """
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
        


class GetSnapOverviewRequest(AbstractModel):
    """GetSnapOverview request structure.

    """


class GetSnapOverviewResponse(AbstractModel):
    """GetSnapOverview response structure.

    """

    def __init__(self):
        r"""
        :param TotalSize: The total snapshot size of the user
        :type TotalSize: float
        :param RealTradeSize: The total billed snapshot size of the user
        :type RealTradeSize: float
        :param FreeQuota: Free tier of snapshot
        :type FreeQuota: float
        :param TotalNums: Total number of snapshots
        :type TotalNums: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalSize = None
        self.RealTradeSize = None
        self.FreeQuota = None
        self.TotalNums = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalSize = params.get("TotalSize")
        self.RealTradeSize = params.get("RealTradeSize")
        self.FreeQuota = params.get("FreeQuota")
        self.TotalNums = params.get("TotalNums")
        self.RequestId = params.get("RequestId")


class Image(AbstractModel):
    """Image

    """

    def __init__(self):
        r"""
        :param ImageId: Image instance ID.
        :type ImageId: str
        :param ImageName: Image name.
        :type ImageName: str
        """
        self.ImageId = None
        self.ImageName = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitializeDisksRequest(AbstractModel):
    """InitializeDisks request structure.

    """

    def __init__(self):
        r"""
        :param DiskIds: ID list of the cloud disks to be reinitialized. Up to 20 disks can be reinitialized at a time.
        :type DiskIds: list of str
        """
        self.DiskIds = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitializeDisksResponse(AbstractModel):
    """InitializeDisks response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InquirePriceModifyDiskBackupQuotaRequest(AbstractModel):
    """InquirePriceModifyDiskBackupQuota request structure.

    """

    def __init__(self):
        r"""
        :param DiskId: Cloud disk ID, which can be queried through the `DescribeDisks` API.
        :type DiskId: str
        :param DiskBackupQuota: Cloud disk backup point quota after the modification, i.e., the number of backup points that a cloud disk can have.
        :type DiskBackupQuota: int
        """
        self.DiskId = None
        self.DiskBackupQuota = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDiskBackupQuotaResponse(AbstractModel):
    """InquirePriceModifyDiskBackupQuota response structure.

    """

    def __init__(self):
        r"""
        :param DiskPrice: Price of the cloud disk after its backup point quota is modified.
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = Price()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class InquirePriceModifyDiskExtraPerformanceRequest(AbstractModel):
    """InquirePriceModifyDiskExtraPerformance request structure.

    """

    def __init__(self):
        r"""
        :param DiskId: Cloud disk ID, which can be queried via the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskId: str
        :param ThroughputPerformance: The extra throughput to purchase, in MB/s
        :type ThroughputPerformance: int
        """
        self.DiskId = None
        self.ThroughputPerformance = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.ThroughputPerformance = params.get("ThroughputPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDiskExtraPerformanceResponse(AbstractModel):
    """InquirePriceModifyDiskExtraPerformance response structure.

    """

    def __init__(self):
        r"""
        :param DiskPrice: Price for purchasing the extra performance
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = Price()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateDisksRequest(AbstractModel):
    """InquiryPriceCreateDisks request structure.

    """

    def __init__(self):
        r"""
        :param DiskChargeType: Cloud disk billing mode. <br><li>POSTPAID_BY_HOUR: Hourly pay-as-you-go.
        :type DiskChargeType: str
        :param DiskType: Cloud disk media type. Valid values: <br><li>CLOUD_BASIC: HDD Cloud Storage<br><li>CLOUD_PREMIUM: Premium Cloud Disk<br><li>CLOUD_SSD: SSD<br><li>CLOUD_HSSD: Enhanced SSD<br><li>CLOUD_TSSD: ulTra SSD.
        :type DiskType: str
        :param DiskSize: Cloud disk size in GB. For the value range, see [Cloud Disk Types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        :param ProjectId: ID of the project to which the cloud disk belongs.
        :type ProjectId: int
        :param DiskCount: Number of cloud disks to be purchased. If it is not specified, `1` will be used by default.
        :type DiskCount: int
        :param ThroughputPerformance: Extra performance in MB/s purchased for a cloud disk.<br>This parameter is only valid for Enhanced SSD (CLOUD_HSSD) and ulTra SSD (CLOUD_TSSD).
        :type ThroughputPerformance: int
        :param DiskChargePrepaid: Relevant parameter settings for the prepaid mode (i.e., monthly subscription). The monthly subscription cloud disk purchase attributes such as usage period and whether or not auto-renewal is set up can be specified using this parameter. <br>This parameter is required when creating a prepaid cloud disk. This parameter is not required when creating an hourly postpaid cloud disk.
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param DiskBackupQuota: Specifies the cloud disk backup point quota.
        :type DiskBackupQuota: int
        """
        self.DiskChargeType = None
        self.DiskType = None
        self.DiskSize = None
        self.ProjectId = None
        self.DiskCount = None
        self.ThroughputPerformance = None
        self.DiskChargePrepaid = None
        self.DiskBackupQuota = None


    def _deserialize(self, params):
        self.DiskChargeType = params.get("DiskChargeType")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.ProjectId = params.get("ProjectId")
        self.DiskCount = params.get("DiskCount")
        self.ThroughputPerformance = params.get("ThroughputPerformance")
        if params.get("DiskChargePrepaid") is not None:
            self.DiskChargePrepaid = DiskChargePrepaid()
            self.DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self.DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateDisksResponse(AbstractModel):
    """InquiryPriceCreateDisks response structure.

    """

    def __init__(self):
        r"""
        :param DiskPrice: Describes the price of newly purchased cloud disks.
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = Price()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResizeDiskRequest(AbstractModel):
    """InquiryPriceResizeDisk request structure.

    """

    def __init__(self):
        r"""
        :param DiskId: ID of the cloud disk, which can be queried via the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1).
        :type DiskId: str
        :param DiskSize: Cloud disk size after scale out (in GB). This cannot be smaller than the current size of the cloud disk. For the value range of the cloud disk sizes, see cloud disk [Product Types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        :param ProjectId: ID of project the cloud disk belongs to. If selected, it can only be used for authentication.
        :type ProjectId: int
        """
        self.DiskId = None
        self.DiskSize = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResizeDiskResponse(AbstractModel):
    """InquiryPriceResizeDisk response structure.

    """

    def __init__(self):
        r"""
        :param DiskPrice: Describes the price of expanding the cloud disk.
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = PrepayPrice()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class ModifyAutoSnapshotPolicyAttributeRequest(AbstractModel):
    """ModifyAutoSnapshotPolicyAttribute request structure.

    """

    def __init__(self):
        r"""
        :param AutoSnapshotPolicyId: Scheduled snapshot policy ID.
        :type AutoSnapshotPolicyId: str
        :param IsActivated: Whether or not the scheduled snapshot policy is activated. FALSE: Not activated. TRUE: Activated. The default value is TRUE.
        :type IsActivated: bool
        :param IsPermanent: Whether the snapshot created by this scheduled snapshot policy is retained permanently. FALSE: Not retained permanently. TRUE: Retained permanently. The default value is FALSE.
        :type IsPermanent: bool
        :param AutoSnapshotPolicyName: The name of the scheduled snapshot policy to be created. If it is left empty, the default is 'Not named'. The maximum length cannot exceed 60 bytes.
        :type AutoSnapshotPolicyName: str
        :param Policy: The policy for executing the scheduled snapshot.
        :type Policy: list of Policy
        :param RetentionDays: Number of days to retain the snapshots created according to this scheduled snapshot policy. If this parameter is specified, `IsPermanent` cannot be specified as `TRUE`; otherwise, they will conflict with each other.
        :type RetentionDays: int
        """
        self.AutoSnapshotPolicyId = None
        self.IsActivated = None
        self.IsPermanent = None
        self.AutoSnapshotPolicyName = None
        self.Policy = None
        self.RetentionDays = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.IsActivated = params.get("IsActivated")
        self.IsPermanent = params.get("IsPermanent")
        self.AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        if params.get("Policy") is not None:
            self.Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self.Policy.append(obj)
        self.RetentionDays = params.get("RetentionDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoSnapshotPolicyAttributeResponse(AbstractModel):
    """ModifyAutoSnapshotPolicyAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDiskAttributesRequest(AbstractModel):
    """ModifyDiskAttributes request structure.

    """

    def __init__(self):
        r"""
        :param DiskIds: IDs of one or more cloud disks to be operated. If multiple cloud disk IDs are selected, it only supports modifying all cloud disks with the same attributes.
        :type DiskIds: list of str
        :param ProjectId: The new project ID of the cloud disk. Only the project ID of elastic cloud disk can be modified. The available projects and their IDs can be queried via the API [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1).
        :type ProjectId: int
        :param DiskName: Name of new cloud disk.
        :type DiskName: str
        :param Portable: Whether it is an elastic cloud disk. FALSE: non-elastic cloud disk; TRUE: elastic cloud disk. You can only modify non-elastic cloud disks to elastic cloud disks.
        :type Portable: bool
        :param DeleteWithInstance: Whether the cloud disk is terminated with the CVM after it has been successfully mounted. `TRUE` indicates that it is terminated with the CVM. `FALSE` indicates that it is not terminated with the CVM. This is only supported for cloud disks and data disks that are pay-as-you-go.
        :type DeleteWithInstance: bool
        :param DiskType: When changing the type of a cloud disk, this parameter can be passed to indicate the desired cloud disk type. Value range: <br><li>CLOUD_PREMIUM: Premium cloud storage.  <br><li>CLOUD_SSD: SSD cloud disk. <br>Currently, batch operations are not supported for changing type. That is, when `DiskType` is passed, only one cloud disk can be passed through `DiskIds`. <br>When the cloud disk type is changed, the changing of other attributes is not supported concurrently.
        :type DiskType: str
        """
        self.DiskIds = None
        self.ProjectId = None
        self.DiskName = None
        self.Portable = None
        self.DeleteWithInstance = None
        self.DiskType = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.ProjectId = params.get("ProjectId")
        self.DiskName = params.get("DiskName")
        self.Portable = params.get("Portable")
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskAttributesResponse(AbstractModel):
    """ModifyDiskAttributes response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDiskBackupQuotaRequest(AbstractModel):
    """ModifyDiskBackupQuota request structure.

    """

    def __init__(self):
        r"""
        :param DiskId: Cloud disk ID.
        :type DiskId: str
        :param DiskBackupQuota: Cloud disk backup point quota after the adjustment
        :type DiskBackupQuota: int
        """
        self.DiskId = None
        self.DiskBackupQuota = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.DiskBackupQuota = params.get("DiskBackupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskBackupQuotaResponse(AbstractModel):
    """ModifyDiskBackupQuota response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDiskExtraPerformanceRequest(AbstractModel):
    """ModifyDiskExtraPerformance request structure.

    """

    def __init__(self):
        r"""
        :param DiskId: ID of the cloud disk to create a snapshot, which can be obtained via the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API.
        :type DiskId: str
        :param ThroughputPerformance: The extra throughput to purchase, in MB/s
        :type ThroughputPerformance: int
        """
        self.DiskId = None
        self.ThroughputPerformance = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.ThroughputPerformance = params.get("ThroughputPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiskExtraPerformanceResponse(AbstractModel):
    """ModifyDiskExtraPerformance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotAttributeRequest(AbstractModel):
    """ModifySnapshotAttribute request structure.

    """

    def __init__(self):
        r"""
        :param SnapshotId: Snapshot ID, which can be queried via [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        :type SnapshotId: str
        :param SnapshotName: Name of new snapshot. Maximum length is 60 bytes.
        :type SnapshotName: str
        :param IsPermanent: Snapshot retention mode. Valid values: `FALSE`: non-permanent retention; `TRUE`: permanent retention.
        :type IsPermanent: bool
        :param Deadline: Expiration time of the snapshot. Setting this parameter will set the snapshot retention mode to `FALSE` (non-permanent retention) and the snapshot will be automatically deleted upon expiration.
        :type Deadline: str
        """
        self.SnapshotId = None
        self.SnapshotName = None
        self.IsPermanent = None
        self.Deadline = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.SnapshotName = params.get("SnapshotName")
        self.IsPermanent = params.get("IsPermanent")
        self.Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotAttributeResponse(AbstractModel):
    """ModifySnapshotAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotsSharePermissionRequest(AbstractModel):
    """ModifySnapshotsSharePermission request structure.

    """

    def __init__(self):
        r"""
        :param AccountIds: List of account IDs with which a snapshot is shared. For the format of array-type parameters, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/568?from_cn_redirect=1). You can find the account ID in [Account Information](https://console.cloud.tencent.com/developer).
        :type AccountIds: list of str
        :param Permission: Operations. Valid values: `SHARE`, sharing an image; `CANCEL`, cancelling the sharing of an image.
        :type Permission: str
        :param SnapshotIds: The ID of the snapshot. You can obtain this by using [DescribeSnapshots](https://intl.cloud.tencent.com/document/api/362/15647?from_cn_redirect=1).
        :type SnapshotIds: list of str
        """
        self.AccountIds = None
        self.Permission = None
        self.SnapshotIds = None


    def _deserialize(self, params):
        self.AccountIds = params.get("AccountIds")
        self.Permission = params.get("Permission")
        self.SnapshotIds = params.get("SnapshotIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotsSharePermissionResponse(AbstractModel):
    """ModifySnapshotsSharePermission response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Placement(AbstractModel):
    """This describes the abstract location of the instance, including the availability zone in which it is located, the projects to which it belongs, and the ID and name of the dedicated clusters to which it belongs.

    """

    def __init__(self):
        r"""
        :param Zone: The ID of the [Availability Zone](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#ZoneInfo) to which the cloud disk belongs. This parameter can be obtained from the Zone field in the returned values of [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1).
        :type Zone: str
        :param CageId: Cage ID. When it is an input parameter, the specified CageID resource is operated, and it can be left blank. When it is an output parameter, it is the ID of the cage the resource belongs to, and it can be left blank.
Note: This field may return null, indicating that no valid value was found.
        :type CageId: str
        :param ProjectId: ID of the project to which the instance belongs. This parameter can be obtained from the projectId field in the returned values of [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1). If this is left empty, default project is used.
        :type ProjectId: int
        :param CdcName: Dedicated cluster name. When it is an input parameter, it is ignored.  When it is an output parameter, it is the name of the dedicated cluster the cloud disk belongs to, and it can be left blank.
Note: This field may return null, indicating that no valid value was found.
        :type CdcName: str
        :param CdcId: ID of dedicated cluster which the instance belongs to. When it is an input parameter, the specified CdcId dedicated cluster resource is operated, and it can be left blank. When it is an output parameter, it is the ID of the dedicated cluster which the resource belongs to, and it can be left blank.
Note: This field may return null, indicating that no valid value was found.
        :type CdcId: str
        :param DedicatedClusterId: Dedicated cluster ID
        :type DedicatedClusterId: str
        """
        self.Zone = None
        self.CageId = None
        self.ProjectId = None
        self.CdcName = None
        self.CdcId = None
        self.DedicatedClusterId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.CageId = params.get("CageId")
        self.ProjectId = params.get("ProjectId")
        self.CdcName = params.get("CdcName")
        self.CdcId = params.get("CdcId")
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Policy(AbstractModel):
    """Execution policy for scheduled snapshot. It indicates that a scheduled snapshot policy is executed at the specified `Hour` in the days specified by `DayOfWeek` or `DayOfMonth` or once every `IntervalDays` days. Note: `DayOfWeek`, `DayOfMonth`, and `IntervalDays` are mutually exclusive, and only one policy rule can be set.

    """

    def __init__(self):
        r"""
        :param Hour: Specifies the time that that the scheduled snapshot policy will be triggered. The unit is hour. The value range is [0-23]. 00:00-23:00 is a total of 24 time points that can be selected. 1 indicates 01:00, and so on.
        :type Hour: list of int non-negative
        :param DayOfWeek: Specifies the days of the week, from Monday to Sunday, on which a scheduled snapshot will be triggered. Value range: [0, 6]. 0 indicates triggering on Sunday, 1-6 indicate triggering on Monday-Saturday.
        :type DayOfWeek: list of int non-negative
        """
        self.Hour = None
        self.DayOfWeek = None


    def _deserialize(self, params):
        self.Hour = params.get("Hour")
        self.DayOfWeek = params.get("DayOfWeek")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrepayPrice(AbstractModel):
    """The cost of a prepaid order.

    """

    def __init__(self):
        r"""
        :param OriginalPrice: Original payment of a monthly-subscribed cloud disk or a snapshot, in USD.
        :type OriginalPrice: float
        :param DiscountPrice: Discounted price of a monthly-subscribed cloud disk or a snapshot, in USD.
        :type DiscountPrice: float
        :param OriginalPriceHigh: Original payment of a monthly-subscribed cloud disk or a snapshot, in USD, with six decimal places.
        :type OriginalPriceHigh: str
        :param DiscountPriceHigh: Discounted price of a monthly-subscribed cloud disk or a snapshot, in USD, with six decimal places.
        :type DiscountPriceHigh: str
        :param UnitPrice: Original unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param ChargeUnit: Billing unit for pay-as-you-go cloud disks. Valid value: <br><li>HOUR: billed hourly.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ChargeUnit: str
        :param UnitPriceDiscount: Discount unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: float
        :param UnitPriceHigh: Original unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceHigh: str
        :param UnitPriceDiscountHigh: Discounted unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceDiscountHigh: str
        """
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.OriginalPriceHigh = None
        self.DiscountPriceHigh = None
        self.UnitPrice = None
        self.ChargeUnit = None
        self.UnitPriceDiscount = None
        self.UnitPriceHigh = None
        self.UnitPriceDiscountHigh = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.OriginalPriceHigh = params.get("OriginalPriceHigh")
        self.DiscountPriceHigh = params.get("DiscountPriceHigh")
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.UnitPriceDiscount = params.get("UnitPriceDiscount")
        self.UnitPriceHigh = params.get("UnitPriceHigh")
        self.UnitPriceDiscountHigh = params.get("UnitPriceDiscountHigh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """Describes the prepaid or postpaid price for the cloud disk.

    """

    def __init__(self):
        r"""
        :param OriginalPrice: Original price of a monthly-subscribed cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginalPrice: float
        :param DiscountPrice: Discounted price of a monthly-subscribed cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiscountPrice: float
        :param UnitPrice: Original unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPrice: float
        :param ChargeUnit: Billing unit of a postpaid cloud disk. Value range: <br><li>HOUR: Billed by hour.
Note: This field may return null, indicating that no valid value was found.
        :type ChargeUnit: str
        :param UnitPriceDiscount: Discount unit price of a pay-as-you-go cloud disk, in USD.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceDiscount: float
        :param OriginalPriceHigh: Original payment of a monthly-subscribed cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginalPriceHigh: str
        :param DiscountPriceHigh: Discounted payment price of a monthly-subscribed cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiscountPriceHigh: str
        :param UnitPriceHigh: Original unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceHigh: str
        :param UnitPriceDiscountHigh: Discounted unit price of a pay-as-you-go cloud disk, in USD, with six decimal places.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnitPriceDiscountHigh: str
        """
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.UnitPrice = None
        self.ChargeUnit = None
        self.UnitPriceDiscount = None
        self.OriginalPriceHigh = None
        self.DiscountPriceHigh = None
        self.UnitPriceHigh = None
        self.UnitPriceDiscountHigh = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.UnitPriceDiscount = params.get("UnitPriceDiscount")
        self.OriginalPriceHigh = params.get("OriginalPriceHigh")
        self.DiscountPriceHigh = params.get("DiscountPriceHigh")
        self.UnitPriceHigh = params.get("UnitPriceHigh")
        self.UnitPriceDiscountHigh = params.get("UnitPriceDiscountHigh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskRequest(AbstractModel):
    """ResizeDisk request structure.

    """

    def __init__(self):
        r"""
        :param DiskId: ID of the cloud disk, which can be queried via the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1).
        :type DiskId: str
        :param DiskSize: Cloud disk size after scale out (in GB). This must be larger than the current size of the cloud disk. For the value range of the cloud disk sizes, see cloud disk [Product Types](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1).
        :type DiskSize: int
        """
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskResponse(AbstractModel):
    """ResizeDisk response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SharePermission(AbstractModel):
    """Snapshot sharing information set

    """

    def __init__(self):
        r"""
        :param CreatedTime: Snapshot sharing time
        :type CreatedTime: str
        :param AccountId: ID of the shared account
        :type AccountId: str
        """
        self.CreatedTime = None
        self.AccountId = None


    def _deserialize(self, params):
        self.CreatedTime = params.get("CreatedTime")
        self.AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """The details of a snapshot

    """

    def __init__(self):
        r"""
        :param Placement: Location of the snapshot.
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param CopyFromRemote: Whether the snapshot is replicated across regions. Value range: <br><li>true: Indicates that the snapshot is replicated across regions. <br><li>false: Indicates that the snapshot belongs to the local region.
        :type CopyFromRemote: bool
        :param SnapshotState: Snapshot status. Valid values: <br><li>NORMAL: normal <br><li>CREATING: creating<br><li>ROLLBACKING: rolling back<br><li>COPYING_FROM_REMOTE: cross-region replicating<li>CHECKING_COPIED: verifying the cross-region replicated data<br><li>TORECYCLE: to be repossessed.
        :type SnapshotState: str
        :param IsPermanent: Whether it is a permanent snapshot. Value range: <br><li>true: Permanent snapshot <br><li>false: Non-permanent snapshot.
        :type IsPermanent: bool
        :param SnapshotName: Snapshot name, the user-defined snapshot alias. Call [ModifySnapshotAttribute](https://intl.cloud.tencent.com/document/product/362/15650?from_cn_redirect=1) to modify this field.
        :type SnapshotName: str
        :param DeadlineTime: The expiration time of the snapshot. If the snapshot is permanently retained, this field is blank.
        :type DeadlineTime: str
        :param Percent: The progress percentage for snapshot creation. This field is always 100 after the snapshot is created successfully.
        :type Percent: int
        :param Images: List of images associated with snapshot.
        :type Images: list of Image
        :param ShareReference: Number of snapshots currently shared
        :type ShareReference: int
        :param SnapshotType: Snapshot type. This value can currently be either PRIVATE_SNAPSHOT or SHARED_SNAPSHOT.
        :type SnapshotType: str
        :param DiskSize: Size of the cloud disk used to create this snapshot (in GB).
        :type DiskSize: int
        :param DiskId: ID of the cloud disk used to create this snapshot.
        :type DiskId: str
        :param CopyingToRegions: The destination region to which the snapshot is being replicated. Default value is [ ].
        :type CopyingToRegions: list of str
        :param Encrypt: Whether the snapshot is created from an encrypted disk. Value range: <br><li>true: Yes <br><li>false: No.
        :type Encrypt: bool
        :param CreateTime: Creation time of the snapshot.
        :type CreateTime: str
        :param ImageCount: Number of images associated with snapshot.
        :type ImageCount: int
        :param DiskUsage: The type of the cloud disk used to create the snapshot. Value range: <br><li>SYSTEM_DISK: System disk <br><li>DATA_DISK: Data disk.
        :type DiskUsage: str
        :param SnapshotId: Snapshot ID.
        :type SnapshotId: str
        :param TimeStartShare: The time when the snapshot sharing starts
        :type TimeStartShare: str
        :param Tags: List of tags associated with the snapshot.
        :type Tags: list of Tag
        """
        self.Placement = None
        self.CopyFromRemote = None
        self.SnapshotState = None
        self.IsPermanent = None
        self.SnapshotName = None
        self.DeadlineTime = None
        self.Percent = None
        self.Images = None
        self.ShareReference = None
        self.SnapshotType = None
        self.DiskSize = None
        self.DiskId = None
        self.CopyingToRegions = None
        self.Encrypt = None
        self.CreateTime = None
        self.ImageCount = None
        self.DiskUsage = None
        self.SnapshotId = None
        self.TimeStartShare = None
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CopyFromRemote = params.get("CopyFromRemote")
        self.SnapshotState = params.get("SnapshotState")
        self.IsPermanent = params.get("IsPermanent")
        self.SnapshotName = params.get("SnapshotName")
        self.DeadlineTime = params.get("DeadlineTime")
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
        self.Encrypt = params.get("Encrypt")
        self.CreateTime = params.get("CreateTime")
        self.ImageCount = params.get("ImageCount")
        self.DiskUsage = params.get("DiskUsage")
        self.SnapshotId = params.get("SnapshotId")
        self.TimeStartShare = params.get("TimeStartShare")
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
        


class SnapshotCopyResult(AbstractModel):
    """Result of the cross-region replication task

    """

    def __init__(self):
        r"""
        :param SnapshotId: ID of the snapshot replica
        :type SnapshotId: str
        :param Message: Error message. It’s null if the request succeeds.
        :type Message: str
        :param Code: Error code. It’s `Success` if the request succeeds.
        :type Code: str
        :param DestinationRegion: Destination region of the replication task
        :type DestinationRegion: str
        """
        self.SnapshotId = None
        self.Message = None
        self.Code = None
        self.DestinationRegion = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        self.DestinationRegion = params.get("DestinationRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotOperationLog(AbstractModel):
    """The snapshot operation log.

    """

    def __init__(self):
        r"""
        :param Operator: UIN of operator.
Note: This field may return null, indicating that no valid value was found.
        :type Operator: str
        :param Operation: Operation type. Value range:
SNAP_OPERATION_DELETE: Delete snapshot
SNAP_OPERATION_ROLLBACK: Roll back snapshot
SNAP_OPERATION_MODIFY: Modify snapshot attributes
SNAP_OPERATION_CREATE: Create snapshot
SNAP_OPERATION_COPY: Cross-region replication of snapshot
ASP_OPERATION_CREATE_SNAP: Create snapshot with scheduled snapshot policy
ASP_OPERATION_DELETE_SNAP: Delete snapshot from scheduled snapshot policy
        :type Operation: str
        :param SnapshotId: ID of snapshot being operated.
        :type SnapshotId: str
        :param OperationState: Status of operation. Value range:
SUCCESS: Operation successful 
FAILED: Operation failed 
PROCESSING: Operation in process
        :type OperationState: str
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        """
        self.Operator = None
        self.Operation = None
        self.SnapshotId = None
        self.OperationState = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Operation = params.get("Operation")
        self.SnapshotId = params.get("SnapshotId")
        self.OperationState = params.get("OperationState")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag.

    """

    def __init__(self):
        r"""
        :param Key: Tag key.
        :type Key: str
        :param Value: Tag value.
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
        


class TerminateDisksRequest(AbstractModel):
    """TerminateDisks request structure.

    """

    def __init__(self):
        r"""
        :param DiskIds: List of cloud disk IDs required to be returned.
        :type DiskIds: list of str
        :param DeleteSnapshot: Delete the associated non-permanently reserved snapshots upon deletion of the source cloud disk. `0`: No (default). `1`: Yes. To check whether a snapshot is permanently reserved, refer to the `IsPermanent` field returned by the `DescribeSnapshots` API. 
        :type DeleteSnapshot: int
        """
        self.DiskIds = None
        self.DeleteSnapshot = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.DeleteSnapshot = params.get("DeleteSnapshot")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDisksResponse(AbstractModel):
    """TerminateDisks response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindAutoSnapshotPolicyRequest(AbstractModel):
    """UnbindAutoSnapshotPolicy request structure.

    """

    def __init__(self):
        r"""
        :param DiskIds: List of cloud disk IDs scheduled snapshot policy to be unbound from.
        :type DiskIds: list of str
        :param AutoSnapshotPolicyId: ID of scheduled snapshot policy to be unbound.
        :type AutoSnapshotPolicyId: str
        """
        self.DiskIds = None
        self.AutoSnapshotPolicyId = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoSnapshotPolicyResponse(AbstractModel):
    """UnbindAutoSnapshotPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")