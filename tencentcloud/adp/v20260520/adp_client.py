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
from tencentcloud.adp.v20260520 import models


class AdpClient(AbstractClient):
    _apiVersion = '2026-05-20'
    _endpoint = 'adp.intl.tencentcloudapi.com'
    _service = 'adp'


    def CallMCPTool(self, request):
        r"""Tool call triggered by a user in the MCP App iframe.

        :param request: Request instance for CallMCPTool.
        :type request: :class:`tencentcloud.adp.v20260520.models.CallMCPToolRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CallMCPToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CallMCPTool", params, headers=headers)
            response = json.loads(body)
            model = models.CallMCPToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckLabel(self, request):
        r"""Validate tags

        :param request: Request instance for CheckLabel.
        :type request: :class:`tencentcloud.adp.v20260520.models.CheckLabelRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CheckLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckLabel", params, headers=headers)
            response = json.loads(body)
            model = models.CheckLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyAgentFromApp(self, request):
        r"""This API is used to replicate an Agent. Currently only support claw mode.

        :param request: Request instance for CopyAgentFromApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.CopyAgentFromAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CopyAgentFromAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyAgentFromApp", params, headers=headers)
            response = json.loads(body)
            model = models.CopyAgentFromAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyApp(self, request):
        r"""Copy an application

        :param request: Request instance for CopyApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.CopyAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CopyAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyApp", params, headers=headers)
            response = json.loads(body)
            model = models.CopyAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAgent(self, request):
        r"""This API is used to create an Agent. Currently only support claw mode.

        :param request: Request instance for CreateAgent.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateAgentRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApp(self, request):
        r"""This API is used to create an application.

        :param request: Request instance for CreateApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAppTrigger(self, request):
        r"""CreateAppTrigger

        :param request: Request instance for CreateAppTrigger.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateAppTriggerRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateAppTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAppTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCategory(self, request):
        r"""Create a category

        :param request: Request instance for CreateCategory.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateCategoryRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCategory", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateChannel(self, request):
        r"""Create a channel (distinguish B-end application release channels from C-end IM channels by scene)

        :param request: Request instance for CreateChannel.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateChannelRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateChannel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConversation(self, request):
        r"""Create session

        :param request: Request instance for CreateConversation.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateConversationRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConversation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKB(self, request):
        r"""This API is used to create a knowledge base.

        :param request: Request instance for CreateKB.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateKBRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateKBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKB", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLabel(self, request):
        r"""Create a tag

        :param request: Request instance for CreateLabel.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateLabelRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLabel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMsgRecordCategory(self, request):
        r"""This API is used to create a message record category, with support for specifying the category name and parent category. A ParentId of 0 indicates a level-1 category.

        :param request: Request instance for CreateMsgRecordCategory.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateMsgRecordCategoryRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateMsgRecordCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMsgRecordCategory", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMsgRecordCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePlugin(self, request):
        r"""This API is used to query plugin details.

        :param request: Request instance for CreatePlugin.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreatePluginRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreatePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQAGenerationTask(self, request):
        r"""Create a QA generation task

        :param request: Request instance for CreateQAGenerationTask.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateQAGenerationTaskRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateQAGenerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQAGenerationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQAGenerationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQAList(self, request):
        r"""Batch create QA

        :param request: Request instance for CreateQAList.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateQAListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateQAListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQAList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQAListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRelease(self, request):
        r"""Add new release task

        :param request: Request instance for CreateRelease.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateReleaseRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRelease", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSimilarQuestion(self, request):
        r"""This API is used to create a similar question generation task.

        :param request: Request instance for CreateSimilarQuestion.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateSimilarQuestionRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateSimilarQuestionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSimilarQuestion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSimilarQuestionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSkill(self, request):
        r"""Creates a skill

        :param request: Request instance for CreateSkill.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateSkillRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSkill", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSkillShare(self, request):
        r"""Submit a custom Skill for enterprise-level shared approval (two-segment: submit, approve, callback to create a shared task)

        :param request: Request instance for CreateSkillShare.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateSkillShareRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateSkillShareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSkillShare", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSkillShareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSpace(self, request):
        r"""Create a space

        :param request: Request instance for CreateSpace.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateSpaceRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSpace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVariable(self, request):
        r"""This API is used to create parameter variables.

        :param request: Request instance for CreateVariable.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateVariableRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateVariableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVariable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVariableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWebSocketToken(self, request):
        r"""This API is used to create a WebSocket Token.

        :param request: Request instance for CreateWebSocketToken.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateWebSocketTokenRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateWebSocketTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebSocketToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWebSocketTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkflowRun(self, request):
        r"""This API is used to create an asynchronous running instance of a workflow. After successful creation, the workflow runs asynchronously in the backend. The API returns the workflow running instance ID (WorkflowRunId) and other information. You can call the DescribeWorkflowRun API to query the workflow running details.
        Note: Asynchronous execution of a workflow is application-based. The corresponding application configuration must be set to "Single Workflow Mode" before it can be successfully created.

        :param request: Request instance for CreateWorkflowRun.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateWorkflowRunRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkspaceCredential(self, request):
        r"""Create a workspace credential

        :param request: Request instance for CreateWorkspaceCredential.
        :type request: :class:`tencentcloud.adp.v20260520.models.CreateWorkspaceCredentialRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.CreateWorkspaceCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkspaceCredential", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkspaceCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAgent(self, request):
        r"""This API is used to delete an Agent.

        :param request: Request instance for DeleteAgent.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteAgentRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApp(self, request):
        r"""This API is used to delete applications

        :param request: Request instance for DeleteApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAppTrigger(self, request):
        r"""DeleteAppTrigger

        :param request: Request instance for DeleteAppTrigger.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteAppTriggerRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteAppTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAppTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCategory(self, request):
        r"""Delete a category

        :param request: Request instance for DeleteCategory.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteCategoryRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCategory", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteChannel(self, request):
        r"""Delete a channel (scenarios are distinguished by scene)

        :param request: Request instance for DeleteChannel.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteChannelRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConversation(self, request):
        r"""Delete conversation

        :param request: Request instance for DeleteConversation.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteConversationRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConversation", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDocList(self, request):
        r"""Delete documents in batches

        :param request: Request instance for DeleteDocList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteDocListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteDocListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDocList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDocListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteKB(self, request):
        r"""This API is used to delete the knowledge base.

        :param request: Request instance for DeleteKB.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteKBRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteKBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteKB", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteKBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLabelList(self, request):
        r"""Batch deletes tags

        :param request: Request instance for DeleteLabelList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteLabelListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteLabelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLabelList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLabelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMsgRecordCategory(self, request):
        r"""Deletes a specified message record category

        :param request: Request instance for DeleteMsgRecordCategory.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteMsgRecordCategoryRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteMsgRecordCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMsgRecordCategory", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMsgRecordCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePlugin(self, request):
        r"""Modify a plug-in

        :param request: Request instance for DeletePlugin.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeletePluginRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeletePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQAList(self, request):
        r"""Delete QAs in batches

        :param request: Request instance for DeleteQAList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteQAListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteQAListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQAList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQAListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSkill(self, request):
        r"""Delete a Custom Skill Authorization: creator ∨ (edit permission ∧ delete permission) Denied scenarios: non-Custom type / shared / in security detection / pending listing approval / pending delisting approval

        :param request: Request instance for DeleteSkill.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteSkillRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSkill", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSkillShare(self, request):
        r"""Submit a shared Skill delisting approval (v2, two-segment: submit → approve → callback to delist the shared Skill) Authorization: right to erasure Denied scenarios: not shared / pending listing approval / pending delisting approval

        :param request: Request instance for DeleteSkillShare.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteSkillShareRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteSkillShareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSkillShare", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSkillShareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSpace(self, request):
        r"""Delete a space

        :param request: Request instance for DeleteSpace.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteSpaceRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSpace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVariable(self, request):
        r"""Delete a parameter variable

        :param request: Request instance for DeleteVariable.
        :type request: :class:`tencentcloud.adp.v20260520.models.DeleteVariableRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DeleteVariableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVariable", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVariableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountList(self, request):
        r"""View the employee list of a business

        :param request: Request instance for DescribeAccountList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAccountListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAccountListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentDetail(self, request):
        r"""Query Agent details

        :param request: Request instance for DescribeAgentDetail.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAgentDetailRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAgentDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentReleasePreviewList(self, request):
        r"""Get the release preview list of agents under an application

        :param request: Request instance for DescribeAgentReleasePreviewList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAgentReleasePreviewListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAgentReleasePreviewListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentReleasePreviewList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentReleasePreviewListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentSummaryList(self, request):
        r"""Queries the abstract information list of an Agent.

        :param request: Request instance for DescribeAgentSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAgentSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAgentSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApp(self, request):
        r"""This API is used to obtain application information.

        :param request: Request instance for DescribeApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppStatisticsOverview(self, request):
        r"""This API is used to query the invocation statistics overview under an application view, including the total number of calls, call success rate, avg duration of total tokens, and avg duration of first tokens. For RAG applications, it also returns the count and proportion of calls for each response method for drawing a pie chart.

        :param request: Request instance for DescribeAppStatisticsOverview.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAppStatisticsOverviewRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAppStatisticsOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppStatisticsOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppStatisticsOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppSummaryList(self, request):
        r"""Retrieve the abstract list of applications.

        :param request: Request instance for DescribeAppSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAppSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAppSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppTrigger(self, request):
        r"""DescribeAppTrigger

        :param request: Request instance for DescribeAppTrigger.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAppTriggerRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAppTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppTriggerInstance(self, request):
        r"""DescribeAppTriggerInstance

        :param request: Request instance for DescribeAppTriggerInstance.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAppTriggerInstanceRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAppTriggerInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppTriggerInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppTriggerInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppTriggerRunLogList(self, request):
        r"""DescribeAppTriggerRunLogList

        :param request: Request instance for DescribeAppTriggerRunLogList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAppTriggerRunLogListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAppTriggerRunLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppTriggerRunLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppTriggerRunLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppTriggerSummaryList(self, request):
        r"""DescribeAppTriggerSummaryList

        :param request: Request instance for DescribeAppTriggerSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAppTriggerSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAppTriggerSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppTriggerSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppTriggerSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditLogList(self, request):
        r"""View operation log list

        :param request: Request instance for DescribeAuditLogList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeAuditLogListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeAuditLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCategoryList(self, request):
        r"""Query the classification list

        :param request: Request instance for DescribeCategoryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeCategoryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConcurrencyLimitDetailList(self, request):
        r"""Query concurrency overrun details, including QPM/TPM overruns and exclusive concurrency overruns. Return the overrun time, space, app, model, and request content.

        :param request: Request instance for DescribeConcurrencyLimitDetailList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeConcurrencyLimitDetailListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeConcurrencyLimitDetailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConcurrencyLimitDetailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConcurrencyLimitDetailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConflictQA(self, request):
        r"""Queries the conflict query details

        :param request: Request instance for DescribeConflictQA.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeConflictQARequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeConflictQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConflictQA", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConflictQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConflictQASummaryList(self, request):
        r"""Query the conflict list

        :param request: Request instance for DescribeConflictQASummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeConflictQASummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeConflictQASummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConflictQASummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConflictQASummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConversation(self, request):
        r"""View session information.

        :param request: Request instance for DescribeConversation.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeConversationRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConversation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConversationList(self, request):
        r"""Get session list.

        :param request: Request instance for DescribeConversationList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeConversationListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeConversationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConversationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConversationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConversationMessageList(self, request):
        r"""Get historical messages of a conversation.

        :param request: Request instance for DescribeConversationMessageList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeConversationMessageListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeConversationMessageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConversationMessageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConversationMessageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLabel(self, request):
        r"""Queries tag details.

        :param request: Request instance for DescribeLabel.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeLabelRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLabelSummaryList(self, request):
        r"""Querying the Tag List

        :param request: Request instance for DescribeLabelSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeLabelSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeLabelSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLabelSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLabelSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLatestRelease(self, request):
        r"""Pull the latest release info (including release time, status, and channel).

        :param request: Request instance for DescribeLatestRelease.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeLatestReleaseRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeLatestReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLatestRelease", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLatestReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelList(self, request):
        r"""Query the model list

        :param request: Request instance for DescribeModelList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeModelListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeModelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMsgRecordCategoryList(self, request):
        r"""Query the message record category tree of an app, return categories and subcategories, number of records under each category, and operation permissions.

        :param request: Request instance for DescribeMsgRecordCategoryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeMsgRecordCategoryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeMsgRecordCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMsgRecordCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMsgRecordCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeBatchRun(self, request):
        r"""DescribeNodeBatchRun

        :param request: Request instance for DescribeNodeBatchRun.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeNodeBatchRunRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeNodeBatchRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeBatchRun", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeBatchRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeRunDetail(self, request):
        r"""View workflow node running details.

        :param request: Request instance for DescribeNodeRunDetail.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeNodeRunDetailRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeNodeRunDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeRunDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeRunDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlugin(self, request):
        r"""This API is used to query plugin details.

        :param request: Request instance for DescribePlugin.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribePluginRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePluginSummaryList(self, request):
        r"""Querying the List of Plugins

        :param request: Request instance for DescribePluginSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribePluginSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribePluginSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePluginSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQA(self, request):
        r"""Query QA details

        :param request: Request instance for DescribeQA.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeQARequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQA", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQASummaryList(self, request):
        r"""Queries the QA list

        :param request: Request instance for DescribeQASummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeQASummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeQASummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQASummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQASummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseList(self, request):
        r"""Release record list

        :param request: Request instance for DescribeReleaseList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeReleaseListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeReleaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseSummary(self, request):
        r"""Queries a publication task

        :param request: Request instance for DescribeReleaseSummary.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeReleaseSummaryRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeReleaseSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillCategoryList(self, request):
        r"""Query the Skill classification list

        :param request: Request instance for DescribeSkillCategoryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSkillCategoryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSkillCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillReferenceList(self, request):
        r"""This API is used to query the list of details where a certain Skill is referenced, grouped by SkillRefType: OpenClaw, cloud agent, or business assistant agent. Authentication: same as DescribeSkillDetail.

        :param request: Request instance for DescribeSkillReferenceList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSkillReferenceListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSkillReferenceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillReferenceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillReferenceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillSummaryList(self, request):
        r"""Query the Skill list

        :param request: Request instance for DescribeSkillSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSkillSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSkillSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpaceList(self, request):
        r"""This API is used to obtain the space list.

        :param request: Request instance for DescribeSpaceList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSpaceListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSpaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSystemVariableList(self, request):
        r"""Obtain system variables

        :param request: Request instance for DescribeSystemVariableList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeSystemVariableListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeSystemVariableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemVariableList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSystemVariableListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsageSummaryList(self, request):
        r"""This API is used to query aggregated details of resource usage, including three types of resources: models, plug-ins, and platforms. It displays indicators such as call count and Token consumption, aggregated by space or application dimension.

        :param request: Request instance for DescribeUsageSummaryList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeUsageSummaryListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeUsageSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsageSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsageSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVariable(self, request):
        r"""Get parameter variables

        :param request: Request instance for DescribeVariable.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeVariableRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeVariableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVariable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVariableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVariableList(self, request):
        r"""Gets the parameter variable list

        :param request: Request instance for DescribeVariableList.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeVariableListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeVariableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVariableList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVariableListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowRun(self, request):
        r"""Queries workflow running details.

        :param request: Request instance for DescribeWorkflowRun.
        :type request: :class:`tencentcloud.adp.v20260520.models.DescribeWorkflowRunRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.DescribeWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportQA(self, request):
        r"""Asynchronously export QAs.

        :param request: Request instance for ExportQA.
        :type request: :class:`tencentcloud.adp.v20260520.models.ExportQARequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ExportQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportQA", params, headers=headers)
            response = json.loads(body)
            model = models.ExportQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgent(self, request):
        r"""Modify Agent configuration information

        :param request: Request instance for ModifyAgent.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyAgentRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgent", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApp(self, request):
        r"""Modifies applications

        :param request: Request instance for ModifyApp.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyAppRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAppTrigger(self, request):
        r"""ModifyAppTrigger

        :param request: Request instance for ModifyAppTrigger.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyAppTriggerRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyAppTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAppTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAppTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConversation(self, request):
        r"""Modify session information.

        :param request: Request instance for ModifyConversation.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyConversationRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConversation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDocList(self, request):
        r"""Batch modify documents.

        :param request: Request instance for ModifyDocList.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyDocListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyDocListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDocList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDocListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyKB(self, request):
        r"""This API is used to modify the knowledge base.

        :param request: Request instance for ModifyKB.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyKBRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyKBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyKB", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyKBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLabel(self, request):
        r"""Modify a tag

        :param request: Request instance for ModifyLabel.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyLabelRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLabel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQA(self, request):
        r"""Modify single QA

        :param request: Request instance for ModifyQA.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyQARequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQA", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQAList(self, request):
        r"""Batch modify QAs

        :param request: Request instance for ModifyQAList.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyQAListRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyQAListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQAList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQAListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySpace(self, request):
        r"""Edit a space

        :param request: Request instance for ModifySpace.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifySpaceRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifySpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySpace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVariable(self, request):
        r"""Update parameter variables

        :param request: Request instance for ModifyVariable.
        :type request: :class:`tencentcloud.adp.v20260520.models.ModifyVariableRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModifyVariableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVariable", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVariableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseAppTrigger(self, request):
        r"""PauseAppTrigger

        :param request: Request instance for PauseAppTrigger.
        :type request: :class:`tencentcloud.adp.v20260520.models.PauseAppTriggerRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.PauseAppTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseAppTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.PauseAppTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseSkill(self, request):
        r"""This API is used to list a skill.

        :param request: Request instance for ReleaseSkill.
        :type request: :class:`tencentcloud.adp.v20260520.models.ReleaseSkillRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ReleaseSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseSkill", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetConversation(self, request):
        r"""Reset a session
        Note: Resetting is not supported for the current Claw mode application session.

        :param request: Request instance for ResetConversation.
        :type request: :class:`tencentcloud.adp.v20260520.models.ResetConversationRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.ResetConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetConversation", params, headers=headers)
            response = json.loads(body)
            model = models.ResetConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryRelease(self, request):
        r"""Retry publishing (republish after suspension)

        :param request: Request instance for RetryRelease.
        :type request: :class:`tencentcloud.adp.v20260520.models.RetryReleaseRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.RetryReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryRelease", params, headers=headers)
            response = json.loads(body)
            model = models.RetryReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackRelease(self, request):
        r"""Roll back a release

        :param request: Request instance for RollbackRelease.
        :type request: :class:`tencentcloud.adp.v20260520.models.RollbackReleaseRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.RollbackReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackRelease", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunAppTriggerNow(self, request):
        r"""RunAppTriggerNow

        :param request: Request instance for RunAppTriggerNow.
        :type request: :class:`tencentcloud.adp.v20260520.models.RunAppTriggerNowRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.RunAppTriggerNowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunAppTriggerNow", params, headers=headers)
            response = json.loads(body)
            model = models.RunAppTriggerNowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchKnowledge(self, request):
        r"""Knowledge retrieval

        :param request: Request instance for SearchKnowledge.
        :type request: :class:`tencentcloud.adp.v20260520.models.SearchKnowledgeRequest`
        :rtype: :class:`tencentcloud.adp.v20260520.models.SearchKnowledgeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchKnowledge", params, headers=headers)
            response = json.loads(body)
            model = models.SearchKnowledgeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))