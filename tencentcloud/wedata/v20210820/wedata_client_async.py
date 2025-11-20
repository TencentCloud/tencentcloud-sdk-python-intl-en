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
from tencentcloud.wedata.v20210820 import models
from typing import Dict


class WedataClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'wedata.intl.tencentcloudapi.com'
    _service = 'wedata'

    async def AddProjectUserRole(
            self,
            request: models.AddProjectUserRoleRequest,
            opts: Dict = None,
    ) -> models.AddProjectUserRoleResponse:
        """
        This API is used to add a user role to a project.
        """
        
        kwargs = {}
        kwargs["action"] = "AddProjectUserRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddProjectUserRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateIntegrationTaskAlarms(
            self,
            request: models.BatchCreateIntegrationTaskAlarmsRequest,
            opts: Dict = None,
    ) -> models.BatchCreateIntegrationTaskAlarmsResponse:
        """
        Bulk Create Task Alert Rules
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateIntegrationTaskAlarms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateIntegrationTaskAlarmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateTaskVersionAsync(
            self,
            request: models.BatchCreateTaskVersionAsyncRequest,
            opts: Dict = None,
    ) -> models.BatchCreateTaskVersionAsyncResponse:
        """
        This API is used to asynchronously create task versions in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateTaskVersionAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateTaskVersionAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteIntegrationTasks(
            self,
            request: models.BatchDeleteIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteIntegrationTasksResponse:
        """
        Batch Delete Integration Tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteOpsTasks(
            self,
            request: models.BatchDeleteOpsTasksRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteOpsTasksResponse:
        """
        Task Operation and Maintenance - Batch Delete Tasks
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchForceSuccessIntegrationTaskInstances(
            self,
            request: models.BatchForceSuccessIntegrationTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.BatchForceSuccessIntegrationTaskInstancesResponse:
        """
        Batch set successful integration task instances
        """
        
        kwargs = {}
        kwargs["action"] = "BatchForceSuccessIntegrationTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchForceSuccessIntegrationTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchKillIntegrationTaskInstances(
            self,
            request: models.BatchKillIntegrationTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.BatchKillIntegrationTaskInstancesResponse:
        """
        Batch Terminate Integration Task Instances
        """
        
        kwargs = {}
        kwargs["action"] = "BatchKillIntegrationTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchKillIntegrationTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchMakeUpIntegrationTasks(
            self,
            request: models.BatchMakeUpIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchMakeUpIntegrationTasksResponse:
        """
        Perform Batch Data Supplement Operation on Integrated Offline Tasks
        """
        
        kwargs = {}
        kwargs["action"] = "BatchMakeUpIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchMakeUpIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyOpsOwners(
            self,
            request: models.BatchModifyOpsOwnersRequest,
            opts: Dict = None,
    ) -> models.BatchModifyOpsOwnersResponse:
        """
        Batch Modify Task Assignee
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyOpsOwners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyOpsOwnersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchRerunIntegrationTaskInstances(
            self,
            request: models.BatchRerunIntegrationTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.BatchRerunIntegrationTaskInstancesResponse:
        """
        Batch Rerun Integration Task Instances
        """
        
        kwargs = {}
        kwargs["action"] = "BatchRerunIntegrationTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchRerunIntegrationTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchResumeIntegrationTasks(
            self,
            request: models.BatchResumeIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchResumeIntegrationTasksResponse:
        """
        Batch Continue Execution of Integrated Real-time Tasks
        """
        
        kwargs = {}
        kwargs["action"] = "BatchResumeIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchResumeIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchRunOpsTask(
            self,
            request: models.BatchRunOpsTaskRequest,
            opts: Dict = None,
    ) -> models.BatchRunOpsTaskResponse:
        """
        Task Operation and Maintenance - Task List Batch Startup
        """
        
        kwargs = {}
        kwargs["action"] = "BatchRunOpsTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchRunOpsTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchStartIntegrationTasks(
            self,
            request: models.BatchStartIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchStartIntegrationTasksResponse:
        """
        Batch Run Integration Tasks
        """
        
        kwargs = {}
        kwargs["action"] = "BatchStartIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchStartIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchStopIntegrationTasks(
            self,
            request: models.BatchStopIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchStopIntegrationTasksResponse:
        """
        Batch Stop Integration Tasks
        """
        
        kwargs = {}
        kwargs["action"] = "BatchStopIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchStopIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchStopOpsTasks(
            self,
            request: models.BatchStopOpsTasksRequest,
            opts: Dict = None,
    ) -> models.BatchStopOpsTasksResponse:
        """
        Only valid for tasks in "Scheduling In Progress" and "Paused" statuses, terminate the task instances of the selected tasks, and stop scheduling
        """
        
        kwargs = {}
        kwargs["action"] = "BatchStopOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchStopOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchStopWorkflowsByIds(
            self,
            request: models.BatchStopWorkflowsByIdsRequest,
            opts: Dict = None,
    ) -> models.BatchStopWorkflowsByIdsResponse:
        """
        Batch Stop Workflow
        """
        
        kwargs = {}
        kwargs["action"] = "BatchStopWorkflowsByIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchStopWorkflowsByIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchSuspendIntegrationTasks(
            self,
            request: models.BatchSuspendIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchSuspendIntegrationTasksResponse:
        """
        Batch pause integration tasks
        """
        
        kwargs = {}
        kwargs["action"] = "BatchSuspendIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchSuspendIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchUpdateIntegrationTasks(
            self,
            request: models.BatchUpdateIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchUpdateIntegrationTasksResponse:
        """
        Bulk Update Integration Tasks (Currently only supports bulk updating of the person in charge)
        """
        
        kwargs = {}
        kwargs["action"] = "BatchUpdateIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchUpdateIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckAlarmRegularNameExist(
            self,
            request: models.CheckAlarmRegularNameExistRequest,
            opts: Dict = None,
    ) -> models.CheckAlarmRegularNameExistResponse:
        """
        Check for Duplicate Alert Rule Names
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAlarmRegularNameExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAlarmRegularNameExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIntegrationNodeNameExists(
            self,
            request: models.CheckIntegrationNodeNameExistsRequest,
            opts: Dict = None,
    ) -> models.CheckIntegrationNodeNameExistsResponse:
        """
        Determining if the name of the integrated node exists
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIntegrationNodeNameExists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIntegrationNodeNameExistsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIntegrationTaskNameExists(
            self,
            request: models.CheckIntegrationTaskNameExistsRequest,
            opts: Dict = None,
    ) -> models.CheckIntegrationTaskNameExistsResponse:
        """
        Check if Integration Task Name Exists
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIntegrationTaskNameExists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIntegrationTaskNameExistsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckTaskNameExist(
            self,
            request: models.CheckTaskNameExistRequest,
            opts: Dict = None,
    ) -> models.CheckTaskNameExistResponse:
        """
        Offline Task Renaming Verification
        """
        
        kwargs = {}
        kwargs["action"] = "CheckTaskNameExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckTaskNameExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitIntegrationTask(
            self,
            request: models.CommitIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.CommitIntegrationTaskResponse:
        """
        Submit integration task
        """
        
        kwargs = {}
        kwargs["action"] = "CommitIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommitIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitRuleGroupTask(
            self,
            request: models.CommitRuleGroupTaskRequest,
            opts: Dict = None,
    ) -> models.CommitRuleGroupTaskResponse:
        """
        Submit Rule Group to Run Task Interface
        """
        
        kwargs = {}
        kwargs["action"] = "CommitRuleGroupTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommitRuleGroupTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CountOpsInstanceState(
            self,
            request: models.CountOpsInstanceStateRequest,
            opts: Dict = None,
    ) -> models.CountOpsInstanceStateResponse:
        """
        Statistics on task instance status
        """
        
        kwargs = {}
        kwargs["action"] = "CountOpsInstanceState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CountOpsInstanceStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomFunction(
            self,
            request: models.CreateCustomFunctionRequest,
            opts: Dict = None,
    ) -> models.CreateCustomFunctionResponse:
        """
        Create User-Defined Function
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataSource(
            self,
            request: models.CreateDataSourceRequest,
            opts: Dict = None,
    ) -> models.CreateDataSourceResponse:
        """
        Create Data Source
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDsFolder(
            self,
            request: models.CreateDsFolderRequest,
            opts: Dict = None,
    ) -> models.CreateDsFolderResponse:
        """
        Orchestration Space - Create Folder
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDsFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDsFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHiveTable(
            self,
            request: models.CreateHiveTableRequest,
            opts: Dict = None,
    ) -> models.CreateHiveTableResponse:
        """
        Create Hive Table
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHiveTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHiveTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHiveTableByDDL(
            self,
            request: models.CreateHiveTableByDDLRequest,
            opts: Dict = None,
    ) -> models.CreateHiveTableByDDLResponse:
        """
        Create Hive table and return table name
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHiveTableByDDL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHiveTableByDDLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIntegrationNode(
            self,
            request: models.CreateIntegrationNodeRequest,
            opts: Dict = None,
    ) -> models.CreateIntegrationNodeResponse:
        """
        Create Integration Node
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIntegrationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIntegrationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIntegrationTask(
            self,
            request: models.CreateIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateIntegrationTaskResponse:
        """
        Create Integration Task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOfflineTask(
            self,
            request: models.CreateOfflineTaskRequest,
            opts: Dict = None,
    ) -> models.CreateOfflineTaskResponse:
        """
        Create Offline Task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOfflineTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOfflineTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpsMakePlan(
            self,
            request: models.CreateOpsMakePlanRequest,
            opts: Dict = None,
    ) -> models.CreateOpsMakePlanResponse:
        """
        Bulk Data Supplement (Create Supplementary Entry Task)
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpsMakePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpsMakePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        Create quality rule interface
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRuleTemplate(
            self,
            request: models.CreateRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateRuleTemplateResponse:
        """
        Create Rule Template
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTask(
            self,
            request: models.CreateTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTaskResponse:
        """
        This API is used to create a task. This API is deprecated. Use the CreateTaskNew API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskAlarmRegular(
            self,
            request: models.CreateTaskAlarmRegularRequest,
            opts: Dict = None,
    ) -> models.CreateTaskAlarmRegularResponse:
        """
        Create task alert rules
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskAlarmRegular"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskAlarmRegularResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskFolder(
            self,
            request: models.CreateTaskFolderRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFolderResponse:
        """
        Orchestration Space - Workflow - Create Task Folder
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskNew(
            self,
            request: models.CreateTaskNewRequest,
            opts: Dict = None,
    ) -> models.CreateTaskNewResponse:
        """
        This API is used to aggregate task creation.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskVersionDs(
            self,
            request: models.CreateTaskVersionDsRequest,
            opts: Dict = None,
    ) -> models.CreateTaskVersionDsResponse:
        """
        Submit Task Version
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskVersionDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskVersionDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflowDs(
            self,
            request: models.CreateWorkflowDsRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowDsResponse:
        """
        Creating workflow
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflowDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DagInstances(
            self,
            request: models.DagInstancesRequest,
            opts: Dict = None,
    ) -> models.DagInstancesResponse:
        """
        Pull DAG Instance
        """
        
        kwargs = {}
        kwargs["action"] = "DagInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DagInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomFunction(
            self,
            request: models.DeleteCustomFunctionRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomFunctionResponse:
        """
        Delete user-defined Definition functions
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataSources(
            self,
            request: models.DeleteDataSourcesRequest,
            opts: Dict = None,
    ) -> models.DeleteDataSourcesResponse:
        """
        Delete Data Source
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataSources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataSourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDsFolder(
            self,
            request: models.DeleteDsFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteDsFolderResponse:
        """
        Orchestration space - delete folders
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDsFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDsFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFile(
            self,
            request: models.DeleteFileRequest,
            opts: Dict = None,
    ) -> models.DeleteFileResponse:
        """
        Delete File
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFilePath(
            self,
            request: models.DeleteFilePathRequest,
            opts: Dict = None,
    ) -> models.DeleteFilePathResponse:
        """
        Development Space - Batch Delete Directories and Files
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFilePath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFilePathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIntegrationNode(
            self,
            request: models.DeleteIntegrationNodeRequest,
            opts: Dict = None,
    ) -> models.DeleteIntegrationNodeResponse:
        """
        Delete Integration Node
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIntegrationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIntegrationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIntegrationTask(
            self,
            request: models.DeleteIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteIntegrationTaskResponse:
        """
        Delete integration tasks
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOfflineTask(
            self,
            request: models.DeleteOfflineTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteOfflineTaskResponse:
        """
        Deleting task
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOfflineTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOfflineTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjectParamDs(
            self,
            request: models.DeleteProjectParamDsRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectParamDsResponse:
        """
        Delete Project Parameters
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjectParamDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectParamDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjectUsers(
            self,
            request: models.DeleteProjectUsersRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectUsersResponse:
        """
        Delete Project Users
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjectUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResource(
            self,
            request: models.DeleteResourceRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceResponse:
        """
        Remove resources in Resource Management
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceFile(
            self,
            request: models.DeleteResourceFileRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceFileResponse:
        """
        Resource Management - Delete Resource File
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceFiles(
            self,
            request: models.DeleteResourceFilesRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceFilesResponse:
        """
        Resource Management-Batch Delete Resource Files
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRule(
            self,
            request: models.DeleteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleResponse:
        """
        Delete Quality Rule Interface
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRuleTemplate(
            self,
            request: models.DeleteRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleTemplateResponse:
        """
        Deleting Rule Template
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTaskAlarmRegular(
            self,
            request: models.DeleteTaskAlarmRegularRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskAlarmRegularResponse:
        """
        Delete Task Alert Rule
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTaskAlarmRegular"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskAlarmRegularResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTaskDs(
            self,
            request: models.DeleteTaskDsRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskDsResponse:
        """
        Delete Orchestration Space Task
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTaskDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkflowById(
            self,
            request: models.DeleteWorkflowByIdRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowByIdResponse:
        """
        Delete Workflow by Workflow Id
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflowById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmEvents(
            self,
            request: models.DescribeAlarmEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmEventsResponse:
        """
        Alert event list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmReceiver(
            self,
            request: models.DescribeAlarmReceiverRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmReceiverResponse:
        """
        Alert Recipient Details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllByFolderNew(
            self,
            request: models.DescribeAllByFolderNewRequest,
            opts: Dict = None,
    ) -> models.DescribeAllByFolderNewResponse:
        """
        Query all subfolders + workflows under the parent directory
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllByFolderNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllByFolderNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApproveList(
            self,
            request: models.DescribeApproveListRequest,
            opts: Dict = None,
    ) -> models.DescribeApproveListResponse:
        """
        Getting pending approval list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApproveList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApproveListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApproveTypeList(
            self,
            request: models.DescribeApproveTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeApproveTypeListResponse:
        """
        Get Approval Category List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApproveTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApproveTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchOperateTask(
            self,
            request: models.DescribeBatchOperateTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchOperateTaskResponse:
        """
        Batch operation page to retrieve task list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchOperateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchOperateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeColumnLineage(
            self,
            request: models.DescribeColumnLineageRequest,
            opts: Dict = None,
    ) -> models.DescribeColumnLineageResponse:
        """
        List Field Lineage Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeColumnLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeColumnLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeColumnsMeta(
            self,
            request: models.DescribeColumnsMetaRequest,
            opts: Dict = None,
    ) -> models.DescribeColumnsMetaResponse:
        """
        Query all column metadata of the table
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeColumnsMeta"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeColumnsMetaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataCheckStat(
            self,
            request: models.DescribeDataCheckStatRequest,
            opts: Dict = None,
    ) -> models.DescribeDataCheckStatResponse:
        """
        Data Quality Overview Page Data Monitoring Interface
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataCheckStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataCheckStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSourceInfoList(
            self,
            request: models.DescribeDataSourceInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSourceInfoListResponse:
        """
        Obtain Data Source Information - Data Source Pagination List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSourceInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSourceInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSourceList(
            self,
            request: models.DescribeDataSourceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSourceListResponse:
        """
        Data Source Details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSourceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSourceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseInfoList(
            self,
            request: models.DescribeDatabaseInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseInfoListResponse:
        """
        Obtain Database Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseMetas(
            self,
            request: models.DescribeDatabaseMetasRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseMetasResponse:
        """
        Querying database list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseMetas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseMetasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatasource(
            self,
            request: models.DescribeDatasourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDatasourceResponse:
        """
        Data Source Details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatasource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatasourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDependOpsTasks(
            self,
            request: models.DescribeDependOpsTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeDependOpsTasksResponse:
        """
        Search for upstream/downstream task nodes by hierarchy
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDependOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDependOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDependTaskLists(
            self,
            request: models.DescribeDependTaskListsRequest,
            opts: Dict = None,
    ) -> models.DescribeDependTaskListsResponse:
        """
        Query Task Detail List by taskIds
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDependTaskLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDependTaskListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDimensionScore(
            self,
            request: models.DescribeDimensionScoreRequest,
            opts: Dict = None,
    ) -> models.DescribeDimensionScoreResponse:
        """
        Quality Report - Query Quality Score
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDimensionScore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDimensionScoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDrInstancePage(
            self,
            request: models.DescribeDrInstancePageRequest,
            opts: Dict = None,
    ) -> models.DescribeDrInstancePageResponse:
        """
        Paginated Query of Trial Run Instance List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDrInstancePage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDrInstancePageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDsFolderTree(
            self,
            request: models.DescribeDsFolderTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeDsFolderTreeResponse:
        """
        Query Directory Tree
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDsFolderTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDsFolderTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDsParentFolderTree(
            self,
            request: models.DescribeDsParentFolderTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeDsParentFolderTreeResponse:
        """
        Query Parent Directory Tree, for Workflow, Task Localization
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDsParentFolderTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDsParentFolderTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEvent(
            self,
            request: models.DescribeEventRequest,
            opts: Dict = None,
    ) -> models.DescribeEventResponse:
        """
        View Event Details by Project ID and Event Name
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventCases(
            self,
            request: models.DescribeEventCasesRequest,
            opts: Dict = None,
    ) -> models.DescribeEventCasesResponse:
        """
        Find Event Instances Based on Conditions
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventCases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventCasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventConsumeTasks(
            self,
            request: models.DescribeEventConsumeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeEventConsumeTasksResponse:
        """
        Viewing consumption tasks of event instances
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventConsumeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventConsumeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExecStrategy(
            self,
            request: models.DescribeExecStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeExecStrategyResponse:
        """
        Query Rule Group Execution Policy
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExecStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExecStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFieldBasicInfo(
            self,
            request: models.DescribeFieldBasicInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeFieldBasicInfoResponse:
        """
        Metadata Model - Field Basic Information Query Interface
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFieldBasicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFieldBasicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFolderWorkflowList(
            self,
            request: models.DescribeFolderWorkflowListRequest,
            opts: Dict = None,
    ) -> models.DescribeFolderWorkflowListResponse:
        """
        Get all workflow lists under the project by Project ID
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFolderWorkflowList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFolderWorkflowListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctionKinds(
            self,
            request: models.DescribeFunctionKindsRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionKindsResponse:
        """
        Query Function Classification
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctionKinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionKindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctionTypes(
            self,
            request: models.DescribeFunctionTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionTypesResponse:
        """
        Query Function Type
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctionTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceByCycle(
            self,
            request: models.DescribeInstanceByCycleRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceByCycleResponse:
        """
        Query all instances by cycle type
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceByCycle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceByCycleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLastLog(
            self,
            request: models.DescribeInstanceLastLogRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLastLogResponse:
        """
        Log Detail Acquisition Page
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLastLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLastLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceList(
            self,
            request: models.DescribeInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceListResponse:
        """
        Get Instance List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLog(
            self,
            request: models.DescribeInstanceLogRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogResponse:
        """
        Get Instance Running Logs
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLogDetail(
            self,
            request: models.DescribeInstanceLogDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogDetailResponse:
        """
        Obtain Specific Instance-related Log Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLogDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLogFile(
            self,
            request: models.DescribeInstanceLogFileRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogFileResponse:
        """
        Download Log File, Return Log Download URL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLogList(
            self,
            request: models.DescribeInstanceLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogListResponse:
        """
        Offline Task Instance Run Log List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationNode(
            self,
            request: models.DescribeIntegrationNodeRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationNodeResponse:
        """
        Query integrated nodes
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationStatistics(
            self,
            request: models.DescribeIntegrationStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationStatisticsResponse:
        """
        DataInLong Dashboard Overview
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationStatisticsInstanceTrend(
            self,
            request: models.DescribeIntegrationStatisticsInstanceTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationStatisticsInstanceTrendResponse:
        """
        DataInLong dashboard instance status statistical trend
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationStatisticsInstanceTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationStatisticsInstanceTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationStatisticsRecordsTrend(
            self,
            request: models.DescribeIntegrationStatisticsRecordsTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationStatisticsRecordsTrendResponse:
        """
        DataInLong Dashboard synchronization count trend
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationStatisticsRecordsTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationStatisticsRecordsTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationStatisticsTaskStatus(
            self,
            request: models.DescribeIntegrationStatisticsTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationStatisticsTaskStatusResponse:
        """
        DataInLong Dashboard Task Status Distribution Statistics
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationStatisticsTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationStatisticsTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationStatisticsTaskStatusTrend(
            self,
            request: models.DescribeIntegrationStatisticsTaskStatusTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationStatisticsTaskStatusTrendResponse:
        """
        DataInLong Dashboard Task Status Statistical Trend
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationStatisticsTaskStatusTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationStatisticsTaskStatusTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationTask(
            self,
            request: models.DescribeIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationTaskResponse:
        """
        Query integration tasks
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationTasks(
            self,
            request: models.DescribeIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationTasksResponse:
        """
        Query Integration Task List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationVersionNodesInfo(
            self,
            request: models.DescribeIntegrationVersionNodesInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationVersionNodesInfoResponse:
        """
        Query Integration Task Version Node Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationVersionNodesInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationVersionNodesInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOfflineTaskToken(
            self,
            request: models.DescribeOfflineTaskTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeOfflineTaskTokenResponse:
        """
        Getting long connection Token for offline tasks
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOfflineTaskToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOfflineTaskTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOperateOpsTasks(
            self,
            request: models.DescribeOperateOpsTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeOperateOpsTasksResponse:
        """
        Task Operation and Maintenance List Combined Condition Query
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOperateOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOperateOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpsInstanceLogList(
            self,
            request: models.DescribeOpsInstanceLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeOpsInstanceLogListResponse:
        """
        Instance Operation and Maintenance - Get Instance Log List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpsInstanceLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpsInstanceLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpsMakePlanInstances(
            self,
            request: models.DescribeOpsMakePlanInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeOpsMakePlanInstancesResponse:
        """
        Obtain the Supplementary Instance List based on the Supplementary Plan and Task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpsMakePlanInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpsMakePlanInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpsMakePlanTasks(
            self,
            request: models.DescribeOpsMakePlanTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeOpsMakePlanTasksResponse:
        """
        View Supplemental Plan Tasks
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpsMakePlanTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpsMakePlanTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpsMakePlans(
            self,
            request: models.DescribeOpsMakePlansRequest,
            opts: Dict = None,
    ) -> models.DescribeOpsMakePlansResponse:
        """
        Paginated Query of Supplement Plan Based on Conditions
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpsMakePlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpsMakePlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpsWorkflows(
            self,
            request: models.DescribeOpsWorkflowsRequest,
            opts: Dict = None,
    ) -> models.DescribeOpsWorkflowsResponse:
        """
        Querying User Production Workflow List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpsWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpsWorkflowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationalFunctions(
            self,
            request: models.DescribeOrganizationalFunctionsRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationalFunctionsResponse:
        """
        Query Full Functionality
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationalFunctions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationalFunctionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProject(
            self,
            request: models.DescribeProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectResponse:
        """
        Retrieving Project Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityScore(
            self,
            request: models.DescribeQualityScoreRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityScoreResponse:
        """
        Quality Report - Quality Score
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityScore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityScoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityScoreTrend(
            self,
            request: models.DescribeQualityScoreTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityScoreTrendResponse:
        """
        Quality Report - Quality Score Periodic Trend
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityScoreTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityScoreTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealTimeTaskInstanceNodeInfo(
            self,
            request: models.DescribeRealTimeTaskInstanceNodeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRealTimeTaskInstanceNodeInfoResponse:
        """
        Query Real-time Task Instance Node Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealTimeTaskInstanceNodeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealTimeTaskInstanceNodeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealTimeTaskMetricOverview(
            self,
            request: models.DescribeRealTimeTaskMetricOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeRealTimeTaskMetricOverviewResponse:
        """
        Real-time Task Running Metrics Overview
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealTimeTaskMetricOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealTimeTaskMetricOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealTimeTaskSpeed(
            self,
            request: models.DescribeRealTimeTaskSpeedRequest,
            opts: Dict = None,
    ) -> models.DescribeRealTimeTaskSpeedResponse:
        """
        Real-time task synchronization speed trend
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealTimeTaskSpeed"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealTimeTaskSpeedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReportTaskDetail(
            self,
            request: models.DescribeReportTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeReportTaskDetailResponse:
        """
        This API is used to query task details for reports.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReportTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReportTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReportTaskList(
            self,
            request: models.DescribeReportTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeReportTaskListResponse:
        """
        This API is used to query the task submission list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReportTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReportTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceManagePathTrees(
            self,
            request: models.DescribeResourceManagePathTreesRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceManagePathTreesResponse:
        """
        Retrieve resource management directory tree
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceManagePathTrees"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceManagePathTreesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoleList(
            self,
            request: models.DescribeRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeRoleListResponse:
        """
        This API is used to retrieve role list information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRule(
            self,
            request: models.DescribeRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleResponse:
        """
        Queries rule details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleDimStat(
            self,
            request: models.DescribeRuleDimStatRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleDimStatResponse:
        """
        Data Quality Overview Page Triggers Dimension Distribution Statistics Interface
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleDimStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleDimStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleExecDetail(
            self,
            request: models.DescribeRuleExecDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleExecDetailResponse:
        """
        Query Rule Execution Result Details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleExecDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleExecDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleExecLog(
            self,
            request: models.DescribeRuleExecLogRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleExecLogResponse:
        """
        Rule Execution Log Query
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleExecLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleExecLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleExecResults(
            self,
            request: models.DescribeRuleExecResultsRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleExecResultsResponse:
        """
        Query Rule Execution Result List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleExecResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleExecResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleExecStat(
            self,
            request: models.DescribeRuleExecStatRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleExecStatResponse:
        """
        Data Quality Overview Page Rule Operation Interface
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleExecStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleExecStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleGroup(
            self,
            request: models.DescribeRuleGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleGroupResponse:
        """
        Query Rule Group Details Interface
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleGroupExecResultsByPage(
            self,
            request: models.DescribeRuleGroupExecResultsByPageRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleGroupExecResultsByPageResponse:
        """
        Rule Group Execution Result Pagination Query Interface
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleGroupExecResultsByPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleGroupExecResultsByPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleGroupSubscription(
            self,
            request: models.DescribeRuleGroupSubscriptionRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleGroupSubscriptionResponse:
        """
        Query Rule Group Subscription Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleGroupSubscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleGroupSubscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleGroupTable(
            self,
            request: models.DescribeRuleGroupTableRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleGroupTableResponse:
        """
        Query Table Binding Execution Rule Group Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleGroupTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleGroupTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleGroupsByPage(
            self,
            request: models.DescribeRuleGroupsByPageRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleGroupsByPageResponse:
        """
        [Filter Criteria]
        {Table Name (TableName), supports fuzzy matching}       {Table Owner (TableOwnerName), supports fuzzy matching}      {Monitoring Methods (MonitorTypes), 1. Not Configured 2. Linked to Production Scheduling 3. Offline Periodic Inspection, supports multiple selections}  {Subscriber (ReceiverUin)}
        [Required Fields]
        {Data Source (DatasourceId)}
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleGroupsByPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleGroupsByPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleTemplate(
            self,
            request: models.DescribeRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleTemplateResponse:
        """
        Query Template Details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleTemplates(
            self,
            request: models.DescribeRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleTemplatesResponse:
        """
        Viewing Rule Template List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleTemplatesByPage(
            self,
            request: models.DescribeRuleTemplatesByPageRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleTemplatesByPageResponse:
        """
        [Filter Conditions] {Template Name (Name), supports fuzzy matching} {Template Type (type), 1.System Template 2.Custom Definition Template} {Quality Detection Dimensions (QualityDims), 1.Accuracy 2.Uniqueness 3.Integrity 4.Consistency 5.Timeliness 6.Validity} [Sorting Field] {Citation Sorting Type (CitationOrderType), sort by citation count ASC DESC}
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleTemplatesByPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleTemplatesByPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRules(
            self,
            request: models.DescribeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesResponse:
        """
        Query Quality Rule List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRulesByPage(
            self,
            request: models.DescribeRulesByPageRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesByPageResponse:
        """
        Paginated Query of Quality Rules
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRulesByPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesByPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScheduleInstances(
            self,
            request: models.DescribeScheduleInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeScheduleInstancesResponse:
        """
        Get Instance List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScheduleInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScheduleInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedulerInstanceStatus(
            self,
            request: models.DescribeSchedulerInstanceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulerInstanceStatusResponse:
        """
        Operation and Maintenance Dashboard-Instance Status Distribution
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedulerInstanceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulerInstanceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedulerRunTimeInstanceCntByStatus(
            self,
            request: models.DescribeSchedulerRunTimeInstanceCntByStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulerRunTimeInstanceCntByStatusResponse:
        """
        Operation and Maintenance Dashboard - Instance Running Duration Ranking
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedulerRunTimeInstanceCntByStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulerRunTimeInstanceCntByStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedulerTaskCntByStatus(
            self,
            request: models.DescribeSchedulerTaskCntByStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulerTaskCntByStatusResponse:
        """
        Task Status Statistics
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedulerTaskCntByStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulerTaskCntByStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedulerTaskTypeCnt(
            self,
            request: models.DescribeSchedulerTaskTypeCntRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulerTaskTypeCntResponse:
        """
        Operation and Maintenance Dashboard - Task Status Distribution
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedulerTaskTypeCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulerTaskTypeCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStatisticInstanceStatusTrendOps(
            self,
            request: models.DescribeStatisticInstanceStatusTrendOpsRequest,
            opts: Dict = None,
    ) -> models.DescribeStatisticInstanceStatusTrendOpsResponse:
        """
        Task Status Trend
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStatisticInstanceStatusTrendOps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStatisticInstanceStatusTrendOpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamTaskLogList(
            self,
            request: models.DescribeStreamTaskLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamTaskLogListResponse:
        """
        Query real-time task log list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamTaskLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamTaskLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSuccessorOpsTaskInfos(
            self,
            request: models.DescribeSuccessorOpsTaskInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeSuccessorOpsTaskInfosResponse:
        """
        Get Downstream Task Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSuccessorOpsTaskInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSuccessorOpsTaskInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableBasicInfo(
            self,
            request: models.DescribeTableBasicInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTableBasicInfoResponse:
        """
        Metadata Model-Table Basic Information Query Interface
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableBasicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableBasicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableInfoList(
            self,
            request: models.DescribeTableInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeTableInfoListResponse:
        """
        Retrieve Data Table Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableLineage(
            self,
            request: models.DescribeTableLineageRequest,
            opts: Dict = None,
    ) -> models.DescribeTableLineageResponse:
        """
        List Table Lineage Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableLineageInfo(
            self,
            request: models.DescribeTableLineageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTableLineageInfoResponse:
        """
        List Table Lineage Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableLineageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableLineageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableMeta(
            self,
            request: models.DescribeTableMetaRequest,
            opts: Dict = None,
    ) -> models.DescribeTableMetaResponse:
        """
        Querying Table Metadata Details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableMeta"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableMetaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableMetas(
            self,
            request: models.DescribeTableMetasRequest,
            opts: Dict = None,
    ) -> models.DescribeTableMetasResponse:
        """
        Get Table Metadata List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableMetas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableMetasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableQualityDetails(
            self,
            request: models.DescribeTableQualityDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeTableQualityDetailsResponse:
        """
        Quality Report - Query Table Quality Details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableQualityDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableQualityDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableSchemaInfo(
            self,
            request: models.DescribeTableSchemaInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTableSchemaInfoResponse:
        """
        Retrieve Table Schema Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableSchemaInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableSchemaInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableScoreTrend(
            self,
            request: models.DescribeTableScoreTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeTableScoreTrendResponse:
        """
        Query Table Score Trend
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableScoreTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableScoreTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskAlarmRegulations(
            self,
            request: models.DescribeTaskAlarmRegulationsRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskAlarmRegulationsResponse:
        """
        Query Task Alert Rule List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskAlarmRegulations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskAlarmRegulationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskByCycle(
            self,
            request: models.DescribeTaskByCycleRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskByCycleResponse:
        """
        Query all tasks by cycle type
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskByCycle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskByCycleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskByCycleReport(
            self,
            request: models.DescribeTaskByCycleReportRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskByCycleReportResponse:
        """
        Task Status Cycle Growth Trend
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskByCycleReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskByCycleReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskByStatusReport(
            self,
            request: models.DescribeTaskByStatusReportRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskByStatusReportResponse:
        """
        Task Status Trend
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskByStatusReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskByStatusReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLockStatus(
            self,
            request: models.DescribeTaskLockStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLockStatusResponse:
        """
        View Task Lock Status Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLockStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLockStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskRunHistory(
            self,
            request: models.DescribeTaskRunHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskRunHistoryResponse:
        """
        Paging Query Task Execution History
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskRunHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskRunHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskScript(
            self,
            request: models.DescribeTaskScriptRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskScriptResponse:
        """
        Query Task Script
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplateDimCount(
            self,
            request: models.DescribeTemplateDimCountRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateDimCountResponse:
        """
        Query rule template dimension distribution
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplateDimCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateDimCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeThirdTaskRunLog(
            self,
            request: models.DescribeThirdTaskRunLogRequest,
            opts: Dict = None,
    ) -> models.DescribeThirdTaskRunLogResponse:
        """
        Get third-party operation logs
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeThirdTaskRunLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeThirdTaskRunLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopTableStat(
            self,
            request: models.DescribeTopTableStatRequest,
            opts: Dict = None,
    ) -> models.DescribeTopTableStatResponse:
        """
        Data Quality Overview Page Table Ranking Interface
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopTableStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopTableStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrendStat(
            self,
            request: models.DescribeTrendStatRequest,
            opts: Dict = None,
    ) -> models.DescribeTrendStatResponse:
        """
        Data Quality Overview Page Trend Change Interface
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrendStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrendStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowCanvasInfo(
            self,
            request: models.DescribeWorkflowCanvasInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowCanvasInfoResponse:
        """
        Query Workflow Canvas
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowCanvasInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowCanvasInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowExecuteById(
            self,
            request: models.DescribeWorkflowExecuteByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowExecuteByIdResponse:
        """
        Query Workflow Canvas Run Start and End Time
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowExecuteById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowExecuteByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowInfoById(
            self,
            request: models.DescribeWorkflowInfoByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowInfoByIdResponse:
        """
        Query Workflow Details by Workflow ID
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowInfoById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowInfoByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowListByProjectId(
            self,
            request: models.DescribeWorkflowListByProjectIdRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowListByProjectIdResponse:
        """
        Get all workflow lists under the project by Project ID
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowListByProjectId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowListByProjectIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowTaskCount(
            self,
            request: models.DescribeWorkflowTaskCountRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowTaskCountResponse:
        """
        Query the number of workflow tasks
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowTaskCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowTaskCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DiagnosePro(
            self,
            request: models.DiagnoseProRequest,
            opts: Dict = None,
    ) -> models.DiagnoseProResponse:
        """
        Instance diagnosis for diagnosing instances in INITIAL, DEPENDENCE, ALLOCATED, LAUNCHED, EVENT_LISTENING, BEFORE_ASPECT, EXPIRED, FAILED states
        """
        
        kwargs = {}
        kwargs["action"] = "DiagnosePro"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DiagnoseProResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DryRunDIOfflineTask(
            self,
            request: models.DryRunDIOfflineTaskRequest,
            opts: Dict = None,
    ) -> models.DryRunDIOfflineTaskResponse:
        """
        Debug and Run Integration Task
        """
        
        kwargs = {}
        kwargs["action"] = "DryRunDIOfflineTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DryRunDIOfflineTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FindAllFolder(
            self,
            request: models.FindAllFolderRequest,
            opts: Dict = None,
    ) -> models.FindAllFolderResponse:
        """
        Orchestration Space Bulk Operation Page Find All Folders
        """
        
        kwargs = {}
        kwargs["action"] = "FindAllFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FindAllFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FreezeOpsTasks(
            self,
            request: models.FreezeOpsTasksRequest,
            opts: Dict = None,
    ) -> models.FreezeOpsTasksResponse:
        """
        Task Operation and Maintenance - Bulk Pause Tasks
        """
        
        kwargs = {}
        kwargs["action"] = "FreezeOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FreezeOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FreezeTasksByWorkflowIds(
            self,
            request: models.FreezeTasksByWorkflowIdsRequest,
            opts: Dict = None,
    ) -> models.FreezeTasksByWorkflowIdsResponse:
        """
        Pause All Tasks Under Workflow
        """
        
        kwargs = {}
        kwargs["action"] = "FreezeTasksByWorkflowIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FreezeTasksByWorkflowIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenHiveTableDDLSql(
            self,
            request: models.GenHiveTableDDLSqlRequest,
            opts: Dict = None,
    ) -> models.GenHiveTableDDLSqlResponse:
        """
        Generate SQL for Creating Hive Table
        """
        
        kwargs = {}
        kwargs["action"] = "GenHiveTableDDLSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenHiveTableDDLSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFileInfo(
            self,
            request: models.GetFileInfoRequest,
            opts: Dict = None,
    ) -> models.GetFileInfoResponse:
        """
        Development Space - Obtain data development script information
        """
        
        kwargs = {}
        kwargs["action"] = "GetFileInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFileInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetInstanceLog(
            self,
            request: models.GetInstanceLogRequest,
            opts: Dict = None,
    ) -> models.GetInstanceLogResponse:
        """
        This API is used to obtain instance lists.
        """
        
        kwargs = {}
        kwargs["action"] = "GetInstanceLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetInstanceLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetIntegrationNodeColumnSchema(
            self,
            request: models.GetIntegrationNodeColumnSchemaRequest,
            opts: Dict = None,
    ) -> models.GetIntegrationNodeColumnSchemaResponse:
        """
        Extracting DataInLong Node Field Schema
        """
        
        kwargs = {}
        kwargs["action"] = "GetIntegrationNodeColumnSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetIntegrationNodeColumnSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOfflineDIInstanceList(
            self,
            request: models.GetOfflineDIInstanceListRequest,
            opts: Dict = None,
    ) -> models.GetOfflineDIInstanceListResponse:
        """
        Get Offline Task Instance List (New)
        """
        
        kwargs = {}
        kwargs["action"] = "GetOfflineDIInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOfflineDIInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOfflineInstanceList(
            self,
            request: models.GetOfflineInstanceListRequest,
            opts: Dict = None,
    ) -> models.GetOfflineInstanceListResponse:
        """
        Obtain Offline Task Instances
        """
        
        kwargs = {}
        kwargs["action"] = "GetOfflineInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOfflineInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskInstance(
            self,
            request: models.GetTaskInstanceRequest,
            opts: Dict = None,
    ) -> models.GetTaskInstanceResponse:
        """
        This API is used to obtain instance lists.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillOpsMakePlanInstances(
            self,
            request: models.KillOpsMakePlanInstancesRequest,
            opts: Dict = None,
    ) -> models.KillOpsMakePlanInstancesResponse:
        """
        Batch Termination of Instances by Supplement Plan.
        """
        
        kwargs = {}
        kwargs["action"] = "KillOpsMakePlanInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillOpsMakePlanInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillScheduleInstances(
            self,
            request: models.KillScheduleInstancesRequest,
            opts: Dict = None,
    ) -> models.KillScheduleInstancesResponse:
        """
        Batch Termination of Instances
        """
        
        kwargs = {}
        kwargs["action"] = "KillScheduleInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillScheduleInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListInstances(
            self,
            request: models.ListInstancesRequest,
            opts: Dict = None,
    ) -> models.ListInstancesResponse:
        """
        This API is used to obtain instance lists.
        """
        
        kwargs = {}
        kwargs["action"] = "ListInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LockIntegrationTask(
            self,
            request: models.LockIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.LockIntegrationTaskResponse:
        """
        Lock Integration Task
        """
        
        kwargs = {}
        kwargs["action"] = "LockIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LockIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApproveStatus(
            self,
            request: models.ModifyApproveStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApproveStatusResponse:
        """
        Modify Approval Form Status
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApproveStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApproveStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDataSource(
            self,
            request: models.ModifyDataSourceRequest,
            opts: Dict = None,
    ) -> models.ModifyDataSourceResponse:
        """
        Modify Data Source
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDimensionWeight(
            self,
            request: models.ModifyDimensionWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyDimensionWeightResponse:
        """
        Quality Report - Modify Dimension Permissions
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDimensionWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDimensionWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDsFolder(
            self,
            request: models.ModifyDsFolderRequest,
            opts: Dict = None,
    ) -> models.ModifyDsFolderResponse:
        """
        Data Development Module - Folder Update
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDsFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDsFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExecStrategy(
            self,
            request: models.ModifyExecStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyExecStrategyResponse:
        """
        Update Rule Group Execution Strategy
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExecStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExecStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIntegrationNode(
            self,
            request: models.ModifyIntegrationNodeRequest,
            opts: Dict = None,
    ) -> models.ModifyIntegrationNodeResponse:
        """
        Updating Integrated Nodes
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIntegrationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIntegrationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIntegrationTask(
            self,
            request: models.ModifyIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyIntegrationTaskResponse:
        """
        Update Integration Task
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMonitorStatus(
            self,
            request: models.ModifyMonitorStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyMonitorStatusResponse:
        """
        Update Monitoring Status
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMonitorStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMonitorStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRule(
            self,
            request: models.ModifyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleResponse:
        """
        Update Quality Rule Interface
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRuleGroupSubscription(
            self,
            request: models.ModifyRuleGroupSubscriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleGroupSubscriptionResponse:
        """
        Update Rule Group Subscription Information
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRuleGroupSubscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleGroupSubscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRuleTemplate(
            self,
            request: models.ModifyRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleTemplateResponse:
        """
        Edit Rule Template
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskAlarmRegular(
            self,
            request: models.ModifyTaskAlarmRegularRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskAlarmRegularResponse:
        """
        Modify task alert rules
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskAlarmRegular"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskAlarmRegularResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskInfo(
            self,
            request: models.ModifyTaskInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskInfoResponse:
        """
        <p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Update Task
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskLinks(
            self,
            request: models.ModifyTaskLinksRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskLinksResponse:
        """
        <p style="color:red;">[Note: This version is only available to some whitelist customers in the Guangzhou zone]</p>.
        Add parent task dependency. This API is deprecated. Use API ModifyTaskLinksDs.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskLinks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskLinksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskLinksDs(
            self,
            request: models.ModifyTaskLinksDsRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskLinksDsResponse:
        """
        This API is used to add parent task dependency.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskLinksDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskLinksDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskName(
            self,
            request: models.ModifyTaskNameRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskNameResponse:
        """
        Rename Task (Task Editing)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskScript(
            self,
            request: models.ModifyTaskScriptRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskScriptResponse:
        """
        <p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Modify Task Script
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkflowInfo(
            self,
            request: models.ModifyWorkflowInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkflowInfoResponse:
        """
        This API is used to update workflow information. (deprecated). Use API UpdateWorkflowInfo.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkflowInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkflowInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkflowSchedule(
            self,
            request: models.ModifyWorkflowScheduleRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkflowScheduleResponse:
        """
        This API is used to update workflow scheduling. This API is deprecated. Use the RenewWorkflowSchedulerInfoDs API instead.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkflowSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkflowScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MoveTasksToFolder(
            self,
            request: models.MoveTasksToFolderRequest,
            opts: Dict = None,
    ) -> models.MoveTasksToFolderResponse:
        """
        Orchestration Space - Workflow - Move Task to Workflow Folder
        """
        
        kwargs = {}
        kwargs["action"] = "MoveTasksToFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MoveTasksToFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterDsEvent(
            self,
            request: models.RegisterDsEventRequest,
            opts: Dict = None,
    ) -> models.RegisterDsEventResponse:
        """
        This API is used to register an event.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterDsEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterDsEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterEvent(
            self,
            request: models.RegisterEventRequest,
            opts: Dict = None,
    ) -> models.RegisterEventResponse:
        """
        <p style="color:red;">[Note: This version is only available for partial allowlisted customers in the Guangzhou region]</p>.
        This API is used to register events. This API is deprecated. Use API RegisterDsEvent.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterEventListener(
            self,
            request: models.RegisterEventListenerRequest,
            opts: Dict = None,
    ) -> models.RegisterEventListenerResponse:
        """
        <p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Register Event Listener
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterEventListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterEventListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveWorkflowDs(
            self,
            request: models.RemoveWorkflowDsRequest,
            opts: Dict = None,
    ) -> models.RemoveWorkflowDsResponse:
        """
        Delete orchestration space workflow
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveWorkflowDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveWorkflowDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewWorkflowOwnerDs(
            self,
            request: models.RenewWorkflowOwnerDsRequest,
            opts: Dict = None,
    ) -> models.RenewWorkflowOwnerDsResponse:
        """
        This API is used to batch update the task owner under a workflow.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewWorkflowOwnerDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewWorkflowOwnerDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewWorkflowSchedulerInfoDs(
            self,
            request: models.RenewWorkflowSchedulerInfoDsRequest,
            opts: Dict = None,
    ) -> models.RenewWorkflowSchedulerInfoDsResponse:
        """
        This API is used to update task scheduling information under a workflow.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewWorkflowSchedulerInfoDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewWorkflowSchedulerInfoDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeIntegrationTask(
            self,
            request: models.ResumeIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.ResumeIntegrationTaskResponse:
        """
        Continue Integration Task
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RobAndLockIntegrationTask(
            self,
            request: models.RobAndLockIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.RobAndLockIntegrationTaskResponse:
        """
        Preemptive locking of integration tasks
        """
        
        kwargs = {}
        kwargs["action"] = "RobAndLockIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RobAndLockIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunForceSucScheduleInstances(
            self,
            request: models.RunForceSucScheduleInstancesRequest,
            opts: Dict = None,
    ) -> models.RunForceSucScheduleInstancesResponse:
        """
        Instance Batch Successfully Configured
        """
        
        kwargs = {}
        kwargs["action"] = "RunForceSucScheduleInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunForceSucScheduleInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunRerunScheduleInstances(
            self,
            request: models.RunRerunScheduleInstancesRequest,
            opts: Dict = None,
    ) -> models.RunRerunScheduleInstancesResponse:
        """
        Instance Batch Rerun
        """
        
        kwargs = {}
        kwargs["action"] = "RunRerunScheduleInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunRerunScheduleInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunTasksByMultiWorkflow(
            self,
            request: models.RunTasksByMultiWorkflowRequest,
            opts: Dict = None,
    ) -> models.RunTasksByMultiWorkflowResponse:
        """
        Batch startup of workflows
        """
        
        kwargs = {}
        kwargs["action"] = "RunTasksByMultiWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunTasksByMultiWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SaveCustomFunction(
            self,
            request: models.SaveCustomFunctionRequest,
            opts: Dict = None,
    ) -> models.SaveCustomFunctionResponse:
        """
        Save User-Defined Function
        """
        
        kwargs = {}
        kwargs["action"] = "SaveCustomFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SaveCustomFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTaskAlarmNew(
            self,
            request: models.SetTaskAlarmNewRequest,
            opts: Dict = None,
    ) -> models.SetTaskAlarmNewResponse:
        """
        <p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Set Task Alerts, Create/Update Alert Information (Latest)
        """
        
        kwargs = {}
        kwargs["action"] = "SetTaskAlarmNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTaskAlarmNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartIntegrationTask(
            self,
            request: models.StartIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.StartIntegrationTaskResponse:
        """
        Initiate Integration Task
        """
        
        kwargs = {}
        kwargs["action"] = "StartIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopIntegrationTask(
            self,
            request: models.StopIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.StopIntegrationTaskResponse:
        """
        Stop Integration Task
        """
        
        kwargs = {}
        kwargs["action"] = "StopIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitCustomFunction(
            self,
            request: models.SubmitCustomFunctionRequest,
            opts: Dict = None,
    ) -> models.SubmitCustomFunctionResponse:
        """
        Submit Custom Definition Function
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitCustomFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitCustomFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitSqlTask(
            self,
            request: models.SubmitSqlTaskRequest,
            opts: Dict = None,
    ) -> models.SubmitSqlTaskResponse:
        """
        Ad Hoc Analysis - Submit SQL Task
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitSqlTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitSqlTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTask(
            self,
            request: models.SubmitTaskRequest,
            opts: Dict = None,
    ) -> models.SubmitTaskResponse:
        """
        <p style="color:red;">[Note: This version is only available for partial whitelist customers in the Guangzhou zone]</p>.
        This API is used to submit tasks. This API is deprecated. Use the CreateTaskVersionDs API.
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTaskTestRun(
            self,
            request: models.SubmitTaskTestRunRequest,
            opts: Dict = None,
    ) -> models.SubmitTaskTestRunResponse:
        """
        No
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTaskTestRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTaskTestRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitWorkflow(
            self,
            request: models.SubmitWorkflowRequest,
            opts: Dict = None,
    ) -> models.SubmitWorkflowResponse:
        """
        Submit a workflow. This API is deprecated. Use the BatchCreateTaskVersionAsync API.
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SuspendIntegrationTask(
            self,
            request: models.SuspendIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.SuspendIntegrationTaskResponse:
        """
        Pause Integration Task
        """
        
        kwargs = {}
        kwargs["action"] = "SuspendIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SuspendIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TaskLog(
            self,
            request: models.TaskLogRequest,
            opts: Dict = None,
    ) -> models.TaskLogResponse:
        """
        Query Inlong Manager Logs
        """
        
        kwargs = {}
        kwargs["action"] = "TaskLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TaskLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerDsEvent(
            self,
            request: models.TriggerDsEventRequest,
            opts: Dict = None,
    ) -> models.TriggerDsEventResponse:
        """
        Event Management - Triggered Events
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerDsEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerDsEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerEvent(
            self,
            request: models.TriggerEventRequest,
            opts: Dict = None,
    ) -> models.TriggerEventResponse:
        """
        <p style="color:red;">[Note: This version is only available to some allowlisted customers in the Guangzhou region]</p>.
        This API is used to trigger event. This API is deprecated. Use API TriggerDsEvent.
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnlockIntegrationTask(
            self,
            request: models.UnlockIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.UnlockIntegrationTaskResponse:
        """
        Unlock Integration Task
        """
        
        kwargs = {}
        kwargs["action"] = "UnlockIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnlockIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProjectUserRole(
            self,
            request: models.UpdateProjectUserRoleRequest,
            opts: Dict = None,
    ) -> models.UpdateProjectUserRoleResponse:
        """
        This API is used to modify user roles in a project.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProjectUserRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProjectUserRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkflowInfo(
            self,
            request: models.UpdateWorkflowInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkflowInfoResponse:
        """
        This API is developed in ds.
        This API is used to update a workflow, including its basic information and workflow parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflowInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkflowOwner(
            self,
            request: models.UpdateWorkflowOwnerRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkflowOwnerResponse:
        """
        This API is used to modify the workflow owner. Deprecated. Use the RenewWorkflowOwnerDs API.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflowOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadContent(
            self,
            request: models.UploadContentRequest,
            opts: Dict = None,
    ) -> models.UploadContentResponse:
        """
        Save Task Information
        """
        
        kwargs = {}
        kwargs["action"] = "UploadContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)