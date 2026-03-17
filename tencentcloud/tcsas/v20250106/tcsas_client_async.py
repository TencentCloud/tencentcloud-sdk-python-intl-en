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
from tencentcloud.tcsas.v20250106 import models
from typing import Dict


class TcsasClient(AbstractClient):
    _apiVersion = '2025-01-06'
    _endpoint = 'tcsas.intl.tencentcloudapi.com'
    _service = 'tcsas'

    async def DescribeMNGMAUDataDetail(
            self,
            request: models.DescribeMNGMAUDataDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGMAUDataDetailResponse:
        """
        This API is used to retrieve the detailed mini game monthly active user data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGMAUDataDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGMAUDataDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGMAULineChart(
            self,
            request: models.DescribeMNGMAULineChartRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGMAULineChartResponse:
        """
        This API is used to retrieve mini game monthly active user data in a line chart format.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGMAULineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGMAULineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGMAUMonthlyComparisonMetricCard(
            self,
            request: models.DescribeMNGMAUMonthlyComparisonMetricCardRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGMAUMonthlyComparisonMetricCardResponse:
        """
        This API is used to retrieve MAU comparison data for a mini game between two months.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGMAUMonthlyComparisonMetricCard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGMAUMonthlyComparisonMetricCardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPMAUDataDetail(
            self,
            request: models.DescribeMNPMAUDataDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPMAUDataDetailResponse:
        """
        This API is used to retrieve the detailed mini program monthly active user data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPMAUDataDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPMAUDataDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPMAULineChart(
            self,
            request: models.DescribeMNPMAULineChartRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPMAULineChartResponse:
        """
        This API is used to retrieve mini program monthly active user data in a line chart format.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPMAULineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPMAULineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPMAUMetricCard(
            self,
            request: models.DescribeMNPMAUMetricCardRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPMAUMetricCardResponse:
        """
        This API is used to retrieve MAU comparison data for a mini program between two months.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPMAUMetricCard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPMAUMetricCardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)