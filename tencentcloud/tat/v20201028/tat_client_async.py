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
from tencentcloud.tat.v20201028 import models
from typing import Dict


class TatClient(AbstractClient):
    _apiVersion = '2020-10-28'
    _endpoint = 'tat.intl.tencentcloudapi.com'
    _service = 'tat'

    async def CancelInvocation(
            self,
            request: models.CancelInvocationRequest,
            opts: Dict = None,
    ) -> models.CancelInvocationResponse:
        """
        This API is used to cancel the command executed on one or more CVM instances.

        * If the command has not been delivered to the TAT agent, the task status is `PENDING`, `DELIVERING`, or `DELIVER_DELAYED`, and will be `CANCELLED` after the command is canceled.
        * If the command has been delivered to the TAT agent, the task status is `RUNNING`, and will be `TERMINATED` after the command is canceled.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelInvocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelInvocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCommand(
            self,
            request: models.CreateCommandRequest,
            opts: Dict = None,
    ) -> models.CreateCommandResponse:
        """
        This API is used to create a command.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInvoker(
            self,
            request: models.CreateInvokerRequest,
            opts: Dict = None,
    ) -> models.CreateInvokerResponse:
        """
        This API is used to create an invoker.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInvoker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInvokerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCommand(
            self,
            request: models.DeleteCommandRequest,
            opts: Dict = None,
    ) -> models.DeleteCommandResponse:
        """
        This API is used to delete a command.
        Commands bound to an invoker cannot be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInvoker(
            self,
            request: models.DeleteInvokerRequest,
            opts: Dict = None,
    ) -> models.DeleteInvokerResponse:
        """
        This API is used to delete an invoker.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInvoker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInvokerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutomationAgentStatus(
            self,
            request: models.DescribeAutomationAgentStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeAutomationAgentStatusResponse:
        """
        This API is used to query the status of the TAT agent.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutomationAgentStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutomationAgentStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCommands(
            self,
            request: models.DescribeCommandsRequest,
            opts: Dict = None,
    ) -> models.DescribeCommandsResponse:
        """
        This API is used to query command details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCommands"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCommandsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvocationTasks(
            self,
            request: models.DescribeInvocationTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeInvocationTasksResponse:
        """
        This API is used to query execution task details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvocationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvocationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvocations(
            self,
            request: models.DescribeInvocationsRequest,
            opts: Dict = None,
    ) -> models.DescribeInvocationsResponse:
        """
        This API is used to query execution activity details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvocations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvocationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvokerRecords(
            self,
            request: models.DescribeInvokerRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeInvokerRecordsResponse:
        """
        This API is used to query the execution history of an invoker.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvokerRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvokerRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvokers(
            self,
            request: models.DescribeInvokersRequest,
            opts: Dict = None,
    ) -> models.DescribeInvokersResponse:
        """
        This API is used to query invoker details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvokers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvokersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        This API is used to query the list of regions that supports TAT.
        If the `RegionState` is `AVAILABLE`, it means that TAT is available in the region. If no value is returned, TAT is not available in the region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableInvoker(
            self,
            request: models.DisableInvokerRequest,
            opts: Dict = None,
    ) -> models.DisableInvokerResponse:
        """
        This API is used to disable an invoker.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableInvoker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableInvokerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableInvoker(
            self,
            request: models.EnableInvokerRequest,
            opts: Dict = None,
    ) -> models.EnableInvokerResponse:
        """
        This API is used to enable an invoker.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableInvoker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableInvokerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeCommand(
            self,
            request: models.InvokeCommandRequest,
            opts: Dict = None,
    ) -> models.InvokeCommandResponse:
        """
        This API is used to trigger a command on the specified instance and returns the execution activity ID (inv-xxxxxxxx) on success. Each execution activity has one or more execution tasks (invt-xxxxxxxx) and each execution task indicates an execution record on a CVM or Lighthouse instance.

        * If the agent is not installed on the instance or is offline, an error is returned.
        * If the command type is not supported by the agent runtime environment, an error is returned.
        * The specified instance needs to be in a VPC network.
        * The specified instance needs to be in the RUNNING status.
        * Only one type of instances (CVM or Lighthouse) can be specified in a single request.
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCommand(
            self,
            request: models.ModifyCommandRequest,
            opts: Dict = None,
    ) -> models.ModifyCommandResponse:
        """
        This API is used to modify a command.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInvoker(
            self,
            request: models.ModifyInvokerRequest,
            opts: Dict = None,
    ) -> models.ModifyInvokerResponse:
        """
        This API is used to modify an invoker.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInvoker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInvokerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PreviewReplacedCommandContent(
            self,
            request: models.PreviewReplacedCommandContentRequest,
            opts: Dict = None,
    ) -> models.PreviewReplacedCommandContentResponse:
        """
        This API is used to preview the command with custom parameters. The command is not executed.
        """
        
        kwargs = {}
        kwargs["action"] = "PreviewReplacedCommandContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PreviewReplacedCommandContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunCommand(
            self,
            request: models.RunCommandRequest,
            opts: Dict = None,
    ) -> models.RunCommandResponse:
        """
        This API is used to execute a command and returns the execution activity ID (inv-xxxxxxxx) on success. Each execution has one or more execution tasks (invt-xxxxxxxx) and each execution task indicates an execution record on a CVM or Lighthouse instance.

        * If the agent is not installed on the instance or is offline, an error is returned.
        * If the command type is not supported by the agent runtime environment, an error is returned.
        * The specified instance needs to be in a VPC network.
        * The specified instance needs to be in the `RUNNING` status.
        * Only one type of instances (CVM or Lighthouse) can be specified in a single request.
        """
        
        kwargs = {}
        kwargs["action"] = "RunCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)