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
from tencentcloud.cdz.v20221123 import models
from typing import Dict


class CdzClient(AbstractClient):
    _apiVersion = '2022-11-23'
    _endpoint = 'cdz.intl.tencentcloudapi.com'
    _service = 'cdz'

    async def DescribeCloudDedicatedZoneResourceSummary(
            self,
            request: models.DescribeCloudDedicatedZoneResourceSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudDedicatedZoneResourceSummaryResponse:
        """
        This API is used to query resource usage of each vertical product in Cloud Dedicated Zone.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudDedicatedZoneResourceSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudDedicatedZoneResourceSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)