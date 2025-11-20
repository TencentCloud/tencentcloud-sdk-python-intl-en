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
from tencentcloud.eb.v20210416 import models
from typing import Dict


class EbClient(AbstractClient):
    _apiVersion = '2021-04-16'
    _endpoint = 'eb.intl.tencentcloudapi.com'
    _service = 'eb'

    async def CheckRule(
            self,
            request: models.CheckRuleRequest,
            opts: Dict = None,
    ) -> models.CheckRuleResponse:
        """
        This API is used to check a rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckTransformation(
            self,
            request: models.CheckTransformationRequest,
            opts: Dict = None,
    ) -> models.CheckTransformationResponse:
        """
        This API is used to test rules and data on the ETL configuration page.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckTransformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckTransformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConnection(
            self,
            request: models.CreateConnectionRequest,
            opts: Dict = None,
    ) -> models.CreateConnectionResponse:
        """
        This API is used to create an event connector.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEventBus(
            self,
            request: models.CreateEventBusRequest,
            opts: Dict = None,
    ) -> models.CreateEventBusResponse:
        """
        This API is used to create an event bus.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEventBus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEventBusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        This API is used to create an event rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTarget(
            self,
            request: models.CreateTargetRequest,
            opts: Dict = None,
    ) -> models.CreateTargetResponse:
        """
        This API is used to create a delivery target.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTransformation(
            self,
            request: models.CreateTransformationRequest,
            opts: Dict = None,
    ) -> models.CreateTransformationResponse:
        """
        This API is used to create a transformer.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTransformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTransformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConnection(
            self,
            request: models.DeleteConnectionRequest,
            opts: Dict = None,
    ) -> models.DeleteConnectionResponse:
        """
        This API is used to delete an event connector.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEventBus(
            self,
            request: models.DeleteEventBusRequest,
            opts: Dict = None,
    ) -> models.DeleteEventBusResponse:
        """
        This API is used to delete an event bus.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEventBus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEventBusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRule(
            self,
            request: models.DeleteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleResponse:
        """
        This API is used to delete an event rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTarget(
            self,
            request: models.DeleteTargetRequest,
            opts: Dict = None,
    ) -> models.DeleteTargetResponse:
        """
        This API is used to delete a delivery target.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTransformation(
            self,
            request: models.DeleteTransformationRequest,
            opts: Dict = None,
    ) -> models.DeleteTransformationResponse:
        """
        This API is used to delete a transformer.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTransformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTransformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogTagValue(
            self,
            request: models.DescribeLogTagValueRequest,
            opts: Dict = None,
    ) -> models.DescribeLogTagValueResponse:
        """
        This API is used to query log searching metric values.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogTagValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogTagValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetEventBus(
            self,
            request: models.GetEventBusRequest,
            opts: Dict = None,
    ) -> models.GetEventBusResponse:
        """
        This API is used to get the details of an event bus.
        """
        
        kwargs = {}
        kwargs["action"] = "GetEventBus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetEventBusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRule(
            self,
            request: models.GetRuleRequest,
            opts: Dict = None,
    ) -> models.GetRuleResponse:
        """
        This API is used to get the details of an event rule.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTransformation(
            self,
            request: models.GetTransformationRequest,
            opts: Dict = None,
    ) -> models.GetTransformationResponse:
        """
        This API is used to get the details of a transformer.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTransformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTransformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConnections(
            self,
            request: models.ListConnectionsRequest,
            opts: Dict = None,
    ) -> models.ListConnectionsResponse:
        """
        This API is used to get the list of event connectors.
        """
        
        kwargs = {}
        kwargs["action"] = "ListConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEventBuses(
            self,
            request: models.ListEventBusesRequest,
            opts: Dict = None,
    ) -> models.ListEventBusesResponse:
        """
        This API is used to get the list of event buses.
        """
        
        kwargs = {}
        kwargs["action"] = "ListEventBuses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEventBusesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRules(
            self,
            request: models.ListRulesRequest,
            opts: Dict = None,
    ) -> models.ListRulesResponse:
        """
        This API is used to get the list of event rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTargets(
            self,
            request: models.ListTargetsRequest,
            opts: Dict = None,
    ) -> models.ListTargetsResponse:
        """
        This API is used to get the list delivery targets.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchLog(
            self,
            request: models.SearchLogRequest,
            opts: Dict = None,
    ) -> models.SearchLogResponse:
        """
        This API is used to query logs.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConnection(
            self,
            request: models.UpdateConnectionRequest,
            opts: Dict = None,
    ) -> models.UpdateConnectionResponse:
        """
        This API is used to update an event connector.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEventBus(
            self,
            request: models.UpdateEventBusRequest,
            opts: Dict = None,
    ) -> models.UpdateEventBusResponse:
        """
        This API is used to update an event bus.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEventBus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEventBusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRule(
            self,
            request: models.UpdateRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateRuleResponse:
        """
        This API is used to update an event rule.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTarget(
            self,
            request: models.UpdateTargetRequest,
            opts: Dict = None,
    ) -> models.UpdateTargetResponse:
        """
        This API is used to update a delivery target.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTransformation(
            self,
            request: models.UpdateTransformationRequest,
            opts: Dict = None,
    ) -> models.UpdateTransformationResponse:
        """
        This API is used to update a transformer.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTransformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTransformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)