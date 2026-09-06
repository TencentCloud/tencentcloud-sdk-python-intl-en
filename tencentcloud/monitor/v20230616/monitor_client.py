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
from tencentcloud.monitor.v20230616 import models


class MonitorClient(AbstractClient):
    _apiVersion = '2023-06-16'
    _endpoint = 'monitor.intl.tencentcloudapi.com'
    _service = 'monitor'


    def CancelAIWorkbenchChat(self, request):
        r"""Cancel dialogue execution

        :param request: Request instance for CancelAIWorkbenchChat.
        :type request: :class:`tencentcloud.monitor.v20230616.models.CancelAIWorkbenchChatRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.CancelAIWorkbenchChatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelAIWorkbenchChat", params, headers=headers)
            response = json.loads(body)
            model = models.CancelAIWorkbenchChatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIWorkbenchAgent(self, request):
        r"""This API is used to create an Agent.

        :param request: Request instance for CreateAIWorkbenchAgent.
        :type request: :class:`tencentcloud.monitor.v20230616.models.CreateAIWorkbenchAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.CreateAIWorkbenchAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIWorkbenchAgent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIWorkbenchAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIWorkbenchTask(self, request):
        r"""Create a task

        :param request: Request instance for CreateAIWorkbenchTask.
        :type request: :class:`tencentcloud.monitor.v20230616.models.CreateAIWorkbenchTaskRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.CreateAIWorkbenchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIWorkbenchTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIWorkbenchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAIWorkbenchAgent(self, request):
        r"""Delete Agent

        :param request: Request instance for DeleteAIWorkbenchAgent.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DeleteAIWorkbenchAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DeleteAIWorkbenchAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIWorkbenchAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIWorkbenchAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAIWorkbenchTask(self, request):
        r"""This API is used to delete a task.

        :param request: Request instance for DeleteAIWorkbenchTask.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DeleteAIWorkbenchTaskRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DeleteAIWorkbenchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIWorkbenchTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIWorkbenchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchAgent(self, request):
        r"""Query Agent details.

        :param request: Request instance for DescribeAIWorkbenchAgent.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchArtifact(self, request):
        r"""Query artifact details.

        :param request: Request instance for DescribeAIWorkbenchArtifact.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchArtifactRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchArtifactResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchArtifact", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchArtifactResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchExecution(self, request):
        r"""Query execution details.

        :param request: Request instance for DescribeAIWorkbenchExecution.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchExecutionRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchExecutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchExecution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchExecutionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchSession(self, request):
        r"""Query session details

        :param request: Request instance for DescribeAIWorkbenchSession.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSessionRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchSkill(self, request):
        r"""Query skill details

        :param request: Request instance for DescribeAIWorkbenchSkill.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSkillRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchSkill", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmNotifyHistories(self, request):
        r"""Query alarm notification history as needed

        :param request: Request instance for DescribeAlarmNotifyHistories.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAlarmNotifyHistoriesRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAlarmNotifyHistoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmNotifyHistories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmNotifyHistoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAIWorkbenchArtifactDownloadURL(self, request):
        r"""Get the download URL of AI Workbench artifacts.

        :param request: Request instance for GetAIWorkbenchArtifactDownloadURL.
        :type request: :class:`tencentcloud.monitor.v20230616.models.GetAIWorkbenchArtifactDownloadURLRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.GetAIWorkbenchArtifactDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAIWorkbenchArtifactDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.GetAIWorkbenchArtifactDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchAgents(self, request):
        r"""Query the Agent list.

        :param request: Request instance for ListAIWorkbenchAgents.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchAgentsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchAgentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchAgents", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchAgentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchArtifacts(self, request):
        r"""Query the product list

        :param request: Request instance for ListAIWorkbenchArtifacts.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchArtifactsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchArtifactsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchArtifacts", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchArtifactsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchExecutions(self, request):
        r"""Query the execution list

        :param request: Request instance for ListAIWorkbenchExecutions.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchExecutionsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchExecutionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchExecutions", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchExecutionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchMCPs(self, request):
        r"""Query the MCP list.

        :param request: Request instance for ListAIWorkbenchMCPs.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchMCPsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchMCPsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchMCPs", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchMCPsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchMessages(self, request):
        r"""This API is used to query message list.

        :param request: Request instance for ListAIWorkbenchMessages.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchMessagesRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchMessages", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchMessagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchResourceInstances(self, request):
        r"""List resource instances.

        :param request: Request instance for ListAIWorkbenchResourceInstances.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchResourceInstancesRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchResourceInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchResourceInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchResourceInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchResourceMaps(self, request):
        r"""Query the list of resource maps

        :param request: Request instance for ListAIWorkbenchResourceMaps.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchResourceMapsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchResourceMapsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchResourceMaps", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchResourceMapsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchSessions(self, request):
        r"""Query session list

        :param request: Request instance for ListAIWorkbenchSessions.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchSessionsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchSessions", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchSkills(self, request):
        r"""Query the skill list

        :param request: Request instance for ListAIWorkbenchSkills.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchSkillsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchSkillsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchSkills", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchSkillsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchTasks(self, request):
        r"""This API is used to query the task list.

        :param request: Request instance for ListAIWorkbenchTasks.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchTasksRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerAIWorkbenchTask(self, request):
        r"""Manually trigger a task.

        :param request: Request instance for TriggerAIWorkbenchTask.
        :type request: :class:`tencentcloud.monitor.v20230616.models.TriggerAIWorkbenchTaskRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.TriggerAIWorkbenchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerAIWorkbenchTask", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerAIWorkbenchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAIWorkbenchAgent(self, request):
        r"""Update an Agent

        :param request: Request instance for UpdateAIWorkbenchAgent.
        :type request: :class:`tencentcloud.monitor.v20230616.models.UpdateAIWorkbenchAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.UpdateAIWorkbenchAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAIWorkbenchAgent", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAIWorkbenchAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))