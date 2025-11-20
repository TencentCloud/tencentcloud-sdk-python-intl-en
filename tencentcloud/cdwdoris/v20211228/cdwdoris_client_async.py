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
from tencentcloud.cdwdoris.v20211228 import models
from typing import Dict


class CdwdorisClient(AbstractClient):
    _apiVersion = '2021-12-28'
    _endpoint = 'cdwdoris.intl.tencentcloudapi.com'
    _service = 'cdwdoris'

    async def ActionAlterUser(
            self,
            request: models.ActionAlterUserRequest,
            opts: Dict = None,
    ) -> models.ActionAlterUserResponse:
        """
        This API is used to add and modify a user.
        """
        
        kwargs = {}
        kwargs["action"] = "ActionAlterUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActionAlterUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelBackupJob(
            self,
            request: models.CancelBackupJobRequest,
            opts: Dict = None,
    ) -> models.CancelBackupJobResponse:
        """
        This API is used to cancel the corresponding backup instance task.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelBackupJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelBackupJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCoolDownWorkingVariableConfigCorrect(
            self,
            request: models.CheckCoolDownWorkingVariableConfigCorrectRequest,
            opts: Dict = None,
    ) -> models.CheckCoolDownWorkingVariableConfigCorrectResponse:
        """
        This API is used to check whether variables and configurations for hot/cold data layering are correct.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCoolDownWorkingVariableConfigCorrect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCoolDownWorkingVariableConfigCorrectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyTableDatas(
            self,
            request: models.CopyTableDatasRequest,
            opts: Dict = None,
    ) -> models.CopyTableDatasResponse:
        """
        This API is used to copy the source table to the target table.
        """
        
        kwargs = {}
        kwargs["action"] = "CopyTableDatas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyTableDatasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackUpSchedule(
            self,
            request: models.CreateBackUpScheduleRequest,
            opts: Dict = None,
    ) -> models.CreateBackUpScheduleResponse:
        """
        This API is used to create or modify backup policies.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackUpSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackUpScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCoolDownPolicy(
            self,
            request: models.CreateCoolDownPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateCoolDownPolicyResponse:
        """
        This API is used to create a hot/cold data layering policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCoolDownPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCoolDownPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatabase(
            self,
            request: models.CreateDatabaseRequest,
            opts: Dict = None,
    ) -> models.CreateDatabaseResponse:
        """
        This API is used to create a TCHouse-D database.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceNew(
            self,
            request: models.CreateInstanceNewRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceNewResponse:
        """
        This API is used to create clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTable(
            self,
            request: models.CreateTableRequest,
            opts: Dict = None,
    ) -> models.CreateTableResponse:
        """
        This API is used to create a TCHouse-D table under the specified database.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkloadGroup(
            self,
            request: models.CreateWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.CreateWorkloadGroupResponse:
        """
        This API is used to create resource groups.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackUpData(
            self,
            request: models.DeleteBackUpDataRequest,
            opts: Dict = None,
    ) -> models.DeleteBackUpDataResponse:
        """
        This API is used to delete backup data.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackUpData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackUpDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTable(
            self,
            request: models.DeleteTableRequest,
            opts: Dict = None,
    ) -> models.DeleteTableResponse:
        """
        This API is used to delete the specified table in the specified database.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkloadGroup(
            self,
            request: models.DeleteWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkloadGroupResponse:
        """
        This API is used to delete resource groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAreaRegion(
            self,
            request: models.DescribeAreaRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeAreaRegionResponse:
        """
        This API is used to display region information and the total number of clusters in each region on the cluster list page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAreaRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAreaRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackUpJob(
            self,
            request: models.DescribeBackUpJobRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpJobResponse:
        """
        This API is used to query the list of backup instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackUpJobDetail(
            self,
            request: models.DescribeBackUpJobDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpJobDetailResponse:
        """
        This API is used to query backup task details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpJobDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpJobDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackUpSchedules(
            self,
            request: models.DescribeBackUpSchedulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpSchedulesResponse:
        """
        This API is used to obtain the scheduled task information for the backup and migration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpSchedules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpSchedulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackUpTables(
            self,
            request: models.DescribeBackUpTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpTablesResponse:
        """
        This API is used to obtain the information of the table available for backup.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackUpTaskDetail(
            self,
            request: models.DescribeBackUpTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpTaskDetailResponse:
        """
        This API is used to query the progress details of backup tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterConfigs(
            self,
            request: models.DescribeClusterConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterConfigsResponse:
        """
        This API is used to get the contents of the latest configuration files (config.xml, metrika.xml, and user.xml) of the cluster and display them to the user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterConfigsHistory(
            self,
            request: models.DescribeClusterConfigsHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterConfigsHistoryResponse:
        """
        This API is used to obtain the modification history of cluster configuration files.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterConfigsHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterConfigsHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCoolDownBackends(
            self,
            request: models.DescribeCoolDownBackendsRequest,
            opts: Dict = None,
    ) -> models.DescribeCoolDownBackendsResponse:
        """
        This API is used to query the list of backend nodes supporting hot/cold data layering.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCoolDownBackends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCoolDownBackendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCoolDownPolicies(
            self,
            request: models.DescribeCoolDownPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeCoolDownPoliciesResponse:
        """
        This API is used to query the list of hot/cold data layering policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCoolDownPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCoolDownPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCoolDownTableData(
            self,
            request: models.DescribeCoolDownTableDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCoolDownTableDataResponse:
        """
        This API is used to query the layered hot and cold data in a table.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCoolDownTableData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCoolDownTableDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCreateTablesDDL(
            self,
            request: models.DescribeCreateTablesDDLRequest,
            opts: Dict = None,
    ) -> models.DescribeCreateTablesDDLResponse:
        """
        This API is used to batch obtain the table creation DDL.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCreateTablesDDL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCreateTablesDDLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabase(
            self,
            request: models.DescribeDatabaseRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseResponse:
        """
        This API is used to obtain the database information under a specific data source.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseAuditDownload(
            self,
            request: models.DescribeDatabaseAuditDownloadRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseAuditDownloadResponse:
        """
        This API is used to download database audit logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseAuditDownload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseAuditDownloadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseAuditRecords(
            self,
            request: models.DescribeDatabaseAuditRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseAuditRecordsResponse:
        """
        This API is used to get database audit records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseAuditRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseAuditRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstance(
            self,
            request: models.DescribeInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceResponse:
        """
        This API is used to query the specific information of a cluster based on the cluster ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodes(
            self,
            request: models.DescribeInstanceNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodesResponse:
        """
        This API is used to get the list of cluster node information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodesInfo(
            self,
            request: models.DescribeInstanceNodesInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodesInfoResponse:
        """
        This API is used to get the BE/FE node roles.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodesInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodesInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodesRole(
            self,
            request: models.DescribeInstanceNodesRoleRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodesRoleResponse:
        """
        This API is used to obtain cluster node roles.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodesRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodesRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceOperationHistory(
            self,
            request: models.DescribeInstanceOperationHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceOperationHistoryResponse:
        """
        This API is used to pull the operation list of the cluster. The API supports pagination query and filtering operation records by time range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceOperationHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceOperationHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceOperations(
            self,
            request: models.DescribeInstanceOperationsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceOperationsResponse:
        """
        This API is used to pull operations of the cluster on the cluster details page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceOperations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceOperationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceState(
            self,
            request: models.DescribeInstanceStateRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceStateResponse:
        """
        This API is used to display cluster status, process progress, etc. in the cluster details page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceUsedSubnets(
            self,
            request: models.DescribeInstanceUsedSubnetsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceUsedSubnetsResponse:
        """
        This API is used to obtain the information of subnets used by the cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceUsedSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceUsedSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to get the list of clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesHealthState(
            self,
            request: models.DescribeInstancesHealthStateRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesHealthStateResponse:
        """
        This API is used to check cluster health
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesHealthState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesHealthStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQueryAnalyse(
            self,
            request: models.DescribeQueryAnalyseRequest,
            opts: Dict = None,
    ) -> models.DescribeQueryAnalyseResponse:
        """
        This API is used to obtain the SQL query details of the Doris user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQueryAnalyse"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQueryAnalyseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRestoreTaskDetail(
            self,
            request: models.DescribeRestoreTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRestoreTaskDetailResponse:
        """
        This API is used to query the progress details of the recovery task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRestoreTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRestoreTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowQueryRecords(
            self,
            request: models.DescribeSlowQueryRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowQueryRecordsResponse:
        """
        This API is used to get the slow log list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowQueryRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowQueryRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowQueryRecordsDownload(
            self,
            request: models.DescribeSlowQueryRecordsDownloadRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowQueryRecordsDownloadResponse:
        """
        This API is used to download slow log files.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowQueryRecordsDownload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowQueryRecordsDownloadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpec(
            self,
            request: models.DescribeSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecResponse:
        """
        This API is used to pull the specification list of data nodes and zookeeper nodes for the cluster on the purchase page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSqlApis(
            self,
            request: models.DescribeSqlApisRequest,
            opts: Dict = None,
    ) -> models.DescribeSqlApisResponse:
        """
        This API is used to query the cluster information by executing SQL commands.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSqlApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSqlApisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTable(
            self,
            request: models.DescribeTableRequest,
            opts: Dict = None,
    ) -> models.DescribeTableResponse:
        """
        This API is used to obtain the table information. It only supports querying table information in the TCHouse-D internal catalog.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableList(
            self,
            request: models.DescribeTableListRequest,
            opts: Dict = None,
    ) -> models.DescribeTableListResponse:
        """
        This API is used to obtain the list of tables under the specified data source and database.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserBindWorkloadGroup(
            self,
            request: models.DescribeUserBindWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeUserBindWorkloadGroupResponse:
        """
        This API is used to obtain the resource information bound to each user in the current cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserBindWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserBindWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserPolicy(
            self,
            request: models.DescribeUserPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeUserPolicyResponse:
        """
        This API is used to obtain detailed information of Doris users, including account information, permission host, and permission configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkloadGroup(
            self,
            request: models.DescribeWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkloadGroupResponse:
        """
        This API is used to obtain resource group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyInstance(
            self,
            request: models.DestroyInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyInstanceResponse:
        """
        This API is used to terminate clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteParametrizedQuery(
            self,
            request: models.ExecuteParametrizedQueryRequest,
            opts: Dict = None,
    ) -> models.ExecuteParametrizedQueryResponse:
        """
        This API is used to execute an SQL query statement with parameters and return the query results.
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteParametrizedQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteParametrizedQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteSelectQuery(
            self,
            request: models.ExecuteSelectQueryRequest,
            opts: Dict = None,
    ) -> models.ExecuteSelectQueryResponse:
        """
        This API is used to query data according to the specified database and table name, and support field selection and pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteSelectQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteSelectQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InsertDatasToTable(
            self,
            request: models.InsertDatasToTableRequest,
            opts: Dict = None,
    ) -> models.InsertDatasToTableResponse:
        """
        This API is used to insert data into TCHouse-D.
        """
        
        kwargs = {}
        kwargs["action"] = "InsertDatasToTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InsertDatasToTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterConfigs(
            self,
            request: models.ModifyClusterConfigsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterConfigsResponse:
        """
        This API is used to modify the XML cluster configuration file on the cluster configuration page.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCoolDownPolicy(
            self,
            request: models.ModifyCoolDownPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyCoolDownPolicyResponse:
        """
        This API is used to modify the hot/cold data layering policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCoolDownPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCoolDownPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseTableAccess(
            self,
            request: models.ModifyDatabaseTableAccessRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseTableAccessResponse:
        """
        This API is used to GRANT and REVOKE the database and table in the Doris database.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseTableAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseTableAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        This API is used to modify the cluster's name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceKeyValConfigs(
            self,
            request: models.ModifyInstanceKeyValConfigsRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceKeyValConfigsResponse:
        """
        This API is used to modify configurations in the KV mode.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceKeyValConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceKeyValConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNodeStatus(
            self,
            request: models.ModifyNodeStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyNodeStatusResponse:
        """
        This API is used to change the node status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNodeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNodeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroups(
            self,
            request: models.ModifySecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupsResponse:
        """
        This API is used to edit security groups.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserBindWorkloadGroup(
            self,
            request: models.ModifyUserBindWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyUserBindWorkloadGroupResponse:
        """
        This API is used to modify the resource group bound to the user.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserBindWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserBindWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserPrivilegesV3(
            self,
            request: models.ModifyUserPrivilegesV3Request,
            opts: Dict = None,
    ) -> models.ModifyUserPrivilegesV3Response:
        """
        This API is used to modify user permissions and support three permission setting categories: catalog, all db, and some db tables.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserPrivilegesV3"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserPrivilegesV3Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkloadGroup(
            self,
            request: models.ModifyWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkloadGroupResponse:
        """
        This API is used to modify the resource group information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkloadGroupStatus(
            self,
            request: models.ModifyWorkloadGroupStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkloadGroupStatusResponse:
        """
        This API is used to enable or disable resource groups.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkloadGroupStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkloadGroupStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenCoolDown(
            self,
            request: models.OpenCoolDownRequest,
            opts: Dict = None,
    ) -> models.OpenCoolDownResponse:
        """
        This API is used to enable hot/cold data layering.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenCoolDown"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenCoolDownResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenCoolDownPolicy(
            self,
            request: models.OpenCoolDownPolicyRequest,
            opts: Dict = None,
    ) -> models.OpenCoolDownPolicyResponse:
        """
        This API is used to enable and describe the cold storage policy.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenCoolDownPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenCoolDownPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryTableData(
            self,
            request: models.QueryTableDataRequest,
            opts: Dict = None,
    ) -> models.QueryTableDataResponse:
        """
        This API is used to query data according to the specified database and table names, and support field selection and pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryTableData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryTableDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverBackUpJob(
            self,
            request: models.RecoverBackUpJobRequest,
            opts: Dict = None,
    ) -> models.RecoverBackUpJobResponse:
        """
        This API is used to back up and recover.
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverBackUpJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverBackUpJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReduceInstance(
            self,
            request: models.ReduceInstanceRequest,
            opts: Dict = None,
    ) -> models.ReduceInstanceResponse:
        """
        This API is used to scale in clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "ReduceInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReduceInstanceResponse
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
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartClusterForConfigs(
            self,
            request: models.RestartClusterForConfigsRequest,
            opts: Dict = None,
    ) -> models.RestartClusterForConfigsResponse:
        """
        This API is used to restart the cluster to make the configuration file take effect.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartClusterForConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartClusterForConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartClusterForNode(
            self,
            request: models.RestartClusterForNodeRequest,
            opts: Dict = None,
    ) -> models.RestartClusterForNodeResponse:
        """
        This API is used to indicate the rolling restart of the clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartClusterForNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartClusterForNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutInstance(
            self,
            request: models.ScaleOutInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleOutInstanceResponse:
        """
        This API is used to horizontally scale out nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleUpInstance(
            self,
            request: models.ScaleUpInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleUpInstanceResponse:
        """
        This API is used to scale up/down computing resources.
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleUpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleUpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCoolDown(
            self,
            request: models.UpdateCoolDownRequest,
            opts: Dict = None,
    ) -> models.UpdateCoolDownResponse:
        """
        This API is used to update the hot/cold data layering information on a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCoolDown"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCoolDownResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDatabase(
            self,
            request: models.UpdateDatabaseRequest,
            opts: Dict = None,
    ) -> models.UpdateDatabaseResponse:
        """
        This API is used to modify the attributes of a specified database, including setting the data volume quota, renaming the database, setting the replica quantity quota, and modifying other attributes of the database.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTableSchema(
            self,
            request: models.UpdateTableSchemaRequest,
            opts: Dict = None,
    ) -> models.UpdateTableSchemaResponse:
        """
        This API is used to modify the attributes of a specified table. The API parameters are consistent with those for creating a table.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTableSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTableSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)