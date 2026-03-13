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
from tencentcloud.cfs.v20190719 import models


class CfsClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'cfs.intl.tencentcloudapi.com'
    _service = 'cfs'


    def ApplyPathLifecyclePolicy(self, request):
        r"""Configure the directory list associated with the lifecycle policy.

        :param request: Request instance for ApplyPathLifecyclePolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.ApplyPathLifecyclePolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.ApplyPathLifecyclePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyPathLifecyclePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyPathLifecyclePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindAutoSnapshotPolicy(self, request):
        r"""This API is used to bind one or multiple file systems to a snapshot policy. A file system can be bound to only one policy.

        :param request: Request instance for BindAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.BindAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.BindAutoSnapshotPolicyResponse`

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


    def CreateAutoSnapshotPolicy(self, request):
        r"""This API is used to create a scheduled snapshot policy.

        :param request: Request instance for CreateAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateAutoSnapshotPolicyResponse`

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


    def CreateCfsFileSystem(self, request):
        r"""This API is used to create a file system.

        :param request: Request instance for CreateCfsFileSystem.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsFileSystemRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCfsFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCfsPGroup(self, request):
        r"""This API is used to create a permission group.

        :param request: Request instance for CreateCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCfsPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCfsRule(self, request):
        r"""This API is used to create a permission group rule.

        :param request: Request instance for CreateCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCfsRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCfsSnapshot(self, request):
        r"""This API is used to create a file system snapshot.

        :param request: Request instance for CreateCfsSnapshot.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsSnapshotRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCfsSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataFlow(self, request):
        r"""This API is used to create a data flow.

        :param request: Request instance for CreateDataFlow.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateDataFlowRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateDataFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLifecycleDataTask(self, request):
        r"""Support proactive settlement/preheat API.

        :param request: Request instance for CreateLifecycleDataTask.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateLifecycleDataTaskRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateLifecycleDataTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLifecycleDataTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLifecycleDataTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLifecyclePolicy(self, request):
        r"""This API is used to create a file storage lifecycle policy.

        :param request: Request instance for CreateLifecyclePolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateLifecyclePolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateLifecyclePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLifecyclePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLifecyclePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLifecyclePolicyDownloadTask(self, request):
        r"""Download the file list in a lifecycle task.

        :param request: Request instance for CreateLifecyclePolicyDownloadTask.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateLifecyclePolicyDownloadTaskRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateLifecyclePolicyDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLifecyclePolicyDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLifecyclePolicyDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMigrationTask(self, request):
        r"""This API is used to create a migration task.

        :param request: Request instance for CreateMigrationTask.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateMigrationTaskRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAutoSnapshotPolicy(self, request):
        r"""This API is used to delete a scheduled snapshot policy.

        :param request: Request instance for DeleteAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCfsFileSystem(self, request):
        r"""This API is used to delete a file system.

        :param request: Request instance for DeleteCfsFileSystem.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsFileSystemRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCfsFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCfsPGroup(self, request):
        r"""This API is used to delete a permission group. Only permission groups not bound to a file system can be deleted by this API.

        :param request: Request instance for DeleteCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCfsPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCfsRule(self, request):
        r"""This API is used to delete a permission group rule.

        :param request: Request instance for DeleteCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCfsRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCfsSnapshot(self, request):
        r"""This API is used to delete a file system snapshot.

        :param request: Request instance for DeleteCfsSnapshot.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsSnapshotRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCfsSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataFlow(self, request):
        r"""Delete a data flow.

        :param request: Request instance for DeleteDataFlow.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteDataFlowRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteDataFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLifecyclePolicy(self, request):
        r"""Delete a lifecycle management policy.

        :param request: Request instance for DeleteLifecyclePolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteLifecyclePolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteLifecyclePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLifecyclePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLifecyclePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMigrationTask(self, request):
        r"""This API is used to delete migration tasks. Deletion is not supported for tasks in the status of Waiting, creating, running, canceling, or terminating.

        :param request: Request instance for DeleteMigrationTask.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteMigrationTaskRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoSnapshotPolicies(self, request):
        r"""This API is used to query the list of scheduled snapshot policies of a file system.

        :param request: Request instance for DescribeAutoSnapshotPolicies.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeAutoSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeAutoSnapshotPoliciesResponse`

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


    def DescribeAvailableZoneInfo(self, request):
        r"""This API is used to query the availability of a region.

        :param request: Request instance for DescribeAvailableZoneInfo.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeAvailableZoneInfoRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeAvailableZoneInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableZoneInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableZoneInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBucketList(self, request):
        r"""To obtain the list of data source buckets.

        :param request: Request instance for DescribeBucketList.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeBucketListRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeBucketListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBucketList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBucketListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsFileSystemClients(self, request):
        r"""This API is used to query clients on which this file system is mounted. To do so, the client needs to have the CFS monitoring plugin installed.

        :param request: Request instance for DescribeCfsFileSystemClients.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemClientsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemClientsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsFileSystemClients", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsFileSystemClientsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsFileSystems(self, request):
        r"""This API is used to query file systems.

        :param request: Request instance for DescribeCfsFileSystems.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsFileSystems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsFileSystemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsPGroups(self, request):
        r"""This API is used to query the list of permission groups.

        :param request: Request instance for DescribeCfsPGroups.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsPGroupsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsPGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsPGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsPGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsRules(self, request):
        r"""This API is used to query the list of permission group rules.

        :param request: Request instance for DescribeCfsRules.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsRulesRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsServiceStatus(self, request):
        r"""This API is used to query the status of the CFS service.

        :param request: Request instance for DescribeCfsServiceStatus.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsServiceStatusRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsServiceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsServiceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsServiceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsSnapshotOverview(self, request):
        r"""This API is used to get the snapshot overview of a file system.

        :param request: Request instance for DescribeCfsSnapshotOverview.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotOverviewRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsSnapshotOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsSnapshotOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsSnapshots(self, request):
        r"""This API is used to query the list of snapshots of a file system.

        :param request: Request instance for DescribeCfsSnapshots.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataFlow(self, request):
        r"""This API is used to query data flow information.

        :param request: Request instance for DescribeDataFlow.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeDataFlowRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeDataFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLifecycleDataTask(self, request):
        r"""This API is used to query the lifecycle task. It only supports querying task data within 3 months.

        :param request: Request instance for DescribeLifecycleDataTask.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeLifecycleDataTaskRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeLifecycleDataTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLifecycleDataTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLifecycleDataTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLifecyclePolicies(self, request):
        r"""Query lifecycle management policies.

        :param request: Request instance for DescribeLifecyclePolicies.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeLifecyclePoliciesRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeLifecyclePoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLifecyclePolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLifecyclePoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationTasks(self, request):
        r"""This API is used to get the list of migration tasks.
        To use this API, submit a ticket for us to add you to the allowlist.

        :param request: Request instance for DescribeMigrationTasks.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeMigrationTasksRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeMigrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMountTargets(self, request):
        r"""This API is used to query the mount targets of a file system.

        :param request: Request instance for DescribeMountTargets.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeMountTargetsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeMountTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMountTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMountTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotOperationLogs(self, request):
        r"""This API is used to query the operation logs of a snapshot.

        :param request: Request instance for DescribeSnapshotOperationLogs.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeSnapshotOperationLogsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeSnapshotOperationLogsResponse`

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


    def DoDirectoryOperation(self, request):
        r"""File system directory operation API. Currently, only the Turbo series file system supports calling this API to perform directory operations. The Universal Series file system (including the enhanced version) does not support calling.

        :param request: Request instance for DoDirectoryOperation.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DoDirectoryOperationRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DoDirectoryOperationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DoDirectoryOperation", params, headers=headers)
            response = json.loads(body)
            model = models.DoDirectoryOperationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataFlow(self, request):
        r"""Modify data flow parameters.

        :param request: Request instance for ModifyDataFlow.
        :type request: :class:`tencentcloud.cfs.v20190719.models.ModifyDataFlowRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.ModifyDataFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileSystemAutoScaleUpRule(self, request):
        r"""This API is used to set the file system scaling policy. It supports only the turbo file system.

        :param request: Request instance for ModifyFileSystemAutoScaleUpRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.ModifyFileSystemAutoScaleUpRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.ModifyFileSystemAutoScaleUpRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileSystemAutoScaleUpRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileSystemAutoScaleUpRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLifecyclePolicy(self, request):
        r"""Update a file storage lifecycle policy.

        :param request: Request instance for ModifyLifecyclePolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.ModifyLifecyclePolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.ModifyLifecyclePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLifecyclePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLifecyclePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleUpFileSystem(self, request):
        r"""This API is used to expand the turbo file system. It only supports expansion and does not support scale-down. The scaling increment for the turbo standard type is 10240 GIB, and for the turbo performance type, it is 5120 GIB.

        :param request: Request instance for ScaleUpFileSystem.
        :type request: :class:`tencentcloud.cfs.v20190719.models.ScaleUpFileSystemRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.ScaleUpFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleUpFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleUpFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SignUpCfsService(self, request):
        r"""This API is used to activate the CFS service.

        :param request: Request instance for SignUpCfsService.
        :type request: :class:`tencentcloud.cfs.v20190719.models.SignUpCfsServiceRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.SignUpCfsServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SignUpCfsService", params, headers=headers)
            response = json.loads(body)
            model = models.SignUpCfsServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopLifecycleDataTask(self, request):
        r"""This API is used to terminate a lifecycle task.

        :param request: Request instance for StopLifecycleDataTask.
        :type request: :class:`tencentcloud.cfs.v20190719.models.StopLifecycleDataTaskRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.StopLifecycleDataTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopLifecycleDataTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopLifecycleDataTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopMigrationTask(self, request):
        r"""This API is used to terminate a migration task, including tasks in the Waiting or Running status.

        :param request: Request instance for StopMigrationTask.
        :type request: :class:`tencentcloud.cfs.v20190719.models.StopMigrationTaskRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.StopMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindAutoSnapshotPolicy(self, request):
        r"""This API is used to unbind a snapshot policy from a file system.

        :param request: Request instance for UnbindAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UnbindAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UnbindAutoSnapshotPolicyResponse`

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


    def UpdateAutoSnapshotPolicy(self, request):
        r"""This API is used to update a scheduled snapshot policy.

        :param request: Request instance for UpdateAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsFileSystemName(self, request):
        r"""This API is used to update a file system name.

        :param request: Request instance for UpdateCfsFileSystemName.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemNameRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsFileSystemName", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsFileSystemNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsFileSystemPGroup(self, request):
        r"""This API is used to update the permission group used by a file system.

        :param request: Request instance for UpdateCfsFileSystemPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsFileSystemPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsFileSystemPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsFileSystemSizeLimit(self, request):
        r"""This API is used to update the capacity limit of a file system.

        :param request: Request instance for UpdateCfsFileSystemSizeLimit.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemSizeLimitRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemSizeLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsFileSystemSizeLimit", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsFileSystemSizeLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsPGroup(self, request):
        r"""This API is used to update the information of a permission group.

        :param request: Request instance for UpdateCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsRule(self, request):
        r"""This API is used to update a permission rule.

        :param request: Request instance for UpdateCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsSnapshotAttribute(self, request):
        r"""This API is used to update the name and retention period of a file system snapshot.

        :param request: Request instance for UpdateCfsSnapshotAttribute.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsSnapshotAttributeRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsSnapshotAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsSnapshotAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsSnapshotAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))