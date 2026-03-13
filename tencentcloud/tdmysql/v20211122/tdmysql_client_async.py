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
        
    async def CreateDBSBackup(
            self,
            request: models.CreateDBSBackupRequest,
            opts: Dict = None,
    ) -> models.CreateDBSBackupResponse:
        """
        Create an instance backup set.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBSBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBSBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDBSBackupSets(
            self,
            request: models.DeleteDBSBackupSetsRequest,
            opts: Dict = None,
    ) -> models.DeleteDBSBackupSetsResponse:
        """
        Delete instance backup sets.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDBSBackupSets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBSBackupSetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingEnable(
            self,
            request: models.DescribeBillingEnableRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingEnableResponse:
        """
        No place to call.

        This API is used to query whether billing is enabled.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingEnable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingEnableResponse
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
        
    async def DescribeDBSAvailableRecoveryTime(
            self,
            request: models.DescribeDBSAvailableRecoveryTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSAvailableRecoveryTimeResponse:
        """
        Query recoverable time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSAvailableRecoveryTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSAvailableRecoveryTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSCloneInstances(
            self,
            request: models.DescribeDBSCloneInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSCloneInstancesResponse:
        """
        Query clone list of instances.
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
        
    async def DescribeDatabaseTable(
            self,
            request: models.DescribeDatabaseTableRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseTableResponse:
        """
        Redundant API, no API calls.

        This API is used to query table information of a cloud database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseTableResponse
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
        
    async def ModifyBinlogStatus(
            self,
            request: models.ModifyBinlogStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBinlogStatusResponse:
        """
        This API is used to entirely overwrite the API feature of ModifyInstanceCdc.

        Modify the binlog status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBinlogStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBinlogStatusResponse
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
        Modify the instance backup strategy.
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
        Modify the backup set remark.
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