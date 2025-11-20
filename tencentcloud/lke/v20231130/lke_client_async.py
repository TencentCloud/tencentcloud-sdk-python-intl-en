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
from tencentcloud.lke.v20231130 import models
from typing import Dict


class LkeClient(AbstractClient):
    _apiVersion = '2023-11-30'
    _endpoint = 'lke.intl.tencentcloudapi.com'
    _service = 'lke'

    async def CheckAttributeLabelExist(
            self,
            request: models.CheckAttributeLabelExistRequest,
            opts: Dict = None,
    ) -> models.CheckAttributeLabelExistResponse:
        """
        This API is used to check if the label name under an attribute exist.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAttributeLabelExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAttributeLabelExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckAttributeLabelRefer(
            self,
            request: models.CheckAttributeLabelReferRequest,
            opts: Dict = None,
    ) -> models.CheckAttributeLabelReferResponse:
        """
        This API is used to check attribute label references.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAttributeLabelRefer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAttributeLabelReferResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApp(
            self,
            request: models.CreateAppRequest,
            opts: Dict = None,
    ) -> models.CreateAppResponse:
        """
        This API is used to create knowledge engine applications.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAttributeLabel(
            self,
            request: models.CreateAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.CreateAttributeLabelResponse:
        """
        This API is used to create attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCorp(
            self,
            request: models.CreateCorpRequest,
            opts: Dict = None,
    ) -> models.CreateCorpResponse:
        """
        This API is used to create enterprises.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCorp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCorpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDocCate(
            self,
            request: models.CreateDocCateRequest,
            opts: Dict = None,
    ) -> models.CreateDocCateResponse:
        """
        This API is used to create doc categories.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDocCate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDocCateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateQA(
            self,
            request: models.CreateQARequest,
            opts: Dict = None,
    ) -> models.CreateQAResponse:
        """
        This API is used to enter Q&As.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateQACate(
            self,
            request: models.CreateQACateRequest,
            opts: Dict = None,
    ) -> models.CreateQACateResponse:
        """
        This API is used to create Q&A categories.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateQACate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateQACateResponse
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
        Document parsing supports converting images or PDF files into Markdown format files, and can parse content elements including tables, formulas, images, headings, paragraphs, headers, and footers, and intelligently convert the content into reading order.
        During the trial period, the QPS limit for a single account is only 1. If you need to access officially, please contact our R&D team.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReconstructDocumentFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReconstructDocumentFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRejectedQuestion(
            self,
            request: models.CreateRejectedQuestionRequest,
            opts: Dict = None,
    ) -> models.CreateRejectedQuestionResponse:
        """
        This API is used to create rejected questions.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRejectedQuestion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRejectedQuestionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRelease(
            self,
            request: models.CreateReleaseRequest,
            opts: Dict = None,
    ) -> models.CreateReleaseResponse:
        """
        This API is used to create a release.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApp(
            self,
            request: models.DeleteAppRequest,
            opts: Dict = None,
    ) -> models.DeleteAppResponse:
        """
        This API is used to delete applications.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAttributeLabel(
            self,
            request: models.DeleteAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.DeleteAttributeLabelResponse:
        """
        This API is used to delete attribute labels.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDoc(
            self,
            request: models.DeleteDocRequest,
            opts: Dict = None,
    ) -> models.DeleteDocResponse:
        """
        This API is used to delete documents.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDocCate(
            self,
            request: models.DeleteDocCateRequest,
            opts: Dict = None,
    ) -> models.DeleteDocCateResponse:
        """
        This API is used to delete Doc categories.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDocCate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDocCateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteQA(
            self,
            request: models.DeleteQARequest,
            opts: Dict = None,
    ) -> models.DeleteQAResponse:
        """
        This API is used to delete Q&As.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteQACate(
            self,
            request: models.DeleteQACateRequest,
            opts: Dict = None,
    ) -> models.DeleteQACateResponse:
        """
        This API is used to delete categories.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteQACate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteQACateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRejectedQuestion(
            self,
            request: models.DeleteRejectedQuestionRequest,
            opts: Dict = None,
    ) -> models.DeleteRejectedQuestionResponse:
        """
        This API is used to delete rejected questions.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRejectedQuestion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRejectedQuestionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApp(
            self,
            request: models.DescribeAppRequest,
            opts: Dict = None,
    ) -> models.DescribeAppResponse:
        """
        This API is used to obtain application details under the corporate.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttributeLabel(
            self,
            request: models.DescribeAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.DescribeAttributeLabelResponse:
        """
        This API is used to query attribute label details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallStatsGraph(
            self,
            request: models.DescribeCallStatsGraphRequest,
            opts: Dict = None,
    ) -> models.DescribeCallStatsGraphResponse:
        """
        This API is used to show line chart of API calls.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallStatsGraph"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallStatsGraphResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConcurrencyUsage(
            self,
            request: models.DescribeConcurrencyUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeConcurrencyUsageResponse:
        """
        This API is used to response to concurrent calls.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConcurrencyUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConcurrencyUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConcurrencyUsageGraph(
            self,
            request: models.DescribeConcurrencyUsageGraphRequest,
            opts: Dict = None,
    ) -> models.DescribeConcurrencyUsageGraphResponse:
        """
        This API is used to show line chart of concurrent calls.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConcurrencyUsageGraph"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConcurrencyUsageGraphResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCorp(
            self,
            request: models.DescribeCorpRequest,
            opts: Dict = None,
    ) -> models.DescribeCorpResponse:
        """
        This API is used to query corporate details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCorp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCorpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDoc(
            self,
            request: models.DescribeDocRequest,
            opts: Dict = None,
    ) -> models.DescribeDocResponse:
        """
        This API is used to query document details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKnowledgeUsage(
            self,
            request: models.DescribeKnowledgeUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeKnowledgeUsageResponse:
        """
        This API is used to query the knowledge library usage.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKnowledgeUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKnowledgeUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKnowledgeUsagePieGraph(
            self,
            request: models.DescribeKnowledgeUsagePieGraphRequest,
            opts: Dict = None,
    ) -> models.DescribeKnowledgeUsagePieGraphResponse:
        """
        This API is used to query pie chart of the enterprise knowledge base capacity .
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKnowledgeUsagePieGraph"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKnowledgeUsagePieGraphResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQA(
            self,
            request: models.DescribeQARequest,
            opts: Dict = None,
    ) -> models.DescribeQAResponse:
        """
        This API is used to query Q&A details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRefer(
            self,
            request: models.DescribeReferRequest,
            opts: Dict = None,
    ) -> models.DescribeReferResponse:
        """
        This API is used to get the reference source details list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRefer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReferResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRelease(
            self,
            request: models.DescribeReleaseRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseResponse:
        """
        This API is used to query release details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseInfo(
            self,
            request: models.DescribeReleaseInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseInfoResponse:
        """
        This API is used to pull the release button status and last release time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRobotBizIDByAppKey(
            self,
            request: models.DescribeRobotBizIDByAppKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeRobotBizIDByAppKeyResponse:
        """
        This API is used to get application business ID through appKey.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRobotBizIDByAppKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRobotBizIDByAppKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchStatsGraph(
            self,
            request: models.DescribeSearchStatsGraphRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchStatsGraphResponse:
        """
        This API is used to query line chart of search service calls.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchStatsGraph"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchStatsGraphResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSegments(
            self,
            request: models.DescribeSegmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeSegmentsResponse:
        """
        This API is used to get fragment details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSegments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSegmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStorageCredential(
            self,
            request: models.DescribeStorageCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageCredentialResponse:
        """
        This API is used to get the temporary key for file upload.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorageCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenUsage(
            self,
            request: models.DescribeTokenUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenUsageResponse:
        """
        This API is used to query API call token details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenUsageGraph(
            self,
            request: models.DescribeTokenUsageGraphRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenUsageGraphResponse:
        """
        This API is used to show API call token line chart.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenUsageGraph"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenUsageGraphResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnsatisfiedReplyContext(
            self,
            request: models.DescribeUnsatisfiedReplyContextRequest,
            opts: Dict = None,
    ) -> models.DescribeUnsatisfiedReplyContextResponse:
        """
        This API is used to get the context of dissatisfied responses.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnsatisfiedReplyContext"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnsatisfiedReplyContextResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAttributeLabel(
            self,
            request: models.ExportAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.ExportAttributeLabelResponse:
        """
        This API is used to export attribute labels.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportQAList(
            self,
            request: models.ExportQAListRequest,
            opts: Dict = None,
    ) -> models.ExportQAListResponse:
        """
        This API is used to export Q&A list.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportQAList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportQAListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportUnsatisfiedReply(
            self,
            request: models.ExportUnsatisfiedReplyRequest,
            opts: Dict = None,
    ) -> models.ExportUnsatisfiedReplyResponse:
        """
        This API is used to export dissatisfied responses.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportUnsatisfiedReply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportUnsatisfiedReplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateQA(
            self,
            request: models.GenerateQARequest,
            opts: Dict = None,
    ) -> models.GenerateQAResponse:
        """
        This API is used to generate Q%A from document.
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAnswerTypeDataCount(
            self,
            request: models.GetAnswerTypeDataCountRequest,
            opts: Dict = None,
    ) -> models.GetAnswerTypeDataCountResponse:
        """
        This API is used to get response type data statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAnswerTypeDataCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAnswerTypeDataCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAppKnowledgeCount(
            self,
            request: models.GetAppKnowledgeCountRequest,
            opts: Dict = None,
    ) -> models.GetAppKnowledgeCountResponse:
        """
        This API is used to get a model list.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAppKnowledgeCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAppKnowledgeCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAppSecret(
            self,
            request: models.GetAppSecretRequest,
            opts: Dict = None,
    ) -> models.GetAppSecretResponse:
        """
        This API is used to get application secret keys.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAppSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAppSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDocPreview(
            self,
            request: models.GetDocPreviewRequest,
            opts: Dict = None,
    ) -> models.GetDocPreviewResponse:
        """
        This API is used to get document preview information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDocPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDocPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLikeDataCount(
            self,
            request: models.GetLikeDataCountRequest,
            opts: Dict = None,
    ) -> models.GetLikeDataCountResponse:
        """
        This API is used to get likes and dislikes data statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "GetLikeDataCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLikeDataCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMsgRecord(
            self,
            request: models.GetMsgRecordRequest,
            opts: Dict = None,
    ) -> models.GetMsgRecordResponse:
        """
        This API is used to obtain chat history based on the session ID (only historical session data within the past 180 days will be retained).
        """
        
        kwargs = {}
        kwargs["action"] = "GetMsgRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMsgRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetReconstructDocumentResult(
            self,
            request: models.GetReconstructDocumentResultRequest,
            opts: Dict = None,
    ) -> models.GetReconstructDocumentResultResponse:
        """
        This is an asynchronous APIs, used to get document parsing task results.
        """
        
        kwargs = {}
        kwargs["action"] = "GetReconstructDocumentResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetReconstructDocumentResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskStatus(
            self,
            request: models.GetTaskStatusRequest,
            opts: Dict = None,
    ) -> models.GetTaskStatusResponse:
        """
        This API is used to get the task status.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWsToken(
            self,
            request: models.GetWsTokenRequest,
            opts: Dict = None,
    ) -> models.GetWsTokenResponse:
        """
        This API is used to get ws token.
        """
        
        kwargs = {}
        kwargs["action"] = "GetWsToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWsTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GroupDoc(
            self,
            request: models.GroupDocRequest,
            opts: Dict = None,
    ) -> models.GroupDocResponse:
        """
        DocGroup.
        """
        
        kwargs = {}
        kwargs["action"] = "GroupDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GroupDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GroupQA(
            self,
            request: models.GroupQARequest,
            opts: Dict = None,
    ) -> models.GroupQAResponse:
        """
        Q&A Group.
        """
        
        kwargs = {}
        kwargs["action"] = "GroupQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GroupQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IgnoreUnsatisfiedReply(
            self,
            request: models.IgnoreUnsatisfiedReplyRequest,
            opts: Dict = None,
    ) -> models.IgnoreUnsatisfiedReplyResponse:
        """
        This API is used to ignore dissatisfied responses.
        """
        
        kwargs = {}
        kwargs["action"] = "IgnoreUnsatisfiedReply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IgnoreUnsatisfiedReplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListApp(
            self,
            request: models.ListAppRequest,
            opts: Dict = None,
    ) -> models.ListAppResponse:
        """
        This API is used to get the application list under the corporate.
        """
        
        kwargs = {}
        kwargs["action"] = "ListApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAppCategory(
            self,
            request: models.ListAppCategoryRequest,
            opts: Dict = None,
    ) -> models.ListAppCategoryResponse:
        """
        This API is used to get list of application types.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAppCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAppCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAppKnowledgeDetail(
            self,
            request: models.ListAppKnowledgeDetailRequest,
            opts: Dict = None,
    ) -> models.ListAppKnowledgeDetailResponse:
        """
        This API is used to query the knowledge base capacity details in a list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAppKnowledgeDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAppKnowledgeDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAttributeLabel(
            self,
            request: models.ListAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.ListAttributeLabelResponse:
        """
        This API is used to query attribute label lists.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDoc(
            self,
            request: models.ListDocRequest,
            opts: Dict = None,
    ) -> models.ListDocResponse:
        """
        This API is used to get document list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDocCate(
            self,
            request: models.ListDocCateRequest,
            opts: Dict = None,
    ) -> models.ListDocCateResponse:
        """
        This API is used to get document category.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDocCate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDocCateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListModel(
            self,
            request: models.ListModelRequest,
            opts: Dict = None,
    ) -> models.ListModelResponse:
        """
        This API is used to get the model list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListQA(
            self,
            request: models.ListQARequest,
            opts: Dict = None,
    ) -> models.ListQAResponse:
        """
        This API is used to query Q&A lists.
        """
        
        kwargs = {}
        kwargs["action"] = "ListQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListQACate(
            self,
            request: models.ListQACateRequest,
            opts: Dict = None,
    ) -> models.ListQACateResponse:
        """
        This API is used to get Q&A categories.
        """
        
        kwargs = {}
        kwargs["action"] = "ListQACate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListQACateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRejectedQuestion(
            self,
            request: models.ListRejectedQuestionRequest,
            opts: Dict = None,
    ) -> models.ListRejectedQuestionResponse:
        """
        This API is used to get rejected questions.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRejectedQuestion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRejectedQuestionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRejectedQuestionPreview(
            self,
            request: models.ListRejectedQuestionPreviewRequest,
            opts: Dict = None,
    ) -> models.ListRejectedQuestionPreviewResponse:
        """
        This API is used to release a preview of rejected questions.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRejectedQuestionPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRejectedQuestionPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRelease(
            self,
            request: models.ListReleaseRequest,
            opts: Dict = None,
    ) -> models.ListReleaseResponse:
        """
        This API is used to get the release list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReleaseConfigPreview(
            self,
            request: models.ListReleaseConfigPreviewRequest,
            opts: Dict = None,
    ) -> models.ListReleaseConfigPreviewResponse:
        """
        This API is used to preview the release configuration items.
        """
        
        kwargs = {}
        kwargs["action"] = "ListReleaseConfigPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReleaseConfigPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReleaseDocPreview(
            self,
            request: models.ListReleaseDocPreviewRequest,
            opts: Dict = None,
    ) -> models.ListReleaseDocPreviewResponse:
        """
        This API is used to preview released documents.
        """
        
        kwargs = {}
        kwargs["action"] = "ListReleaseDocPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReleaseDocPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReleaseQAPreview(
            self,
            request: models.ListReleaseQAPreviewRequest,
            opts: Dict = None,
    ) -> models.ListReleaseQAPreviewResponse:
        """
        List of documents.
        """
        
        kwargs = {}
        kwargs["action"] = "ListReleaseQAPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReleaseQAPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSelectDoc(
            self,
            request: models.ListSelectDocRequest,
            opts: Dict = None,
    ) -> models.ListSelectDocResponse:
        """
        This API is used to get account information.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSelectDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSelectDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUnsatisfiedReply(
            self,
            request: models.ListUnsatisfiedReplyRequest,
            opts: Dict = None,
    ) -> models.ListUnsatisfiedReplyResponse:
        """
        This API is used to query a list of dissatisfied responses.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUnsatisfiedReply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUnsatisfiedReplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsageCallDetail(
            self,
            request: models.ListUsageCallDetailRequest,
            opts: Dict = None,
    ) -> models.ListUsageCallDetailResponse:
        """
        This API is used to query single call details in a list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsageCallDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsageCallDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApp(
            self,
            request: models.ModifyAppRequest,
            opts: Dict = None,
    ) -> models.ModifyAppResponse:
        """
        This API is used to modify application request structure.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAttributeLabel(
            self,
            request: models.ModifyAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.ModifyAttributeLabelResponse:
        """
        This API is used to edit attribute labels.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDoc(
            self,
            request: models.ModifyDocRequest,
            opts: Dict = None,
    ) -> models.ModifyDocResponse:
        """
        This API is used to modify documents.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDocAttrRange(
            self,
            request: models.ModifyDocAttrRangeRequest,
            opts: Dict = None,
    ) -> models.ModifyDocAttrRangeResponse:
        """
        This API is used to modify applicable scope of the document in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDocAttrRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDocAttrRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDocCate(
            self,
            request: models.ModifyDocCateRequest,
            opts: Dict = None,
    ) -> models.ModifyDocCateResponse:
        """
        This API is used to modify Doc categories.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDocCate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDocCateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyQA(
            self,
            request: models.ModifyQARequest,
            opts: Dict = None,
    ) -> models.ModifyQAResponse:
        """
        This API is used to update Q&As.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyQAAttrRange(
            self,
            request: models.ModifyQAAttrRangeRequest,
            opts: Dict = None,
    ) -> models.ModifyQAAttrRangeResponse:
        """
        This API is used to modify Q&A applicable scope in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyQAAttrRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyQAAttrRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyQACate(
            self,
            request: models.ModifyQACateRequest,
            opts: Dict = None,
    ) -> models.ModifyQACateResponse:
        """
        This API is used to modify Q&A categories.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyQACate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyQACateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRejectedQuestion(
            self,
            request: models.ModifyRejectedQuestionRequest,
            opts: Dict = None,
    ) -> models.ModifyRejectedQuestionResponse:
        """
        This API is used to modify rejected questions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRejectedQuestion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRejectedQuestionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RateMsgRecord(
            self,
            request: models.RateMsgRecordRequest,
            opts: Dict = None,
    ) -> models.RateMsgRecordResponse:
        """
        This API is used to show messages for likes and dislikes.
        """
        
        kwargs = {}
        kwargs["action"] = "RateMsgRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RateMsgRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenameDoc(
            self,
            request: models.RenameDocRequest,
            opts: Dict = None,
    ) -> models.RenameDocResponse:
        """
        This API is used to rename a document.
        """
        
        kwargs = {}
        kwargs["action"] = "RenameDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenameDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryDocAudit(
            self,
            request: models.RetryDocAuditRequest,
            opts: Dict = None,
    ) -> models.RetryDocAuditResponse:
        """
        This API is used to retry document parsing.
        """
        
        kwargs = {}
        kwargs["action"] = "RetryDocAudit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryDocAuditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryDocParse(
            self,
            request: models.RetryDocParseRequest,
            opts: Dict = None,
    ) -> models.RetryDocParseResponse:
        """
        This API is used to retry document parsing.
        """
        
        kwargs = {}
        kwargs["action"] = "RetryDocParse"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryDocParseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryRelease(
            self,
            request: models.RetryReleaseRequest,
            opts: Dict = None,
    ) -> models.RetryReleaseResponse:
        """
        This API is used to retry after release suspension.
        """
        
        kwargs = {}
        kwargs["action"] = "RetryRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SaveDoc(
            self,
            request: models.SaveDocRequest,
            opts: Dict = None,
    ) -> models.SaveDocResponse:
        """
        This API is used to save a knowledge base document Q&As.
        Three steps to store a file in the knowledge library of the application:
        1. Obtain a temporary key. For more information, see [API Documentation](https://cloud.tencent.com/document/product/1759/105050). Different parameter combinations of the temporary key have different permissions. For more information, see [Tencent Cloud Agent Development Platform/ADP COS Guide](https://cloud.tencent.com/document/product/1759/116238).
        2. Call the COS storage API provided by Tencent Cloud to store the file in the COS of ADP. For details, see [COS SDK Overview](https://cloud.tencent.com/document/product/436/6474). Note that the temporary key method is used to operate COS.
        3. Call this API to store the basic information of the file in ADP.
        For the above steps, see [Documentation](https://cloud.tencent.com/document/product/1759/108903). At the end of the documentation, there is a [code demo](https://cloud.tencent.com/document/product/1759/108903#demo), which can be used as a reference.
        """
        
        kwargs = {}
        kwargs["action"] = "SaveDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SaveDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopDocParse(
            self,
            request: models.StopDocParseRequest,
            opts: Dict = None,
    ) -> models.StopDocParseResponse:
        """
        This API is used to terminate document parsing.
        """
        
        kwargs = {}
        kwargs["action"] = "StopDocParse"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopDocParseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadAttributeLabel(
            self,
            request: models.UploadAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.UploadAttributeLabelResponse:
        """
        This API is used to upload and import attribute labels.
        """
        
        kwargs = {}
        kwargs["action"] = "UploadAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyQA(
            self,
            request: models.VerifyQARequest,
            opts: Dict = None,
    ) -> models.VerifyQAResponse:
        """
        This API is used to verify Q&A.
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)