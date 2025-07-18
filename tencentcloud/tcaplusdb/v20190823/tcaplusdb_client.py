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
from tencentcloud.tcaplusdb.v20190823 import models


class TcaplusdbClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'tcaplusdb.intl.tencentcloudapi.com'
    _service = 'tcaplusdb'


    def ClearTables(self, request):
        """This API is used to clear table data based on the specified table information.

        :param request: Request instance for ClearTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ClearTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ClearTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearTables", params, headers=headers)
            response = json.loads(body)
            model = models.ClearTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompareIdlFiles(self, request):
        """This API is used to select a target table, upload and verify the table modification file, and return the result of whether the table structure is allowed to be modified.

        :param request: Request instance for CompareIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareIdlFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompareIdlFiles", params, headers=headers)
            response = json.loads(body)
            model = models.CompareIdlFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackup(self, request):
        """This API is used to create a backup task.

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        """This API is used to create a TcaplusDB cluster.

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSnapshots(self, request):
        """This API is used to create one or more table snapshots at a specified past time point.

        :param request: Request instance for CreateSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTableGroup(self, request):
        """This API is used to create a table group in a TcaplusDB cluster.

        :param request: Request instance for CreateTableGroup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTableGroupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTableGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTableGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTableGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTables(self, request):
        """This API is used to create tables in batches based on the selected IDL file list.

        :param request: Request instance for CreateTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTables", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackupRecords(self, request):
        """This API is used to delete a manual backup.

        :param request: Request instance for DeleteBackupRecords.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteBackupRecordsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteBackupRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackupRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCluster(self, request):
        """This API is used to delete a TcaplusDB cluster, which will succeed only after all resources (including table groups and tables) in the cluster are released.

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIdlFiles(self, request):
        """This API is used to delete a target IDL file by specifying the cluster ID and information of the file to be deleted. If the file is associated with a table, deletion will fail.

        :param request: Request instance for DeleteIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteIdlFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIdlFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIdlFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshots(self, request):
        """This API is used to delete one or more table snapshots.

        :param request: Request instance for DeleteSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteSnapshotsResponse`

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


    def DeleteTableDataFlow(self, request):
        """This API is used to disable data subscription for tables.

        :param request: Request instance for DeleteTableDataFlow.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableDataFlowRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableDataFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTableDataFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableDataFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTableGroup(self, request):
        """This API is used to delete a table group.

        :param request: Request instance for DeleteTableGroup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableGroupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTableGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTableIndex(self, request):
        """This API is used to delete the global index from a table.

        :param request: Request instance for DeleteTableIndex.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableIndexRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTableIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTables(self, request):
        """This API is used to drop a specified table. Calling this API for the first time means to move the table to the recycle bin, while calling it again means to drop the table completely from the recycle bin.

        :param request: Request instance for DeleteTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTables", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupRecords(self, request):
        """This API is used to query backup records.

        When querying the cluster level, set `TableGroupId` to `-1` and `TableName` to `-1`.
        When querying the cluster and table group levels, set `TableName` to `-1`.
        When querying the cluster, table group, and table levels, both `TableGroupId` and `TableName` cannot be set to `-1`.

        :param request: Request instance for DescribeBackupRecords.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeBackupRecordsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeBackupRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterTags(self, request):
        """This API is used to get the associated tag list of a cluster.

        :param request: Request instance for DescribeClusterTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClusterTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClusterTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusters(self, request):
        """This API is used to query the TcaplusDB cluster list, including cluster details.

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdlFileInfos(self, request):
        """This API is used to query table description file details.

        :param request: Request instance for DescribeIdlFileInfos.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeIdlFileInfosRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeIdlFileInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdlFileInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdlFileInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachine(self, request):
        """This API is used to query the available machines in a dedicated cluster.

        :param request: Request instance for DescribeMachine.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeMachineRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """This API is used to query the list of regions supported by the TcaplusDB service.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshots(self, request):
        """This API is used to query the list of table snapshots.

        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeSnapshotsResponse`

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


    def DescribeTableGroupTags(self, request):
        """This API is used to get the associated tag list of a table group.

        :param request: Request instance for DescribeTableGroupTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableGroupTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableGroupTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableGroups(self, request):
        """This API is used to query the table group list.

        :param request: Request instance for DescribeTableGroups.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableTags(self, request):
        """This API is used to get table tags.

        :param request: Request instance for DescribeTableTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTables(self, request):
        """This API is used to query table details.

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTablesInRecycle(self, request):
        """This API is used to query the details of a table in recycle bin.

        :param request: Request instance for DescribeTablesInRecycle.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesInRecycleRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesInRecycleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTablesInRecycle", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesInRecycleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        """This API is used to query the task list.

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUinInWhitelist(self, request):
        """This API is used to query whether the current user is in the allowlist and control whether the user can create TDR-type apps or tables.

        :param request: Request instance for DescribeUinInWhitelist.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeUinInWhitelistRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeUinInWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUinInWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUinInWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableRestProxy(self, request):
        """This API is used to disable the RESTful API.

        :param request: Request instance for DisableRestProxy.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DisableRestProxyRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DisableRestProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableRestProxy", params, headers=headers)
            response = json.loads(body)
            model = models.DisableRestProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableRestProxy(self, request):
        """This API is used to enable the RESTful API.

        :param request: Request instance for EnableRestProxy.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.EnableRestProxyRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.EnableRestProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableRestProxy", params, headers=headers)
            response = json.loads(body)
            model = models.EnableRestProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportSnapshots(self, request):
        """This API is used to import a snapshot into a new table or the original table from which the snapshot was created.

        :param request: Request instance for ImportSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ImportSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ImportSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.ImportSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MergeTablesData(self, request):
        """This API is used to merge tables.

        :param request: Request instance for MergeTablesData.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.MergeTablesDataRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.MergeTablesDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MergeTablesData", params, headers=headers)
            response = json.loads(body)
            model = models.MergeTablesDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCensorship(self, request):
        """This API is used to enable or disable the cluster operation approval feature.

        :param request: Request instance for ModifyCensorship.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyCensorshipRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyCensorshipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCensorship", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCensorshipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterMachine(self, request):
        """This API is used to modify the machines of a dedicated cluster.

        :param request: Request instance for ModifyClusterMachine.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterMachineRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterMachine", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterName(self, request):
        """This API is used to rename a specified cluster.

        :param request: Request instance for ModifyClusterName.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterNameRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterPassword(self, request):
        """This API is used to change the password of a specified cluster. The backend will allow the TcaplusDB SDK to access databases with both old and new passwords before the old password expires. You cannot submit a new password change request before the old password expires or submit a request to modify the expiration time of the old password after the old password expires.

        :param request: Request instance for ModifyClusterPassword.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterPasswordRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterTags(self, request):
        """This API is used to modify cluster tags.

        :param request: Request instance for ModifyClusterTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshots(self, request):
        """This API is used to modify the expiration time of one or more table snapshots.

        :param request: Request instance for ModifySnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifySnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifySnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableGroupName(self, request):
        """This API is used to rename a TcaplusDB table group.

        :param request: Request instance for ModifyTableGroupName.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupNameRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableGroupName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableGroupNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableGroupTags(self, request):
        """This API is used to modify table group tags.

        :param request: Request instance for ModifyTableGroupTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableGroupTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableGroupTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableMemos(self, request):
        """This API is used to modify table remarks.

        :param request: Request instance for ModifyTableMemos.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableMemosRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableMemosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableMemos", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableMemosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableQuotas(self, request):
        """This API is used to scale a table.

        :param request: Request instance for ModifyTableQuotas.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableQuotasRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableTags(self, request):
        """This API is used to modify table tags.

        :param request: Request instance for ModifyTableTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTables(self, request):
        """This API is used to modify specified tables in batches based on the selected table definition IDL file.

        :param request: Request instance for ModifyTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTables", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverRecycleTables(self, request):
        """This API is used to recover a dropped table from the recycle bin. It will not work for tables to be released due to arrears.

        :param request: Request instance for RecoverRecycleTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.RecoverRecycleTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.RecoverRecycleTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverRecycleTables", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverRecycleTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackTables(self, request):
        """This API is used to roll back table data.

        :param request: Request instance for RollbackTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.RollbackTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.RollbackTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackTables", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetBackupExpireRule(self, request):
        """This API is used to add/delete/modify backup expiration policy. `ClusterId` must be a specific cluster ID (appid).

        :param request: Request instance for SetBackupExpireRule.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.SetBackupExpireRuleRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.SetBackupExpireRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetBackupExpireRule", params, headers=headers)
            response = json.loads(body)
            model = models.SetBackupExpireRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTableDataFlow(self, request):
        """This API is used to enable data subscription for tables or modify the feature's configurations.

        :param request: Request instance for SetTableDataFlow.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableDataFlowRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableDataFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTableDataFlow", params, headers=headers)
            response = json.loads(body)
            model = models.SetTableDataFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTableIndex(self, request):
        """This API is used to create a global index for a table.

        :param request: Request instance for SetTableIndex.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableIndexRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTableIndex", params, headers=headers)
            response = json.loads(body)
            model = models.SetTableIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateApply(self, request):
        """This API is used to update the application status.

        :param request: Request instance for UpdateApply.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.UpdateApplyRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.UpdateApplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApply", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyIdlFiles(self, request):
        """This API is used to upload and verify a table creation file and return the definition of tables that are verified to be valid.

        :param request: Request instance for VerifyIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.VerifyIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.VerifyIdlFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyIdlFiles", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyIdlFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))