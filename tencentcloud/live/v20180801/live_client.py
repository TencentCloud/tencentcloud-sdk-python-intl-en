# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def AddDelayLiveStream(self, request):
        """This API is used to set the delay time for the stream.
        Note: If you want to set delayed playback before pushing, you need to set 5 minutes in advance.
        Currently, this API only supports stream granularity, and the feature supporting domain name and application granularities will be available in the future.

        :param request: Request instance for AddDelayLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.AddDelayLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddDelayLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddDelayLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddLiveDomain(self, request):
        """This API is used to add a domain name. Only one domain name can be submitted at a time, and it must have an ICP filing.

        :param request: Request instance for AddLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.AddLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddLiveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddLiveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddLiveDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddLiveWatermark(self, request):
        """After a watermark is added and a watermark ID is successfully returned, you need to call the [CreateLiveWatermarkRule](/document/product/267/32629) API and bind the watermark ID to the stream.

        :param request: Request instance for AddLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.AddLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindLiveDomainCert(self, request):
        """This API is used to bind a domain name certificate.
        Note: you need to call the `CreateLiveCert` API first to add a certificate. After getting the certificate ID, call this API for binding.

        :param request: Request instance for BindLiveDomainCert.
        :type request: :class:`tencentcloud.live.v20180801.models.BindLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.BindLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindLiveDomainCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelCommonMixStream(self, request):
        """This API is used to cancel a stream mix. It can be used basically in the same way as `mix_streamv2.cancel_mix_stream`.

        :param request: Request instance for CancelCommonMixStream.
        :type request: :class:`tencentcloud.live.v20180801.models.CancelCommonMixStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CancelCommonMixStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelCommonMixStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelCommonMixStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCommonMixStream(self, request):
        """This API is used to create a general stream mix. It can be used basically in the same way as the legacy `mix_streamv2.cancel_mix_stream` API.
        Note: currently, up to 16 streams can be mixed.

        :param request: Request instance for CreateCommonMixStream.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateCommonMixStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateCommonMixStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCommonMixStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCommonMixStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveCallbackRule(self, request):
        """To create a callback rule, you need to first call the [CreateLiveCallbackTemplate](/document/product/267/32637) API to create a callback template and bind the returned template ID to the domain name/path.
        <br>Callback protocol-related document: [Event Message Notification](/document/product/267/32744).

        :param request: Request instance for CreateLiveCallbackRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveCallbackRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveCallbackRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveCallbackTemplate(self, request):
        """This API is used to create a callback template. After a template ID is successfully returned, you need to call the [CreateLiveCallbackRule](/document/product/267/32638) API to bind the template ID to the domain name/path.
        <br>Callback protocol document: [Event Message Notification](/document/product/267/32744).

        :param request: Request instance for CreateLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveCallbackTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveCert(self, request):
        """This API is used to add a certificate.

        :param request: Request instance for CreateLiveCert.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveRecord(self, request):
        """- Prerequisites
          1. Recording files are stored on the VOD platform, so if you need to use the recording feature, you must first activate the VOD service.
          2. After the recording files are stored, applicable fees (including storage fees and downstream playback traffic fees) will be charged according to the VOD billing mode. For more information, please see the [corresponding document](https://cloud.tencent.com/document/product/266/2838).

        - Mode description
          This API supports two recording modes:
          1. Scheduled recording mode **(default mode)**.
            The start time and end time need to be passed in, and the recording task will automatically start and end based on the time parameters.
          2. Real-time video recording mode.
            The start time passed in will be ignored, and recording will be started immediately after the recording task is created. The recording duration can be up to 30 minutes. If the end time passed in is more than 30 minutes after the current time, it will be counted as 30 minutes. Real-time video recording is mainly used for recording highlight scenes, and you are recommended to keep the duration within 5 minutes.

        - Precautions
          1. The API call timeout period should be set to more than 3 seconds; otherwise, retries and frequent calls may result in repeated recording tasks.
          2. Subject to the audio and video file formats (FLV/MP4/HLS), the video codec of H.264 and audio codec of AAC are supported.
          3. In order to avoid malicious or non-subjective frequent API requests, the maximum number of tasks that can be created in scheduled recording mode is limited: up to 4,000 tasks can be created per day (excluding deleted ones), and up to 400 ones can run concurrently. If you need a higher upper limit, please submit a ticket for application.

        :param request: Request instance for CreateLiveRecord.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveRecordRule(self, request):
        """To create a recording rule, you need to first call the [CreateLiveRecordTemplate](/document/product/267/32614) API to create a recording template and bind the returned template ID to the stream.
        <br>Recording-related document: [LVB Recording](/document/product/267/32739).

        :param request: Request instance for CreateLiveRecordRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveRecordRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveRecordTemplate(self, request):
        """After a recording template is created and a template ID is successfully returned, you need to call the [CreateLiveRecordRule](/document/product/267/32615) API and bind the template ID to the stream.
        <br>Recording-related document: [LVB Recording](/document/product/267/32739).

        :param request: Request instance for CreateLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveSnapshotRule(self, request):
        """This API is used to create a screencapturing rule. You need to first call the [CreateLiveSnapshotTemplate](/document/product/267/32624) API to create a screencapturing template to bind the returned template ID to the stream.
        <br>Screencapturing document: [LVB Screencapturing](/document/product/267/32737).
        Note: only one screencapturing template can be associated with one domain name.

        :param request: Request instance for CreateLiveSnapshotRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveSnapshotRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveSnapshotRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveSnapshotTemplate(self, request):
        """After a screencapturing template is created and a template ID is successfully returned, you need to call the [CreateLiveSnapshotRule](/document/product/267/32625) API and bind the template ID to the stream.
        <br>Screencapturing-related document: [LVB Screencapturing](/document/product/267/32737).

        :param request: Request instance for CreateLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveTranscodeRule(self, request):
        """To create a transcoding rule, you need to first call the [CreateLiveTranscodeTemplate](/document/product/267/32646) API to create a transcoding template and bind the returned template ID to the stream.
        <br>Transcoding-related document: [LVB Remuxing and Transcoding](/document/product/267/32736).

        :param request: Request instance for CreateLiveTranscodeRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveTranscodeRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveTranscodeRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveTranscodeTemplate(self, request):
        """After a transcoding template is created and a template ID is successfully returned, you need to call the [CreateLiveTranscodeRule](/document/product/267/32647) API and bind the returned template ID to the stream.
        <br>Transcoding-related document: [LVB Remuxing and Transcoding](/document/product/267/32736).

        :param request: Request instance for CreateLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveWatermarkRule(self, request):
        """To create a watermarking rule, you need to first call the [AddLiveWatermark](/document/product/267/30154) API to add a watermark and bind the returned watermark ID to the stream.

        :param request: Request instance for CreateLiveWatermarkRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveWatermarkRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveWatermarkRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveWatermarkRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveWatermarkRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveCallbackRule(self, request):
        """This API is used to delete a callback rule.

        :param request: Request instance for DeleteLiveCallbackRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveCallbackRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveCallbackRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveCallbackTemplate(self, request):
        """This API deletes a callback template.

        :param request: Request instance for DeleteLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveCallbackTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveCert(self, request):
        """This API is used to delete a certificate corresponding to the domain name.

        :param request: Request instance for DeleteLiveCert.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveDomain(self, request):
        """This API is used to delete an added LVB domain name.

        :param request: Request instance for DeleteLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveRecord(self, request):
        """Note: The `DeleteLiveRecord` API is only used to delete the record of recording tasks but not stop recording or deleting an ongoing recording task. If you need to stop a recording task, please use the [StopLiveRecord](/document/product/267/30146) API.

        :param request: Request instance for DeleteLiveRecord.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveRecordRule(self, request):
        """This API is used to delete a recording rule.

        :param request: Request instance for DeleteLiveRecordRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveRecordRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveRecordTemplate(self, request):
        """This API is used to delete a recording template.

        :param request: Request instance for DeleteLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveSnapshotRule(self, request):
        """This API is used to delete a screencapturing rule.

        :param request: Request instance for DeleteLiveSnapshotRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveSnapshotRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveSnapshotRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveSnapshotTemplate(self, request):
        """This API is used to delete a screencapturing template.

        :param request: Request instance for DeleteLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveTranscodeRule(self, request):
        """This API is used to delete a transcoding rule.
        `DomainName+AppName+StreamName+TemplateId` uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. `TemplateId` is required. Even if other parameters are empty, you still need to pass in an empty string to make a strong match.

        :param request: Request instance for DeleteLiveTranscodeRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveTranscodeRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveTranscodeRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveTranscodeTemplate(self, request):
        """This API is used to delete a transcoding template.

        :param request: Request instance for DeleteLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveWatermark(self, request):
        """This API is used to delete a watermark.

        :param request: Request instance for DeleteLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveWatermarkRule(self, request):
        """This API is used to delete a watermarking rule.

        :param request: Request instance for DeleteLiveWatermarkRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveWatermarkRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveWatermarkRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBillBandwidthAndFluxList(self, request):
        """This API is used to query the data of billable LVB bandwidth and traffic.

        :param request: Request instance for DescribeBillBandwidthAndFluxList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeBillBandwidthAndFluxListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeBillBandwidthAndFluxListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillBandwidthAndFluxList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillBandwidthAndFluxListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConcurrentRecordStreamNum(self, request):
        """This API is used to query the number of concurrent recording channels, which is applicable to LCB and LVB.

        :param request: Request instance for DescribeConcurrentRecordStreamNum.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeConcurrentRecordStreamNumRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeConcurrentRecordStreamNumResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConcurrentRecordStreamNum", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConcurrentRecordStreamNumResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroupProIspPlayInfoList(self, request):
        """This API is used to query the downstream playback data by district and ISP.

        :param request: Request instance for DescribeGroupProIspPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeGroupProIspPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeGroupProIspPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupProIspPlayInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupProIspPlayInfoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveCallbackRules(self, request):
        """This API is used to get the callback rule list.

        :param request: Request instance for DescribeLiveCallbackRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCallbackRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCallbackRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveCallbackTemplate(self, request):
        """This API is used to get a single callback template.

        :param request: Request instance for DescribeLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCallbackTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveCallbackTemplates(self, request):
        """This API is used to get the callback template list.

        :param request: Request instance for DescribeLiveCallbackTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCallbackTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCallbackTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveCert(self, request):
        """This API is used to get certificate information.

        :param request: Request instance for DescribeLiveCert.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveCerts(self, request):
        """This API is used to get the certificate information list.

        :param request: Request instance for DescribeLiveCerts.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCerts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCertsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveDelayInfoList(self, request):
        """This API is used to get the list of delayed playbacks.

        :param request: Request instance for DescribeLiveDelayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDelayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDelayInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveDelayInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveDelayInfoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveDomain(self, request):
        """This API is used to query the LVB domain name information.

        :param request: Request instance for DescribeLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveDomainCert(self, request):
        """This API is used to get the domain name certificate information.

        :param request: Request instance for DescribeLiveDomainCert.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveDomainCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveDomains(self, request):
        """This API is used to query domain names by domain name status and type.

        :param request: Request instance for DescribeLiveDomains.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveDomainsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveForbidStreamList(self, request):
        """This API is used to get the forbidden stream list.

        :param request: Request instance for DescribeLiveForbidStreamList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveForbidStreamListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveForbidStreamListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveForbidStreamList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveForbidStreamListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLivePlayAuthKey(self, request):
        """This API is used to query the playback authentication key.

        :param request: Request instance for DescribeLivePlayAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePlayAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLivePlayAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLivePlayAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLivePushAuthKey(self, request):
        """This API is used to query the LVB push authentication key.

        :param request: Request instance for DescribeLivePushAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePushAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLivePushAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLivePushAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveRecordRules(self, request):
        """This API is used to get the list of recording rules.

        :param request: Request instance for DescribeLiveRecordRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveRecordRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveRecordTemplate(self, request):
        """This API is used to get a single recording template.

        :param request: Request instance for DescribeLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveRecordTemplates(self, request):
        """This API is used to get the recording template list.

        :param request: Request instance for DescribeLiveRecordTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveRecordTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveSnapshotRules(self, request):
        """This API is used to get the screencapturing rule list.

        :param request: Request instance for DescribeLiveSnapshotRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveSnapshotRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveSnapshotRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveSnapshotTemplate(self, request):
        """This API is used to get a single screencapturing template.

        :param request: Request instance for DescribeLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveSnapshotTemplates(self, request):
        """This API is used to get the screencapturing template list.

        :param request: Request instance for DescribeLiveSnapshotTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveSnapshotTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveSnapshotTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamEventList(self, request):
        """This API is used to query streaming events.<br>

        Note: This API can filter by IsFilter and return the push history.

        :param request: Request instance for DescribeLiveStreamEventList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamEventListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamEventListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamEventList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamEventListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamOnlineList(self, request):
        """This API is used to return the live stream list.

        :param request: Request instance for DescribeLiveStreamOnlineList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamOnlineList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamOnlineListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamPublishedList(self, request):
        """This API is used to return the list of pushed streams. <br>
        Note: Up to 10,000 entries can be queried per page. More data can be obtained by adjusting the query time range.

        :param request: Request instance for DescribeLiveStreamPublishedList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPublishedListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPublishedListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamPublishedList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamPublishedListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamState(self, request):
        """This API is used to return the stream status such as active, inactive, or forbidden.

        :param request: Request instance for DescribeLiveStreamState.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamStateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveTranscodeRules(self, request):
        """This API is used to get the list of transcoding rules.

        :param request: Request instance for DescribeLiveTranscodeRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveTranscodeRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveTranscodeRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveTranscodeTemplate(self, request):
        """This API is used to get a single transcoding template.

        :param request: Request instance for DescribeLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveTranscodeTemplates(self, request):
        """This API is used to get the transcoding template list.

        :param request: Request instance for DescribeLiveTranscodeTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveTranscodeTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveTranscodeTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveWatermark(self, request):
        """This API is used to get the information of a single watermark.

        :param request: Request instance for DescribeLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveWatermarkRules(self, request):
        """This API is used to get the watermarking rule list.

        :param request: Request instance for DescribeLiveWatermarkRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveWatermarkRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveWatermarkRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveWatermarks(self, request):
        """This API is used to query the watermark list.

        :param request: Request instance for DescribeLiveWatermarks.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarksRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveWatermarks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveWatermarksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProIspPlaySumInfoList(self, request):
        """This API is used to query the average traffic per second, total traffic, and number of total requests by country/region, district, and ISP in a certain period of time.

        :param request: Request instance for DescribeProIspPlaySumInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeProIspPlaySumInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeProIspPlaySumInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProIspPlaySumInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProIspPlaySumInfoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamDayPlayInfoList(self, request):
        """This API is used to query the playback data of each stream at the day level, including the total traffic.

        :param request: Request instance for DescribeStreamDayPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeStreamDayPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeStreamDayPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStreamDayPlayInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStreamDayPlayInfoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamPushInfoList(self, request):
        """This API is used to query the upstream push quality data by stream ID, including frame rate, bitrate, elapsed time, and codec of audio and video files.

        :param request: Request instance for DescribeStreamPushInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeStreamPushInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeStreamPushInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStreamPushInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStreamPushInfoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DropLiveStream(self, request):
        """This API is used to disconnect the push connection, which can be resumed.

        :param request: Request instance for DropLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.DropLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DropLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DropLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DropLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableLiveDomain(self, request):
        """This API is used to enable a disabled LVB domain name.

        :param request: Request instance for EnableLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.EnableLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.EnableLiveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableLiveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableLiveDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ForbidLiveDomain(self, request):
        """This API is used to disable an LVB domain name.

        :param request: Request instance for ForbidLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.ForbidLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ForbidLiveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ForbidLiveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForbidLiveDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ForbidLiveStream(self, request):
        """This API is used to forbid the push of a specific stream. You can preset a time point to resume the stream.

        :param request: Request instance for ForbidLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.ForbidLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ForbidLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ForbidLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForbidLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveCallbackTemplate(self, request):
        """This API is used to modify a callback template.

        :param request: Request instance for ModifyLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveCallbackTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveCert(self, request):
        """This API is used to modify a certificate.

        :param request: Request instance for ModifyLiveCert.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveDomainCert(self, request):
        """This API is used to modify the domain name and certificate binding information.

        :param request: Request instance for ModifyLiveDomainCert.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveDomainCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLivePlayAuthKey(self, request):
        """This API is used to modify the playback authentication key.

        :param request: Request instance for ModifyLivePlayAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLivePlayAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLivePlayAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLivePlayDomain(self, request):
        """This API is used to modify a playback domain name.

        :param request: Request instance for ModifyLivePlayDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLivePlayDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLivePlayDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLivePushAuthKey(self, request):
        """This API is used to modify the LVB push authentication key.

        :param request: Request instance for ModifyLivePushAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePushAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLivePushAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLivePushAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveRecordTemplate(self, request):
        """This API is used to modify the recording template configuration.

        :param request: Request instance for ModifyLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveRecordTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveSnapshotTemplate(self, request):
        """This API is used to modify the screencapturing template configuration.

        :param request: Request instance for ModifyLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveTranscodeTemplate(self, request):
        """This API is used to modify the transcoding template configuration.

        :param request: Request instance for ModifyLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeDelayLiveStream(self, request):
        """This API is used to resume a delayed playback.

        :param request: Request instance for ResumeDelayLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.ResumeDelayLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ResumeDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResumeDelayLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeDelayLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeLiveStream(self, request):
        """This API is used to resume the push of a specific stream.

        :param request: Request instance for ResumeLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.ResumeLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ResumeLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResumeLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopLiveRecord(self, request):
        """Note: Recording files are stored on the VOD platform. To use the recording feature, you need to activate a VOD account and ensure that it is available. After the recording files are stored, applicable fees (including storage fees and downstream playback traffic fees) will be charged according to the VOD billing method. For more information, please see the corresponding document.

        :param request: Request instance for StopLiveRecord.
        :type request: :class:`tencentcloud.live.v20180801.models.StopLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopLiveRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindLiveDomainCert(self, request):
        """This API is used to unbind a domain name certificate.

        :param request: Request instance for UnBindLiveDomainCert.
        :type request: :class:`tencentcloud.live.v20180801.models.UnBindLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.UnBindLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindLiveDomainCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateLiveWatermark(self, request):
        """This API is used to update a watermark.

        :param request: Request instance for UpdateLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.UpdateLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.UpdateLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)