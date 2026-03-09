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
from tencentcloud.wedata.v20250806 import models


class WedataClient(AbstractClient):
    _apiVersion = '2025-08-06'
    _endpoint = 'wedata.intl.tencentcloudapi.com'
    _service = 'wedata'


    def AddCalcEnginesToProject(self, request):
        r"""Associate a project cluster.

        :param request: Request instance for AddCalcEnginesToProject.
        :type request: :class:`tencentcloud.wedata.v20250806.models.AddCalcEnginesToProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AddCalcEnginesToProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCalcEnginesToProject", params, headers=headers)
            response = json.loads(body)
            model = models.AddCalcEnginesToProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateResourceGroupToProject(self, request):
        r"""This API is used to bind the designated execution resource group to the project.

        :param request: Request instance for AssociateResourceGroupToProject.
        :type request: :class:`tencentcloud.wedata.v20250806.models.AssociateResourceGroupToProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AssociateResourceGroupToProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateResourceGroupToProject", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateResourceGroupToProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AuthorizeDataSource(self, request):
        r"""Authorize a data source.

        :param request: Request instance for AuthorizeDataSource.
        :type request: :class:`tencentcloud.wedata.v20250806.models.AuthorizeDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AuthorizeDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuthorizeDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.AuthorizeDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AuthorizePrivileges(self, request):
        r"""Authorization in Catalog mode.

        :param request: Request instance for AuthorizePrivileges.
        :type request: :class:`tencentcloud.wedata.v20250806.models.AuthorizePrivilegesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AuthorizePrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuthorizePrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.AuthorizePrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCodeFile(self, request):
        r"""This API is used to create a code file.

        :param request: Request instance for CreateCodeFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateCodeFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateCodeFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodeFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCodeFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCodeFolder(self, request):
        r"""This API is used to create a code folder.

        :param request: Request instance for CreateCodeFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateCodeFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateCodeFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodeFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCodeFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCodePermissions(self, request):
        r"""Configure CodeStudio entity permission.

        :param request: Request instance for CreateCodePermissions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateCodePermissionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateCodePermissionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodePermissions", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCodePermissionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataBackfillPlan(self, request):
        r"""This API is used to create a data backfill plan.

        :param request: Request instance for CreateDataBackfillPlan.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateDataBackfillPlanRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateDataBackfillPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataBackfillPlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataBackfillPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataSource(self, request):
        r"""This API is used to create a data source in the designated project.

        :param request: Request instance for CreateDataSource.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOpsAlarmRule(self, request):
        r"""This API is used to set alarm rules.

        :param request: Request instance for CreateOpsAlarmRule.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateOpsAlarmRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateOpsAlarmRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpsAlarmRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpsAlarmRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProject(self, request):
        r"""Create a project with cluster information upon creation.

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProjectMember(self, request):
        r"""Add project user role.

        :param request: Request instance for CreateProjectMember.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateProjectMemberRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateProjectMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProjectMember", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProjectMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourceFile(self, request):
        r"""This API is used to create a resource file.

        :param request: Request instance for CreateResourceFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourceFolder(self, request):
        r"""This API is used to create a resource file folder.

        :param request: Request instance for CreateResourceFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourceFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourceGroup(self, request):
        r"""This API is used to purchase resources.

        :param request: Request instance for CreateResourceGroup.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateResourceGroupRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSQLFolder(self, request):
        r"""This API is used to create an SQL folder

        :param request: Request instance for CreateSQLFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateSQLFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateSQLFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSQLFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSQLFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSQLScript(self, request):
        r"""This API is used to add an SQL script.

        :param request: Request instance for CreateSQLScript.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateSQLScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateSQLScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSQLScript", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSQLScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTask(self, request):
        r"""This API is used to create a task.

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskFolder(self, request):
        r"""Create a folder.

        :param request: Request instance for CreateTaskFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateTaskFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTriggerTask(self, request):
        r"""This API is used to create a task.

        :param request: Request instance for CreateTriggerTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateTriggerTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTriggerTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTriggerTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTriggerTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTriggerWorkflow(self, request):
        r"""create workflow.

        :param request: Request instance for CreateTriggerWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateTriggerWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTriggerWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTriggerWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTriggerWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkflow(self, request):
        r"""This API is used to create workflow.

        :param request: Request instance for CreateWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkflowFolder(self, request):
        r"""This API is used to create a workflow folder.

        :param request: Request instance for CreateWorkflowFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflowFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkflowPermissions(self, request):
        r"""This API is used to configure data development permissions.

        :param request: Request instance for CreateWorkflowPermissions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowPermissionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowPermissionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflowPermissions", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowPermissionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCodeFile(self, request):
        r"""This API is used to delete a code file.

        :param request: Request instance for DeleteCodeFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteCodeFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteCodeFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCodeFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCodeFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCodeFolder(self, request):
        r"""This API is used to delete folders in data exploration.

        :param request: Request instance for DeleteCodeFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteCodeFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteCodeFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCodeFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCodeFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCodePermissions(self, request):
        r"""Delete CodeStudio entity permission.

        :param request: Request instance for DeleteCodePermissions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteCodePermissionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteCodePermissionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCodePermissions", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCodePermissionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataBackfillPlanAsync(self, request):
        r"""Delete a replenishment plan.

        :param request: Request instance for DeleteDataBackfillPlanAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteDataBackfillPlanAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteDataBackfillPlanAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataBackfillPlanAsync", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataBackfillPlanAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataSource(self, request):
        r"""This API is used to delete a data source.

        :param request: Request instance for DeleteDataSource.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLineage(self, request):
        r"""RegisterLineage

        :param request: Request instance for DeleteLineage.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLineage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOpsAlarmRule(self, request):
        r"""Deletes alarm rules

        :param request: Request instance for DeleteOpsAlarmRule.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteOpsAlarmRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteOpsAlarmRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOpsAlarmRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOpsAlarmRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        r"""This API is used to delete a project.

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProjectMember(self, request):
        r"""This API is used to delete project users.

        :param request: Request instance for DeleteProjectMember.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteProjectMemberRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteProjectMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProjectMember", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceFile(self, request):
        r"""This API is used to delete a resource file.

        :param request: Request instance for DeleteResourceFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceFolder(self, request):
        r"""This API is used to delete a resource folder.

        :param request: Request instance for DeleteResourceFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceGroup(self, request):
        r"""This API is used to destroy resources.

        :param request: Request instance for DeleteResourceGroup.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceGroupRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSQLFolder(self, request):
        r"""This API is used to delete a SQL folder.

        :param request: Request instance for DeleteSQLFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteSQLFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteSQLFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSQLFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSQLFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSQLScript(self, request):
        r"""This API is used to delete an SQL script.

        :param request: Request instance for DeleteSQLScript.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteSQLScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteSQLScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSQLScript", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSQLScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTask(self, request):
        r"""This API is used to delete an orchestration space task.

        :param request: Request instance for DeleteTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTaskFolder(self, request):
        r"""Delete a data development task folder.

        :param request: Request instance for DeleteTaskFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteTaskFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteTaskFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTriggerTask(self, request):
        r"""Delete a workflow scheduling task.

        :param request: Request instance for DeleteTriggerTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteTriggerTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteTriggerTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTriggerTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTriggerTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTriggerWorkflow(self, request):
        r"""Deletes a workflow

        :param request: Request instance for DeleteTriggerWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteTriggerWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteTriggerWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTriggerWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTriggerWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkflow(self, request):
        r"""Deletes a workflow

        :param request: Request instance for DeleteWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkflowFolder(self, request):
        r"""This API is used to delete a data development folder

        :param request: Request instance for DeleteWorkflowFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflowFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkflowPermissions(self, request):
        r"""This API is used to delete workflow folder permissions.

        :param request: Request instance for DeleteWorkflowPermissions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowPermissionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowPermissionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflowPermissions", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowPermissionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSourceAuthority(self, request):
        r"""View Data Source Permission.

        :param request: Request instance for DescribeDataSourceAuthority.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DescribeDataSourceAuthorityRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DescribeDataSourceAuthorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSourceAuthority", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceAuthorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableProject(self, request):
        r"""Disable a project.

        :param request: Request instance for DisableProject.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DisableProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DisableProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableProject", params, headers=headers)
            response = json.loads(body)
            model = models.DisableProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DissociateResourceGroupFromProject(self, request):
        r"""This API is used to unbind the designated execution resource group from the project.

        :param request: Request instance for DissociateResourceGroupFromProject.
        :type request: :class:`tencentcloud.wedata.v20250806.models.DissociateResourceGroupFromProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DissociateResourceGroupFromProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DissociateResourceGroupFromProject", params, headers=headers)
            response = json.loads(body)
            model = models.DissociateResourceGroupFromProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableProject(self, request):
        r"""Enable a project.

        :param request: Request instance for EnableProject.
        :type request: :class:`tencentcloud.wedata.v20250806.models.EnableProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.EnableProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableProject", params, headers=headers)
            response = json.loads(body)
            model = models.EnableProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAlarmMessage(self, request):
        r"""This API is used to query alert information details.

        :param request: Request instance for GetAlarmMessage.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetAlarmMessageRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetAlarmMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAlarmMessage", params, headers=headers)
            response = json.loads(body)
            model = models.GetAlarmMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCodeFile(self, request):
        r"""This API is used to view code file details.

        :param request: Request instance for GetCodeFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetCodeFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetCodeFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCodeFile", params, headers=headers)
            response = json.loads(body)
            model = models.GetCodeFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCodeFolder(self, request):
        r"""Retrieve sql folder details.

        :param request: Request instance for GetCodeFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetCodeFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetCodeFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCodeFolder", params, headers=headers)
            response = json.loads(body)
            model = models.GetCodeFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDataBackfillPlan(self, request):
        r"""Retrieve supplementary plan details.

        :param request: Request instance for GetDataBackfillPlan.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetDataBackfillPlanRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetDataBackfillPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDataBackfillPlan", params, headers=headers)
            response = json.loads(body)
            model = models.GetDataBackfillPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDataSource(self, request):
        r"""This API is used to view detailed information of the specified data source.

        :param request: Request instance for GetDataSource.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.GetDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDataSourceRelatedTasks(self, request):
        r"""Query the associated task details of a data source.

        :param request: Request instance for GetDataSourceRelatedTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetDataSourceRelatedTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetDataSourceRelatedTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDataSourceRelatedTasks", params, headers=headers)
            response = json.loads(body)
            model = models.GetDataSourceRelatedTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMyCodeMaxPermission(self, request):
        r"""View the current user's maximum permission scope for the CodeStudio entity.

        :param request: Request instance for GetMyCodeMaxPermission.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetMyCodeMaxPermissionRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetMyCodeMaxPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMyCodeMaxPermission", params, headers=headers)
            response = json.loads(body)
            model = models.GetMyCodeMaxPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMyWorkflowMaxPermission(self, request):
        r"""Check the current user's maximum permission scope for the workflow folder recursively.

        :param request: Request instance for GetMyWorkflowMaxPermission.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetMyWorkflowMaxPermissionRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetMyWorkflowMaxPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMyWorkflowMaxPermission", params, headers=headers)
            response = json.loads(body)
            model = models.GetMyWorkflowMaxPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsAlarmRule(self, request):
        r"""This API is used to query alert rule information based on alarm rule id or name.

        :param request: Request instance for GetOpsAlarmRule.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsAlarmRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsAlarmRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsAlarmRule", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsAlarmRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsAsyncJob(self, request):
        r"""This API is used to query async operation details in Ops center.

        :param request: Request instance for GetOpsAsyncJob.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsAsyncJobRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsAsyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsAsyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsAsyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsTask(self, request):
        r"""Obtaining Task Details

        :param request: Request instance for GetOpsTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsTask", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsTaskCode(self, request):
        r"""This API is used to retrieve task code.

        :param request: Request instance for GetOpsTaskCode.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsTaskCodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsTaskCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsTaskCode", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsTaskCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsTriggerWorkflow(self, request):
        r"""Query workflow task details.

        :param request: Request instance for GetOpsTriggerWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsTriggerWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsTriggerWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsTriggerWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsTriggerWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOpsWorkflow(self, request):
        r"""This API is used to obtain workflow scheduling details based on the workflow id.

        :param request: Request instance for GetOpsWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetOpsWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetOpsWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOpsWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.GetOpsWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetProject(self, request):
        r"""This API is used to get project information.

        :param request: Request instance for GetProject.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetProject", params, headers=headers)
            response = json.loads(body)
            model = models.GetProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetResourceFile(self, request):
        r"""This API is used to obtain resource file details.

        :param request: Request instance for GetResourceFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.GetResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetResourceFolder(self, request):
        r"""Query a resource file folder details.

        :param request: Request instance for GetResourceFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetResourceFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetResourceFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetResourceFolder", params, headers=headers)
            response = json.loads(body)
            model = models.GetResourceFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetResourceGroupMetrics(self, request):
        r"""This API is used to view specified execution resource group monitoring metrics.

        :param request: Request instance for GetResourceGroupMetrics.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetResourceGroupMetricsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetResourceGroupMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetResourceGroupMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.GetResourceGroupMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSQLFolder(self, request):
        r"""Retrieve sql folder details.

        :param request: Request instance for GetSQLFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetSQLFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetSQLFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSQLFolder", params, headers=headers)
            response = json.loads(body)
            model = models.GetSQLFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSQLScript(self, request):
        r"""This API is used to query script details.

        :param request: Request instance for GetSQLScript.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetSQLScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetSQLScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSQLScript", params, headers=headers)
            response = json.loads(body)
            model = models.GetSQLScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTable(self, request):
        r"""Query table details.

        :param request: Request instance for GetTable.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTableRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTable", params, headers=headers)
            response = json.loads(body)
            model = models.GetTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTableColumns(self, request):
        r"""This API is used to obtain the list of all fields in a table.

        :param request: Request instance for GetTableColumns.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTableColumnsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTableColumnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTableColumns", params, headers=headers)
            response = json.loads(body)
            model = models.GetTableColumnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTask(self, request):
        r"""This API is used to retrieve task details.

        :param request: Request instance for GetTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTask", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskCode(self, request):
        r"""This API is used to obtain task code.

        :param request: Request instance for GetTaskCode.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskCodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskCode", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskFolder(self, request):
        r"""Query Task Folder Details.

        :param request: Request instance for GetTaskFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskFolder", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskInstance(self, request):
        r"""This API is used to query the details of a scheduling instance.

        :param request: Request instance for GetTaskInstance.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskInstanceRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskInstance", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskInstanceLog(self, request):
        r"""This API is used to obtain instance lists.

        :param request: Request instance for GetTaskInstanceLog.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskInstanceLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskInstanceLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskInstanceLog", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskInstanceLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskVersion(self, request):
        r"""This API is used to list task versions.

        :param request: Request instance for GetTaskVersion.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTaskVersionRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTaskVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskVersion", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTriggerTask(self, request):
        r"""This API is used to retrieve task details.

        :param request: Request instance for GetTriggerTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTriggerTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTriggerTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTriggerTask", params, headers=headers)
            response = json.loads(body)
            model = models.GetTriggerTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTriggerTaskCode(self, request):
        r"""Retrieve workflow scheduling task code.

        :param request: Request instance for GetTriggerTaskCode.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTriggerTaskCodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTriggerTaskCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTriggerTaskCode", params, headers=headers)
            response = json.loads(body)
            model = models.GetTriggerTaskCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTriggerTaskRun(self, request):
        r"""Query task execution details.

        :param request: Request instance for GetTriggerTaskRun.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTriggerTaskRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTriggerTaskRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTriggerTaskRun", params, headers=headers)
            response = json.loads(body)
            model = models.GetTriggerTaskRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTriggerTaskVersion(self, request):
        r"""Get task version list.

        :param request: Request instance for GetTriggerTaskVersion.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTriggerTaskVersionRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTriggerTaskVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTriggerTaskVersion", params, headers=headers)
            response = json.loads(body)
            model = models.GetTriggerTaskVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTriggerWorkflow(self, request):
        r"""Retrieve workflow information.

        :param request: Request instance for GetTriggerWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTriggerWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTriggerWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTriggerWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.GetTriggerWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTriggerWorkflowRun(self, request):
        r"""Query workflow task details.

        :param request: Request instance for GetTriggerWorkflowRun.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetTriggerWorkflowRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetTriggerWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTriggerWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.GetTriggerWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWorkflow(self, request):
        r"""This API is used to retrieve workflow information.

        :param request: Request instance for GetWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.GetWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWorkflowFolder(self, request):
        r"""Query folder details.

        :param request: Request instance for GetWorkflowFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GetWorkflowFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GetWorkflowFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWorkflowFolder", params, headers=headers)
            response = json.loads(body)
            model = models.GetWorkflowFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GrantMemberProjectRole(self, request):
        r"""Modify project user roles.

        :param request: Request instance for GrantMemberProjectRole.
        :type request: :class:`tencentcloud.wedata.v20250806.models.GrantMemberProjectRoleRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.GrantMemberProjectRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GrantMemberProjectRole", params, headers=headers)
            response = json.loads(body)
            model = models.GrantMemberProjectRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillTaskInstancesAsync(self, request):
        r"""This API is used to terminate instances in batches asynchronously.

        :param request: Request instance for KillTaskInstancesAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.KillTaskInstancesAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.KillTaskInstancesAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillTaskInstancesAsync", params, headers=headers)
            response = json.loads(body)
            model = models.KillTaskInstancesAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillTriggerWorkflowRuns(self, request):
        r"""Terminate running.

        :param request: Request instance for KillTriggerWorkflowRuns.
        :type request: :class:`tencentcloud.wedata.v20250806.models.KillTriggerWorkflowRunsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.KillTriggerWorkflowRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillTriggerWorkflowRuns", params, headers=headers)
            response = json.loads(body)
            model = models.KillTriggerWorkflowRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAlarmMessages(self, request):
        r"""This API is used to search the alarm information list.

        :param request: Request instance for ListAlarmMessages.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListAlarmMessagesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListAlarmMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAlarmMessages", params, headers=headers)
            response = json.loads(body)
            model = models.ListAlarmMessagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCatalog(self, request):
        r"""Retrieve asset catalog info.

        :param request: Request instance for ListCatalog.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListCatalogRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListCatalogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCatalog", params, headers=headers)
            response = json.loads(body)
            model = models.ListCatalogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCodeFolderContents(self, request):
        r"""This API is used to get folder content.

        :param request: Request instance for ListCodeFolderContents.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListCodeFolderContentsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListCodeFolderContentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCodeFolderContents", params, headers=headers)
            response = json.loads(body)
            model = models.ListCodeFolderContentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCodePermissions(self, request):
        r"""View CodeStudio entity permission.

        :param request: Request instance for ListCodePermissions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListCodePermissionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListCodePermissionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCodePermissions", params, headers=headers)
            response = json.loads(body)
            model = models.ListCodePermissionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListColumnLineage(self, request):
        r"""This API is used to obtain table field lineage information.

        :param request: Request instance for ListColumnLineage.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListColumnLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListColumnLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListColumnLineage", params, headers=headers)
            response = json.loads(body)
            model = models.ListColumnLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDataBackfillInstances(self, request):
        r"""This API is used to retrieve all instances of a single backfill.

        :param request: Request instance for ListDataBackfillInstances.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDataBackfillInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDataBackfillInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDataBackfillInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListDataBackfillInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDataSources(self, request):
        r"""This API is used to query the data source list in the designated project.

        :param request: Request instance for ListDataSources.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDataSourcesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDataSourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDataSources", params, headers=headers)
            response = json.loads(body)
            model = models.ListDataSourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDatabase(self, request):
        r"""This API is used to obtain asset database info.

        :param request: Request instance for ListDatabase.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDatabaseRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.ListDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDownstreamOpsTasks(self, request):
        r"""This API is used to retrieve task direct downstream details.

        :param request: Request instance for ListDownstreamOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDownstreamOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListDownstreamOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDownstreamTaskInstances(self, request):
        r"""This API is used to get the direct upstream of an instance.

        :param request: Request instance for ListDownstreamTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDownstreamTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListDownstreamTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDownstreamTasks(self, request):
        r"""This API is used to retrieve the direct downstream task details.

        :param request: Request instance for ListDownstreamTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDownstreamTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListDownstreamTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDownstreamTriggerTasks(self, request):
        r"""This API is used to retrieve direct downstream task details.

        :param request: Request instance for ListDownstreamTriggerTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamTriggerTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListDownstreamTriggerTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDownstreamTriggerTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListDownstreamTriggerTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListLineage(self, request):
        r"""This API is used to obtain asset lineage information.

        :param request: Request instance for ListLineage.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLineage", params, headers=headers)
            response = json.loads(body)
            model = models.ListLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOpsAlarmRules(self, request):
        r"""This API is used to query the alarm rule list.

        :param request: Request instance for ListOpsAlarmRules.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListOpsAlarmRulesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListOpsAlarmRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOpsAlarmRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListOpsAlarmRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOpsTasks(self, request):
        r"""This API is used to obtain the task list based on the project id.

        :param request: Request instance for ListOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOpsTriggerWorkflows(self, request):
        r"""This API is used to query the list of workflows.

        :param request: Request instance for ListOpsTriggerWorkflows.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListOpsTriggerWorkflowsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListOpsTriggerWorkflowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOpsTriggerWorkflows", params, headers=headers)
            response = json.loads(body)
            model = models.ListOpsTriggerWorkflowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOpsWorkflows(self, request):
        r"""Get Workflows under a Project by Project ID.

        :param request: Request instance for ListOpsWorkflows.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListOpsWorkflowsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListOpsWorkflowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOpsWorkflows", params, headers=headers)
            response = json.loads(body)
            model = models.ListOpsWorkflowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListPermissions(self, request):
        r"""Retrieve authorizable permission details.

        :param request: Request instance for ListPermissions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListPermissionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListPermissionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPermissions", params, headers=headers)
            response = json.loads(body)
            model = models.ListPermissionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListProcessLineage(self, request):
        r"""This API is used to obtain asset lineage information.

        :param request: Request instance for ListProcessLineage.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListProcessLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListProcessLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListProcessLineage", params, headers=headers)
            response = json.loads(body)
            model = models.ListProcessLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListProjectMembers(self, request):
        r"""This API is used to obtain the user under the project with pagination return.

        :param request: Request instance for ListProjectMembers.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListProjectMembersRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListProjectMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListProjectMembers", params, headers=headers)
            response = json.loads(body)
            model = models.ListProjectMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListProjectRoles(self, request):
        r"""Get role list info.

        :param request: Request instance for ListProjectRoles.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListProjectRolesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListProjectRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListProjectRoles", params, headers=headers)
            response = json.loads(body)
            model = models.ListProjectRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListProjects(self, request):
        r"""The project list in the tenant's global scope is irrelevant to the user's viewing range.

        :param request: Request instance for ListProjects.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListProjectsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListProjects", params, headers=headers)
            response = json.loads(body)
            model = models.ListProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListQualityRuleTemplates(self, request):
        r"""[Filter criteria] {template Name, query usage with Keyword fuzzy matching} {template type, 1. system template 2. custom template} {quality detection dimensions (QualityDims), 1. accuracy 2. uniqueness 3. integrity 4. consistency 5. timeliness 6. validity} [Sorting field] {citation sorting type, sort ASC or DESC based on the number of references}.

        :param request: Request instance for ListQualityRuleTemplates.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListQualityRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListQualityRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListQualityRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ListQualityRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListResourceFiles(self, request):
        r"""This API is used to view resource file list

        :param request: Request instance for ListResourceFiles.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListResourceFilesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListResourceFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListResourceFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ListResourceFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListResourceFolders(self, request):
        r"""This API is used to query the resource file folder list.

        :param request: Request instance for ListResourceFolders.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListResourceFoldersRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListResourceFoldersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListResourceFolders", params, headers=headers)
            response = json.loads(body)
            model = models.ListResourceFoldersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListResourceGroups(self, request):
        r"""This API is used to query the execution resource group list.

        :param request: Request instance for ListResourceGroups.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListResourceGroupsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListResourceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListResourceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ListResourceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSQLFolderContents(self, request):
        r"""This API is used to retrieve the content list of an sql folder

        :param request: Request instance for ListSQLFolderContents.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListSQLFolderContentsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListSQLFolderContentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSQLFolderContents", params, headers=headers)
            response = json.loads(body)
            model = models.ListSQLFolderContentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSQLScriptRuns(self, request):
        r"""This API is used to query SQL run history.

        :param request: Request instance for ListSQLScriptRuns.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListSQLScriptRunsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListSQLScriptRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSQLScriptRuns", params, headers=headers)
            response = json.loads(body)
            model = models.ListSQLScriptRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSchema(self, request):
        r"""This API is used to obtain the asset database Schema information.

        :param request: Request instance for ListSchema.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListSchemaRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListSchemaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSchema", params, headers=headers)
            response = json.loads(body)
            model = models.ListSchemaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTable(self, request):
        r"""This API is used to obtain table information of assets.

        :param request: Request instance for ListTable.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTableRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTable", params, headers=headers)
            response = json.loads(body)
            model = models.ListTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTaskFolders(self, request):
        r"""Query Task Folder List.

        :param request: Request instance for ListTaskFolders.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTaskFoldersRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskFoldersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTaskFolders", params, headers=headers)
            response = json.loads(body)
            model = models.ListTaskFoldersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTaskInstanceExecutions(self, request):
        r"""This API is used to query the details of a scheduling instance.

        :param request: Request instance for ListTaskInstanceExecutions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTaskInstanceExecutionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskInstanceExecutionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTaskInstanceExecutions", params, headers=headers)
            response = json.loads(body)
            model = models.ListTaskInstanceExecutionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTaskInstances(self, request):
        r"""This API is used to obtain instance lists.

        :param request: Request instance for ListTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTaskVersions(self, request):
        r"""This API is used to list saved task versions.

        :param request: Request instance for ListTaskVersions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTaskVersionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTaskVersions", params, headers=headers)
            response = json.loads(body)
            model = models.ListTaskVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTasks(self, request):
        r"""This API is used to query pagination information of tasks.

        :param request: Request instance for ListTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTenantRoles(self, request):
        r"""Get the role list of all root accounts.

        :param request: Request instance for ListTenantRoles.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTenantRolesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTenantRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTenantRoles", params, headers=headers)
            response = json.loads(body)
            model = models.ListTenantRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTriggerTaskVersions(self, request):
        r"""Task save version list.

        :param request: Request instance for ListTriggerTaskVersions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTriggerTaskVersionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTriggerTaskVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTriggerTaskVersions", params, headers=headers)
            response = json.loads(body)
            model = models.ListTriggerTaskVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTriggerTasks(self, request):
        r"""Query job pagination information.

        :param request: Request instance for ListTriggerTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTriggerTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTriggerTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTriggerTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListTriggerTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTriggerWorkflowRuns(self, request):
        r"""Query workflow operation.

        :param request: Request instance for ListTriggerWorkflowRuns.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTriggerWorkflowRunsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTriggerWorkflowRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTriggerWorkflowRuns", params, headers=headers)
            response = json.loads(body)
            model = models.ListTriggerWorkflowRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTriggerWorkflows(self, request):
        r"""This API is used to query the list of workflows.

        :param request: Request instance for ListTriggerWorkflows.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListTriggerWorkflowsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTriggerWorkflowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTriggerWorkflows", params, headers=headers)
            response = json.loads(body)
            model = models.ListTriggerWorkflowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUpstreamOpsTasks(self, request):
        r"""This API is used to retrieve task direct upstream.

        :param request: Request instance for ListUpstreamOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUpstreamOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListUpstreamOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUpstreamTaskInstances(self, request):
        r"""This API is used to get the direct upstream of an instance.

        :param request: Request instance for ListUpstreamTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUpstreamTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListUpstreamTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUpstreamTasks(self, request):
        r"""This API is used to retrieve the direct upstream task.

        :param request: Request instance for ListUpstreamTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUpstreamTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListUpstreamTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUpstreamTriggerTasks(self, request):
        r"""This API is used to retrieve direct upstream tasks.

        :param request: Request instance for ListUpstreamTriggerTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamTriggerTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListUpstreamTriggerTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUpstreamTriggerTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListUpstreamTriggerTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflowFolders(self, request):
        r"""This API is used to query the folder list.

        :param request: Request instance for ListWorkflowFolders.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowFoldersRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowFoldersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflowFolders", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowFoldersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflowPermissions(self, request):
        r"""Query workflow authorization permissions.

        :param request: Request instance for ListWorkflowPermissions.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowPermissionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowPermissionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflowPermissions", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowPermissionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflows(self, request):
        r"""This API is used to query the list of workflows.

        :param request: Request instance for ListWorkflows.
        :type request: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowsRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflows", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseOpsTasksAsync(self, request):
        r"""This API is used to pause tasks in batches asynchronously.

        :param request: Request instance for PauseOpsTasksAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.PauseOpsTasksAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.PauseOpsTasksAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseOpsTasksAsync", params, headers=headers)
            response = json.loads(body)
            model = models.PauseOpsTasksAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterLineage(self, request):
        r"""RegisterLineage

        :param request: Request instance for RegisterLineage.
        :type request: :class:`tencentcloud.wedata.v20250806.models.RegisterLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.RegisterLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterLineage", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveMemberProjectRole(self, request):
        r"""Delete project user roles.

        :param request: Request instance for RemoveMemberProjectRole.
        :type request: :class:`tencentcloud.wedata.v20250806.models.RemoveMemberProjectRoleRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.RemoveMemberProjectRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveMemberProjectRole", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveMemberProjectRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RerunTaskInstancesAsync(self, request):
        r"""This API is used to batch rerun instances asynchronously.

        :param request: Request instance for RerunTaskInstancesAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.RerunTaskInstancesAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.RerunTaskInstancesAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunTaskInstancesAsync", params, headers=headers)
            response = json.loads(body)
            model = models.RerunTaskInstancesAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RerunTriggerWorkflowRunAsync(self, request):
        r"""Rerun an operation.

        :param request: Request instance for RerunTriggerWorkflowRunAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.RerunTriggerWorkflowRunAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.RerunTriggerWorkflowRunAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunTriggerWorkflowRunAsync", params, headers=headers)
            response = json.loads(body)
            model = models.RerunTriggerWorkflowRunAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevokeDataSourceAuthorization(self, request):
        r"""Revoke data source permission.

        :param request: Request instance for RevokeDataSourceAuthorization.
        :type request: :class:`tencentcloud.wedata.v20250806.models.RevokeDataSourceAuthorizationRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.RevokeDataSourceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokeDataSourceAuthorization", params, headers=headers)
            response = json.loads(body)
            model = models.RevokeDataSourceAuthorizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevokePrivileges(self, request):
        r"""Authorization Revoked in Catalog mode.

        :param request: Request instance for RevokePrivileges.
        :type request: :class:`tencentcloud.wedata.v20250806.models.RevokePrivilegesRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.RevokePrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokePrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.RevokePrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunSQLScript(self, request):
        r"""This API is used to run an SQL script.

        :param request: Request instance for RunSQLScript.
        :type request: :class:`tencentcloud.wedata.v20250806.models.RunSQLScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.RunSQLScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunSQLScript", params, headers=headers)
            response = json.loads(body)
            model = models.RunSQLScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetSuccessTaskInstancesAsync(self, request):
        r"""This API is used to batch configure instances asynchronously.

        :param request: Request instance for SetSuccessTaskInstancesAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.SetSuccessTaskInstancesAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SetSuccessTaskInstancesAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetSuccessTaskInstancesAsync", params, headers=headers)
            response = json.loads(body)
            model = models.SetSuccessTaskInstancesAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartOpsTasks(self, request):
        r"""Start tasks asynchronously in batch.

        :param request: Request instance for StartOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20250806.models.StartOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.StartOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.StartOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopOpsTasksAsync(self, request):
        r"""This API is used to asynchronously deactivate tasks in batch.

        :param request: Request instance for StopOpsTasksAsync.
        :type request: :class:`tencentcloud.wedata.v20250806.models.StopOpsTasksAsyncRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.StopOpsTasksAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopOpsTasksAsync", params, headers=headers)
            response = json.loads(body)
            model = models.StopOpsTasksAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopSQLScriptRun(self, request):
        r"""This API is used to stop running an SQL script.

        :param request: Request instance for StopSQLScriptRun.
        :type request: :class:`tencentcloud.wedata.v20250806.models.StopSQLScriptRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.StopSQLScriptRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopSQLScriptRun", params, headers=headers)
            response = json.loads(body)
            model = models.StopSQLScriptRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTask(self, request):
        r"""This API is used to submit a task.

        :param request: Request instance for SubmitTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.SubmitTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SubmitTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTriggerTask(self, request):
        r"""Submit a workflow scheduling task.

        :param request: Request instance for SubmitTriggerTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.SubmitTriggerTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SubmitTriggerTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTriggerTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTriggerTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCodeFile(self, request):
        r"""This API is used to update a code file.

        :param request: Request instance for UpdateCodeFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateCodeFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateCodeFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCodeFile", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCodeFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCodeFolder(self, request):
        r"""This API is used to rename a code folder.

        :param request: Request instance for UpdateCodeFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateCodeFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateCodeFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCodeFolder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCodeFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDataSource(self, request):
        r"""This API is used to update a data source.

        :param request: Request instance for UpdateDataSource.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOpsAlarmRule(self, request):
        r"""Modifies alarm rules

        :param request: Request instance for UpdateOpsAlarmRule.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateOpsAlarmRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateOpsAlarmRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOpsAlarmRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOpsAlarmRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOpsTasksOwner(self, request):
        r"""This API is used to modify the task owner.

        :param request: Request instance for UpdateOpsTasksOwner.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateOpsTasksOwnerRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateOpsTasksOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOpsTasksOwner", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOpsTasksOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOpsTriggerTasksOwner(self, request):
        r"""Query task execution details.

        :param request: Request instance for UpdateOpsTriggerTasksOwner.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateOpsTriggerTasksOwnerRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateOpsTriggerTasksOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOpsTriggerTasksOwner", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOpsTriggerTasksOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateProject(self, request):
        r"""This API is used to modify project basic information.

        :param request: Request instance for UpdateProject.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProject", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateResourceFile(self, request):
        r"""This API is used to update a resource file.

        :param request: Request instance for UpdateResourceFile.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateResourceFolder(self, request):
        r"""Update resource folder.

        :param request: Request instance for UpdateResourceFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateResourceFolder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateResourceFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateResourceGroup(self, request):
        r"""This API is used to modify configurations or renew resources.

        :param request: Request instance for UpdateResourceGroup.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceGroupRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSQLFolder(self, request):
        r"""This API is used to rename an SQL folder.

        :param request: Request instance for UpdateSQLFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateSQLFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateSQLFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSQLFolder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSQLFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSQLScript(self, request):
        r"""This API is used to save the script content for data exploration.

        :param request: Request instance for UpdateSQLScript.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateSQLScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateSQLScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSQLScript", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSQLScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTask(self, request):
        r"""This API is used to update a task.

        :param request: Request instance for UpdateTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTask", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTaskFolder(self, request):
        r"""Update a task folder.

        :param request: Request instance for UpdateTaskFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTaskFolder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTaskFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTaskPartially(self, request):
        r"""This API is used to update a task.

        :param request: Request instance for UpdateTaskPartially.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskPartiallyRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskPartiallyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTaskPartially", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTaskPartiallyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTriggerTask(self, request):
        r"""This API is used to update a task.

        :param request: Request instance for UpdateTriggerTask.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateTriggerTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTriggerTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTriggerTask", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTriggerTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTriggerTaskPartially(self, request):
        r"""This API is used to update a task.

        :param request: Request instance for UpdateTriggerTaskPartially.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateTriggerTaskPartiallyRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTriggerTaskPartiallyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTriggerTaskPartially", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTriggerTaskPartiallyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTriggerWorkflow(self, request):
        r"""This API is used to update workflow, including basic information and workflow parameters.

        :param request: Request instance for UpdateTriggerWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateTriggerWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTriggerWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTriggerWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTriggerWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTriggerWorkflowPartially(self, request):
        r"""Update workflow (including basic info and workflow parameters).

        :param request: Request instance for UpdateTriggerWorkflowPartially.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateTriggerWorkflowPartiallyRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTriggerWorkflowPartiallyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTriggerWorkflowPartially", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTriggerWorkflowPartiallyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkflow(self, request):
        r"""This API is used to update a workflow including basic information and workflow parameters.

        :param request: Request instance for UpdateWorkflow.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkflowFolder(self, request):
        r"""Refresh workflow folder.

        :param request: Request instance for UpdateWorkflowFolder.
        :type request: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkflowFolder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkflowFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))