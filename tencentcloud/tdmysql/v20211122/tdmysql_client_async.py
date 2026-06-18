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
from tencentcloud.tdmysql.v20211122 import models
from typing import Dict


class TdmysqlClient(AbstractClient):
    _apiVersion = '2021-11-22'
    _endpoint = 'tdmysql.intl.tencentcloudapi.com'
    _service = 'tdmysql'

    async def CancelIsolateDBInstances(
            self,
            request: models.CancelIsolateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CancelIsolateDBInstancesResponse:
        """
        This API is used to lift isolation for instances in batch.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelIsolateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelIsolateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloneInstance(
            self,
            request: models.CreateCloneInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateCloneInstanceResponse:
        """
        This API is used to create clone instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloneInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloneInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstances(
            self,
            request: models.CreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstancesResponse:
        """
        This API is used to batch create instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBSBackup(
            self,
            request: models.CreateDBSBackupRequest,
            opts: Dict = None,
    ) -> models.CreateDBSBackupResponse:
        """
        This API is used to create a manual backup of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBSBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBSBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUsers(
            self,
            request: models.CreateUsersRequest,
            opts: Dict = None,
    ) -> models.CreateUsersResponse:
        """
        This API is used to create users in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDBSBackupSets(
            self,
            request: models.DeleteDBSBackupSetsRequest,
            opts: Dict = None,
    ) -> models.DeleteDBSBackupSetsResponse:
        """
        This API is used to delete manual backups of instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDBSBackupSets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBSBackupSetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsers(
            self,
            request: models.DeleteUsersRequest,
            opts: Dict = None,
    ) -> models.DeleteUsersResponse:
        """
        This API is used to batch delete users.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceDetail(
            self,
            request: models.DescribeDBInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceDetailResponse:
        """
        This API is used to query instance details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        This API is used to query instance list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBParameters(
            self,
            request: models.DescribeDBParametersRequest,
            opts: Dict = None,
    ) -> models.DescribeDBParametersResponse:
        """
        This API is used to obtain the current parameter settings of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSArchiveLogs(
            self,
            request: models.DescribeDBSArchiveLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSArchiveLogsResponse:
        """
        This API is used to query instance archived WAL log list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSArchiveLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSArchiveLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSAvailableRecoveryTime(
            self,
            request: models.DescribeDBSAvailableRecoveryTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSAvailableRecoveryTimeResponse:
        """
        This API is used to obtain the recoverable time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSAvailableRecoveryTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSAvailableRecoveryTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSBackupPolicy(
            self,
            request: models.DescribeDBSBackupPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSBackupPolicyResponse:
        """
        Query an instance backup strategy
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSBackupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSBackupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSBackupSets(
            self,
            request: models.DescribeDBSBackupSetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSBackupSetsResponse:
        """
        This API is used to query instance backup set information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSBackupSets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSBackupSetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSBackupStatistics(
            self,
            request: models.DescribeDBSBackupStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSBackupStatisticsResponse:
        """
        This API is used to query instance backup space overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSBackupStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSBackupStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSBackupStatisticsDetail(
            self,
            request: models.DescribeDBSBackupStatisticsDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSBackupStatisticsDetailResponse:
        """
        This API is used to query backup set statistical detail.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSBackupStatisticsDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSBackupStatisticsDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSCloneInstances(
            self,
            request: models.DescribeDBSCloneInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSCloneInstancesResponse:
        """
        Query clone list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSCloneInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSCloneInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        This API is used to query instance security group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseObjects(
            self,
            request: models.DescribeDatabaseObjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseObjectsResponse:
        """
        This API is used to query the object list in the database of a cloud database instance, including table, stored procedure, view and function.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        This API is used to query the database list of a cloud database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlow(
            self,
            request: models.DescribeFlowRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowResponse:
        """
        This API is used to query the process status of an asynchronous task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSSLStatus(
            self,
            request: models.DescribeInstanceSSLStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSSLStatusResponse:
        """
        This API is used to query the SSL status of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSSLStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSSLStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaintenanceWindow(
            self,
            request: models.DescribeMaintenanceWindowRequest,
            opts: Dict = None,
    ) -> models.DescribeMaintenanceWindowResponse:
        """
        Query maintenance time window configurations
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaintenanceWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaintenanceWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSaleInfo(
            self,
            request: models.DescribeSaleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSaleInfoResponse:
        """
        This API is used to query available regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSaleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSaleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogs(
            self,
            request: models.DescribeSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogsResponse:
        """
        This API is used to query slow logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpecs(
            self,
            request: models.DescribeSpecsRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecsResponse:
        """
        This API is used to list available component specifications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserPrivileges(
            self,
            request: models.DescribeUserPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeUserPrivilegesResponse:
        """
        This API is used to query user permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsers(
            self,
            request: models.DescribeUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersResponse:
        """
        This API is used to query user list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyInstances(
            self,
            request: models.DestroyInstancesRequest,
            opts: Dict = None,
    ) -> models.DestroyInstancesResponse:
        """
        This API is used to destroy instances in batch.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExpandInstance(
            self,
            request: models.ExpandInstanceRequest,
            opts: Dict = None,
    ) -> models.ExpandInstanceResponse:
        """
        This API is used to horizontally scale out instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ExpandInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExpandInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBInstance(
            self,
            request: models.IsolateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDBInstanceResponse:
        """
        This API is used to batch isolate instances.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoRenewFlag(
            self,
            request: models.ModifyAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoRenewFlagResponse:
        """
        This API is used to modify the auto-renewal flag.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        This API is used to modify cloud database security groups.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceVPort(
            self,
            request: models.ModifyDBInstanceVPortRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceVPortResponse:
        """
        This API is used to modify the VPC port of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceVPort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceVPortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBParameters(
            self,
            request: models.ModifyDBParametersRequest,
            opts: Dict = None,
    ) -> models.ModifyDBParametersResponse:
        """
        This API is used to modify instance parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBSBackupPolicy(
            self,
            request: models.ModifyDBSBackupPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyDBSBackupPolicyResponse:
        """
        This API is used to modify the instance backup strategy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBSBackupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBSBackupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBSBackupSetComment(
            self,
            request: models.ModifyDBSBackupSetCommentRequest,
            opts: Dict = None,
    ) -> models.ModifyDBSBackupSetCommentResponse:
        """
        This API is used to modify backup notes of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBSBackupSetComment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBSBackupSetCommentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceName(
            self,
            request: models.ModifyInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNameResponse:
        """
        This API is used to modify instance name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceNetwork(
            self,
            request: models.ModifyInstanceNetworkRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNetworkResponse:
        """
        This API is used to modify the network to which the instance belongs.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceSSLStatus(
            self,
            request: models.ModifyInstanceSSLStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceSSLStatusResponse:
        """
        This API is used to enable or disable the SSL feature of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceSSLStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceSSLStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaintenanceWindow(
            self,
            request: models.ModifyMaintenanceWindowRequest,
            opts: Dict = None,
    ) -> models.ModifyMaintenanceWindowResponse:
        """
        Add new or modify instance maintenance time window configurations
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaintenanceWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaintenanceWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserPrivileges(
            self,
            request: models.ModifyUserPrivilegesRequest,
            opts: Dict = None,
    ) -> models.ModifyUserPrivilegesResponse:
        """
        This API is used to modify user permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetUserPassword(
            self,
            request: models.ResetUserPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetUserPasswordResponse:
        """
        This API is used to reset user password.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetUserPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetUserPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartDBInstances(
            self,
            request: models.RestartDBInstancesRequest,
            opts: Dict = None,
    ) -> models.RestartDBInstancesResponse:
        """
        This API is used to restart database instances.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        This API is used to scale up a TDSQL Boundless instance, which can be a primary instance or a disaster recovery instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)