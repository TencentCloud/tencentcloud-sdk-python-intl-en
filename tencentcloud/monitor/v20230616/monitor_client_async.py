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
from tencentcloud.monitor.v20230616 import models
from typing import Dict


class MonitorClient(AbstractClient):
    _apiVersion = '2023-06-16'
    _endpoint = 'monitor.intl.tencentcloudapi.com'
    _service = 'monitor'

    async def CancelAIWorkbenchChat(
            self,
            request: models.CancelAIWorkbenchChatRequest,
            opts: Dict = None,
    ) -> models.CancelAIWorkbenchChatResponse:
        """
        Cancel dialogue execution
        """
        
        kwargs = {}
        kwargs["action"] = "CancelAIWorkbenchChat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelAIWorkbenchChatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIWorkbenchAgent(
            self,
            request: models.CreateAIWorkbenchAgentRequest,
            opts: Dict = None,
    ) -> models.CreateAIWorkbenchAgentResponse:
        """
        This API is used to create an Agent.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIWorkbenchAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIWorkbenchAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIWorkbenchTask(
            self,
            request: models.CreateAIWorkbenchTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAIWorkbenchTaskResponse:
        """
        Create a task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIWorkbenchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIWorkbenchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIWorkbenchAgent(
            self,
            request: models.DeleteAIWorkbenchAgentRequest,
            opts: Dict = None,
    ) -> models.DeleteAIWorkbenchAgentResponse:
        """
        Delete Agent
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIWorkbenchAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIWorkbenchAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIWorkbenchTask(
            self,
            request: models.DeleteAIWorkbenchTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteAIWorkbenchTaskResponse:
        """
        This API is used to delete a task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIWorkbenchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIWorkbenchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchAgent(
            self,
            request: models.DescribeAIWorkbenchAgentRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchAgentResponse:
        """
        Query Agent details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchArtifact(
            self,
            request: models.DescribeAIWorkbenchArtifactRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchArtifactResponse:
        """
        Query artifact details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchArtifact"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchArtifactResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchExecution(
            self,
            request: models.DescribeAIWorkbenchExecutionRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchExecutionResponse:
        """
        Query execution details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchExecution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchExecutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchSession(
            self,
            request: models.DescribeAIWorkbenchSessionRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchSessionResponse:
        """
        Query session details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchSkill(
            self,
            request: models.DescribeAIWorkbenchSkillRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchSkillResponse:
        """
        Query skill details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchSkill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchSkillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNotifyHistories(
            self,
            request: models.DescribeAlarmNotifyHistoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNotifyHistoriesResponse:
        """
        Query alarm notification history as needed
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNotifyHistories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNotifyHistoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAIWorkbenchArtifactDownloadURL(
            self,
            request: models.GetAIWorkbenchArtifactDownloadURLRequest,
            opts: Dict = None,
    ) -> models.GetAIWorkbenchArtifactDownloadURLResponse:
        """
        Get the download URL of AI Workbench artifacts.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAIWorkbenchArtifactDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAIWorkbenchArtifactDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchAgents(
            self,
            request: models.ListAIWorkbenchAgentsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchAgentsResponse:
        """
        Query the Agent list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchAgents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchAgentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchArtifacts(
            self,
            request: models.ListAIWorkbenchArtifactsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchArtifactsResponse:
        """
        Query the product list
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchArtifacts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchArtifactsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchExecutions(
            self,
            request: models.ListAIWorkbenchExecutionsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchExecutionsResponse:
        """
        Query the execution list
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchExecutions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchExecutionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchMCPs(
            self,
            request: models.ListAIWorkbenchMCPsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchMCPsResponse:
        """
        Query the MCP list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchMCPs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchMCPsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchMessages(
            self,
            request: models.ListAIWorkbenchMessagesRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchMessagesResponse:
        """
        This API is used to query message list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchMessages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchMessagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchResourceInstances(
            self,
            request: models.ListAIWorkbenchResourceInstancesRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchResourceInstancesResponse:
        """
        List resource instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchResourceInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchResourceInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchResourceMaps(
            self,
            request: models.ListAIWorkbenchResourceMapsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchResourceMapsResponse:
        """
        Query the list of resource maps
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchResourceMaps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchResourceMapsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchSessions(
            self,
            request: models.ListAIWorkbenchSessionsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchSessionsResponse:
        """
        Query session list
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchSessions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchSessionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchSkills(
            self,
            request: models.ListAIWorkbenchSkillsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchSkillsResponse:
        """
        Query the skill list
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchSkills"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchSkillsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchTasks(
            self,
            request: models.ListAIWorkbenchTasksRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchTasksResponse:
        """
        This API is used to query the task list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerAIWorkbenchTask(
            self,
            request: models.TriggerAIWorkbenchTaskRequest,
            opts: Dict = None,
    ) -> models.TriggerAIWorkbenchTaskResponse:
        """
        Manually trigger a task.
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerAIWorkbenchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerAIWorkbenchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAIWorkbenchAgent(
            self,
            request: models.UpdateAIWorkbenchAgentRequest,
            opts: Dict = None,
    ) -> models.UpdateAIWorkbenchAgentResponse:
        """
        Update an Agent
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAIWorkbenchAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAIWorkbenchAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)