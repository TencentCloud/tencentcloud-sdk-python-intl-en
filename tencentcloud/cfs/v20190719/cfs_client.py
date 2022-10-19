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
from tencentcloud.cfs.v20190719 import models


class CfsClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'cfs.tencentcloudapi.com'
    _service = 'cfs'


    def BindAutoSnapshotPolicy(self, request):
        """This API is used to bind one or multiple file systems to a snapshot policy. A file system can be bound to only one policy.

        :param request: Request instance for BindAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.BindAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.BindAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindAutoSnapshotPolicy", params, headers=headers)
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
        """This API is used to create a scheduled snapshot policy.

        :param request: Request instance for CreateAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoSnapshotPolicy", params, headers=headers)
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


    def CreateCfsFileSystem(self, request):
        """This API is used to create a file system.

        :param request: Request instance for CreateCfsFileSystem.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsFileSystemRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsFileSystem", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCfsFileSystemResponse()
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


    def CreateCfsPGroup(self, request):
        """This API is used to create a permission group.

        :param request: Request instance for CreateCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsPGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCfsPGroupResponse()
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


    def CreateCfsRule(self, request):
        """This API is used to create a permission group rule.

        :param request: Request instance for CreateCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCfsRuleResponse()
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


    def CreateCfsSnapshot(self, request):
        """This API is used to create a file system snapshot.

        :param request: Request instance for CreateCfsSnapshot.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsSnapshotRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsSnapshot", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCfsSnapshotResponse()
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


    def DeleteAutoSnapshotPolicy(self, request):
        """This API is used to delete a scheduled snapshot policy.

        :param request: Request instance for DeleteAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAutoSnapshotPolicyResponse()
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


    def DeleteCfsFileSystem(self, request):
        """This API is used to delete a file system.

        :param request: Request instance for DeleteCfsFileSystem.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsFileSystemRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsFileSystem", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCfsFileSystemResponse()
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


    def DeleteCfsPGroup(self, request):
        """This API is used to delete a permission group.

        :param request: Request instance for DeleteCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsPGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCfsPGroupResponse()
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


    def DeleteCfsRule(self, request):
        """This API is used to delete a permission group rule.

        :param request: Request instance for DeleteCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCfsRuleResponse()
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


    def DeleteCfsSnapshot(self, request):
        """This API is used to delete a file system snapshot.

        :param request: Request instance for DeleteCfsSnapshot.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsSnapshotRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsSnapshot", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCfsSnapshotResponse()
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


    def DeleteMountTarget(self, request):
        """This API is used to delete a mount target.

        :param request: Request instance for DeleteMountTarget.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteMountTargetRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteMountTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMountTarget", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMountTargetResponse()
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
        """This API is used to query the list of scheduled snapshot policies of a file system.

        :param request: Request instance for DescribeAutoSnapshotPolicies.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeAutoSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeAutoSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoSnapshotPolicies", params, headers=headers)
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


    def DescribeAvailableZoneInfo(self, request):
        """This API is used to query the availability of a region.

        :param request: Request instance for DescribeAvailableZoneInfo.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeAvailableZoneInfoRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeAvailableZoneInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableZoneInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailableZoneInfoResponse()
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


    def DescribeCfsFileSystemClients(self, request):
        """This API is used to query clients on which this file system is mounted. To do so, the client needs to have the CFS monitoring plugin installed.

        :param request: Request instance for DescribeCfsFileSystemClients.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemClientsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemClientsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsFileSystemClients", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsFileSystemClientsResponse()
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


    def DescribeCfsFileSystems(self, request):
        """This API is used to query file systems.

        :param request: Request instance for DescribeCfsFileSystems.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsFileSystems", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsFileSystemsResponse()
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


    def DescribeCfsPGroups(self, request):
        """This API is used to query the list of permission groups.

        :param request: Request instance for DescribeCfsPGroups.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsPGroupsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsPGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsPGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsPGroupsResponse()
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


    def DescribeCfsRules(self, request):
        """This API is used to query the list of permission group rules.

        :param request: Request instance for DescribeCfsRules.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsRulesRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsRulesResponse()
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


    def DescribeCfsServiceStatus(self, request):
        """This API is used to query the status of the CFS service.

        :param request: Request instance for DescribeCfsServiceStatus.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsServiceStatusRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsServiceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsServiceStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsServiceStatusResponse()
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


    def DescribeCfsSnapshotOverview(self, request):
        """This API is used to get the snapshot overview of a file system.

        :param request: Request instance for DescribeCfsSnapshotOverview.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotOverviewRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsSnapshotOverview", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsSnapshotOverviewResponse()
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


    def DescribeCfsSnapshots(self, request):
        """This API is used to query the list of snapshots of a file system.

        :param request: Request instance for DescribeCfsSnapshots.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsSnapshots", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsSnapshotsResponse()
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


    def DescribeMountTargets(self, request):
        """This API is used to query the mount targets of a file system.

        :param request: Request instance for DescribeMountTargets.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeMountTargetsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeMountTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMountTargets", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMountTargetsResponse()
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
        """This API is used to query the operation logs of a snapshot.

        :param request: Request instance for DescribeSnapshotOperationLogs.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeSnapshotOperationLogsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeSnapshotOperationLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotOperationLogs", params, headers=headers)
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


    def SignUpCfsService(self, request):
        """This API is used to activate the CFS service.

        :param request: Request instance for SignUpCfsService.
        :type request: :class:`tencentcloud.cfs.v20190719.models.SignUpCfsServiceRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.SignUpCfsServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SignUpCfsService", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SignUpCfsServiceResponse()
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
        """This API is used to unbind a snapshot policy from a file system.

        :param request: Request instance for UnbindAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UnbindAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UnbindAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindAutoSnapshotPolicy", params, headers=headers)
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


    def UpdateAutoSnapshotPolicy(self, request):
        """This API is used to update a scheduled snapshot policy.

        :param request: Request instance for UpdateAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAutoSnapshotPolicyResponse()
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


    def UpdateCfsFileSystemName(self, request):
        """This API is used to update a file system name.

        :param request: Request instance for UpdateCfsFileSystemName.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemNameRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsFileSystemName", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsFileSystemNameResponse()
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


    def UpdateCfsFileSystemPGroup(self, request):
        """This API is used to update the permission group used by a file system.

        :param request: Request instance for UpdateCfsFileSystemPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsFileSystemPGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsFileSystemPGroupResponse()
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


    def UpdateCfsFileSystemSizeLimit(self, request):
        """This API is used to update the capacity limit of a file system.

        :param request: Request instance for UpdateCfsFileSystemSizeLimit.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemSizeLimitRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemSizeLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsFileSystemSizeLimit", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsFileSystemSizeLimitResponse()
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


    def UpdateCfsPGroup(self, request):
        """This API is used to update the information of a permission group.

        :param request: Request instance for UpdateCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsPGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsPGroupResponse()
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


    def UpdateCfsRule(self, request):
        """This API is used to update a permission rule.

        :param request: Request instance for UpdateCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsRuleResponse()
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


    def UpdateCfsSnapshotAttribute(self, request):
        """This API is used to update the name and retention period of a file system snapshot.

        :param request: Request instance for UpdateCfsSnapshotAttribute.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsSnapshotAttributeRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsSnapshotAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsSnapshotAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsSnapshotAttributeResponse()
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