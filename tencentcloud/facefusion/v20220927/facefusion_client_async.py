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
from tencentcloud.facefusion.v20220927 import models
from typing import Dict


class FacefusionClient(AbstractClient):
    _apiVersion = '2022-09-27'
    _endpoint = 'facefusion.intl.tencentcloudapi.com'
    _service = 'facefusion'

    async def FuseFace(
            self,
            request: models.FuseFaceRequest,
            opts: Dict = None,
    ) -> models.FuseFaceResponse:
        """
        This API is used to perform the fusion of a single face, multiple faces, and specified faces with the material template by uploading face images. Users can add logos to generated images. See <a href="https://intl.cloud.tencent.com/document/product/670/38247?from_cn_redirect=1" target="_blank">Fusion Access Guide</a>.



        - The signature method in the public parameters must be specified as the V3 version. In other words, set the SignatureMethod parameter to TC3-HMAC-SHA256.
        """
        
        kwargs = {}
        kwargs["action"] = "FuseFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FuseFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryVideoFaceFusionJob(
            self,
            request: models.QueryVideoFaceFusionJobRequest,
            opts: Dict = None,
    ) -> models.QueryVideoFaceFusionJobResponse:
        """
        This API is used to query the progress and status of video face fusion tasks by Job ID.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryVideoFaceFusionJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryVideoFaceFusionJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitVideoFaceFusionJob(
            self,
            request: models.SubmitVideoFaceFusionJobRequest,
            opts: Dict = None,
    ) -> models.SubmitVideoFaceFusionJobResponse:
        """
        This API is used to submit asynchronous processing tasks of video face fusion. After a task is submitted, the Job ID, estimated completion time, and current queue length will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitVideoFaceFusionJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitVideoFaceFusionJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)