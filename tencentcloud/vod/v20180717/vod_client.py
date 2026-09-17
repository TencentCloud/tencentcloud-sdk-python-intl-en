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
from tencentcloud.vod.v20180717 import models


class VodClient(AbstractClient):
    _apiVersion = '2018-07-17'
    _endpoint = 'vod.intl.tencentcloudapi.com'
    _service = 'vod'


    def ApplyUpload(self, request):
        r"""We strongly recommend that you use the [server-side upload SDK](https://www.tencentcloud.comhttps://www.tencentcloud.com/document/product/266/9759?from_cn_redirect=1?from_cn_redirect=1#1.-.E5.8F.91.E8.B5.B7.E4.B8.8A.E4.BC.A0) provided by VOD to upload files. Directly invoking the API for upload is significantly more difficult and requires a larger workload than using the SDK.
        * This API is used to apply for upload of media files (and cover files), obtain meta information for file upload to VOD (including upload path, upload signature), for subsequent upload API.
        For the upload process, see [Server-Side Upload Overview](https://www.tencentcloud.com/document/product/266/9759?from_cn_redirect=1).

        :param request: Request instance for ApplyUpload.
        :type request: :class:`tencentcloud.vod.v20180717.models.ApplyUploadRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ApplyUploadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyUpload", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyUploadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachMediaSubtitles(self, request):
        r"""Associate media asset subtitles with the media output file corresponding to the adaptive bitrate streaming template ID (or disassociate them).

        :param request: Request instance for AttachMediaSubtitles.
        :type request: :class:`tencentcloud.vod.v20180717.models.AttachMediaSubtitlesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.AttachMediaSubtitlesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachMediaSubtitles", params, headers=headers)
            response = json.loads(body)
            model = models.AttachMediaSubtitlesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneCDNDomain(self, request):
        r"""Clone CDN Domain.

        :param request: Request instance for CloneCDNDomain.
        :type request: :class:`tencentcloud.vod.v20180717.models.CloneCDNDomainRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CloneCDNDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneCDNDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CloneCDNDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneVoiceAsync(self, request):
        r"""This API is used to initiate a voice cloning task. It generates an exclusive voice based on reference audio. The generated voice can be used for subsequent text to speech. Voice cloning is an asynchronous task. The voice ID and audio audition are generated after task completion.

        :param request: Request instance for CloneVoiceAsync.
        :type request: :class:`tencentcloud.vod.v20180717.models.CloneVoiceAsyncRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CloneVoiceAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneVoiceAsync", params, headers=headers)
            response = json.loads(body)
            model = models.CloneVoiceAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneVoiceSync(self, request):
        r"""This API is used to initiate a voice cloning task to clone an exclusive voice based on reference audio. The generated voice can be used for subsequent text to speech.

        :param request: Request instance for CloneVoiceSync.
        :type request: :class:`tencentcloud.vod.v20180717.models.CloneVoiceSyncRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CloneVoiceSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneVoiceSync", params, headers=headers)
            response = json.loads(body)
            model = models.CloneVoiceSyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitUpload(self, request):
        r"""This API is used to confirm the result of uploading media files and cover files to Tencent Cloud VOD, store media information, and return the playback addresses and file IDs.

        :param request: Request instance for CommitUpload.
        :type request: :class:`tencentcloud.vod.v20180717.models.CommitUploadRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CommitUploadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitUpload", params, headers=headers)
            response = json.loads(body)
            model = models.CommitUploadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ComposeMedia(self, request):
        r"""This API is used to compose media files to achieve the following effects:

        1. **Image rotation**: Rotate the image of a video or picture by a certain degree, or flip it in a certain direction.
        2. **Audio control**: Increase or reduce the volume of video and audio, or mute the video.
        3. **Screen overlay**: Overlay frames from videos and images in sequence, for example, to achieve a Picture-in-Picture effect.
        4. **Audio mixing**: Mix the sound in video and audio together.
        5. **Audio extraction**: Extract the audio from the video (the visual is not retained).
        6. **Crop**: Crop a specified time period from a video or audio.
        7. **Splicing**: Splice videos, audio, and images in chronological order.
        8. **Transitions**: When stitching multiple videos or images, you can add transition effects between paragraphs.

        The muxing format of the synthesized media can be MP4 (video) or MP3 (audio). If event notification is used, its type is [Video synthesis completed](https://www.tencentcloud.com/document/product/266/43000?from_cn_redirect=1).

        :param request: Request instance for ComposeMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.ComposeMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ComposeMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ComposeMedia", params, headers=headers)
            response = json.loads(body)
            model = models.ComposeMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfirmEvents(self, request):
        r"""* Developers call the event notification pull API. After obtaining an event, they must call this API to acknowledge that the message has been received.
        * After the developer obtains the event handler, the validity time for pending confirmation is 30 seconds. If it exceeds 30 seconds, a parameter error (4000) is reported.
        * For more references on reliable callback for event notification, see [Reliable Callback](https://www.tencentcloud.com/document/product/266/33779?from_cn_redirect=1#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83).

        :param request: Request instance for ConfirmEvents.
        :type request: :class:`tencentcloud.vod.v20180717.models.ConfirmEventsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ConfirmEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIAnalysisTemplate(self, request):
        r"""This API is used to create a user-defined audio and video content analysis template. Maximum quantity: 50. HLS format is not supported currently.

        :param request: Request instance for CreateAIAnalysisTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIAnalysisTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIAnalysisTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIRecognitionTemplate(self, request):
        r"""This API is used to create a user-defined audio and video content recognition template. Maximum quantity: 50.

        :param request: Request instance for CreateAIRecognitionTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIRecognitionTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIRecognitionTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAdaptiveDynamicStreamingTemplate(self, request):
        r"""Create adaptive bitrate streaming templates. Maximum quantity: 100.

        :param request: Request instance for CreateAdaptiveDynamicStreamingTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAdaptiveDynamicStreamingTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAdaptiveDynamicStreamingTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcAdvancedCustomElement(self, request):
        r"""This API is used to create advanced custom AIGC subjects.

        :param request: Request instance for CreateAigcAdvancedCustomElement.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcAdvancedCustomElementRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcAdvancedCustomElementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcAdvancedCustomElement", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcAdvancedCustomElementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcApiToken(self, request):
        r"""This API is used to create a Token for AIGC API calls. Data sync may delay after creation. It can be queried or deleted after about 30 seconds.

        :param request: Request instance for CreateAigcApiToken.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcApiTokenRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcApiTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcApiToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcApiTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcAudioClone(self, request):
        r"""This API is used to create AIGC voice replication. Note that calling this API incurs fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).

        :param request: Request instance for CreateAigcAudioClone.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcAudioCloneRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcAudioCloneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcAudioClone", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcAudioCloneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcAudioTask(self, request):
        r"""This API is used to create AI audio generation tasks.

        :param request: Request instance for CreateAigcAudioTask.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcAudioTaskRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcAudioTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcAudioTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcAudioTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcCustomElement(self, request):
        r"""Call this API to create a subject for a specified model.

        :param request: Request instance for CreateAigcCustomElement.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcCustomElementRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcCustomElementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcCustomElement", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcCustomElementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcCustomVoice(self, request):
        r"""This API is used to create AIGC custom voice types. Note that calling this API incurs custom voice type creation fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#5e5217e8-29fc-467e-ac2d-853648f988b7).

        :param request: Request instance for CreateAigcCustomVoice.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcCustomVoiceRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcCustomVoiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcCustomVoice", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcCustomVoiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcHunyuan3DTask(self, request):
        r"""This API is used to generate AIGC Hunyuan 3D Files.

        :param request: Request instance for CreateAigcHunyuan3DTask.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcHunyuan3DTaskRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcHunyuan3DTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcHunyuan3DTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcHunyuan3DTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcImageTask(self, request):
        r"""This API is used to generate AIGC images. The default limit is 1 concurrent processing. API calls incur actual fees. Refer to the VOD AIGC image generation billing documentation. The settlement mode for this feature is pay-as-you-go. For daily billing customers, usage on the day is billed on the second day. For monthly billing customers, the previous month's usage fees are billed on the 1st of the next month.

        :param request: Request instance for CreateAigcImageTask.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcImageTaskRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcImageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcImageTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcImageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcQuota(self, request):
        r"""This API is used to create and enable AIGC quota configuration. Quota usage starts accumulating when the quota feature is enabled. Once the quota is reached, AIGC features will no longer be usable.

        If the quota is deleted and re-enabled, the amount will be cleared and recalculated.

        Since AGC content generation is an async task, real-time usage data cannot be obtained. Therefore, quota limits result in some errors, and full precise control over the set limit cannot be achieved.

        :param request: Request instance for CreateAigcQuota.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcQuotaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcQuota", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcSubject(self, request):
        r"""This API is used to create AIGC custom subjects (Vidu). Note that calling this API incurs fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).

        :param request: Request instance for CreateAigcSubject.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcSubjectRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcSubjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcSubject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcSubjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcVideoRedrawTask(self, request):
        r"""This API is used to generate AIGC videos. API calls incur actual fees. Refer to the VOD AIGC video generation billing documentation. The settlement mode for this feature is pay-as-you-go. For daily billing customers, usage on the day is billed on the second day. For monthly billing customers, usage fees for the previous month are billed on the 1st of the next month.

        :param request: Request instance for CreateAigcVideoRedrawTask.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcVideoRedrawTaskRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcVideoRedrawTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcVideoRedrawTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcVideoRedrawTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAigcVideoTask(self, request):
        r"""This API is used to generate AIGC videos. The default limit is 1 concurrent processing. API calls incur actual fees. Refer to the VOD AIGC video generation billing documentation. The feature uses postpaid settlement mode. Daily billing customers are billed on the second day after usage. Monthly settlement customers are billed on the 1st of the next month for the previous month's usage fees.

        :param request: Request instance for CreateAigcVideoTask.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAigcVideoTaskRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAigcVideoTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAigcVideoTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAigcVideoTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAnimatedGraphicsTemplate(self, request):
        r"""This API is used to create custom animated image generating templates. Maximum quantity: 16.

        :param request: Request instance for CreateAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAnimatedGraphicsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAnimatedGraphicsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBlindWatermarkTemplate(self, request):
        r"""This API is used to create a user-defined digital watermark template.

        :param request: Request instance for CreateBlindWatermarkTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateBlindWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateBlindWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBlindWatermarkTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBlindWatermarkTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCDNDomain(self, request):
        r"""This API is used for adding domain names to VOD. A user can add up to 20 domain names. 1. After the domain name is added successfully, VOD will carry out the deployment of the domain name. It takes approximately 2 minutes for the domain name to change from the deployment status to the online status.

        :param request: Request instance for CreateCDNDomain.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateCDNDomainRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateCDNDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCDNDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCDNDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCLSLogset(self, request):
        r"""Create a logset via VOD.

        :param request: Request instance for CreateCLSLogset.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateCLSLogsetRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateCLSLogsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCLSLogset", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCLSLogsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCLSTopic(self, request):
        r"""This API is used to create a CLS log topic for VOD.

        :param request: Request instance for CreateCLSTopic.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateCLSTopicRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateCLSTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCLSTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCLSTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClass(self, request):
        r"""* Used to categorize and manage media;
        * This API does not affect the existing media categories. To modify media categories, call the [ModifyMediaInfo](https://www.tencentcloud.com/document/product/266/31762?from_cn_redirect=1) API.
        * The classification hierarchy cannot exceed 4 levels.
        The number of subcategories in each category cannot exceed 500.

        :param request: Request instance for CreateClass.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateClassRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClass", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateComplexAdaptiveDynamicStreamingTask(self, request):
        r"""Initiates a complex adaptive bitstream processing task. Features include:
        1. Output HLS and DASH adaptive bitrate streams based on the designated adaptive bitrate template;
        2. Content protection solutions for adaptive bitrate streams can be unencrypted, Widevine, or FairPlay.
        3. Support adding opening and ending segments;
        4. The output adaptive bitrate stream can contain multilingual audio streams, each language comes from a different media file;
        5. The output adaptive bitrate stream can include multilingual subtitle streams.

        Notes:
        1. When using an opening scene, the video stream in the opening scene media needs to align with the audio stream; otherwise, the output content will have audio and video synchronization issues.
        2. If the output adaptive bitrate stream needs to include the audio of the main media, the FileId of the main media needs to be specified in the AudioSet parameter.
        3. To use subtitles, add them to the main media first via the ModifyMediaInfo API or the audio and video details page in the console;
        4. Top speed Codec and watermark are not currently supported.

        :param request: Request instance for CreateComplexAdaptiveDynamicStreamingTask.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateComplexAdaptiveDynamicStreamingTaskRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateComplexAdaptiveDynamicStreamingTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateComplexAdaptiveDynamicStreamingTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateComplexAdaptiveDynamicStreamingTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateContentReviewTemplate(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of the moderation template supports video moderation and image moderation. For details, please see [Create Moderation Template](https://www.tencentcloud.com/document/api/266/84391?from_cn_redirect=1).
        This API is used to create a user-customized audio/video moderation template. Up to 50 templates can be created.

        :param request: Request instance for CreateContentReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateContentReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateContentReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainVerifyRecord(self, request):
        r"""This API is used to generate a subdomain name resolution and prompt customers to add it to the domain name resolution for wildcard domain name and domain name retrieval ownership verification.

        :param request: Request instance for CreateDomainVerifyRecord.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateDomainVerifyRecordRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateDomainVerifyRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainVerifyRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainVerifyRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEnhanceMediaTemplate(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of the [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        This API is used to create an audio and video quality rebirth template.

        :param request: Request instance for CreateEnhanceMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateEnhanceMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateEnhanceMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnhanceMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnhanceMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHeadTailTemplate(self, request):
        r"""This API is used to create a title and trailer template.
        -Maximum supported template quantity: 100.

        :param request: Request instance for CreateHeadTailTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateHeadTailTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateHeadTailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHeadTailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHeadTailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageProcessingTemplate(self, request):
        r"""Create a custom image processing template. Maximum quantity: 16. Supports up to ten operations, for example: crop-thumbnail-crop-blur-thumbnail-crop-thumbnail-crop-blur-thumbnail.

        :param request: Request instance for CreateImageProcessingTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateImageProcessingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateImageProcessingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageProcessingTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageProcessingTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageSpriteTemplate(self, request):
        r"""This API is used to create a user-customized image sprite template. Maximum number: 16.

        :param request: Request instance for CreateImageSpriteTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageSpriteTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageSpriteTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateJustInTimeTranscodeTemplate(self, request):
        r"""This API is used to create a just in time transcoding template.

        :param request: Request instance for CreateJustInTimeTranscodeTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateJustInTimeTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateJustInTimeTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJustInTimeTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJustInTimeTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKnowledgeBase(self, request):
        r"""Create a knowledge base. This API is used to create a new knowledge base for Intelligent Media Assets. Each user can create up to 20 knowledge bases.

        :param request: Request instance for CreateKnowledgeBase.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateKnowledgeBaseRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateKnowledgeBaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKnowledgeBase", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKnowledgeBaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLLMComprehendTemplate(self, request):
        r"""This API is used to create a large model parsing template.

        :param request: Request instance for CreateLLMComprehendTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateLLMComprehendTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateLLMComprehendTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLLMComprehendTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLLMComprehendTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMPSTemplate(self, request):
        r"""This API is used to create a custom template for partial features of the ProcessMediaByMPS API.
        When creating a template, fill in the MPS related parameters in JSON format in the MPSCreateTemplateParams parameter. For specific task parameter configuration methods, refer to the MPS task template documentation.
        Currently supported MPS features for creating custom templates:
        1. [Audio and video enhancement](https://www.tencentcloud.com/document/product/862/118703?from_cn_redirect=1).
        2. [Media AI](https://www.tencentcloud.com/document/product/862/113756?from_cn_redirect=1)

        > Template for tasks created this way:
        > 1. Template management is still done in the VOD platform.
        > 2. The feature is currently in beta test. If needed, you can contact us for support to get testing experience.

        :param request: Request instance for CreateMPSTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateMPSTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateMPSTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMPSTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMPSTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePersonSample(self, request):
        r"""This API is used to create material samples for video processing such as content recognition and inappropriate video recognition through technologies like facial feature positioning.

        :param request: Request instance for CreatePersonSample.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreatePersonSampleRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreatePersonSampleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePersonSample", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePersonSampleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProcedureTemplate(self, request):
        r"""This API is used to create user-defined task flow templates. Template capacity limit: 50.

        :param request: Request instance for CreateProcedureTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateProcedureTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProcedureTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProcedureTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProcessImageAsyncTemplate(self, request):
        r"""Create a user-customized async image processing template. Maximum number: 50. HLS format is not supported currently.

        :param request: Request instance for CreateProcessImageAsyncTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateProcessImageAsyncTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateProcessImageAsyncTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProcessImageAsyncTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProcessImageAsyncTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQualityInspectTemplate(self, request):
        r"""Creates an audio-visual quality inspection template.

        :param request: Request instance for CreateQualityInspectTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateQualityInspectTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateQualityInspectTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQualityInspectTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQualityInspectTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRebuildMediaTemplate(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of the [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        This API is used to create a video rebirth template.

        :param request: Request instance for CreateRebuildMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateRebuildMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateRebuildMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRebuildMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRebuildMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReviewTemplate(self, request):
        r"""This API is used to create a user-customized moderation template. Up to 50 templates can be created.
        >Template is applicable only to the ReviewAudioVideo (https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) and ReviewImage (https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1) APIs.

        :param request: Request instance for CreateReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoundPlay(self, request):
        r"""This API is used to create a carousel playlist. Maximum quantity: 100.
        Each file in a carousel playlist can specify a source file or a transcoded file.
        The specified file must be in hls format. All playlist files should have the same bitrate and resolution.

        :param request: Request instance for CreateRoundPlay.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateRoundPlayRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateRoundPlayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoundPlay", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoundPlayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSampleSnapshotTemplate(self, request):
        r"""This API is used to create custom sampled screenshot templates. Maximum quantity: 16.

        :param request: Request instance for CreateSampleSnapshotTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateSampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateSampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSampleSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSampleSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSceneAigcImageTask(self, request):
        r"""This API is used to generate scenario-based AIGC images. API calls incur actual fees. Refer to the VOD AIGC image generation billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#9c4dc6ff-4b3f-4b25-bf2d-393889dfb9ac). The feature uses pay-as-you-go settlement mode (https://www.tencentcloud.com/document/product/266/2838?from_cn_redirect=1). For daily billing customers, usage on the day is billed on the second day. For monthly settlement customers, the previous month's usage fees are billed on the 1st of the next month.

        :param request: Request instance for CreateSceneAigcImageTask.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateSceneAigcImageTaskRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateSceneAigcImageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSceneAigcImageTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSceneAigcImageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSceneAigcVideoTask(self, request):
        r"""This API is used to generate scenario-based AIGC images. <b>The API is in beta. To use it, please [contact us](https://www.tencentcloud.com/online?from_cn_redirect=1-service?from=sales_sales&source=PRESALE). API calls will incur actual fees.</b>

        :param request: Request instance for CreateSceneAigcVideoTask.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateSceneAigcVideoTaskRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateSceneAigcVideoTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSceneAigcVideoTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSceneAigcVideoTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSnapshotByTimeOffsetTemplate(self, request):
        r"""This API is used to create a user-customized specified time point screenshot template. Maximum quantity: 16.

        :param request: Request instance for CreateSnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateSnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshotByTimeOffsetTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotByTimeOffsetTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStorageRegion(self, request):
        r"""This API is used to enable storage in a region.
        1. When a user enables the VOD service, storage in partial regions is enabled by default. If the user needs storage in other regions, they can use this API to enable it.
        2. The DescribeStorageRegions API can be used to query all storage regions and regions that are already opened.

        :param request: Request instance for CreateStorageRegion.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateStorageRegionRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateStorageRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStorageRegion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStorageRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubAppId(self, request):
        r"""This API is used to create a VOD application.

        :param request: Request instance for CreateSubAppId.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateSubAppIdRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateSubAppIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubAppId", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubAppIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSuperPlayerConfig(self, request):
        r"""This API is <font color='red'>no longer maintained</font>. The new version of player signature no longer uses player configuration templates. For details, please see [Player Signature](https://www.tencentcloud.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to create player configurations. Maximum quantity: 100.

        :param request: Request instance for CreateSuperPlayerConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateSuperPlayerConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateSuperPlayerConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSuperPlayerConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSuperPlayerConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTranscodeTemplate(self, request):
        r"""Create custom transcoding templates. Maximum quantity: 100.

        :param request: Request instance for CreateTranscodeTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVodDomain(self, request):
        r"""This API is used to add acceleration domain names to VOD. A user can add up to 20 acceleration domain names.
        1. After the domain name is successfully added, VOD will deploy the domain name. It takes about 2 minutes for the domain name to change from deployment status to online status.

        :param request: Request instance for CreateVodDomain.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateVodDomainRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateVodDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVodDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVodDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWatermarkTemplate(self, request):
        r"""This API is used to create a user-defined watermark template with an upper limit of 1000.

        :param request: Request instance for CreateWatermarkTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWatermarkTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWatermarkTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWordSamples(self, request):
        r"""This API is used to create keyword samples in batches. Samples are used for video processing such as inappropriate content recognition and content recognition through OCR and ASR technologies.

        :param request: Request instance for CreateWordSamples.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateWordSamplesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateWordSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWordSamples", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWordSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAIAnalysisTemplate(self, request):
        r"""This API is used to delete a user-defined audio and video content analysis template.

        Note: Templates with IDs below 10000 are system-preset templates and cannot be deleted.

        :param request: Request instance for DeleteAIAnalysisTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIAnalysisTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIAnalysisTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAIRecognitionTemplate(self, request):
        r"""This API is used to delete a user-defined audio and video content recognition template.

        :param request: Request instance for DeleteAIRecognitionTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIRecognitionTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIRecognitionTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAdaptiveDynamicStreamingTemplate(self, request):
        r"""Delete an adaptive bitrate streaming template

        :param request: Request instance for DeleteAdaptiveDynamicStreamingTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAdaptiveDynamicStreamingTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAdaptiveDynamicStreamingTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAigcAdvancedCustomElement(self, request):
        r"""This API is used to delete AIGC advanced custom subjects.

        :param request: Request instance for DeleteAigcAdvancedCustomElement.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAigcAdvancedCustomElementRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAigcAdvancedCustomElementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAigcAdvancedCustomElement", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAigcAdvancedCustomElementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAigcApiToken(self, request):
        r"""Delete an AIGC API Token. The AIGC quota associated with the Token will also be deleted.

        :param request: Request instance for DeleteAigcApiToken.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAigcApiTokenRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAigcApiTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAigcApiToken", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAigcApiTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAigcQuota(self, request):
        r"""This API is used to delete AIGC quota configurations. Once deleted, AIGC task initiation will no longer be limited.

        If the quota is deleted and re-enabled, the amount will be cleared and recalculated.

        :param request: Request instance for DeleteAigcQuota.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAigcQuotaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAigcQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAigcQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAigcQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAnimatedGraphicsTemplate(self, request):
        r"""This API is used to delete a custom animated image generating template.

        :param request: Request instance for DeleteAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAnimatedGraphicsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAnimatedGraphicsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBlindWatermarkTemplate(self, request):
        r"""This API is used to delete a user-defined digital watermark template.

        :param request: Request instance for DeleteBlindWatermarkTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteBlindWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteBlindWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBlindWatermarkTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBlindWatermarkTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCDNDomain(self, request):
        r"""Delete CDN Domain

        :param request: Request instance for DeleteCDNDomain.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteCDNDomainRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteCDNDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCDNDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCDNDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCLSTopic(self, request):
        r"""Delete the log topic enabled for VOD.

        :param request: Request instance for DeleteCLSTopic.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteCLSTopicRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteCLSTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCLSTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCLSTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClass(self, request):
        r"""* A category can be deleted only when it has no subcategories and no associated media.
        * Otherwise, execute [delete media](https://www.tencentcloud.com/document/product/266/31764?from_cn_redirect=1) and subcategories first, then delete the category;

        :param request: Request instance for DeleteClass.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteClassRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClass", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteContentReviewTemplate(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of the moderation template supports video moderation and image moderation. For details, please see [Deleting a Moderation Template](https://www.tencentcloud.com/document/api/266/84390?from_cn_redirect=1).
        Delete a user-customized audio/video moderation template.

        :param request: Request instance for DeleteContentReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteContentReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteContentReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEnhanceMediaTemplate(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) interface uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        This API is used to delete an audio and video quality rebirth template.

        :param request: Request instance for DeleteEnhanceMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteEnhanceMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteEnhanceMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEnhanceMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEnhanceMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHeadTailTemplate(self, request):
        r"""Delete a title and trailer template.

        :param request: Request instance for DeleteHeadTailTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteHeadTailTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteHeadTailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHeadTailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHeadTailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageProcessingTemplate(self, request):
        r"""This API is used to delete a user-customized image processing template.

        :param request: Request instance for DeleteImageProcessingTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteImageProcessingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteImageProcessingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageProcessingTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageProcessingTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageSpriteTemplate(self, request):
        r"""Delete an image sprite template.

        :param request: Request instance for DeleteImageSpriteTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageSpriteTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageSpriteTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteJustInTimeTranscodeTemplate(self, request):
        r"""Delete a just in time transcoding template.

        :param request: Request instance for DeleteJustInTimeTranscodeTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteJustInTimeTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteJustInTimeTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteJustInTimeTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteJustInTimeTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteKnowledgeBase(self, request):
        r"""Delete a knowledge base.
        After the API is called, the knowledge base is in the "Deleting" status, and the deletion operation is performed in the backend.

        :param request: Request instance for DeleteKnowledgeBase.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteKnowledgeBaseRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteKnowledgeBaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteKnowledgeBase", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteKnowledgeBaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLLMComprehendTemplate(self, request):
        r"""Delete a user-customized large model parsing template.

        Note: Templates with IDs below 10000 are system-preset templates and cannot be deleted.

        :param request: Request instance for DeleteLLMComprehendTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteLLMComprehendTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteLLMComprehendTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLLMComprehendTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLLMComprehendTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMPSTemplate(self, request):
        r"""This API is used to delete a user-defined MPS task template.

        :param request: Request instance for DeleteMPSTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteMPSTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteMPSTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMPSTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMPSTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMedia(self, request):
        r"""* Delete media and its corresponding video processing files (raw files, such as transcoded videos, sprite sheets, screenshots, WeChat video releases, etc.);
        * You can separately delete the original file, transcoded video, and WeChat-published video under a specified video file ID.
        * Note: After the original file is deleted, you cannot initiate any video processing operations such as transcoding or WeChat publishing.

        :param request: Request instance for DeleteMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMedia", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePersonSample(self, request):
        r"""This API is used to delete material samples based on person ID.

        :param request: Request instance for DeletePersonSample.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeletePersonSampleRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeletePersonSampleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePersonSample", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePersonSampleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProcedureTemplate(self, request):
        r"""This API is used to delete a user-defined task flow template.

        :param request: Request instance for DeleteProcedureTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteProcedureTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProcedureTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProcedureTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProcessImageAsyncTemplate(self, request):
        r"""This API is used to delete a user-customized image asynchronous processing template.

        Note: Templates with IDs below 10000 are system-preset templates and cannot be deleted.

        :param request: Request instance for DeleteProcessImageAsyncTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteProcessImageAsyncTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteProcessImageAsyncTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProcessImageAsyncTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProcessImageAsyncTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQualityInspectTemplate(self, request):
        r"""This API is used to delete an audio-visual quality inspection template.

        :param request: Request instance for DeleteQualityInspectTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteQualityInspectTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteQualityInspectTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQualityInspectTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQualityInspectTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRebuildMediaTemplate(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of the [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        This API is used to delete a video rebirth template.

        :param request: Request instance for DeleteRebuildMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteRebuildMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteRebuildMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRebuildMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRebuildMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReviewTemplate(self, request):
        r"""This API is used to delete a user-customized moderation template.
        >Template is applicable only to the ReviewAudioVideo (https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) and ReviewImage (https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1) APIs.

        :param request: Request instance for DeleteReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoundPlay(self, request):
        r"""This API is used to delete a carousel playlist.

        :param request: Request instance for DeleteRoundPlay.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteRoundPlayRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteRoundPlayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoundPlay", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoundPlayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSampleSnapshotTemplate(self, request):
        r"""This API is used to delete a user-customized sampled screenshot template.

        :param request: Request instance for DeleteSampleSnapshotTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteSampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteSampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSampleSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSampleSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshotByTimeOffsetTemplate(self, request):
        r"""This API is used to delete a user-defined specified time point screenshot template.

        :param request: Request instance for DeleteSnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteSnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshotByTimeOffsetTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotByTimeOffsetTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSuperPlayerConfig(self, request):
        r"""This API is <font color='red'>no longer maintained</font>. The new version of player signature no longer uses player configuration templates. For details, please see [Player Signature](https://www.tencentcloud.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to delete player configurations.
        *Note: System preset player configurations cannot be deleted.*

        :param request: Request instance for DeleteSuperPlayerConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteSuperPlayerConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteSuperPlayerConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSuperPlayerConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSuperPlayerConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTranscodeTemplate(self, request):
        r"""This API is used to delete a custom transcoding template.

        :param request: Request instance for DeleteTranscodeTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVodDomain(self, request):
        r"""This API is used to delete VOD acceleration domains.
        1. Before domain deletion, acceleration in all regions needs to be disabled.

        :param request: Request instance for DeleteVodDomain.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteVodDomainRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteVodDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVodDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVodDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVoice(self, request):
        r"""This API is used to delete a specified voice by voice ID. Deletion is irreversible and the voice cannot be used for subsequent APIs. It only supports deletion of voices for this account. System preset voices cannot be deleted.

        Note: Newly designed or cloned voice types cannot be deleted before activation (not found means non-operational). They are activated only after the newly created voice type is used for TTS once.

        :param request: Request instance for DeleteVoice.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteVoiceRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteVoiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVoice", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVoiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWatermarkTemplate(self, request):
        r"""This API is used to delete a user-customized watermark template.

        :param request: Request instance for DeleteWatermarkTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWatermarkTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWatermarkTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWordSamples(self, request):
        r"""This API is used to delete keyword samples in batches.

        :param request: Request instance for DeleteWordSamples.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteWordSamplesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteWordSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWordSamples", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWordSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisTemplates(self, request):
        r"""This API is used to retrieve the detail list of audio and video content analysis templates based on the unique identifier of an audio and video content analysis template. The returned results include all eligible user-defined audio and video content analysis templates and [system preset audio/video content analysis templates](https://www.tencentcloud.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.88.86.E6.9E.90.E6.A8.A1.E6.9D.BF).

        :param request: Request instance for DescribeAIAnalysisTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAIAnalysisTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAIAnalysisTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIRecognitionTemplates(self, request):
        r"""This API is used to get the list of details of audio/video content recognition templates by unique identifier. The returned results include all eligible user-defined audio/video content recognition templates and system preset audio/video content recognition templates (https://www.tencentcloud.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E8.AF.86.E5.88.AB.E6.A8.A1.E6.9D.BF).

        :param request: Request instance for DescribeAIRecognitionTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAIRecognitionTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAIRecognitionTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIRecognitionTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIRecognitionTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAdaptiveDynamicStreamingTemplates(self, request):
        r"""This API is used to query adaptive bitrate streaming templates, and the pagination query is supported based on conditions.

        :param request: Request instance for DescribeAdaptiveDynamicStreamingTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAdaptiveDynamicStreamingTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAdaptiveDynamicStreamingTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAdaptiveDynamicStreamingTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAdaptiveDynamicStreamingTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAigcAdvancedCustomElements(self, request):
        r"""This API is used to obtain advanced custom AIGC subjects.

        :param request: Request instance for DescribeAigcAdvancedCustomElements.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAigcAdvancedCustomElementsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAigcAdvancedCustomElementsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAigcAdvancedCustomElements", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAigcAdvancedCustomElementsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAigcApiTokens(self, request):
        r"""Query the list of AIGC API tokens. Data sync may delay after creation or deletion. You can query the latest data after about 30 seconds.

        :param request: Request instance for DescribeAigcApiTokens.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAigcApiTokensRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAigcApiTokensResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAigcApiTokens", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAigcApiTokensResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAigcFaceInfo(self, request):
        r"""This API is used to retrieve AIGC face information. Note that calling this API will incur face recognition fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).

        :param request: Request instance for DescribeAigcFaceInfo.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAigcFaceInfoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAigcFaceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAigcFaceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAigcFaceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAigcFaceInfoAsync(self, request):
        r"""This API is used to asynchronously fetch AIGC face information. Note that calling this API will incur face recognition fees. Refer to the [billing documentation](https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).

        :param request: Request instance for DescribeAigcFaceInfoAsync.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAigcFaceInfoAsyncRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAigcFaceInfoAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAigcFaceInfoAsync", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAigcFaceInfoAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAigcQuotas(self, request):
        r"""This API is used to query AIGC quota configurations.

        :param request: Request instance for DescribeAigcQuotas.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAigcQuotasRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAigcQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAigcQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAigcQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAigcUsageData(self, request):
        r"""This API is used to return AIGC statistical information within a specified time range.
        1. AIGC statistical data from the last 365 days can be queried.
           2. The query time span should not exceed 90 days.
        3. If the query time span exceeds 1 day, the data of day granularity is returned. Otherwise, the data of 5-minute granularity is returned.

        :param request: Request instance for DescribeAigcUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAigcUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAigcUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAigcUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAigcUsageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllClass(self, request):
        r"""* Obtain all classification information of the user.

        :param request: Request instance for DescribeAllClass.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAllClassRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAllClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllClass", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAnimatedGraphicsTemplates(self, request):
        r"""Queries the list of rotating image templates based on conditions with paging.

        :param request: Request instance for DescribeAnimatedGraphicsTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAnimatedGraphicsTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAnimatedGraphicsTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAnimatedGraphicsTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAnimatedGraphicsTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlindWatermarkTemplates(self, request):
        r"""Queries user-customized digital watermark templates.

        :param request: Request instance for DescribeBlindWatermarkTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeBlindWatermarkTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeBlindWatermarkTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlindWatermarkTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlindWatermarkTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCDNDomains(self, request):
        r"""Describe CDN Domains

        :param request: Request instance for DescribeCDNDomains.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCDNDomainsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCDNDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCDNDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCDNDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCDNStatDetails(self, request):
        r"""This API is used to query CDN bandwidth, traffic, and other stats of an on-demand domain name.
        * The time span between the query start time and end time should not exceed 90 days.
        * Data in different service regions can be queried.
        * Data support within the Chinese mainland for querying stats by specified region and carrier.
        Playback statistics only target VOD domains. Distribution through EdgeOne domain names is not included in playback statistics.

        :param request: Request instance for DescribeCDNStatDetails.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCDNStatDetailsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCDNStatDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCDNStatDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCDNStatDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCDNUsageData(self, request):
        r"""This API is used to query VOD CDN stats such as traffic and bandwidth.
        1. CDN usage data is retained on the system side for 13 months. You can only query usage data from the most recent 365 days through the API. If you need to retrieve historical usage data beyond 365 days, contact us.
           2. The query time span should not exceed 90 days.
        3. You can specify the time granularity of usage data. Supported granularities: 5 minutes, 1 hour, and 1 day.
        4. Traffic is the total traffic within the query time granularity, and bandwidth is the peak bandwidth within the query time granularity.
        5. Playback statistics only target VOD domains. Distribution through EdgeOne domain names is not included in playback statistics.

        :param request: Request instance for DescribeCDNUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCDNUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCDNUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCDNUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCDNUsageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCLSLogsets(self, request):
        r"""Queries CLS log sets created by VOD.

        :param request: Request instance for DescribeCLSLogsets.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCLSLogsetsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCLSLogsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCLSLogsets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCLSLogsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCLSPushTargets(self, request):
        r"""Queries the destination topic for log delivery under an on-demand domain name.

        :param request: Request instance for DescribeCLSPushTargets.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCLSPushTargetsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCLSPushTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCLSPushTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCLSPushTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCLSTopics(self, request):
        r"""Queries the list of CLS log topics created by VOD.

        :param request: Request instance for DescribeCLSTopics.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCLSTopicsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCLSTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCLSTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCLSTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdnLogs(self, request):
        r"""This API is used to query the download URL of CDN access logs for a VOD domain, excluding logs where EdgeOne pulls from the VOD domain.
        1. Can query CDN log download links from the most recent 30 days.
        2. By default, CDN generates a log file per hour. If there is no CDN access in an hour, no log file is generated.
        3. The CDN log download link has a validity of 24 hours.

        :param request: Request instance for DescribeCdnLogs.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCdnLogsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCdnLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdnLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdnLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientUploadAccelerationUsageData(self, request):
        r"""This API returns client upload acceleration statistics within a specified time range.
        1. Can query client upload acceleration statistics data for the most recent 365 days.
           2. The query time span should not exceed 90 days.
        3. If the query time span exceeds 1 day, the data is returned at a granularity of 1 day. Otherwise, the data is returned at a granularity of 5 minutes.

        :param request: Request instance for DescribeClientUploadAccelerationUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeClientUploadAccelerationUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeClientUploadAccelerationUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientUploadAccelerationUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientUploadAccelerationUsageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContentReviewTemplates(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of moderation template supports video moderation and image moderation. For details, please see [Get Moderation Template List](https://www.tencentcloud.com/document/api/266/84389?from_cn_redirect=1).
        This API is used to retrieve the list of audio/video moderation template details based on the unique identifier of an audio/video moderation template. The returned results include all eligible custom templates and system preset content review templates (https://www.tencentcloud.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.AE.A1.E6.A0.B8.E6.A8.A1.E6.9D.BF).

        :param request: Request instance for DescribeContentReviewTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeContentReviewTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeContentReviewTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentReviewTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContentReviewTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCurrentPlaylist(self, request):
        r"""Query the carousel current playlist.

        :param request: Request instance for DescribeCurrentPlaylist.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCurrentPlaylistRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCurrentPlaylistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCurrentPlaylist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCurrentPlaylistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDailyMediaPlayStat(self, request):
        r"""This API is used to query the daily playback statistics within the specified date range.
        * Playback statistics from the past one year can be queried.
        * The time span between the start date and end date can be up to 90 days.
        Playback statistics only target VOD domains. Distribution of EdgeOne domain names is not included in playback statistics.
        * Due to data delay, you are advised to query the usage data of the previous day after 12:00 noon the next day.

        :param request: Request instance for DescribeDailyMediaPlayStat.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDailyMediaPlayStatRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDailyMediaPlayStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDailyMediaPlayStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDailyMediaPlayStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDailyMostPlayedStat(self, request):
        r"""This API is used to query playback statistics of the Top 100 daily played media files.
        * Playback statistics from the past one year can be queried.
        * You can query by number of plays or playback traffic.
        * Playback count statistics description:
        1. HLS file: The number of plays is counted when an M3U8 file is accessed, but not when a TS file is accessed.
        2. Other files (for example, MP4 files): If a playback request includes the range parameter and the start parameter of range is not equal to 0, the number of plays is not counted. In other cases, the number of plays is counted.
        * Playback statistics only target VOD domains. Distribution through EdgeOne domain names is not included in playback statistics.

        :param request: Request instance for DescribeDailyMostPlayedStat.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDailyMostPlayedStatRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDailyMostPlayedStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDailyMostPlayedStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDailyMostPlayedStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDailyPlayStatFileList(self, request):
        r"""This API is used to query the download address of playback statistics files.
        * You can query the download link for playback statistics files from the past one year. The time span between the start date and end date cannot exceed 90 days.
        VOD analyzes and processes the CDN request logs of the previous day to generate playback statistics files.
        * The playback statistics file contains statistical information such as the number of plays and total traffic of media files.
        * Statistical description of the number of plays:
        1. HLS file: The number of plays is counted when accessing M3U8 files, but not when accessing TS files.
        2. Other files (for example, MP4 files): If the playback request includes the range parameter and the start parameter of range is not equal to 0, the number of plays is not counted. In other cases, the number of plays is counted.
        * Statistics of playback devices: If a playback request includes the UserAgent parameter and the UserAgent contains identifiers such as Android or iPhone, it is counted as a mobile playback count. Otherwise, it is counted as a PC playback count.
        Playback statistics only target VOD domain names. Distribution of EdgeOne domain names is not included in playback statistics.

        :param request: Request instance for DescribeDailyPlayStatFileList.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDailyPlayStatFileListRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDailyPlayStatFileListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDailyPlayStatFileList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDailyPlayStatFileListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultDistributionConfig(self, request):
        r"""This API is used to query the default distribution configuration.
        * Distribution domain name and distribution protocol, i.e., the domain name and protocol in the media file distribution URL. Media files are distributed based on the default distribution configuration.
        Playback key, used to calculate player signature.

        :param request: Request instance for DescribeDefaultDistributionConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDefaultDistributionConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDefaultDistributionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultDistributionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultDistributionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDrmKeyProviderInfo(self, request):
        r"""This API is used to query DRM key provider information.

        :param request: Request instance for DescribeDrmKeyProviderInfo.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDrmKeyProviderInfoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDrmKeyProviderInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDrmKeyProviderInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDrmKeyProviderInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnhanceMediaTemplates(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of the [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        This API is used to retrieve the audio and video quality regeneration template list.

        :param request: Request instance for DescribeEnhanceMediaTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeEnhanceMediaTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeEnhanceMediaTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnhanceMediaTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnhanceMediaTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventConfig(self, request):
        r"""Tencent Cloud Video on Demand (VOD) provides customers with media upload, media management, media processing, and other services. During or after the execution of these services, VOD also provides various event notifications, helping developers detect service processing status and perform next business operations.

        Developers can use this API to query the current configuration of event notification receiving methods, recipient addresses, and which events have callback notifications enabled.

        Default API request rate limit: 100 requests/second.

        :param request: Request instance for DescribeEventConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeEventConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeEventConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileAttributes(self, request):
        r"""Used to asynchronously fetch file attributes.
        -Currently only support getting the Md5 and Sha1 of the source file.
        -For HLS or DASH input files, only get the attributes of the index file.

        :param request: Request instance for DescribeFileAttributes.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeFileAttributesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeFileAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHeadTailTemplates(self, request):
        r"""This API is used to get the list of title and trailer templates.

        :param request: Request instance for DescribeHeadTailTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeHeadTailTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeHeadTailTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHeadTailTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHeadTailTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageProcessingTemplates(self, request):
        r"""This API is used to query the list of image processing templates based on conditions with paging.

        :param request: Request instance for DescribeImageProcessingTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeImageProcessingTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeImageProcessingTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageProcessingTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageProcessingTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageReviewUsageData(self, request):
        r"""This API is used to return the daily image moderation usage information within the specified query time range.
        1. Image moderation statistics data from the last 365 days can be queried.
           2. The query time span should not exceed 90 days.
        3. If the query time span exceeds 1 day, the data is returned at a granularity of 1 day. Otherwise, the data is returned at a granularity of 5 minutes.

        :param request: Request instance for DescribeImageReviewUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeImageReviewUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeImageReviewUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageReviewUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageReviewUsageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageSpriteTemplates(self, request):
        r"""This API is used to query sprite sheet templates based on conditions with paging.

        :param request: Request instance for DescribeImageSpriteTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeImageSpriteTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeImageSpriteTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageSpriteTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageSpriteTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJustInTimeTranscodeTemplates(self, request):
        r"""Queries the list of instant transcoding templates.

        :param request: Request instance for DescribeJustInTimeTranscodeTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeJustInTimeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeJustInTimeTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJustInTimeTranscodeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJustInTimeTranscodeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKnowledgeBases(self, request):
        r"""Query the knowledge base list. Return all knowledge base information under the specified user.

        :param request: Request instance for DescribeKnowledgeBases.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeKnowledgeBasesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeKnowledgeBasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKnowledgeBases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKnowledgeBasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLLMComprehendTemplates(self, request):
        r"""This API is used to obtain the template detail list of large model parsing templates based on the Template Unique Identifier. The returned results include all eligible user-customized large model parsing templates.

        :param request: Request instance for DescribeLLMComprehendTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeLLMComprehendTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeLLMComprehendTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLLMComprehendTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLLMComprehendTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseUsageData(self, request):
        r"""This API is used to return the daily License request count within the specified query time range.
        1. License request count stats from the last 365 days can be queried.
           2. The query time span should not exceed 90 days.
        3. If the query time span exceeds 1 day, the data returned is at day granularity. Otherwise, the data returned is at 5-minute granularity.

        :param request: Request instance for DescribeLicenseUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeLicenseUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeLicenseUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseUsageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMPSTemplates(self, request):
        r"""This API is used to obtain user-customized media processing service task templates.
        When querying the template list, fill in MPS-related parameters in MPSDescribeTemplateParams in JSON format. For task parameter configuration, refer to the MPS task template documentation.

        :param request: Request instance for DescribeMPSTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeMPSTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeMPSTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMPSTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMPSTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMediaInfos(self, request):
        r"""1. This API can obtain multiple types of info of multiple media files, including:
        1. Basic information (basicInfo): including media name, categorization, playback address, cover image, and more.
        2. Meta information (metaData): including size, duration, video stream information, and audio stream information.
        3. Transcode result information (transcodeInfo): includes media addresses of various specifications generated by transcoding the media, video stream parameters, audio stream parameters, etc.
        4. Animated graphics info (animatedGraphicsInfo): the animated graphics info after converting a video to gif (for example, gif).
        5. sampleSnapshotInfo: sampling screenshot information.
        6. Sprite image information (imageSpriteInfo): sprite image information after capturing sprite image files from a video.
        7. snapshotByTimeOffsetInfo: screenshot information after taking screenshots of a video at specified time points.
        8. Video timestamp information (keyFrameDescInfo): Dotting information set for a video.
        9. Adaptive Bitrate Streaming information (adaptiveDynamicStreamingInfo): information including specification, encryption type, and packaging format.
        10. Review information (reviewInfo): includes media moderation and media cover review information.
        2. You can specify to only return partial information in the response.

        :param request: Request instance for DescribeMediaInfos.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeMediaInfosRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeMediaInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMediaInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMediaInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMediaPlayStatDetails(self, request):
        r"""This API is used to query playback data of media files by specified time granularity.
        * Playback statistics from the past one year can be queried.
        Time granularity: hour. The maximum span between start time and end time is 7 days.
        Time granularity: day. The maximum span between the end time and start time is 90 days.
        * Playback statistics only target VOD domains (distribution from EdgeOne domain names is not included in playback statistics).

        :param request: Request instance for DescribeMediaPlayStatDetails.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeMediaPlayStatDetailsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeMediaPlayStatDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMediaPlayStatDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMediaPlayStatDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMediaProcessUsageData(self, request):
        r"""This API is used to return the daily video processing usage information within the specified query time range.
        1. Video processing usage data is retained in the data system for 13 months. You can query usage data from the most recent 365 days through the API. To call historical usage data beyond 365 days, contact us.
           2. The query time span should not exceed 90 days.

        :param request: Request instance for DescribeMediaProcessUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeMediaProcessUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeMediaProcessUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMediaProcessUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMediaProcessUsageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePersonSamples(self, request):
        r"""This API is used to query material sample information by material ID, name, or tag with pagination.

        :param request: Request instance for DescribePersonSamples.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribePersonSamplesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribePersonSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePersonSamples", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcedureTemplates(self, request):
        r"""This API is used to search the task flow template detail list based on the task flow template name.

        :param request: Request instance for DescribeProcedureTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeProcedureTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeProcedureTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcedureTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcedureTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcessImageAsyncTemplates(self, request):
        r"""This API is used to obtain the template details list based on the template unique identifier. The returned results include all eligible user-customized image asynchronous processing templates.

        :param request: Request instance for DescribeProcessImageAsyncTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeProcessImageAsyncTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeProcessImageAsyncTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessImageAsyncTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessImageAsyncTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQualityInspectTemplates(self, request):
        r"""This API is used to query the audio and video quality detection template list.

        :param request: Request instance for DescribeQualityInspectTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeQualityInspectTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeQualityInspectTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityInspectTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityInspectTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRebuildMediaTemplates(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of the [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        Queries the video rebirth template list.

        :param request: Request instance for DescribeRebuildMediaTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeRebuildMediaTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeRebuildMediaTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRebuildMediaTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRebuildMediaTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReviewDetails(self, request):
        r"""<b>This API is not recommended. Use [DescribeMediaProcessUsageData](https://www.tencentcloud.com/document/product/266/41464?from_cn_redirect=1) as an alternative.</b>

        This API is used to return the daily video content intelligent identification duration data within the specified query time range. Unit: seconds.

        1. Video content intelligent identification duration stats from the last 365 days can be queried.
        2. The query time span should not exceed 90 days.

        :param request: Request instance for DescribeReviewDetails.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeReviewDetailsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeReviewDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReviewDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReviewDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReviewTemplates(self, request):
        r"""This API is used to query the moderation template list.
        >Template is applicable only to the [audio/video moderation (ReviewAudioVideo)](https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) and [image moderation (ReviewImage)](https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1) APIs.

        :param request: Request instance for DescribeReviewTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeReviewTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeReviewTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReviewTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReviewTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoundPlays(self, request):
        r"""This API is used to get the carousel playlist list.

        :param request: Request instance for DescribeRoundPlays.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeRoundPlaysRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeRoundPlaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoundPlays", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoundPlaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSampleSnapshotTemplates(self, request):
        r"""This API is used to query sampled screenshot templates based on conditions with paging.

        :param request: Request instance for DescribeSampleSnapshotTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeSampleSnapshotTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeSampleSnapshotTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSampleSnapshotTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSampleSnapshotTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotByTimeOffsetTemplates(self, request):
        r"""Queries specified time point screenshot templates and supports paging query based on conditions.

        :param request: Request instance for DescribeSnapshotByTimeOffsetTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeSnapshotByTimeOffsetTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeSnapshotByTimeOffsetTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotByTimeOffsetTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotByTimeOffsetTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStorageData(self, request):
        r"""Queries storage space usage and number of files.

        :param request: Request instance for DescribeStorageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeStorageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeStorageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStorageDetails(self, request):
        r"""This API is used to return the VOD storage space used within a specified time range, in bytes.
        1. Storage usage data is retained for 13 months in the data system. You can only query usage data from the most recent 365 days through the API. If you need to access historical usage data beyond 365 days, contact us;
        2. The query time span should not exceed 90 days.
        3. The query span at a minute granularity should not exceed 7 days;

        :param request: Request instance for DescribeStorageDetails.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeStorageDetailsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeStorageDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorageDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStorageRegions(self, request):
        r"""This API is used to:
        1. Query the list of all storage campuses available for on-demand activation.
        2. Query the list of opened parks.
        3. Query the storage campus used by default.

        :param request: Request instance for DescribeStorageRegions.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeStorageRegionsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeStorageRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorageRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubAppIds(self, request):
        r"""This API is used to get the application list of the current account.

        :param request: Request instance for DescribeSubAppIds.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeSubAppIdsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeSubAppIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubAppIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubAppIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSuperPlayerConfigs(self, request):
        r"""This API is <font color='red'>no longer maintained</font>. The new version of player signature no longer uses player configuration templates. For details, please see [Player Signature](https://www.tencentcloud.com/document/product/266/45554?from_cn_redirect=1).
        Queries player configurations and supports paging query based on conditions.

        :param request: Request instance for DescribeSuperPlayerConfigs.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeSuperPlayerConfigsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeSuperPlayerConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSuperPlayerConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSuperPlayerConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskDetail(self, request):
        r"""This API is used to query the details of the task execution status and results by task ID (tasks submitted within the last 3 days can be queried).

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        r"""* This API is used to query the task list.
        * When the list contains a large amount of data, a single API call cannot pull the entire list. You can use the ScrollToken parameter to pull in batches.
        * Only tasks from the last three days (72 hours) can be queried.

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTranscodeTemplates(self, request):
        r"""This API is used to retrieve the transcoding template detail list based on the transcoding template unique identifier. The returned results include all eligible custom templates and [system preset transcoding templates](https://www.tencentcloud.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF).

        :param request: Request instance for DescribeTranscodeTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVodDomains(self, request):
        r"""This API is used to query the list of on-demand video domain names.

        :param request: Request instance for DescribeVodDomains.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeVodDomainsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeVodDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVodDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVodDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVoices(self, request):
        r"""Query the available timbre list under the current account. It supports filtering by optional conditions such as voice ID, kind, name, gender, age, language, tag, and scenario.

        Note: Newly designed or cloned voice types cannot be queried before activation. They are activated only after the newly created voice type is used for TTS once.

        :param request: Request instance for DescribeVoices.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeVoicesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeVoicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVoices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVoicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWatermarkTemplates(self, request):
        r"""This API is used to query user-defined watermark templates, and paging query is supported based on conditions.

        :param request: Request instance for DescribeWatermarkTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeWatermarkTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeWatermarkTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWatermarkTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWatermarkTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWordSamples(self, request):
        r"""This API is used to paginate keyword sample information by scenario, keyword, and tag.

        :param request: Request instance for DescribeWordSamples.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeWordSamplesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeWordSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWordSamples", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWordSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DesignVoiceAsync(self, request):
        r"""This API is used to initiate a voice design task. It generates a custom voice based on a natural language description. You can also specify a voice profile, such as name, gender, age, language, tag, and scenario. If trial text is attached upon submission, an audio audition is generated after task completion. Voice design is an asynchronous task, and the voice ID is generated after task completion.

        :param request: Request instance for DesignVoiceAsync.
        :type request: :class:`tencentcloud.vod.v20180717.models.DesignVoiceAsyncRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DesignVoiceAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DesignVoiceAsync", params, headers=headers)
            response = json.loads(body)
            model = models.DesignVoiceAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditMedia(self, request):
        r"""This API is used to edit a video, such as clipping and concatenation, to generate a new on-demand video. Editing features include:

        1) Edit a file in on-demand playback to generate a new video.
        2) Splice multiple on-demand files to generate a new video.
        3) Edit multiple on-demand video files and then splice them to generate a new video;
        4. Directly generate a new video for one stream in VOD;
        5. Edit one stream in VOD to generate a new video;
        6) Splice multiple on-demand streams to generate a new video.
        7) Edit multiple streams in VOD and then splice them to generate a new video.

        For the generated new video, you can also specify whether to execute task flow for the generated video.

        When editing or splicing a live stream, please ensure the stream ended before you operate. Otherwise, the generated video may be incomplete.

        If event notification is used, its type is [video editing completed](https://www.tencentcloud.com/document/product/266/33794?from_cn_redirect=1).

        :param request: Request instance for EditMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.EditMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.EditMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditMedia", params, headers=headers)
            response = json.loads(body)
            model = models.EditMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnhanceMediaByTemplate(self, request):
        r"""This API is <font color=red>no longer maintained</font>. Please use the new version of APIs [audio and video quality revival](https://www.tencentcloud.com/document/api/266/102571?from_cn_redirect=1).
        Use a template to initiate audio and video quality revival.

        :param request: Request instance for EnhanceMediaByTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.EnhanceMediaByTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.EnhanceMediaByTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnhanceMediaByTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.EnhanceMediaByTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnhanceMediaQuality(self, request):
        r"""This API is used to initiate an audio and video quality regeneration task for on-demand audio-video media.

        :param request: Request instance for EnhanceMediaQuality.
        :type request: :class:`tencentcloud.vod.v20180717.models.EnhanceMediaQualityRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.EnhanceMediaQualityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnhanceMediaQuality", params, headers=headers)
            response = json.loads(body)
            model = models.EnhanceMediaQualityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteFunction(self, request):
        r"""This API is only used for special scenarios of customized development. Do not call this API unless VOD customer service proactively informs you to use it.

        :param request: Request instance for ExecuteFunction.
        :type request: :class:`tencentcloud.vod.v20180717.models.ExecuteFunctionRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ExecuteFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteFunction", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExtractBlindWatermark(self, request):
        r"""This API is used to initiate a digital watermark extraction task for a video. The extraction result can be queried through DescribeTaskDetail.

        :param request: Request instance for ExtractBlindWatermark.
        :type request: :class:`tencentcloud.vod.v20180717.models.ExtractBlindWatermarkRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ExtractBlindWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExtractBlindWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.ExtractBlindWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExtractCopyRightWatermark(self, request):
        r"""If you need source tracing for piracy, see Ghost Watermark (https://www.tencentcloud.com/document/product/266/94228?from_cn_redirect=1).

        :param request: Request instance for ExtractCopyRightWatermark.
        :type request: :class:`tencentcloud.vod.v20180717.models.ExtractCopyRightWatermarkRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ExtractCopyRightWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExtractCopyRightWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.ExtractCopyRightWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExtractTraceWatermark(self, request):
        r"""If source tracing for piracy is required, ghost watermark is recommended for use (https://www.tencentcloud.com/document/product/266/94228?from_cn_redirect=1).

        :param request: Request instance for ExtractTraceWatermark.
        :type request: :class:`tencentcloud.vod.v20180717.models.ExtractTraceWatermarkRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ExtractTraceWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExtractTraceWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.ExtractTraceWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FastEditMedia(self, request):
        r"""Quickly splice and edit HLS videos in VOD to generate new media in HLS format.

        Quickly splice or edit the generated video to create a new FileId and solidify it. After successful solidification, the new video file exists independently of the original input video and is not affected by deletion of the original video.

        <font color='red'>Note:</font> Enable reception of editing solidification event notifications through the ModifyEventConfig API. After successful solidification, you will receive a PersistenceComplete event notification. Before receiving this event notification, you should not delete or transition the original input video to colder storage. Otherwise, playback of the video generated by splicing and clipping may be abnormal.

        :param request: Request instance for FastEditMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.FastEditMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.FastEditMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FastEditMedia", params, headers=headers)
            response = json.loads(body)
            model = models.FastEditMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForbidMediaDistribution(self, request):
        r"""* After media blocking, except for VOD console preview, accessing URLs of various video resources (original files, transcoding output files, screenshots, etc.) for other scenarios will return 403.
        It takes about 5 to 10 minutes for the block or unblock operation to take effect across the entire network.
        * Note: Media blocking can only be performed on media stored in standard storage and infrequent storage. Media stored in infrequent storage must be stored for at least 30 days. If it is deleted early or its storage class is changed, it will still be billed for 30 days. If media stored in infrequent storage is blocked and its infrequent storage duration is less than 30 days, early deletion billing will occur. In addition, after blocking, the infrequent storage duration of the media will restart from the current time. If the media is deleted or its storage class is changed before reaching 30 days, early deletion billing will also occur. For example, media 001 has been stored in infrequent storage for 10 days. If 001 is blocked at this point, infrequent storage billing is still calculated based on 30 days (early deletion billing duration: 30 - 10 = 20 days). After blocking, the infrequent storage duration of 001 restarts. If 001 is deleted on the 5th day after blocking, infrequent storage billing is also calculated based on 30 days (early deletion billing duration: 30 - 5 = 25 days). The actual infrequent storage duration of 001 is 10 + 5 = 15 days, while the infrequent storage billing duration is 10 + 20 (early deletion billing) + 5 + 25 (early deletion billing) = 60 days.

        :param request: Request instance for ForbidMediaDistribution.
        :type request: :class:`tencentcloud.vod.v20180717.models.ForbidMediaDistributionRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ForbidMediaDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForbidMediaDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.ForbidMediaDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HandleCurrentPlaylist(self, request):
        r"""Manipulate the carousel current playlist. Supported operations: <li> Insert: Insert a program into the current playlist.</li><li> Delete: Delete a program from the playlist.</li>

        :param request: Request instance for HandleCurrentPlaylist.
        :type request: :class:`tencentcloud.vod.v20180717.models.HandleCurrentPlaylistRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.HandleCurrentPlaylistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HandleCurrentPlaylist", params, headers=headers)
            response = json.loads(body)
            model = models.HandleCurrentPlaylistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportMediaKnowledge(self, request):
        r"""Used to import AI analysis results into the knowledge base.

        :param request: Request instance for ImportMediaKnowledge.
        :type request: :class:`tencentcloud.vod.v20180717.models.ImportMediaKnowledgeRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ImportMediaKnowledgeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportMediaKnowledge", params, headers=headers)
            response = json.loads(body)
            model = models.ImportMediaKnowledgeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InspectMediaQuality(self, request):
        r"""This API is used to initiate an audio and video quality inspection task for on-demand audio-video media.

        :param request: Request instance for InspectMediaQuality.
        :type request: :class:`tencentcloud.vod.v20180717.models.InspectMediaQualityRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.InspectMediaQualityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InspectMediaQuality", params, headers=headers)
            response = json.loads(body)
            model = models.InspectMediaQualityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListFiles(self, request):
        r"""This API is used to list stored file entries under a sub-application.

        **This API is only available in "FileID+Path mode"**

        :param request: Request instance for ListFiles.
        :type request: :class:`tencentcloud.vod.v20180717.models.ListFilesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ListFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ListFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LiveRealTimeClip(self, request):
        r"""Live stream clipping refers to the ability for customers to select a segment from the live stream content during live streaming (that is, before the live stream has ended), and generate a new video in HLS format in real time. Developers can share it immediately or save it for long-term preservation.

        Tencent Cloud VOD supports two real-time clipping modes:
        - Edit and save: Save the edited video as a standalone video with an independent FileId. This is suitable for long-term preservation of highlights.
        - Editing is not solidified: The edited video is attached to the live streaming recording file and has no standalone FileId. This is suitable for scenarios where highlights are shared temporarily.

        Note:
        - The premise for using the live stream clipping feature is that the target live stream has the time shifting and playback (https://www.tencentcloud.com/document/product/267/32742?from_cn_redirect=1) feature enabled.
        -Live streaming Instant Editing is based on the m3u8 file generated by live recording, so its minimum editing precision is one ts slice. Second-level or more precise editing precision cannot be achieved.
        -Since stream disconnection may occur during live streaming, the actual video duration generated by editing may differ from the expected duration. For example, if you edit a live stream from 2018-09-20T10:30:00Z to 2018-09-20T10:40:00Z, and stream disconnection occurred during this time interval, the returned media file duration will be less than 10 minutes. In such cases, you can perceive it through the output parameter <a href="#p_segmentset">SegmentSet</a>.

        ### Edit solidification
        Clipping persistence refers to saving an edited video as an independent video with its own FileId. Its lifecycle is not subject to any impact from the original live recorded video. Even if the original recorded video is deleted, the clipping result is not affected. You can also transcode it or publish it on WeChat for secondary processing.

        For example, a complete football match live recording may produce raw video lasting for over 2 hours. For cost savings, a customer can store this video for 2 months, but can specify longer storage for highlight videos from live stream clipping. You can also perform additional on-demand operations on highlight videos separately, such as transcoding and publishing on WeChat. In this case, you can choose a live stream clipping and persistent solution.

        The advantage of solidified editing is that its lifecycle is independent of the original recorded video, allowing for separate management and long-term preservation.

        <font color='red'>Note:</font> If solidification is specified when editing, enable reception of editing solidification event notifications through the ModifyEventConfig API. After successful solidification, you will receive a PersistenceComplete event notification. Before receiving this event notification, you should not delete or transition the live video recording to colder storage. Otherwise, playback of the generated video may be abnormal.

        ### Editing is not solidified
        So-called non-solidified editing means that the result of editing (m3u8 file) shares the same TS segments with the live video recording. The newly generated video is not an independent and complete video (no standalone FileId, only a playback URL), and its valid period is consistent with that of the full live recording video. Once the live recording video is deleted, the clip will also become unplayable.

        Editing is not solidified. Since the clipping result is not an independent video, it is not included in video management of on-demand media assets (for example, the total number of videos in the console does not count this clip), and no video processing operation such as transcoding or publishing on WeChat can be performed against this clip separately.

        The advantage of non-solidified editing is that the editing operation is relatively "lightweight" and will not generate additional storage overhead. However, its shortcoming is that the lifecycle is identical to the original recorded video, and it is unable to further transcode or perform other video processing.

        :param request: Request instance for LiveRealTimeClip.
        :type request: :class:`tencentcloud.vod.v20180717.models.LiveRealTimeClipRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.LiveRealTimeClipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LiveRealTimeClip", params, headers=headers)
            response = json.loads(body)
            model = models.LiveRealTimeClipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageTask(self, request):
        r"""Manage initiated tasks.

        :param request: Request instance for ManageTask.
        :type request: :class:`tencentcloud.vod.v20180717.models.ManageTaskRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ManageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageTask", params, headers=headers)
            response = json.loads(body)
            model = models.ManageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAIAnalysisTemplate(self, request):
        r"""This API is used to modify a user-defined audio and video content analysis template.

        Note: Templates with IDs below 10000 are system-preset templates and cannot be modified.

        :param request: Request instance for ModifyAIAnalysisTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAIAnalysisTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAIAnalysisTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAIRecognitionTemplate(self, request):
        r"""This API is used to modify a user-defined audio and video content recognition template.

        :param request: Request instance for ModifyAIRecognitionTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAIRecognitionTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAIRecognitionTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAdaptiveDynamicStreamingTemplate(self, request):
        r"""Modifying an Adaptive Bitrate Streaming Template

        :param request: Request instance for ModifyAdaptiveDynamicStreamingTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAdaptiveDynamicStreamingTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAdaptiveDynamicStreamingTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAigcQuota(self, request):
        r"""Used to edit AIGC quota configuration. Quota usage starts accumulating when the quota feature is enabled. Once the quota is reached, AIGC features will no longer be usable.

        Since AGC content generation is an async task, real-time usage data cannot be obtained. Therefore, quota limits result in some errors, and complete precise control with the set limit cannot be achieved.

        :param request: Request instance for ModifyAigcQuota.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyAigcQuotaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyAigcQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAigcQuota", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAigcQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAnimatedGraphicsTemplate(self, request):
        r"""Modify a custom animated image generating template.

        :param request: Request instance for ModifyAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAnimatedGraphicsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAnimatedGraphicsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlindWatermarkTemplate(self, request):
        r"""This API is used to modify a user-defined digital watermark template. The digital watermark type cannot be modified.

        :param request: Request instance for ModifyBlindWatermarkTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyBlindWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyBlindWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlindWatermarkTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlindWatermarkTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCDNDomainConfig(self, request):
        r"""Modify CDN Domain Config.

        :param request: Request instance for ModifyCDNDomainConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyCDNDomainConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyCDNDomainConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCDNDomainConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCDNDomainConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClass(self, request):
        r"""Modify media classification attributes.

        :param request: Request instance for ModifyClass.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyClassRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClass", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyContentReviewTemplate(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of moderation template supports audio/video moderation and image moderation. For details, please see [Modify Moderation Template](https://www.tencentcloud.com/document/api/266/84388?from_cn_redirect=1).
        Modify a user-customized audio/video moderation template.

        :param request: Request instance for ModifyContentReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyContentReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyContentReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDefaultDistributionConfig(self, request):
        r"""This API is used to modify the default distribution configuration.
        * Distribution domain name and distribution protocol, i.e., the domain name and protocol in the media file distribution URL. Media files are distributed based on the default distribution configuration.
        Playback key, used to calculate player signature.

        :param request: Request instance for ModifyDefaultDistributionConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyDefaultDistributionConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyDefaultDistributionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDefaultDistributionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDefaultDistributionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDefaultStorageRegion(self, request):
        r"""This API is used to set the default storage region. If no region is specified during file upload, files will be uploaded to the default region.

        :param request: Request instance for ModifyDefaultStorageRegion.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyDefaultStorageRegionRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyDefaultStorageRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDefaultStorageRegion", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDefaultStorageRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnhanceMediaTemplate(self, request):
        r"""This API is no longer maintained. The new version of the [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        Modify an audio and video quality rebirth template.

        :param request: Request instance for ModifyEnhanceMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyEnhanceMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyEnhanceMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnhanceMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnhanceMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEventConfig(self, request):
        r"""Tencent Cloud VOD provides customers with media upload, media management, media processing, and other services. During or after the execution of these services, Tencent Cloud VOD also offers various corresponding event notifications, allowing developers to detect the service processing status and perform the next business operation.

        Developers can call this interface to:
        - Set the type for receiving callback notifications. Currently, there are two types: [HTTP callback notification](https://www.tencentcloud.com/document/product/266/33779?from_cn_redirect=1) and [reliable notification based on message queue](https://www.tencentcloud.com/document/product/266/33779?from_cn_redirect=1).
        - For [HTTP callback notification](https://www.tencentcloud.com/document/product/266/33779?from_cn_redirect=1), you can set the address for 3.0 format callback. For 3.0 format callback details, see [historical format callback](https://www.tencentcloud.com/document/product/266/33796?from_cn_redirect=1).
        -Select to receive or ignore notification events for a specific event service.

        :param request: Request instance for ModifyEventConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyEventConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyEventConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEventConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEventConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHeadTailTemplate(self, request):
        r"""Modify a title and trailer template.

        :param request: Request instance for ModifyHeadTailTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyHeadTailTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyHeadTailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHeadTailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHeadTailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageSpriteTemplate(self, request):
        r"""Modify a user-customized image sprite template.

        :param request: Request instance for ModifyImageSpriteTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageSpriteTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageSpriteTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyJustInTimeTranscodeTemplate(self, request):
        r"""Modify a just in time transcoding template.
        -Note: Once a just in time transcoding template is created, modification is not recommended. If parameter modification is needed, adding a template is recommended.

        :param request: Request instance for ModifyJustInTimeTranscodeTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyJustInTimeTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyJustInTimeTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyJustInTimeTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyJustInTimeTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyKnowledgeBase(self, request):
        r"""This API is used to modify a knowledge base. The name and/or description of the knowledge base can be modified. At least one of the Name or Description fields is required.

        :param request: Request instance for ModifyKnowledgeBase.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyKnowledgeBaseRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyKnowledgeBaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyKnowledgeBase", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyKnowledgeBaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLLMComprehendTemplate(self, request):
        r"""Modify a large model parsing template

        :param request: Request instance for ModifyLLMComprehendTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyLLMComprehendTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyLLMComprehendTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLLMComprehendTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLLMComprehendTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMPSTemplate(self, request):
        r"""Modify a user-customized MPS task template.
        When modifying a template, fill in the MPS related parameters in JSON format into the MPSModifyTemplateParams parameter. For specific task parameter configuration methods, see the MPS task template related documentation.

        :param request: Request instance for ModifyMPSTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyMPSTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyMPSTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMPSTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMPSTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMediaInfo(self, request):
        r"""This API is used to modify the attributes of a media file, including category, name, description, tag, expiration time, dotting information, video cover, and subtitle information.

        :param request: Request instance for ModifyMediaInfo.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyMediaInfoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyMediaInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMediaInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMediaInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMediaStorageClass(self, request):
        r"""Modifies the storage type of media files.
        When the storage type of a media file is standard storage, it can be modified to the following types:
        <li>Infrequent storage</li>
        <li>Archive storage</li>
        <li>DEEP_ARCHIVE</li>
        When the current storage type of a media file is infrequent storage, it can be modified to the following types:
        <li>Standard storage</li>
        <li>Archive storage</li>
        <li>DEEP_ARCHIVE</li>
        When the current storage type of a media file is archive storage, it can be modified to the following types:
        <li>Standard storage</li>
        When the current storage type of a media file is DEEP_ARCHIVE, it can be modified to the following types:
        <li>Standard storage</li>

        :param request: Request instance for ModifyMediaStorageClass.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyMediaStorageClassRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyMediaStorageClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMediaStorageClass", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMediaStorageClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPersonSample(self, request):
        r"""This API is used to modify material sample information based on the material ID, including modification of the name and description, as well as addition, deletion, and reset of facial features and tags. Ensure at least 1 image remains after facial feature deletion. Otherwise, use the reset operation.

        :param request: Request instance for ModifyPersonSample.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyPersonSampleRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyPersonSampleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPersonSample", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPersonSampleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProcessImageAsyncTemplate(self, request):
        r"""This API is used to modify a user-customized image async processing template.

        Note: Templates with IDs below 10000 are preset templates and are not allowed to be modified.

        :param request: Request instance for ModifyProcessImageAsyncTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyProcessImageAsyncTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyProcessImageAsyncTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProcessImageAsyncTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProcessImageAsyncTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQualityInspectTemplate(self, request):
        r"""This API is used to modify an audio and video quality inspection template.

        :param request: Request instance for ModifyQualityInspectTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyQualityInspectTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyQualityInspectTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQualityInspectTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQualityInspectTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRebuildMediaTemplate(self, request):
        r"""This API is <font color=red>no longer maintained</font>. The new version of [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) interface uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        Modifying a Video Rebirth Template.

        :param request: Request instance for ModifyRebuildMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyRebuildMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyRebuildMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRebuildMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRebuildMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReviewTemplate(self, request):
        r"""Modifies a user-customized moderation template.
        >Template is applicable only to the ReviewAudioVideo (https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) and ReviewImage (https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1) APIs.

        :param request: Request instance for ModifyReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRoundPlay(self, request):
        r"""This API is used to modify a carousel playlist.
        After modification, only new playback requests will take effect. Users already playing can still play the previous playlist within 7 days.

        :param request: Request instance for ModifyRoundPlay.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyRoundPlayRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyRoundPlayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoundPlay", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoundPlayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySampleSnapshotTemplate(self, request):
        r"""Modify a user-customized sampled screenshot template.

        :param request: Request instance for ModifySampleSnapshotTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifySampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifySampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySampleSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySampleSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshotByTimeOffsetTemplate(self, request):
        r"""Modify a user-customized specified time point screenshot template.

        :param request: Request instance for ModifySnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifySnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifySnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshotByTimeOffsetTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotByTimeOffsetTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubAppIdInfo(self, request):
        r"""This API is used to change application information, but default application information is not allowed to be modified.

        :param request: Request instance for ModifySubAppIdInfo.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifySubAppIdInfoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifySubAppIdInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubAppIdInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubAppIdInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubAppIdStatus(self, request):
        r"""This API is used to enable or disable applications. Disabled applications will have their corresponding domains blocked and console access restricted.

        :param request: Request instance for ModifySubAppIdStatus.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifySubAppIdStatusRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifySubAppIdStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubAppIdStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubAppIdStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySuperPlayerConfig(self, request):
        r"""This API is <font color='red'>no longer maintained</font>. The new version of player signature no longer uses player configuration templates. For details, please see [Player Signature](https://www.tencentcloud.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to modify player configuration.

        :param request: Request instance for ModifySuperPlayerConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifySuperPlayerConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifySuperPlayerConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySuperPlayerConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySuperPlayerConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTranscodeTemplate(self, request):
        r"""Modify the information of a custom transcoding template.

        :param request: Request instance for ModifyTranscodeTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVodDomainAccelerateConfig(self, request):
        r"""This API is used to modify the acceleration region of a VOD domain.
        1. The acceleration region can be modified only when the domain name deployment state is Online.

        :param request: Request instance for ModifyVodDomainAccelerateConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyVodDomainAccelerateConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyVodDomainAccelerateConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVodDomainAccelerateConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVodDomainAccelerateConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVodDomainConfig(self, request):
        r"""This API is used to modify domain name configuration, including hotlink protection configuration.
        1. The domain name configuration can be modified only when the domain name deployment state is Online.

        :param request: Request instance for ModifyVodDomainConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyVodDomainConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyVodDomainConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVodDomainConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVodDomainConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWatermarkTemplate(self, request):
        r"""This API is used to modify a user-defined watermark template. The watermark type cannot be modified.

        :param request: Request instance for ModifyWatermarkTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWatermarkTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWatermarkTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWordSample(self, request):
        r"""This API is used to modify the application scenario and tags of a keyword. The keyword itself cannot be modified. If modification is needed, delete and rebuild it.

        :param request: Request instance for ModifyWordSample.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyWordSampleRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyWordSampleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWordSample", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWordSampleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ParseStreamingManifest(self, request):
        r"""When uploading HLS videos, this API parses the index file content and returns a list of shard files to be uploaded. The shard file path must be a relative path in the current directory or subdirectory. It cannot be a URL or an absolute path.

        :param request: Request instance for ParseStreamingManifest.
        :type request: :class:`tencentcloud.vod.v20180717.models.ParseStreamingManifestRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ParseStreamingManifestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ParseStreamingManifest", params, headers=headers)
            response = json.loads(body)
            model = models.ParseStreamingManifestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessImageAsync(self, request):
        r"""This API is used to process image tasks.

        :param request: Request instance for ProcessImageAsync.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessImageAsyncRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessImageAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessImageAsync", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessImageAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessMedia(self, request):
        r"""This API is used to initiate processing tasks for audio-video media in VOD, with features including:
        1. Watermarked video transcoding;
        2. Animated image generating;
        3. Screenshot taking at specified time points;
        4. Sampled screenshot taking;
        5. Capture CSS sprites for videos;
        6. Capture a frame from a video as the cover.
        7. Transcoding to adaptive bitrate streaming (and encrypting);
        8. Content review (offensive content, unsafe information, inappropriate information), it is <font color=red>not recommended</font> to use this API to initiate. It is recommended to use [Audio/Video Moderation (ReviewAudioVideo)](https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) or [Image Moderation (ReviewImage)](https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1);
        9. Content analysis (tag, categorization, cover, frame tagging), HLS format not supported currently.
        10. Content recognition (video intro and outro, human face, full text, text keyword, full speech, speech keyword, object).

        If event notification is used, the event notification type is task flow status change (https://www.tencentcloud.com/document/product/266/9636?from_cn_redirect=1).

        :param request: Request instance for ProcessMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMedia", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessMediaByMPS(self, request):
        r"""Use the media processing capability of Media Processing Service (MPS) to initiate media processing for videos in VOD.
        Currently supported MPS features:
        1. Smart subtitling: The feature supports processing offline audio files, video files, and live streams. It can extract subtitles in the video source language through ASR speech recognition or OCR text recognition, and implement multilingual translation. View details in the integration guide (https://www.tencentcloud.com/document/product/266/131210?from_cn_redirect=1).
        2. Intelligent erasure: It can blur, mosaic, or seamlessly process elements such as logos, subtitles, human faces, and license plates in video footage, making it easy to spread and share content. The new video generated by this task will be assigned a new FileId and stored in a subapplication of the VOD platform. For details, see the Access Guide (https://www.tencentcloud.com/document/product/266/131211?from_cn_redirect=1).
        3. AI analysis: This feature supports all-in-one translation (https://www.tencentcloud.com/document/product/266/131212?from_cn_redirect=1), highlights (https://www.tencentcloud.com/document/product/266/131213?from_cn_redirect=1), LLM video summary (https://www.tencentcloud.com/document/product/266/131214?from_cn_redirect=1), LLM audio/video understanding (https://www.tencentcloud.com/document/product/266/131215?from_cn_redirect=1), intelligent splitting (https://www.tencentcloud.com/document/product/266/131216?from_cn_redirect=1), intelligent landscape-to-portrait (https://www.tencentcloud.com/document/product/266/131217?from_cn_redirect=1), video deduplication (https://www.tencentcloud.com/document/product/266/131218?from_cn_redirect=1), and other features.


        > Video processing tasks initiated this method:
        > 1. Query of task status and results is still completed in the VOD platform. Use [DescribeTaskDetail](https://www.tencentcloud.com/document/product/266/33431?from_cn_redirect=1) or [DescribeTasks](https://www.tencentcloud.com/document/product/266/33430?from_cn_redirect=1) to query tasks.
        > 2. The amount and bills of related features will be provided on the PS platform. Before using this feature, first enable Media Processing Service (MPS) in the console. For the activation method, see the preliminary operations in the access documentation.

        :param request: Request instance for ProcessMediaByMPS.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByMPSRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByMPSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMediaByMPS", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessMediaByMPSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessMediaByProcedure(self, request):
        r"""Use a task flow template to initiate processing tasks for videos in VOD.
        There are two ways to create a task flow template:
        1. Create and modify a task flow template in the console;
        2. Create a task flow template through the task flow template API.

        If event notification is used, the type of event notification for tasks other than audio/video moderation tasks is task flow status change (https://www.tencentcloud.com/document/product/266/9636?from_cn_redirect=1); the type of event notification for audio/video moderation tasks is audio/video moderation completed (https://www.tencentcloud.com/document/product/266/81258?from_cn_redirect=1).

        :param request: Request instance for ProcessMediaByProcedure.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByProcedureRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByProcedureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMediaByProcedure", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessMediaByProcedureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessMediaByUrl(self, request):
        r"""This API is <font color='red'>no longer maintained</font>. Please use the [ProcessMedia](https://www.tencentcloud.com/document/product/862/37578?from_cn_redirect=1) API of MPS and specify the video URL in the input parameter InputInfo.UrlInputInfo.Url.

        :param request: Request instance for ProcessMediaByUrl.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByUrlRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMediaByUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessMediaByUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PullEvents(self, request):
        r"""* This API is used for the business server to get event notifications via reliable callback (https://www.tencentcloud.com/document/product/266/33779?from_cn_redirect=1#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83);
        * The API uses long polling mode. If there are unconsumed events on the server, they will be returned to the requester immediately. If there are no unconsumed events, the request will be suspended in the background until a new event occurs.
        * The request can be suspended for up to 5 seconds. It is advisable to set the timeout to 10 seconds for the requester.
        * Event notifications that are not pulled are retained for up to 4 days. Notifications exceeding this time limit may be purged.
        * If this API returns an event, the caller must call the [Confirm Event Notification](https://www.tencentcloud.com/document/product/266/33434?from_cn_redirect=1) API within <font color="red">30 seconds</font> to confirm that the event notification has been processed. Otherwise, the event notification will be pulled again after <font color="red">30 seconds</font>.
        * Currently, a maximum of 16 event notifications can be obtained per API call.

        :param request: Request instance for PullEvents.
        :type request: :class:`tencentcloud.vod.v20180717.models.PullEventsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.PullEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullEvents", params, headers=headers)
            response = json.loads(body)
            model = models.PullEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PullUpload(self, request):
        r"""This API is used to pull a video from the network to the VOD platform.

        :param request: Request instance for PullUpload.
        :type request: :class:`tencentcloud.vod.v20180717.models.PullUploadRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.PullUploadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullUpload", params, headers=headers)
            response = json.loads(body)
            model = models.PullUploadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PushUrlCache(self, request):
        r"""1. Preheat the specified URL list.
        2. The domain name of the URL must be registered in VOD.
        3. Specify up to 20 URLs per request.
        4. The default prefetch quota is 10,000 URLs per day.

        :param request: Request instance for PushUrlCache.
        :type request: :class:`tencentcloud.vod.v20180717.models.PushUrlCacheRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.PushUrlCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PushUrlCache", params, headers=headers)
            response = json.loads(body)
            model = models.PushUrlCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebuildMedia(self, request):
        r"""This API is <font color=red>no longer maintained</font>. Please use the new version of APIs [audio and video quality revival](https://www.tencentcloud.com/document/api/266/102571?from_cn_redirect=1).
        This API is used to initiate audio and video quality revival.

        :param request: Request instance for RebuildMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.RebuildMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.RebuildMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebuildMedia", params, headers=headers)
            response = json.loads(body)
            model = models.RebuildMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebuildMediaByTemplate(self, request):
        r"""This API is <font color=red>no longer maintained</font>. Please use the new version of APIs for [audio and video quality revival](https://www.tencentcloud.com/document/api/266/102571?from_cn_redirect=1).
        Use a template to initiate video rebirth.

        :param request: Request instance for RebuildMediaByTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.RebuildMediaByTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.RebuildMediaByTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebuildMediaByTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.RebuildMediaByTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshUrlCache(self, request):
        r"""1. Refresh a specified URL list.
        2. The domain name of the URL must be registered in VOD.
        3. A maximum of 20 URLs can be specified per request.
        4. The default refresh quota is 100,000 URLs per day.

        :param request: Request instance for RefreshUrlCache.
        :type request: :class:`tencentcloud.vod.v20180717.models.RefreshUrlCacheRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.RefreshUrlCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshUrlCache", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshUrlCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveWatermark(self, request):
        r"""Watermark removal

        :param request: Request instance for RemoveWatermark.
        :type request: :class:`tencentcloud.vod.v20180717.models.RemoveWatermarkRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.RemoveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetProcedureTemplate(self, request):
        r"""Reset the content of the user-defined task flow template.

        :param request: Request instance for ResetProcedureTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ResetProcedureTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ResetProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetProcedureTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ResetProcedureTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestoreMedia(self, request):
        r"""If the storage type of a media file is archive storage or deep archive storage, it is inaccessible. If you need access, call this API to unfreeze it. After unfreezing, the accessible media file is temporary and becomes inaccessible after the validity period expires.

        :param request: Request instance for RestoreMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.RestoreMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.RestoreMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreMedia", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReviewAudioVideo(self, request):
        r"""This API is used to initiate a moderation task for on-demand audio-video media, intelligently detecting violative content in video footage, text in images, text in speech, and sound.

        If event notification is used, the event notification type is [audio/video moderation completed](https://www.tencentcloud.com/document/product/266/81258?from_cn_redirect=1).

        :param request: Request instance for ReviewAudioVideo.
        :type request: :class:`tencentcloud.vod.v20180717.models.ReviewAudioVideoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ReviewAudioVideoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReviewAudioVideo", params, headers=headers)
            response = json.loads(body)
            model = models.ReviewAudioVideoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReviewImage(self, request):
        r"""Initiate a review task for image files in VOD to detect offensive, unsafe, and inappropriate content.

        <li>Supported image file size: file < 5M;</li>
        <li>Image file resolution support: recommended resolution above 256x256, otherwise it may affect review effectiveness;</li>
        <li>Supported image file formats: PNG, JPG, JPEG, BMP, GIF, WEBP.</li>

        :param request: Request instance for ReviewImage.
        :type request: :class:`tencentcloud.vod.v20180717.models.ReviewImageRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ReviewImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReviewImage", params, headers=headers)
            response = json.loads(body)
            model = models.ReviewImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchMedia(self, request):
        r"""This API is used to search media information with multiple filter criteria, sort and filter returned results, and other features. This includes:
        -Specify the file ID collection FileIds to return media matching any ID in the collection.
        -Perform fuzzy search by multiple media file names (Names) or descriptions (Descriptions).
        -Search by multiple filename prefixes NamePrefixes.
        - Specify the category collection ClassIds (see input parameter), and media that meet any category in the collection will be returned. For example, media categories include movies, TV series, and variety shows. The movie category has subcategories such as historical films, action films, and romance films. If ClassIds specifies movies and TV series, all subcategories under movies and TV series will be returned. If ClassIds specifies historical films and action films, only media under these two subcategories will be returned.
        - Specify tag collection Tags (see input parameters) to return media that match any tag in the collection. For example, if media tags include ACG, palace intrigue, and parody remix, and Tags specifies ACG and parody remix, any media that meets either of these two tags will be retrieved.
        -Specified file type collection Categories (see input parameter). Returns media that meet any type in the collection. For example, file types include Video, Audio, and Image. If Categories specifies Video and Audio, media that meet these types will be retrieved.
        -Specify the source collection SourceTypes (see input parameters) to return media that meets any source in the collection. For example, media sources include Record (live recording), Upload, and so on. If SourceTypes specifies Record and Upload, media that meets these sources will be retrieved.
        -Specify the file packaging format set MediaTypes (see input parameters), and return media that meets any packaging format in the collection. For example, packaging formats include MP4, AVI, MP3, and so on. If MediaTypes specifies MP4 and MP3, then media that complies with these packaging formats will be retrieved.
        -Specify the file status collection Status (see input parameters) to return media that meet any status in the collection. For example, file statuses include Normal, SystemForbidden (Platform Ban), and Forbidden (proactive ban). If Status specifies Normal and Forbidden, media that meet these statuses will be retrieved.
        -Specify the file review result set ReviewResults (see input parameters) to return media that meets any status in the collection. For example, file review results include pass and block. If ReviewResults specifies both pass and block, media that complies with these review results will be retrieved.
        -Filter the media of live recording service by specifying the collection of live streaming codes StreamIds (see input parameter).
        -Filter media by the create time range of the specified media.
        -Specify a TRTC application ID collection to filter media.
        -Specify a TRTC room ID collection to filter media.

        - The above parameters can be combined in any way for retrieval. For example: filter media with a creation time between 2018-12-01 12:00:00 and 2018-12-08 12:00:00, categorized as movie or TV series, and tagged with palace intrigue and suspense. Note that for any parameter that supports array input, the search logic between its elements is "OR". The logical relationship between all parameters is "AND".

        -Allow passage of Filters to control the type of media information returned (default return all information). Selectable inputs include:
        1. Basic information (basicInfo): including media name, category, playback address, cover image, etc.
        2. Meta information (metaData): including size, duration, video stream information, and audio stream information.
        3. transcodeInfo: includes media addresses, video stream parameters, and audio stream parameters of various specifications generated for the transcoded media.
        4. animatedGraphicsInfo: The animated graphics info after converting a video to gif (for example, gif).
        5. sampleSnapshotInfo: screenshot information after sampling screenshots from the video.
        6. Sprite image information (imageSpriteInfo): sprite image information after capturing sprite images from a video.
        7. snapshotByTimeOffsetInfo: screenshot information after taking screenshots of a video at specified time points.
        8. Video timestamp information (keyFrameDescInfo): Dotting information set for the video.
        9. Adaptive Bitrate Streaming information (adaptiveDynamicStreamingInfo): information including specification, encryption type, and packaging format.

        -Permission to sort results by creation time and return in pages. Use Offset and Limit (see input parameters) to control pagination.

        <div id="maxResultsDesc">API return result count limit:</div>

        -<b><a href="#p_offset">Offset</a> and <a href="#p_limit">Limit</a> impact the number of results per pagination query. Special attention: when both are omitted, this interface returns up to 10 query results by default.</b>
        -<b>Supports returning up to 5,000 search results. Results beyond this limit can no longer be queried. If the search result volume is too large, recommend using more granular criteria to reduce the search results.</b>

        <br>Conditional filtering not recommended:
        - (Not recommended: use Names, NamePrefixes, or Descriptions instead) Specify single text Text for fuzzy search on media file name or description.
        -(Not recommended: use SourceTypes instead) Specify a single media file source SourceType for search.
        -(Not recommended: Use StreamIds instead) Specify a single push stream live code StreamId to search.
        -(Not recommended: use CreateTime as an alternative) Specify a single starting creation time StartTime to search.
        -(Not recommended: use CreateTime instead) Specify a single end time EndTime to search.

        :param request: Request instance for SearchMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.SearchMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SearchMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchMedia", params, headers=headers)
            response = json.loads(body)
            model = models.SearchMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchMediaBySemantics(self, request):
        r"""Use natural language to conduct semantic search on media.

        :param request: Request instance for SearchMediaBySemantics.
        :type request: :class:`tencentcloud.vod.v20180717.models.SearchMediaBySemanticsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SearchMediaBySemanticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchMediaBySemantics", params, headers=headers)
            response = json.loads(body)
            model = models.SearchMediaBySemanticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetCLSPushTarget(self, request):
        r"""Set a delivery destination in CLS for a vod domain.

        :param request: Request instance for SetCLSPushTarget.
        :type request: :class:`tencentcloud.vod.v20180717.models.SetCLSPushTargetRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SetCLSPushTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetCLSPushTarget", params, headers=headers)
            response = json.loads(body)
            model = models.SetCLSPushTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetDrmKeyProviderInfo(self, request):
        r"""Sets DRM key provider information.

        :param request: Request instance for SetDrmKeyProviderInfo.
        :type request: :class:`tencentcloud.vod.v20180717.models.SetDrmKeyProviderInfoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SetDrmKeyProviderInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetDrmKeyProviderInfo", params, headers=headers)
            response = json.loads(body)
            model = models.SetDrmKeyProviderInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetVodDomainCertificate(self, request):
        r"""Set the HTTPS certificate for a vod domain.

        :param request: Request instance for SetVodDomainCertificate.
        :type request: :class:`tencentcloud.vod.v20180717.models.SetVodDomainCertificateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SetVodDomainCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVodDomainCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.SetVodDomainCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SimpleHlsClip(self, request):
        r"""Crop HLS video by time period and generate a new HLS video in real time. Developers can share it immediately or save it for long-term preservation.

        Tencent Cloud VOD supports two editing modes:
        - Clip solidification: Save the edited video as a standalone video with an independent FileId; suitable for long-term preservation of highlights.
        - Editing is not solidified: The edited video is attached to the input file and has no standalone FileId. This is suitable for scenarios where highlight clips are shared temporarily.

        This API is used to crop an input m3u8 file. The minimum editing precision is one ts slice, so second-level or more precise editing precision cannot be achieved.

        ### Edit solidification
        Clip solidification refers to saving an edited video as an independent video with its own FileId. Its lifecycle is not subject to any impact from the original input video. Even if the original input video is deleted, the clipping result is not affected. You can also transcode it or publish it on WeChat.

        For example, a complete football match may have raw video lasting over 2 hours. For cost savings, a customer can store this video for 2 months, but specify longer storage for the edited highlights video. You can also perform additional on-demand operations on the highlights video separately, such as transcoding and publishing on WeChat. In this case, you can choose the edit and solidify solution.

        The advantage of solidified edits is that their lifecycle is independent of the original input video, allowing them to be managed separately and preserved long-term.

        <font color='red'>Note:</font> If solidification is specified when editing, enable reception of editing solidification event notifications through the ModifyEventConfig API. After successful solidification, you will receive a PersistenceComplete event notification. Before receiving this event notification, you should not delete or transition the original input video to colder storage. Otherwise, playback of the generated video may be abnormal.

        ### Editing is not solidified
        Editing is not solidified, meaning the result of editing (m3u8 file) shares the same TS segments with the original input video. The newly generated video is not a standalone complete video (no independent FileId, only a playback URL), and its valid period is consistent with that of the original input full video. Once the original input video is deleted, the clip will also become unplayable.

        Editing is not solidified. Since the clipping result is not an independent video, it is not included in the video management of on-demand media assets (for example, the total number of videos in the console does not count this clip). It is also unable to separately perform any video processing operations such as transcoding or WeChat publishing on this clip.

        The advantage of non-solidified editing is that the editing operation is Relatively "lightweight" and will not generate additional storage overhead. However, its shortcoming is that the lifecycle is identical to the original recorded video, and it is unable to further transcode or perform other video processing.

        :param request: Request instance for SimpleHlsClip.
        :type request: :class:`tencentcloud.vod.v20180717.models.SimpleHlsClipRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SimpleHlsClipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SimpleHlsClip", params, headers=headers)
            response = json.loads(body)
            model = models.SimpleHlsClipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SplitMedia(self, request):
        r"""This API is used to split an on-demand video into multiple new on-demand videos.

        :param request: Request instance for SplitMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.SplitMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SplitMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SplitMedia", params, headers=headers)
            response = json.loads(body)
            model = models.SplitMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartCDNDomain(self, request):
        r"""This API is used for enabling/disabling the CDN acceleration domain.

        :param request: Request instance for StartCDNDomain.
        :type request: :class:`tencentcloud.vod.v20180717.models.StartCDNDomainRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.StartCDNDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartCDNDomain", params, headers=headers)
            response = json.loads(body)
            model = models.StartCDNDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextToSpeechAsync(self, request):
        r"""Initiate a speech synthesis task to convert text into speech, oriented towards long text scenarios (maximum 200,000 characters), supporting specified timbre and synthesis parameters such as speaking rate, volume, pitch, sampling rate, and output format. Speech synthesis is an asynchronous task, and audio results are generated upon completion.

        :param request: Request instance for TextToSpeechAsync.
        :type request: :class:`tencentcloud.vod.v20180717.models.TextToSpeechAsyncRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.TextToSpeechAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextToSpeechAsync", params, headers=headers)
            response = json.loads(body)
            model = models.TextToSpeechAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextToSpeechSync(self, request):
        r"""Initiate a speech synthesis task to convert text into speech.

        :param request: Request instance for TextToSpeechSync.
        :type request: :class:`tencentcloud.vod.v20180717.models.TextToSpeechSyncRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.TextToSpeechSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextToSpeechSync", params, headers=headers)
            response = json.loads(body)
            model = models.TextToSpeechSyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAigcApiToken(self, request):
        r"""This API is used to create a Token for AIGC API calls. Data sync may delay after creation. It can be queried or deleted after about 30 seconds.

        :param request: Request instance for UpdateAigcApiToken.
        :type request: :class:`tencentcloud.vod.v20180717.models.UpdateAigcApiTokenRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.UpdateAigcApiTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAigcApiToken", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAigcApiTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateVoice(self, request):
        r"""This API is used to update the profile of a voice by voice ID, including its name, description, gender, age, language, tags, and scenarios, and returns the complete voice information after the update. Only voices under this account can be updated. System preset voices do not support update.

        Note: Newly designed or cloned voice types cannot be updated before activation. They are activated only after the newly created voice type is used for TTS once.

        :param request: Request instance for UpdateVoice.
        :type request: :class:`tencentcloud.vod.v20180717.models.UpdateVoiceRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.UpdateVoiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateVoice", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateVoiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyDomainRecord(self, request):
        r"""This API is used to verify domain name resolution values.

        :param request: Request instance for VerifyDomainRecord.
        :type request: :class:`tencentcloud.vod.v20180717.models.VerifyDomainRecordRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.VerifyDomainRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyDomainRecord", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyDomainRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))