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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cbs.v20170312 import models


class CbsClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'cbs.tencentcloudapi.com'
    _service = 'cbs'


    def ApplyDiskBackup(self, request):
        """This API is used to roll back a backup point to the original cloud disk.

        * Only rollback to the original cloud disk is supported. For a data disk backup point, if you want to copy the backup point data to another cloud disk, use the `CreateSnapshot` API to convert the backup point into a snapshot, use the `CreateDisks` API to create an elastic cloud disk, and then copy the snapshot data to it.
        * Only backup points in `NORMAL` status can be rolled back. To query the status of a backup point, call the `DescribeDiskBackups` API and see the `BackupState` field in the response.
        * For an elastic cloud disk, it must be in unattached status. To query the status of the cloud disk, call the `DescribeDisks` API and see the `Attached` field in the response. For a non-elastic cloud disk purchased together with an instance, the instance must be in shutdown status, which can be queried through the `DescribeInstancesStatus` API.

        :param request: Request instance for ApplyDiskBackup.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ApplyDiskBackupRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ApplyDiskBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyDiskBackup", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyDiskBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApplySnapshot(self, request):
        """This API (ApplySnapshot) is used to roll back a snapshot to the original cloud disk.

        * The snapshot can only be rolled back to the original cloud disk. For data disk snapshots, if you need to copy the snapshot data to other cloud disks, use the API [CreateDisks](https://intl.cloud.tencent.com/document/product/362/16312?from_cn_redirect=1) to create an elastic cloud disk and then copy the snapshot data to the created cloud disk.
        * The snapshot for rollback must be in NORMAL status. The snapshot status can be queried in the SnapshotState field in the output parameters through the API [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        * For elastic cloud disks, the cloud disk must be in UNMOUNTED status. The cloud disk status can be queried in the Attached field returned by the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1). For non-elastic cloud disks purchased together with instances, the instance must be in SHUTDOWN status. The instance status can be queried through the API [DescribeInstancesStatus](https://intl.cloud.tencent.com/document/product/213/15738?from_cn_redirect=1).

        :param request: Request instance for ApplySnapshot.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ApplySnapshotRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ApplySnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplySnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.ApplySnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachDisks(self, request):
        """This API is used to mount one or more cloud disks.

        * Batch operation is supported. You can mount multiple cloud disks to one CVM in a single request. If any of these cloud disks cannot be mounted, the operation fails and a specific error code returns.
        * This is an async API. A successful request indicates that the mounting is initiated. You can call the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API to query the status of cloud disks. If the status changes from `ATTACHING` to `ATTACHED`, the mounting is successful.

        :param request: Request instance for AttachDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.AttachDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.AttachDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachDisks", params, headers=headers)
            response = json.loads(body)
            model = models.AttachDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindAutoSnapshotPolicy(self, request):
        """This API (BindAutoSnapshotPolicy) is used to bind the cloud disk to the specified scheduled snapshot policy.

        * For the scheduled snapshot policy limit of each region, see [Scheduled Snapshots](https://intl.cloud.tencent.com/document/product/362/8191?from_cn_redirect=1).
        * When a cloud disk that is bound to a scheduled snapshot policy is in the unused state (that is, an elastic cloud disk has not been mounted or the server of an inelastic disk is powered off) scheduled snapshots are not created.

        :param request: Request instance for BindAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cbs.v20170312.models.BindAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.BindAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.BindAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopySnapshotCrossRegions(self, request):
        """This API is used to replicate a snapshot to another region.

        * This is an async API. A new snapshot ID is issued when the cross-region replication task is generated. It does not mean that the snapshot has been replicated successfully. You can all the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API in the destination region to check for this snapshot. If the snapshot status is `NORMAL`, the snapshot is replicated successfully.
        * The snapshot cross-region replication service will be commercialized in the Q3 of 2022. We will notify users about the commercialization in advance. Please check your messages in the Message Center.

        :param request: Request instance for CopySnapshotCrossRegions.
        :type request: :class:`tencentcloud.cbs.v20170312.models.CopySnapshotCrossRegionsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.CopySnapshotCrossRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopySnapshotCrossRegions", params, headers=headers)
            response = json.loads(body)
            model = models.CopySnapshotCrossRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoSnapshotPolicy(self, request):
        """This API (CreateAutoSnapshotPolicy) is used to create a scheduled snapshot policy.

        * For the limits on the number of scheduled snapshot policies that can be created in each region, see [Scheduled Snapshots](https://intl.cloud.tencent.com/document/product/362/8191?from_cn_redirect=1).
        * The quantity and capacity of the snapshots that can be created in each region are limited. For more information, see the **Snapshots** page on the Tencent Cloud Console. If the number of snapshots exceeds the quota, the creation of the scheduled snapshots will fail.

        :param request: Request instance for CreateAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cbs.v20170312.models.CreateAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.CreateAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDiskBackup(self, request):
        """This API is used to create a backup point for a cloud disk.

        :param request: Request instance for CreateDiskBackup.
        :type request: :class:`tencentcloud.cbs.v20170312.models.CreateDiskBackupRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.CreateDiskBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDiskBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDiskBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDisks(self, request):
        """This API is used to create cloud disks.

        * This API supports creating a cloud disk with a data disk snapshot so that the snapshot data can be copied to the purchased cloud disk.
        * This API is async. A cloud disk ID list will be returned when a request is made successfully, but it does not mean that the creation has been completed. You can call the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API to query cloud disks by `DiskId`. If a new cloud disk can be found and its status is `UNATTACHED` or `ATTACHED`, the cloud disk has been created successfully.

        :param request: Request instance for CreateDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.CreateDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.CreateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSnapshot(self, request):
        """This API is used to create a snapshot for the specified cloud disk.

        * You can only create snapshots for cloud disks with the snapshot capability. To check whether a cloud disk is snapshot-enabled, call the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API and see the `SnapshotAbility` field in the response.
        * For the maximum number of snapshots that can be created, see [Use Limits](https://intl.cloud.tencent.com/doc/product/362/5145?from_cn_redirect=1).
        * Currently, you can convert backup points into general snapshots. After the conversion, snapshot usage fees may be charged, backup points will not be retained, and the occupied backup point quota will be released.

        :param request: Request instance for CreateSnapshot.
        :type request: :class:`tencentcloud.cbs.v20170312.models.CreateSnapshotRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.CreateSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAutoSnapshotPolicies(self, request):
        """This API (DeleteAutoSnapshotPolicies) is used to delete scheduled snapshot policies.

        * Batch operations are supported. If one of the scheduled snapshot policies in a batch cannot be deleted, the operation is not performed and a specific error code is returned.

        :param request: Request instance for DeleteAutoSnapshotPolicies.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DeleteAutoSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DeleteAutoSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAutoSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDiskBackups(self, request):
        """This API is used to delete the backup points of the specified cloud disk in batches.

        :param request: Request instance for DeleteDiskBackups.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DeleteDiskBackupsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DeleteDiskBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDiskBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDiskBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshots(self, request):
        """This API is used to delete snapshots.

        * Only snapshots in the `NORMAL` state can be deleted. To query the state of a snapshot, you can call the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API and check the `SnapshotState` field in the response.
        * Batch operations are supported. If there is any snapshot that cannot be deleted, the operation will not be performed and a specific error code will be returned.

        :param request: Request instance for DeleteSnapshots.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DeleteSnapshotsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DeleteSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoSnapshotPolicies(self, request):
        """This API is used to query scheduled snapshot policies.

        * You can filter scheduled snapshot policies by ID, name, state, etc. The relationship between different filters is logical `AND`. For details on filters, see `Filter`.
        * If no parameter is specified, a certain number of scheduled snapshot policies under the current account will be returned. The number is specified by `Limit` and is 20 by default.

        :param request: Request instance for DescribeAutoSnapshotPolicies.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeAutoSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeAutoSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiskAssociatedAutoSnapshotPolicy(self, request):
        """This API (DescribeDiskAssociatedAutoSnapshotPolicy) is used to query the scheduled snapshot policy bound to a cloud disk.

        :param request: Request instance for DescribeDiskAssociatedAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskAssociatedAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskAssociatedAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskAssociatedAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskAssociatedAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiskBackups(self, request):
        """This API is used to query the details of backup points.

        You can filter results by backup point ID. You can also look for certain backup points by specifying the ID or type of the cloud disk for which the backup points are created. The relationship between different filters is logical `AND`. For more information on filters, see `Filter`.
        If the parameter is empty, a certain number (as specified by `Limit` and 20 by default) of backup points will be returned.

        :param request: Request instance for DescribeDiskBackups.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskBackupsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiskConfigQuota(self, request):
        """This API (DescribeDiskConfigQuota) is used to query the cloud disk quota.

        :param request: Request instance for DescribeDiskConfigQuota.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskConfigQuotaRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskConfigQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskConfigQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskConfigQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiskOperationLogs(self, request):
        """接口已废弃，切换至云审计接口。见https://tapd.woa.com/pro/prong/stories/view/1010114221880719007

        This API has been disused. Use the CloudAudit API instead, For more information, visit https://tapd.woa.com/pro/prong/stories/view/1010114221880719007.

        This API is used to query the operation logs of a cloud disk. It will be disused soon. Use [LookUpEvents](https://intl.cloud.tencent.com/document/product/629/12359?from_cn_redirect=1) instead.

        :param request: Request instance for DescribeDiskOperationLogs.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskOperationLogsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskOperationLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskOperationLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskOperationLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisks(self, request):
        """This API (DescribeDisks) is used to query the list of cloud disks.

        * The details of the cloud disk can be queried based on the ID, type or status of the cloud disk. The relationship between different conditions is AND. For more information about filtering, please see the `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of cloud disk lists are returned to the current user.

        :param request: Request instance for DescribeDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesDiskNum(self, request):
        """This API (DescribeInstancesDiskNum) is used to query the number of cloud disks mounted in the instance.

        * Batch operations are supported. If multiple CVM instance IDs are specified, the returned results will list the number of cloud disks mounted on each CVM.

        :param request: Request instance for DescribeInstancesDiskNum.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeInstancesDiskNumRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeInstancesDiskNumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesDiskNum", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesDiskNumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotOperationLogs(self, request):
        """接口已废弃，切换至云审计接口。见https://tapd.woa.com/pro/prong/stories/view/1010114221880719007

        This API has been disused. Use the CloudAudit API instead, For more information, visit https://tapd.woa.com/pro/prong/stories/view/1010114221880719007.

        This API is used to query the operation logs of a snapshot. It will be disused soon. Use [LookUpEvents](https://intl.cloud.tencent.com/document/product/629/12359?from_cn_redirect=1) instead.

        :param request: Request instance for DescribeSnapshotOperationLogs.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotOperationLogsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotOperationLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotOperationLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotOperationLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotSharePermission(self, request):
        """This API is used to query the sharing information of snapshots.

        :param request: Request instance for DescribeSnapshotSharePermission.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotSharePermissionRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotSharePermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotSharePermission", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotSharePermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshots(self, request):
        """This API (DescribeSnapshots) is used to query the details of snapshots.

        * Filter the results by the snapshot ID, the ID of cloud disk, for which the snapshot is created, and the type of cloud disk, for which the snapshot is created. The relationship between different conditions is AND. For more information about filtering, please see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of snapshot lists are returned to the current user.

        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachDisks(self, request):
        """This API is used to unmount one or more cloud disks.

        * Batch operation is supported. You can unmount multiple cloud disks from the same CVM in a single request. If any of these cloud disks cannot be unmounted, the operation fails and a specific error code returns.
        * This is an async API. A successful request does not mean that the cloud disks have been unmounted successfully. You can call the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API to query the status of cloud disks. When the status changes from `ATTACHED` to `UNATTACHED`, the unmounting is successful.

        :param request: Request instance for DetachDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DetachDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DetachDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DetachDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSnapOverview(self, request):
        """This API is used to get snapshot overview information.

        :param request: Request instance for GetSnapOverview.
        :type request: :class:`tencentcloud.cbs.v20170312.models.GetSnapOverviewRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.GetSnapOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSnapOverview", params, headers=headers)
            response = json.loads(body)
            model = models.GetSnapOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InitializeDisks(self, request):
        """This API is used to reinitialize the cloud disks. Note the following when reinitializing the cloud disks:
        1. For a cloud disk created from a snapshot, it is rolled back to the state of the snapshot;
        2. For a cloud disk created from the scratch, all data are cleared. Please check and back up the necessary data before the reinitialization;
        3. Currently, you can only re-initialize a cloud disk when it’s not attached to a resource and not shared by others;
        4. For a cloud disk created from a snapshot, if the snapshot has been deleted, it cannot be reinitialized.

        :param request: Request instance for InitializeDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.InitializeDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.InitializeDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitializeDisks", params, headers=headers)
            response = json.loads(body)
            model = models.InitializeDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceModifyDiskBackupQuota(self, request):
        """This API is used to query the price of a cloud disk after its backup point quota is modified.

        :param request: Request instance for InquirePriceModifyDiskBackupQuota.
        :type request: :class:`tencentcloud.cbs.v20170312.models.InquirePriceModifyDiskBackupQuotaRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.InquirePriceModifyDiskBackupQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceModifyDiskBackupQuota", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceModifyDiskBackupQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceModifyDiskExtraPerformance(self, request):
        """This API is used to query the price for adjusting the cloud disk’s extra performance.

        :param request: Request instance for InquirePriceModifyDiskExtraPerformance.
        :type request: :class:`tencentcloud.cbs.v20170312.models.InquirePriceModifyDiskExtraPerformanceRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.InquirePriceModifyDiskExtraPerformanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceModifyDiskExtraPerformance", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceModifyDiskExtraPerformanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateDisks(self, request):
        """This API is used to query the price of creating cloud disks.

        * You can query the price of creating multiple cloud disks in a single request. In this case, the price returned will be the total price.

        :param request: Request instance for InquiryPriceCreateDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.InquiryPriceCreateDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.InquiryPriceCreateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceResizeDisk(self, request):
        """This API is used to query the price for expanding cloud disks.

        :param request: Request instance for InquiryPriceResizeDisk.
        :type request: :class:`tencentcloud.cbs.v20170312.models.InquiryPriceResizeDiskRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.InquiryPriceResizeDiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceResizeDisk", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceResizeDiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoSnapshotPolicyAttribute(self, request):
        """This API (ModifyAutoSnapshotPolicyAttribute) is used to modify the attributes of an automatic snapshot policy.

        * You can use this API to modify the attributes of a scheduled snapshot policy, including the execution policy, name, and activation.
        * When modifying the number of days for retention, you must ensure that there is no clash with the permanent retention attribute. Otherwise, the entire operation will fail and a specific error code will be returned.

        :param request: Request instance for ModifyAutoSnapshotPolicyAttribute.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ModifyAutoSnapshotPolicyAttributeRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ModifyAutoSnapshotPolicyAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoSnapshotPolicyAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoSnapshotPolicyAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDiskAttributes(self, request):
        """* Only the project ID of elastic cloud disk can be modified. The project ID of the cloud disk created with the CVM is linked with the CVM. The project ID can be can be queried in the Portable field in the output parameters through the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1).
        * "Cloud disk name" is only used by users for their management. Tencent Cloud does not use the name as the basis for ticket submission or cloud disk management.
        * Batch operations are supported. If multiple cloud disk IDs are specified, all the specified cloud disks must have the same attribute. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned.

        :param request: Request instance for ModifyDiskAttributes.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ModifyDiskAttributesRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ModifyDiskAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDiskAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDiskAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDiskBackupQuota(self, request):
        """This API is used to modify the cloud disk backup point quota.

        :param request: Request instance for ModifyDiskBackupQuota.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ModifyDiskBackupQuotaRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ModifyDiskBackupQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDiskBackupQuota", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDiskBackupQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDiskExtraPerformance(self, request):
        """This API is used to adjust extra performance for Enhanced SSD (CLOUD_HSSD) and ulTra SSD.

        *This API only supports adjust extra performance for Enhanced SSD and ulTra SSD.

        :param request: Request instance for ModifyDiskExtraPerformance.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ModifyDiskExtraPerformanceRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ModifyDiskExtraPerformanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDiskExtraPerformance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDiskExtraPerformanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshotAttribute(self, request):
        """This API (ModifySnapshotAttribute) is used to modify the attributes of a specified snapshot.

        * Currently, you can only modify snapshot name and change non-permanent snapshots into permanent snapshots.
        * "Snapshot name" is only used by users for their management. Tencent Cloud does not use the name as the basis for ticket submission or snapshot management.

        :param request: Request instance for ModifySnapshotAttribute.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ModifySnapshotAttributeRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ModifySnapshotAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshotAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshotsSharePermission(self, request):
        """This API is used to modify snapshot sharing information.

        After snapshots are shared, the accounts they are shared to can use the snapshot to create cloud disks.
        * Each snapshot can be shared to at most 50 accounts.
        * You can use a shared snapshot to create cloud disks, but you cannot change its name or description.
        * Snapshots can only be shared with accounts in the same region.
        * Only data disk snapshots can be shared.

        :param request: Request instance for ModifySnapshotsSharePermission.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ModifySnapshotsSharePermissionRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ModifySnapshotsSharePermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshotsSharePermission", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotsSharePermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeDisk(self, request):
        """This API is used to expand cloud disks.

        *This API supports only the expansion of elastic cloud disks. To query the type of a cloud disk, you can call the [DescribeDisks](https://intl.cloud.tencent.comhttps://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1?from_cn_redirect=1) API and check the `Portable` field in the response. To expand non-elastic cloud disks, you can call the [ResizeInstanceDisks](https://intl.cloud.tencent.com/document/product/213/15731?from_cn_redirect=1) API. *This is an async API. A successful return of this API does not mean that the cloud disk has been expanded successfully. You can call the [DescribeDisks](https://intl.cloud.tencent.comhttps://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1?from_cn_redirect=1) API to query the status of a cloud disk. `EXPANDING` indicates that the expansion is in process.

        :param request: Request instance for ResizeDisk.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ResizeDiskRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ResizeDiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeDisk", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeDiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateDisks(self, request):
        """This API is used to return cloud disks.

        * You can use this API to return cloud disks you no longer need.
        * This API can be used to return pay-as-you-go cloud disks billed on hourly basis.
        * Batch operations are supported. The maximum number of cloud disks in each request is 50. If there is any specified cloud disk that cannot be returned, an error code will be returned.

        :param request: Request instance for TerminateDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.TerminateDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.TerminateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindAutoSnapshotPolicy(self, request):
        """This API (UnbindAutoSnapshotPolicy) is used to unbind the cloud disk from the specified scheduled snapshot policy.

        * Batch operations are supported. Multiple cloud disks can be unbound from a snapshot policy at one time.
        * If the passed-in cloud disks are not bound to the current scheduled snapshot policy, they will be skipped. Only cloud disks that are bound to the current scheduled snapshot policy are processed.

        :param request: Request instance for UnbindAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cbs.v20170312.models.UnbindAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.UnbindAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))