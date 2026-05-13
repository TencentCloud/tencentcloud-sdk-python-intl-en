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
from tencentcloud.ccc.v20200210 import models
from typing import Dict


class CccClient(AbstractClient):
    _apiVersion = '2020-02-10'
    _endpoint = 'ccc.intl.tencentcloudapi.com'
    _service = 'ccc'

    async def AbortAgentCruiseDialingCampaign(
            self,
            request: models.AbortAgentCruiseDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.AbortAgentCruiseDialingCampaignResponse:
        """
        Stop Agent Cruise-style Outbound Call Task
        """
        
        kwargs = {}
        kwargs["action"] = "AbortAgentCruiseDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AbortAgentCruiseDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AbortPredictiveDialingCampaign(
            self,
            request: models.AbortPredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.AbortPredictiveDialingCampaignResponse:
        """
        This API is used to pause the predictive outbound call task.
        """
        
        kwargs = {}
        kwargs["action"] = "AbortPredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AbortPredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindNumberCallInInterface(
            self,
            request: models.BindNumberCallInInterfaceRequest,
            opts: Dict = None,
    ) -> models.BindNumberCallInInterfaceResponse:
        """
        This API is used to bind a number to a callback API for incoming calls.
        """
        
        kwargs = {}
        kwargs["action"] = "BindNumberCallInInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindNumberCallInInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindNumberCallOutSkillGroup(
            self,
            request: models.BindNumberCallOutSkillGroupRequest,
            opts: Dict = None,
    ) -> models.BindNumberCallOutSkillGroupResponse:
        """
        This API is used to bind outbound skill group of number.
        """
        
        kwargs = {}
        kwargs["action"] = "BindNumberCallOutSkillGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindNumberCallOutSkillGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindStaffSkillGroupList(
            self,
            request: models.BindStaffSkillGroupListRequest,
            opts: Dict = None,
    ) -> models.BindStaffSkillGroupListResponse:
        """
        This API is used to bind the agent's skill group.
        """
        
        kwargs = {}
        kwargs["action"] = "BindStaffSkillGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindStaffSkillGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlAIConversation(
            self,
            request: models.ControlAIConversationRequest,
            opts: Dict = None,
    ) -> models.ControlAIConversationResponse:
        """
        This API is used to provide server-side robot control feature.
        """
        
        kwargs = {}
        kwargs["action"] = "ControlAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIAgentCall(
            self,
            request: models.CreateAIAgentCallRequest,
            opts: Dict = None,
    ) -> models.CreateAIAgentCallResponse:
        """
        Used to create one-time Intelligent Agent outbound calls. You can create a voice Intelligent Agent in the management console - Intelligent Agent Management and perform dialogue process configuration (https://www.tencentcloud.com/document/product/679/119796?from_cn_redirect=1). This API is used to initiate a single outbound call task with a configured Intelligent Agent. To create batch Intelligent Agent outbound call tasks, refer to the documentation for creating automatic outbound call tasks (https://www.tencentcloud.com/document/product/679/69194?from_cn_redirect=1).

        The feature requires purchase of the Intelligent Agent call package and is only available for own telephone number. For details, refer to the [Intelligent Agent Call Purchase Guide](https://www.tencentcloud.com/document/product/679/125953?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIAgentCall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIAgentCallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAICall(
            self,
            request: models.CreateAICallRequest,
            opts: Dict = None,
    ) -> models.CreateAICallResponse:
        """
        This API is used to **call the AI model directly** to trigger a **single** outbound call. It supports configuring the model, prompt content, voice, and all call elements through API parameters.

        The feature requires purchase of the Intelligent Agent call package and is only available for own telephone numbers. For details, refer to the Intelligent Agent Call Purchase Guide (https://www.tencentcloud.com/document/product/679/125953?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAICall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAICallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAdminURL(
            self,
            request: models.CreateAdminURLRequest,
            opts: Dict = None,
    ) -> models.CreateAdminURLResponse:
        """
        This API is used to create a management access link.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAdminURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAdminURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentCruiseDialingCampaign(
            self,
            request: models.CreateAgentCruiseDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.CreateAgentCruiseDialingCampaignResponse:
        """
        Agent Cruise-style Outbound Call.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentCruiseDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentCruiseDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoCalloutTask(
            self,
            request: models.CreateAutoCalloutTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAutoCalloutTaskResponse:
        """
        This API is used to create bulk automatic outbound calls. The system will automatically initiate outbound calls to the designated called number list based on task configuration. This API can call the configured Intelligent Agent to perform batch outbound call tasks. You can create a voice Intelligent Agent in the management console-Intelligent Agent Management and configure the dialogue process (https://www.tencentcloud.com/document/product/679/119796?from_cn_redirect=1). To create a single Intelligent Agent outbound call task, refer to the documentation (https://www.tencentcloud.com/document/product/679/115681?from_cn_redirect=1).

        The feature requires purchase of the Intelligent Agent call package and is only available for own telephone number.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoCalloutTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoCalloutTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCCCSkillGroup(
            self,
            request: models.CreateCCCSkillGroupRequest,
            opts: Dict = None,
    ) -> models.CreateCCCSkillGroupResponse:
        """
        This API is used to create a new skill group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCCCSkillGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCCCSkillGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCallOutSession(
            self,
            request: models.CreateCallOutSessionRequest,
            opts: Dict = None,
    ) -> models.CreateCallOutSessionResponse:
        """
        This API is used to create an outbound call session. Currently, only dual calls are supported. That is, first use the platform number to call the agent mobile phone. After the agent answers, then make an outbound call to the user. Moreover, due to ISP frequency restrictions, the agent phone number must be added to the allowlist first to avoid frequency control leading to the failure of the outbound call. Therefore, before calling this API, the following operations have been completed.
        1. The agent specified by UserId has already bound the mobile number. https://intl.cloud.tencent.com/document/product/679/76067?from_cn_redirect=1#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E5.AE.8C.E5.96.84.E8.B4.A6.E5.8F.B7.E4.BF.A1.E6.81.AF.
        2. The agent's bound mobile number has applied for and passed the outbound call allowlist.
        This API is used to make calls. Currently, the agent side can only call the user's mobile phone, so the IsForceMobile field must be true.
        4. Do not fill in the mobile number bound to the current UserId for the callee, otherwise it can lead to call failure due to a busy line.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCallOutSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCallOutSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExtension(
            self,
            request: models.CreateExtensionRequest,
            opts: Dict = None,
    ) -> models.CreateExtensionResponse:
        """
        This API is used to create the telephone account.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExtension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExtensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIVRSession(
            self,
            request: models.CreateIVRSessionRequest,
            opts: Dict = None,
    ) -> models.CreateIVRSessionResponse:
        """
        Create a session associated with IVR. This feature is supported only in the Advanced Version. Currently, it supports inbound and automatic outbound IVR types. Upon receiving the request, TCCC will first attempt to call the callee, then enter the IVR flow.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIVRSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIVRSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOwnNumberApply(
            self,
            request: models.CreateOwnNumberApplyRequest,
            opts: Dict = None,
    ) -> models.CreateOwnNumberApplyResponse:
        """
        Create customer's own number access review
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOwnNumberApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOwnNumberApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePredictiveDialingCampaign(
            self,
            request: models.CreatePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.CreatePredictiveDialingCampaignResponse:
        """
        This API is used to create the predictive outbound call task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSDKLoginToken(
            self,
            request: models.CreateSDKLoginTokenRequest,
            opts: Dict = None,
    ) -> models.CreateSDKLoginTokenResponse:
        """
        This API is used to create the SDK log-in token.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSDKLoginToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSDKLoginTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStaff(
            self,
            request: models.CreateStaffRequest,
            opts: Dict = None,
    ) -> models.CreateStaffResponse:
        """
        This API is used to create the customer service account.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStaff"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStaffResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserSig(
            self,
            request: models.CreateUserSigRequest,
            opts: Dict = None,
    ) -> models.CreateUserSigResponse:
        """
        This API is used to create a user data signature.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserSig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserSigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCCSkillGroup(
            self,
            request: models.DeleteCCCSkillGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteCCCSkillGroupResponse:
        """
        This API is used to delete a skill group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCCSkillGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCCSkillGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteExtension(
            self,
            request: models.DeleteExtensionRequest,
            opts: Dict = None,
    ) -> models.DeleteExtensionResponse:
        """
        This API is used to delete telephone accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteExtension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteExtensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePredictiveDialingCampaign(
            self,
            request: models.DeletePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.DeletePredictiveDialingCampaignResponse:
        """
        This API is used to delete the predictive outbound call task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStaff(
            self,
            request: models.DeleteStaffRequest,
            opts: Dict = None,
    ) -> models.DeleteStaffResponse:
        """
        This API is used to delete the agent information.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStaff"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStaffResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAgentInfoList(
            self,
            request: models.DescribeAIAgentInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAgentInfoListResponse:
        """
        This API is used to query the information list of configured Intelligent Agents under a specified instance (SdkAppId) by paging, including basic information such as Intelligent Agent ID and name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAgentInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAgentInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisResult(
            self,
            request: models.DescribeAIAnalysisResultRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisResultResponse:
        """
        This API is used to obtain AI Conversation Analytics results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAICallExtractResult(
            self,
            request: models.DescribeAICallExtractResultRequest,
            opts: Dict = None,
    ) -> models.DescribeAICallExtractResultResponse:
        """
        This API is used to query specified session's post-call Tag results by Session ID after the Intelligent Agent call session ends. Related post-call Tags need to be configured in advance in the management console. For details, please refer to post-call Tags (https://www.tencentcloud.com/document/product/679/119800?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAICallExtractResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAICallExtractResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAILatency(
            self,
            request: models.DescribeAILatencyRequest,
            opts: Dict = None,
    ) -> models.DescribeAILatencyResponse:
        """
        Call this API to query the processing latency detail and stats of specified Session by Session ID within a specific time period. The latency info includes:.
        -End-to-end (ETE) delay: Statistics of the overall duration from user voice input to AI returning a complete response.
        -ASR latency: statistics of the processing time consumption required for voice input to be recognized as text.
        -LLM latency: Statistics of inference latency for AI model to generate text content.
        -Text To Speech (TTS) latency: Statistics of text conversion to speech audio synthesis duration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAILatency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAILatencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentCruiseDialingCampaign(
            self,
            request: models.DescribeAgentCruiseDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentCruiseDialingCampaignResponse:
        """
        Query Agent Cruise-style Outbound Call Task
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentCruiseDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentCruiseDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoCalloutTask(
            self,
            request: models.DescribeAutoCalloutTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoCalloutTaskResponse:
        """
        This API is used to query detailed information of an automatic outbound call task by TaskId, including basic configuration, start and end time, name list, execution status, and call status.
        This API is usually used together with Create Bulk Automatic Outbound Call Task (https://www.tencentcloud.com/document/product/679/69194?from_cn_redirect=1) to check whether the task configuration takes effect, the current task status, and real-time progress during execution once created.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoCalloutTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoCalloutTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoCalloutTasks(
            self,
            request: models.DescribeAutoCalloutTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoCalloutTasksResponse:
        """
        Batch Query Automatic Outbound Call Tasks
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoCalloutTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoCalloutTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCCBuyInfoList(
            self,
            request: models.DescribeCCCBuyInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCCBuyInfoListResponse:
        """
        This API is used to access the user purchasing information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCCBuyInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCCBuyInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallInMetrics(
            self,
            request: models.DescribeCallInMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeCallInMetricsResponse:
        """
        This API is used to access the inbound real-time data statistical metrics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallInMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallInMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExtension(
            self,
            request: models.DescribeExtensionRequest,
            opts: Dict = None,
    ) -> models.DescribeExtensionResponse:
        """
        This API is used to access the telephone information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExtension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExtensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExtensions(
            self,
            request: models.DescribeExtensionsRequest,
            opts: Dict = None,
    ) -> models.DescribeExtensionsResponse:
        """
        This API is used to query the telephone list information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExtensions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExtensionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIvrAudioList(
            self,
            request: models.DescribeIvrAudioListRequest,
            opts: Dict = None,
    ) -> models.DescribeIvrAudioListResponse:
        """
        Query IVR Audio File List Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIvrAudioList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIvrAudioListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNumbers(
            self,
            request: models.DescribeNumbersRequest,
            opts: Dict = None,
    ) -> models.DescribeNumbersResponse:
        """
        This API is used to query the number list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNumbers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNumbersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePSTNActiveSessionList(
            self,
            request: models.DescribePSTNActiveSessionListRequest,
            opts: Dict = None,
    ) -> models.DescribePSTNActiveSessionListResponse:
        """
        This API is used to access the current calling session list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePSTNActiveSessionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePSTNActiveSessionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePredictiveDialingCampaign(
            self,
            request: models.DescribePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.DescribePredictiveDialingCampaignResponse:
        """
        This API is used to query the predictive outbound call task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePredictiveDialingCampaigns(
            self,
            request: models.DescribePredictiveDialingCampaignsRequest,
            opts: Dict = None,
    ) -> models.DescribePredictiveDialingCampaignsResponse:
        """
        This API is used to query the predictive outbound call task list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePredictiveDialingCampaigns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePredictiveDialingCampaignsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePredictiveDialingSessions(
            self,
            request: models.DescribePredictiveDialingSessionsRequest,
            opts: Dict = None,
    ) -> models.DescribePredictiveDialingSessionsResponse:
        """
        This API is used to query the predictive outbound call list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePredictiveDialingSessions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePredictiveDialingSessionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProtectedTelCdr(
            self,
            request: models.DescribeProtectedTelCdrRequest,
            opts: Dict = None,
    ) -> models.DescribeProtectedTelCdrResponse:
        """
        This API is used to access protected phone service records and recordings for both inbound and outbound calls.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProtectedTelCdr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProtectedTelCdrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionDetail(
            self,
            request: models.DescribeSessionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionDetailResponse:
        """
        This API is used to query call details for a single call by session id and timestamp after call ends, including caller and contact information, voice recording.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillGroupInfoList(
            self,
            request: models.DescribeSkillGroupInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillGroupInfoListResponse:
        """
        This API is used to access the skill group information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillGroupInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillGroupInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStaffInfoList(
            self,
            request: models.DescribeStaffInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeStaffInfoListResponse:
        """
        This API is used to access the agent information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStaffInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStaffInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStaffStatusHistory(
            self,
            request: models.DescribeStaffStatusHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeStaffStatusHistoryResponse:
        """
        This API is used to query agent status history.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStaffStatusHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStaffStatusHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStaffStatusMetrics(
            self,
            request: models.DescribeStaffStatusMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeStaffStatusMetricsResponse:
        """
        This API is used to access the real-time status statistics metrics of the agent.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStaffStatusMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStaffStatusMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTelCallInfo(
            self,
            request: models.DescribeTelCallInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTelCallInfoResponse:
        """
        This API is used to access telephone consumption statistics by instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTelCallInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTelCallInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTelCdr(
            self,
            request: models.DescribeTelCdrRequest,
            opts: Dict = None,
    ) -> models.DescribeTelCdrResponse:
        """
        This API is used to access phone service records and recordings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTelCdr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTelCdrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTelRecordAsr(
            self,
            request: models.DescribeTelRecordAsrRequest,
            opts: Dict = None,
    ) -> models.DescribeTelRecordAsrResponse:
        """
        Pull conversation recording for text information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTelRecordAsr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTelRecordAsrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTelSession(
            self,
            request: models.DescribeTelSessionRequest,
            opts: Dict = None,
    ) -> models.DescribeTelSessionResponse:
        """
        This API is used to access the PSTN session information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTelSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTelSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableCCCPhoneNumber(
            self,
            request: models.DisableCCCPhoneNumberRequest,
            opts: Dict = None,
    ) -> models.DisableCCCPhoneNumberResponse:
        """
        This API is used to disable numbers.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableCCCPhoneNumber"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableCCCPhoneNumberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForceMemberOffline(
            self,
            request: models.ForceMemberOfflineRequest,
            opts: Dict = None,
    ) -> models.ForceMemberOfflineResponse:
        """
        This API is used to force customer service to go offline.
        """
        
        kwargs = {}
        kwargs["action"] = "ForceMemberOffline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForceMemberOfflineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HangUpCall(
            self,
            request: models.HangUpCallRequest,
            opts: Dict = None,
    ) -> models.HangUpCallResponse:
        """
        This API is used to hang up the phone.
        """
        
        kwargs = {}
        kwargs["action"] = "HangUpCall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HangUpCallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExtension(
            self,
            request: models.ModifyExtensionRequest,
            opts: Dict = None,
    ) -> models.ModifyExtensionResponse:
        """
        This API is used to modify telephone accounts (binding skill group, binding agent account).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExtension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExtensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwnNumberApply(
            self,
            request: models.ModifyOwnNumberApplyRequest,
            opts: Dict = None,
    ) -> models.ModifyOwnNumberApplyResponse:
        """
        Modify customer's own number approval form
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwnNumberApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwnNumberApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStaff(
            self,
            request: models.ModifyStaffRequest,
            opts: Dict = None,
    ) -> models.ModifyStaffResponse:
        """
        This API is used to modify the customer service account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStaff"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStaffResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStaffPassword(
            self,
            request: models.ModifyStaffPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyStaffPasswordResponse:
        """
        Modify Agent's Password
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStaffPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStaffPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseAutoCalloutTask(
            self,
            request: models.PauseAutoCalloutTaskRequest,
            opts: Dict = None,
    ) -> models.PauseAutoCalloutTaskResponse:
        """
        This API is used to suspend an ongoing automatic outbound call task by TaskId. After calling this API, the task will be temporarily interrupted and no longer initiate new outbound call requests; initiated calls are not affected.
        A paused task can continue execution via the [Restore Suspended Automatic Outbound Call Task](https://www.tencentcloud.com/document/product/679/125356?from_cn_redirect=1) API. If needed, refer to [Stop Automatic Outbound Call Task](https://www.tencentcloud.com/document/product/679/69192?from_cn_redirect=1) to permanently terminate the task.
        """
        
        kwargs = {}
        kwargs["action"] = "PauseAutoCalloutTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseAutoCalloutTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PausePredictiveDialingCampaign(
            self,
            request: models.PausePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.PausePredictiveDialingCampaignResponse:
        """
        This API is used to pause the predictive outbound call task.
        """
        
        kwargs = {}
        kwargs["action"] = "PausePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PausePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PlaySoundCall(
            self,
            request: models.PlaySoundCallRequest,
            opts: Dict = None,
    ) -> models.PlaySoundCallResponse:
        """
        This API is used to perform playback for a session in a call with an agent.
        """
        
        kwargs = {}
        kwargs["action"] = "PlaySoundCall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PlaySoundCallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetExtensionPassword(
            self,
            request: models.ResetExtensionPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetExtensionPasswordResponse:
        """
        This API is used to reset the telephone register password.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetExtensionPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetExtensionPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreMemberOnline(
            self,
            request: models.RestoreMemberOnlineRequest,
            opts: Dict = None,
    ) -> models.RestoreMemberOnlineResponse:
        """
        This API is used to restore customer service to go live.
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreMemberOnline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreMemberOnlineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeAutoCalloutTask(
            self,
            request: models.ResumeAutoCalloutTaskRequest,
            opts: Dict = None,
    ) -> models.ResumeAutoCalloutTaskResponse:
        """
        This API is used to restore a paused automatic outbound call task by TaskId. This API is suitable for scenarios where you need to continue execution of the remaining outbound call plan after calling Suspend Automatic Outbound Call Task. After a successful call, the task will resume from the paused state and re-initiate incomplete outbound requests.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeAutoCalloutTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeAutoCalloutTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumePredictiveDialingCampaign(
            self,
            request: models.ResumePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.ResumePredictiveDialingCampaignResponse:
        """
        This API is used to resume the predictive outbound call task.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetStaffStatus(
            self,
            request: models.SetStaffStatusRequest,
            opts: Dict = None,
    ) -> models.SetStaffStatusResponse:
        """
        This API is used to set staff status.
        """
        
        kwargs = {}
        kwargs["action"] = "SetStaffStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetStaffStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAutoCalloutTask(
            self,
            request: models.StopAutoCalloutTaskRequest,
            opts: Dict = None,
    ) -> models.StopAutoCalloutTaskResponse:
        """
        This API is used to stop the automatic outbound call task.
        """
        
        kwargs = {}
        kwargs["action"] = "StopAutoCalloutTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAutoCalloutTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransferToManual(
            self,
            request: models.TransferToManualRequest,
            opts: Dict = None,
    ) -> models.TransferToManualResponse:
        """
        This API is used to transfer a session to an agent in specific scenarios.
        """
        
        kwargs = {}
        kwargs["action"] = "TransferToManual"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransferToManualResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindNumberCallOutSkillGroup(
            self,
            request: models.UnbindNumberCallOutSkillGroupRequest,
            opts: Dict = None,
    ) -> models.UnbindNumberCallOutSkillGroupResponse:
        """
        This API is used to unbind the number from the outbound call skill group.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindNumberCallOutSkillGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindNumberCallOutSkillGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindStaffSkillGroupList(
            self,
            request: models.UnbindStaffSkillGroupListRequest,
            opts: Dict = None,
    ) -> models.UnbindStaffSkillGroupListResponse:
        """
        This API is used to unbind the agent's skill group.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindStaffSkillGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindStaffSkillGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCCCSkillGroup(
            self,
            request: models.UpdateCCCSkillGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateCCCSkillGroupResponse:
        """
        This API is used to update the skill group.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCCCSkillGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCCCSkillGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePredictiveDialingCampaign(
            self,
            request: models.UpdatePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.UpdatePredictiveDialingCampaignResponse:
        """
        This API is used to update the predictive outbound call task before it starts.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadIvrAudio(
            self,
            request: models.UploadIvrAudioRequest,
            opts: Dict = None,
    ) -> models.UploadIvrAudioResponse:
        """
        Upload audio files used in IVR, with a daily upload limit of 50 files. (It is recommended to use temporary links stored in Tencent Cloud Cos for the audio file URL in the parameters)
        """
        
        kwargs = {}
        kwargs["action"] = "UploadIvrAudio"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadIvrAudioResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)