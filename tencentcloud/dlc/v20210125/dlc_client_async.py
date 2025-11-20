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
from tencentcloud.dlc.v20210125 import models
from typing import Dict


class DlcClient(AbstractClient):
    _apiVersion = '2021-01-25'
    _endpoint = 'dlc.intl.tencentcloudapi.com'
    _service = 'dlc'

    async def AddUsersToWorkGroup(
            self,
            request: models.AddUsersToWorkGroupRequest,
            opts: Dict = None,
    ) -> models.AddUsersToWorkGroupResponse:
        """
        This API is used to add users to working groups.
        """
        
        kwargs = {}
        kwargs["action"] = "AddUsersToWorkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUsersToWorkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AlterDMSDatabase(
            self,
            request: models.AlterDMSDatabaseRequest,
            opts: Dict = None,
    ) -> models.AlterDMSDatabaseResponse:
        """
        This API is used to update databases in the DMS metadata module.
        """
        
        kwargs = {}
        kwargs["action"] = "AlterDMSDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AlterDMSDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachDataMaskPolicy(
            self,
            request: models.AttachDataMaskPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachDataMaskPolicyResponse:
        """
        This API is used to bind a DMask policy.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachDataMaskPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachDataMaskPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachUserPolicy(
            self,
            request: models.AttachUserPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachUserPolicyResponse:
        """
        This API is used to bind the authentication policy to the user.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachUserPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachUserPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachWorkGroupPolicy(
            self,
            request: models.AttachWorkGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachWorkGroupPolicyResponse:
        """
        This API is used to bind an authentication policy to a working group.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachWorkGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachWorkGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindWorkGroupsToUser(
            self,
            request: models.BindWorkGroupsToUserRequest,
            opts: Dict = None,
    ) -> models.BindWorkGroupsToUserResponse:
        """
        This API is used to bind working groups to users.
        """
        
        kwargs = {}
        kwargs["action"] = "BindWorkGroupsToUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindWorkGroupsToUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelSparkSessionBatchSQL(
            self,
            request: models.CancelSparkSessionBatchSQLRequest,
            opts: Dict = None,
    ) -> models.CancelSparkSessionBatchSQLResponse:
        """
        This API is used to cancel a Spark SQL batch task.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelSparkSessionBatchSQL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelSparkSessionBatchSQLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelTask(
            self,
            request: models.CancelTaskRequest,
            opts: Dict = None,
    ) -> models.CancelTaskResponse:
        """
        This API is used to cancel a task.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckDataEngineConfigPairsValidity(
            self,
            request: models.CheckDataEngineConfigPairsValidityRequest,
            opts: Dict = None,
    ) -> models.CheckDataEngineConfigPairsValidityResponse:
        """
        This API is used to check the validity of the engine's user-defined parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckDataEngineConfigPairsValidity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckDataEngineConfigPairsValidityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckDataEngineImageCanBeRollback(
            self,
            request: models.CheckDataEngineImageCanBeRollbackRequest,
            opts: Dict = None,
    ) -> models.CheckDataEngineImageCanBeRollbackResponse:
        """
        This API is used to check whether the cluster can be rolled back.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckDataEngineImageCanBeRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckDataEngineImageCanBeRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckDataEngineImageCanBeUpgrade(
            self,
            request: models.CheckDataEngineImageCanBeUpgradeRequest,
            opts: Dict = None,
    ) -> models.CheckDataEngineImageCanBeUpgradeResponse:
        """
        This API is used to check whether the cluster image can be upgraded.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckDataEngineImageCanBeUpgrade"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckDataEngineImageCanBeUpgradeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckGrantedPermission(
            self,
            request: models.CheckGrantedPermissionRequest,
            opts: Dict = None,
    ) -> models.CheckGrantedPermissionResponse:
        """
        This API is used to check the permission status.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckGrantedPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckGrantedPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyDLCTable(
            self,
            request: models.CopyDLCTableRequest,
            opts: Dict = None,
    ) -> models.CopyDLCTableResponse:
        """
        This API is used to copy a table.
        """
        
        kwargs = {}
        kwargs["action"] = "CopyDLCTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyDLCTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCHDFSBindingProduct(
            self,
            request: models.CreateCHDFSBindingProductRequest,
            opts: Dict = None,
    ) -> models.CreateCHDFSBindingProductResponse:
        """
        This API is used to create metadata acceleration buckets and the binding relationship between products.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCHDFSBindingProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCHDFSBindingProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDLCTable(
            self,
            request: models.CreateDLCTableRequest,
            opts: Dict = None,
    ) -> models.CreateDLCTableResponse:
        """
        This API is used to create a table.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDLCTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDLCTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDMSDatabase(
            self,
            request: models.CreateDMSDatabaseRequest,
            opts: Dict = None,
    ) -> models.CreateDMSDatabaseResponse:
        """
        This API is used to create databases in the DMS metadata module.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDMSDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDMSDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataEngine(
            self,
            request: models.CreateDataEngineRequest,
            opts: Dict = None,
    ) -> models.CreateDataEngineResponse:
        """
        This API is used to create a data engine.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataMaskStrategy(
            self,
            request: models.CreateDataMaskStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateDataMaskStrategyResponse:
        """
        This API is used to create a DMask policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataMaskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataMaskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInternalTable(
            self,
            request: models.CreateInternalTableRequest,
            opts: Dict = None,
    ) -> models.CreateInternalTableResponse:
        """
        This API is used to create a managed internal table. It has been disused.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInternalTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInternalTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResultDownload(
            self,
            request: models.CreateResultDownloadRequest,
            opts: Dict = None,
    ) -> models.CreateResultDownloadResponse:
        """
        This API is used to create a query result download task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResultDownload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResultDownloadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSparkApp(
            self,
            request: models.CreateSparkAppRequest,
            opts: Dict = None,
    ) -> models.CreateSparkAppResponse:
        """
        This API is used to create a Spark job.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSparkApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSparkAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSparkAppTask(
            self,
            request: models.CreateSparkAppTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSparkAppTaskResponse:
        """
        This API is used to start a Spark job.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSparkAppTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSparkAppTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSparkSessionBatchSQL(
            self,
            request: models.CreateSparkSessionBatchSQLRequest,
            opts: Dict = None,
    ) -> models.CreateSparkSessionBatchSQLResponse:
        """
        This API is used to submit a Spark SQL batch task to the job engine.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSparkSessionBatchSQL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSparkSessionBatchSQLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStoreLocation(
            self,
            request: models.CreateStoreLocationRequest,
            opts: Dict = None,
    ) -> models.CreateStoreLocationResponse:
        """
        This API is used to add or overwrite the storage location of results.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStoreLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStoreLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTask(
            self,
            request: models.CreateTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTaskResponse:
        """
        This API is used to create and execute a SQL task. (`CreateTasks` is recommended.)
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTasks(
            self,
            request: models.CreateTasksRequest,
            opts: Dict = None,
    ) -> models.CreateTasksResponse:
        """
        This API is used to create and execute SQL tasks in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        This API is used to create users.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkGroup(
            self,
            request: models.CreateWorkGroupRequest,
            opts: Dict = None,
    ) -> models.CreateWorkGroupResponse:
        """
        This API is used to create working groups.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCHDFSBindingProduct(
            self,
            request: models.DeleteCHDFSBindingProductRequest,
            opts: Dict = None,
    ) -> models.DeleteCHDFSBindingProductResponse:
        """
        This API is used to delete the binding relationship between metadata acceleration buckets and products.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCHDFSBindingProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCHDFSBindingProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataEngine(
            self,
            request: models.DeleteDataEngineRequest,
            opts: Dict = None,
    ) -> models.DeleteDataEngineResponse:
        """
        This API is used to delete the data engine.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataMaskStrategy(
            self,
            request: models.DeleteDataMaskStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteDataMaskStrategyResponse:
        """
        This API is used to delete a data masking policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataMaskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataMaskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSparkApp(
            self,
            request: models.DeleteSparkAppRequest,
            opts: Dict = None,
    ) -> models.DeleteSparkAppResponse:
        """
        This API is used to delete a Spark job.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSparkApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSparkAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteThirdPartyAccessUser(
            self,
            request: models.DeleteThirdPartyAccessUserRequest,
            opts: Dict = None,
    ) -> models.DeleteThirdPartyAccessUserResponse:
        """
        This API is used to remove visits through the third-party platform.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteThirdPartyAccessUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteThirdPartyAccessUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        This API is used to delete users.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsersFromWorkGroup(
            self,
            request: models.DeleteUsersFromWorkGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteUsersFromWorkGroupResponse:
        """
        This API is used to delete users from working groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsersFromWorkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsersFromWorkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkGroup(
            self,
            request: models.DeleteWorkGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkGroupResponse:
        """
        This API is used to delete working groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAdvancedStoreLocation(
            self,
            request: models.DescribeAdvancedStoreLocationRequest,
            opts: Dict = None,
    ) -> models.DescribeAdvancedStoreLocationResponse:
        """
        This API is used to query the advanced settings of the SQL query interface.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAdvancedStoreLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAdvancedStoreLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDLCCatalogAccess(
            self,
            request: models.DescribeDLCCatalogAccessRequest,
            opts: Dict = None,
    ) -> models.DescribeDLCCatalogAccessResponse:
        """
        This API is used to query the DLC Catalog authorization list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDLCCatalogAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDLCCatalogAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDLCTable(
            self,
            request: models.DescribeDLCTableRequest,
            opts: Dict = None,
    ) -> models.DescribeDLCTableResponse:
        """
        This API is used to obtain the table.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDLCTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDLCTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDLCTableList(
            self,
            request: models.DescribeDLCTableListRequest,
            opts: Dict = None,
    ) -> models.DescribeDLCTableListResponse:
        """
        This API is used to obtain the list of tables.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDLCTableList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDLCTableListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDMSDatabase(
            self,
            request: models.DescribeDMSDatabaseRequest,
            opts: Dict = None,
    ) -> models.DescribeDMSDatabaseResponse:
        """
        This API is used to obtain databases in the DMS metadata module.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDMSDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDMSDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDMSDatabaseList(
            self,
            request: models.DescribeDMSDatabaseListRequest,
            opts: Dict = None,
    ) -> models.DescribeDMSDatabaseListResponse:
        """
        This API is used to obtain the list of databases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDMSDatabaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDMSDatabaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEngine(
            self,
            request: models.DescribeDataEngineRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEngineResponse:
        """
        This API is used to obtain detailed data engine information based on names.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEngineImageVersions(
            self,
            request: models.DescribeDataEngineImageVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEngineImageVersionsResponse:
        """
        This API is used to obtain the major version image list of exclusive clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEngineImageVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEngineImageVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEnginePythonSparkImages(
            self,
            request: models.DescribeDataEnginePythonSparkImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEnginePythonSparkImagesResponse:
        """
        This API is used to obtain the PYSPARK image list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEnginePythonSparkImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEnginePythonSparkImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEnginesScaleDetail(
            self,
            request: models.DescribeDataEnginesScaleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEnginesScaleDetailResponse:
        """
        This API is used to query engine specification details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEnginesScaleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEnginesScaleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataMaskStrategies(
            self,
            request: models.DescribeDataMaskStrategiesRequest,
            opts: Dict = None,
    ) -> models.DescribeDataMaskStrategiesResponse:
        """
        This API is used to query the DMask list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataMaskStrategies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataMaskStrategiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEngineUsageInfo(
            self,
            request: models.DescribeEngineUsageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEngineUsageInfoResponse:
        """
        This API is used to query the resource usage of a data engine based on its ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEngineUsageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEngineUsageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeForbiddenTablePro(
            self,
            request: models.DescribeForbiddenTableProRequest,
            opts: Dict = None,
    ) -> models.DescribeForbiddenTableProResponse:
        """
        This API is used to get the list of disabled table attributes (new).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeForbiddenTablePro"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeForbiddenTableProResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJob(
            self,
            request: models.DescribeJobRequest,
            opts: Dict = None,
    ) -> models.DescribeJobResponse:
        """
        This API is used to obtain the job information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobs(
            self,
            request: models.DescribeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobsResponse:
        """
        This API is used to obtain the list of job information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLakeFsDirSummary(
            self,
            request: models.DescribeLakeFsDirSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeLakeFsDirSummaryResponse:
        """
        This API is used to query the summary of a specified directory in a managed storage.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLakeFsDirSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLakeFsDirSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLakeFsInfo(
            self,
            request: models.DescribeLakeFsInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLakeFsInfoResponse:
        """
        This API is used to query managed storage information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLakeFsInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLakeFsInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOtherCHDFSBindingList(
            self,
            request: models.DescribeOtherCHDFSBindingListRequest,
            opts: Dict = None,
    ) -> models.DescribeOtherCHDFSBindingListResponse:
        """
        This API is used to query the list of metadata acceleration buckets bound to other products.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOtherCHDFSBindingList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOtherCHDFSBindingListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuery(
            self,
            request: models.DescribeQueryRequest,
            opts: Dict = None,
    ) -> models.DescribeQueryResponse:
        """
        This API is used to obtain the query results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResultDownload(
            self,
            request: models.DescribeResultDownloadRequest,
            opts: Dict = None,
    ) -> models.DescribeResultDownloadResponse:
        """
        This API is used to get a query result download task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResultDownload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResultDownloadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionImageVersion(
            self,
            request: models.DescribeSessionImageVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionImageVersionResponse:
        """
        This API is used to retrieve all built-in images of all minor versions under a specified major version.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionImageVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionImageVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkAppJob(
            self,
            request: models.DescribeSparkAppJobRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkAppJobResponse:
        """
        u200cThis API is used to query the information of a Spark job.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkAppJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkAppJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkAppJobs(
            self,
            request: models.DescribeSparkAppJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkAppJobsResponse:
        """
        This API is used to query the list of Spark jobs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkAppJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkAppJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkAppTasks(
            self,
            request: models.DescribeSparkAppTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkAppTasksResponse:
        """
        This API is used to query the list of running task instances of a Spark job.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkAppTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkAppTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkSessionBatchSqlLog(
            self,
            request: models.DescribeSparkSessionBatchSqlLogRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkSessionBatchSqlLogResponse:
        """
        This API is used to query Spark SQL batch task logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkSessionBatchSqlLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkSessionBatchSqlLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStoreLocation(
            self,
            request: models.DescribeStoreLocationRequest,
            opts: Dict = None,
    ) -> models.DescribeStoreLocationResponse:
        """
        This API is used to query the storage location of calculation results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStoreLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStoreLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubUserAccessPolicy(
            self,
            request: models.DescribeSubUserAccessPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeSubUserAccessPolicyResponse:
        """
        This API is used to query the sub-user's visiting policy for users accessing through the third-party platform.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubUserAccessPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubUserAccessPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTablesName(
            self,
            request: models.DescribeTablesNameRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesNameResponse:
        """
        This API is used to query the data table name list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTablesName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResult(
            self,
            request: models.DescribeTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResultResponse:
        """
        This API is used to query the result of a task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatistics(
            self,
            request: models.DescribeTaskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatisticsResponse:
        """
        This API is used to describe the information on task statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        This API is used to query the list of tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeThirdPartyAccessUser(
            self,
            request: models.DescribeThirdPartyAccessUserRequest,
            opts: Dict = None,
    ) -> models.DescribeThirdPartyAccessUserResponse:
        """
        This API is used to query the information of users visiting through the third-party platform.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeThirdPartyAccessUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeThirdPartyAccessUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpdatableDataEngines(
            self,
            request: models.DescribeUpdatableDataEnginesRequest,
            opts: Dict = None,
    ) -> models.DescribeUpdatableDataEnginesResponse:
        """
        This API is used to query the list of engines that are able to upgrade their configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpdatableDataEngines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpdatableDataEnginesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDataEngineConfig(
            self,
            request: models.DescribeUserDataEngineConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDataEngineConfigResponse:
        """
        This API is used to query user-defined engine parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDataEngineConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDataEngineConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserInfo(
            self,
            request: models.DescribeUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserInfoResponse:
        """
        This API is used to get detailed user information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserRoles(
            self,
            request: models.DescribeUserRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeUserRolesResponse:
        """
        This API is used to enumerate user roles.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserType(
            self,
            request: models.DescribeUserTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeUserTypeResponse:
        """
        This API is used to get the types of users.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsers(
            self,
            request: models.DescribeUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersResponse:
        """
        This API is used to obtain the user list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkGroupInfo(
            self,
            request: models.DescribeWorkGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkGroupInfoResponse:
        """
        This API is used to get detailed information about working groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkGroups(
            self,
            request: models.DescribeWorkGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkGroupsResponse:
        """
        This API is used to get a list of working groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachUserPolicy(
            self,
            request: models.DetachUserPolicyRequest,
            opts: Dict = None,
    ) -> models.DetachUserPolicyResponse:
        """
        This API is used to unbind the authentication policy from the user.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachUserPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachUserPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachWorkGroupPolicy(
            self,
            request: models.DetachWorkGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.DetachWorkGroupPolicyResponse:
        """
        This API is used to unbind the authentication policy from the working group.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachWorkGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachWorkGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DropDLCTable(
            self,
            request: models.DropDLCTableRequest,
            opts: Dict = None,
    ) -> models.DropDLCTableResponse:
        """
        This API is used to delete the table.
        """
        
        kwargs = {}
        kwargs["action"] = "DropDLCTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DropDLCTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DropDMSDatabase(
            self,
            request: models.DropDMSDatabaseRequest,
            opts: Dict = None,
    ) -> models.DropDMSDatabaseResponse:
        """
        This API is used to delete databases in the DMS metadata module.
        """
        
        kwargs = {}
        kwargs["action"] = "DropDMSDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DropDMSDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DropDMSTable(
            self,
            request: models.DropDMSTableRequest,
            opts: Dict = None,
    ) -> models.DropDMSTableResponse:
        """
        This API is used to delete tables in the DMS metadata module.
        """
        
        kwargs = {}
        kwargs["action"] = "DropDMSTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DropDMSTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateCreateMangedTableSql(
            self,
            request: models.GenerateCreateMangedTableSqlRequest,
            opts: Dict = None,
    ) -> models.GenerateCreateMangedTableSqlResponse:
        """
        This API is used to generate SQL statements for creating a managed table.
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateCreateMangedTableSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateCreateMangedTableSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOptimizerPolicy(
            self,
            request: models.GetOptimizerPolicyRequest,
            opts: Dict = None,
    ) -> models.GetOptimizerPolicyResponse:
        """
        GetOptimizerPolicy
        """
        
        kwargs = {}
        kwargs["action"] = "GetOptimizerPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOptimizerPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GrantDLCCatalogAccess(
            self,
            request: models.GrantDLCCatalogAccessRequest,
            opts: Dict = None,
    ) -> models.GrantDLCCatalogAccessResponse:
        """
        This API is used to grant permissions for visiting DLC Catalog.
        """
        
        kwargs = {}
        kwargs["action"] = "GrantDLCCatalogAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GrantDLCCatalogAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAdvancedStoreLocation(
            self,
            request: models.ModifyAdvancedStoreLocationRequest,
            opts: Dict = None,
    ) -> models.ModifyAdvancedStoreLocationResponse:
        """
        This API is used to modify the advanced settings of the SQL query interface.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAdvancedStoreLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAdvancedStoreLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDataEngineDescription(
            self,
            request: models.ModifyDataEngineDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyDataEngineDescriptionResponse:
        """
        This API is used to modify the engine's description.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDataEngineDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDataEngineDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGovernEventRule(
            self,
            request: models.ModifyGovernEventRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyGovernEventRuleResponse:
        """
        This API is used to change data governance event thresholds.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGovernEventRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGovernEventRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySparkApp(
            self,
            request: models.ModifySparkAppRequest,
            opts: Dict = None,
    ) -> models.ModifySparkAppResponse:
        """
        This API is used to update a Spark job.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySparkApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySparkAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySparkAppBatch(
            self,
            request: models.ModifySparkAppBatchRequest,
            opts: Dict = None,
    ) -> models.ModifySparkAppBatchResponse:
        """
        This API is used to modify Spark job parameters in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySparkAppBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySparkAppBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUser(
            self,
            request: models.ModifyUserRequest,
            opts: Dict = None,
    ) -> models.ModifyUserResponse:
        """
        This API is used to modify user information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserType(
            self,
            request: models.ModifyUserTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyUserTypeResponse:
        """
        This API is used to modify the types of users. Only users who are also administrators can call this API to conduct the operation.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkGroup(
            self,
            request: models.ModifyWorkGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkGroupResponse:
        """
        This API is used to modify working group information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryResult(
            self,
            request: models.QueryResultRequest,
            opts: Dict = None,
    ) -> models.QueryResultResponse:
        """
        This API is used to query the result of obtaining tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryTaskCostDetail(
            self,
            request: models.QueryTaskCostDetailRequest,
            opts: Dict = None,
    ) -> models.QueryTaskCostDetailResponse:
        """
        This API is used to query task consumption details.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryTaskCostDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryTaskCostDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterThirdPartyAccessUser(
            self,
            request: models.RegisterThirdPartyAccessUserRequest,
            opts: Dict = None,
    ) -> models.RegisterThirdPartyAccessUserResponse:
        """
        This API is used to enable visits to the third-party platform.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterThirdPartyAccessUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterThirdPartyAccessUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDataEngine(
            self,
            request: models.RenewDataEngineRequest,
            opts: Dict = None,
    ) -> models.RenewDataEngineResponse:
        """
        This API is used to renew the data engine.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartDataEngine(
            self,
            request: models.RestartDataEngineRequest,
            opts: Dict = None,
    ) -> models.RestartDataEngineResponse:
        """
        This API is used to restart engines.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokeDLCCatalogAccess(
            self,
            request: models.RevokeDLCCatalogAccessRequest,
            opts: Dict = None,
    ) -> models.RevokeDLCCatalogAccessResponse:
        """
        This API is used to revoke permissions for visiting DLC Catalog.
        """
        
        kwargs = {}
        kwargs["action"] = "RevokeDLCCatalogAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokeDLCCatalogAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackDataEngineImage(
            self,
            request: models.RollbackDataEngineImageRequest,
            opts: Dict = None,
    ) -> models.RollbackDataEngineImageResponse:
        """
        This API is used to roll back the versions of the engine image.
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackDataEngineImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackDataEngineImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SuspendResumeDataEngine(
            self,
            request: models.SuspendResumeDataEngineRequest,
            opts: Dict = None,
    ) -> models.SuspendResumeDataEngineResponse:
        """
        This API is used to suspend or start a data engine.
        """
        
        kwargs = {}
        kwargs["action"] = "SuspendResumeDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SuspendResumeDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDataEngine(
            self,
            request: models.SwitchDataEngineRequest,
            opts: Dict = None,
    ) -> models.SwitchDataEngineResponse:
        """
        This API is used to switch between the primary and standby clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDataEngineImage(
            self,
            request: models.SwitchDataEngineImageRequest,
            opts: Dict = None,
    ) -> models.SwitchDataEngineImageResponse:
        """
        This API is used to switch the versions of the engine image.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDataEngineImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDataEngineImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindWorkGroupsFromUser(
            self,
            request: models.UnbindWorkGroupsFromUserRequest,
            opts: Dict = None,
    ) -> models.UnbindWorkGroupsFromUserResponse:
        """
        This API is used to unbind a user group from a user.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindWorkGroupsFromUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindWorkGroupsFromUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataEngine(
            self,
            request: models.UpdateDataEngineRequest,
            opts: Dict = None,
    ) -> models.UpdateDataEngineResponse:
        """
        This API is used to upgrade data engine configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataEngineConfig(
            self,
            request: models.UpdateDataEngineConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateDataEngineConfigResponse:
        """
        This API is used to trigger the modification of the engine configuration by the user through a certain operation.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataEngineConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataEngineConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataMaskStrategy(
            self,
            request: models.UpdateDataMaskStrategyRequest,
            opts: Dict = None,
    ) -> models.UpdateDataMaskStrategyResponse:
        """
        This API is used to update the DMask policy.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataMaskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataMaskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRowFilter(
            self,
            request: models.UpdateRowFilterRequest,
            opts: Dict = None,
    ) -> models.UpdateRowFilterResponse:
        """
        This API is used to update row filters. Please note that it updates filters only but not catalogs, databases, or tables.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRowFilter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRowFilterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserDataEngineConfig(
            self,
            request: models.UpdateUserDataEngineConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateUserDataEngineConfigResponse:
        """
        This API is used to modify the custom configuration of the user's engine.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserDataEngineConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserDataEngineConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDataEngineImage(
            self,
            request: models.UpgradeDataEngineImageRequest,
            opts: Dict = None,
    ) -> models.UpgradeDataEngineImageResponse:
        """
        This API is used to upgrade the engine image.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDataEngineImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDataEngineImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)