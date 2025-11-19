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
from tencentcloud.lkeap.v20240522 import models


class LkeapClient(AbstractClient):
    _apiVersion = '2024-05-22'
    _endpoint = 'lkeap.intl.tencentcloudapi.com'
    _service = 'lkeap'


    def CreateReconstructDocumentFlow(self, request):
        r"""This API is used to initiate requests for this asynchronous API, for initiating document parsing tasks.
        Document parsing supports converting images or PDF files into Markdown format files, and can parse content elements including tables, formulas, images, headings, paragraphs, headers, and footers, and intelligently convert the content into reading order. Please refer to the input parameter list below for specific supported file types.
        During the trial period, the QPS limit for a single account is only 1. If you need to access officially, please contact our R&D team.

        :param request: Request instance for CreateReconstructDocumentFlow.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.CreateReconstructDocumentFlowRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CreateReconstructDocumentFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReconstructDocumentFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReconstructDocumentFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSplitDocumentFlow(self, request):
        r"""This API is used to create document segmentation tasks, support various file types, possess mllm capacity, and can analyze and deeply understand the information in charts.

        :param request: Request instance for CreateSplitDocumentFlow.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.CreateSplitDocumentFlowRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CreateSplitDocumentFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSplitDocumentFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSplitDocumentFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEmbedding(self, request):
        r"""This API is used to call the text representation model to convert text into a vector represented by numbers, which can be used in scenarios such as text retrieval, information recommendation, and knowledge mining. There is a single-account call limit control for this API. If you need to increase the concurrency limit, please contact us (https://cloud.tencent.com/act/event/Online_service).

        :param request: Request instance for GetEmbedding.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.GetEmbeddingRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.GetEmbeddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEmbedding", params, headers=headers)
            response = json.loads(body)
            model = models.GetEmbeddingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetReconstructDocumentResult(self, request):
        r"""This is an asynchronous API for querying results, which is used to obtain the result of document parsing.

        :param request: Request instance for GetReconstructDocumentResult.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.GetReconstructDocumentResultRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.GetReconstructDocumentResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetReconstructDocumentResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetReconstructDocumentResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSplitDocumentResult(self, request):
        r"""This API is used to query the results of document splitting tasks.

        :param request: Request instance for GetSplitDocumentResult.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.GetSplitDocumentResultRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.GetSplitDocumentResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSplitDocumentResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetSplitDocumentResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryRewrite(self, request):
        r"""QueryRewrite is mainly used in multi-round conversations for reference resolution and ellipsis completion. Using this API, you don't need to input prompt descriptions. A more accurate user query can be generated based on the conversation history. In terms of application scenarios, this API can be applied to various scenarios such as intelligent Q&A and conversational search.
        There is a call limit for single-account for this API. If you need to increase the concurrency limit, please contact us (https://cloud.tencent.com/act/event/Online_service).

        :param request: Request instance for QueryRewrite.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.QueryRewriteRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.QueryRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.QueryRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReconstructDocumentSSE(self, request):
        r"""This API is used for quasi-real-time document parsing, using HTTP SSE protocol for communication.

        :param request: Request instance for ReconstructDocumentSSE.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.ReconstructDocumentSSERequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.ReconstructDocumentSSEResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("ReconstructDocumentSSE", params, models.ReconstructDocumentSSEResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunRerank(self, request):
        r"""This API is used to reorder the results of multi-channel recall based on the rerank model of knowledge engine fine-tuning model technology, sort the segments according to the relevance between the query and the segment content from high to low score, and output the corresponding scoring results.

        :param request: Request instance for RunRerank.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.RunRerankRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.RunRerankResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunRerank", params, headers=headers)
            response = json.loads(body)
            model = models.RunRerankResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))