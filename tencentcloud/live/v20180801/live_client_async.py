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
from tencentcloud.live.v20180801 import models
from typing import Dict


class LiveClient(AbstractClient):
    _apiVersion = '2018-08-01'
    _endpoint = 'live.intl.tencentcloudapi.com'
    _service = 'live'

    async def AddDelayLiveStream(
            self,
            request: models.AddDelayLiveStreamRequest,
            opts: Dict = None,
    ) -> models.AddDelayLiveStreamResponse:
        """
        This API is used to set a delay in playing the images of large live streaming events, in case of emergencies.

        Note: if you are to set the delay before stream push, set it at least 5 minutes before the push. This API supports configuration only by stream.
        """
        
        kwargs = {}
        kwargs["action"] = "AddDelayLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDelayLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddLiveDomain(
            self,
            request: models.AddLiveDomainRequest,
            opts: Dict = None,
    ) -> models.AddLiveDomainResponse:
        """
        This API is used to add a domain name. Only one domain name can be submitted at a time, and it must have an ICP filing.
        """
        
        kwargs = {}
        kwargs["action"] = "AddLiveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddLiveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddLiveWatermark(
            self,
            request: models.AddLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.AddLiveWatermarkResponse:
        """
        After a watermark is added and a watermark ID is successfully returned, you need to call the [CreateLiveWatermarkRule](https://intl.cloud.tencent.com/document/product/267/32629?from_cn_redirect=1) API to bind the watermark ID to a stream.
        After the number of watermarks exceeds the upper limit of 100, to add a new watermark, you must delete an old one first.
        """
        
        kwargs = {}
        kwargs["action"] = "AddLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AuthenticateDomainOwner(
            self,
            request: models.AuthenticateDomainOwnerRequest,
            opts: Dict = None,
    ) -> models.AuthenticateDomainOwnerResponse:
        """
        This API is used to verify the ownership of a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "AuthenticateDomainOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AuthenticateDomainOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelCommonMixStream(
            self,
            request: models.CancelCommonMixStreamRequest,
            opts: Dict = None,
    ) -> models.CancelCommonMixStreamResponse:
        """
        This API is used to cancel a stream mix. It can be used basically in the same way as `mix_streamv2.cancel_mix_stream`.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelCommonMixStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelCommonMixStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCommonMixStream(
            self,
            request: models.CreateCommonMixStreamRequest,
            opts: Dict = None,
    ) -> models.CreateCommonMixStreamResponse:
        """
        This API is used to create a general stream mix. It can be used basically in the same way as the legacy `mix_streamv2.start_mix_stream_advanced` API.
        Note: currently, up to 16 streams can be mixed.
        Best practice: https://intl.cloud.tencent.com/document/product/267/45566?from_cn_redirect=1
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCommonMixStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCommonMixStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveCallbackRule(
            self,
            request: models.CreateLiveCallbackRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveCallbackRuleResponse:
        """
        To create a callback rule, you need to first call the [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1) API to create a callback template and bind the returned template ID to the domain name/path.
        <br>Callback protocol-related document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveCallbackRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveCallbackRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveCallbackTemplate(
            self,
            request: models.CreateLiveCallbackTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveCallbackTemplateResponse:
        """
        This API is used to create a callback template. Up to 50 templates can be created. After the template ID is returned, you need to call the [CreateLiveCallbackRule](https://intl.cloud.tencent.com/document/product/267/32638?from_cn_redirect=1) API to bind the template ID to a domain name/path.
        <br>For information about callback protocols, see [How to Receive Event Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).
        Note: You need to specify at least one callback URL.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveCallbackTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveCallbackTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLivePadRule(
            self,
            request: models.CreateLivePadRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLivePadRuleResponse:
        """
        create a live pad rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLivePadRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLivePadRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLivePadTemplate(
            self,
            request: models.CreateLivePadTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLivePadTemplateResponse:
        """
        create a live pad template
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLivePadTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLivePadTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLivePullStreamTask(
            self,
            request: models.CreateLivePullStreamTaskRequest,
            opts: Dict = None,
    ) -> models.CreateLivePullStreamTaskResponse:
        """
        This API is used to create a task to pull streams from video files or an external live streaming source and publish them to a specified destination URL.
        Notes:
        1. By default, you can have at most 20 stream pulling tasks at a time. You can submit a ticket to raise the limit.
        2. Only H.264 and H.265 are supported for video. If the source video is in a different format, please transcode it first.
        3. Only AAC is supported for audio. If the source audio is in a different format, please transcode it first.
        4. You can enable auto deletion in the console to delete expired tasks automatically.
        5. The pull and relay feature is a paid feature. For its billing details, see [Relay](https://intl.cloud.tencent.com/document/product/267/53308?from_cn_redirect=1).
        6. CSS is only responsible for pulling and relaying content. Please make sure that your content is authorized and complies with relevant laws and regulations. In case of copyright infringement or violation of laws or regulations, CSS will suspend its service for you and reserves the right to seek legal remedies.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLivePullStreamTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLivePullStreamTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveRecord(
            self,
            request: models.CreateLiveRecordRequest,
            opts: Dict = None,
    ) -> models.CreateLiveRecordResponse:
        """
        - Prerequisites
          1. Recording files are stored on the VOD platform, so if you need to use the recording feature, you must first activate the VOD service.
          2. After the recording files are stored, applicable fees (including storage fees and downstream playback traffic fees) will be charged according to the VOD billing mode. For more information, please see the [corresponding document](https://intl.cloud.tencent.com/document/product/266/2838?from_cn_redirect=1).

        - Mode description
          This API supports two recording modes:
          1. Scheduled recording mode **(default mode)**.
            The start time and end time need to be passed in, according to which the recording task will start and end automatically. Before the set end time expires (provided that `StopLiveRecord` is not called to terminate the task prematurely), the recording task is valid and will be started even after the push is interrupted and restarted multiple times.
          2. Real-time video recording mode.
            The start time passed in will be ignored, and recording will be started immediately after the recording task is created. The recording duration can be up to 30 minutes. If the end time passed in is more than 30 minutes after the current time, it will be counted as 30 minutes. Real-time video recording is mainly used for recording highlight scenes, and you are recommended to keep the duration within 5 minutes.

        - Precautions
          1. The API call timeout period should be set to more than 3 seconds; otherwise, retries and calls by different start/end time values may result in repeated recording tasks and thus incur additional recording fees.
          2. Subject to the audio and video file formats (FLV/MP4/HLS), the video codec of H.264 and audio codec of AAC are supported.
          3. In order to avoid malicious or unintended frequent API requests, the maximum number of tasks that can be created in scheduled recording mode is limited: up to 4,000 tasks can be created per day (excluding deleted ones), and up to 400 ones can run concurrently. If you need a higher upper limit, please submit a ticket for application.
          4. This calling method does not support recording streams outside Mainland China for the time being.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveRecordRule(
            self,
            request: models.CreateLiveRecordRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveRecordRuleResponse:
        """
        To create a recording rule, you need to first call the [CreateLiveRecordTemplate](https://intl.cloud.tencent.com/document/product/267/32614?from_cn_redirect=1) API to create a recording template and bind the returned template ID to the stream.
        <br>Recording-related document: [LVB Recording](https://intl.cloud.tencent.com/document/product/267/32739?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveRecordRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveRecordRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveRecordTemplate(
            self,
            request: models.CreateLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveRecordTemplateResponse:
        """
        This API is used to create a recording template. You can create up to 50 templates. To use a template, you need to call the [CreateLiveRecordRule](https://intl.cloud.tencent.com/document/product/267/32615?from_cn_redirect=1) API to bind the template ID returned by this API to a stream.
        <br>More on recording: [Live Recording](https://intl.cloud.tencent.com/document/product/267/32739?from_cn_redirect=1)
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveSnapshotRule(
            self,
            request: models.CreateLiveSnapshotRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveSnapshotRuleResponse:
        """
        This API is used to create a screencapturing rule. You need to first call the [CreateLiveSnapshotTemplate](https://intl.cloud.tencent.com/document/product/267/32624?from_cn_redirect=1) API to create a screencapturing template to bind the returned template ID to the stream.
        <br>Screencapturing document: [LVB Screencapturing](https://intl.cloud.tencent.com/document/product/267/32737?from_cn_redirect=1).
        Note: only one screencapturing template can be associated with one domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveSnapshotRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveSnapshotRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveSnapshotTemplate(
            self,
            request: models.CreateLiveSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveSnapshotTemplateResponse:
        """
        This API is used to create a screencapture template. After a template ID is returned, you need to call the [CreateLiveSnapshotRule](https://intl.cloud.tencent.com/document/product/267/32625?from_cn_redirect=1) API to bind the template ID to a stream. You can create up to 50 screencapture templates.
        <br>To learn more about the live screencapture feature, see [Live Screencapture](https://intl.cloud.tencent.com/document/product/267/32737?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveTimeShiftRule(
            self,
            request: models.CreateLiveTimeShiftRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveTimeShiftRuleResponse:
        """
        This API is used to create a time shifting rule. You need to first call the [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/86169?from_cn_redirect=1) API to create a time shifting template, and then call this API to bind the template ID returned to a stream.
        <br>More about time shifting: [Time Shifting](https://intl.cloud.tencent.com/document/product/267/86134?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveTimeShiftRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveTimeShiftRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveTimeShiftTemplate(
            self,
            request: models.CreateLiveTimeShiftTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveTimeShiftTemplateResponse:
        """
        This API is used to create a time shifting template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveTimeShiftTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveTimeShiftTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveTranscodeRule(
            self,
            request: models.CreateLiveTranscodeRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveTranscodeRuleResponse:
        """
        This API is used to create a transcoding rule that binds a template ID to a stream. Up to 50 transcoding rules can be created in total. Before you call this API, you need to first call [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1) to get the template ID.
        <br>Related document: [Live Remuxing and Transcoding](https://intl.cloud.tencent.com/document/product/267/32736?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveTranscodeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveTranscodeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveTranscodeTemplate(
            self,
            request: models.CreateLiveTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveTranscodeTemplateResponse:
        """
        This API is used to create a transcoding template. Up to 50 transcoding templates can be created in total. To use a template, you need to call [CreateLiveTranscodeRule](https://intl.cloud.tencent.com/document/product/267/32647?from_cn_redirect=1) to bind the template ID returned by this API to a stream.
        <br>For more information about transcoding, see [Live Remuxing and Transcoding](https://intl.cloud.tencent.com/document/product/267/32736?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveWatermarkRule(
            self,
            request: models.CreateLiveWatermarkRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveWatermarkRuleResponse:
        """
        To create a watermarking rule, you need to first call the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API to add a watermark and bind the returned watermark ID to the stream.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveWatermarkRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveWatermarkRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordTask(
            self,
            request: models.CreateRecordTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRecordTaskResponse:
        """
        This API is used to create a recording task that starts and ends at specific times and records videos according to a specific recording template.
        - Prerequisites
        1. Because recording files are saved in VOD, you must first activate VOD.
        2. Storage and playback traffic fees are charged for storing and playing the videos recorded. For details, see [Purchase Guide](https://intl.cloud.tencent.com/document/product/266/2837).
        - Notes
        1. If streaming is interrupted, the current recording will stop and a recording file will be generated. When streaming resumes, as long as it’s before the end time of the task, recording will start again.
        2. Avoid creating recording tasks with overlapping time periods. If there are multiple tasks with overlapping time periods for the same stream, the system will start three recording tasks at most to avoid repeated recording.
        3. Task records are kept for three months by the platform.
        4. Do not use the new [CreateRecordTask](https://intl.cloud.tencent.com/document/product/267/45983?from_cn_redirect=1), [StopRecordTask](https://intl.cloud.tencent.com/document/product/267/45981?from_cn_redirect=1), and [DeleteRecordTask] APIs together with the old `CreateLiveRecord`, `StopLiveRecord`, and `DeleteLiveRecord` APIs.
        5. Do not create recording tasks and push streams at the same time. After creating a recording task, we recommend you wait at least three seconds before pushing streams.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScreenshotTask(
            self,
            request: models.CreateScreenshotTaskRequest,
            opts: Dict = None,
    ) -> models.CreateScreenshotTaskResponse:
        """
        This API is used to create a screencapturing task that has a specific start and end time and takes screenshots according to the template configured.
        - Note
        1. If the stream is interrupted, screencapturing will stop. However, the task will still be valid before the specified end time, and screencapturing will be performed as required after the stream is resumed.
        2. Avoid creating screencapturing tasks with overlapping time periods. The system will execute at most three screencapturing tasks on the same stream at a time.
        3. Task records are only kept for three months.
        4. The new screencapturing APIs (CreateScreenshotTask/StopScreenshotTask/DeleteScreenshotTask) are not compatible with the legacy ones (CreateLiveInstantSnapshot/StopLiveInstantSnapshot). Do not mix them when you call APIs to manage screencapturing tasks.
        5. If you create a screencapturing task and publish the stream at the same time, the task may fail to be executed at the specified time. After creating a screencapturing task, we recommend you wait at least three seconds before publishing the stream.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScreenshotTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScreenshotTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveCallbackRule(
            self,
            request: models.DeleteLiveCallbackRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveCallbackRuleResponse:
        """
        This API is used to delete a callback rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveCallbackRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveCallbackRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveCallbackTemplate(
            self,
            request: models.DeleteLiveCallbackTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveCallbackTemplateResponse:
        """
        This API deletes a callback template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveCallbackTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveCallbackTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveDomain(
            self,
            request: models.DeleteLiveDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveDomainResponse:
        """
        This API is used to delete an added LVB domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLivePullStreamTask(
            self,
            request: models.DeleteLivePullStreamTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteLivePullStreamTaskResponse:
        """
        This API is used to delete a task created by `CreateLivePullStreamTask`.
        Notes:
        1. For the `TaskId` request parameter, pass in the task ID returned by the `CreateLivePullStreamTask` API.
        2. You can query the ID of a task using the `DescribeLivePullStreamTasks` API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLivePullStreamTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLivePullStreamTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveRecord(
            self,
            request: models.DeleteLiveRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveRecordResponse:
        """
        Note: The `DeleteLiveRecord` API is only used to delete the record of recording tasks but not stop recording or deleting an ongoing recording task. If you need to stop a recording task, please use the [StopLiveRecord](https://intl.cloud.tencent.com/document/product/267/30146?from_cn_redirect=1) API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveRecordRule(
            self,
            request: models.DeleteLiveRecordRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveRecordRuleResponse:
        """
        This API is used to delete a recording rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveRecordRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveRecordRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveRecordTemplate(
            self,
            request: models.DeleteLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveRecordTemplateResponse:
        """
        This API is used to delete a recording template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveSnapshotRule(
            self,
            request: models.DeleteLiveSnapshotRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveSnapshotRuleResponse:
        """
        This API is used to delete a screencapturing rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveSnapshotRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveSnapshotRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveSnapshotTemplate(
            self,
            request: models.DeleteLiveSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveSnapshotTemplateResponse:
        """
        This API is used to delete a screencapturing template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveTimeShiftRule(
            self,
            request: models.DeleteLiveTimeShiftRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveTimeShiftRuleResponse:
        """
        This API is used to delete a time shifting rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveTimeShiftRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveTimeShiftRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveTimeShiftTemplate(
            self,
            request: models.DeleteLiveTimeShiftTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveTimeShiftTemplateResponse:
        """
        This API is used to delete a time shifting template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveTimeShiftTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveTimeShiftTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveTranscodeRule(
            self,
            request: models.DeleteLiveTranscodeRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveTranscodeRuleResponse:
        """
        This API is used to delete a transcoding rule.
        `DomainName+AppName+StreamName+TemplateId` uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. `TemplateId` is required. Even if other parameters are empty, you still need to pass in an empty string to make a strong match.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveTranscodeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveTranscodeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveTranscodeTemplate(
            self,
            request: models.DeleteLiveTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveTranscodeTemplateResponse:
        """
        This API is used to delete a transcoding template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveWatermark(
            self,
            request: models.DeleteLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveWatermarkResponse:
        """
        This API is used to delete a watermark.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveWatermarkRule(
            self,
            request: models.DeleteLiveWatermarkRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveWatermarkRuleResponse:
        """
        This API is used to delete a watermarking rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveWatermarkRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveWatermarkRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordTask(
            self,
            request: models.DeleteRecordTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordTaskResponse:
        """
        This API is used to delete a recording task configuration. The deletion does not affect running tasks and takes effect only for new pushes.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllStreamPlayInfoList(
            self,
            request: models.DescribeAllStreamPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAllStreamPlayInfoListResponse:
        """
        This API is used to get the playback data of all streams at a specified time point (accurate to the minute).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllStreamPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllStreamPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillBandwidthAndFluxList(
            self,
            request: models.DescribeBillBandwidthAndFluxListRequest,
            opts: Dict = None,
    ) -> models.DescribeBillBandwidthAndFluxListResponse:
        """
        This API is used to query the data of billable bandwidth and traffic.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillBandwidthAndFluxList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillBandwidthAndFluxListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConcurrentRecordStreamNum(
            self,
            request: models.DescribeConcurrentRecordStreamNumRequest,
            opts: Dict = None,
    ) -> models.DescribeConcurrentRecordStreamNumResponse:
        """
        This API is used to query the number of concurrent recording channels, which is applicable to LCB and LVB.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConcurrentRecordStreamNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConcurrentRecordStreamNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeliverBandwidthList(
            self,
            request: models.DescribeDeliverBandwidthListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeliverBandwidthListResponse:
        """
        This API is used to query the billable bandwidth of live stream relaying in the last 3 months. The query period is up to 31 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeliverBandwidthList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeliverBandwidthListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupProIspPlayInfoList(
            self,
            request: models.DescribeGroupProIspPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupProIspPlayInfoListResponse:
        """
        This API is used to query the downstream playback data by district and ISP.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupProIspPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupProIspPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHttpStatusInfoList(
            self,
            request: models.DescribeHttpStatusInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeHttpStatusInfoListResponse:
        """
        This API is used to query the number of each playback HTTP status code at a 5-minute granularity in a certain period of time.
        Note: data can be queried one hour after it is generated. For example, data between 10:00 and 10:59 cannot be queried until 12:00.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHttpStatusInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHttpStatusInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCallbackRules(
            self,
            request: models.DescribeLiveCallbackRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCallbackRulesResponse:
        """
        This API is used to get the callback rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCallbackRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCallbackRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCallbackTemplate(
            self,
            request: models.DescribeLiveCallbackTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCallbackTemplateResponse:
        """
        This API is used to get a single callback template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCallbackTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCallbackTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCallbackTemplates(
            self,
            request: models.DescribeLiveCallbackTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCallbackTemplatesResponse:
        """
        This API is used to get the callback template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCallbackTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCallbackTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCert(
            self,
            request: models.DescribeLiveCertRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCertResponse:
        """
        This API is used to get certificate information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCerts(
            self,
            request: models.DescribeLiveCertsRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCertsResponse:
        """
        This API is used to get the certificate information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCerts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCertsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDelayInfoList(
            self,
            request: models.DescribeLiveDelayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDelayInfoListResponse:
        """
        This API is used to get the list of delayed playbacks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDelayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDelayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomain(
            self,
            request: models.DescribeLiveDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainResponse:
        """
        This API is used to query the LVB domain name information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomainCert(
            self,
            request: models.DescribeLiveDomainCertRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainCertResponse:
        """
        This API is used to get the domain name certificate information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomainCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomainCertBindings(
            self,
            request: models.DescribeLiveDomainCertBindingsRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainCertBindingsResponse:
        """
        This API is used to query domains bound with certificates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomainCertBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainCertBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomainReferer(
            self,
            request: models.DescribeLiveDomainRefererRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainRefererResponse:
        """
        This API is used to query referer allowlist/blocklist configuration of a live streaming domain name.
        Referer information is included in HTTP requests. After you enable referer configuration, live streams using RTMP or WebRTC for playback will not authenticate the referer and can be played back normally. To make the referer configuration effective, the HTTP-FLV or HLS protocol is recommended for playback.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomainReferer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainRefererResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomains(
            self,
            request: models.DescribeLiveDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainsResponse:
        """
        This API is used to query domain names by domain name status and type.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveForbidStreamList(
            self,
            request: models.DescribeLiveForbidStreamListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveForbidStreamListResponse:
        """
        This API is used to get the list of disabled streams.

        Note: this API is used for query only and should not be relied too much upon in important business scenarios.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveForbidStreamList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveForbidStreamListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePlayAuthKey(
            self,
            request: models.DescribeLivePlayAuthKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePlayAuthKeyResponse:
        """
        This API is used to query the playback authentication key.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePlayAuthKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePlayAuthKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePullStreamTasks(
            self,
            request: models.DescribeLivePullStreamTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePullStreamTasksResponse:
        """
        This API is used to query the stream pulling tasks created by `CreateLivePullStreamTask`.
        The tasks returned are sorted by last updated time in descending order.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePullStreamTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePullStreamTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePushAuthKey(
            self,
            request: models.DescribeLivePushAuthKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePushAuthKeyResponse:
        """
        This API is used to query the LVB push authentication key.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePushAuthKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePushAuthKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveRecordRules(
            self,
            request: models.DescribeLiveRecordRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveRecordRulesResponse:
        """
        This API is used to get the list of recording rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveRecordRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveRecordRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveRecordTemplate(
            self,
            request: models.DescribeLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveRecordTemplateResponse:
        """
        This API is used to get a single recording template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveRecordTemplates(
            self,
            request: models.DescribeLiveRecordTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveRecordTemplatesResponse:
        """
        This API is used to get the recording template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveRecordTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveRecordTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveSnapshotRules(
            self,
            request: models.DescribeLiveSnapshotRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveSnapshotRulesResponse:
        """
        This API is used to get the screencapturing rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveSnapshotRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveSnapshotRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveSnapshotTemplate(
            self,
            request: models.DescribeLiveSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveSnapshotTemplateResponse:
        """
        This API is used to get a single screencapturing template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveSnapshotTemplates(
            self,
            request: models.DescribeLiveSnapshotTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveSnapshotTemplatesResponse:
        """
        This API is used to get the screencapturing template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveSnapshotTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveSnapshotTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamEventList(
            self,
            request: models.DescribeLiveStreamEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamEventListResponse:
        """
        This API is used to query stream push/interruption events.<br>

        Notes:
        1. This API is used to query stream push/interruption records, and should not be relied too much upon in important business scenarios.
        2. You can use the `IsFilter` parameter of this API to filter and get required push records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamOnlineList(
            self,
            request: models.DescribeLiveStreamOnlineListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamOnlineListResponse:
        """
        This API is used to get the list of ongoing live streams. It queries the information of live streams after they are pushed successfully.

        Notes:
        1. This API is used to query the list of active live streams only, and should not be relied too much upon in important business scenarios.
        2. This API can query up to 20,000 streams. To query more streams, please contact our after-sales service team.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamOnlineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamOnlineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamPublishedList(
            self,
            request: models.DescribeLiveStreamPublishedListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamPublishedListResponse:
        """
        This API is used to return the list of pushed streams. <br>
        Note: Up to 10,000 entries can be queried per page. More data can be obtained by adjusting the query time range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamPublishedList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamPublishedListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamPushInfoList(
            self,
            request: models.DescribeLiveStreamPushInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamPushInfoListResponse:
        """
        This API is used to query the push information of all real-time streams, including client IP, server IP, frame rate, bitrate, domain name, and push start time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamPushInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamPushInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamState(
            self,
            request: models.DescribeLiveStreamStateRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamStateResponse:
        """
        This API is used to get the stream status, which may be active, inactive, or disabled.

        Notes:
        This API allows you to query the status of a stream in real time. Given external factors such as network jitter, note the following when you determine whether a host is online:
        1. If possible, use your own logic of stream starting/stopping in a room, such as streaming signaling on the client and the online heartbeat of a host, to determine whether the host is online.
        2. If your application does not provide the room management feature, use the following methods to determine whether a host is online:
        2.1 Use the [live stream callback](https://intl.cloud.tencent.com/document/product/267/20388?from_cn_redirect=1).
        2.2 Call [DescribeLiveStreamOnlineList](https://intl.cloud.tencent.com/document/api/267/20472?from_cn_redirect=1) on a regular basis (interval > 1 min).
        2.3 Call this API.
        2.4 A host is considered to be online if the result returned by any of the above methods indicates so. If an API call times out or a parsing error occurs, to minimize the impact on your business, CSS will also consider the host online.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTimeShiftBillInfoList(
            self,
            request: models.DescribeLiveTimeShiftBillInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTimeShiftBillInfoListResponse:
        """
        This API is used to query the time-shift video length, time-shift days, and total time-shift period of push domains. The data returned is on a five-minute basis. You can use it for reconciliation.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTimeShiftBillInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTimeShiftBillInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTimeShiftRules(
            self,
            request: models.DescribeLiveTimeShiftRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTimeShiftRulesResponse:
        """
        This API is used to query time shifting rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTimeShiftRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTimeShiftRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTimeShiftTemplates(
            self,
            request: models.DescribeLiveTimeShiftTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTimeShiftTemplatesResponse:
        """
        This API is used to query time shifting templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTimeShiftTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTimeShiftTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTranscodeDetailInfo(
            self,
            request: models.DescribeLiveTranscodeDetailInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTranscodeDetailInfoResponse:
        """
        This API is used to query the transcoding details of a particular day or a specific time period. Querying may fail if the amount of data queried is too large. In such cases, try shortening the time period.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTranscodeDetailInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTranscodeDetailInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTranscodeRules(
            self,
            request: models.DescribeLiveTranscodeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTranscodeRulesResponse:
        """
        This API is used to get the list of transcoding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTranscodeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTranscodeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTranscodeTemplate(
            self,
            request: models.DescribeLiveTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTranscodeTemplateResponse:
        """
        This API is used to get a single transcoding template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTranscodeTemplates(
            self,
            request: models.DescribeLiveTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTranscodeTemplatesResponse:
        """
        This API is used to get the transcoding template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTranscodeTotalInfo(
            self,
            request: models.DescribeLiveTranscodeTotalInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTranscodeTotalInfoResponse:
        """
        This API is used to query transcoding usage. You can use it to query data in the past three months.
        Notes:
        If the start time and end time are on the same day, the data returned will be on a 5-minute basis.
        If the start time and end time are not on the same day or if the data of specified domains is queried, the data returned will be on an hourly basis.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTranscodeTotalInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTranscodeTotalInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveWatermark(
            self,
            request: models.DescribeLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveWatermarkResponse:
        """
        This API is used to get the information of a single watermark.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveWatermarkRules(
            self,
            request: models.DescribeLiveWatermarkRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveWatermarkRulesResponse:
        """
        This API is used to get the watermarking rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveWatermarkRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveWatermarkRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveWatermarks(
            self,
            request: models.DescribeLiveWatermarksRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveWatermarksResponse:
        """
        This API is used to query the watermark list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveWatermarks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveWatermarksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlayErrorCodeDetailInfoList(
            self,
            request: models.DescribePlayErrorCodeDetailInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribePlayErrorCodeDetailInfoListResponse:
        """
        This API is used to query the information of downstream playback error codes, i.e., the occurrences of each HTTP error code (4xx and 5xx) at a 1-minute granularity in a certain period of time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlayErrorCodeDetailInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlayErrorCodeDetailInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlayErrorCodeSumInfoList(
            self,
            request: models.DescribePlayErrorCodeSumInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribePlayErrorCodeSumInfoListResponse:
        """
        This API is used to query the information of downstream playback error codes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlayErrorCodeSumInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlayErrorCodeSumInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProvinceIspPlayInfoList(
            self,
            request: models.DescribeProvinceIspPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeProvinceIspPlayInfoListResponse:
        """
        This API is used to query the downstream playback data of a specified ISP in a specified district, including bandwidth, traffic, number of requests, and number of concurrent connections.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProvinceIspPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProvinceIspPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordTask(
            self,
            request: models.DescribeRecordTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordTaskResponse:
        """
        This API is used to retrieve a list of recording tasks that were started and ended within a specified time range.
        - Prerequisites:
        1. This API is only used to query recording tasks created by the CreateRecordTask interface.
        2. It cannot retrieve recording tasks that have been deleted by the DeleteRecordTask interface or tasks that have expired (platform retains for 3 months).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenShotSheetNumList(
            self,
            request: models.DescribeScreenShotSheetNumListRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenShotSheetNumListResponse:
        """
        The API is used to query the number of screenshots as an LVB value-added service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenShotSheetNumList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenShotSheetNumListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamDayPlayInfoList(
            self,
            request: models.DescribeStreamDayPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamDayPlayInfoListResponse:
        """
        This API is used to query the playback data of each stream at the day level, including the total traffic.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamDayPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamDayPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPlayInfoList(
            self,
            request: models.DescribeStreamPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPlayInfoListResponse:
        """
        This API is used to query the playback data. It supports querying the playback details by stream name and aggregated data by playback domain name. Data in the last 4 minutes or so cannot be queried due to delay.
        Note: to query by `AppName`, you need to submit a ticket first. After your application succeeds, it will take about 5 business days (subject to the time in the reply) for the configuration to take effect.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPushInfoList(
            self,
            request: models.DescribeStreamPushInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPushInfoListResponse:
        """
        This API is used to get the push data of a stream, including the audio/video frame rate, bitrate, elapsed time, and codec.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPushInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPushInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimeShiftRecordDetail(
            self,
            request: models.DescribeTimeShiftRecordDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTimeShiftRecordDetailResponse:
        """
        This API is used to query the time shifting details of a specific time period (up to 24 hours). You need to call `DescribeTimeShiftStreamList` first to get the request parameters of this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimeShiftRecordDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimeShiftRecordDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimeShiftStreamList(
            self,
            request: models.DescribeTimeShiftStreamListRequest,
            opts: Dict = None,
    ) -> models.DescribeTimeShiftStreamListResponse:
        """
        This API is used to query the time shifted streams in a specific time period (up to 24 hours).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimeShiftStreamList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimeShiftStreamListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopClientIpSumInfoList(
            self,
            request: models.DescribeTopClientIpSumInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeTopClientIpSumInfoListResponse:
        """
        This API is used to query the information of the top n client IPs in a certain period of time (top 1,000 is supported currently).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopClientIpSumInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopClientIpSumInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTranscodeTaskNum(
            self,
            request: models.DescribeTranscodeTaskNumRequest,
            opts: Dict = None,
    ) -> models.DescribeTranscodeTaskNumResponse:
        """
        This API is used to query the number of transcoding tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTranscodeTaskNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTranscodeTaskNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUploadStreamNums(
            self,
            request: models.DescribeUploadStreamNumsRequest,
            opts: Dict = None,
    ) -> models.DescribeUploadStreamNumsResponse:
        """
        This API is used to query the number of LVB upstream channels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUploadStreamNums"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUploadStreamNumsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVisitTopSumInfoList(
            self,
            request: models.DescribeVisitTopSumInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeVisitTopSumInfoListResponse:
        """
        This API is used to query the information of the top n domain names or stream IDs in a certain period of time (top 1,000 is supported currently).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVisitTopSumInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVisitTopSumInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DropLiveStream(
            self,
            request: models.DropLiveStreamRequest,
            opts: Dict = None,
    ) -> models.DropLiveStreamResponse:
        """
        This API is used to pause a live stream. The stream can be resumed if it is paused.
        Note: If you call this API to pause an inactive stream, the request will be considered successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DropLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DropLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableLiveDomain(
            self,
            request: models.EnableLiveDomainRequest,
            opts: Dict = None,
    ) -> models.EnableLiveDomainResponse:
        """
        This API is used to enable a disabled LVB domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableLiveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableLiveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForbidLiveDomain(
            self,
            request: models.ForbidLiveDomainRequest,
            opts: Dict = None,
    ) -> models.ForbidLiveDomainResponse:
        """
        This API is used to disable an LVB domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "ForbidLiveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForbidLiveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForbidLiveStream(
            self,
            request: models.ForbidLiveStreamRequest,
            opts: Dict = None,
    ) -> models.ForbidLiveStreamResponse:
        """
        This API is used to disable a stream. You can set a time to resume the stream.
        Note:
        1. As long as the correct stream name is passed in, the stream will be disabled successfully.
        2. If you want a stream to be disabled only if the push domain, push path, and stream name match, please submit a ticket.
        3. If you have configured domain groups, you must pass in the correct push domain in order to disable a stream.
        """
        
        kwargs = {}
        kwargs["action"] = "ForbidLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForbidLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveCallbackTemplate(
            self,
            request: models.ModifyLiveCallbackTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveCallbackTemplateResponse:
        """
        This API is used to modify a callback template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveCallbackTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveCallbackTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveDomainCertBindings(
            self,
            request: models.ModifyLiveDomainCertBindingsRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveDomainCertBindingsResponse:
        """
        This API is used to bind a certificate to multiple playback domains and update the HTTPS configuration of the domains.
        If a self-owned certificate is used, it will be automatically uploaded to Tencent Cloud’s SSL Certificate Service.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveDomainCertBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveDomainCertBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveDomainReferer(
            self,
            request: models.ModifyLiveDomainRefererRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveDomainRefererResponse:
        """
        This API is used to configure referer allowlist/blocklist of a live streaming domain name.
        Referer information is included in HTTP requests. After you enable referer configuration, live streams using RTMP or WebRTC for playback will not authenticate the referer and can be played back normally. To make the referer configuration effective, the HTTP-FLV or HLS protocol is recommended for playback.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveDomainReferer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveDomainRefererResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLivePlayAuthKey(
            self,
            request: models.ModifyLivePlayAuthKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyLivePlayAuthKeyResponse:
        """
        This API is used to modify the playback authentication key.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLivePlayAuthKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLivePlayAuthKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLivePlayDomain(
            self,
            request: models.ModifyLivePlayDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyLivePlayDomainResponse:
        """
        This API is used to modify a playback domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLivePlayDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLivePlayDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLivePullStreamTask(
            self,
            request: models.ModifyLivePullStreamTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyLivePullStreamTaskResponse:
        """
        This API is used to modify a stream pulling task.
        1. You cannot modify the destination URL. To publish to a new destination, please create a new task.
        2. You cannot modify the source type. To use a different source type, please create a new task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLivePullStreamTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLivePullStreamTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLivePushAuthKey(
            self,
            request: models.ModifyLivePushAuthKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyLivePushAuthKeyResponse:
        """
        This API is used to modify the LVB push authentication key.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLivePushAuthKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLivePushAuthKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveRecordTemplate(
            self,
            request: models.ModifyLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveRecordTemplateResponse:
        """
        This API is used to modify the recording template configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveSnapshotTemplate(
            self,
            request: models.ModifyLiveSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveSnapshotTemplateResponse:
        """
        This API is used to modify the screencapturing template configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveTimeShiftTemplate(
            self,
            request: models.ModifyLiveTimeShiftTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveTimeShiftTemplateResponse:
        """
        This API is used to modify a time shifting template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveTimeShiftTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveTimeShiftTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveTranscodeTemplate(
            self,
            request: models.ModifyLiveTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveTranscodeTemplateResponse:
        """
        This API is used to modify the transcoding template configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartLivePullStreamTask(
            self,
            request: models.RestartLivePullStreamTaskRequest,
            opts: Dict = None,
    ) -> models.RestartLivePullStreamTaskResponse:
        """
        Restart the running live streaming pull task.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartLivePullStreamTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartLivePullStreamTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeDelayLiveStream(
            self,
            request: models.ResumeDelayLiveStreamRequest,
            opts: Dict = None,
    ) -> models.ResumeDelayLiveStreamResponse:
        """
        This API is used to cancel the delay setting and recover the real-time display of the live streaming image.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeDelayLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeDelayLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeLiveStream(
            self,
            request: models.ResumeLiveStreamRequest,
            opts: Dict = None,
    ) -> models.ResumeLiveStreamResponse:
        """
        This API is used to resume the push of a specific stream.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartLivePadStream(
            self,
            request: models.StartLivePadStreamRequest,
            opts: Dict = None,
    ) -> models.StartLivePadStreamResponse:
        """
        Call this API to switch the live broadcast to standby footage.
        """
        
        kwargs = {}
        kwargs["action"] = "StartLivePadStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartLivePadStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopLivePadStream(
            self,
            request: models.StopLivePadStreamRequest,
            opts: Dict = None,
    ) -> models.StopLivePadStreamResponse:
        """
        Call this API to end the transition to standby footage.
        """
        
        kwargs = {}
        kwargs["action"] = "StopLivePadStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopLivePadStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopLiveRecord(
            self,
            request: models.StopLiveRecordRequest,
            opts: Dict = None,
    ) -> models.StopLiveRecordResponse:
        """
        Note: Recording files are stored on the VOD platform. To use the recording feature, you need to activate a VOD account and ensure that it is available. After the recording files are stored, applicable fees (including storage fees and downstream playback traffic fees) will be charged according to the VOD billing method. For more information, please see the corresponding document.
        """
        
        kwargs = {}
        kwargs["action"] = "StopLiveRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopLiveRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopRecordTask(
            self,
            request: models.StopRecordTaskRequest,
            opts: Dict = None,
    ) -> models.StopRecordTaskResponse:
        """
        This API is used to terminate an ongoing recording task and generate a recording file.
        """
        
        kwargs = {}
        kwargs["action"] = "StopRecordTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRecordTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindLiveDomainCert(
            self,
            request: models.UnBindLiveDomainCertRequest,
            opts: Dict = None,
    ) -> models.UnBindLiveDomainCertResponse:
        """
        This API is used to unbind a domain name certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindLiveDomainCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindLiveDomainCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateLiveWatermark(
            self,
            request: models.UpdateLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.UpdateLiveWatermarkResponse:
        """
        This API is used to update a watermark.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)