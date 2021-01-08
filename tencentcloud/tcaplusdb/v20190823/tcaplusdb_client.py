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
from tencentcloud.tcaplusdb.v20190823 import models


class TcaplusdbClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'tcaplusdb.tencentcloudapi.com'
    _service = 'tcaplusdb'


    def ClearTables(self, request):
        """This API is used to clear table data based on the specified table information.

        :param request: Request instance for ClearTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ClearTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ClearTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ClearTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearTablesResponse()
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


    def CompareIdlFiles(self, request):
        """This API is used to select a target table, upload and verify the table modification file, and return the result of whether the table structure is allowed to be modified.

        :param request: Request instance for CompareIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareIdlFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompareIdlFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompareIdlFilesResponse()
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


    def CreateBackup(self, request):
        """This API is used to create a backup task.

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBackup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBackupResponse()
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


    def CreateCluster(self, request):
        """This API is used to create a TcaplusDB cluster.

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterResponse()
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


    def CreateTableGroup(self, request):
        """This API is used to create a table group in a TcaplusDB cluster.

        :param request: Request instance for CreateTableGroup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTableGroupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTableGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTableGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTableGroupResponse()
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


    def CreateTables(self, request):
        """This API is used to create tables in batches based on the selected IDL file list.

        :param request: Request instance for CreateTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTablesResponse()
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


    def DeleteCluster(self, request):
        """This API is used to delete a TcaplusDB cluster, which will succeed only after all resources (including table groups and tables) in the cluster are released.

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterResponse()
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


    def DeleteIdlFiles(self, request):
        """This API is used to delete a target IDL file by specifying the cluster ID and information of the file to be deleted. If the file is associated with a table, deletion will fail.

        :param request: Request instance for DeleteIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteIdlFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteIdlFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteIdlFilesResponse()
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


    def DeleteTableGroup(self, request):
        """This API is used to delete a table group.

        :param request: Request instance for DeleteTableGroup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableGroupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTableGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTableGroupResponse()
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


    def DeleteTableIndex(self, request):
        """This API is used to delete the global index from a table.

        :param request: Request instance for DeleteTableIndex.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableIndexRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableIndexResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTableIndex", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTableIndexResponse()
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


    def DeleteTables(self, request):
        """This API is used to drop a specified table. Calling this API for the first time means to move the table to the recycle bin, while calling it again means to drop the table completely from the recycle bin.

        :param request: Request instance for DeleteTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTablesResponse()
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


    def DescribeClusterTags(self, request):
        """This API is used to get the associated tag list of a cluster.

        :param request: Request instance for DescribeClusterTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClusterTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClusterTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterTagsResponse()
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


    def DescribeClusters(self, request):
        """This API is used to query the TcaplusDB cluster list, including cluster details.

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClustersResponse()
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


    def DescribeIdlFileInfos(self, request):
        """This API is used to query table description file details.

        :param request: Request instance for DescribeIdlFileInfos.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeIdlFileInfosRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeIdlFileInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIdlFileInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIdlFileInfosResponse()
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


    def DescribeMachine(self, request):
        """This API is used to query the available machines in a dedicated cluster.

        :param request: Request instance for DescribeMachine.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeMachineRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeMachineResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMachine", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMachineResponse()
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


    def DescribeRegions(self, request):
        """This API is used to query the list of regions supported by the TcaplusDB service.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def DescribeTableGroupTags(self, request):
        """This API is used to get the associated tag list of a table group.

        :param request: Request instance for DescribeTableGroupTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTableGroupTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTableGroupTagsResponse()
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


    def DescribeTableGroups(self, request):
        """This API is used to query the table group list.

        :param request: Request instance for DescribeTableGroups.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTableGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTableGroupsResponse()
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


    def DescribeTableTags(self, request):
        """This API is used to get table tags.

        :param request: Request instance for DescribeTableTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTableTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTableTagsResponse()
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


    def DescribeTables(self, request):
        """This API is used to query table details.

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTablesResponse()
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


    def DescribeTablesInRecycle(self, request):
        """This API is used to query the details of a table in recycle bin.

        :param request: Request instance for DescribeTablesInRecycle.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesInRecycleRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesInRecycleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTablesInRecycle", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTablesInRecycleResponse()
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


    def DescribeTasks(self, request):
        """This API is used to query the task list.

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
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


    def DescribeUinInWhitelist(self, request):
        """This API is used to query whether the current user is in the allowlist and control whether the user can create TDR-type apps or tables.

        :param request: Request instance for DescribeUinInWhitelist.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeUinInWhitelistRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeUinInWhitelistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUinInWhitelist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUinInWhitelistResponse()
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


    def ModifyClusterMachine(self, request):
        """This API is used to modify the machines of a dedicated cluster.

        :param request: Request instance for ModifyClusterMachine.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterMachineRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterMachineResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterMachine", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterMachineResponse()
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


    def ModifyClusterName(self, request):
        """This API is used to rename a specified cluster.

        :param request: Request instance for ModifyClusterName.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterNameRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterNameResponse()
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


    def ModifyClusterPassword(self, request):
        """This API is used to change the password of a specified cluster. The backend will allow the TcaplusDB SDK to access databases with both old and new passwords before the old password expires. You cannot submit a new password change request before the old password expires or submit a request to modify the expiration time of the old password after the old password expires.

        :param request: Request instance for ModifyClusterPassword.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterPasswordRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterPasswordResponse()
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


    def ModifyClusterTags(self, request):
        """This API is used to modify cluster tags.

        :param request: Request instance for ModifyClusterTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterTagsResponse()
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


    def ModifyTableGroupName(self, request):
        """This API is used to rename a TcaplusDB table group.

        :param request: Request instance for ModifyTableGroupName.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupNameRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableGroupName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableGroupNameResponse()
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


    def ModifyTableGroupTags(self, request):
        """This API is used to modify table group tags.

        :param request: Request instance for ModifyTableGroupTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableGroupTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableGroupTagsResponse()
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


    def ModifyTableMemos(self, request):
        """This API is used to modify table remarks.

        :param request: Request instance for ModifyTableMemos.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableMemosRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableMemosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableMemos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableMemosResponse()
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


    def ModifyTableQuotas(self, request):
        """This API is used to scale a table.

        :param request: Request instance for ModifyTableQuotas.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableQuotasRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableQuotasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableQuotas", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableQuotasResponse()
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


    def ModifyTableTags(self, request):
        """This API is used to modify table tags.

        :param request: Request instance for ModifyTableTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableTagsResponse()
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


    def ModifyTables(self, request):
        """This API is used to modify specified tables in batches based on the selected table definition IDL file.

        :param request: Request instance for ModifyTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTablesResponse()
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


    def RecoverRecycleTables(self, request):
        """This API is used to recover a dropped table from the recycle bin. It will not work for tables to be released due to arrears.

        :param request: Request instance for RecoverRecycleTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.RecoverRecycleTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.RecoverRecycleTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecoverRecycleTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecoverRecycleTablesResponse()
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


    def RollbackTables(self, request):
        """This API is used to roll back table data.

        :param request: Request instance for RollbackTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.RollbackTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.RollbackTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RollbackTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RollbackTablesResponse()
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


    def SetTableIndex(self, request):
        """This API is used to create a global index for a table.

        :param request: Request instance for SetTableIndex.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableIndexRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableIndexResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetTableIndex", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetTableIndexResponse()
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


    def VerifyIdlFiles(self, request):
        """This API is used to upload and verify a table creation file and return the definition of tables that are verified to be valid.

        :param request: Request instance for VerifyIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.VerifyIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.VerifyIdlFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyIdlFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyIdlFilesResponse()
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