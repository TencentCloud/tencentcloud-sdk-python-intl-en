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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.hunyuan.v20230901 import models


class HunyuanClient(AbstractClient):
    _apiVersion = '2023-09-01'
    _endpoint = 'hunyuan.intl.tencentcloudapi.com'
    _service = 'hunyuan'


    def ChatTranslations(self, request):
        r"""Tencent Hunyuan is a large language model (LLM) developed by Tencent R&D. It possesses powerful Chinese creation capacity, logical reasoning in complex context, and reliable task execution power. This API supports streaming or non-streaming calls. When using streaming calls, it follows the SSE protocol.

        1. This API does not currently support returning Image Content.
        2. By default, this API has account restrictions with a number of concurrencies of 5.
        3. Please use the SDK to call this API. examples are provided in the Git repository examples/hunyuan/v20230901/ directory for each development language. The SDK link is provided in the "**Developer Resources - SDK**" part under the document.
        4. We recommend you use API Explorer for quick online debugging interface and download example code in languages, [click to open](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions).

        :param request: Request instance for ChatTranslations.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.ChatTranslationsRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ChatTranslationsResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("ChatTranslations", params, models.ChatTranslationsResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Convert3DFormat(self, request):
        r"""After inputting a 3D model file, the 3D model file format can be switched.

        :param request: Request instance for Convert3DFormat.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.Convert3DFormatRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Convert3DFormatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Convert3DFormat", params, headers=headers)
            response = json.loads(body)
            model = models.Convert3DFormatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Describe3DSmartTopologyJob(self, request):
        r"""The SmartTopoly API uses the Polygon 1.5 model. After manually inputting a 3D high-poly model, it can generate a neat 3D model with lower polygon count.
        1 concurrent is provided by default, which means 1 submitted task can be processed simultaneously. The next task can be processed only after the previous task is completed.

        :param request: Request instance for Describe3DSmartTopologyJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.Describe3DSmartTopologyJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Describe3DSmartTopologyJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Describe3DSmartTopologyJob", params, headers=headers)
            response = json.loads(body)
            model = models.Describe3DSmartTopologyJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryHunyuan3DPartJob(self, request):
        r"""This API is used to query the generation task of a component.

        :param request: Request instance for QueryHunyuan3DPartJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuan3DPartJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuan3DPartJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuan3DPartJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuan3DPartJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryHunyuanTo3DProJob(self, request):
        r"""This API is used to intelligently generate 3D content based on the HunYuan Large Model and input text descriptions/images.
        This API is used to provide 3 concurrent tasks by default, which can process 3 submitted tasks simultaneously. The next task can be processed only after the previous task is completed.

        :param request: Request instance for QueryHunyuanTo3DProJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuanTo3DProJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuanTo3DProJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuanTo3DProJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuanTo3DProJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryHunyuanTo3DRapidJob(self, request):
        r"""This API is used to intelligently generate 3D content based on the HunYuan Large Model with input text descriptions or images.
        This API is used to provide 1 concurrent task by default, which means only 1 submitted task can be processed simultaneously. The next task can be processed only after the previous task is completed.

        :param request: Request instance for QueryHunyuanTo3DRapidJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuanTo3DRapidJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuanTo3DRapidJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuanTo3DRapidJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuanTo3DRapidJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Submit3DSmartTopologyJob(self, request):
        r"""The SmartTopoly API uses the Polygen 1.5 model. After manually inputting a 3D high-poly model, it can generate a neat 3D model with lower polygon count.
        1 concurrent is provided by default, which means 1 submitted task can be processed simultaneously. The next task can be processed only after the previous task is completed.

        :param request: Request instance for Submit3DSmartTopologyJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.Submit3DSmartTopologyJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Submit3DSmartTopologyJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Submit3DSmartTopologyJob", params, headers=headers)
            response = json.loads(body)
            model = models.Submit3DSmartTopologyJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuan3DPartJob(self, request):
        r"""This API is used to automatically perform component identification and generation based on the model structure after inputting a 3D model file.

        :param request: Request instance for SubmitHunyuan3DPartJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuan3DPartJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuan3DPartJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuan3DPartJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuan3DPartJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanTo3DProJob(self, request):
        r"""This API is used to intelligently generate 3D content based on the HunYuan Large Model and input text descriptions/images.
        This API is used to provide 3 concurrent tasks by default. Up to 3 submitted tasks can be processed simultaneously. A new task can be processed only after the previous one is completed.

        :param request: Request instance for SubmitHunyuanTo3DProJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuanTo3DProJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuanTo3DProJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanTo3DProJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanTo3DProJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanTo3DRapidJob(self, request):
        r"""This API is used to intelligently generate 3D content based on the HunYuan Large Model with input text descriptions or images.
        This API is used to provide 1 concurrent task by default, which means only 1 submitted task can be processed simultaneously. The next task can be processed only after the previous task is completed.

        :param request: Request instance for SubmitHunyuanTo3DRapidJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuanTo3DRapidJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuanTo3DRapidJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanTo3DRapidJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanTo3DRapidJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))