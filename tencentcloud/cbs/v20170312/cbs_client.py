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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cbs.v20170312 import models


class CbsClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'cbs.intl.tencentcloudapi.com'
    _service = 'cbs'


    def ApplyDiskBackup(self, request):
        r"""This API is used to roll back a backup to the original cloud disk.

        This API only supports rolling back to the original cloud disk. For data disk backup points, if you need to copy backup point data to other CBS, use first [CreateSnapshot](https://www.tencentcloud.com/document/product/362/15648?from_cn_redirect=1) to convert the backup point to a snapshot, and use [CreateDisks](https://www.tencentcloud.com/document/product/362/16312?from_cn_redirect=1) to create a new elastic cloud disk, then copy snapshot data to the newly purchased cloud disk.
        The backup point used for rollback must be in NORMAL status. The backup point status can be checked through the [DescribeDiskBackups](https://www.tencentcloud.com/document/product/362/80278?from_cn_redirect=1) API, see BackupState field explanation in the output parameter.
        If it is an elastic cloud disk, the CBS must be in an unmounted state. The CBS mount status can be queried through the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API. See Attached field explanation. If it is a non-elastic cloud hard disk purchased together with the instance, the instance must be in a powered off state. The instance status can be queried through the [DescribeInstancesStatus](https://www.tencentcloud.com/document/product/213/15738?from_cn_redirect=1) API.

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
        r"""This API (ApplySnapshot) is used to roll back a snapshot to the original cloud disk.

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


    def ApplySnapshotGroup(self, request):
        r"""This API is used to rollback a snapshot group and restore the instance to the state at the moment the snapshot group was created.
        This API is used to roll back all or part of the disks in the snapshot group.
        This API is used to roll back disks. If the disks to be rolled back contain mounted disks, they must be mounted to the same instance, and the instance must be shut down before rollback.
        Rollback is an asynchronous operation. A successful API return does not indicate a successful rollback. You can call DescribeSnapshotGroups to check the snapshot group status.

        :param request: Request instance for ApplySnapshotGroup.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ApplySnapshotGroupRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ApplySnapshotGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplySnapshotGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ApplySnapshotGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachDisks(self, request):
        r"""This API is used to mount one or more cloud disks.

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
        r"""This API (BindAutoSnapshotPolicy) is used to bind the cloud disk to the specified scheduled snapshot policy.

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
        r"""This API is used to replicate snapshots across regions.

        This API is asynchronous. When the cross-region replication request is issued successfully, it returns a new snapshot ID. At this point, the snapshot is not immediately replicated to the target region. You can use the [DescribeSnapshots](https://www.tencentcloud.com/document/product/362/15647?from_cn_redirect=1) API for the query in the target region to check the snapshot status and determine whether the replication is complete. If the snapshot status is "NORMAL", it indicates snapshot replication is complete.
        This API is used to perform snapshot cross-region replication, which will generate cross-region traffic. Commercial billing for this feature is expected in Q3 2025. Please check subsequent Message Center notices to avoid unexpected charges.

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
        r"""This API (CreateAutoSnapshotPolicy) is used to create a scheduled snapshot policy.

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
        r"""This API is used to create a backup point for a cloud disk.

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
        r"""This API is used to create cloud disks.

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
        r"""This API is used to create a snapshot for the specified cloud disk.

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


    def CreateSnapshotGroup(self, request):
        r"""This API is used to create a snapshot group.
        This API is used to create snapshot groups. The CBS list must be mounted on the same instance.
        This API is used to create snapshot groups for all or some of the disks mounted to instance.

        :param request: Request instance for CreateSnapshotGroup.
        :type request: :class:`tencentcloud.cbs.v20170312.models.CreateSnapshotGroupRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.CreateSnapshotGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshotGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAutoSnapshotPolicies(self, request):
        r"""This API (DeleteAutoSnapshotPolicies) is used to delete scheduled snapshot policies.

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
        r"""This API is used to delete the backup points of the specified cloud disk in batches.

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


    def DeleteSnapshotGroup(self, request):
        r"""This API is used to delete snapshot groups. One snapshot group can be deleted per call.
        This API is used to delete all snapshots in the snapshot group by default.
        This API is used to delete a snapshot group. If a snapshot in the snapshot group has an associated image, deletion will fail and no snapshot will be deleted. Parameters can be input to enable simultaneous deletion of images bound to the snapshot by setting DeleteBindImages equal to true.

        :param request: Request instance for DeleteSnapshotGroup.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DeleteSnapshotGroupRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DeleteSnapshotGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshotGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshots(self, request):
        r"""This API is used to delete snapshots.

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
        r"""This API is used to query scheduled snapshot policies.

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
        r"""This API (DescribeDiskAssociatedAutoSnapshotPolicy) is used to query the scheduled snapshot policy bound to a cloud disk.

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
        r"""This API is used to query the details of backup points.

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
        r"""This API (DescribeDiskConfigQuota) is used to query the cloud disk quota.

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


    def DescribeDiskStoragePool(self, request):
        r"""This API is used to query the list of dedicated cloud disk clusters under the current user account.

        * You can query by the dedicated cloud disk cluster ID (`CdcId`) and availability zone (`zone`). Multiple filters are combined with AND. For details about filtering, please see `Filter`.
        * If the parameter is empty, a number (as specified by `Limit`; the default is 20) of dedicated cloud disk clusters are returned.

        :param request: Request instance for DescribeDiskStoragePool.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskStoragePoolRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskStoragePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskStoragePool", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskStoragePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisks(self, request):
        r"""This API (DescribeDisks) is used to query the list of cloud disks.

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
        r"""This API (DescribeInstancesDiskNum) is used to query the number of cloud disks mounted in the instance.

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


    def DescribeSnapshotGroups(self, request):
        r"""This API is used to query the snapshot group list.
        This API is used to query the snapshot group list based on snapshot group ID, snapshot group status or snapshot ID associated with the snapshot group. The relationship among different criteria is AND. For detailed filtering information, see `Filter`.
        If the parameter is empty, a certain number of the cloud disk list for the current user is returned (specified by `Limit`, defaults to 20).

        :param request: Request instance for DescribeSnapshotGroups.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotGroupsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotOverview(self, request):
        r"""This API is used to query the usage overview of user snapshots, including total snapshot capacity, cost capacity, etc.

        :param request: Request instance for DescribeSnapshotOverview.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotOverviewRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotSharePermission(self, request):
        r"""This API is used to query the sharing information of snapshots.

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
        r"""This API (DescribeSnapshots) is used to query the details of snapshots.

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
        r"""This API is used to unmount one or more cloud disks.

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
        r"""This API is used to standardize API naming. This API will be decommissioned and replaced by the new API named DescribeSnapshotOverview.

        This API is used to obtain snapshot overview information.

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
        r"""This API is used to reinitialize the cloud disks. Note the following when reinitializing the cloud disks:
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
        r"""This API is used to query the price of a cloud disk after its backup point quota is modified.

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
        r"""This API is used to query the price for adjusting the cloud disk’s extra performance.

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
        r"""This API is used to query the price of creating cloud disks.

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


    def InquiryPriceRenewDisks(self, request):
        r"""This API is used to query the renewal price of CBS.

        This API is used to support renewal along with mounted instances. The parameter specifies CurInstanceDeadline in [DiskChargePrepaid](https://www.tencentcloud.com/document/product/362/15669?from_cn_redirect=1#DiskChargePrepaid), and renewal will be performed at the expiry date after the instance is renewed.
        This API is used to support specifying different renewal durations for multiple cloud disks. The total price for renewing multiple cloud disks is returned.

        :param request: Request instance for InquiryPriceRenewDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.InquiryPriceRenewDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.InquiryPriceRenewDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewDisks", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceResizeDisk(self, request):
        r"""This API is used to query the price for expanding cloud disks.

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
        r"""This API (ModifyAutoSnapshotPolicyAttribute) is used to modify the attributes of an automatic snapshot policy.

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
        r"""This API is used to modify only the Project ID of elastic cloud disks. The Project ID of a cloud disk created with a host is linked to the host. Whether a cloud disk is elastic can be checked through the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315?from_cn_redirect=1) API. See the Portable field explanation in the output parameters.
        The "cloud disk name" is only for ease of management for users. Tencent Cloud does not use this name as a basis for submitting tickets or performing cloud disk management operations.
        This API is used to support batch operations. If multiple cloud disk IDs are passed in, modify cloud disks to the same attribute. If there is a cloud disk that does not allow operation, the operation will not be executed and return a specific error code.

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
        r"""This API is used to modify the cloud disk backup point quota.

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
        r"""This API is used to adjust extra performance for Enhanced SSD (CLOUD_HSSD) and ulTra SSD.

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
        r"""This API is used to modify the attributes of a specified snapshot.

        This API supports modifying snapshot name and expiration time, as well as changing a non-permanent snapshot to a permanent one.
        The "snapshot name" is only for making user management convenient. Tencent Cloud does not use this name as a basis for submitting tickets or managing snapshot operations.

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
        r"""This API is used to modify snapshot sharing information.

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


    def RenewDisk(self, request):
        r"""This API is used to renew cloud disks.

        This API is used to support renewal along with mounted instances. The parameter specifies CurInstanceDeadline in [DiskChargePrepaid](https://www.tencentcloud.com/document/product/362/15669?from_cn_redirect=1#DiskChargePrepaid), and renewal will be at the expiry date after the instance is renewed.

        :param request: Request instance for RenewDisk.
        :type request: :class:`tencentcloud.cbs.v20170312.models.RenewDiskRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.RenewDiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDisk", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeDisk(self, request):
        r"""This API is used to expand cloud disks.

        *This API supports only the expansion of elastic cloud disks. To query the type of a cloud disk, you can call the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315) API and check the `Portable` field in the response. To expand non-elastic cloud disks, you can call the [ResizeInstanceDisks](https://intl.cloud.tencent.com/document/product/213/15731?from_cn_redirect=1) API. *This is an async API. A successful return of this API does not mean that the cloud disk has been expanded successfully. You can call the [DescribeDisks](https://www.tencentcloud.com/document/product/362/16315) API to query the status of a cloud disk. `EXPANDING` indicates that the expansion is in process.

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
        r"""This API is used to return cloud disks.

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
        r"""This API (UnbindAutoSnapshotPolicy) is used to unbind the cloud disk from the specified scheduled snapshot policy.

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