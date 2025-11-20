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
from tencentcloud.lkeap.v20240522 import models
from typing import Dict


class LkeapClient(AbstractClient):
    _apiVersion = '2024-05-22'
    _endpoint = 'lkeap.intl.tencentcloudapi.com'
    _service = 'lkeap'

    async def CreateReconstructDocumentFlow(
            self,
            request: models.CreateReconstructDocumentFlowRequest,
            opts: Dict = None,
    ) -> models.CreateReconstructDocumentFlowResponse:
        """
        This API is used to initiate requests for this asynchronous API, for initiating document parsing tasks.
        Document parsing supports converting images or PDF files into Markdown format files, and can parse content elements including tables, formulas, images, headings, paragraphs, headers, and footers, and intelligently convert the content into reading order. Please refer to the input parameter list below for specific supported file types.
        During the trial period, the QPS limit for a single account is only 1. If you need to access officially, please contact our R&D team.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReconstructDocumentFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReconstructDocumentFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSplitDocumentFlow(
            self,
            request: models.CreateSplitDocumentFlowRequest,
            opts: Dict = None,
    ) -> models.CreateSplitDocumentFlowResponse:
        """
        This API is used to create document segmentation tasks, support various file types, possess mllm capacity, and can analyze and deeply understand the information in charts.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSplitDocumentFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSplitDocumentFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetEmbedding(
            self,
            request: models.GetEmbeddingRequest,
            opts: Dict = None,
    ) -> models.GetEmbeddingResponse:
        """
        This API is used to call the text representation model to convert text into a vector represented by numbers, which can be used in scenarios such as text retrieval, information recommendation, and knowledge mining. There is a single-account call limit control for this API. If you need to increase the concurrency limit, please contact us (https://cloud.tencent.com/act/event/Online_service).
        """
        
        kwargs = {}
        kwargs["action"] = "GetEmbedding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetEmbeddingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetReconstructDocumentResult(
            self,
            request: models.GetReconstructDocumentResultRequest,
            opts: Dict = None,
    ) -> models.GetReconstructDocumentResultResponse:
        """
        This is an asynchronous API for querying results, which is used to obtain the result of document parsing.
        """
        
        kwargs = {}
        kwargs["action"] = "GetReconstructDocumentResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetReconstructDocumentResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSplitDocumentResult(
            self,
            request: models.GetSplitDocumentResultRequest,
            opts: Dict = None,
    ) -> models.GetSplitDocumentResultResponse:
        """
        This API is used to query the results of document splitting tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSplitDocumentResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSplitDocumentResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryRewrite(
            self,
            request: models.QueryRewriteRequest,
            opts: Dict = None,
    ) -> models.QueryRewriteResponse:
        """
        QueryRewrite is mainly used in multi-round conversations for reference resolution and ellipsis completion. Using this API, you don't need to input prompt descriptions. A more accurate user query can be generated based on the conversation history. In terms of application scenarios, this API can be applied to various scenarios such as intelligent Q&A and conversational search.
        There is a call limit for single-account for this API. If you need to increase the concurrency limit, please contact us (https://cloud.tencent.com/act/event/Online_service).
        """
        
        kwargs = {}
        kwargs["action"] = "QueryRewrite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryRewriteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReconstructDocumentSSE(
            self,
            request: models.ReconstructDocumentSSERequest,
            opts: Dict = None,
    ) -> models.ReconstructDocumentSSEResponse:
        """
        This API is used for quasi-real-time document parsing, using HTTP SSE protocol for communication.
        """
        
        kwargs = {}
        kwargs["action"] = "ReconstructDocumentSSE"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReconstructDocumentSSEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunRerank(
            self,
            request: models.RunRerankRequest,
            opts: Dict = None,
    ) -> models.RunRerankResponse:
        """
        This API is used to reorder the results of multi-channel recall based on the rerank model of knowledge engine fine-tuning model technology, sort the segments according to the relevance between the query and the segment content from high to low score, and output the corresponding scoring results.
        """
        
        kwargs = {}
        kwargs["action"] = "RunRerank"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunRerankResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)