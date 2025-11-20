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
from tencentcloud.vclm.v20240523 import models
from typing import Dict


class VclmClient(AbstractClient):
    _apiVersion = '2024-05-23'
    _endpoint = 'vclm.intl.tencentcloudapi.com'
    _service = 'vclm'

    async def DescribeImageAnimateJob(
            self,
            request: models.DescribeImageAnimateJobRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAnimateJobResponse:
        """
        This API is used to query image animation tasks. The image animation feature supports generating videos based on dance movements and images to meet the needs of scenarios such as social entertainment and interactive marketing.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAnimateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAnimateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitImageAnimateJob(
            self,
            request: models.SubmitImageAnimateJobRequest,
            opts: Dict = None,
    ) -> models.SubmitImageAnimateJobResponse:
        """
        This API is used to submit image animation tasks. The image animation feature supports generating videos based on dance movements and images to meet the needs of scenarios such as social entertainment and interactive marketing.
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitImageAnimateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitImageAnimateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)