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
from tencentcloud.es.v20250101 import models
from typing import Dict


class EsClient(AbstractClient):
    _apiVersion = '2025-01-01'
    _endpoint = 'es.intl.tencentcloudapi.com'
    _service = 'es'

    async def ChunkDocument(
            self,
            request: models.ChunkDocumentRequest,
            opts: Dict = None,
    ) -> models.ChunkDocumentResponse:
        """
        Text segmentation is a technology that splits long text into short fragments for adapting to model input, improving processing efficiency, or information retrieval. It balances fragment length and semantic consistency, suitable for NLP and data analysis scenarios.
        This API is used to slice text based on delimiter rules. It has a single-account call limit. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ChunkDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChunkDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChunkDocumentAsync(
            self,
            request: models.ChunkDocumentAsyncRequest,
            opts: Dict = None,
    ) -> models.ChunkDocumentAsyncResponse:
        """
        Text segmentation is a technology that splits long text into short clips for adapting to model input, improving processing efficiency, or information retrieval. It balances clip length and semantic consistency, suitable for NLP and data analysis scenarios.
        This API is an async API with a model dimensional call limit. Each model has a qps limit of 5. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ChunkDocumentAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChunkDocumentAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDocumentChunkResult(
            self,
            request: models.GetDocumentChunkResultRequest,
            opts: Dict = None,
    ) -> models.GetDocumentChunkResultResponse:
        """
        Retrieve document slices
        """
        
        kwargs = {}
        kwargs["action"] = "GetDocumentChunkResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDocumentChunkResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDocumentParseResult(
            self,
            request: models.GetDocumentParseResultRequest,
            opts: Dict = None,
    ) -> models.GetDocumentParseResultResponse:
        """
        This API is used to retrieve the asynchronous processing result of document parsing.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDocumentParseResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDocumentParseResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMultiModalEmbedding(
            self,
            request: models.GetMultiModalEmbeddingRequest,
            opts: Dict = None,
    ) -> models.GetMultiModalEmbeddingResponse:
        """
        Embedding is a technology that maps high-dimensional data to a low-dimensional space, usually used for converting unstructured data such as text, images, or audio into vector representation, making it easier to input into machine models for processing, and the distance between vectors can reflect the similarity between objects.
        This API has a model dimensional call limit. Each model has a qps limit of 10. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "GetMultiModalEmbedding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMultiModalEmbeddingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTextEmbedding(
            self,
            request: models.GetTextEmbeddingRequest,
            opts: Dict = None,
    ) -> models.GetTextEmbeddingResponse:
        """
        Embedding is a technology that maps high-dimensional data to a low-dimensional space, usually used for converting unstructured data such as text, images, or audio into vector representation, making it easier to input into machine models for processing, and the distance between vectors can reflect the similarity between objects.
        This API has a model dimensional call limit. Each model has a qps limit of 20. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "GetTextEmbedding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTextEmbeddingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseDocument(
            self,
            request: models.ParseDocumentRequest,
            opts: Dict = None,
    ) -> models.ParseDocumentResponse:
        """
        This service can accurately convert various types of documents into a standard format to meet the requirements for building an enterprise knowledge base, migrating technical documentation, and structured storage for content platforms.
        This API has a model dimensional call limit. Each model has a qps limit of 5. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ParseDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        kwargs["opts"]["Endpoint"] = "%s://es.ai.tencentcloudapi.com" % self.profile.httpProfile.scheme
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseDocumentAsync(
            self,
            request: models.ParseDocumentAsyncRequest,
            opts: Dict = None,
    ) -> models.ParseDocumentAsyncResponse:
        """
        This service accurately converts various format documents into standard format, meeting requirements for Enterprise Knowledge Base construction, technical documentation migration, and structured storage for content platforms.
        This API is an async API with a model dimensional call limit. Each model has a qps limit of 5. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ParseDocumentAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseDocumentAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunRerank(
            self,
            request: models.RunRerankRequest,
            opts: Dict = None,
    ) -> models.RunRerankResponse:
        """
        Rearrangement refers to the process in RAG where, by assessing the relevance between documents and queries, the most relevant documents are placed at the front. This ensures that the language model prioritizes high-ranking context when generating responses, improving the accuracy and reliability of generated results. It can also be used for filtering to reduce large model costs.
        This API has a single-account call limit. If you need to increase the concurrent limit, please contact us (https://www.tencentcloud.com/act/event/Online_service?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "RunRerank"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunRerankResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)