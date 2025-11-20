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
from tencentcloud.aiart.v20221229 import models
from typing import Dict


class AiartClient(AbstractClient):
    _apiVersion = '2022-12-29'
    _endpoint = 'aiart.intl.tencentcloudapi.com'
    _service = 'aiart'

    async def ImageToImage(
            self,
            request: models.ImageToImageRequest,
            opts: Dict = None,
    ) -> models.ImageToImageResponse:
        """
        This API is used to transfer the image style based on the image to image technology. Images with small figures, complex gestures or too many figures are not recommended.
        It supports 3 concurrency by default, which means that up to 3 submitted tasks can be processed simultaneously. Subsequent tasks can be processed only after ongoing ones are completed.
        """
        
        kwargs = {}
        kwargs["action"] = "ImageToImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageToImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)