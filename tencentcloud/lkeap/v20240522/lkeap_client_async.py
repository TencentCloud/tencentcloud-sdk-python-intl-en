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

    async def ChatCompletions(
            self,
            request: models.ChatCompletionsRequest,
            opts: Dict = None,
    ) -> models.ChatCompletionsResponse:
        """
        ### API Features Call the API to initiate a chat request. The concurrency limit for API calls of a single account is 5. To use OpenAI compatible APIs, please refer to [Deepseek OpenAI Chat API](https://cloud.tencent.com/document/product/1772/115969) #### Online Experience If you want to directly experience the DeepSeek model on the web page, it is recommended that you go to [Tencent Cloud TI-AppStudio](https://cloud.tencent.com/product/lke) and use [ DeepSeek Online Assistant](https://lke.cloud.tencent.com/webim_exp/#/chat/wQrAwR). #### Supported models - DeepSeek-V3-0324 (parameter value of model is **deepseek-v3-0324**) - DeepSeek-V3-0324 is a 671B parameter MoE model with outstanding advantages in programming and technical capabilities, context understanding, and long text processing. - Supports 64K context length, maximum input 56K, maximum output 8K (excluding thought chain). - Note: Compared with DeepSeek-V3, DeepSeek-V3-0324 only updated the model weights without increasing the number of parameters. The total model size is 685B, including 671B of main model weights and 14B of multi-token prediction (MTP) module weights. Subsequently, the main model parameter count will be described. - DeepSeek-V3 (model parameter value: **deepseek-v3**) - DeepSeek-V3 is a 671B parameter MoE model with outstanding advantages in multiple tasks such as encyclopedic knowledge and math reasoning. Its evaluation scores rank first among open-source models on mainstream ranked lists. - Supports 64K context length, maximum input 56K, maximum output 8K (excluding thought chain). - DeepSeek-R1 (model parameter value: **deepseek-r1**) - DeepSeek-R1 is a 671B model trained with reinforcement learning. The reasoning process includes a large amount of reflection and verification, and the length of the thought chain can reach tens of thousands of characters. This series of models has excellent reasoning effectiveness in math, coding, and various complex logic reasoning tasks, and displays the complete thinking process for users. - Supports 64K context length, maximum input 56K, maximum output 8K (excluding thought chain). ### Billing Description - Standard billing (effective from February 26, 2025). The billing mode is postpaid hourly settlement. To ensure the normal use of your account resources, please [open postpaid](https://lke.cloud.tencent.com/lke#/app/system/charge/postpaid) in advance and [recharge](https://console.cloud.tencent.com/expense/recharge) in time. - DeepSeek-R1 model | Input: 0.004 CNY/thousand tokens | Output (including thought chain): 0.016 CNY/thousand tokens. - DeepSeek-V3 model | Input: 0.002 CNY/thousand tokens | Output: 0.008 CNY/thousand tokens. - DeepSeek-V3-0324 model | Input: 0.002 CNY/thousand tokens | Output: 0.008 CNY/thousand tokens. ### OpenAI Compatible Protocol API The Knowledge Engine Atomic Power Large Model Dialogue API is compatible with the interface specifications of OpenAI, which means you can directly use the SDK officially provided by OpenAI to call the large model chat API. You only need to replace base_url and [api_key](https://intl.cloud.tencent.com/document/product/1772/115970) with relevant configuration. No additional modifications to your application are required. You can seamlessly switch your application to the corresponding large model. Please refer to the documentation: [Deepseek OpenAI Chat API](https://cloud.tencent.com/document/product/1772/115969). > base_url: https://api.lkeap.cloud.tencent.com/v1 > To obtain api_key, please refer to [API KEY Management](https://cloud.tencent.com/document/product/1772/115970) ### Quick Access 1. Complete [real-name authentication](https://console.cloud.tencent.com/developer/auth). 2. Go to [Console](https://console.cloud.tencent.com/lkeap) to activate the service for the master account. If it is a sub-account, it needs to be authorized by the main account in [Permission Management](https://console.cloud.tencent.com/cam), and associated with a preset policy. Policy name: QcloudLKEAPFullAccess. 3. Debug the API online through API Explorer (https://console.cloud.tencent.com/api/explorer?Product=lkeap&Version=2024-05-22&Action=ChatCompletions). 4. Use [official SDK ](https://cloud.tencent.com/document/product/1772/115963#SDK) to call this API (Python/Java/PHP/Go/Node.js/. NET and other languages are supported). ----------- ### SDK Call Example Call this API through local code (support languages such as Python, Java, PHP, Go, Node.js, .NET): The following code takes Python as an example to show how to access the DeepSeek model API on Tencent Cloud. (1) Install environment ``` python3 -m pip install --upgrade tencentcloud-sdk-python-common python3 -m pip install --upgrade tencentcloud-sdk-python-lkeap ``` (2) Sample code - Among them, SecretKey and SecretID need to be obtained from the Tencent Cloud console. - The field "Model" in the parameter "params" can be set to "deepseek-r1" or "deepseek-v3". ``` # -*- coding: utf-8 -*- import json from tencentcloud.common.common_client import CommonClient from tencentcloud.common import credential from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException from tencentcloud.common.profile.client_profile import ClientProfile from tencentcloud.common.profile.http_profile import HttpProfile class NonStreamResponse(object): def __init__(self): self.response = "" def _deserialize(self, obj): self.response = json.dumps(obj) try: # Instantiate an authentication object. Input parameters are required, including the Tencent Cloud account SecretId and SecretKey. Here, you also need to pay attention to keeping the confidentiality of the key pair. # Code leakage may lead to the leakage of SecretId and SecretKey and threaten the security of all resources under the account. The following code examples are for reference only. It is recommended to use keys in a more secure way. Please refer to: https://cloud.tencent.com/document/product/1278/85305 # Obtain the key in the official website console at https://console.cloud.tencent.com/cam/capi cred = credential.Credential("", "") httpProfile = HttpProfile() httpProfile.endpoint = "lkeap.tencentcloudapi.com" httpProfile.reqTimeout = 40000 # The streaming API may take a longer time.  clientProfile = ClientProfile() clientProfile.httpProfile = httpProfile params = "{\"Model\":\"deepseek-r1\",\"Messages\":[{\"Role\":\"user\",\"Content\":\"Hello\"}],\"Stream\":true}"; common_client = CommonClient("lkeap", "2024-05-22", cred, "ap-guangzhou", profile=clientProfile) resp = common_client._call_and_deserialize("ChatCompletions", json.loads(params), NonStreamResponse) if isinstance(resp, NonStreamResponse): # Non-streaming response print(resp.response) else: # Streaming response for event in resp: print(event) except TencentCloudSDKException as err: print(err) ``` **DeepSeek-R1 usage recommendations** 1. Set the temperature in the range of 0.5-0.7 (0.6 is recommended) to prevent endless repetition or incoherent output. 2. Avoid adding system prompts. All descriptions should be included in user prompts.
        """
        
        kwargs = {}
        kwargs["action"] = "ChatCompletions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChatCompletionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
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