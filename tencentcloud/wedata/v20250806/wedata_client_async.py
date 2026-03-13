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

    async def AddCalcEnginesToProject(
            self,
            request: models.AddCalcEnginesToProjectRequest,
            opts: Dict = None,
    ) -> models.AddCalcEnginesToProjectResponse:
        """
        Associate a project cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "AddCalcEnginesToProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCalcEnginesToProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateResourceGroupToProject(
            self,
            request: models.AssociateResourceGroupToProjectRequest,
            opts: Dict = None,
    ) -> models.AssociateResourceGroupToProjectResponse:
        """
        This API is used to bind the designated execution resource group to the project.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateResourceGroupToProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateResourceGroupToProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AuthorizeDataSource(
            self,
            request: models.AuthorizeDataSourceRequest,
            opts: Dict = None,
    ) -> models.AuthorizeDataSourceResponse:
        """
        Authorize a data source.
        """
        
        kwargs = {}
        kwargs["action"] = "AuthorizeDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AuthorizeDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AuthorizePrivileges(
            self,
            request: models.AuthorizePrivilegesRequest,
            opts: Dict = None,
    ) -> models.AuthorizePrivilegesResponse:
        """
        Authorization in Catalog mode.
        """
        
        kwargs = {}
        kwargs["action"] = "AuthorizePrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AuthorizePrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
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
        
    async def CreateCodePermissions(
            self,
            request: models.CreateCodePermissionsRequest,
            opts: Dict = None,
    ) -> models.CreateCodePermissionsResponse:
        """
        Configure CodeStudio entity permission.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCodePermissions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCodePermissionsResponse
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
        
    async def CreateDataSource(
            self,
            request: models.CreateDataSourceRequest,
            opts: Dict = None,
    ) -> models.CreateDataSourceResponse:
        """
        This API is used to create a data source in the designated project.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataSourceResponse
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
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        Create a project with cluster information upon creation.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProjectMember(
            self,
            request: models.CreateProjectMemberRequest,
            opts: Dict = None,
    ) -> models.CreateProjectMemberResponse:
        """
        Add project user role.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProjectMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectMemberResponse
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
        
    async def CreateResourceGroup(
            self,
            request: models.CreateResourceGroupRequest,
            opts: Dict = None,
    ) -> models.CreateResourceGroupResponse:
        """
        This API is used to purchase resources.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceGroupResponse
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
        
    async def CreateTaskFolder(
            self,
            request: models.CreateTaskFolderRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFolderResponse:
        """
        Create a folder.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTriggerTask(
            self,
            request: models.CreateTriggerTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTriggerTaskResponse:
        """
        This API is used to create a task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTriggerTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTriggerTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTriggerWorkflow(
            self,
            request: models.CreateTriggerWorkflowRequest,
            opts: Dict = None,
    ) -> models.CreateTriggerWorkflowResponse:
        """
        create workflow.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTriggerWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTriggerWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTriggerWorkflowRun(
            self,
            request: models.CreateTriggerWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.CreateTriggerWorkflowRunResponse:
        """
        Run workflow under workflow scheduling model.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTriggerWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTriggerWorkflowRunResponse
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
        
    async def CreateWorkflowPermissions(
            self,
            request: models.CreateWorkflowPermissionsRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowPermissionsResponse:
        """
        This API is used to configure data development permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflowPermissions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowPermissionsResponse
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
        
    async def DeleteCodePermissions(
            self,
            request: models.DeleteCodePermissionsRequest,
            opts: Dict = None,
    ) -> models.DeleteCodePermissionsResponse:
        """
        Delete CodeStudio entity permission.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCodePermissions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCodePermissionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataBackfillPlanAsync(
            self,
            request: models.DeleteDataBackfillPlanAsyncRequest,
            opts: Dict = None,
    ) -> models.DeleteDataBackfillPlanAsyncResponse:
        """
        Delete a replenishment plan.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataBackfillPlanAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataBackfillPlanAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataSource(
            self,
            request: models.DeleteDataSourceRequest,
            opts: Dict = None,
    ) -> models.DeleteDataSourceResponse:
        """
        This API is used to delete a data source.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLineage(
            self,
            request: models.DeleteLineageRequest,
            opts: Dict = None,
    ) -> models.DeleteLineageResponse:
        """
        RegisterLineage
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLineageResponse
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
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        This API is used to delete a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjectMember(
            self,
            request: models.DeleteProjectMemberRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectMemberResponse:
        """
        This API is used to delete project users.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjectMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectMemberResponse
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
        
    async def DeleteResourceGroup(
            self,
            request: models.DeleteResourceGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceGroupResponse:
        """
        This API is used to destroy resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceGroupResponse
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
        
    async def DeleteTaskFolder(
            self,
            request: models.DeleteTaskFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskFolderResponse:
        """
        Delete a data development task folder.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTaskFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTriggerTask(
            self,
            request: models.DeleteTriggerTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteTriggerTaskResponse:
        """
        Delete a workflow scheduling task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTriggerTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTriggerTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTriggerWorkflow(
            self,
            request: models.DeleteTriggerWorkflowRequest,
            opts: Dict = None,
    ) -> models.DeleteTriggerWorkflowResponse:
        """
        Deletes a workflow
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTriggerWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTriggerWorkflowResponse
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
        
    async def DeleteWorkflowPermissions(
            self,
            request: models.DeleteWorkflowPermissionsRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowPermissionsResponse:
        """
        This API is used to delete workflow folder permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflowPermissions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowPermissionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSourceAuthority(
            self,
            request: models.DescribeDataSourceAuthorityRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSourceAuthorityResponse:
        """
        View Data Source Permission.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSourceAuthority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSourceAuthorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableProject(
            self,
            request: models.DisableProjectRequest,
            opts: Dict = None,
    ) -> models.DisableProjectResponse:
        """
        Disable a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DissociateResourceGroupFromProject(
            self,
            request: models.DissociateResourceGroupFromProjectRequest,
            opts: Dict = None,
    ) -> models.DissociateResourceGroupFromProjectResponse:
        """
        This API is used to unbind the designated execution resource group from the project.
        """
        
        kwargs = {}
        kwargs["action"] = "DissociateResourceGroupFromProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DissociateResourceGroupFromProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableProject(
            self,
            request: models.EnableProjectRequest,
            opts: Dict = None,
    ) -> models.EnableProjectResponse:
        """
        Enable a project.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableProjectResponse
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
        
    async def GetCodeFolder(
            self,
            request: models.GetCodeFolderRequest,
            opts: Dict = None,
    ) -> models.GetCodeFolderResponse:
        """
        Retrieve sql folder details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetCodeFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCodeFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataBackfillPlan(
            self,
            request: models.GetDataBackfillPlanRequest,
            opts: Dict = None,
    ) -> models.GetDataBackfillPlanResponse:
        """
        Retrieve supplementary plan details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataBackfillPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataBackfillPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataSource(
            self,
            request: models.GetDataSourceRequest,
            opts: Dict = None,
    ) -> models.GetDataSourceResponse:
        """
        This API is used to view detailed information of the specified data source.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataSourceRelatedTasks(
            self,
            request: models.GetDataSourceRelatedTasksRequest,
            opts: Dict = None,
    ) -> models.GetDataSourceRelatedTasksResponse:
        """
        Query the associated task details of a data source.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataSourceRelatedTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataSourceRelatedTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMyCodeMaxPermission(
            self,
            request: models.GetMyCodeMaxPermissionRequest,
            opts: Dict = None,
    ) -> models.GetMyCodeMaxPermissionResponse:
        """
        View the current user's maximum permission scope for the CodeStudio entity.
        """
        
        kwargs = {}
        kwargs["action"] = "GetMyCodeMaxPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMyCodeMaxPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMyWorkflowMaxPermission(
            self,
            request: models.GetMyWorkflowMaxPermissionRequest,
            opts: Dict = None,
    ) -> models.GetMyWorkflowMaxPermissionResponse:
        """
        Check the current user's maximum permission scope for the workflow folder recursively.
        """
        
        kwargs = {}
        kwargs["action"] = "GetMyWorkflowMaxPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMyWorkflowMaxPermissionResponse
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
        
    async def GetOpsTriggerWorkflow(
            self,
            request: models.GetOpsTriggerWorkflowRequest,
            opts: Dict = None,
    ) -> models.GetOpsTriggerWorkflowResponse:
        """
        Query workflow task details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsTriggerWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsTriggerWorkflowResponse
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
        
    async def GetProject(
            self,
            request: models.GetProjectRequest,
            opts: Dict = None,
    ) -> models.GetProjectResponse:
        """
        This API is used to get project information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetProjectResponse
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
        
    async def GetResourceFolder(
            self,
            request: models.GetResourceFolderRequest,
            opts: Dict = None,
    ) -> models.GetResourceFolderResponse:
        """
        Query a resource file folder details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetResourceFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetResourceFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetResourceGroupMetrics(
            self,
            request: models.GetResourceGroupMetricsRequest,
            opts: Dict = None,
    ) -> models.GetResourceGroupMetricsResponse:
        """
        This API is used to view specified execution resource group monitoring metrics.
        """
        
        kwargs = {}
        kwargs["action"] = "GetResourceGroupMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetResourceGroupMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSQLFolder(
            self,
            request: models.GetSQLFolderRequest,
            opts: Dict = None,
    ) -> models.GetSQLFolderResponse:
        """
        Retrieve sql folder details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSQLFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSQLFolderResponse
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
        
    async def GetTable(
            self,
            request: models.GetTableRequest,
            opts: Dict = None,
    ) -> models.GetTableResponse:
        """
        Query table details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTableColumns(
            self,
            request: models.GetTableColumnsRequest,
            opts: Dict = None,
    ) -> models.GetTableColumnsResponse:
        """
        This API is used to obtain the list of all fields in a table.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTableColumns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTableColumnsResponse
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
        
    async def GetTaskFolder(
            self,
            request: models.GetTaskFolderRequest,
            opts: Dict = None,
    ) -> models.GetTaskFolderResponse:
        """
        Query Task Folder Details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskFolderResponse
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
        
    async def GetTriggerTask(
            self,
            request: models.GetTriggerTaskRequest,
            opts: Dict = None,
    ) -> models.GetTriggerTaskResponse:
        """
        This API is used to retrieve task details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTriggerTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTriggerTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTriggerTaskCode(
            self,
            request: models.GetTriggerTaskCodeRequest,
            opts: Dict = None,
    ) -> models.GetTriggerTaskCodeResponse:
        """
        Retrieve workflow scheduling task code.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTriggerTaskCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTriggerTaskCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTriggerTaskRun(
            self,
            request: models.GetTriggerTaskRunRequest,
            opts: Dict = None,
    ) -> models.GetTriggerTaskRunResponse:
        """
        Query task execution details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTriggerTaskRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTriggerTaskRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTriggerTaskVersion(
            self,
            request: models.GetTriggerTaskVersionRequest,
            opts: Dict = None,
    ) -> models.GetTriggerTaskVersionResponse:
        """
        Get task version list.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTriggerTaskVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTriggerTaskVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTriggerWorkflow(
            self,
            request: models.GetTriggerWorkflowRequest,
            opts: Dict = None,
    ) -> models.GetTriggerWorkflowResponse:
        """
        Retrieve workflow information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTriggerWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTriggerWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTriggerWorkflowRun(
            self,
            request: models.GetTriggerWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.GetTriggerWorkflowRunResponse:
        """
        Query workflow task details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTriggerWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTriggerWorkflowRunResponse
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
        
    async def GetWorkflowFolder(
            self,
            request: models.GetWorkflowFolderRequest,
            opts: Dict = None,
    ) -> models.GetWorkflowFolderResponse:
        """
        Query folder details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkflowFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkflowFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GrantMemberProjectRole(
            self,
            request: models.GrantMemberProjectRoleRequest,
            opts: Dict = None,
    ) -> models.GrantMemberProjectRoleResponse:
        """
        Modify project user roles.
        """
        
        kwargs = {}
        kwargs["action"] = "GrantMemberProjectRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GrantMemberProjectRoleResponse
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
        
    async def KillTriggerWorkflowRuns(
            self,
            request: models.KillTriggerWorkflowRunsRequest,
            opts: Dict = None,
    ) -> models.KillTriggerWorkflowRunsResponse:
        """
        Terminate running.
        """
        
        kwargs = {}
        kwargs["action"] = "KillTriggerWorkflowRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillTriggerWorkflowRunsResponse
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
        
    async def ListCatalog(
            self,
            request: models.ListCatalogRequest,
            opts: Dict = None,
    ) -> models.ListCatalogResponse:
        """
        Retrieve asset catalog info.
        """
        
        kwargs = {}
        kwargs["action"] = "ListCatalog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCatalogResponse
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
        
    async def ListCodePermissions(
            self,
            request: models.ListCodePermissionsRequest,
            opts: Dict = None,
    ) -> models.ListCodePermissionsResponse:
        """
        View CodeStudio entity permission.
        """
        
        kwargs = {}
        kwargs["action"] = "ListCodePermissions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCodePermissionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListColumnLineage(
            self,
            request: models.ListColumnLineageRequest,
            opts: Dict = None,
    ) -> models.ListColumnLineageResponse:
        """
        This API is used to obtain table field lineage information.
        """
        
        kwargs = {}
        kwargs["action"] = "ListColumnLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListColumnLineageResponse
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
        
    async def ListDataSources(
            self,
            request: models.ListDataSourcesRequest,
            opts: Dict = None,
    ) -> models.ListDataSourcesResponse:
        """
        This API is used to query the data source list in the designated project.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDataSources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDataSourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDatabase(
            self,
            request: models.ListDatabaseRequest,
            opts: Dict = None,
    ) -> models.ListDatabaseResponse:
        """
        This API is used to obtain asset database info.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDatabaseResponse
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
        
    async def ListDownstreamTriggerTasks(
            self,
            request: models.ListDownstreamTriggerTasksRequest,
            opts: Dict = None,
    ) -> models.ListDownstreamTriggerTasksResponse:
        """
        This API is used to retrieve direct downstream task details.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDownstreamTriggerTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDownstreamTriggerTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListLineage(
            self,
            request: models.ListLineageRequest,
            opts: Dict = None,
    ) -> models.ListLineageResponse:
        """
        This API is used to obtain asset lineage information.
        """
        
        kwargs = {}
        kwargs["action"] = "ListLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLineageResponse
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
        
    async def ListOpsTriggerWorkflows(
            self,
            request: models.ListOpsTriggerWorkflowsRequest,
            opts: Dict = None,
    ) -> models.ListOpsTriggerWorkflowsResponse:
        """
        This API is used to query the list of workflows.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOpsTriggerWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOpsTriggerWorkflowsResponse
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
        
    async def ListPermissions(
            self,
            request: models.ListPermissionsRequest,
            opts: Dict = None,
    ) -> models.ListPermissionsResponse:
        """
        Retrieve authorizable permission details.
        """
        
        kwargs = {}
        kwargs["action"] = "ListPermissions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPermissionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListProcessLineage(
            self,
            request: models.ListProcessLineageRequest,
            opts: Dict = None,
    ) -> models.ListProcessLineageResponse:
        """
        This API is used to obtain asset lineage information.
        """
        
        kwargs = {}
        kwargs["action"] = "ListProcessLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListProcessLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListProjectMembers(
            self,
            request: models.ListProjectMembersRequest,
            opts: Dict = None,
    ) -> models.ListProjectMembersResponse:
        """
        This API is used to obtain the user under the project with pagination return.
        """
        
        kwargs = {}
        kwargs["action"] = "ListProjectMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListProjectMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListProjectRoles(
            self,
            request: models.ListProjectRolesRequest,
            opts: Dict = None,
    ) -> models.ListProjectRolesResponse:
        """
        Get role list info.
        """
        
        kwargs = {}
        kwargs["action"] = "ListProjectRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListProjectRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListProjects(
            self,
            request: models.ListProjectsRequest,
            opts: Dict = None,
    ) -> models.ListProjectsResponse:
        """
        The project list in the tenant's global scope is irrelevant to the user's viewing range.
        """
        
        kwargs = {}
        kwargs["action"] = "ListProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListQualityRuleTemplates(
            self,
            request: models.ListQualityRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.ListQualityRuleTemplatesResponse:
        """
        [Filter criteria] {template Name, query usage with Keyword fuzzy matching} {template type, 1. system template 2. custom template} {quality detection dimensions (QualityDims), 1. accuracy 2. uniqueness 3. integrity 4. consistency 5. timeliness 6. validity} [Sorting field] {citation sorting type, sort ASC or DESC based on the number of references}.
        """
        
        kwargs = {}
        kwargs["action"] = "ListQualityRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListQualityRuleTemplatesResponse
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
        
    async def ListResourceGroups(
            self,
            request: models.ListResourceGroupsRequest,
            opts: Dict = None,
    ) -> models.ListResourceGroupsResponse:
        """
        This API is used to query the execution resource group list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListResourceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListResourceGroupsResponse
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
        
    async def ListSchema(
            self,
            request: models.ListSchemaRequest,
            opts: Dict = None,
    ) -> models.ListSchemaResponse:
        """
        This API is used to obtain the asset database Schema information.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTable(
            self,
            request: models.ListTableRequest,
            opts: Dict = None,
    ) -> models.ListTableResponse:
        """
        This API is used to obtain table information of assets.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTaskFolders(
            self,
            request: models.ListTaskFoldersRequest,
            opts: Dict = None,
    ) -> models.ListTaskFoldersResponse:
        """
        Query Task Folder List.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTaskFolders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTaskFoldersResponse
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
        
    async def ListTenantRoles(
            self,
            request: models.ListTenantRolesRequest,
            opts: Dict = None,
    ) -> models.ListTenantRolesResponse:
        """
        Get the role list of all root accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTenantRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTenantRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTriggerTaskVersions(
            self,
            request: models.ListTriggerTaskVersionsRequest,
            opts: Dict = None,
    ) -> models.ListTriggerTaskVersionsResponse:
        """
        Task save version list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTriggerTaskVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTriggerTaskVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTriggerTasks(
            self,
            request: models.ListTriggerTasksRequest,
            opts: Dict = None,
    ) -> models.ListTriggerTasksResponse:
        """
        Query job pagination information.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTriggerTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTriggerTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTriggerWorkflowRuns(
            self,
            request: models.ListTriggerWorkflowRunsRequest,
            opts: Dict = None,
    ) -> models.ListTriggerWorkflowRunsResponse:
        """
        Query workflow operation.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTriggerWorkflowRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTriggerWorkflowRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTriggerWorkflows(
            self,
            request: models.ListTriggerWorkflowsRequest,
            opts: Dict = None,
    ) -> models.ListTriggerWorkflowsResponse:
        """
        This API is used to query the list of workflows.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTriggerWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTriggerWorkflowsResponse
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
        
    async def ListUpstreamTriggerTasks(
            self,
            request: models.ListUpstreamTriggerTasksRequest,
            opts: Dict = None,
    ) -> models.ListUpstreamTriggerTasksResponse:
        """
        This API is used to retrieve direct upstream tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUpstreamTriggerTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUpstreamTriggerTasksResponse
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
        
    async def ListWorkflowPermissions(
            self,
            request: models.ListWorkflowPermissionsRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowPermissionsResponse:
        """
        Query workflow authorization permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflowPermissions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowPermissionsResponse
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
        
    async def RegisterLineage(
            self,
            request: models.RegisterLineageRequest,
            opts: Dict = None,
    ) -> models.RegisterLineageResponse:
        """
        RegisterLineage
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveMemberProjectRole(
            self,
            request: models.RemoveMemberProjectRoleRequest,
            opts: Dict = None,
    ) -> models.RemoveMemberProjectRoleResponse:
        """
        Delete project user roles.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveMemberProjectRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveMemberProjectRoleResponse
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
        
    async def RerunTriggerWorkflowRunAsync(
            self,
            request: models.RerunTriggerWorkflowRunAsyncRequest,
            opts: Dict = None,
    ) -> models.RerunTriggerWorkflowRunAsyncResponse:
        """
        Rerun an operation.
        """
        
        kwargs = {}
        kwargs["action"] = "RerunTriggerWorkflowRunAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RerunTriggerWorkflowRunAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokeDataSourceAuthorization(
            self,
            request: models.RevokeDataSourceAuthorizationRequest,
            opts: Dict = None,
    ) -> models.RevokeDataSourceAuthorizationResponse:
        """
        Revoke data source permission.
        """
        
        kwargs = {}
        kwargs["action"] = "RevokeDataSourceAuthorization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokeDataSourceAuthorizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokePrivileges(
            self,
            request: models.RevokePrivilegesRequest,
            opts: Dict = None,
    ) -> models.RevokePrivilegesResponse:
        """
        Authorization Revoked in Catalog mode.
        """
        
        kwargs = {}
        kwargs["action"] = "RevokePrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokePrivilegesResponse
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
        
    async def StartOpsTasks(
            self,
            request: models.StartOpsTasksRequest,
            opts: Dict = None,
    ) -> models.StartOpsTasksResponse:
        """
        Start tasks asynchronously in batch.
        """
        
        kwargs = {}
        kwargs["action"] = "StartOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartOpsTasksResponse
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
        
    async def SubmitTriggerTask(
            self,
            request: models.SubmitTriggerTaskRequest,
            opts: Dict = None,
    ) -> models.SubmitTriggerTaskResponse:
        """
        Submit a workflow scheduling task.
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTriggerTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTriggerTaskResponse
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
        
    async def UpdateDataSource(
            self,
            request: models.UpdateDataSourceRequest,
            opts: Dict = None,
    ) -> models.UpdateDataSourceResponse:
        """
        This API is used to update a data source.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataSourceResponse
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
        
    async def UpdateOpsTriggerTasksOwner(
            self,
            request: models.UpdateOpsTriggerTasksOwnerRequest,
            opts: Dict = None,
    ) -> models.UpdateOpsTriggerTasksOwnerResponse:
        """
        Query task execution details.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOpsTriggerTasksOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOpsTriggerTasksOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProject(
            self,
            request: models.UpdateProjectRequest,
            opts: Dict = None,
    ) -> models.UpdateProjectResponse:
        """
        This API is used to modify project basic information.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProjectResponse
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
        Update resource folder.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateResourceFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateResourceFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateResourceGroup(
            self,
            request: models.UpdateResourceGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateResourceGroupResponse:
        """
        This API is used to modify configurations or renew resources.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateResourceGroupResponse
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
        
    async def UpdateTaskFolder(
            self,
            request: models.UpdateTaskFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateTaskFolderResponse:
        """
        Update a task folder.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTaskFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTaskFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTaskPartially(
            self,
            request: models.UpdateTaskPartiallyRequest,
            opts: Dict = None,
    ) -> models.UpdateTaskPartiallyResponse:
        """
        This API is used to update a task.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTaskPartially"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTaskPartiallyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTriggerTask(
            self,
            request: models.UpdateTriggerTaskRequest,
            opts: Dict = None,
    ) -> models.UpdateTriggerTaskResponse:
        """
        This API is used to update a task.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTriggerTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTriggerTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTriggerTaskPartially(
            self,
            request: models.UpdateTriggerTaskPartiallyRequest,
            opts: Dict = None,
    ) -> models.UpdateTriggerTaskPartiallyResponse:
        """
        This API is used to update a task.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTriggerTaskPartially"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTriggerTaskPartiallyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTriggerWorkflow(
            self,
            request: models.UpdateTriggerWorkflowRequest,
            opts: Dict = None,
    ) -> models.UpdateTriggerWorkflowResponse:
        """
        This API is used to update workflow, including basic information and workflow parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTriggerWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTriggerWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTriggerWorkflowPartially(
            self,
            request: models.UpdateTriggerWorkflowPartiallyRequest,
            opts: Dict = None,
    ) -> models.UpdateTriggerWorkflowPartiallyResponse:
        """
        Update workflow (including basic info and workflow parameters).
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTriggerWorkflowPartially"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTriggerWorkflowPartiallyResponse
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
        Refresh workflow folder.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflowFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)