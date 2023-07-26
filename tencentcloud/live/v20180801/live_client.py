# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.live.v20180801 import models


class LiveClient(AbstractClient):
    _apiVersion = '2018-08-01'
    _endpoint = 'live.tencentcloudapi.com'
    _service = 'live'


    def AddDelayLiveStream(self, request):
        """This API is used to set a delay in playing the images of large live streaming events, in case of emergencies.

        Note: if you are to set the delay before stream push, set it at least 5 minutes before the push. This API supports configuration only by stream.

        :param request: Request instance for AddDelayLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.AddDelayLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDelayLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.AddDelayLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddLiveDomain(self, request):
        """This API is used to add a domain name. Only one domain name can be submitted at a time, and it must have an ICP filing.

        :param request: Request instance for AddLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.AddLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddLiveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLiveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.AddLiveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddLiveWatermark(self, request):
        """After a watermark is added and a watermark ID is successfully returned, you need to call the [CreateLiveWatermarkRule](https://intl.cloud.tencent.com/document/product/267/32629?from_cn_redirect=1) API to bind the watermark ID to a stream.
        After the number of watermarks exceeds the upper limit of 100, to add a new watermark, you must delete an old one first.

        :param request: Request instance for AddLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.AddLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.AddLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AuthenticateDomainOwner(self, request):
        """This API is used to verify the ownership of a domain.

        :param request: Request instance for AuthenticateDomainOwner.
        :type request: :class:`tencentcloud.live.v20180801.models.AuthenticateDomainOwnerRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AuthenticateDomainOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuthenticateDomainOwner", params, headers=headers)
            response = json.loads(body)
            model = models.AuthenticateDomainOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelCommonMixStream(self, request):
        """This API is used to cancel a stream mix. It can be used basically in the same way as `mix_streamv2.cancel_mix_stream`.

        :param request: Request instance for CancelCommonMixStream.
        :type request: :class:`tencentcloud.live.v20180801.models.CancelCommonMixStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CancelCommonMixStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelCommonMixStream", params, headers=headers)
            response = json.loads(body)
            model = models.CancelCommonMixStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCommonMixStream(self, request):
        """This API is used to create a general stream mix. It can be used basically in the same way as the legacy `mix_streamv2.start_mix_stream_advanced` API.
        Note: currently, up to 16 streams can be mixed.
        Best practice: https://intl.cloud.tencent.com/document/product/267/45566?from_cn_redirect=1

        :param request: Request instance for CreateCommonMixStream.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateCommonMixStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateCommonMixStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCommonMixStream", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCommonMixStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveCallbackRule(self, request):
        """To create a callback rule, you need to first call the [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1) API to create a callback template and bind the returned template ID to the domain name/path.
        <br>Callback protocol-related document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).

        :param request: Request instance for CreateLiveCallbackRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveCallbackRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveCallbackRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveCallbackTemplate(self, request):
        """This API is used to create a callback template. Up to 50 templates can be created. After the template ID is returned, you need to call the [CreateLiveCallbackRule](https://intl.cloud.tencent.com/document/product/267/32638?from_cn_redirect=1) API to bind the template ID to a domain name/path.
        <br>For information about callback protocols, see [How to Receive Event Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).
        Note: You need to specify at least one callback URL.

        :param request: Request instance for CreateLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveCallbackTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveCallbackTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLivePullStreamTask(self, request):
        """This API is used to create a task to pull streams from video files or an external live streaming source and publish them to a specified destination URL.
        Notes:
        1. By default, you can have at most 20 stream pulling tasks at a time. You can submit a ticket to raise the limit.
        2. Only H.264 and H.265 are supported for video. If the source video is in a different format, please transcode it first.
        3. Only AAC is supported for audio. If the source audio is in a different format, please transcode it first.
        4. You can enable auto deletion in the console to delete expired tasks automatically.
        5. The pull and relay feature is a paid feature. For its billing details, see [Relay](https://intl.cloud.tencent.com/document/product/267/53308?from_cn_redirect=1).
        6. CSS is only responsible for pulling and relaying content. Please make sure that your content is authorized and complies with relevant laws and regulations. In case of copyright infringement or violation of laws or regulations, CSS will suspend its service for you and reserves the right to seek legal remedies.

        :param request: Request instance for CreateLivePullStreamTask.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLivePullStreamTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLivePullStreamTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLivePullStreamTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLivePullStreamTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveRecord(self, request):
        """- Prerequisites
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

        :param request: Request instance for CreateLiveRecord.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveRecordRule(self, request):
        """To create a recording rule, you need to first call the [CreateLiveRecordTemplate](https://intl.cloud.tencent.com/document/product/267/32614?from_cn_redirect=1) API to create a recording template and bind the returned template ID to the stream.
        <br>Recording-related document: [LVB Recording](https://intl.cloud.tencent.com/document/product/267/32739?from_cn_redirect=1).

        :param request: Request instance for CreateLiveRecordRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveRecordRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveRecordRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveRecordTemplate(self, request):
        """This API is used to create a recording template. You can create up to 50 templates. To use a template, you need to call the [CreateLiveRecordRule](https://intl.cloud.tencent.com/document/product/267/32615?from_cn_redirect=1) API to bind the template ID returned by this API to a stream.
        <br>More on recording: [Live Recording](https://intl.cloud.tencent.com/document/product/267/32739?from_cn_redirect=1)

        :param request: Request instance for CreateLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveSnapshotRule(self, request):
        """This API is used to create a screencapturing rule. You need to first call the [CreateLiveSnapshotTemplate](https://intl.cloud.tencent.com/document/product/267/32624?from_cn_redirect=1) API to create a screencapturing template to bind the returned template ID to the stream.
        <br>Screencapturing document: [LVB Screencapturing](https://intl.cloud.tencent.com/document/product/267/32737?from_cn_redirect=1).
        Note: only one screencapturing template can be associated with one domain name.

        :param request: Request instance for CreateLiveSnapshotRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveSnapshotRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveSnapshotRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveSnapshotTemplate(self, request):
        """This API is used to create a screencapture template. After a template ID is returned, you need to call the [CreateLiveSnapshotRule](https://intl.cloud.tencent.com/document/product/267/32625?from_cn_redirect=1) API to bind the template ID to a stream. You can create up to 50 screencapture templates.
        <br>To learn more about the live screencapture feature, see [Live Screencapture](https://intl.cloud.tencent.com/document/product/267/32737?from_cn_redirect=1).

        :param request: Request instance for CreateLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveTimeShiftRule(self, request):
        """This API is used to create a time shifting rule. You need to first call the [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/86169?from_cn_redirect=1) API to create a time shifting template, and then call this API to bind the template ID returned to a stream.
        <br>More about time shifting: [Time Shifting](https://intl.cloud.tencent.com/document/product/267/86134?from_cn_redirect=1).

        :param request: Request instance for CreateLiveTimeShiftRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTimeShiftRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTimeShiftRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveTimeShiftRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveTimeShiftRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveTimeShiftTemplate(self, request):
        """This API is used to create a time shifting template.

        :param request: Request instance for CreateLiveTimeShiftTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTimeShiftTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTimeShiftTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveTimeShiftTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveTimeShiftTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveTranscodeRule(self, request):
        """This API is used to create a transcoding rule that binds a template ID to a stream. Up to 50 transcoding rules can be created in total. Before you call this API, you need to first call [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1) to get the template ID.
        <br>Related document: [Live Remuxing and Transcoding](https://intl.cloud.tencent.com/document/product/267/32736?from_cn_redirect=1).

        :param request: Request instance for CreateLiveTranscodeRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveTranscodeRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveTranscodeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveTranscodeTemplate(self, request):
        """This API is used to create a transcoding template. Up to 50 transcoding templates can be created in total. To use a template, you need to call [CreateLiveTranscodeRule](https://intl.cloud.tencent.com/document/product/267/32647?from_cn_redirect=1) to bind the template ID returned by this API to a stream.
        <br>For more information about transcoding, see [Live Remuxing and Transcoding](https://intl.cloud.tencent.com/document/product/267/32736?from_cn_redirect=1).

        :param request: Request instance for CreateLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveWatermarkRule(self, request):
        """To create a watermarking rule, you need to first call the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API to add a watermark and bind the returned watermark ID to the stream.

        :param request: Request instance for CreateLiveWatermarkRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveWatermarkRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveWatermarkRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveWatermarkRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveWatermarkRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecordTask(self, request):
        """This API is used to create a recording task that starts and ends at specific times and records videos according to a specific recording template.
        - Prerequisites
        1. Because recording files are saved in VOD, you must first activate VOD.
        2. Storage and playback traffic fees are charged for storing and playing the videos recorded. For details, see [Purchase Guide](https://intl.cloud.tencent.com/document/product/266/2837).
        - Notes
        1. If streaming is interrupted, the current recording will stop and a recording file will be generated. When streaming resumes, as long as it’s before the end time of the task, recording will start again.
        2. Avoid creating recording tasks with overlapping time periods. If there are multiple tasks with overlapping time periods for the same stream, the system will start three recording tasks at most to avoid repeated recording.
        3. Task records are kept for three months by the platform.
        4. Do not use the new [CreateRecordTask](https://intl.cloud.tencent.com/document/product/267/45983?from_cn_redirect=1), [StopRecordTask](https://intl.cloud.tencent.com/document/product/267/45981?from_cn_redirect=1), and [DeleteRecordTask] APIs together with the old `CreateLiveRecord`, `StopLiveRecord`, and `DeleteLiveRecord` APIs.
        5. Do not create recording tasks and push streams at the same time. After creating a recording task, we recommend you wait at least three seconds before pushing streams.

        :param request: Request instance for CreateRecordTask.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateRecordTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateRecordTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScreenshotTask(self, request):
        """This API is used to create a screencapturing task that has a specific start and end time and takes screenshots according to the template configured.
        - Note
        1. If the stream is interrupted, screencapturing will stop. However, the task will still be valid before the specified end time, and screencapturing will be performed as required after the stream is resumed.
        2. Avoid creating screencapturing tasks with overlapping time periods. The system will execute at most three screencapturing tasks on the same stream at a time.
        3. Task records are only kept for three months.
        4. The new screencapturing APIs (CreateScreenshotTask/StopScreenshotTask/DeleteScreenshotTask) are not compatible with the legacy ones (CreateLiveInstantSnapshot/StopLiveInstantSnapshot). Do not mix them when you call APIs to manage screencapturing tasks.
        5. If you create a screencapturing task and publish the stream at the same time, the task may fail to be executed at the specified time. After creating a screencapturing task, we recommend you wait at least three seconds before publishing the stream.

        :param request: Request instance for CreateScreenshotTask.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateScreenshotTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateScreenshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScreenshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScreenshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveCallbackRule(self, request):
        """This API is used to delete a callback rule.

        :param request: Request instance for DeleteLiveCallbackRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveCallbackRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveCallbackRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveCallbackTemplate(self, request):
        """This API deletes a callback template.

        :param request: Request instance for DeleteLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveCallbackTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveCallbackTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveDomain(self, request):
        """This API is used to delete an added LVB domain name.

        :param request: Request instance for DeleteLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLivePullStreamTask(self, request):
        """This API is used to delete a task created by `CreateLivePullStreamTask`.
        Notes:
        1. For the `TaskId` request parameter, pass in the task ID returned by the `CreateLivePullStreamTask` API.
        2. You can query the ID of a task using the `DescribeLivePullStreamTasks` API.

        :param request: Request instance for DeleteLivePullStreamTask.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLivePullStreamTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLivePullStreamTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLivePullStreamTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLivePullStreamTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveRecord(self, request):
        """Note: The `DeleteLiveRecord` API is only used to delete the record of recording tasks but not stop recording or deleting an ongoing recording task. If you need to stop a recording task, please use the [StopLiveRecord](https://intl.cloud.tencent.com/document/product/267/30146?from_cn_redirect=1) API.

        :param request: Request instance for DeleteLiveRecord.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveRecordRule(self, request):
        """This API is used to delete a recording rule.

        :param request: Request instance for DeleteLiveRecordRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveRecordRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveRecordRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveRecordTemplate(self, request):
        """This API is used to delete a recording template.

        :param request: Request instance for DeleteLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveSnapshotRule(self, request):
        """This API is used to delete a screencapturing rule.

        :param request: Request instance for DeleteLiveSnapshotRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveSnapshotRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveSnapshotRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveSnapshotTemplate(self, request):
        """This API is used to delete a screencapturing template.

        :param request: Request instance for DeleteLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveTimeShiftRule(self, request):
        """This API is used to delete a time shifting rule.

        :param request: Request instance for DeleteLiveTimeShiftRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTimeShiftRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTimeShiftRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveTimeShiftRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveTimeShiftRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveTimeShiftTemplate(self, request):
        """This API is used to delete a time shifting template.

        :param request: Request instance for DeleteLiveTimeShiftTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTimeShiftTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTimeShiftTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveTimeShiftTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveTimeShiftTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveTranscodeRule(self, request):
        """This API is used to delete a transcoding rule.
        `DomainName+AppName+StreamName+TemplateId` uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. `TemplateId` is required. Even if other parameters are empty, you still need to pass in an empty string to make a strong match.

        :param request: Request instance for DeleteLiveTranscodeRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveTranscodeRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveTranscodeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveTranscodeTemplate(self, request):
        """This API is used to delete a transcoding template.

        :param request: Request instance for DeleteLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveWatermark(self, request):
        """This API is used to delete a watermark.

        :param request: Request instance for DeleteLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveWatermarkRule(self, request):
        """This API is used to delete a watermarking rule.

        :param request: Request instance for DeleteLiveWatermarkRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveWatermarkRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveWatermarkRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordTask(self, request):
        """This API is used to delete a recording task configuration. The deletion does not affect running tasks and takes effect only for new pushes.

        :param request: Request instance for DeleteRecordTask.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteRecordTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteRecordTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllStreamPlayInfoList(self, request):
        """This API is used to get the playback data of all streams at a specified time point (accurate to the minute).

        :param request: Request instance for DescribeAllStreamPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeAllStreamPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeAllStreamPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllStreamPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllStreamPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillBandwidthAndFluxList(self, request):
        """This API is used to query the data of billable LVB bandwidth and traffic.

        :param request: Request instance for DescribeBillBandwidthAndFluxList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeBillBandwidthAndFluxListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeBillBandwidthAndFluxListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillBandwidthAndFluxList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillBandwidthAndFluxListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConcurrentRecordStreamNum(self, request):
        """This API is used to query the number of concurrent recording channels, which is applicable to LCB and LVB.

        :param request: Request instance for DescribeConcurrentRecordStreamNum.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeConcurrentRecordStreamNumRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeConcurrentRecordStreamNumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConcurrentRecordStreamNum", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConcurrentRecordStreamNumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeliverBandwidthList(self, request):
        """This API is used to query the billable bandwidth of live stream relaying in the last 3 months. The query period is up to 31 days.

        :param request: Request instance for DescribeDeliverBandwidthList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeDeliverBandwidthListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeDeliverBandwidthListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeliverBandwidthList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeliverBandwidthListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupProIspPlayInfoList(self, request):
        """This API is used to query the downstream playback data by district and ISP.

        :param request: Request instance for DescribeGroupProIspPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeGroupProIspPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeGroupProIspPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupProIspPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupProIspPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHttpStatusInfoList(self, request):
        """This API is used to query the number of each playback HTTP status code at a 5-minute granularity in a certain period of time.
        Note: data can be queried one hour after it is generated. For example, data between 10:00 and 10:59 cannot be queried until 12:00.

        :param request: Request instance for DescribeHttpStatusInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeHttpStatusInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeHttpStatusInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHttpStatusInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHttpStatusInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCallbackRules(self, request):
        """This API is used to get the callback rule list.

        :param request: Request instance for DescribeLiveCallbackRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCallbackRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCallbackRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCallbackTemplate(self, request):
        """This API is used to get a single callback template.

        :param request: Request instance for DescribeLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCallbackTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCallbackTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCallbackTemplates(self, request):
        """This API is used to get the callback template list.

        :param request: Request instance for DescribeLiveCallbackTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCallbackTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCallbackTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCert(self, request):
        """This API is used to get certificate information.

        :param request: Request instance for DescribeLiveCert.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCert", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCerts(self, request):
        """This API is used to get the certificate information list.

        :param request: Request instance for DescribeLiveCerts.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCerts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCertsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDelayInfoList(self, request):
        """This API is used to get the list of delayed playbacks.

        :param request: Request instance for DescribeLiveDelayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDelayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDelayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDelayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDelayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomain(self, request):
        """This API is used to query the LVB domain name information.

        :param request: Request instance for DescribeLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomainCert(self, request):
        """This API is used to get the domain name certificate information.

        :param request: Request instance for DescribeLiveDomainCert.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomainCert", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomainCertBindings(self, request):
        """This API is used to query domains bound with certificates.

        :param request: Request instance for DescribeLiveDomainCertBindings.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertBindingsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomainCertBindings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainCertBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomainReferer(self, request):
        """This API is used to query referer allowlist/blocklist configuration of a live streaming domain name.
        Referer information is included in HTTP requests. After you enable referer configuration, live streams using RTMP or WebRTC for playback will not authenticate the referer and can be played back normally. To make the referer configuration effective, the HTTP-FLV or HLS protocol is recommended for playback.

        :param request: Request instance for DescribeLiveDomainReferer.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainRefererRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainRefererResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomainReferer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainRefererResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomains(self, request):
        """This API is used to query domain names by domain name status and type.

        :param request: Request instance for DescribeLiveDomains.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveForbidStreamList(self, request):
        """This API is used to get the list of disabled streams.

        Note: this API is used for query only and should not be relied too much upon in important business scenarios.

        :param request: Request instance for DescribeLiveForbidStreamList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveForbidStreamListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveForbidStreamListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveForbidStreamList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveForbidStreamListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePlayAuthKey(self, request):
        """This API is used to query the playback authentication key.

        :param request: Request instance for DescribeLivePlayAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePlayAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePlayAuthKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePlayAuthKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePullStreamTasks(self, request):
        """This API is used to query the stream pulling tasks created by `CreateLivePullStreamTask`.
        The tasks returned are sorted by last updated time in descending order.

        :param request: Request instance for DescribeLivePullStreamTasks.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePullStreamTasksRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePullStreamTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePullStreamTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePullStreamTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePushAuthKey(self, request):
        """This API is used to query the LVB push authentication key.

        :param request: Request instance for DescribeLivePushAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePushAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePushAuthKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePushAuthKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveRecordRules(self, request):
        """This API is used to get the list of recording rules.

        :param request: Request instance for DescribeLiveRecordRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveRecordRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveRecordRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveRecordTemplate(self, request):
        """This API is used to get a single recording template.

        :param request: Request instance for DescribeLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveRecordTemplates(self, request):
        """This API is used to get the recording template list.

        :param request: Request instance for DescribeLiveRecordTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveRecordTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveRecordTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveSnapshotRules(self, request):
        """This API is used to get the screencapturing rule list.

        :param request: Request instance for DescribeLiveSnapshotRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveSnapshotRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveSnapshotRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveSnapshotTemplate(self, request):
        """This API is used to get a single screencapturing template.

        :param request: Request instance for DescribeLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveSnapshotTemplates(self, request):
        """This API is used to get the screencapturing template list.

        :param request: Request instance for DescribeLiveSnapshotTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveSnapshotTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveSnapshotTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamEventList(self, request):
        """This API is used to query stream push/interruption events.<br>

        Notes:
        1. This API is used to query stream push/interruption records, and should not be relied too much upon in important business scenarios.
        2. You can use the `IsFilter` parameter of this API to filter and get required push records.

        :param request: Request instance for DescribeLiveStreamEventList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamEventListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamOnlineList(self, request):
        """This API is used to get the list of ongoing live streams. It queries the information of live streams after they are pushed successfully.

        Notes:
        1. This API is used to query the list of active live streams only, and should not be relied too much upon in important business scenarios.
        2. This API can query up to 20,000 streams. To query more streams, please contact our after-sales service team.

        :param request: Request instance for DescribeLiveStreamOnlineList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamOnlineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamOnlineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamPublishedList(self, request):
        """This API is used to return the list of pushed streams. <br>
        Note: Up to 10,000 entries can be queried per page. More data can be obtained by adjusting the query time range.

        :param request: Request instance for DescribeLiveStreamPublishedList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPublishedListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPublishedListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamPublishedList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamPublishedListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamPushInfoList(self, request):
        """This API is used to query the push information of all real-time streams, including client IP, server IP, frame rate, bitrate, domain name, and push start time.

        :param request: Request instance for DescribeLiveStreamPushInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPushInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPushInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamPushInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamPushInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamState(self, request):
        """This API is used to get the stream status, which may be active, inactive, or disabled.

        Notes:
        This API allows you to query the status of a stream in real time. Given external factors such as network jitter, note the following when you determine whether a host is online:
        1. If possible, use your own logic of stream starting/stopping in a room, such as streaming signaling on the client and the online heartbeat of a host, to determine whether the host is online.
        2. If your application does not provide the room management feature, use the following methods to determine whether a host is online:
        2.1 Use the [live stream callback](https://intl.cloud.tencent.com/document/product/267/20388?from_cn_redirect=1).
        2.2 Call [DescribeLiveStreamOnlineList](https://intl.cloud.tencent.com/document/api/267/20472?from_cn_redirect=1) on a regular basis (interval > 1 min).
        2.3 Call this API.
        2.4 A host is considered to be online if the result returned by any of the above methods indicates so. If an API call times out or a parsing error occurs, to minimize the impact on your business, CSS will also consider the host online.

        :param request: Request instance for DescribeLiveStreamState.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamStateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTimeShiftBillInfoList(self, request):
        """This API is used to query the time-shift video length, time-shift days, and total time-shift period of push domains. The data returned is on a five-minute basis. You can use it for reconciliation.

        :param request: Request instance for DescribeLiveTimeShiftBillInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftBillInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftBillInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTimeShiftBillInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTimeShiftBillInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTimeShiftRules(self, request):
        """This API is used to query time shifting rules.

        :param request: Request instance for DescribeLiveTimeShiftRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTimeShiftRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTimeShiftRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTimeShiftTemplates(self, request):
        """This API is used to query time shifting templates.

        :param request: Request instance for DescribeLiveTimeShiftTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTimeShiftTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTimeShiftTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTranscodeDetailInfo(self, request):
        """This API is used to query the transcoding details of a particular day or a specific time period. Querying may fail if the amount of data queried is too large. In such cases, try shortening the time period.

        :param request: Request instance for DescribeLiveTranscodeDetailInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeDetailInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTranscodeDetailInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTranscodeDetailInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTranscodeRules(self, request):
        """This API is used to get the list of transcoding rules.

        :param request: Request instance for DescribeLiveTranscodeRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTranscodeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTranscodeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTranscodeTemplate(self, request):
        """This API is used to get a single transcoding template.

        :param request: Request instance for DescribeLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTranscodeTemplates(self, request):
        """This API is used to get the transcoding template list.

        :param request: Request instance for DescribeLiveTranscodeTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTranscodeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTranscodeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTranscodeTotalInfo(self, request):
        """This API is used to query transcoding usage. You can use it to query data in the past three months.
        Notes:
        If the start time and end time are on the same day, the data returned will be on a 5-minute basis.
        If the start time and end time are not on the same day or if the data of specified domains is queried, the data returned will be on an hourly basis.

        :param request: Request instance for DescribeLiveTranscodeTotalInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTotalInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTotalInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTranscodeTotalInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTranscodeTotalInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveWatermark(self, request):
        """This API is used to get the information of a single watermark.

        :param request: Request instance for DescribeLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveWatermarkRules(self, request):
        """This API is used to get the watermarking rule list.

        :param request: Request instance for DescribeLiveWatermarkRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveWatermarkRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveWatermarkRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveWatermarks(self, request):
        """This API is used to query the watermark list.

        :param request: Request instance for DescribeLiveWatermarks.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarksRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveWatermarks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveWatermarksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlayErrorCodeDetailInfoList(self, request):
        """This API is used to query the information of downstream playback error codes, i.e., the occurrences of each HTTP error code (4xx and 5xx) at a 1-minute granularity in a certain period of time.


        :param request: Request instance for DescribePlayErrorCodeDetailInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribePlayErrorCodeDetailInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribePlayErrorCodeDetailInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlayErrorCodeDetailInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlayErrorCodeDetailInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlayErrorCodeSumInfoList(self, request):
        """This API is used to query the information of downstream playback error codes.

        :param request: Request instance for DescribePlayErrorCodeSumInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribePlayErrorCodeSumInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribePlayErrorCodeSumInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlayErrorCodeSumInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlayErrorCodeSumInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProvinceIspPlayInfoList(self, request):
        """This API is used to query the downstream playback data of a specified ISP in a specified district, including bandwidth, traffic, number of requests, and number of concurrent connections.

        :param request: Request instance for DescribeProvinceIspPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeProvinceIspPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeProvinceIspPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProvinceIspPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProvinceIspPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordTask(self, request):
        """This API is used to retrieve a list of recording tasks that were started and ended within a specified time range.
        - Prerequisites:
        1. This API is only used to query recording tasks created by the CreateRecordTask interface.
        2. It cannot retrieve recording tasks that have been deleted by the DeleteRecordTask interface or tasks that have expired (platform retains for 3 months).

        :param request: Request instance for DescribeRecordTask.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeRecordTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeRecordTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenShotSheetNumList(self, request):
        """The API is used to query the number of screenshots as an LVB value-added service.

        :param request: Request instance for DescribeScreenShotSheetNumList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeScreenShotSheetNumListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeScreenShotSheetNumListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenShotSheetNumList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenShotSheetNumListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamDayPlayInfoList(self, request):
        """This API is used to query the playback data of each stream at the day level, including the total traffic.

        :param request: Request instance for DescribeStreamDayPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeStreamDayPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeStreamDayPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamDayPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamDayPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPlayInfoList(self, request):
        """This API is used to query the playback data. It supports querying the playback details by stream name and aggregated data by playback domain name. Data in the last 4 minutes or so cannot be queried due to delay.
        Note: to query by `AppName`, you need to submit a ticket first. After your application succeeds, it will take about 5 business days (subject to the time in the reply) for the configuration to take effect.

        :param request: Request instance for DescribeStreamPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeStreamPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeStreamPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPushInfoList(self, request):
        """This API is used to get the push data of a stream, including the audio/video frame rate, bitrate, elapsed time, and codec.

        :param request: Request instance for DescribeStreamPushInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeStreamPushInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeStreamPushInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPushInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPushInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimeShiftRecordDetail(self, request):
        """This API is used to query the time shifting details of a specific time period (up to 24 hours). You need to call `DescribeTimeShiftStreamList` first to get the request parameters of this API.

        :param request: Request instance for DescribeTimeShiftRecordDetail.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeTimeShiftRecordDetailRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeTimeShiftRecordDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimeShiftRecordDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimeShiftRecordDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimeShiftStreamList(self, request):
        """This API is used to query the time shifted streams in a specific time period (up to 24 hours).

        :param request: Request instance for DescribeTimeShiftStreamList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeTimeShiftStreamListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeTimeShiftStreamListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimeShiftStreamList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimeShiftStreamListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopClientIpSumInfoList(self, request):
        """This API is used to query the information of the top n client IPs in a certain period of time (top 1,000 is supported currently).

        :param request: Request instance for DescribeTopClientIpSumInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeTopClientIpSumInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeTopClientIpSumInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopClientIpSumInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopClientIpSumInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTranscodeTaskNum(self, request):
        """This API is used to query the number of transcoding tasks.

        :param request: Request instance for DescribeTranscodeTaskNum.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeTranscodeTaskNumRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeTranscodeTaskNumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeTaskNum", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeTaskNumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUploadStreamNums(self, request):
        """This API is used to query the number of LVB upstream channels.

        :param request: Request instance for DescribeUploadStreamNums.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeUploadStreamNumsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeUploadStreamNumsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUploadStreamNums", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUploadStreamNumsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVisitTopSumInfoList(self, request):
        """This API is used to query the information of the top n domain names or stream IDs in a certain period of time (top 1,000 is supported currently).

        :param request: Request instance for DescribeVisitTopSumInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeVisitTopSumInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeVisitTopSumInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVisitTopSumInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVisitTopSumInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DropLiveStream(self, request):
        """This API is used to pause a live stream. The stream can be resumed if it is paused.
        Note: If you call this API to pause an inactive stream, the request will be considered successful.

        :param request: Request instance for DropLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.DropLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DropLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DropLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.DropLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableLiveDomain(self, request):
        """This API is used to enable a disabled LVB domain name.

        :param request: Request instance for EnableLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.EnableLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.EnableLiveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableLiveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.EnableLiveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForbidLiveDomain(self, request):
        """This API is used to disable an LVB domain name.

        :param request: Request instance for ForbidLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.ForbidLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ForbidLiveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForbidLiveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ForbidLiveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForbidLiveStream(self, request):
        """This API is used to disable a stream. You can set a time to resume the stream.
        Note:
        1. As long as the correct stream name is passed in, the stream will be disabled successfully.
        2. If you want a stream to be disabled only if the push domain, push path, and stream name match, please submit a ticket.
        3. If you have configured domain groups, you must pass in the correct push domain in order to disable a stream.

        :param request: Request instance for ForbidLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.ForbidLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ForbidLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForbidLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.ForbidLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveCallbackTemplate(self, request):
        """This API is used to modify a callback template.

        :param request: Request instance for ModifyLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveCallbackTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveCallbackTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveDomainCertBindings(self, request):
        """This API is used to bind a certificate to multiple playback domains and update the HTTPS configuration of the domains.
        If a self-owned certificate is used, it will be automatically uploaded to Tencent Cloud’s SSL Certificate Service.

        :param request: Request instance for ModifyLiveDomainCertBindings.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainCertBindingsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainCertBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveDomainCertBindings", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveDomainCertBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveDomainReferer(self, request):
        """This API is used to configure referer allowlist/blocklist of a live streaming domain name.
        Referer information is included in HTTP requests. After you enable referer configuration, live streams using RTMP or WebRTC for playback will not authenticate the referer and can be played back normally. To make the referer configuration effective, the HTTP-FLV or HLS protocol is recommended for playback.

        :param request: Request instance for ModifyLiveDomainReferer.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainRefererRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainRefererResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveDomainReferer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveDomainRefererResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLivePlayAuthKey(self, request):
        """This API is used to modify the playback authentication key.

        :param request: Request instance for ModifyLivePlayAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLivePlayAuthKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLivePlayAuthKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLivePlayDomain(self, request):
        """This API is used to modify a playback domain name.

        :param request: Request instance for ModifyLivePlayDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLivePlayDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLivePlayDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLivePullStreamTask(self, request):
        """This API is used to modify a stream pulling task.
        1. You cannot modify the destination URL. To publish to a new destination, please create a new task.
        2. You cannot modify the source type. To use a different source type, please create a new task.

        :param request: Request instance for ModifyLivePullStreamTask.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePullStreamTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePullStreamTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLivePullStreamTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLivePullStreamTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLivePushAuthKey(self, request):
        """This API is used to modify the LVB push authentication key.

        :param request: Request instance for ModifyLivePushAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePushAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLivePushAuthKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLivePushAuthKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveRecordTemplate(self, request):
        """This API is used to modify the recording template configuration.

        :param request: Request instance for ModifyLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveSnapshotTemplate(self, request):
        """This API is used to modify the screencapturing template configuration.

        :param request: Request instance for ModifyLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveTimeShiftTemplate(self, request):
        """This API is used to modify a time shifting template.

        :param request: Request instance for ModifyLiveTimeShiftTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveTimeShiftTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveTimeShiftTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveTimeShiftTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveTimeShiftTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveTranscodeTemplate(self, request):
        """This API is used to modify the transcoding template configuration.

        :param request: Request instance for ModifyLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeDelayLiveStream(self, request):
        """This API is used to cancel the delay setting and recover the real-time display of the live streaming image.

        :param request: Request instance for ResumeDelayLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.ResumeDelayLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ResumeDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeDelayLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeDelayLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeLiveStream(self, request):
        """This API is used to resume the push of a specific stream.

        :param request: Request instance for ResumeLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.ResumeLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ResumeLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopLiveRecord(self, request):
        """Note: Recording files are stored on the VOD platform. To use the recording feature, you need to activate a VOD account and ensure that it is available. After the recording files are stored, applicable fees (including storage fees and downstream playback traffic fees) will be charged according to the VOD billing method. For more information, please see the corresponding document.

        :param request: Request instance for StopLiveRecord.
        :type request: :class:`tencentcloud.live.v20180801.models.StopLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopLiveRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopLiveRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StopLiveRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopRecordTask(self, request):
        """This API is used to terminate an ongoing recording task and generate a recording file.

        :param request: Request instance for StopRecordTask.
        :type request: :class:`tencentcloud.live.v20180801.models.StopRecordTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopRecordTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopRecordTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopRecordTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnBindLiveDomainCert(self, request):
        """This API is used to unbind a domain name certificate.

        :param request: Request instance for UnBindLiveDomainCert.
        :type request: :class:`tencentcloud.live.v20180801.models.UnBindLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.UnBindLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindLiveDomainCert", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindLiveDomainCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateLiveWatermark(self, request):
        """This API is used to update a watermark.

        :param request: Request instance for UpdateLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.UpdateLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.UpdateLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))