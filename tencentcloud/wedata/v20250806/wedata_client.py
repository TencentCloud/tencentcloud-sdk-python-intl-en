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
        r"""This API is used to update a resource folder.

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
        r"""This API is used to update a workflow folder

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