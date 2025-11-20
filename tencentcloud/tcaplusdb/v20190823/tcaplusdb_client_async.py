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
from tencentcloud.tcaplusdb.v20190823 import models
from typing import Dict


class TcaplusdbClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'tcaplusdb.intl.tencentcloudapi.com'
    _service = 'tcaplusdb'

    async def ClearTables(
            self,
            request: models.ClearTablesRequest,
            opts: Dict = None,
    ) -> models.ClearTablesResponse:
        """
        This API is used to clear table data based on the specified table information.
        """
        
        kwargs = {}
        kwargs["action"] = "ClearTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompareIdlFiles(
            self,
            request: models.CompareIdlFilesRequest,
            opts: Dict = None,
    ) -> models.CompareIdlFilesResponse:
        """
        This API is used to select a target table, upload and verify the table modification file, and return the result of whether the table structure is allowed to be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "CompareIdlFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompareIdlFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackup(
            self,
            request: models.CreateBackupRequest,
            opts: Dict = None,
    ) -> models.CreateBackupResponse:
        """
        This API is used to create a backup task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        This API is used to create a TcaplusDB cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshots(
            self,
            request: models.CreateSnapshotsRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotsResponse:
        """
        This API is used to create one or more table snapshots at a specified past time point.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTableGroup(
            self,
            request: models.CreateTableGroupRequest,
            opts: Dict = None,
    ) -> models.CreateTableGroupResponse:
        """
        This API is used to create a table group in a TcaplusDB cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTableGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTableGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTables(
            self,
            request: models.CreateTablesRequest,
            opts: Dict = None,
    ) -> models.CreateTablesResponse:
        """
        This API is used to create tables in batches based on the selected IDL file list.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackupRecords(
            self,
            request: models.DeleteBackupRecordsRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupRecordsResponse:
        """
        This API is used to delete a manual backup.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackupRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        This API is used to delete a TcaplusDB cluster, which will succeed only after all resources (including table groups and tables) in the cluster are released.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIdlFiles(
            self,
            request: models.DeleteIdlFilesRequest,
            opts: Dict = None,
    ) -> models.DeleteIdlFilesResponse:
        """
        This API is used to delete a target IDL file by specifying the cluster ID and information of the file to be deleted. If the file is associated with a table, deletion will fail.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIdlFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIdlFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshots(
            self,
            request: models.DeleteSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotsResponse:
        """
        This API is used to delete one or more table snapshots.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTableDataFlow(
            self,
            request: models.DeleteTableDataFlowRequest,
            opts: Dict = None,
    ) -> models.DeleteTableDataFlowResponse:
        """
        This API is used to disable data subscription for tables.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTableDataFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableDataFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTableGroup(
            self,
            request: models.DeleteTableGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteTableGroupResponse:
        """
        This API is used to delete a table group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTableGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTableIndex(
            self,
            request: models.DeleteTableIndexRequest,
            opts: Dict = None,
    ) -> models.DeleteTableIndexResponse:
        """
        This API is used to delete the global index from a table.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTableIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTables(
            self,
            request: models.DeleteTablesRequest,
            opts: Dict = None,
    ) -> models.DeleteTablesResponse:
        """
        This API is used to drop a specified table. Calling this API for the first time means to move the table to the recycle bin, while calling it again means to drop the table completely from the recycle bin.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupRecords(
            self,
            request: models.DescribeBackupRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupRecordsResponse:
        """
        This API is used to query backup records.

        When querying the cluster level, set `TableGroupId` to `-1` and `TableName` to `-1`.
        When querying the cluster and table group levels, set `TableName` to `-1`.
        When querying the cluster, table group, and table levels, both `TableGroupId` and `TableName` cannot be set to `-1`.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterTags(
            self,
            request: models.DescribeClusterTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterTagsResponse:
        """
        This API is used to get the associated tag list of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        This API is used to query the TcaplusDB cluster list, including cluster details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdlFileInfos(
            self,
            request: models.DescribeIdlFileInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeIdlFileInfosResponse:
        """
        This API is used to query table description file details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdlFileInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdlFileInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachine(
            self,
            request: models.DescribeMachineRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineResponse:
        """
        This API is used to query the available machines in a dedicated cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        This API is used to query the list of regions supported by the TcaplusDB service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshots(
            self,
            request: models.DescribeSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotsResponse:
        """
        This API is used to query the list of table snapshots.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableGroupTags(
            self,
            request: models.DescribeTableGroupTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTableGroupTagsResponse:
        """
        This API is used to get the associated tag list of a table group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableGroupTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableGroupTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableGroups(
            self,
            request: models.DescribeTableGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeTableGroupsResponse:
        """
        This API is used to query the table group list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableTags(
            self,
            request: models.DescribeTableTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTableTagsResponse:
        """
        This API is used to get table tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTables(
            self,
            request: models.DescribeTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesResponse:
        """
        This API is used to query table details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTablesInRecycle(
            self,
            request: models.DescribeTablesInRecycleRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesInRecycleResponse:
        """
        This API is used to query the details of a table in recycle bin.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTablesInRecycle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesInRecycleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        This API is used to query the task list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUinInWhitelist(
            self,
            request: models.DescribeUinInWhitelistRequest,
            opts: Dict = None,
    ) -> models.DescribeUinInWhitelistResponse:
        """
        This API is used to query whether the current user is in the allowlist and control whether the user can create TDR-type apps or tables.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUinInWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUinInWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableRestProxy(
            self,
            request: models.DisableRestProxyRequest,
            opts: Dict = None,
    ) -> models.DisableRestProxyResponse:
        """
        This API is used to disable the RESTful API.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableRestProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableRestProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableRestProxy(
            self,
            request: models.EnableRestProxyRequest,
            opts: Dict = None,
    ) -> models.EnableRestProxyResponse:
        """
        This API is used to enable the RESTful API.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableRestProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableRestProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportSnapshots(
            self,
            request: models.ImportSnapshotsRequest,
            opts: Dict = None,
    ) -> models.ImportSnapshotsResponse:
        """
        This API is used to import a snapshot into a new table or the original table from which the snapshot was created.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MergeTablesData(
            self,
            request: models.MergeTablesDataRequest,
            opts: Dict = None,
    ) -> models.MergeTablesDataResponse:
        """
        This API is used to merge tables.
        """
        
        kwargs = {}
        kwargs["action"] = "MergeTablesData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MergeTablesDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCensorship(
            self,
            request: models.ModifyCensorshipRequest,
            opts: Dict = None,
    ) -> models.ModifyCensorshipResponse:
        """
        This API is used to enable or disable the cluster operation approval feature.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCensorship"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCensorshipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterMachine(
            self,
            request: models.ModifyClusterMachineRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterMachineResponse:
        """
        This API is used to modify the machines of a dedicated cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterName(
            self,
            request: models.ModifyClusterNameRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterNameResponse:
        """
        This API is used to rename a specified cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterPassword(
            self,
            request: models.ModifyClusterPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterPasswordResponse:
        """
        This API is used to change the password of a specified cluster. The backend will allow the TcaplusDB SDK to access databases with both old and new passwords before the old password expires. You cannot submit a new password change request before the old password expires or submit a request to modify the expiration time of the old password after the old password expires.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterTags(
            self,
            request: models.ModifyClusterTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterTagsResponse:
        """
        This API is used to modify cluster tags.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshots(
            self,
            request: models.ModifySnapshotsRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotsResponse:
        """
        This API is used to modify the expiration time of one or more table snapshots.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableGroupName(
            self,
            request: models.ModifyTableGroupNameRequest,
            opts: Dict = None,
    ) -> models.ModifyTableGroupNameResponse:
        """
        This API is used to rename a TcaplusDB table group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableGroupName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableGroupNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableGroupTags(
            self,
            request: models.ModifyTableGroupTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyTableGroupTagsResponse:
        """
        This API is used to modify table group tags.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableGroupTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableGroupTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableMemos(
            self,
            request: models.ModifyTableMemosRequest,
            opts: Dict = None,
    ) -> models.ModifyTableMemosResponse:
        """
        This API is used to modify table remarks.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableMemos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableMemosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableQuotas(
            self,
            request: models.ModifyTableQuotasRequest,
            opts: Dict = None,
    ) -> models.ModifyTableQuotasResponse:
        """
        This API is used to scale a table.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableTags(
            self,
            request: models.ModifyTableTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyTableTagsResponse:
        """
        This API is used to modify table tags.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTables(
            self,
            request: models.ModifyTablesRequest,
            opts: Dict = None,
    ) -> models.ModifyTablesResponse:
        """
        This API is used to modify specified tables in batches based on the selected table definition IDL file.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverRecycleTables(
            self,
            request: models.RecoverRecycleTablesRequest,
            opts: Dict = None,
    ) -> models.RecoverRecycleTablesResponse:
        """
        This API is used to recover a dropped table from the recycle bin. It will not work for tables to be released due to arrears.
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverRecycleTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverRecycleTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackTables(
            self,
            request: models.RollbackTablesRequest,
            opts: Dict = None,
    ) -> models.RollbackTablesResponse:
        """
        This API is used to roll back table data.
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetBackupExpireRule(
            self,
            request: models.SetBackupExpireRuleRequest,
            opts: Dict = None,
    ) -> models.SetBackupExpireRuleResponse:
        """
        This API is used to add/delete/modify backup expiration policy. `ClusterId` must be a specific cluster ID (appid).
        """
        
        kwargs = {}
        kwargs["action"] = "SetBackupExpireRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetBackupExpireRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTableDataFlow(
            self,
            request: models.SetTableDataFlowRequest,
            opts: Dict = None,
    ) -> models.SetTableDataFlowResponse:
        """
        This API is used to enable data subscription for tables or modify the feature's configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "SetTableDataFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTableDataFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTableIndex(
            self,
            request: models.SetTableIndexRequest,
            opts: Dict = None,
    ) -> models.SetTableIndexResponse:
        """
        This API is used to create a global index for a table.
        """
        
        kwargs = {}
        kwargs["action"] = "SetTableIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTableIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateApply(
            self,
            request: models.UpdateApplyRequest,
            opts: Dict = None,
    ) -> models.UpdateApplyResponse:
        """
        This API is used to update the application status.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyIdlFiles(
            self,
            request: models.VerifyIdlFilesRequest,
            opts: Dict = None,
    ) -> models.VerifyIdlFilesResponse:
        """
        This API is used to upload and verify a table creation file and return the definition of tables that are verified to be valid.
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyIdlFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyIdlFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)