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
from tencentcloud.wedata.v20250806 import models
from typing import Dict


class WedataClient(AbstractClient):
    _apiVersion = '2025-08-06'
    _endpoint = 'wedata.intl.tencentcloudapi.com'
    _service = 'wedata'

    async def CreateCodeFile(
            self,
            request: models.CreateCodeFileRequest,
            opts: Dict = None,
    ) -> models.CreateCodeFileResponse:
        """
        This API is used to create a code file.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCodeFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCodeFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCodeFolder(
            self,
            request: models.CreateCodeFolderRequest,
            opts: Dict = None,
    ) -> models.CreateCodeFolderResponse:
        """
        This API is used to create a code folder.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCodeFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCodeFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataBackfillPlan(
            self,
            request: models.CreateDataBackfillPlanRequest,
            opts: Dict = None,
    ) -> models.CreateDataBackfillPlanResponse:
        """
        This API is used to create a data backfill plan.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataBackfillPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataBackfillPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpsAlarmRule(
            self,
            request: models.CreateOpsAlarmRuleRequest,
            opts: Dict = None,
    ) -> models.CreateOpsAlarmRuleResponse:
        """
        This API is used to set alarm rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpsAlarmRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpsAlarmRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResourceFile(
            self,
            request: models.CreateResourceFileRequest,
            opts: Dict = None,
    ) -> models.CreateResourceFileResponse:
        """
        This API is used to create a resource file.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResourceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResourceFolder(
            self,
            request: models.CreateResourceFolderRequest,
            opts: Dict = None,
    ) -> models.CreateResourceFolderResponse:
        """
        This API is used to create a resource file folder.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResourceFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSQLFolder(
            self,
            request: models.CreateSQLFolderRequest,
            opts: Dict = None,
    ) -> models.CreateSQLFolderResponse:
        """
        This API is used to create an SQL folder
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSQLFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSQLFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSQLScript(
            self,
            request: models.CreateSQLScriptRequest,
            opts: Dict = None,
    ) -> models.CreateSQLScriptResponse:
        """
        This API is used to add an SQL script.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSQLScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSQLScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTask(
            self,
            request: models.CreateTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTaskResponse:
        """
        This API is used to create a task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflow(
            self,
            request: models.CreateWorkflowRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowResponse:
        """
        This API is used to create workflow.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflowFolder(
            self,
            request: models.CreateWorkflowFolderRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowFolderResponse:
        """
        This API is used to create a workflow folder.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflowFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCodeFile(
            self,
            request: models.DeleteCodeFileRequest,
            opts: Dict = None,
    ) -> models.DeleteCodeFileResponse:
        """
        This API is used to delete a code file.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCodeFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCodeFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCodeFolder(
            self,
            request: models.DeleteCodeFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteCodeFolderResponse:
        """
        This API is used to delete folders in data exploration.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCodeFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCodeFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOpsAlarmRule(
            self,
            request: models.DeleteOpsAlarmRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteOpsAlarmRuleResponse:
        """
        Deletes alarm rules
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOpsAlarmRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOpsAlarmRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceFile(
            self,
            request: models.DeleteResourceFileRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceFileResponse:
        """
        This API is used to delete a resource file.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceFolder(
            self,
            request: models.DeleteResourceFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceFolderResponse:
        """
        This API is used to delete a resource folder.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSQLFolder(
            self,
            request: models.DeleteSQLFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteSQLFolderResponse:
        """
        This API is used to delete a SQL folder.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSQLFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSQLFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSQLScript(
            self,
            request: models.DeleteSQLScriptRequest,
            opts: Dict = None,
    ) -> models.DeleteSQLScriptResponse:
        """
        This API is used to delete an SQL script.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSQLScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSQLScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTask(
            self,
            request: models.DeleteTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskResponse:
        """
        This API is used to delete an orchestration space task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkflow(
            self,
            request: models.DeleteWorkflowRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowResponse:
        """
        Deletes a workflow
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkflowFolder(
            self,
            request: models.DeleteWorkflowFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowFolderResponse:
        """
        This API is used to delete a data development folder
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflowFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAlarmMessage(
            self,
            request: models.GetAlarmMessageRequest,
            opts: Dict = None,
    ) -> models.GetAlarmMessageResponse:
        """
        This API is used to query alert information details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAlarmMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAlarmMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCodeFile(
            self,
            request: models.GetCodeFileRequest,
            opts: Dict = None,
    ) -> models.GetCodeFileResponse:
        """
        This API is used to view code file details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetCodeFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCodeFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOpsAlarmRule(
            self,
            request: models.GetOpsAlarmRuleRequest,
            opts: Dict = None,
    ) -> models.GetOpsAlarmRuleResponse:
        """
        This API is used to query alert rule information based on alarm rule id or name.
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsAlarmRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsAlarmRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOpsAsyncJob(
            self,
            request: models.GetOpsAsyncJobRequest,
            opts: Dict = None,
    ) -> models.GetOpsAsyncJobResponse:
        """
        This API is used to query async operation details in Ops center.
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsAsyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsAsyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOpsTask(
            self,
            request: models.GetOpsTaskRequest,
            opts: Dict = None,
    ) -> models.GetOpsTaskResponse:
        """
        Obtaining Task Details
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOpsTaskCode(
            self,
            request: models.GetOpsTaskCodeRequest,
            opts: Dict = None,
    ) -> models.GetOpsTaskCodeResponse:
        """
        This API is used to retrieve task code.
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsTaskCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsTaskCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOpsWorkflow(
            self,
            request: models.GetOpsWorkflowRequest,
            opts: Dict = None,
    ) -> models.GetOpsWorkflowResponse:
        """
        This API is used to obtain workflow scheduling details based on the workflow id.
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetResourceFile(
            self,
            request: models.GetResourceFileRequest,
            opts: Dict = None,
    ) -> models.GetResourceFileResponse:
        """
        This API is used to obtain resource file details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetResourceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetResourceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSQLScript(
            self,
            request: models.GetSQLScriptRequest,
            opts: Dict = None,
    ) -> models.GetSQLScriptResponse:
        """
        This API is used to query script details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSQLScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSQLScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTask(
            self,
            request: models.GetTaskRequest,
            opts: Dict = None,
    ) -> models.GetTaskResponse:
        """
        This API is used to retrieve task details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskCode(
            self,
            request: models.GetTaskCodeRequest,
            opts: Dict = None,
    ) -> models.GetTaskCodeResponse:
        """
        This API is used to obtain task code.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskInstance(
            self,
            request: models.GetTaskInstanceRequest,
            opts: Dict = None,
    ) -> models.GetTaskInstanceResponse:
        """
        This API is used to query the details of a scheduling instance.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskInstanceLog(
            self,
            request: models.GetTaskInstanceLogRequest,
            opts: Dict = None,
    ) -> models.GetTaskInstanceLogResponse:
        """
        This API is used to obtain instance lists.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskInstanceLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskInstanceLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskVersion(
            self,
            request: models.GetTaskVersionRequest,
            opts: Dict = None,
    ) -> models.GetTaskVersionResponse:
        """
        This API is used to list task versions.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWorkflow(
            self,
            request: models.GetWorkflowRequest,
            opts: Dict = None,
    ) -> models.GetWorkflowResponse:
        """
        This API is used to retrieve workflow information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillTaskInstancesAsync(
            self,
            request: models.KillTaskInstancesAsyncRequest,
            opts: Dict = None,
    ) -> models.KillTaskInstancesAsyncResponse:
        """
        This API is used to terminate instances in batches asynchronously.
        """
        
        kwargs = {}
        kwargs["action"] = "KillTaskInstancesAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillTaskInstancesAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAlarmMessages(
            self,
            request: models.ListAlarmMessagesRequest,
            opts: Dict = None,
    ) -> models.ListAlarmMessagesResponse:
        """
        This API is used to search the alarm information list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAlarmMessages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAlarmMessagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCodeFolderContents(
            self,
            request: models.ListCodeFolderContentsRequest,
            opts: Dict = None,
    ) -> models.ListCodeFolderContentsResponse:
        """
        This API is used to get folder content.
        """
        
        kwargs = {}
        kwargs["action"] = "ListCodeFolderContents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCodeFolderContentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDataBackfillInstances(
            self,
            request: models.ListDataBackfillInstancesRequest,
            opts: Dict = None,
    ) -> models.ListDataBackfillInstancesResponse:
        """
        This API is used to retrieve all instances of a single backfill.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDataBackfillInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDataBackfillInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDownstreamOpsTasks(
            self,
            request: models.ListDownstreamOpsTasksRequest,
            opts: Dict = None,
    ) -> models.ListDownstreamOpsTasksResponse:
        """
        This API is used to retrieve task direct downstream details.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDownstreamOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDownstreamOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDownstreamTaskInstances(
            self,
            request: models.ListDownstreamTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.ListDownstreamTaskInstancesResponse:
        """
        This API is used to get the direct upstream of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDownstreamTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDownstreamTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDownstreamTasks(
            self,
            request: models.ListDownstreamTasksRequest,
            opts: Dict = None,
    ) -> models.ListDownstreamTasksResponse:
        """
        This API is used to retrieve the direct downstream task details.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDownstreamTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDownstreamTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOpsAlarmRules(
            self,
            request: models.ListOpsAlarmRulesRequest,
            opts: Dict = None,
    ) -> models.ListOpsAlarmRulesResponse:
        """
        This API is used to query the alarm rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOpsAlarmRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOpsAlarmRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOpsTasks(
            self,
            request: models.ListOpsTasksRequest,
            opts: Dict = None,
    ) -> models.ListOpsTasksResponse:
        """
        This API is used to obtain the task list based on the project id.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOpsWorkflows(
            self,
            request: models.ListOpsWorkflowsRequest,
            opts: Dict = None,
    ) -> models.ListOpsWorkflowsResponse:
        """
        Get Workflows under a Project by Project ID.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOpsWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOpsWorkflowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListResourceFiles(
            self,
            request: models.ListResourceFilesRequest,
            opts: Dict = None,
    ) -> models.ListResourceFilesResponse:
        """
        This API is used to view resource file list
        """
        
        kwargs = {}
        kwargs["action"] = "ListResourceFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListResourceFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListResourceFolders(
            self,
            request: models.ListResourceFoldersRequest,
            opts: Dict = None,
    ) -> models.ListResourceFoldersResponse:
        """
        This API is used to query the resource file folder list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListResourceFolders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListResourceFoldersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSQLFolderContents(
            self,
            request: models.ListSQLFolderContentsRequest,
            opts: Dict = None,
    ) -> models.ListSQLFolderContentsResponse:
        """
        This API is used to retrieve the content list of an sql folder
        """
        
        kwargs = {}
        kwargs["action"] = "ListSQLFolderContents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSQLFolderContentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSQLScriptRuns(
            self,
            request: models.ListSQLScriptRunsRequest,
            opts: Dict = None,
    ) -> models.ListSQLScriptRunsResponse:
        """
        This API is used to query SQL run history.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSQLScriptRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSQLScriptRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTaskInstanceExecutions(
            self,
            request: models.ListTaskInstanceExecutionsRequest,
            opts: Dict = None,
    ) -> models.ListTaskInstanceExecutionsResponse:
        """
        This API is used to query the details of a scheduling instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTaskInstanceExecutions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTaskInstanceExecutionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTaskInstances(
            self,
            request: models.ListTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.ListTaskInstancesResponse:
        """
        This API is used to obtain instance lists.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTaskVersions(
            self,
            request: models.ListTaskVersionsRequest,
            opts: Dict = None,
    ) -> models.ListTaskVersionsResponse:
        """
        This API is used to list saved task versions.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTaskVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTaskVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTasks(
            self,
            request: models.ListTasksRequest,
            opts: Dict = None,
    ) -> models.ListTasksResponse:
        """
        This API is used to query pagination information of tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUpstreamOpsTasks(
            self,
            request: models.ListUpstreamOpsTasksRequest,
            opts: Dict = None,
    ) -> models.ListUpstreamOpsTasksResponse:
        """
        This API is used to retrieve task direct upstream.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUpstreamOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUpstreamOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUpstreamTaskInstances(
            self,
            request: models.ListUpstreamTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.ListUpstreamTaskInstancesResponse:
        """
        This API is used to get the direct upstream of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUpstreamTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUpstreamTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUpstreamTasks(
            self,
            request: models.ListUpstreamTasksRequest,
            opts: Dict = None,
    ) -> models.ListUpstreamTasksResponse:
        """
        This API is used to retrieve the direct upstream task.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUpstreamTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUpstreamTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflowFolders(
            self,
            request: models.ListWorkflowFoldersRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowFoldersResponse:
        """
        This API is used to query the folder list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflowFolders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowFoldersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflows(
            self,
            request: models.ListWorkflowsRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowsResponse:
        """
        This API is used to query the list of workflows.
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseOpsTasksAsync(
            self,
            request: models.PauseOpsTasksAsyncRequest,
            opts: Dict = None,
    ) -> models.PauseOpsTasksAsyncResponse:
        """
        This API is used to pause tasks in batches asynchronously.
        """
        
        kwargs = {}
        kwargs["action"] = "PauseOpsTasksAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseOpsTasksAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RerunTaskInstancesAsync(
            self,
            request: models.RerunTaskInstancesAsyncRequest,
            opts: Dict = None,
    ) -> models.RerunTaskInstancesAsyncResponse:
        """
        This API is used to batch rerun instances asynchronously.
        """
        
        kwargs = {}
        kwargs["action"] = "RerunTaskInstancesAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RerunTaskInstancesAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunSQLScript(
            self,
            request: models.RunSQLScriptRequest,
            opts: Dict = None,
    ) -> models.RunSQLScriptResponse:
        """
        This API is used to run an SQL script.
        """
        
        kwargs = {}
        kwargs["action"] = "RunSQLScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunSQLScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetSuccessTaskInstancesAsync(
            self,
            request: models.SetSuccessTaskInstancesAsyncRequest,
            opts: Dict = None,
    ) -> models.SetSuccessTaskInstancesAsyncResponse:
        """
        This API is used to batch configure instances asynchronously.
        """
        
        kwargs = {}
        kwargs["action"] = "SetSuccessTaskInstancesAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetSuccessTaskInstancesAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopOpsTasksAsync(
            self,
            request: models.StopOpsTasksAsyncRequest,
            opts: Dict = None,
    ) -> models.StopOpsTasksAsyncResponse:
        """
        This API is used to asynchronously deactivate tasks in batch.
        """
        
        kwargs = {}
        kwargs["action"] = "StopOpsTasksAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopOpsTasksAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopSQLScriptRun(
            self,
            request: models.StopSQLScriptRunRequest,
            opts: Dict = None,
    ) -> models.StopSQLScriptRunResponse:
        """
        This API is used to stop running an SQL script.
        """
        
        kwargs = {}
        kwargs["action"] = "StopSQLScriptRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopSQLScriptRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTask(
            self,
            request: models.SubmitTaskRequest,
            opts: Dict = None,
    ) -> models.SubmitTaskResponse:
        """
        This API is used to submit a task.
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCodeFile(
            self,
            request: models.UpdateCodeFileRequest,
            opts: Dict = None,
    ) -> models.UpdateCodeFileResponse:
        """
        This API is used to update a code file.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCodeFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCodeFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCodeFolder(
            self,
            request: models.UpdateCodeFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateCodeFolderResponse:
        """
        This API is used to rename a code folder.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCodeFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCodeFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOpsAlarmRule(
            self,
            request: models.UpdateOpsAlarmRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateOpsAlarmRuleResponse:
        """
        Modifies alarm rules
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOpsAlarmRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOpsAlarmRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOpsTasksOwner(
            self,
            request: models.UpdateOpsTasksOwnerRequest,
            opts: Dict = None,
    ) -> models.UpdateOpsTasksOwnerResponse:
        """
        This API is used to modify the task owner.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOpsTasksOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOpsTasksOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateResourceFile(
            self,
            request: models.UpdateResourceFileRequest,
            opts: Dict = None,
    ) -> models.UpdateResourceFileResponse:
        """
        This API is used to update a resource file.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateResourceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateResourceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateResourceFolder(
            self,
            request: models.UpdateResourceFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateResourceFolderResponse:
        """
        This API is used to update a resource folder.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateResourceFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateResourceFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSQLFolder(
            self,
            request: models.UpdateSQLFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateSQLFolderResponse:
        """
        This API is used to rename an SQL folder.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSQLFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSQLFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSQLScript(
            self,
            request: models.UpdateSQLScriptRequest,
            opts: Dict = None,
    ) -> models.UpdateSQLScriptResponse:
        """
        This API is used to save the script content for data exploration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSQLScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSQLScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTask(
            self,
            request: models.UpdateTaskRequest,
            opts: Dict = None,
    ) -> models.UpdateTaskResponse:
        """
        This API is used to update a task.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkflow(
            self,
            request: models.UpdateWorkflowRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkflowResponse:
        """
        This API is used to update a workflow including basic information and workflow parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkflowFolder(
            self,
            request: models.UpdateWorkflowFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkflowFolderResponse:
        """
        This API is used to update a workflow folder
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflowFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)