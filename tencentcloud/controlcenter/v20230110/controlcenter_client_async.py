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
from tencentcloud.controlcenter.v20230110 import models
from typing import Dict


class ControlcenterClient(AbstractClient):
    _apiVersion = '2023-01-10'
    _endpoint = 'controlcenter.intl.tencentcloudapi.com'
    _service = 'controlcenter'

    async def BatchApplyAccountBaselines(
            self,
            request: models.BatchApplyAccountBaselinesRequest,
            opts: Dict = None,
    ) -> models.BatchApplyAccountBaselinesResponse:
        """
        This API is used to apply baselines to existing accounts in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchApplyAccountBaselines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchApplyAccountBaselinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAccountFactoryBaseline(
            self,
            request: models.GetAccountFactoryBaselineRequest,
            opts: Dict = None,
    ) -> models.GetAccountFactoryBaselineResponse:
        """
        This API is used to retrieve user baseline configuration data.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAccountFactoryBaseline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAccountFactoryBaselineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAccountFactoryBaselineItems(
            self,
            request: models.ListAccountFactoryBaselineItemsRequest,
            opts: Dict = None,
    ) -> models.ListAccountFactoryBaselineItemsResponse:
        """
        This API is used to obtain account factory system baseline items.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAccountFactoryBaselineItems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAccountFactoryBaselineItemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDeployStepTasks(
            self,
            request: models.ListDeployStepTasksRequest,
            opts: Dict = None,
    ) -> models.ListDeployStepTasksResponse:
        """
        This API is used to retrieve the application history of a certain baseline item.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDeployStepTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDeployStepTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAccountFactoryBaseline(
            self,
            request: models.UpdateAccountFactoryBaselineRequest,
            opts: Dict = None,
    ) -> models.UpdateAccountFactoryBaselineResponse:
        """
        This API is used to update the current baseline item configuration of a user. The baseline configuration will be overwritten with the current configuration. When adding new baseline items, the newly-added baseline configuration needs to be added to the existing configuration. When deleting baseline items, the deleted baseline configuration needs to be removed from the existing configuration, then save the latest baseline configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAccountFactoryBaseline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAccountFactoryBaselineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)