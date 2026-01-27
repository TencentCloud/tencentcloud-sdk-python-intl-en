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

    async def ChatTranslations(
            self,
            request: models.ChatTranslationsRequest,
            opts: Dict = None,
    ) -> models.ChatTranslationsResponse:
        """
        Tencent Hunyuan is a large language model (LLM) developed by Tencent R&D. It possesses powerful Chinese creation capacity, logical reasoning in complex context, and reliable task execution power. This API supports streaming or non-streaming calls. When using streaming calls, it follows the SSE protocol.

        1. This API does not currently support returning Image Content.
        2. By default, this API has account restrictions with a number of concurrencies of 5.
        3. Please use the SDK to call this API. examples are provided in the Git repository examples/hunyuan/v20230901/ directory for each development language. The SDK link is provided in the "**Developer Resources - SDK**" part under the document.
        4. We recommend you use API Explorer for quick online debugging interface and download example code in languages, [click to open](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions).
        """
        
        kwargs = {}
        kwargs["action"] = "ChatTranslations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChatTranslationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Convert3DFormat(
            self,
            request: models.Convert3DFormatRequest,
            opts: Dict = None,
    ) -> models.Convert3DFormatResponse:
        """
        After inputting a 3D model file, the 3D model file format can be switched.
        """
        
        kwargs = {}
        kwargs["action"] = "Convert3DFormat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.Convert3DFormatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Describe3DSmartTopologyJob(
            self,
            request: models.Describe3DSmartTopologyJobRequest,
            opts: Dict = None,
    ) -> models.Describe3DSmartTopologyJobResponse:
        """
        The SmartTopoly API uses the Polygon 1.5 model. After manually inputting a 3D high-poly model, it can generate a neat 3D model with lower polygon count.
        1 concurrent is provided by default, which means 1 submitted task can be processed simultaneously. The next task can be processed only after the previous task is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "Describe3DSmartTopologyJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.Describe3DSmartTopologyJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryHunyuan3DPartJob(
            self,
            request: models.QueryHunyuan3DPartJobRequest,
            opts: Dict = None,
    ) -> models.QueryHunyuan3DPartJobResponse:
        """
        This API is used to query the generation task of a component.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryHunyuan3DPartJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryHunyuan3DPartJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
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
        
    async def QueryHunyuanTo3DRapidJob(
            self,
            request: models.QueryHunyuanTo3DRapidJobRequest,
            opts: Dict = None,
    ) -> models.QueryHunyuanTo3DRapidJobResponse:
        """
        This API is used to intelligently generate 3D content based on the HunYuan Large Model with input text descriptions or images.
        This API is used to provide 1 concurrent task by default, which means only 1 submitted task can be processed simultaneously. The next task can be processed only after the previous task is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryHunyuanTo3DRapidJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryHunyuanTo3DRapidJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Submit3DSmartTopologyJob(
            self,
            request: models.Submit3DSmartTopologyJobRequest,
            opts: Dict = None,
    ) -> models.Submit3DSmartTopologyJobResponse:
        """
        The SmartTopoly API uses the Polygen 1.5 model. After manually inputting a 3D high-poly model, it can generate a neat 3D model with lower polygon count.
        1 concurrent is provided by default, which means 1 submitted task can be processed simultaneously. The next task can be processed only after the previous task is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "Submit3DSmartTopologyJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.Submit3DSmartTopologyJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitHunyuan3DPartJob(
            self,
            request: models.SubmitHunyuan3DPartJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHunyuan3DPartJobResponse:
        """
        This API is used to automatically perform component identification and generation based on the model structure after inputting a 3D model file.
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHunyuan3DPartJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHunyuan3DPartJobResponse
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
        
    async def SubmitHunyuanTo3DRapidJob(
            self,
            request: models.SubmitHunyuanTo3DRapidJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHunyuanTo3DRapidJobResponse:
        """
        This API is used to intelligently generate 3D content based on the HunYuan Large Model with input text descriptions or images.
        This API is used to provide 1 concurrent task by default, which means only 1 submitted task can be processed simultaneously. The next task can be processed only after the previous task is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHunyuanTo3DRapidJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHunyuanTo3DRapidJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)