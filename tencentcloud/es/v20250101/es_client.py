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
from tencentcloud.es.v20250101 import models


class EsClient(AbstractClient):
    _apiVersion = '2025-01-01'
    _endpoint = 'es.intl.tencentcloudapi.com'
    _service = 'es'


    def ChunkDocument(self, request):
        r"""Text segmentation is a technology that splits long text into short fragments for adapting to model input, improving processing efficiency, or information retrieval. It balances fragment length and semantic consistency, suitable for NLP and data analysis scenarios.
        This API is used to slice text based on delimiter rules. It has a single-account call limit. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).

        :param request: Request instance for ChunkDocument.
        :type request: :class:`tencentcloud.es.v20250101.models.ChunkDocumentRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChunkDocument", params, headers=headers)
            response = json.loads(body)
            model = models.ChunkDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChunkDocumentAsync(self, request):
        r"""Text segmentation is a technology that splits long text into short clips for adapting to model input, improving processing efficiency, or information retrieval. It balances clip length and semantic consistency, suitable for NLP and data analysis scenarios.
        This API is an async API with a model dimensional call limit. Each model has a qps limit of 5. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).

        :param request: Request instance for ChunkDocumentAsync.
        :type request: :class:`tencentcloud.es.v20250101.models.ChunkDocumentAsyncRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkDocumentAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChunkDocumentAsync", params, headers=headers)
            response = json.loads(body)
            model = models.ChunkDocumentAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDocumentChunkResult(self, request):
        r"""Retrieve document slices

        :param request: Request instance for GetDocumentChunkResult.
        :type request: :class:`tencentcloud.es.v20250101.models.GetDocumentChunkResultRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.GetDocumentChunkResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDocumentChunkResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetDocumentChunkResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDocumentParseResult(self, request):
        r"""This API is used to retrieve the asynchronous processing result of document parsing.

        :param request: Request instance for GetDocumentParseResult.
        :type request: :class:`tencentcloud.es.v20250101.models.GetDocumentParseResultRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.GetDocumentParseResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDocumentParseResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetDocumentParseResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMultiModalEmbedding(self, request):
        r"""Embedding is a technology that maps high-dimensional data to a low-dimensional space, usually used for converting unstructured data such as text, images, or audio into vector representation, making it easier to input into machine models for processing, and the distance between vectors can reflect the similarity between objects.
        This API has a model dimensional call limit. Each model has a qps limit of 10. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).

        :param request: Request instance for GetMultiModalEmbedding.
        :type request: :class:`tencentcloud.es.v20250101.models.GetMultiModalEmbeddingRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.GetMultiModalEmbeddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMultiModalEmbedding", params, headers=headers)
            response = json.loads(body)
            model = models.GetMultiModalEmbeddingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTextEmbedding(self, request):
        r"""Embedding is a technology that maps high-dimensional data to a low-dimensional space, usually used for converting unstructured data such as text, images, or audio into vector representation, making it easier to input into machine models for processing, and the distance between vectors can reflect the similarity between objects.
        This API has a model dimensional call limit. Each model has a qps limit of 20. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).

        :param request: Request instance for GetTextEmbedding.
        :type request: :class:`tencentcloud.es.v20250101.models.GetTextEmbeddingRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.GetTextEmbeddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTextEmbedding", params, headers=headers)
            response = json.loads(body)
            model = models.GetTextEmbeddingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ParseDocument(self, request):
        r"""This service can accurately convert various types of documents into a standard format to meet the requirements for building an enterprise knowledge base, migrating technical documentation, and structured storage for content platforms.
        This API has a model dimensional call limit. Each model has a qps limit of 5. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).

        :param request: Request instance for ParseDocument.
        :type request: :class:`tencentcloud.es.v20250101.models.ParseDocumentRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.ParseDocumentResponse`

        """
        try:
            params = request._serialize()
            options = {"Endpoint": "%s://es.ai.tencentcloudapi.com" % self.profile.httpProfile.scheme}
            return self._call_and_deserialize("ParseDocument", params, models.ParseDocumentResponse, headers=request.headers, options=options)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ParseDocumentAsync(self, request):
        r"""This service accurately converts various format documents into standard format, meeting requirements for Enterprise Knowledge Base construction, technical documentation migration, and structured storage for content platforms.
        This API is an async API with a model dimensional call limit. Each model has a qps limit of 5. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).

        :param request: Request instance for ParseDocumentAsync.
        :type request: :class:`tencentcloud.es.v20250101.models.ParseDocumentAsyncRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.ParseDocumentAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ParseDocumentAsync", params, headers=headers)
            response = json.loads(body)
            model = models.ParseDocumentAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunRerank(self, request):
        r"""Rearrangement refers to the process in RAG where, by assessing the relevance between documents and queries, the most relevant documents are placed at the front. This ensures that the language model prioritizes high-ranking context when generating responses, improving the accuracy and reliability of generated results. It can also be used for filtering to reduce large model costs.
        This API has a single-account call limit. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).

        :param request: Request instance for RunRerank.
        :type request: :class:`tencentcloud.es.v20250101.models.RunRerankRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.RunRerankResponse`

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