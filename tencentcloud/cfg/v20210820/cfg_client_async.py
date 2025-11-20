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
from tencentcloud.cfg.v20210820 import models
from typing import Dict


class CfgClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'cfg.intl.tencentcloudapi.com'
    _service = 'cfg'

    async def CreateTaskFromAction(
            self,
            request: models.CreateTaskFromActionRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFromActionResponse:
        """
        This API is used to create an experiment with an action.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFromAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFromActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskFromTemplate(
            self,
            request: models.CreateTaskFromTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFromTemplateResponse:
        """
        This API is used to create an experiment using a template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFromTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFromTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTask(
            self,
            request: models.DeleteTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskResponse:
        """
        This API is used to delete a task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActionFieldConfigList(
            self,
            request: models.DescribeActionFieldConfigListRequest,
            opts: Dict = None,
    ) -> models.DescribeActionFieldConfigListResponse:
        """
        This API is used to obtain the dynamic configuration parameters of the action field based on action ID, including action-specific parameters and common parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActionFieldConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActionFieldConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActionLibraryList(
            self,
            request: models.DescribeActionLibraryListRequest,
            opts: Dict = None,
    ) -> models.DescribeActionLibraryListResponse:
        """
        This API is used to obtain the action list of Chaotic Fault Generator.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActionLibraryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActionLibraryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeObjectTypeList(
            self,
            request: models.DescribeObjectTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeObjectTypeListResponse:
        """
        This API is used to query the object type list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeObjectTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeObjectTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTask(
            self,
            request: models.DescribeTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResponse:
        """
        This API is used to query a task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskExecuteLogs(
            self,
            request: models.DescribeTaskExecuteLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskExecuteLogsResponse:
        """
        This API is used to obtain all logs generated during an experiment.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskExecuteLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskExecuteLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskList(
            self,
            request: models.DescribeTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskListResponse:
        """
        This API is used to query the task list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskPolicyTriggerLog(
            self,
            request: models.DescribeTaskPolicyTriggerLogRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskPolicyTriggerLogResponse:
        """
        This API is used to obtain the guardrail triggering logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskPolicyTriggerLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskPolicyTriggerLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplate(
            self,
            request: models.DescribeTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateResponse:
        """
        This API is used to query a template library.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplateList(
            self,
            request: models.DescribeTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateListResponse:
        """
        This API is used to query the template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteTask(
            self,
            request: models.ExecuteTaskRequest,
            opts: Dict = None,
    ) -> models.ExecuteTaskResponse:
        """
        This API is used to run a task.
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteTaskInstance(
            self,
            request: models.ExecuteTaskInstanceRequest,
            opts: Dict = None,
    ) -> models.ExecuteTaskInstanceResponse:
        """
        This API is used to trigger the action of the chaos engineering experiment and perform an experiment on the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteTaskInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteTaskInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskRunStatus(
            self,
            request: models.ModifyTaskRunStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskRunStatusResponse:
        """
        This API is used to change the task running status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskRunStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskRunStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerPolicy(
            self,
            request: models.TriggerPolicyRequest,
            opts: Dict = None,
    ) -> models.TriggerPolicyResponse:
        """
        This API is used to trigger the chaos engineering experiment guardrail (two types: trigger and recovery).
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)