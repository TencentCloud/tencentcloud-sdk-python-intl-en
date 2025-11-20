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
from tencentcloud.trabbit.v20230418 import models
from typing import Dict


class TrabbitClient(AbstractClient):
    _apiVersion = '2023-04-18'
    _endpoint = 'trabbit.intl.tencentcloudapi.com'
    _service = 'trabbit'

    async def CreateRabbitMQServerlessBinding(
            self,
            request: models.CreateRabbitMQServerlessBindingRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQServerlessBindingResponse:
        """
        This API is used to create RabbitMQ binding relationships.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQServerlessBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQServerlessBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQServerlessExchange(
            self,
            request: models.CreateRabbitMQServerlessExchangeRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQServerlessExchangeResponse:
        """
        This API is used to create a RabbitMQ exchange.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQServerlessExchange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQServerlessExchangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQServerlessQueue(
            self,
            request: models.CreateRabbitMQServerlessQueueRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQServerlessQueueResponse:
        """
        This API is used to create an RabbitMQ queue.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQServerlessQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQServerlessQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQServerlessUser(
            self,
            request: models.CreateRabbitMQServerlessUserRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQServerlessUserResponse:
        """
        This API is used to create a user for RabbitMQ.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQServerlessUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQServerlessUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQServerlessVirtualHost(
            self,
            request: models.CreateRabbitMQServerlessVirtualHostRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQServerlessVirtualHostResponse:
        """
        This API is used to create a vhost for RabbitMQ.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQServerlessVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQServerlessVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQServerlessBinding(
            self,
            request: models.DeleteRabbitMQServerlessBindingRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQServerlessBindingResponse:
        """
        This API is used to unbind RabbitMQ binding relationships.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQServerlessBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQServerlessBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQServerlessExchange(
            self,
            request: models.DeleteRabbitMQServerlessExchangeRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQServerlessExchangeResponse:
        """
        This API is used to delete the RabbitMQ exchange.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQServerlessExchange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQServerlessExchangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQServerlessPermission(
            self,
            request: models.DeleteRabbitMQServerlessPermissionRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQServerlessPermissionResponse:
        """
        This API is used to delete the permission of RabbitMQ.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQServerlessPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQServerlessPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQServerlessQueue(
            self,
            request: models.DeleteRabbitMQServerlessQueueRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQServerlessQueueResponse:
        """
        This API is used to delete an RabbitMQ queue.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQServerlessQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQServerlessQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQServerlessUser(
            self,
            request: models.DeleteRabbitMQServerlessUserRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQServerlessUserResponse:
        """
        This API is used to delete the user of RabbitMQ.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQServerlessUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQServerlessUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQServerlessVirtualHost(
            self,
            request: models.DeleteRabbitMQServerlessVirtualHostRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQServerlessVirtualHostResponse:
        """
        This API is used to delete a vhost for RabbitMQ.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQServerlessVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQServerlessVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessBindings(
            self,
            request: models.DescribeRabbitMQServerlessBindingsRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessBindingsResponse:
        """
        This API is used to retrieve the binding relationship list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessConnection(
            self,
            request: models.DescribeRabbitMQServerlessConnectionRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessConnectionResponse:
        """
        This API is used to query RabbitMQ connection list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessConsumers(
            self,
            request: models.DescribeRabbitMQServerlessConsumersRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessConsumersResponse:
        """
        This API is used to query RabbitMQ queue consumer list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessConsumers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessConsumersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessExchangeDetail(
            self,
            request: models.DescribeRabbitMQServerlessExchangeDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessExchangeDetailResponse:
        """
        This API is used to query RabbitMQ exchange details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessExchangeDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessExchangeDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessExchanges(
            self,
            request: models.DescribeRabbitMQServerlessExchangesRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessExchangesResponse:
        """
        This API is used to query the list of RabbitMQ exchanges.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessExchanges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessExchangesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessInstance(
            self,
            request: models.DescribeRabbitMQServerlessInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessInstanceResponse:
        """
        This API is used to retrieve dedicated instance information for a single RabbitMQ.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessPermission(
            self,
            request: models.DescribeRabbitMQServerlessPermissionRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessPermissionResponse:
        """
        This API is used to query RabbitMQ permission list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessQueueDetail(
            self,
            request: models.DescribeRabbitMQServerlessQueueDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessQueueDetailResponse:
        """
        This API is used to query RabbitMQ queue details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessQueueDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessQueueDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessQueues(
            self,
            request: models.DescribeRabbitMQServerlessQueuesRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessQueuesResponse:
        """
        This API is used to query a RabbitMQ queue list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessQueues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessQueuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessUser(
            self,
            request: models.DescribeRabbitMQServerlessUserRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessUserResponse:
        """
        This API is used to query RabbitMQ user list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQServerlessVirtualHost(
            self,
            request: models.DescribeRabbitMQServerlessVirtualHostRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQServerlessVirtualHostResponse:
        """
        This API is used to query a RabbitMQ vhost list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQServerlessVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQServerlessVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRabbitMQServerlessInstances(
            self,
            request: models.ListRabbitMQServerlessInstancesRequest,
            opts: Dict = None,
    ) -> models.ListRabbitMQServerlessInstancesResponse:
        """
        This API is used to obtain instance lists.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRabbitMQServerlessInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRabbitMQServerlessInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQServerlessExchange(
            self,
            request: models.ModifyRabbitMQServerlessExchangeRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQServerlessExchangeResponse:
        """
        This API is used to modify the RabbitMQ exchange.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQServerlessExchange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQServerlessExchangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQServerlessInstance(
            self,
            request: models.ModifyRabbitMQServerlessInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQServerlessInstanceResponse:
        """
        This API is used to modify cluster information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQServerlessInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQServerlessInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQServerlessPermission(
            self,
            request: models.ModifyRabbitMQServerlessPermissionRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQServerlessPermissionResponse:
        """
        This API is used to modify the permission of RabbitMQ.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQServerlessPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQServerlessPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQServerlessQueue(
            self,
            request: models.ModifyRabbitMQServerlessQueueRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQServerlessQueueResponse:
        """
        This API is used to modify an RabbitMQ queue.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQServerlessQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQServerlessQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQServerlessUser(
            self,
            request: models.ModifyRabbitMQServerlessUserRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQServerlessUserResponse:
        """
        This API is used to modify the user of RabbitMQ.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQServerlessUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQServerlessUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQServerlessVirtualHost(
            self,
            request: models.ModifyRabbitMQServerlessVirtualHostRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQServerlessVirtualHostResponse:
        """
        This API is used to modify a vhost for RabbitMQ.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQServerlessVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQServerlessVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)