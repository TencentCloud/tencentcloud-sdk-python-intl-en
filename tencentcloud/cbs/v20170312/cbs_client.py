# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
            body = self.call("ApplySnapshot", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplySnapshotResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachDisks(self, request):
        """This API (AttachDisks) is used to mount cloud disks.

        * Batch operations are supported. Multiple cloud disks can be mounted to a CVM. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned.
        * This API is an asynchronous API. If the request for mounting the cloud disk successfully returns results, the operation of mounting cloud disk has been initiated at the background. You can use the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) to query the cloud disk status. If the status changes from "ATTACHING" to "ATTACHED", the cloud disk is mounted.

        :param request: Request instance for AttachDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.AttachDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.AttachDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("BindAutoSnapshotPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindAutoSnapshotPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("CreateAutoSnapshotPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAutoSnapshotPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDisks(self, request):
        """This API is used to create one or more cloud disks.

        * This API supports creating a cloud disk with a data disk snapshot so that the snapshot data can be copied to the purchased cloud disk.
        * This API is an async API. A cloud disk ID list will be returned when a request is made successfully, but it does not mean that the creation has been completed. You can call the [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) API to query cloud disks by `DiskId`. If a new cloud disk can be found and its state is 'UNATTACHED' or 'ATTACHED', it means that the cloud disk has been created successfully.

        :param request: Request instance for CreateDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.CreateDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.CreateDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSnapshot(self, request):
        """This API (CreateSnapshot) is used to create a snapshot of a specified cloud disk.

        * Snapshots can only be created for cloud disks with the snapshot capability. To check whether a cloud disk has the snapshot capability, see the SnapshotAbility field returned by the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1).
        * For the number of snapshots that can be created, please see [Product Usage Restriction](https://intl.cloud.tencent.com/doc/product/362/5145?from_cn_redirect=1).

        :param request: Request instance for CreateSnapshot.
        :type request: :class:`tencentcloud.cbs.v20170312.models.CreateSnapshotRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.CreateSnapshotResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSnapshot", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSnapshotResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAutoSnapshotPolicies(self, request):
        """This API (DeleteAutoSnapshotPolicies) is used to delete scheduled snapshot policies.

        * Batch operations are supported. If one of the scheduled snapshot policies in a batch cannot be deleted, the operation is not performed and a specific error code is returned.

        :param request: Request instance for DeleteAutoSnapshotPolicies.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DeleteAutoSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DeleteAutoSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAutoSnapshotPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAutoSnapshotPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSnapshots(self, request):
        """This API (DeleteSnapshots) is used to delete snapshots.

        * The snapshot must be in NORMAL status. The snapshot status can be queried in the SnapshotState field in the output parameters through the API [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1).
        * Batch operations are supported. If one of the snapshots in a batch cannot be deleted, the operation is not performed and a specific error code is returned.

        :param request: Request instance for DeleteSnapshots.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DeleteSnapshotsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DeleteSnapshotsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSnapshots", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSnapshotsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAutoSnapshotPolicies(self, request):
        """This API (DescribeAutoSnapshotPolicies) is used to query scheduled snapshot policies.

        * You can query the detailed information of scheduled snapshot policies by ID, name, or status. Insert `AND` between different values. For details on filtering information, see `Filter`.
        * If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of the scheduled snapshot policy lists are returned to the current user.

        :param request: Request instance for DescribeAutoSnapshotPolicies.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeAutoSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeAutoSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoSnapshotPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoSnapshotPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDiskAssociatedAutoSnapshotPolicy(self, request):
        """This API (DescribeDiskAssociatedAutoSnapshotPolicy) is used to query the scheduled snapshot policy bound to a cloud disk.

        :param request: Request instance for DescribeDiskAssociatedAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskAssociatedAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskAssociatedAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDiskAssociatedAutoSnapshotPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDiskAssociatedAutoSnapshotPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDiskConfigQuota(self, request):
        """This API (DescribeDiskConfigQuota) is used to query the cloud disk quota.

        :param request: Request instance for DescribeDiskConfigQuota.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskConfigQuotaRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskConfigQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDiskConfigQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDiskConfigQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDiskOperationLogs(self, request):
        """This API (DescribeDiskOperationLogs) is used to query a list of cloud disk operation logs.

        This can be filtered according to the cloud disk ID. The format of cloud disk IDs is as follows: disk-a1kmcp13.

        :param request: Request instance for DescribeDiskOperationLogs.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskOperationLogsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeDiskOperationLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDiskOperationLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDiskOperationLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DescribeDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstancesDiskNum(self, request):
        """This API (DescribeInstancesDiskNum) is used to query the number of cloud disks mounted in the instance.

        * Batch operations are supported. If multiple CVM instance IDs are specified, the returned results will list the number of cloud disks mounted on each CVM.

        :param request: Request instance for DescribeInstancesDiskNum.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeInstancesDiskNumRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeInstancesDiskNumResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesDiskNum", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesDiskNumResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSnapshotOperationLogs(self, request):
        """This API (DescribeSnapshotOperationLogs) is used to query a list of snapshot operation logs.

        You can filter according to the snapshot ID. The snapshot ID format is as follows: snap-a1kmcp13.

        :param request: Request instance for DescribeSnapshotOperationLogs.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotOperationLogsRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotOperationLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSnapshotOperationLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSnapshotOperationLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSnapshotSharePermission(self, request):
        """This API is used to query the sharing information of snapshots.

        :param request: Request instance for DescribeSnapshotSharePermission.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotSharePermissionRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DescribeSnapshotSharePermissionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSnapshotSharePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSnapshotSharePermissionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DescribeSnapshots", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSnapshotsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachDisks(self, request):
        """This API (DetachDisks) is used to unmount cloud disks.

        * Batch operations are supported. Multiple cloud disks mounted to the same CVM can be unmounted in batch. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned.
        * This API is an asynchronous API. When the request successfully returns results, the cloud disk is not unmounted from the CVM immediately. You can use the API [DescribeDisks](https://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1) to query the cloud disk status. If the status changes from "ATTACHED" to "UNATTACHED", the cloud disk is unmounted.

        :param request: Request instance for DetachDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.DetachDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.DetachDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetSnapOverview(self, request):
        """This API is used to get snapshot overview information.

        :param request: Request instance for GetSnapOverview.
        :type request: :class:`tencentcloud.cbs.v20170312.models.GetSnapOverviewRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.GetSnapOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSnapOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSnapOverviewResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceCreateDisks(self, request):
        """This API (InquiryPriceCreateDisks) is used to inquire the price for cloud disk creation.

        * It supports inquiring the price for the creation of multiple cloud disks. The total price for the creation is returned.

        :param request: Request instance for InquiryPriceCreateDisks.
        :type request: :class:`tencentcloud.cbs.v20170312.models.InquiryPriceCreateDisksRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.InquiryPriceCreateDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceResizeDisk(self, request):
        """This API is used to query the price for expanding cloud disks.

        :param request: Request instance for InquiryPriceResizeDisk.
        :type request: :class:`tencentcloud.cbs.v20170312.models.InquiryPriceResizeDiskRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.InquiryPriceResizeDiskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResizeDisk", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResizeDiskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("ModifyAutoSnapshotPolicyAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoSnapshotPolicyAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("ModifyDiskAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDiskAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("ModifySnapshotAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySnapshotAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("ModifySnapshotsSharePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySnapshotsSharePermissionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResizeDisk(self, request):
        """This API is used to expand the capacity of a cloud disk.

        * This API supports only the expansion of elastic cloud disks. To query the type of a cloud disk, you can call the [DescribeDisks](https://intl.cloud.tencent.comhttps://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1?from_cn_redirect=1) API and check the `Portable` field in the response. To expand non-elastic cloud disks, you can call the [ResizeInstanceDisks](https://intl.cloud.tencent.com/document/product/213/15731?from_cn_redirect=1) API.
        * This is an async API. A successful return of this API does not mean that the cloud disk has been expanded successfully. You can call the [DescribeDisks](https://intl.cloud.tencent.comhttps://intl.cloud.tencent.com/document/product/362/16315?from_cn_redirect=1?from_cn_redirect=1) API to query the status of a cloud disk. `EXPANDING` indicates that the expansion is in process.

        :param request: Request instance for ResizeDisk.
        :type request: :class:`tencentcloud.cbs.v20170312.models.ResizeDiskRequest`
        :rtype: :class:`tencentcloud.cbs.v20170312.models.ResizeDiskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResizeDisk", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResizeDiskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("TerminateDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("UnbindAutoSnapshotPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindAutoSnapshotPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)