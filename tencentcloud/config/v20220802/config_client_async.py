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
from tencentcloud.config.v20220802 import models
from typing import Dict


class ConfigClient(AbstractClient):
    _apiVersion = '2022-08-02'
    _endpoint = 'config.intl.tencentcloudapi.com'
    _service = 'config'

    async def DescribeDiscoveredResource(
            self,
            request: models.DescribeDiscoveredResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDiscoveredResourceResponse:
        """
        Resource details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiscoveredResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiscoveredResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateConfigRules(
            self,
            request: models.ListAggregateConfigRulesRequest,
            opts: Dict = None,
    ) -> models.ListAggregateConfigRulesResponse:
        """
        This API is used to get the account group rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateConfigRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateConfigRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateDiscoveredResources(
            self,
            request: models.ListAggregateDiscoveredResourcesRequest,
            opts: Dict = None,
    ) -> models.ListAggregateDiscoveredResourcesResponse:
        """
        Account Group access the list of resources.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateDiscoveredResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateDiscoveredResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConfigRules(
            self,
            request: models.ListConfigRulesRequest,
            opts: Dict = None,
    ) -> models.ListConfigRulesResponse:
        """
        This API is used to get the rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListConfigRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConfigRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDiscoveredResources(
            self,
            request: models.ListDiscoveredResourcesRequest,
            opts: Dict = None,
    ) -> models.ListDiscoveredResourcesResponse:
        """
        This API is used to get the resource list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDiscoveredResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDiscoveredResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutEvaluations(
            self,
            request: models.PutEvaluationsRequest,
            opts: Dict = None,
    ) -> models.PutEvaluationsResponse:
        """
        This API is used to report custom rule evaluation results.
        """
        
        kwargs = {}
        kwargs["action"] = "PutEvaluations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutEvaluationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)