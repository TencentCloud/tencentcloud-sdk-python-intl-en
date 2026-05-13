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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.cbs.v20170312 import models
from typing import Dict


class CbsClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'cbs.intl.tencentcloudapi.com'
    _service = 'cbs'

    async def ApplyDiskBackup(
            self,
            request: models.ApplyDiskBackupRequest,
            opts: Dict = None,
    ) -> models.ApplyDiskBackupResponse:
        """
        This API is used to roll back a backup to the original cloud disk.

        This API only supports rolling back to the original cloud disk. For data disk backup points, if you need to copy backup point data to other CBS, use first [CreateSnapshot](https://www.tencentcloud.com/document/product/362/15648?from_cn_redirect=1) to convert the backup point to a snapshot, and use [CreateDisks](https://www.tencentcloud.com/document/product/362/16312?from_cn_redirect=1) to create a new elastic cloud disk, then copy snapshot data to the newly purchased cloud disk.
        The backup point used for rollback must be in NORMAL status. The backup point status can be checked through the [DescribeDiskBackups](https://www.tencentcloud.com/document/product/362/80278?from_cn_redirect=1) API, see BackupState field explanation in the output parameter.
        If it is an elastic cloud disk, the CBS must be in an unmounted state. The CBS mount status can be queried through the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API. See Attached field explanation. If it is a non-elastic cloud hard disk purchased together with the instance, the instance must be in a powered off state. The instance status can be queried through the [DescribeInstancesStatus](https://www.tencentcloud.com/document/product/213/15738?from_cn_redirect=1) API.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyDiskBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyDiskBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplySnapshot(
            self,
            request: models.ApplySnapshotRequest,
            opts: Dict = None,
    ) -> models.ApplySnapshotResponse:
        """
        This API (ApplySnapshot) is used to roll back a snapshot to the original cloud disk.

        * The snapshot can only be rolled back to the original cloud disk. For data disk snapshots, if you need to copy the snapshot data to other cloud disks, use the API [CreateDisks](https://intl.cloud.tencent.com/document/product/362/16312?from_cn_redirect=1) to create an elastic cloud disk and then copy the snapshot data to the created cloud disk.
        * The snapshot for rollback must be in NORMAL status. The snapshot status can be queried in the SnapshotState field in the output parameters through the API [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        * For elastic cloud disks, the cloud disk must be in UNMOUNTED status. The cloud disk status can be queried in the Attached field returned by the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1). For non-elastic cloud disks purchased together with instances, the instance must be in SHUTDOWN status. The instance status can be queried through the API [DescribeInstancesStatus](https://intl.cloud.tencent.com/document/product/213/15738?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ApplySnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplySnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplySnapshotGroup(
            self,
            request: models.ApplySnapshotGroupRequest,
            opts: Dict = None,
    ) -> models.ApplySnapshotGroupResponse:
        """
        This API is used to rollback a snapshot group and restore the instance to the state at the moment the snapshot group was created.
        This API is used to roll back all or part of the disks in the snapshot group.
        This API is used to roll back disks. If the disks to be rolled back contain mounted disks, they must be mounted to the same instance, and the instance must be shut down before rollback.
        Rollback is an asynchronous operation. A successful API return does not indicate a successful rollback. You can call DescribeSnapshotGroups to check the snapshot group status.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplySnapshotGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplySnapshotGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachDisks(
            self,
            request: models.AttachDisksRequest,
            opts: Dict = None,
    ) -> models.AttachDisksResponse:
        """
        This API is used to mount one or more cloud disks.

        * Batch operation is supported. You can mount multiple cloud disks to one CVM in a single request. If any of these cloud disks cannot be mounted, the operation fails and a specific error code returns.
        * This is an async API. A successful request indicates that the mounting is initiated. You can call the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API to query the status of cloud disks. If the status changes from `ATTACHING` to `ATTACHED`, the mounting is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindAutoSnapshotPolicy(
            self,
            request: models.BindAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.BindAutoSnapshotPolicyResponse:
        """
        This API (BindAutoSnapshotPolicy) is used to bind the cloud disk to the specified scheduled snapshot policy.

        * For the scheduled snapshot policy limit of each region, see [Scheduled Snapshots](https://intl.cloud.tencent.com/document/product/362/8191?from_cn_redirect=1).
        * When a cloud disk that is bound to a scheduled snapshot policy is in the unused state (that is, an elastic cloud disk has not been mounted or the server of an inelastic disk is powered off) scheduled snapshots are not created.
        """
        
        kwargs = {}
        kwargs["action"] = "BindAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopySnapshotCrossRegions(
            self,
            request: models.CopySnapshotCrossRegionsRequest,
            opts: Dict = None,
    ) -> models.CopySnapshotCrossRegionsResponse:
        """
        This API is used to replicate snapshots across regions.

        This API is asynchronous. When the cross-region replication request is issued successfully, it returns a new snapshot ID. At this point, the snapshot is not immediately replicated to the target region. You can use the [DescribeSnapshots](https://www.tencentcloud.com/document/product/362/15647?from_cn_redirect=1) API for the query in the target region to check the snapshot status and determine whether the replication is complete. If the snapshot status is "NORMAL", it indicates snapshot replication is complete.
        This API is used to perform snapshot cross-region replication, which will generate cross-region traffic. Commercial billing for this feature is expected in Q3 2025. Please check subsequent Message Center notices to avoid unexpected charges.
        """
        
        kwargs = {}
        kwargs["action"] = "CopySnapshotCrossRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopySnapshotCrossRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoSnapshotPolicy(
            self,
            request: models.CreateAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAutoSnapshotPolicyResponse:
        """
        This API (CreateAutoSnapshotPolicy) is used to create a scheduled snapshot policy.

        * For the limits on the number of scheduled snapshot policies that can be created in each region, see [Scheduled Snapshots](https://intl.cloud.tencent.com/document/product/362/8191?from_cn_redirect=1).
        * The quantity and capacity of the snapshots that can be created in each region are limited. For more information, see the **Snapshots** page on the Tencent Cloud Console. If the number of snapshots exceeds the quota, the creation of the scheduled snapshots will fail.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDiskBackup(
            self,
            request: models.CreateDiskBackupRequest,
            opts: Dict = None,
    ) -> models.CreateDiskBackupResponse:
        """
        This API is used to create a backup point for a cloud disk.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDiskBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDiskBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDisks(
            self,
            request: models.CreateDisksRequest,
            opts: Dict = None,
    ) -> models.CreateDisksResponse:
        """
        This API is used to create cloud disks.

        * This API supports creating a cloud disk with a data disk snapshot so that the snapshot data can be copied to the purchased cloud disk.
        * This API is async. A cloud disk ID list will be returned when a request is made successfully, but it does not mean that the creation has been completed. You can call the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API to query cloud disks by `DiskId`. If a new cloud disk can be found and its status is `UNATTACHED` or `ATTACHED`, the cloud disk has been created successfully.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshot(
            self,
            request: models.CreateSnapshotRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotResponse:
        """
        This API is used to create a snapshot for the specified cloud disk.

        * You can only create snapshots for cloud disks with the snapshot capability. To check whether a cloud disk is snapshot-enabled, call the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API and see the `SnapshotAbility` field in the response.
        * For the maximum number of snapshots that can be created, see [Use Limits](https://intl.cloud.tencent.com/doc/product/362/5145?from_cn_redirect=1).
        * Currently, you can convert backup points into general snapshots. After the conversion, snapshot usage fees may be charged, backup points will not be retained, and the occupied backup point quota will be released.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshotGroup(
            self,
            request: models.CreateSnapshotGroupRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotGroupResponse:
        """
        This API is used to create a snapshot group.
        This API is used to create snapshot groups. The CBS list must be mounted on the same instance.
        This API is used to create snapshot groups for all or some of the disks mounted to instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshotGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoSnapshotPolicies(
            self,
            request: models.DeleteAutoSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoSnapshotPoliciesResponse:
        """
        This API (DeleteAutoSnapshotPolicies) is used to delete scheduled snapshot policies.

        * Batch operations are supported. If one of the scheduled snapshot policies in a batch cannot be deleted, the operation is not performed and a specific error code is returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDiskBackups(
            self,
            request: models.DeleteDiskBackupsRequest,
            opts: Dict = None,
    ) -> models.DeleteDiskBackupsResponse:
        """
        This API is used to delete the backup points of the specified cloud disk in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDiskBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDiskBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshotGroup(
            self,
            request: models.DeleteSnapshotGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotGroupResponse:
        """
        This API is used to delete snapshot groups. One snapshot group can be deleted per call.
        This API is used to delete all snapshots in the snapshot group by default.
        This API is used to delete a snapshot group. If a snapshot in the snapshot group has an associated image, deletion will fail and no snapshot will be deleted. Parameters can be input to enable simultaneous deletion of images bound to the snapshot by setting DeleteBindImages equal to true.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshotGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshots(
            self,
            request: models.DeleteSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotsResponse:
        """
        This API is used to delete snapshots.

        * Only snapshots in the `NORMAL` state can be deleted. To query the state of a snapshot, you can call the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API and check the `SnapshotState` field in the response.
        * Batch operations are supported. If there is any snapshot that cannot be deleted, the operation will not be performed and a specific error code will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoSnapshotPolicies(
            self,
            request: models.DescribeAutoSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoSnapshotPoliciesResponse:
        """
        This API is used to query scheduled snapshot policies.

        * You can filter scheduled snapshot policies by ID, name, state, etc. The relationship between different filters is logical `AND`. For details on filters, see `Filter`.
        * If no parameter is specified, a certain number of scheduled snapshot policies under the current account will be returned. The number is specified by `Limit` and is 20 by default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiskAssociatedAutoSnapshotPolicy(
            self,
            request: models.DescribeDiskAssociatedAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeDiskAssociatedAutoSnapshotPolicyResponse:
        """
        This API (DescribeDiskAssociatedAutoSnapshotPolicy) is used to query the scheduled snapshot policy bound to a cloud disk.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiskAssociatedAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiskAssociatedAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiskBackups(
            self,
            request: models.DescribeDiskBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDiskBackupsResponse:
        """
        This API is used to query the details of backup points.

        You can filter results by backup point ID. You can also look for certain backup points by specifying the ID or type of the cloud disk for which the backup points are created. The relationship between different filters is logical `AND`. For more information on filters, see `Filter`.
        If the parameter is empty, a certain number (as specified by `Limit` and 20 by default) of backup points will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiskBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiskBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiskConfigQuota(
            self,
            request: models.DescribeDiskConfigQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeDiskConfigQuotaResponse:
        """
        This API (DescribeDiskConfigQuota) is used to query the cloud disk quota.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiskConfigQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiskConfigQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisks(
            self,
            request: models.DescribeDisksRequest,
            opts: Dict = None,
    ) -> models.DescribeDisksResponse:
        """
        This API (DescribeDisks) is used to query the list of cloud disks.

        * The details of the cloud disk can be queried based on the ID, type or status of the cloud disk. The relationship between different conditions is AND. For more information about filtering, please see the `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of cloud disk lists are returned to the current user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesDiskNum(
            self,
            request: models.DescribeInstancesDiskNumRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesDiskNumResponse:
        """
        This API (DescribeInstancesDiskNum) is used to query the number of cloud disks mounted in the instance.

        * Batch operations are supported. If multiple CVM instance IDs are specified, the returned results will list the number of cloud disks mounted on each CVM.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesDiskNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesDiskNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotGroups(
            self,
            request: models.DescribeSnapshotGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotGroupsResponse:
        """
        This API is used to query the snapshot group list.
        This API is used to query the snapshot group list based on snapshot group ID, snapshot group status or snapshot ID associated with the snapshot group. The relationship among different criteria is AND. For detailed filtering information, see `Filter`.
        If the parameter is empty, a certain number of the cloud disk list for the current user is returned (specified by `Limit`, defaults to 20).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotOverview(
            self,
            request: models.DescribeSnapshotOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotOverviewResponse:
        """
        This API is used to query the usage overview of user snapshots, including total snapshot capacity, cost capacity, etc.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotSharePermission(
            self,
            request: models.DescribeSnapshotSharePermissionRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotSharePermissionResponse:
        """
        This API is used to query the sharing information of snapshots.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotSharePermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotSharePermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshots(
            self,
            request: models.DescribeSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotsResponse:
        """
        This API (DescribeSnapshots) is used to query the details of snapshots.

        * Filter the results by the snapshot ID, the ID of cloud disk, for which the snapshot is created, and the type of cloud disk, for which the snapshot is created. The relationship between different conditions is AND. For more information about filtering, please see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of snapshot lists are returned to the current user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachDisks(
            self,
            request: models.DetachDisksRequest,
            opts: Dict = None,
    ) -> models.DetachDisksResponse:
        """
        This API is used to unmount one or more cloud disks.

        * Batch operation is supported. You can unmount multiple cloud disks from the same CVM in a single request. If any of these cloud disks cannot be unmounted, the operation fails and a specific error code returns.
        * This is an async API. A successful request does not mean that the cloud disks have been unmounted successfully. You can call the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API to query the status of cloud disks. When the status changes from `ATTACHED` to `UNATTACHED`, the unmounting is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSnapOverview(
            self,
            request: models.GetSnapOverviewRequest,
            opts: Dict = None,
    ) -> models.GetSnapOverviewResponse:
        """
        This API is used to standardize API naming. This API will be decommissioned and replaced by the new API named DescribeSnapshotOverview.

        This API is used to obtain snapshot overview information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSnapOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSnapOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InitializeDisks(
            self,
            request: models.InitializeDisksRequest,
            opts: Dict = None,
    ) -> models.InitializeDisksResponse:
        """
        This API is used to reinitialize the cloud disks. Note the following when reinitializing the cloud disks:
        1. For a cloud disk created from a snapshot, it is rolled back to the state of the snapshot;
        2. For a cloud disk created from the scratch, all data are cleared. Please check and back up the necessary data before the reinitialization;
        3. Currently, you can only re-initialize a cloud disk when it’s not attached to a resource and not shared by others;
        4. For a cloud disk created from a snapshot, if the snapshot has been deleted, it cannot be reinitialized.
        """
        
        kwargs = {}
        kwargs["action"] = "InitializeDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InitializeDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceModifyDiskBackupQuota(
            self,
            request: models.InquirePriceModifyDiskBackupQuotaRequest,
            opts: Dict = None,
    ) -> models.InquirePriceModifyDiskBackupQuotaResponse:
        """
        This API is used to query the price of a cloud disk after its backup point quota is modified.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceModifyDiskBackupQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceModifyDiskBackupQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceModifyDiskExtraPerformance(
            self,
            request: models.InquirePriceModifyDiskExtraPerformanceRequest,
            opts: Dict = None,
    ) -> models.InquirePriceModifyDiskExtraPerformanceResponse:
        """
        This API is used to query the price for adjusting the cloud disk’s extra performance.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceModifyDiskExtraPerformance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceModifyDiskExtraPerformanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateDisks(
            self,
            request: models.InquiryPriceCreateDisksRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateDisksResponse:
        """
        This API is used to query the price of creating cloud disks.

        * You can query the price of creating multiple cloud disks in a single request. In this case, the price returned will be the total price.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewDisks(
            self,
            request: models.InquiryPriceRenewDisksRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewDisksResponse:
        """
        This API is used to query the renewal price of CBS.

        This API is used to support renewal along with mounted instances. The parameter specifies CurInstanceDeadline in [DiskChargePrepaid](https://www.tencentcloud.com/document/product/362/15669?from_cn_redirect=1#DiskChargePrepaid), and renewal will be performed at the expiry date after the instance is renewed.
        This API is used to support specifying different renewal durations for multiple cloud disks. The total price for renewing multiple cloud disks is returned.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceResizeDisk(
            self,
            request: models.InquiryPriceResizeDiskRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceResizeDiskResponse:
        """
        This API is used to query the price for expanding cloud disks.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceResizeDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceResizeDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoSnapshotPolicyAttribute(
            self,
            request: models.ModifyAutoSnapshotPolicyAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoSnapshotPolicyAttributeResponse:
        """
        This API (ModifyAutoSnapshotPolicyAttribute) is used to modify the attributes of an automatic snapshot policy.

        * You can use this API to modify the attributes of a scheduled snapshot policy, including the execution policy, name, and activation.
        * When modifying the number of days for retention, you must ensure that there is no clash with the permanent retention attribute. Otherwise, the entire operation will fail and a specific error code will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoSnapshotPolicyAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoSnapshotPolicyAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDiskAttributes(
            self,
            request: models.ModifyDiskAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyDiskAttributesResponse:
        """
        This API is used to modify only the Project ID of elastic cloud disks. The Project ID of a cloud disk created with a host is linked to the host. Whether a cloud disk is elastic can be checked through the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API. See the Portable field explanation in the output parameters.
        The "cloud disk name" is only for ease of management for users. Tencent Cloud does not use this name as a basis for submitting tickets or performing cloud disk management operations.
        This API is used to support batch operations. If multiple cloud disk IDs are passed in, modify cloud disks to the same attribute. If there is a cloud disk that does not allow operation, the operation will not be executed and return a specific error code.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDiskAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDiskAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDiskBackupQuota(
            self,
            request: models.ModifyDiskBackupQuotaRequest,
            opts: Dict = None,
    ) -> models.ModifyDiskBackupQuotaResponse:
        """
        This API is used to modify the cloud disk backup point quota.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDiskBackupQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDiskBackupQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDiskExtraPerformance(
            self,
            request: models.ModifyDiskExtraPerformanceRequest,
            opts: Dict = None,
    ) -> models.ModifyDiskExtraPerformanceResponse:
        """
        This API is used to adjust extra performance for Enhanced SSD (CLOUD_HSSD) and ulTra SSD.

        *This API only supports adjust extra performance for Enhanced SSD and ulTra SSD.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDiskExtraPerformance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDiskExtraPerformanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshotAttribute(
            self,
            request: models.ModifySnapshotAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotAttributeResponse:
        """
        This API is used to modify the attributes of a specified snapshot.

        This API supports modifying snapshot name and expiration time, as well as changing a non-permanent snapshot to a permanent one.
        The "snapshot name" is only for making user management convenient. Tencent Cloud does not use this name as a basis for submitting tickets or managing snapshot operations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshotAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshotsSharePermission(
            self,
            request: models.ModifySnapshotsSharePermissionRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotsSharePermissionResponse:
        """
        This API is used to modify snapshot sharing information.

        After snapshots are shared, the accounts they are shared to can use the snapshot to create cloud disks.
        * Each snapshot can be shared to at most 50 accounts.
        * You can use a shared snapshot to create cloud disks, but you cannot change its name or description.
        * Snapshots can only be shared with accounts in the same region.
        * Only data disk snapshots can be shared.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshotsSharePermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotsSharePermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDisk(
            self,
            request: models.RenewDiskRequest,
            opts: Dict = None,
    ) -> models.RenewDiskResponse:
        """
        This API is used to renew cloud disks.

        This API is used to support renewal along with mounted instances. The parameter specifies CurInstanceDeadline in [DiskChargePrepaid](https://www.tencentcloud.com/document/product/362/15669?from_cn_redirect=1#DiskChargePrepaid), and renewal will be at the expiry date after the instance is renewed.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeDisk(
            self,
            request: models.ResizeDiskRequest,
            opts: Dict = None,
    ) -> models.ResizeDiskResponse:
        """
        This API is used to expand cloud disks.

        *This API supports only the expansion of elastic cloud disks. To query the type of a cloud disk, you can call the [DescribeDisks](https://intl.cloud.tencent.comhttps://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1?from_cn_redirect=1) API and check the `Portable` field in the response. To expand non-elastic cloud disks, you can call the [ResizeInstanceDisks](https://intl.cloud.tencent.com/document/product/213/15731?from_cn_redirect=1) API. *This is an async API. A successful return of this API does not mean that the cloud disk has been expanded successfully. You can call the [DescribeDisks](https://intl.cloud.tencent.comhttps://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1?from_cn_redirect=1) API to query the status of a cloud disk. `EXPANDING` indicates that the expansion is in process.
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDisks(
            self,
            request: models.TerminateDisksRequest,
            opts: Dict = None,
    ) -> models.TerminateDisksResponse:
        """
        This API is used to return cloud disks.

        * You can use this API to return cloud disks you no longer need.
        * This API can be used to return pay-as-you-go cloud disks billed on hourly basis.
        * Batch operations are supported. The maximum number of cloud disks in each request is 50. If there is any specified cloud disk that cannot be returned, an error code will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindAutoSnapshotPolicy(
            self,
            request: models.UnbindAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.UnbindAutoSnapshotPolicyResponse:
        """
        This API (UnbindAutoSnapshotPolicy) is used to unbind the cloud disk from the specified scheduled snapshot policy.

        * Batch operations are supported. Multiple cloud disks can be unbound from a snapshot policy at one time.
        * If the passed-in cloud disks are not bound to the current scheduled snapshot policy, they will be skipped. Only cloud disks that are bound to the current scheduled snapshot policy are processed.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)