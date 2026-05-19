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
        r"""* This API is used to apply for uploading a media file (and cover file) to VOD and obtain the metadata of file storage (including upload path and upload signature) for subsequent use by the uploading API.
        * For the detailed upload process, please see [Overview of Upload from Client](https://intl.cloud.tencent.com/document/product/266/9759?from_cn_redirect=1).

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
        r"""This API is used to associate/disassociate subtitles with/from a media file of a specific adaptive bitrate streaming template ID.

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


    def CommitUpload(self, request):
        r"""This API is used to confirm the result of uploading a media file (and cover file) to VOD, store the media information, and return the playback address and ID of the file.

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
        r"""This API is used to compose a media file. You can use it to do the following:

        1. **Rotation/Flipping**: Rotate a video or image by a specific angle or flip a video or image.
        2. **Audio control**: Increase/Lower the volume of an audio/video file or mute an audio/video file.
        3. **Overlaying**: Overlay videos/images in a specified sequence to achieve the picture-in-picture effect.
        4. **Audio mixing**: Mix the audios of audio/video files.
        5 **Audio extraction**: Extract audio from a video.
        6. **Clipping**: Clip segments from audio/video files according to a specified start and end time.
        7. **Splicing**: Splice videos/audios/images in a specified sequence.
        8. **Transition**: Add transition effects between video segments or images that are spliced together.

        The output file is in MP4 or MP3 format. In the callback for media composition, the event type is [ComposeMediaComplete](https://intl.cloud.tencent.com/document/product/266/43000?from_cn_redirect=1).

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
        r"""* After the `PullEvents` API is called to get an event, this API must be called to confirm that the message has been received;
        * After the event handler is obtained, the validity period of waiting for confirmation is 30 seconds. If the wait exceeds 30 seconds, a parameter error will be reported (4000);
        * For more information, please see the [reliable callback](https://intl.cloud.tencent.com/document/product/266/33779?from_cn_redirect=1#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83) of event notification.

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
        r"""Create a user-defined audio and video content analysis template. Maximum quantity: 50. HLS format not supported currently.

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
        r"""This API is used to create a custom video content recognition template. Up to 50 templates can be created.

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
        r"""This API is used to create an adaptive bitrate streaming template. Up to 100 templates can be created.

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
        r"""This API is used to create an advanced custom AIGC subject.

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
        r"""This API is used to create a Token for invoking AIGC API. After creation, there is a delay in data sync. It becomes queryable or deletable after about 30 seconds.

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
        r"""This API is used to create AIGC voice replication. Note that calling this API will incur fees. See the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).

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
        r"""Call this API to target a specified model and perform subject creation.

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
        r"""This API is used to create custom voice types for AIGC.

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


    def CreateAigcImageTask(self, request):
        r"""This API is used to generate AIGC images. The default limit is 1 concurrent processing. API calls will occur actual fee. Refer to the VOD AIGC image generation billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#9c4dc6ff-4b3f-4b25-bf2d-393889dfb9ac). The feature settlement mode is pay-as-you-go. Daily billing customers will be billed on the second day for usage on the day. Monthly billing customers will be billed on the 1st of the next month for usage in the previous month.

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


    def CreateAigcSubject(self, request):
        r"""This API is used to create AIGC custom subjects (Vidu). Note that calling this API may incur fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).

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
        r"""This API is used to generate AIGC videos. API calls will occur actual fee. Refer to the video-on-demand [AIGC video generation billing documentation](https://www.tencentcloud.com/zh/document/product/266/14666#96b3b59a-f9e1-49e9-966a-bedb70a4bf12). The feature settlement mode is [pay-as-you-go](https://www.tencentcloud.com/document/product/266/2838?from_cn_redirect=1). Daily billing customers will be charged on the second day for usage on the day, while monthly billing customers will be billed on the 1st of the next month for usage in the previous month.

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
        r"""This API is used to generate AIGC videos. The default limit is 1 concurrent processing. API calls will incur actual fees. Refer to the VOD AIGC video generation billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12). The feature settlement mode is pay-as-you-go. Daily billing customers will be charged on the second day for usage on the day, while monthly settlement customers will be billed on the 1st of the next month for usage in the previous month.

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
        r"""This API is used to create a custom animated image generating template. Up to 16 templates can be created.

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


    def CreateClass(self, request):
        r"""* This API is used to categorize media assets for management;
        * It does not affect the categories of existing media assets. If you want to modify the category of a media asset, call the [ModifyMediaInfo](https://intl.cloud.tencent.com/document/product/266/31762?from_cn_redirect=1) API.
        * There can be up to 4 levels of categories.
        * One category can have up to 500 subcategories under it.

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
        r"""Initiate complex adaptive bitstream processing. Features include:
        1. Output HLS and DASH adaptive bitrate streams based on the specified template.
        2. The content protection solution for adaptive bitrate streams is available in unencrypted, Widevine, or FairPlay.
        3. Support adding opening and ending segments.
        4. The output adaptive bitrate stream can include multilingual audio streams, each language comes from a different media file.
        5. The output adaptive bitrate stream can include multilingual subtitles.

        Notes:
        1. When using the opening scene, the video stream in the media needs to align with the audio stream, otherwise will cause out-of-sync audio and video in the output content;
        2. If the output adaptive bitrate stream needs to include the audio of the main media, then the FileId of the main media must be specified in the AudioSet parameter.
        3. To use subtitles, you must first add them to the main media. You can add subtitles through the ModifyMediaInfo API or the audio and video details page in the console.
        4. Not currently supported: top speed Codec, watermark.

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
        r"""We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [CreateReviewTemplate](https://intl.cloud.tencent.com/document/api/266/84391?from_cn_redirect=1).
        This API is used to create a custom audio/video moderation template. Up to 50 templates can be created in total.

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
        r"""This API is used for generating a subdomain resolution, prompting the customer to add it to the domain name resolution, used for wildcard domain and domain name retrieval verification of ownership.

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
        r"""Create enhance media template.

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
        -The maximum supported template quantity is 100.

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
        r"""This API is used to create a custom image processing template. A template can include at most 10 operations, for example, crop-scale-crop-blur-scale-crop-scale-crop-blur-scale. You can have up to 16 image processing templates.

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
        r"""This API is used to create a custom image sprite generating template. Up to 16 templates can be created.

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
        r"""Create Just In Time Transcode Template.

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


    def CreateLLMComprehendTemplate(self, request):
        r"""Create a large model comprehend template

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
        When creating a template, you need to fill in MPS-related parameters in JSON format into the MPSCreateTemplateParams parameter. For specific task parameter configuration methods, refer to the MPS task template related documentation.
        Currently supported MPS features: create custom template.
        1. [Audio and video enhancement](https://www.tencentcloud.com/document/product/862/118703?from_cn_redirect=1).
        2. [Media AI](https://www.tencentcloud.com/document/product/1041/54517)

        Task Template created by this method
        Template management is still done on the VOD platform.
        2. The feature is currently in closed beta testing. If needed, you can contact us for support.

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
        r"""This API is used to create samples for using facial features positioning and other technologies to perform video processing operations such as content recognition and inappropriate information recognition.

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
        r"""This API is used to create a custom task flow template. Up to 50 templates can be created.

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
        r"""Create a user-customized image processing template asynchronously. Maximum quantity: 50. HLS format not supported currently.

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
        r"""Creates media quality inspection template.

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
        r"""Create rebuild media template.

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
        r"""This API is used to create a custom moderation template. Up to 50 templates can be created in total.
        > The templates can only be used by the APIs [ReviewAudioVideo](https://intl.cloud.tencent.com/document/api/266/80283?from_cn_redirect=1) and [ReviewImage](https://intl.cloud.tencent.com/document/api/266/73217?from_cn_redirect=1).

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
        r"""This API is used to create a playlist. You can create at most 100 playlists.
        For each video on the list, you can either use the original file or a transcoding file.
        The files must be in HLS format. Preferably, they should have the same bitrate and resolution.

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
        r"""This API is used to create a custom sampled screencapturing template. Up to 16 templates can be created.

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
        r"""This API is used to generate scenario-based AIGC images. <b>This interface is in beta. If you need to use it, please contact us. API calls will incur actual fees.</b>

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
        r"""This API is used to generate scenario-based AIGC images. API calls will occur actual fee.

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
        r"""This API is used to create a custom time point screencapturing template. Up to 16 templates can be created.

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
          1. When you activate VOD, the system will enable storage for you in certain regions. If you need to store data in another region, you can use this API to enable storage in that region.
          2. You can use the `DescribeStorageRegions` API to query all supported storage regions and the regions you have storage access to currently.

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
        r"""This API is used to create a VOD subapplication.

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
        r"""We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to create a player configuration. Up to 100 configurations can be created.

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
        r"""This API is used to create a custom transcoding template. Up to 100 templates can be created.

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
        r"""This API is used to add an acceleration domain name to VOD. One user can add up to 20 domain names.
        1. After a domain name is added, VOD will deploy it, and it takes about 2 minutes for the domain name status to change from `Deploying` to `Online`.

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
        r"""This API is used to create a custom watermarking template. Up to 1,000 templates can be created.

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
        r"""This API is used to create keyword samples in batches for using OCR and ASR technologies to perform video processing operations such as content recognition and inappropriate information recognition.

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
        r"""This API is used to delete a custom video content analysis template.

        Note: templates with an ID below 10000 are preset and cannot be deleted.

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
        r"""This API is used to delete a custom video content recognition template.

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
        r"""This API is used to delete an adaptive bitrate streaming template.

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
        r"""This API is used to delete the senior custom AIGC subject.

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
        r"""Delete an AIGC API Token.

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


    def DeleteClass(self, request):
        r"""* A category can be deleted only if it has no subcategories and associated media files;
        * Otherwise, [delete the media files](https://intl.cloud.tencent.com/document/product/266/31764?from_cn_redirect=1) and subcategories first before deleting the category.

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
        r"""We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [DeleteReviewTemplate](https://intl.cloud.tencent.com/document/api/266/84390?from_cn_redirect=1).
        This API is used to delete a custom audio/video moderation template.

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
        r"""Delete Enhance Media template

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
        r"""Delete HeadTail Template

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
        r"""This API is used to delete an image processing template.

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
        r"""This API is used to delete an image sprite generating template.

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
        r"""Delete Just In Time Transcode Template.

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


    def DeleteLLMComprehendTemplate(self, request):
        r"""This API is used to delete a user's customized large model parsing template.

        Note: Template IDs below 10000 are system-preset templates and cannot be deleted.

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
        r"""* This API is used to delete a media file and its processed files, such as the transcoded video files, image sprites, screenshots, and videos for publishing on WeChat.
        * You can delete the original files, transcoded video files, and videos for publishing on WeChat, etc. of videos with specified IDs.
        * Note: after the original file of a video is deleted, you cannot transcode the video, publish it on WeChat, or perform other operations on it.

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
        r"""This API is used to delete samples according to sample IDs.

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
        r"""Delete user-created task flow templates.

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
        r"""This API is used to delete a user-customized image async processing template.

        Note: Template IDs below 10000 are system-preset templates and cannot be deleted.

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
        r"""Deletes media quality inspection template.

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
        r"""Delete rebuild media template.

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
        r"""This API is used to delete a custom moderation template.
        > The templates can only be used by the APIs [ReviewAudioVideo](https://intl.cloud.tencent.com/document/api/266/80283?from_cn_redirect=1) and [ReviewImage](https://intl.cloud.tencent.com/document/api/266/73217?from_cn_redirect=1).

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
        r"""This API is used to delete a playlist.

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
        r"""This API is used to delete a custom sampled screencapturing template.

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
        r"""This API is used to delete a custom time point screencapturing template.

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
        r"""We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to delete a player configuration.
        *Note: Preset player configurations cannot be deleted.*

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
        r"""This API is used to delete an acceleration domain name from VOD.
        1. Before deleting a domain name, disable its acceleration in all regions.

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


    def DeleteWatermarkTemplate(self, request):
        r"""This API is used to delete a custom watermarking template.

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
        r"""This API is used to get the list of video content analysis templates based on unique template ID. The returned result includes all eligible custom and [preset video content analysis templates](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.88.86.E6.9E.90.E6.A8.A1.E6.9D.BF).

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
        r"""This API is used to get the list of video content recognition templates based on unique template ID. The return result includes all eligible custom and [preset video content recognition templates](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E8.AF.86.E5.88.AB.E6.A8.A1.E6.9D.BF).

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
        r"""This API is used to query the list of transcoding to adaptive bitrate streaming templates and supports paged queries by filters.

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
        r"""This API is used to retrieve an advanced custom AIGC subject.

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
        r"""Query the AIGC API Token list. There is a delay in data sync after creation or deletion. The latest data is queryable after about 30 seconds.

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
        r"""This API is used to obtain AIGC face information. Note that calling this API will incur face recognition fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).

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


    def DescribeAigcUsageData(self, request):
        r"""This API is used to return statistical information of AIGC within a specified time range.
        1. AIGC stats from the last 365 days can be queried.
           2. The query time span should not exceed 90 days.
        3. If the query time span exceeds 1 day, return data with day-level granularity. Otherwise, return data with 5-minute granularity.

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
        r"""* This API is used to get the information of all categories.

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
        r"""This API is used to query the list of animated image generating templates and supports paged queries by filters.

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
        r"""Query user-customized digital watermark templates.

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
        r"""This API is used to query CDN bandwidth, traffic volume and stats of on-demand domain names.
        * The start time and end time of the query should not exceed a 90-day span.
        * You can query data from different service regions.
        Data support within the Chinese mainland allows querying stats by specified region and carrier.
        Playback statistics only target VOD domains (EdgeOne domain name distribution is not included).

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
        r"""This API is used to query traffic, bandwidth and stats of video-on-demand (VOD) CDN.
        1. The system side reserves CDN usage data for 13 months. You can query the most recent 365 days of usage data through the API. If needed, contact us to call historical usage data exceeding 365 days.
           2. The query time span should not exceed 90 days.
        3. You can specify the time granularity of usage data, which supports 5 minutes, 1 hour, and 1 day.
        4. Traffic volume is the total traffic within the query time granularity, and bandwidth is the peak bandwidth within the query time granularity.
        5. Playback statistics only target VOD domains (EdgeOne domain name distribution is not included).

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


    def DescribeCdnLogs(self, request):
        r"""Query the download URL of the access log for the CDN (exclude EdgeOne origin back to VOD domain) of the on-demand domain name.
        1. You can query the log download links for CDN in the most recent 30 days.
        2. By default, CDN creates a log file per hour. If no CDN access occurs in an hour, it does not generate a log file.
        3. The CDN log download link is with a validity of 24 hours.

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
        r"""This interface returns client upload acceleration statistics within the query time range.
         1. You can query the client upload acceleration statistics in the last 365 days.
         2. The query time span does not exceed 90 days.
         3. If the query time span exceeds 1 day, data with day granularity will be returned. Otherwise, data with 5-minute granularity will be returned.

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
        r"""We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [DescribeReviewTemplates](https://intl.cloud.tencent.com/document/api/266/84389?from_cn_redirect=1).
        This API is used to get the information of custom and [preset](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.AE.A1.E6.A0.B8.E6.A8.A1.E6.9D.BF) audio/video moderation templates based on template IDs.

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
        r"""Query current playlist of the round play.

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


    def DescribeDailyPlayStatFileList(self, request):
        r"""This API is used to query the download address of the playback statistics file.
        * You can query the download links for playback statistics from the past one year, with the time span between the start date and end date no more than 90 days.
        VOD analyzes and processes CDN request logs from the previous day to generate playback statistics files.
        The playback statistics file contains statistical information such as the number of plays and total traffic of media files.
        Play count statistics description:
        1. HLS file: Count playback times when accessing M3U8 files; do not count playback times when accessing TS files.
        2. Other files (such as MP4 files): The number of plays is not counted when the playback request has a range parameter and the start parameter is not equal to 0. In other cases, the number of plays is counted.
        * Playback device statistics: If a playback request includes the UserAgent parameter and the UserAgent contains identification such as Android or iPhone, it will be counted as mobile playback. Otherwise, it will be counted as PC playback.
        Playback statistics only target VOD domains (EdgeOne domain name distribution is not included).

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


    def DescribeDrmKeyProviderInfo(self, request):
        r"""This API is used to query DRM key information.

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
        r"""Describe Enhance Media Templates.

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
        r"""Tencent Cloud Video on Demand (VOD) provides customers with services such as media upload, media management, and media processing. During the execution process or when execution ends, VOD also offers various event notifications to help developers monitor service processing status and proceed with next business operations.

        Developers can use this interface to query the current configuration of event notification receiving method, recipient address and which events have enabled callback notification.

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
        r"""This API is used to get file attributes asynchronously.
        - Currently, this API can only get the MD5 hash of a file.
        - If the file queried is in HLS or DASH format, the attributes of the index file will be returned.

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
        r"""Describe HeadTail Templates.

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
        r"""This API is used to query image processing templates. You can specify the filters as well as the offset to start returning records from.

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
        r"""This interface returns the image review usage information used every day within the query time range.
           1. You can query the image review statistics for the last 365 days.
           2. The query time span does not exceed 90 days.
           3. If the query time span exceeds 1 day, data with a granularity of days will be returned. Otherwise, data with a granularity of 5 minutes will be returned.

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
        r"""This API is used to query the list of image sprite generating templates and supports paged queries by filters.

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
        r"""Describe Just In Time Transcode Templates.

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


    def DescribeLLMComprehendTemplates(self, request):
        r"""This API is used to obtain the template detail list based on the Template Unique Identifier of the large model comprehend template. The returned results include all eligible customized large model parsing templates.

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
        r"""This interface returns information about the number of license requests per day within the query time range.
           1. You can query the license request statistics in the last 365 days.
           2. The query time span does not exceed 90 days.
           3. If the query time span exceeds 1 day, data with a granularity of days will be returned. Otherwise, data with a granularity of 5 minutes will be returned.

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
        r"""Retrieve user-customized MPS task templates.
        When querying the template list, require MPS related parameters to be filled in MPSDescribeTemplateParams in JSON format. For task parameter configuration method, refer to MPS task template document description.

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
        r"""1. This API is used to get the information of multiple media files. Specifically, the information returned is as follows:
            1. `basicInfo`: Basic information including the file name, category, playback URL, and thumbnail.
            2. `metaData`: Metadata including the file size, duration, video stream information, and audio stream information.
            3. `transcodeInfo`: Transcoding information including the URLs, video stream parameters, and audio stream parameters of transcoding outputs.
            4. `animatedGraphicsInfo`: The information of the animated images (such as GIF images) generated.
            5. `sampleSnapshotInfo`: The information of the sampled screenshots generated.
            6. `imageSpriteInfo`: The information of the image sprites generated.
            7. `snapshotByTimeOffsetInfo`: The information of the time point screenshots generated.
            8. `keyFrameDescInfo`: The video timestamp information.
            9. `adaptiveDynamicStreamingInfo`: Adaptive bitrate information including the specifications, encryption type, and formats of the streams.
            10. `reviewInfo`: Moderation details for audio/video content and thumbnails.
        2. You can specify what information to return.

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
        r"""This API is used to query playback statistics of media files by specified time granularity.
        * Playback statistics from the past one year can be queried.
        * The time granularity is hourly, and the span between end time and start time cannot exceed 7 days.
        * The time granularity is day, and the span between the end time and start time is up to 90 days.
        Playback statistics only target VOD domains (EdgeOne domain name distribution is not included).

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
        1. The data system reserves video processing usage for 13 months. You can use the interface to query the most recent 365 days of usage data. If needed, contact us to call historical usage data exceeding 365 days.
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
        r"""This API is used to query the information of samples and supports paginated queries by sample ID, name, and tag.

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
        r"""This API is used to get the list of task flow template details by task flow template name.

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
        r"""This API is used to obtain the template details list of image asynchronous processing based on the Template Unique Identifier. The returned results include ALL eligible user-customized image asynchronous processing templates.

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
        r"""Get media quality inspection Template List.

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
        r"""Describe Rebuild Media Templates

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
        r"""<b>This API is disused and replaced by [DescribeMediaProcessUsageData](https://intl.cloud.tencent.com/document/product/266/41464?from_cn_redirect=1).</b>

        This API returns the video content duration for intelligent recognition in seconds per day within the queried period.

        1. The API is used to query statistics on the video content duration for intelligent recognition in the last 365 days.
        2. The query period is up to 90 days.

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
        r"""This API is used to get the information of moderation templates.
        > The templates can only be used by the APIs [ReviewAudioVideo](https://intl.cloud.tencent.com/document/api/266/80283?from_cn_redirect=1) and [ReviewImage](https://intl.cloud.tencent.com/document/api/266/73217?from_cn_redirect=1).

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
        r"""This API is used to query playlists.

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
        r"""This API is used to query the list of sampled screencapturing templates and supports paged queries by filters.

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
        r"""This API is used to query the list of time point screencapturing templates and supports paged queries by filters.

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
        r"""This API is used to query the storage capacity usage and number of files.

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
        r"""This API is used to query the VOD storage space used within a specified time range. The measurement unit is byte.
        1. The system side reserves storage usage data for 13 months. You can be queried usage data within the most recent 365 days through the API. If needed to call historical usage data exceeding 365 days, contact us.
        2. The query time span should not exceed 90 days.
        3. The query span at a minute granularity should not exceed 7 days.

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
        r"""This API is used to query the following information:
          1. All supported storage regions.
          2. The regions you have storage access to currently.
          3. The default storage region.

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
        r"""This API is used to query the list of the primary application and subapplications of the current account.

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
        r"""We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to query player configurations. It supports pagination.

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
        r"""This API is used to query the details of execution status and result of a task submitted in the last 3 days by task ID.

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
        r"""* This API is used to query the task list;
        * If there are many data entries in the list, one single call of the API may not be able to pull the entire list. The `ScrollToken` parameter can be used to pull the list in batches;
        * Only tasks in the last three days (72 hours) can be queried.

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
        r"""This API is used to get the list of transcoding templates based on unique template ID. The return result includes all eligible custom and [preset transcoding templates](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF).

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
        r"""This API is used to query the list of VOD domain names.

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


    def DescribeWatermarkTemplates(self, request):
        r"""This API is used to query custom watermarking templates and supports paged queries by filters.

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
        r"""This API is used to perform paginated queries of keyword sample information by use case, keyword, and tag.

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


    def EditMedia(self, request):
        r"""Edit the video (cut, splice, etc.) to generate a new video. The editing functions include:

        1. Edit a file in the VOD video to generate a new video;
        2. Splice multiple files to generate a new video;
        3. Edit multiple files and then splice them to generate a new video;
        4. Directly generate a new video for a stream;
        5. Edit a stream to generate a new video. Video;
        6. Splice multiple streams to generate a new video;
        7. Clip and then splice multiple streams to generate a new video.

        For the generated new video, you can also specify whether the generated video needs to execute the task flow.

        >When editing or splicing live streams, please make sure to do so after the stream is over. Otherwise the resulting video may be incomplete.

        If event notification is used, the type of event notification is [Video editing completed](https://intl.cloud.tencent.com/document/product/266/33794?from_cn_redirect=1).

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
        r"""Enhance Media By Template.

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
        r"""Initiate a Remaster task for audio and video media in VOD

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
        r"""This API is only used in special scenarios of custom development. Unless requested by VOD customer service, please do not call it.

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
        r"""If you need source tracing for piracy, refer to ghost watermark (https://www.tencentcloud.com/document/product/266/94228?from_cn_redirect=1).

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
        r"""If you need source tracing for piracy, ghost watermark (https://www.tencentcloud.com/document/product/266/94228?from_cn_redirect=1) is recommended.

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
        r"""This API is used to implement quick splice and quick editing for HLS videos in VOD, generating new media in HLS format.

        Quickly splice or edit the generated video to generate a new FileId and perform solidification. After successful solidification, the new video file exists independent of the original input video and is not impacted by the deletion of the original video.

        <font color='red'>Note:</font> Enable reception of editing solidification event notifications through the ModifyEventConfig API. After successful solidification, you will receive an event notification of PersistenceComplete type. Before receiving this event notification, you should not perform operations such as delete or downgrade on the original input video, otherwise exceptions may occur during playback of the generated video from splicing and clipping.

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
        r"""After media blocking is enabled, all URLs for accessing various resources (raw file, transcoding output file, screenshot, etc.) will return 403 except for vod console preview.
        The unblock operation takes effect across the entire network in approximately 5-10 minutes.
        * Note: Banned media can only operate standard storage and infrequent storage media. Infrequent storage media must be stored for at least 30 days. Early deletion or changing the storage class will still be billed for 30 days. If infrequent storage media is banned and its infrequent access storage period is less than 30 days, early deletion billing will occur. Meanwhile, the infrequent access storage duration of the banned media will restart from the current system time. If the media is deleted or its storage class is changed within 30 days, early deletion billing will also occur. For example: Media 001 has been in infrequent storage for 10 days. At this point, if 001 is banned, the infrequent storage billing will still be calculated for 30 days (early deletion billing duration is 30 - 10 = 20 days). After the ban, the infrequent access storage duration of 001 restarts. If 001 is deleted on the 5th day after the ban, the infrequent storage billing will also be calculated for 30 days (early deletion billing duration is 30 - 5 = 25 days). The actual infrequent access storage duration of 001 is 10 + 5 = 15 days, while the infrequent storage billing duration is 10 + 20 (early deletion billing) + 5 + 25 (early deletion billing) = 60 days.

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
        r"""Operate the current play list . Supported operations include:<li> Insert: Insert a playing program into the current playlist.</li><li> Delete: Remove a playing program from the playlist.</li>

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
        r"""This API is used to import AI analysis results into the knowledge base.

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
        r"""Initiate media quality inspection task.

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
        r"""This API is used to list stored file entries under a sub-app.

        This API is available only in "FileID+Path mode".

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
        r"""Live stream clipping refers to the process where, during a live stream (not yet ended), customers can select a segment from past live stream content to generate a new video (HLS format) in real time. Developers can instantly share it or preserve it for long-term storage.

        Tencent Cloud Video on Demand (VOD) supports two instant editing modes:
        - Clip Curing: Save the edited video as an independent video with an independent FileId; applicable to scenes where highlights are ** saved for a long time **;
        - Clip not cured: The resulting video clip is attached to the live recording file and has no separate FileId; applicable to scenes where highlights are ** temporarily shared **.

        Note:
        -Using the live stream clipping functionality is the premise for the target live stream to enable the [time-shifted playback feature](https://www.tencentcloud.com/document/product/267/57281).
        -Live stream clipping is performed based on the m3u8 file generated by live recording generation, so its minimum editing precision is a ts slice, and second-level or more precise editing precision cannot be achieved.
        -Since there may be stream interruptions during live streaming, the actual video duration generated by editing might differ from the expected duration. For example, if a live stream is edited for the time interval from 2018-09-20T10:30:00Z to 2018-09-20T10:40:00Z and stream interruption occurred during this interval, the duration of the returned media asset files will be less than 10 minutes. In such cases, you can perceive this through the output parameter <a href="#p_segmentset">SegmentSet</a>.

        ### Edit solidification
        Clipping persistence means saving the edited video as an independent video (with an independent FileId). Its lifecycle is not subject to the original live recorded video (even if the original recorded video is deleted, the clipping result will not be impacted). It can also be post-processed, such as transcoding or publishing on WeChat.

        For example: A complete football match may last for over 2 hr, and the customer can store the original video for 2 months to save costs. However, for the highlight reel from live stream clipping, you can specify longer storage. You can also perform additional on-demand operations like transcoding and publishing on WeChat separately for the highlight reel. In this case, choose the live stream clipping and solidification solution.

        The advantage of edit solidification is that its lifecycle is independent of the original recorded video, allowing separate management and long-term preservation.

        <font color='red'>Note:</font> If you specify solidification when editing, enable reception of editing solidification event notifications through the ModifyEventConfig API. After successful solidification, you will receive a PersistenceComplete event notification. Upon receiving this event notification, you should not perform operations like deletion or cooling on the live video recording, otherwise exceptions may occur during playback of the generated video.

        ### Editing is not solidified
        Non-solidified editing means the resulting m3u8 file shares the same TS segments with the live video recording. The generated video is not an independent and complete video (it has no standalone FileId, only a playback URL), and its valid period is consistent with the full video of the live recording. Once the live recording is deleted, it will lead to the video clip being unplayable.

        Editing is not solidified. Since the clipping result is not an independent video, it will not be included in video management of on-demand media assets (for example, the total number of videos in the console will not count this video clip). It is also unable to perform any video processing operations such as transcoding or publishing on WeChat targeting this video clip separately.

        The advantage of not curing clips is that they are "lightweight" and do not incur additional storage overhead. However, its shortcomings are that its life cycle is the same as that of the original recorded video, and it is impossible to further transcode and other Media Processing Service.

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
        r"""This API is used to manage initiated tasks.

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
        r"""This API is used to modify a custom video content analysis template.

        Note: templates with an ID below 10000 are preset and cannot be modified.

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
        r"""This API is used to modify a custom video content recognition template.

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
        r"""This API is used to modify an adaptive bitrate streaming template.

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


    def ModifyAnimatedGraphicsTemplate(self, request):
        r"""This API is used to modify a custom animated image generating template.

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
        r"""This API is used to modify the category of a media file.

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
        r"""We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [ModifyReviewTemplate](https://intl.cloud.tencent.com/document/api/266/84388?from_cn_redirect=1).
        This API is used to modify a custom audio/video moderation template.

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


    def ModifyDefaultStorageRegion(self, request):
        r"""This API is used to set the default storage region. A file will be stored in the default region if no region is specified for file upload.

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
        r"""Modify enhance media template.

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
        r"""Tencent Cloud VOD provides customers with media upload, media management, media processing and other services. During or at the end of the execution of these services, Tencent Cloud On-Demand also provides various corresponding event notifications to facilitate developers to perceive the service processing status and Do the next business operation.

        Developers can achieve this by calling this interface:
        - Set the type of callback notification received. Currently, there is [HTTP callback notification](https://www.tencentcloud.com/document/product/266/33948) and [reliable notification based on message queue](https://www.tencentcloud.com/document/product/266/33948) two types.
        - For [HTTP callback notification](https://www.tencentcloud.com/document/product/266/33948), you can set the address of the 3.0 format callback. For the description of 3.0 format callback, see [Historical Format Callback](https://intl.cloud.tencent.com/document/product/266/33796?from_cn_redirect=1).
        - Select settings to receive or ignore notification events for specific event services.

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
        r"""Modify HeadTail Template.

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
        r"""This API is used to modify a custom image sprite generating template.

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
        r"""Modify Just In Time Transcode Template.

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


    def ModifyLLMComprehendTemplate(self, request):
        r"""Modify the parsing template of a large model

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
        When modifying a template, require filling in MPS related parameters in JSON format into the MPSModifyTemplateParams parameter. For specific task parameter configuration methods, refer to the MPS task template document description.

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
        r"""This API is used to modify the attributes of a media file, including category, name, description, tag, expiration time, timestamp information, video thumbnail, and subtitle information.

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
        r"""This API is used to modify the storage class of media files.
        If the current storage class is STANDARD, it can be changed to one of the following classes:
        <li>STANDARD_IA</li>
        <li>ARCHIVE</li>
        <li>DEEP ARCHIVE</li>
        If the current storage class is STANDARD_IA, it can be changed to one of the following classes:
        <li>STANDARD</li>
        <li>ARCHIVE</li>
        <li>DEEP ARCHIVE</li>
        If the current storage class is ARCHIVE, it can be changed to the following class:
        <li>STANDARD</li>
        If the current storage class is DEEP ARCHIVE, it can be changed to the following class:
        <li>STANDARD</li>

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
        r"""This API is used to modify sample information according to the sample ID. You can modify the name and description, add, delete, and reset facial features or tags. Leave at least one image after deleting facial features. To leave no image, please use the reset operation.

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
        r"""This API is used to modify a user-customized image asynchronous processing template.

        Note: Template IDs below 10000 are system-preset templates and not allowed to be modified.

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
        r"""Modifies media quality inspection template.

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
        r"""Modify Rebuild Media Template.

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
        r"""This API is used to modify a custom moderation template.
        > The templates can only be used by the APIs [ReviewAudioVideo](https://intl.cloud.tencent.com/document/api/266/80283?from_cn_redirect=1) and [ReviewImage](https://intl.cloud.tencent.com/document/api/266/73217?from_cn_redirect=1).

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
        r"""This API is used to modify a playlist.
        The modification will only take effect for new playback requests. For ongoing playback, the old playlist will be playable for seven days after the modification.

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
        r"""This API is used to modify a custom sampled screencapturing template.

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
        r"""This API is used to modify a custom time point screencapturing template.

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
        r"""This API is used to modify subapplication information, but it is not allowed to modify primary application information.

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
        r"""This API is used to enable/disable a subapplication. After a subapplication is disabled, its corresponding domain name will be blocked and its access to the console will be restricted.

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
        r"""We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to modify a player configuration.

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
        r"""This API is used to modify a custom transcoding template.

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
        r"""This API is used to modify the acceleration region of a domain name on VOD.
        1. You can modify acceleration regions of only domain names whose status is `Online`.

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
        r"""This API is used to modify domain name settings, such as the hotlink protection configuration.
        1. You can modify settings of only domain names whose status is `Online`.

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
        r"""This API is used to modify a custom watermarking template. The watermark type cannot be modified.

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
        r"""This API is used to modify the use case and tag of a keyword. The keyword itself cannot be modified, but you can delete it and create another one if needed.

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
        r"""This API is used to parse the index file content and return the list of segment files to be uploaded when an HLS video is uploaded. A segment file path must be a relative path of the current directory or subdirectory instead of a URL or absolute path.

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
        r"""This API is used to process images.

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
        r"""This API is used to initiate processing tasks for audio-video media in on-demand video, with features including:
        1. Video transcoding (watermarked);
        2. Video-to-GIF.
        3. Screenshot taking at specified time points;
        4. Sampled screenshot taking;
        5. Capture CSS sprites from video.
        6. Capture a cover image from the video.
        7. Transcoding to adaptive bitrate streaming (and encrypting);
        8. Content review (offensive content, unsafe information, inappropriate information). <font color=red>Not recommended</font> to use this API for initiation. Recommended for use: [Audio-Video Moderation (ReviewAudioVideo)](https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) or [Image Moderation (ReviewImage)](https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1).
        9. Content analysis (tag, category, cover, frame tagging), HLS format not supported currently;
        10. Content recognition (video intro and outro, human face, full text, text keyword, full speech, speech keyword, object).

        If you use event notification, the event notification type is task flow status change (https://www.tencentcloud.com/document/product/266/9636?from_cn_redirect=1).

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
        r"""Use the media processing capability of the media processing service to trigger media processing for on-demand video.

        Video processing tasks initiated by this method:
        Querying the status of tasks and results is still done on the VOD platform. Use [DescribeTaskDetail](https://www.tencentcloud.com/document/product/266/33431?from_cn_redirect=1) or [DescribeTasks](https://www.tencentcloud.com/document/product/266/33430?from_cn_redirect=1) to query tasks.
        2. The amount and bills of related features will be provided on the MPS platform. Before using this feature, start by enabling the Media Processing Service (MPS) in the console. For the activation method, refer to the preliminary operations in the integration guide.

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
        r"""This API is used to start a task flow on a video.
        There are two ways to create a task flow template:
        1. Create and modify a task flow template in the console;
        2. Create a task flow template using the `CreateProcedureTemplate` API.

        If event notifications are used, the event type for moderation tasks is [ReviewAudioVideoComplete](https://intl.cloud.tencent.com/document/product/266/81258?from_cn_redirect=1), and that for other tasks is [ProcedureStateChanged](https://intl.cloud.tencent.com/document/product/266/9636?from_cn_redirect=1).

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
        r"""This API is <font color='red'>disused</font>, please use [ProcessMedia](https://intl.cloud.tencent.com/document/product/862/37578?from_cn_redirect=1) API of MPS, with the input parameter `InputInfo.UrlInputInfo.Url` set to a video URL.

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
        r"""* This API is used to get event notifications from the business server through [reliable callback](https://intl.cloud.tencent.com/document/product/266/33948).
        * The API gets event data through long polling. That is, if there is any unconsumed event on the server, the event notification will be returned to the requester immediately. If there is no unconsumed event on the server, the request will be suspended in the backend until a new event is generated.
        * The request can be suspended for up to 5 seconds. It's recommended to set the request timeout period to 10 seconds.
        * Event notifications not pulled will be retained for up to 4 days and may be cleared after this period.
        * After the API returns an event, the caller must call the [ConfirmEvents](https://intl.cloud.tencent.com/document/product/266/34184) API within <font color="red">30 seconds</font> to confirm that the event notification has been processed. Otherwise, the event notification will be pulled again after <font color="red">30 seconds</font>.
        * This API can get up to 16 event notifications at a time.

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
        r"""This API is used to pull a video on the internet to the VOD platform.

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
        r"""1. This API is used to prefetch a list of specified URLs.
        2. The URL domain names must have already been registered with VOD.
        3. Up to 20 URLs can be specified in one request.
        4. By default, the maximum number of URLs that can be refreshed per day is 10,000.

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
        r"""Initiate rebuild media

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
        r"""Rebuild media by template.

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
        r"""1. This API is used to purge URLs.
        2. The URL domain names must have already been registered with VOD.
        3. Up to 20 URLs can be specified in one request.
        4. By default, the maximum number of URLs allowed for purge per day is 100,000.

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
        r"""This API is used to remove watermarks from a video.

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
        r"""This API is used to modify a custom task flow template.

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
        r"""This API is used to restore files from ARCHIVE or DEEP ARCHIVE. Files stored in ARCHIVE or DEEP ARCHIVE must be restored before they can be accessed. Restored files are available for a limited period of time.

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
        r"""This API is used to start a moderation task on a file stored in VOD to detect non-compliant content in images, text, speech, and voice.

        If event notifications are used, the event type is [ReviewAudioVideoComplete](https://intl.cloud.tencent.com/document/product/266/81258?from_cn_redirect=1).

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
        r"""This API is used to moderate an image stored in VOD (detect pornographic and terrorist content).><li>The image file must be smaller than 5 MB.</li> ><li>To ensure the accuracy of moderation results, the image resolution must be higher than 256 x 256 px.</li> ><li>The format must be PNG, JPG, JPEG, BMP, GIF, or WEBP.</li>

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
        r"""Search media information, support multiple conditions filter criteria, and sort returned results, filter, and other features. This includes:
        -Specify the file id collection FileIds, return media that matches any ID in the collection.
        -Do fuzzy search based on multiple media file Names or Descriptions.
        -Search for multiple filename prefixes NamePrefixes.
        -Specify the category collection ClassIds (see input parameter), and media that meets any category in the collection will be returned. For example: media categories include movie, TV series, variety shows, among which movie has subcategories such as historical film, action film, romance film. If ClassIds specifies movie, TV series, then all subcategories under movie and TV series will be returned. If ClassIds specifies historical film, action film, then only media under these 2 subcategories will be returned.
        -Specify the tag collection Tags (see input parameter), return media that meets any tag in the collection. For example: if a media has tags like ACG, palace drama, or parody remix, and Tags specifies ACG and parody remix, then any media that complies with any one of these two tags will be retrieved.
        -Specify the file type set Categories (see input parameter), and return media that meets any type in the collection. For example: file types include Video, Audio, and Image. If Categories specifies Video and Audio, then media compliant with these types will be retrieved.
        -Specify the source collection SourceTypes (see input parameter), return media that meets any source in the collection. For example: media sources include Record (live recording service) and Upload. If SourceTypes specifies Record and Upload, media that complies with these sources will be retrieved.
        -Specify the file packaging format set MediaTypes (see input parameter), return media that meets any muxing format in the collection. For example: muxing formats include MP4, AVI, MP3. If MediaTypes specifies MP4 and MP3, then media that complies with these muxing formats will be retrieved.
        -Specify the file status collection Status (see input parameter), return media that meets any status in the collection. For example: file status includes Normal, SystemForbidden (Platform Ban), Forbidden (Proactive Ban). If Status specifies Normal and Forbidden, media that complies with these states will be retrieved.
        -Specify the file review result set ReviewResults (see input parameter), return media that meets any status in the collection. For example: file review results include pass and block. If ReviewResults specifies pass and block, media that complies with these review results will be retrieved.
        -Specify the collection of live streaming codes StreamIds (see input parameter) to filter media for live recording.
        -Filter media by creation time range of specified media.
        -Specify TRTC application ID collection to filter media.
        -Specify TRTC room ID collection to filter media.

        -The above parameters can be combined in any combination for search. For example: filter media with creation time between 2018-12-01 12:00:00 and 2018-12-08 12:00:00, categorized as movie or TV series, and tagged with palace intrigue and suspense. Note that for any parameter supporting array input, the search logic between its elements is 'OR'. The logical relationship between ALL parameters is 'AND'.

        -Allow passage through Filters to control the type of media information returned (default return all information). Selectable inputs include:
        1. Basic information (basicInfo): media name, category, playback address, cover image.
        2. Meta information (metaData): include size, duration, video stream information, audio stream information.
        3. Transcoding result information (transcodeInfo): includes generated media addresses, video stream parameters, audio stream parameters for different specifications.
        4. Animated graphics info (animatedGraphicsInfo): The info of animated graphics after video-to-gif conversion, such as gif.
        5. Sampled screenshot information (sampleSnapshotInfo): Screenshot information after sampling screenshot taking.
        6. Sprite image information (imageSpriteInfo): The sprite image information of the captured sprite image file from the video.
        7. Screenshot information at the specified time point (snapshotByTimeOffsetInfo): This API is used to obtain screenshot information after capturing snapshots at specified time points.
        8. Video timestamp information (keyFrameDescInfo): The dotting information for video setting.
        9. Adaptive Bitrate Streaming information (adaptiveDynamicStreamingInfo): including specification, encryption type, packaging format and other related information.

        -Allow sorting the results by creation time and return in pages, using Offset and Limit (see input parameter) to control pagination.

        <div id="maxResultsDesc">API return result count limit:</div>

        -<b>Both <a href="#p_offset">Offset</a> and <a href="#p_limit">Limit</a> parameters impact the number of pagination query results. Special attention: by default, this interface only returns up to 10 query results when both values are not specified.</b>
        -<b>The maximum number of search results supported is 5000. Excess results are no longer supported for querying. If the search result volume is too large, recommend using more granular criteria to reduce the results.</b>

        Conditional filtering not recommend
        -(Not recommended: Use Names, NamePrefixes, or Descriptions as alternatives) Specify single text Text to do fuzzy search on media file name or description.
        -(Not recommended: Use SourceTypes as an alternative) Search for one media file source by specifying SourceType.
        -(Not recommended: Use StreamIds as an alternative) Specify single push stream live code StreamId to search for.
        -(Not recommended: Use CreateTime instead) Specify single start creation time StartTime to search.
        -(Not recommended: Use CreateTime as alternative) Specify single ending creation time EndTime to search.

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
        r"""This API is used to conduct semantic search on media using natural language.

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


    def SetDrmKeyProviderInfo(self, request):
        r"""This API is used to configure DRM key information.

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
        r"""Set Vod Domain Certificate.

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
        r"""This API is used to crop an HLS video by time period and generate a new real-time HLS video. Developers can share it immediately or preserve it for long-term.

        Tencent Cloud Video on Demand (VOD) supports two editing modes:
        -Edit and save: Save the edited video as an independent video with a standalone FileId. Suitable for scenarios requiring long-term preservation of highlight clips.
        -Editing is not solidified: The video obtained by editing is attached to the input file with no standalone FileId. It is suitable for scenarios where highlight clips are temporarily shared.

        This API is used to crop based on input m3u8 files, with a minimum editing precision of a ts slice. Second-level or more precise editing precision cannot be achieved.

        ### Edit solidification
        Video clipping persistence refers to saving an edited video as an independent video (with an independent FileId). Its lifecycle is not subject to the original input video (even if the original input video is deleted, the clipping result will not have any impact). It can also be post-processed, such as transcoding or publishing on WeChat.

        For example, a complete football match may last for over 2 hours. To save costs, the customer can store the original video for 2 months, but may choose to store the highlight reel for longer. You can also transcode the highlight reel, publish it on WeChat, and perform additional on-demand operations. In this case, you can choose the edit and save solution.

        The advantage of edit is that its lifecycle is independent of the original input video, allowing separate management and long-term preservation.

        <font color='red'>Note:</font> If you specify solidification when editing, enable reception of editing solidification event notifications via the ModifyEventConfig API. After successful solidification, you will receive a PersistenceComplete event notification. Before receiving this event notification, you should not delete or downgrade the original input video, otherwise exceptions may occur during playback of the generated video.

        ### Editing is not solidified
        Non-solidified editing means the result of editing (m3u8 file) shares the same TS segments with the original input video. The generated video is not an independent and complete video (it has no standalone FileId, only a playback URL), and its valid period is consistent with that of the original input full video. Once the original input video is deleted, it will lead to the video clip being unable to play.

        Editing is not solidified. Since the clipping result is not an independent video, it will not be included in video management of on-demand media assets (for example, the total number of videos in the console will not count this video clip) and cannot be targeted for any video processing operations such as transcoding or publishing on WeChat.

        The advantage of editing not being solidified is that the editing operation is relatively lightweight and will not generate additional storage overhead. However, the shortcoming is that its lifecycle is the same as the original recorded video, and it is unable to further transcode or perform video processing.

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
        r"""Split the video into strips to generate multiple new videos.

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


    def VerifyDomainRecord(self, request):
        r"""This API is used to verify the domain name resolution value.

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