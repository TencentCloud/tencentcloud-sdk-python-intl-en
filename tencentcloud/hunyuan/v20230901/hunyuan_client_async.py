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
from tencentcloud.hunyuan.v20230901 import models
from typing import Dict


class HunyuanClient(AbstractClient):
    _apiVersion = '2023-09-01'
    _endpoint = 'hunyuan.intl.tencentcloudapi.com'
    _service = 'hunyuan'

    async def QueryHunyuanTo3DProJob(
            self,
            request: models.QueryHunyuanTo3DProJobRequest,
            opts: Dict = None,
    ) -> models.QueryHunyuanTo3DProJobResponse:
        """
        This API is used to intelligently generate 3D content based on the HunYuan Large Model and input text descriptions/images.
        This API is used to provide 3 concurrent tasks by default, which can process 3 submitted tasks simultaneously. The next task can be processed only after the previous task is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryHunyuanTo3DProJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryHunyuanTo3DProJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitHunyuanTo3DProJob(
            self,
            request: models.SubmitHunyuanTo3DProJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHunyuanTo3DProJobResponse:
        """
        This API is used to intelligently generate 3D content based on the HunYuan Large Model and input text descriptions/images.
        This API is used to provide 3 concurrent tasks by default. Up to 3 submitted tasks can be processed simultaneously. A new task can be processed only after the previous one is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHunyuanTo3DProJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHunyuanTo3DProJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)