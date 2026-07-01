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
from tencentcloud.vod.v20180717 import models
from typing import Dict


class VodClient(AbstractClient):
    _apiVersion = '2018-07-17'
    _endpoint = 'vod.intl.tencentcloudapi.com'
    _service = 'vod'

    async def ApplyUpload(
            self,
            request: models.ApplyUploadRequest,
            opts: Dict = None,
    ) -> models.ApplyUploadResponse:
        """
        * This API is used to apply for uploading a media file (and cover file) to VOD and obtain the metadata of file storage (including upload path and upload signature) for subsequent use by the uploading API.
        * For the detailed upload process, please see [Overview of Upload from Client](https://intl.cloud.tencent.com/document/product/266/9759?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachMediaSubtitles(
            self,
            request: models.AttachMediaSubtitlesRequest,
            opts: Dict = None,
    ) -> models.AttachMediaSubtitlesResponse:
        """
        This API is used to associate/disassociate subtitles with/from a media file of a specific adaptive bitrate streaming template ID.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachMediaSubtitles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachMediaSubtitlesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneCDNDomain(
            self,
            request: models.CloneCDNDomainRequest,
            opts: Dict = None,
    ) -> models.CloneCDNDomainResponse:
        """
        Clone CDN Domain.
        """
        
        kwargs = {}
        kwargs["action"] = "CloneCDNDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneCDNDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitUpload(
            self,
            request: models.CommitUploadRequest,
            opts: Dict = None,
    ) -> models.CommitUploadResponse:
        """
        This API is used to confirm the result of uploading a media file (and cover file) to VOD, store the media information, and return the playback address and ID of the file.
        """
        
        kwargs = {}
        kwargs["action"] = "CommitUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommitUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ComposeMedia(
            self,
            request: models.ComposeMediaRequest,
            opts: Dict = None,
    ) -> models.ComposeMediaResponse:
        """
        This API is used to compose a media file. You can use it to do the following:

        1. **Rotation/Flipping**: Rotate a video or image by a specific angle or flip a video or image.
        2. **Audio control**: Increase/Lower the volume of an audio/video file or mute an audio/video file.
        3. **Overlaying**: Overlay videos/images in a specified sequence to achieve the picture-in-picture effect.
        4. **Audio mixing**: Mix the audios of audio/video files.
        5 **Audio extraction**: Extract audio from a video.
        6. **Clipping**: Clip segments from audio/video files according to a specified start and end time.
        7. **Splicing**: Splice videos/audios/images in a specified sequence.
        8. **Transition**: Add transition effects between video segments or images that are spliced together.

        The output file is in MP4 or MP3 format. In the callback for media composition, the event type is [ComposeMediaComplete](https://intl.cloud.tencent.com/document/product/266/43000?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ComposeMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ComposeMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfirmEvents(
            self,
            request: models.ConfirmEventsRequest,
            opts: Dict = None,
    ) -> models.ConfirmEventsResponse:
        """
        * After the `PullEvents` API is called to get an event, this API must be called to confirm that the message has been received;
        * After the event handler is obtained, the validity period of waiting for confirmation is 30 seconds. If the wait exceeds 30 seconds, a parameter error will be reported (4000);
        * For more information, please see the [reliable callback](https://intl.cloud.tencent.com/document/product/266/33779?from_cn_redirect=1#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83) of event notification.
        """
        
        kwargs = {}
        kwargs["action"] = "ConfirmEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfirmEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIAnalysisTemplate(
            self,
            request: models.CreateAIAnalysisTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAIAnalysisTemplateResponse:
        """
        Create a user-defined audio and video content analysis template. Maximum quantity: 50. HLS format not supported currently.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIAnalysisTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIAnalysisTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIRecognitionTemplate(
            self,
            request: models.CreateAIRecognitionTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAIRecognitionTemplateResponse:
        """
        This API is used to create a custom video content recognition template. Up to 50 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIRecognitionTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIRecognitionTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAdaptiveDynamicStreamingTemplate(
            self,
            request: models.CreateAdaptiveDynamicStreamingTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAdaptiveDynamicStreamingTemplateResponse:
        """
        This API is used to create an adaptive bitrate streaming template. Up to 100 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAdaptiveDynamicStreamingTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAdaptiveDynamicStreamingTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcAdvancedCustomElement(
            self,
            request: models.CreateAigcAdvancedCustomElementRequest,
            opts: Dict = None,
    ) -> models.CreateAigcAdvancedCustomElementResponse:
        """
        This API is used to create an advanced custom AIGC subject.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcAdvancedCustomElement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcAdvancedCustomElementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcApiToken(
            self,
            request: models.CreateAigcApiTokenRequest,
            opts: Dict = None,
    ) -> models.CreateAigcApiTokenResponse:
        """
        This API is used to create a Token for invoking AIGC API. After creation, there is a delay in data sync. It becomes queryable or deletable after about 30 seconds.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcApiToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcApiTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcAudioClone(
            self,
            request: models.CreateAigcAudioCloneRequest,
            opts: Dict = None,
    ) -> models.CreateAigcAudioCloneResponse:
        """
        This API is used to create AIGC voice replication. Note that calling this API will incur fees. See the [billing documentation](https://intl.cloud.tencent.com/document/product/266/14666#87e472ca-9c95-4658-ab7b-8f2130608419).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcAudioClone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcAudioCloneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcAudioTask(
            self,
            request: models.CreateAigcAudioTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAigcAudioTaskResponse:
        """
        This API is used to create AI audio generation tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcAudioTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcAudioTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcCustomElement(
            self,
            request: models.CreateAigcCustomElementRequest,
            opts: Dict = None,
    ) -> models.CreateAigcCustomElementResponse:
        """
        Call this API to target a specified model and perform subject creation.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcCustomElement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcCustomElementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcCustomVoice(
            self,
            request: models.CreateAigcCustomVoiceRequest,
            opts: Dict = None,
    ) -> models.CreateAigcCustomVoiceResponse:
        """
        This API is used to create custom voice types. Note that calling this API will incur customization fees. See the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#5e5217e8-29fc-467e-ac2d-853648f988b7).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcCustomVoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcCustomVoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcImageTask(
            self,
            request: models.CreateAigcImageTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAigcImageTaskResponse:
        """
        This API is used to generate AIGC images. The default limit is 1 concurrent processing. API calls will occur actual fee. Refer to the VOD AIGC image generation billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#9c4dc6ff-4b3f-4b25-bf2d-393889dfb9ac). The feature settlement mode is pay-as-you-go. Daily billing customers will be billed on the second day for usage on the day. Monthly billing customers will be billed on the 1st of the next month for usage in the previous month.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcImageTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcImageTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcQuota(
            self,
            request: models.CreateAigcQuotaRequest,
            opts: Dict = None,
    ) -> models.CreateAigcQuotaResponse:
        """
        This API is used to create and enable AIGC quota configuration. Quota usage starts accumulating when the quota feature is enabled. The AIGC feature will no longer be usable when the quota is reached.

        If the quota is re-enabled after deletion, the amount will be cleared and recalculated.

        Since AGC content generation is an async task, real-time usage data cannot be obtained. Therefore, the Quota limit may result in some errors, and completely precise control cannot be achieved with the set limit.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcSubject(
            self,
            request: models.CreateAigcSubjectRequest,
            opts: Dict = None,
    ) -> models.CreateAigcSubjectResponse:
        """
        This API is used to create AIGC custom subjects (Vidu). Note that calling this API may incur fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcSubject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcSubjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcVideoRedrawTask(
            self,
            request: models.CreateAigcVideoRedrawTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAigcVideoRedrawTaskResponse:
        """
        This API is used to generate AIGC videos. API calls will occur actual fee. Refer to the video-on-demand [AIGC video generation billing documentation](https://www.tencentcloud.com/zh/document/product/266/14666#96b3b59a-f9e1-49e9-966a-bedb70a4bf12). The feature settlement mode is [pay-as-you-go](https://www.tencentcloud.com/document/product/266/2838?from_cn_redirect=1). Daily billing customers will be charged on the second day for usage on the day, while monthly billing customers will be billed on the 1st of the next month for usage in the previous month.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcVideoRedrawTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcVideoRedrawTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcVideoTask(
            self,
            request: models.CreateAigcVideoTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAigcVideoTaskResponse:
        """
        This API is used to generate AIGC videos. The default limit is 1 concurrent processing. API calls will incur actual fees. Refer to the VOD AIGC video generation billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12). The feature settlement mode is pay-as-you-go. Daily billing customers will be charged on the second day for usage on the day, while monthly settlement customers will be billed on the 1st of the next month for usage in the previous month.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcVideoTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcVideoTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAnimatedGraphicsTemplate(
            self,
            request: models.CreateAnimatedGraphicsTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAnimatedGraphicsTemplateResponse:
        """
        This API is used to create a custom animated image generating template. Up to 16 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAnimatedGraphicsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAnimatedGraphicsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBlindWatermarkTemplate(
            self,
            request: models.CreateBlindWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateBlindWatermarkTemplateResponse:
        """
        This API is used to create a user-defined digital watermark template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBlindWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBlindWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCDNDomain(
            self,
            request: models.CreateCDNDomainRequest,
            opts: Dict = None,
    ) -> models.CreateCDNDomainResponse:
        """
        This API is used for adding domain names to VOD. A user can add up to 20 domain names. 1. After the domain name is added successfully, VOD will carry out the deployment of the domain name. It takes approximately 2 minutes for the domain name to change from the deployment status to the online status.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCDNDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCDNDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCLSLogset(
            self,
            request: models.CreateCLSLogsetRequest,
            opts: Dict = None,
    ) -> models.CreateCLSLogsetResponse:
        """
        Create a new logset with VOD.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCLSLogset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCLSLogsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCLSTopic(
            self,
            request: models.CreateCLSTopicRequest,
            opts: Dict = None,
    ) -> models.CreateCLSTopicResponse:
        """
        Create a new CLS log topic under VOD
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCLSTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCLSTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClass(
            self,
            request: models.CreateClassRequest,
            opts: Dict = None,
    ) -> models.CreateClassResponse:
        """
        * This API is used to categorize media assets for management;
        * It does not affect the categories of existing media assets. If you want to modify the category of a media asset, call the [ModifyMediaInfo](https://intl.cloud.tencent.com/document/product/266/31762?from_cn_redirect=1) API.
        * There can be up to 4 levels of categories.
        * One category can have up to 500 subcategories under it.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateComplexAdaptiveDynamicStreamingTask(
            self,
            request: models.CreateComplexAdaptiveDynamicStreamingTaskRequest,
            opts: Dict = None,
    ) -> models.CreateComplexAdaptiveDynamicStreamingTaskResponse:
        """
        Initiate complex adaptive bitstream processing. Features include:
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
        """
        
        kwargs = {}
        kwargs["action"] = "CreateComplexAdaptiveDynamicStreamingTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateComplexAdaptiveDynamicStreamingTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateContentReviewTemplate(
            self,
            request: models.CreateContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateContentReviewTemplateResponse:
        """
        We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [CreateReviewTemplate](https://intl.cloud.tencent.com/document/api/266/84391?from_cn_redirect=1).
        This API is used to create a custom audio/video moderation template. Up to 50 templates can be created in total.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateContentReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainVerifyRecord(
            self,
            request: models.CreateDomainVerifyRecordRequest,
            opts: Dict = None,
    ) -> models.CreateDomainVerifyRecordResponse:
        """
        This API is used for generating a subdomain resolution, prompting the customer to add it to the domain name resolution, used for wildcard domain and domain name retrieval verification of ownership.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainVerifyRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainVerifyRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnhanceMediaTemplate(
            self,
            request: models.CreateEnhanceMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateEnhanceMediaTemplateResponse:
        """
        Create enhance media template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnhanceMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnhanceMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHeadTailTemplate(
            self,
            request: models.CreateHeadTailTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateHeadTailTemplateResponse:
        """
        This API is used to create a title and trailer template.
        -The maximum supported template quantity is 100.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHeadTailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHeadTailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageProcessingTemplate(
            self,
            request: models.CreateImageProcessingTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateImageProcessingTemplateResponse:
        """
        This API is used to create a custom image processing template. A template can include at most 10 operations, for example, crop-scale-crop-blur-scale-crop-scale-crop-blur-scale. You can have up to 16 image processing templates.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageProcessingTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageProcessingTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageSpriteTemplate(
            self,
            request: models.CreateImageSpriteTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateImageSpriteTemplateResponse:
        """
        This API is used to create a custom image sprite generating template. Up to 16 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageSpriteTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageSpriteTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateJustInTimeTranscodeTemplate(
            self,
            request: models.CreateJustInTimeTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateJustInTimeTranscodeTemplateResponse:
        """
        Create Just In Time Transcode Template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLLMComprehendTemplate(
            self,
            request: models.CreateLLMComprehendTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLLMComprehendTemplateResponse:
        """
        Create a large model comprehend template
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLLMComprehendTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLLMComprehendTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMPSTemplate(
            self,
            request: models.CreateMPSTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateMPSTemplateResponse:
        """
        This API is used to create a custom template for partial features of the ProcessMediaByMPS API.
        When creating a template, you need to fill in MPS-related parameters in JSON format into the MPSCreateTemplateParams parameter. For specific task parameter configuration methods, refer to the MPS task template related documentation.
        Currently supported MPS features: create custom template.
        1. [Audio and video enhancement](https://www.tencentcloud.com/document/product/862/118703?from_cn_redirect=1).
        2. [Media AI](https://www.tencentcloud.com/document/product/1041/54517)

        Task Template created by this method
        Template management is still done on the VOD platform.
        2. The feature is currently in closed beta testing. If needed, you can contact us for support.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMPSTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMPSTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePersonSample(
            self,
            request: models.CreatePersonSampleRequest,
            opts: Dict = None,
    ) -> models.CreatePersonSampleResponse:
        """
        This API is used to create samples for using facial features positioning and other technologies to perform video processing operations such as content recognition and inappropriate information recognition.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProcedureTemplate(
            self,
            request: models.CreateProcedureTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateProcedureTemplateResponse:
        """
        This API is used to create a custom task flow template. Up to 50 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProcedureTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProcedureTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProcessImageAsyncTemplate(
            self,
            request: models.CreateProcessImageAsyncTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateProcessImageAsyncTemplateResponse:
        """
        Create a user-customized image processing template asynchronously. Maximum quantity: 50. HLS format not supported currently.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProcessImageAsyncTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProcessImageAsyncTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateQualityInspectTemplate(
            self,
            request: models.CreateQualityInspectTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateQualityInspectTemplateResponse:
        """
        Creates media quality inspection template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateQualityInspectTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateQualityInspectTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRebuildMediaTemplate(
            self,
            request: models.CreateRebuildMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateRebuildMediaTemplateResponse:
        """
        Create rebuild media template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRebuildMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRebuildMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReviewTemplate(
            self,
            request: models.CreateReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateReviewTemplateResponse:
        """
        This API is used to create a custom moderation template. Up to 50 templates can be created in total.
        > The templates can only be used by the APIs [ReviewAudioVideo](https://intl.cloud.tencent.com/document/api/266/80283?from_cn_redirect=1) and [ReviewImage](https://intl.cloud.tencent.com/document/api/266/73217?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoundPlay(
            self,
            request: models.CreateRoundPlayRequest,
            opts: Dict = None,
    ) -> models.CreateRoundPlayResponse:
        """
        This API is used to create a playlist. You can create at most 100 playlists.
        For each video on the list, you can either use the original file or a transcoding file.
        The files must be in HLS format. Preferably, they should have the same bitrate and resolution.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoundPlay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoundPlayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSampleSnapshotTemplate(
            self,
            request: models.CreateSampleSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSampleSnapshotTemplateResponse:
        """
        This API is used to create a custom sampled screencapturing template. Up to 16 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSampleSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSampleSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSceneAigcImageTask(
            self,
            request: models.CreateSceneAigcImageTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSceneAigcImageTaskResponse:
        """
        This API is used to generate scenario-based AIGC images. <b>This interface is in beta. If you need to use it, please contact us. API calls will incur actual fees.</b>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSceneAigcImageTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSceneAigcImageTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSceneAigcVideoTask(
            self,
            request: models.CreateSceneAigcVideoTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSceneAigcVideoTaskResponse:
        """
        This API is used to generate scenario-based AIGC images. API calls will occur actual fee.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSceneAigcVideoTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSceneAigcVideoTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshotByTimeOffsetTemplate(
            self,
            request: models.CreateSnapshotByTimeOffsetTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotByTimeOffsetTemplateResponse:
        """
        This API is used to create a custom time point screencapturing template. Up to 16 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshotByTimeOffsetTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotByTimeOffsetTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStorageRegion(
            self,
            request: models.CreateStorageRegionRequest,
            opts: Dict = None,
    ) -> models.CreateStorageRegionResponse:
        """
        This API is used to enable storage in a region.
          1. When you activate VOD, the system will enable storage for you in certain regions. If you need to store data in another region, you can use this API to enable storage in that region.
          2. You can use the `DescribeStorageRegions` API to query all supported storage regions and the regions you have storage access to currently.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStorageRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStorageRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubAppId(
            self,
            request: models.CreateSubAppIdRequest,
            opts: Dict = None,
    ) -> models.CreateSubAppIdResponse:
        """
        This API is used to create a VOD subapplication.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubAppId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubAppIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSuperPlayerConfig(
            self,
            request: models.CreateSuperPlayerConfigRequest,
            opts: Dict = None,
    ) -> models.CreateSuperPlayerConfigResponse:
        """
        We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to create a player configuration. Up to 100 configurations can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSuperPlayerConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSuperPlayerConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTranscodeTemplate(
            self,
            request: models.CreateTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateTranscodeTemplateResponse:
        """
        This API is used to create a custom transcoding template. Up to 100 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVodDomain(
            self,
            request: models.CreateVodDomainRequest,
            opts: Dict = None,
    ) -> models.CreateVodDomainResponse:
        """
        This API is used to add an acceleration domain name to VOD. One user can add up to 20 domain names.
        1. After a domain name is added, VOD will deploy it, and it takes about 2 minutes for the domain name status to change from `Deploying` to `Online`.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVodDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVodDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWatermarkTemplate(
            self,
            request: models.CreateWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateWatermarkTemplateResponse:
        """
        This API is used to create a custom watermarking template. Up to 1,000 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWordSamples(
            self,
            request: models.CreateWordSamplesRequest,
            opts: Dict = None,
    ) -> models.CreateWordSamplesResponse:
        """
        This API is used to create keyword samples in batches for using OCR and ASR technologies to perform video processing operations such as content recognition and inappropriate information recognition.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWordSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWordSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIAnalysisTemplate(
            self,
            request: models.DeleteAIAnalysisTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAIAnalysisTemplateResponse:
        """
        This API is used to delete a custom video content analysis template.

        Note: templates with an ID below 10000 are preset and cannot be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIAnalysisTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIAnalysisTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIRecognitionTemplate(
            self,
            request: models.DeleteAIRecognitionTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAIRecognitionTemplateResponse:
        """
        This API is used to delete a custom video content recognition template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIRecognitionTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIRecognitionTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAdaptiveDynamicStreamingTemplate(
            self,
            request: models.DeleteAdaptiveDynamicStreamingTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAdaptiveDynamicStreamingTemplateResponse:
        """
        This API is used to delete an adaptive bitrate streaming template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAdaptiveDynamicStreamingTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAdaptiveDynamicStreamingTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAigcAdvancedCustomElement(
            self,
            request: models.DeleteAigcAdvancedCustomElementRequest,
            opts: Dict = None,
    ) -> models.DeleteAigcAdvancedCustomElementResponse:
        """
        This API is used to delete the senior custom AIGC subject.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAigcAdvancedCustomElement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAigcAdvancedCustomElementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAigcApiToken(
            self,
            request: models.DeleteAigcApiTokenRequest,
            opts: Dict = None,
    ) -> models.DeleteAigcApiTokenResponse:
        """
        Delete an AIGC API Token.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAigcApiToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAigcApiTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAigcQuota(
            self,
            request: models.DeleteAigcQuotaRequest,
            opts: Dict = None,
    ) -> models.DeleteAigcQuotaResponse:
        """
        This API is used to delete AIGC quota configurations. Once deleted, it will no longer limit the initiation of AIGC tasks.

        If the quota is re-enabled after deletion, the amount will be cleared and recalculated.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAigcQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAigcQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAnimatedGraphicsTemplate(
            self,
            request: models.DeleteAnimatedGraphicsTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAnimatedGraphicsTemplateResponse:
        """
        This API is used to delete a custom animated image generating template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAnimatedGraphicsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAnimatedGraphicsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBlindWatermarkTemplate(
            self,
            request: models.DeleteBlindWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteBlindWatermarkTemplateResponse:
        """
        This API is used to delete a user-defined digital watermark template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBlindWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBlindWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCDNDomain(
            self,
            request: models.DeleteCDNDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteCDNDomainResponse:
        """
        Delete CDN Domain
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCDNDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCDNDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCLSTopic(
            self,
            request: models.DeleteCLSTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteCLSTopicResponse:
        """
        Delete the log topic enabled by VOD.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCLSTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCLSTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClass(
            self,
            request: models.DeleteClassRequest,
            opts: Dict = None,
    ) -> models.DeleteClassResponse:
        """
        * A category can be deleted only if it has no subcategories and associated media files;
        * Otherwise, [delete the media files](https://intl.cloud.tencent.com/document/product/266/31764?from_cn_redirect=1) and subcategories first before deleting the category.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteContentReviewTemplate(
            self,
            request: models.DeleteContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteContentReviewTemplateResponse:
        """
        We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [DeleteReviewTemplate](https://intl.cloud.tencent.com/document/api/266/84390?from_cn_redirect=1).
        This API is used to delete a custom audio/video moderation template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteContentReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnhanceMediaTemplate(
            self,
            request: models.DeleteEnhanceMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteEnhanceMediaTemplateResponse:
        """
        Delete Enhance Media template
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnhanceMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnhanceMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHeadTailTemplate(
            self,
            request: models.DeleteHeadTailTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteHeadTailTemplateResponse:
        """
        Delete HeadTail Template
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHeadTailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHeadTailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageProcessingTemplate(
            self,
            request: models.DeleteImageProcessingTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteImageProcessingTemplateResponse:
        """
        This API is used to delete an image processing template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageProcessingTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageProcessingTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageSpriteTemplate(
            self,
            request: models.DeleteImageSpriteTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteImageSpriteTemplateResponse:
        """
        This API is used to delete an image sprite generating template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageSpriteTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageSpriteTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJustInTimeTranscodeTemplate(
            self,
            request: models.DeleteJustInTimeTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteJustInTimeTranscodeTemplateResponse:
        """
        Delete Just In Time Transcode Template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLLMComprehendTemplate(
            self,
            request: models.DeleteLLMComprehendTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLLMComprehendTemplateResponse:
        """
        This API is used to delete a user's customized large model parsing template.

        Note: Template IDs below 10000 are system-preset templates and cannot be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLLMComprehendTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLLMComprehendTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMPSTemplate(
            self,
            request: models.DeleteMPSTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteMPSTemplateResponse:
        """
        This API is used to delete a user-defined MPS task template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMPSTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMPSTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMedia(
            self,
            request: models.DeleteMediaRequest,
            opts: Dict = None,
    ) -> models.DeleteMediaResponse:
        """
        * This API is used to delete a media file and its processed files, such as the transcoded video files, image sprites, screenshots, and videos for publishing on WeChat.
        * You can delete the original files, transcoded video files, and videos for publishing on WeChat, etc. of videos with specified IDs.
        * Note: after the original file of a video is deleted, you cannot transcode the video, publish it on WeChat, or perform other operations on it.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePersonSample(
            self,
            request: models.DeletePersonSampleRequest,
            opts: Dict = None,
    ) -> models.DeletePersonSampleResponse:
        """
        This API is used to delete samples according to sample IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProcedureTemplate(
            self,
            request: models.DeleteProcedureTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteProcedureTemplateResponse:
        """
        Delete user-created task flow templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProcedureTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProcedureTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProcessImageAsyncTemplate(
            self,
            request: models.DeleteProcessImageAsyncTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteProcessImageAsyncTemplateResponse:
        """
        This API is used to delete a user-customized image async processing template.

        Note: Template IDs below 10000 are system-preset templates and cannot be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProcessImageAsyncTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProcessImageAsyncTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteQualityInspectTemplate(
            self,
            request: models.DeleteQualityInspectTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteQualityInspectTemplateResponse:
        """
        Deletes media quality inspection template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteQualityInspectTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteQualityInspectTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRebuildMediaTemplate(
            self,
            request: models.DeleteRebuildMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteRebuildMediaTemplateResponse:
        """
        Delete rebuild media template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRebuildMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRebuildMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReviewTemplate(
            self,
            request: models.DeleteReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteReviewTemplateResponse:
        """
        This API is used to delete a custom moderation template.
        > The templates can only be used by the APIs [ReviewAudioVideo](https://intl.cloud.tencent.com/document/api/266/80283?from_cn_redirect=1) and [ReviewImage](https://intl.cloud.tencent.com/document/api/266/73217?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoundPlay(
            self,
            request: models.DeleteRoundPlayRequest,
            opts: Dict = None,
    ) -> models.DeleteRoundPlayResponse:
        """
        This API is used to delete a playlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoundPlay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoundPlayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSampleSnapshotTemplate(
            self,
            request: models.DeleteSampleSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSampleSnapshotTemplateResponse:
        """
        This API is used to delete a custom sampled screencapturing template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSampleSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSampleSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshotByTimeOffsetTemplate(
            self,
            request: models.DeleteSnapshotByTimeOffsetTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotByTimeOffsetTemplateResponse:
        """
        This API is used to delete a custom time point screencapturing template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshotByTimeOffsetTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotByTimeOffsetTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSuperPlayerConfig(
            self,
            request: models.DeleteSuperPlayerConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteSuperPlayerConfigResponse:
        """
        We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to delete a player configuration.
        *Note: Preset player configurations cannot be deleted.*
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSuperPlayerConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSuperPlayerConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTranscodeTemplate(
            self,
            request: models.DeleteTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteTranscodeTemplateResponse:
        """
        This API is used to delete a custom transcoding template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVodDomain(
            self,
            request: models.DeleteVodDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteVodDomainResponse:
        """
        This API is used to delete an acceleration domain name from VOD.
        1. Before deleting a domain name, disable its acceleration in all regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVodDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVodDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWatermarkTemplate(
            self,
            request: models.DeleteWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteWatermarkTemplateResponse:
        """
        This API is used to delete a custom watermarking template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWordSamples(
            self,
            request: models.DeleteWordSamplesRequest,
            opts: Dict = None,
    ) -> models.DeleteWordSamplesResponse:
        """
        This API is used to delete keyword samples in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWordSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWordSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisTemplates(
            self,
            request: models.DescribeAIAnalysisTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisTemplatesResponse:
        """
        This API is used to get the list of video content analysis templates based on unique template ID. The returned result includes all eligible custom and [preset video content analysis templates](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.88.86.E6.9E.90.E6.A8.A1.E6.9D.BF).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIRecognitionTemplates(
            self,
            request: models.DescribeAIRecognitionTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAIRecognitionTemplatesResponse:
        """
        This API is used to get the list of video content recognition templates based on unique template ID. The return result includes all eligible custom and [preset video content recognition templates](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E8.AF.86.E5.88.AB.E6.A8.A1.E6.9D.BF).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIRecognitionTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIRecognitionTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAdaptiveDynamicStreamingTemplates(
            self,
            request: models.DescribeAdaptiveDynamicStreamingTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAdaptiveDynamicStreamingTemplatesResponse:
        """
        This API is used to query the list of transcoding to adaptive bitrate streaming templates and supports paged queries by filters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAdaptiveDynamicStreamingTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAdaptiveDynamicStreamingTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAigcAdvancedCustomElements(
            self,
            request: models.DescribeAigcAdvancedCustomElementsRequest,
            opts: Dict = None,
    ) -> models.DescribeAigcAdvancedCustomElementsResponse:
        """
        This API is used to retrieve an advanced custom AIGC subject.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAigcAdvancedCustomElements"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAigcAdvancedCustomElementsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAigcApiTokens(
            self,
            request: models.DescribeAigcApiTokensRequest,
            opts: Dict = None,
    ) -> models.DescribeAigcApiTokensResponse:
        """
        Query the AIGC API Token list. There is a delay in data sync after creation or deletion. The latest data is queryable after about 30 seconds.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAigcApiTokens"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAigcApiTokensResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAigcFaceInfo(
            self,
            request: models.DescribeAigcFaceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAigcFaceInfoResponse:
        """
        This API is used to obtain AIGC face information. Note that calling this API will incur face recognition fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAigcFaceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAigcFaceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAigcFaceInfoAsync(
            self,
            request: models.DescribeAigcFaceInfoAsyncRequest,
            opts: Dict = None,
    ) -> models.DescribeAigcFaceInfoAsyncResponse:
        """
        This API is used to asynchronously fetch AIGC face information. Note that calling this API incurs face recognition fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAigcFaceInfoAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAigcFaceInfoAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAigcQuotas(
            self,
            request: models.DescribeAigcQuotasRequest,
            opts: Dict = None,
    ) -> models.DescribeAigcQuotasResponse:
        """
        This API is used to query the AIGC quota configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAigcQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAigcQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAigcUsageData(
            self,
            request: models.DescribeAigcUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeAigcUsageDataResponse:
        """
        This API is used to return statistical information of AIGC within a specified time range.
        1. AIGC stats from the last 365 days can be queried.
           2. The query time span should not exceed 90 days.
        3. If the query time span exceeds 1 day, return data with day-level granularity. Otherwise, return data with 5-minute granularity.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAigcUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAigcUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllClass(
            self,
            request: models.DescribeAllClassRequest,
            opts: Dict = None,
    ) -> models.DescribeAllClassResponse:
        """
        * This API is used to get the information of all categories.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAnimatedGraphicsTemplates(
            self,
            request: models.DescribeAnimatedGraphicsTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAnimatedGraphicsTemplatesResponse:
        """
        This API is used to query the list of animated image generating templates and supports paged queries by filters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAnimatedGraphicsTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAnimatedGraphicsTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlindWatermarkTemplates(
            self,
            request: models.DescribeBlindWatermarkTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeBlindWatermarkTemplatesResponse:
        """
        Query user-customized digital watermark templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlindWatermarkTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlindWatermarkTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCDNDomains(
            self,
            request: models.DescribeCDNDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeCDNDomainsResponse:
        """
        Describe CDN Domains
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCDNDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCDNDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCDNStatDetails(
            self,
            request: models.DescribeCDNStatDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeCDNStatDetailsResponse:
        """
        This API is used to query CDN bandwidth, traffic volume and stats of on-demand domain names.
        * The start time and end time of the query should not exceed a 90-day span.
        * You can query data from different service regions.
        Data support within the Chinese mainland allows querying stats by specified region and carrier.
        Playback statistics only target VOD domains (EdgeOne domain name distribution is not included).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCDNStatDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCDNStatDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCDNUsageData(
            self,
            request: models.DescribeCDNUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCDNUsageDataResponse:
        """
        This API is used to query traffic, bandwidth and stats of video-on-demand (VOD) CDN.
        1. The system side reserves CDN usage data for 13 months. You can query the most recent 365 days of usage data through the API. If needed, contact us to call historical usage data exceeding 365 days.
           2. The query time span should not exceed 90 days.
        3. You can specify the time granularity of usage data, which supports 5 minutes, 1 hour, and 1 day.
        4. Traffic volume is the total traffic within the query time granularity, and bandwidth is the peak bandwidth within the query time granularity.
        5. Playback statistics only target VOD domains (EdgeOne domain name distribution is not included).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCDNUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCDNUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCLSLogsets(
            self,
            request: models.DescribeCLSLogsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeCLSLogsetsResponse:
        """
        Query the CLS log set created by VOD.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSLogsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSLogsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCLSTopics(
            self,
            request: models.DescribeCLSTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeCLSTopicsResponse:
        """
        Query the log topic list created by VOD.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnLogs(
            self,
            request: models.DescribeCdnLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnLogsResponse:
        """
        Query the download URL of the access log for the CDN (exclude EdgeOne origin back to VOD domain) of the on-demand domain name.
        1. You can query the log download links for CDN in the most recent 30 days.
        2. By default, CDN creates a log file per hour. If no CDN access occurs in an hour, it does not generate a log file.
        3. The CDN log download link is with a validity of 24 hours.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdnLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdnLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientUploadAccelerationUsageData(
            self,
            request: models.DescribeClientUploadAccelerationUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeClientUploadAccelerationUsageDataResponse:
        """
        This interface returns client upload acceleration statistics within the query time range.
         1. You can query the client upload acceleration statistics in the last 365 days.
         2. The query time span does not exceed 90 days.
         3. If the query time span exceeds 1 day, data with day granularity will be returned. Otherwise, data with 5-minute granularity will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientUploadAccelerationUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientUploadAccelerationUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContentReviewTemplates(
            self,
            request: models.DescribeContentReviewTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeContentReviewTemplatesResponse:
        """
        We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [DescribeReviewTemplates](https://intl.cloud.tencent.com/document/api/266/84389?from_cn_redirect=1).
        This API is used to get the information of custom and [preset](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.AE.A1.E6.A0.B8.E6.A8.A1.E6.9D.BF) audio/video moderation templates based on template IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContentReviewTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContentReviewTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCurrentPlaylist(
            self,
            request: models.DescribeCurrentPlaylistRequest,
            opts: Dict = None,
    ) -> models.DescribeCurrentPlaylistResponse:
        """
        Query current playlist of the round play.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCurrentPlaylist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCurrentPlaylistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDailyPlayStatFileList(
            self,
            request: models.DescribeDailyPlayStatFileListRequest,
            opts: Dict = None,
    ) -> models.DescribeDailyPlayStatFileListResponse:
        """
        This API is used to query the download address of the playback statistics file.
        * You can query the download links for playback statistics from the past one year, with the time span between the start date and end date no more than 90 days.
        VOD analyzes and processes CDN request logs from the previous day to generate playback statistics files.
        The playback statistics file contains statistical information such as the number of plays and total traffic of media files.
        Play count statistics description:
        1. HLS file: Count playback times when accessing M3U8 files; do not count playback times when accessing TS files.
        2. Other files (such as MP4 files): The number of plays is not counted when the playback request has a range parameter and the start parameter is not equal to 0. In other cases, the number of plays is counted.
        * Playback device statistics: If a playback request includes the UserAgent parameter and the UserAgent contains identification such as Android or iPhone, it will be counted as mobile playback. Otherwise, it will be counted as PC playback.
        Playback statistics only target VOD domains (EdgeOne domain name distribution is not included).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDailyPlayStatFileList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDailyPlayStatFileListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultDistributionConfig(
            self,
            request: models.DescribeDefaultDistributionConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultDistributionConfigResponse:
        """
        This API is used to query the default distribution configuration.
        * Domain name and distribution protocol, which are the domain name and protocol in the media file distribution URL. Media files are distributed according to the default distribution configuration.
        Playback key, used to calculate player signature.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultDistributionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultDistributionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDrmKeyProviderInfo(
            self,
            request: models.DescribeDrmKeyProviderInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDrmKeyProviderInfoResponse:
        """
        This API is used to query DRM key information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDrmKeyProviderInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDrmKeyProviderInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnhanceMediaTemplates(
            self,
            request: models.DescribeEnhanceMediaTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeEnhanceMediaTemplatesResponse:
        """
        Describe Enhance Media Templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnhanceMediaTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnhanceMediaTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventConfig(
            self,
            request: models.DescribeEventConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeEventConfigResponse:
        """
        Tencent Cloud Video on Demand (VOD) provides customers with services such as media upload, media management, and media processing. During the execution process or when execution ends, VOD also offers various event notifications to help developers monitor service processing status and proceed with next business operations.

        Developers can use this interface to query the current configuration of event notification receiving method, recipient address and which events have enabled callback notification.

        Default API request rate limit: 100 requests/second.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileAttributes(
            self,
            request: models.DescribeFileAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeFileAttributesResponse:
        """
        This API is used to get file attributes asynchronously.
        - Currently, this API can only get the MD5 hash of a file.
        - If the file queried is in HLS or DASH format, the attributes of the index file will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHeadTailTemplates(
            self,
            request: models.DescribeHeadTailTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeHeadTailTemplatesResponse:
        """
        Describe HeadTail Templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHeadTailTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHeadTailTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageProcessingTemplates(
            self,
            request: models.DescribeImageProcessingTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeImageProcessingTemplatesResponse:
        """
        This API is used to query image processing templates. You can specify the filters as well as the offset to start returning records from.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageProcessingTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageProcessingTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageReviewUsageData(
            self,
            request: models.DescribeImageReviewUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeImageReviewUsageDataResponse:
        """
        This interface returns the image review usage information used every day within the query time range.
           1. You can query the image review statistics for the last 365 days.
           2. The query time span does not exceed 90 days.
           3. If the query time span exceeds 1 day, data with a granularity of days will be returned. Otherwise, data with a granularity of 5 minutes will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageReviewUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageReviewUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageSpriteTemplates(
            self,
            request: models.DescribeImageSpriteTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeImageSpriteTemplatesResponse:
        """
        This API is used to query the list of image sprite generating templates and supports paged queries by filters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageSpriteTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageSpriteTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJustInTimeTranscodeTemplates(
            self,
            request: models.DescribeJustInTimeTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeJustInTimeTranscodeTemplatesResponse:
        """
        Describe Just In Time Transcode Templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJustInTimeTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJustInTimeTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLLMComprehendTemplates(
            self,
            request: models.DescribeLLMComprehendTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLLMComprehendTemplatesResponse:
        """
        This API is used to obtain the template detail list based on the Template Unique Identifier of the large model comprehend template. The returned results include all eligible customized large model parsing templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLLMComprehendTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLLMComprehendTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseUsageData(
            self,
            request: models.DescribeLicenseUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseUsageDataResponse:
        """
        This interface returns information about the number of license requests per day within the query time range.
           1. You can query the license request statistics in the last 365 days.
           2. The query time span does not exceed 90 days.
           3. If the query time span exceeds 1 day, data with a granularity of days will be returned. Otherwise, data with a granularity of 5 minutes will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMPSTemplates(
            self,
            request: models.DescribeMPSTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeMPSTemplatesResponse:
        """
        Retrieve user-customized MPS task templates.
        When querying the template list, require MPS related parameters to be filled in MPSDescribeTemplateParams in JSON format. For task parameter configuration method, refer to MPS task template document description.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMPSTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMPSTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMediaInfos(
            self,
            request: models.DescribeMediaInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeMediaInfosResponse:
        """
        1. This API is used to get the information of multiple media files. Specifically, the information returned is as follows:
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
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMediaInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMediaInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMediaPlayStatDetails(
            self,
            request: models.DescribeMediaPlayStatDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeMediaPlayStatDetailsResponse:
        """
        This API is used to query playback statistics of media files by specified time granularity.
        * Playback statistics from the past one year can be queried.
        * The time granularity is hourly, and the span between end time and start time cannot exceed 7 days.
        * The time granularity is day, and the span between the end time and start time is up to 90 days.
        Playback statistics only target VOD domains (EdgeOne domain name distribution is not included).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMediaPlayStatDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMediaPlayStatDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMediaProcessUsageData(
            self,
            request: models.DescribeMediaProcessUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeMediaProcessUsageDataResponse:
        """
        This API is used to return the daily video processing usage information within the specified query time range.
        1. The data system reserves video processing usage for 13 months. You can use the interface to query the most recent 365 days of usage data. If needed, contact us to call historical usage data exceeding 365 days.
           2. The query time span should not exceed 90 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMediaProcessUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMediaProcessUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePersonSamples(
            self,
            request: models.DescribePersonSamplesRequest,
            opts: Dict = None,
    ) -> models.DescribePersonSamplesResponse:
        """
        This API is used to query the information of samples and supports paginated queries by sample ID, name, and tag.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePersonSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePersonSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcedureTemplates(
            self,
            request: models.DescribeProcedureTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeProcedureTemplatesResponse:
        """
        This API is used to get the list of task flow template details by task flow template name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcedureTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcedureTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessImageAsyncTemplates(
            self,
            request: models.DescribeProcessImageAsyncTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessImageAsyncTemplatesResponse:
        """
        This API is used to obtain the template details list of image asynchronous processing based on the Template Unique Identifier. The returned results include ALL eligible user-customized image asynchronous processing templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessImageAsyncTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessImageAsyncTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityInspectTemplates(
            self,
            request: models.DescribeQualityInspectTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityInspectTemplatesResponse:
        """
        Get media quality inspection Template List.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityInspectTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityInspectTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRebuildMediaTemplates(
            self,
            request: models.DescribeRebuildMediaTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeRebuildMediaTemplatesResponse:
        """
        Describe Rebuild Media Templates
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRebuildMediaTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRebuildMediaTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReviewDetails(
            self,
            request: models.DescribeReviewDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeReviewDetailsResponse:
        """
        <b>This API is disused and replaced by [DescribeMediaProcessUsageData](https://intl.cloud.tencent.com/document/product/266/41464?from_cn_redirect=1).</b>

        This API returns the video content duration for intelligent recognition in seconds per day within the queried period.

        1. The API is used to query statistics on the video content duration for intelligent recognition in the last 365 days.
        2. The query period is up to 90 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReviewDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReviewDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReviewTemplates(
            self,
            request: models.DescribeReviewTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeReviewTemplatesResponse:
        """
        This API is used to get the information of moderation templates.
        > The templates can only be used by the APIs [ReviewAudioVideo](https://intl.cloud.tencent.com/document/api/266/80283?from_cn_redirect=1) and [ReviewImage](https://intl.cloud.tencent.com/document/api/266/73217?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReviewTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReviewTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoundPlays(
            self,
            request: models.DescribeRoundPlaysRequest,
            opts: Dict = None,
    ) -> models.DescribeRoundPlaysResponse:
        """
        This API is used to query playlists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoundPlays"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoundPlaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleSnapshotTemplates(
            self,
            request: models.DescribeSampleSnapshotTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleSnapshotTemplatesResponse:
        """
        This API is used to query the list of sampled screencapturing templates and supports paged queries by filters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleSnapshotTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleSnapshotTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotByTimeOffsetTemplates(
            self,
            request: models.DescribeSnapshotByTimeOffsetTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotByTimeOffsetTemplatesResponse:
        """
        This API is used to query the list of time point screencapturing templates and supports paged queries by filters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotByTimeOffsetTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotByTimeOffsetTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStorageData(
            self,
            request: models.DescribeStorageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageDataResponse:
        """
        This API is used to query the storage capacity usage and number of files.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStorageDetails(
            self,
            request: models.DescribeStorageDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageDetailsResponse:
        """
        This API is used to query the VOD storage space used within a specified time range. The measurement unit is byte.
        1. The system side reserves storage usage data for 13 months. You can be queried usage data within the most recent 365 days through the API. If needed to call historical usage data exceeding 365 days, contact us.
        2. The query time span should not exceed 90 days.
        3. The query span at a minute granularity should not exceed 7 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorageDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStorageRegions(
            self,
            request: models.DescribeStorageRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageRegionsResponse:
        """
        This API is used to query the following information:
          1. All supported storage regions.
          2. The regions you have storage access to currently.
          3. The default storage region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorageRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubAppIds(
            self,
            request: models.DescribeSubAppIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubAppIdsResponse:
        """
        This API is used to query the list of the primary application and subapplications of the current account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubAppIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubAppIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSuperPlayerConfigs(
            self,
            request: models.DescribeSuperPlayerConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeSuperPlayerConfigsResponse:
        """
        We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to query player configurations. It supports pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSuperPlayerConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSuperPlayerConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskDetail(
            self,
            request: models.DescribeTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskDetailResponse:
        """
        This API is used to query the details of execution status and result of a task submitted in the last 3 days by task ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        * This API is used to query the task list;
        * If there are many data entries in the list, one single call of the API may not be able to pull the entire list. The `ScrollToken` parameter can be used to pull the list in batches;
        * Only tasks in the last three days (72 hours) can be queried.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTranscodeTemplates(
            self,
            request: models.DescribeTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeTranscodeTemplatesResponse:
        """
        This API is used to get the list of transcoding templates based on unique template ID. The return result includes all eligible custom and [preset transcoding templates](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVodDomains(
            self,
            request: models.DescribeVodDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeVodDomainsResponse:
        """
        This API is used to query the list of VOD domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVodDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVodDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWatermarkTemplates(
            self,
            request: models.DescribeWatermarkTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeWatermarkTemplatesResponse:
        """
        This API is used to query custom watermarking templates and supports paged queries by filters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWatermarkTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWatermarkTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWordSamples(
            self,
            request: models.DescribeWordSamplesRequest,
            opts: Dict = None,
    ) -> models.DescribeWordSamplesResponse:
        """
        This API is used to perform paginated queries of keyword sample information by use case, keyword, and tag.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWordSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWordSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditMedia(
            self,
            request: models.EditMediaRequest,
            opts: Dict = None,
    ) -> models.EditMediaResponse:
        """
        Edit the video (cut, splice, etc.) to generate a new video. The editing functions include:

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
        """
        
        kwargs = {}
        kwargs["action"] = "EditMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnhanceMediaByTemplate(
            self,
            request: models.EnhanceMediaByTemplateRequest,
            opts: Dict = None,
    ) -> models.EnhanceMediaByTemplateResponse:
        """
        Enhance Media By Template.
        """
        
        kwargs = {}
        kwargs["action"] = "EnhanceMediaByTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnhanceMediaByTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnhanceMediaQuality(
            self,
            request: models.EnhanceMediaQualityRequest,
            opts: Dict = None,
    ) -> models.EnhanceMediaQualityResponse:
        """
        Initiate a Remaster task for audio and video media in VOD
        """
        
        kwargs = {}
        kwargs["action"] = "EnhanceMediaQuality"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnhanceMediaQualityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteFunction(
            self,
            request: models.ExecuteFunctionRequest,
            opts: Dict = None,
    ) -> models.ExecuteFunctionResponse:
        """
        This API is only used in special scenarios of custom development. Unless requested by VOD customer service, please do not call it.
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractBlindWatermark(
            self,
            request: models.ExtractBlindWatermarkRequest,
            opts: Dict = None,
    ) -> models.ExtractBlindWatermarkResponse:
        """
        This API is used to initiate a digital watermark extraction task for a video. The extraction result can be queried through DescribeTaskDetail.
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractBlindWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractBlindWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractCopyRightWatermark(
            self,
            request: models.ExtractCopyRightWatermarkRequest,
            opts: Dict = None,
    ) -> models.ExtractCopyRightWatermarkResponse:
        """
        If you need source tracing for piracy, refer to ghost watermark (https://www.tencentcloud.com/document/product/266/94228?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractCopyRightWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractCopyRightWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractTraceWatermark(
            self,
            request: models.ExtractTraceWatermarkRequest,
            opts: Dict = None,
    ) -> models.ExtractTraceWatermarkResponse:
        """
        If you need source tracing for piracy, ghost watermark (https://www.tencentcloud.com/document/product/266/94228?from_cn_redirect=1) is recommended.
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractTraceWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractTraceWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FastEditMedia(
            self,
            request: models.FastEditMediaRequest,
            opts: Dict = None,
    ) -> models.FastEditMediaResponse:
        """
        This API is used to implement quick splice and quick editing for HLS videos in VOD, generating new media in HLS format.

        Quickly splice or edit the generated video to generate a new FileId and perform solidification. After successful solidification, the new video file exists independent of the original input video and is not impacted by the deletion of the original video.

        <font color='red'>Note:</font> Enable reception of editing solidification event notifications through the ModifyEventConfig API. After successful solidification, you will receive an event notification of PersistenceComplete type. Before receiving this event notification, you should not perform operations such as delete or downgrade on the original input video, otherwise exceptions may occur during playback of the generated video from splicing and clipping.
        """
        
        kwargs = {}
        kwargs["action"] = "FastEditMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FastEditMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForbidMediaDistribution(
            self,
            request: models.ForbidMediaDistributionRequest,
            opts: Dict = None,
    ) -> models.ForbidMediaDistributionResponse:
        """
        After media blocking is enabled, all URLs for accessing various resources (raw file, transcoding output file, screenshot, etc.) will return 403 except for vod console preview.
        The unblock operation takes effect across the entire network in approximately 5-10 minutes.
        * Note: Banned media can only operate standard storage and infrequent storage media. Infrequent storage media must be stored for at least 30 days. Early deletion or changing the storage class will still be billed for 30 days. If infrequent storage media is banned and its infrequent access storage period is less than 30 days, early deletion billing will occur. Meanwhile, the infrequent access storage duration of the banned media will restart from the current system time. If the media is deleted or its storage class is changed within 30 days, early deletion billing will also occur. For example: Media 001 has been in infrequent storage for 10 days. At this point, if 001 is banned, the infrequent storage billing will still be calculated for 30 days (early deletion billing duration is 30 - 10 = 20 days). After the ban, the infrequent access storage duration of 001 restarts. If 001 is deleted on the 5th day after the ban, the infrequent storage billing will also be calculated for 30 days (early deletion billing duration is 30 - 5 = 25 days). The actual infrequent access storage duration of 001 is 10 + 5 = 15 days, while the infrequent storage billing duration is 10 + 20 (early deletion billing) + 5 + 25 (early deletion billing) = 60 days.
        """
        
        kwargs = {}
        kwargs["action"] = "ForbidMediaDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForbidMediaDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HandleCurrentPlaylist(
            self,
            request: models.HandleCurrentPlaylistRequest,
            opts: Dict = None,
    ) -> models.HandleCurrentPlaylistResponse:
        """
        Operate the current play list . Supported operations include:<li> Insert: Insert a playing program into the current playlist.</li><li> Delete: Remove a playing program from the playlist.</li>
        """
        
        kwargs = {}
        kwargs["action"] = "HandleCurrentPlaylist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HandleCurrentPlaylistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportMediaKnowledge(
            self,
            request: models.ImportMediaKnowledgeRequest,
            opts: Dict = None,
    ) -> models.ImportMediaKnowledgeResponse:
        """
        This API is used to import AI analysis results into the knowledge base.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportMediaKnowledge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportMediaKnowledgeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InspectMediaQuality(
            self,
            request: models.InspectMediaQualityRequest,
            opts: Dict = None,
    ) -> models.InspectMediaQualityResponse:
        """
        Initiate media quality inspection task.
        """
        
        kwargs = {}
        kwargs["action"] = "InspectMediaQuality"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InspectMediaQualityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListFiles(
            self,
            request: models.ListFilesRequest,
            opts: Dict = None,
    ) -> models.ListFilesResponse:
        """
        This API is used to list stored file entries under a sub-app.

        This API is available only in "FileID+Path mode".
        """
        
        kwargs = {}
        kwargs["action"] = "ListFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LiveRealTimeClip(
            self,
            request: models.LiveRealTimeClipRequest,
            opts: Dict = None,
    ) -> models.LiveRealTimeClipResponse:
        """
        Live stream clipping refers to the process where, during a live stream (not yet ended), customers can select a segment from past live stream content to generate a new video (HLS format) in real time. Developers can instantly share it or preserve it for long-term storage.

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
        """
        
        kwargs = {}
        kwargs["action"] = "LiveRealTimeClip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LiveRealTimeClipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageTask(
            self,
            request: models.ManageTaskRequest,
            opts: Dict = None,
    ) -> models.ManageTaskResponse:
        """
        This API is used to manage initiated tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "ManageTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAIAnalysisTemplate(
            self,
            request: models.ModifyAIAnalysisTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyAIAnalysisTemplateResponse:
        """
        This API is used to modify a custom video content analysis template.

        Note: templates with an ID below 10000 are preset and cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAIAnalysisTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAIAnalysisTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAIRecognitionTemplate(
            self,
            request: models.ModifyAIRecognitionTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyAIRecognitionTemplateResponse:
        """
        This API is used to modify a custom video content recognition template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAIRecognitionTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAIRecognitionTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAdaptiveDynamicStreamingTemplate(
            self,
            request: models.ModifyAdaptiveDynamicStreamingTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyAdaptiveDynamicStreamingTemplateResponse:
        """
        This API is used to modify an adaptive bitrate streaming template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAdaptiveDynamicStreamingTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAdaptiveDynamicStreamingTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAigcQuota(
            self,
            request: models.ModifyAigcQuotaRequest,
            opts: Dict = None,
    ) -> models.ModifyAigcQuotaResponse:
        """
        This API is used to edit AIGC quota configuration. Quota usage starts accumulating when the quota functionality is enabled. The AIGC functionality will no longer be usable once the quota is reached.

        Since AGC content generation is an async task, real-time usage data cannot be obtained. Therefore, the Quota limit may result in some errors, and completely precise control cannot be achieved with the set limit.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAigcQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAigcQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAnimatedGraphicsTemplate(
            self,
            request: models.ModifyAnimatedGraphicsTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyAnimatedGraphicsTemplateResponse:
        """
        This API is used to modify a custom animated image generating template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAnimatedGraphicsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAnimatedGraphicsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBlindWatermarkTemplate(
            self,
            request: models.ModifyBlindWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyBlindWatermarkTemplateResponse:
        """
        This API is used to modify a user-defined digital watermark template. The digital watermark type cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBlindWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBlindWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCDNDomainConfig(
            self,
            request: models.ModifyCDNDomainConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyCDNDomainConfigResponse:
        """
        Modify CDN Domain Config.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCDNDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCDNDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClass(
            self,
            request: models.ModifyClassRequest,
            opts: Dict = None,
    ) -> models.ModifyClassResponse:
        """
        This API is used to modify the category of a media file.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyContentReviewTemplate(
            self,
            request: models.ModifyContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyContentReviewTemplateResponse:
        """
        We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [ModifyReviewTemplate](https://intl.cloud.tencent.com/document/api/266/84388?from_cn_redirect=1).
        This API is used to modify a custom audio/video moderation template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContentReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDefaultStorageRegion(
            self,
            request: models.ModifyDefaultStorageRegionRequest,
            opts: Dict = None,
    ) -> models.ModifyDefaultStorageRegionResponse:
        """
        This API is used to set the default storage region. A file will be stored in the default region if no region is specified for file upload.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDefaultStorageRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDefaultStorageRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnhanceMediaTemplate(
            self,
            request: models.ModifyEnhanceMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyEnhanceMediaTemplateResponse:
        """
        Modify enhance media template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnhanceMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnhanceMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEventConfig(
            self,
            request: models.ModifyEventConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyEventConfigResponse:
        """
        Tencent Cloud VOD provides customers with media upload, media management, media processing and other services. During or at the end of the execution of these services, Tencent Cloud On-Demand also provides various corresponding event notifications to facilitate developers to perceive the service processing status and Do the next business operation.

        Developers can achieve this by calling this interface:
        - Set the type of callback notification received. Currently, there is [HTTP callback notification](https://www.tencentcloud.com/document/product/266/33948) and [reliable notification based on message queue](https://www.tencentcloud.com/document/product/266/33948) two types.
        - For [HTTP callback notification](https://www.tencentcloud.com/document/product/266/33948), you can set the address of the 3.0 format callback. For the description of 3.0 format callback, see [Historical Format Callback](https://intl.cloud.tencent.com/document/product/266/33796?from_cn_redirect=1).
        - Select settings to receive or ignore notification events for specific event services.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEventConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEventConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHeadTailTemplate(
            self,
            request: models.ModifyHeadTailTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyHeadTailTemplateResponse:
        """
        Modify HeadTail Template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHeadTailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHeadTailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageSpriteTemplate(
            self,
            request: models.ModifyImageSpriteTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyImageSpriteTemplateResponse:
        """
        This API is used to modify a custom image sprite generating template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageSpriteTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageSpriteTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyJustInTimeTranscodeTemplate(
            self,
            request: models.ModifyJustInTimeTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyJustInTimeTranscodeTemplateResponse:
        """
        Modify Just In Time Transcode Template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLLMComprehendTemplate(
            self,
            request: models.ModifyLLMComprehendTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLLMComprehendTemplateResponse:
        """
        Modify the parsing template of a large model
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLLMComprehendTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLLMComprehendTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMPSTemplate(
            self,
            request: models.ModifyMPSTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyMPSTemplateResponse:
        """
        Modify a user-customized MPS task template.
        When modifying a template, require filling in MPS related parameters in JSON format into the MPSModifyTemplateParams parameter. For specific task parameter configuration methods, refer to the MPS task template document description.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMPSTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMPSTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMediaInfo(
            self,
            request: models.ModifyMediaInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyMediaInfoResponse:
        """
        This API is used to modify the attributes of a media file, including category, name, description, tag, expiration time, timestamp information, video thumbnail, and subtitle information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMediaInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMediaInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMediaStorageClass(
            self,
            request: models.ModifyMediaStorageClassRequest,
            opts: Dict = None,
    ) -> models.ModifyMediaStorageClassResponse:
        """
        This API is used to modify the storage class of media files.
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
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMediaStorageClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMediaStorageClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPersonSample(
            self,
            request: models.ModifyPersonSampleRequest,
            opts: Dict = None,
    ) -> models.ModifyPersonSampleResponse:
        """
        This API is used to modify sample information according to the sample ID. You can modify the name and description, add, delete, and reset facial features or tags. Leave at least one image after deleting facial features. To leave no image, please use the reset operation.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProcessImageAsyncTemplate(
            self,
            request: models.ModifyProcessImageAsyncTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyProcessImageAsyncTemplateResponse:
        """
        This API is used to modify a user-customized image asynchronous processing template.

        Note: Template IDs below 10000 are system-preset templates and not allowed to be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProcessImageAsyncTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProcessImageAsyncTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyQualityInspectTemplate(
            self,
            request: models.ModifyQualityInspectTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyQualityInspectTemplateResponse:
        """
        Modifies media quality inspection template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyQualityInspectTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyQualityInspectTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRebuildMediaTemplate(
            self,
            request: models.ModifyRebuildMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyRebuildMediaTemplateResponse:
        """
        Modify Rebuild Media Template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRebuildMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRebuildMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReviewTemplate(
            self,
            request: models.ModifyReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyReviewTemplateResponse:
        """
        This API is used to modify a custom moderation template.
        > The templates can only be used by the APIs [ReviewAudioVideo](https://intl.cloud.tencent.com/document/api/266/80283?from_cn_redirect=1) and [ReviewImage](https://intl.cloud.tencent.com/document/api/266/73217?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoundPlay(
            self,
            request: models.ModifyRoundPlayRequest,
            opts: Dict = None,
    ) -> models.ModifyRoundPlayResponse:
        """
        This API is used to modify a playlist.
        The modification will only take effect for new playback requests. For ongoing playback, the old playlist will be playable for seven days after the modification.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoundPlay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoundPlayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySampleSnapshotTemplate(
            self,
            request: models.ModifySampleSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifySampleSnapshotTemplateResponse:
        """
        This API is used to modify a custom sampled screencapturing template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySampleSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySampleSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshotByTimeOffsetTemplate(
            self,
            request: models.ModifySnapshotByTimeOffsetTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotByTimeOffsetTemplateResponse:
        """
        This API is used to modify a custom time point screencapturing template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshotByTimeOffsetTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotByTimeOffsetTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubAppIdInfo(
            self,
            request: models.ModifySubAppIdInfoRequest,
            opts: Dict = None,
    ) -> models.ModifySubAppIdInfoResponse:
        """
        This API is used to modify subapplication information, but it is not allowed to modify primary application information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubAppIdInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubAppIdInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubAppIdStatus(
            self,
            request: models.ModifySubAppIdStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySubAppIdStatusResponse:
        """
        This API is used to enable/disable a subapplication. After a subapplication is disabled, its corresponding domain name will be blocked and its access to the console will be restricted.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubAppIdStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubAppIdStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySuperPlayerConfig(
            self,
            request: models.ModifySuperPlayerConfigRequest,
            opts: Dict = None,
    ) -> models.ModifySuperPlayerConfigResponse:
        """
        We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to modify a player configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySuperPlayerConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySuperPlayerConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTranscodeTemplate(
            self,
            request: models.ModifyTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyTranscodeTemplateResponse:
        """
        This API is used to modify a custom transcoding template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVodDomainAccelerateConfig(
            self,
            request: models.ModifyVodDomainAccelerateConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyVodDomainAccelerateConfigResponse:
        """
        This API is used to modify the acceleration region of a domain name on VOD.
        1. You can modify acceleration regions of only domain names whose status is `Online`.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVodDomainAccelerateConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVodDomainAccelerateConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVodDomainConfig(
            self,
            request: models.ModifyVodDomainConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyVodDomainConfigResponse:
        """
        This API is used to modify domain name settings, such as the hotlink protection configuration.
        1. You can modify settings of only domain names whose status is `Online`.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVodDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVodDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWatermarkTemplate(
            self,
            request: models.ModifyWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyWatermarkTemplateResponse:
        """
        This API is used to modify a custom watermarking template. The watermark type cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWordSample(
            self,
            request: models.ModifyWordSampleRequest,
            opts: Dict = None,
    ) -> models.ModifyWordSampleResponse:
        """
        This API is used to modify the use case and tag of a keyword. The keyword itself cannot be modified, but you can delete it and create another one if needed.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWordSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWordSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseStreamingManifest(
            self,
            request: models.ParseStreamingManifestRequest,
            opts: Dict = None,
    ) -> models.ParseStreamingManifestResponse:
        """
        This API is used to parse the index file content and return the list of segment files to be uploaded when an HLS video is uploaded. A segment file path must be a relative path of the current directory or subdirectory instead of a URL or absolute path.
        """
        
        kwargs = {}
        kwargs["action"] = "ParseStreamingManifest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseStreamingManifestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessImageAsync(
            self,
            request: models.ProcessImageAsyncRequest,
            opts: Dict = None,
    ) -> models.ProcessImageAsyncResponse:
        """
        This API is used to process images.
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessImageAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessImageAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMedia(
            self,
            request: models.ProcessMediaRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaResponse:
        """
        This API is used to initiate processing tasks for audio-video media in on-demand video, with features including:
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
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMediaByMPS(
            self,
            request: models.ProcessMediaByMPSRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaByMPSResponse:
        """
        Use the media processing capability of the media processing service to trigger media processing for on-demand video.

        Video processing tasks initiated by this method:
        Querying the status of tasks and results is still done on the VOD platform. Use [DescribeTaskDetail](https://www.tencentcloud.com/document/product/266/33431?from_cn_redirect=1) or [DescribeTasks](https://www.tencentcloud.com/document/product/266/33430?from_cn_redirect=1) to query tasks.
        2. The amount and bills of related features will be provided on the MPS platform. Before using this feature, start by enabling the Media Processing Service (MPS) in the console. For the activation method, refer to the preliminary operations in the integration guide.
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMediaByMPS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMediaByMPSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMediaByProcedure(
            self,
            request: models.ProcessMediaByProcedureRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaByProcedureResponse:
        """
        This API is used to start a task flow on a video.
        There are two ways to create a task flow template:
        1. Create and modify a task flow template in the console;
        2. Create a task flow template using the `CreateProcedureTemplate` API.

        If event notifications are used, the event type for moderation tasks is [ReviewAudioVideoComplete](https://intl.cloud.tencent.com/document/product/266/81258?from_cn_redirect=1), and that for other tasks is [ProcedureStateChanged](https://intl.cloud.tencent.com/document/product/266/9636?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMediaByProcedure"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMediaByProcedureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMediaByUrl(
            self,
            request: models.ProcessMediaByUrlRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaByUrlResponse:
        """
        This API is <font color='red'>disused</font>, please use [ProcessMedia](https://intl.cloud.tencent.com/document/product/862/37578?from_cn_redirect=1) API of MPS, with the input parameter `InputInfo.UrlInputInfo.Url` set to a video URL.
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMediaByUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMediaByUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullEvents(
            self,
            request: models.PullEventsRequest,
            opts: Dict = None,
    ) -> models.PullEventsResponse:
        """
        * This API is used to get event notifications from the business server through [reliable callback](https://intl.cloud.tencent.com/document/product/266/33948).
        * The API gets event data through long polling. That is, if there is any unconsumed event on the server, the event notification will be returned to the requester immediately. If there is no unconsumed event on the server, the request will be suspended in the backend until a new event is generated.
        * The request can be suspended for up to 5 seconds. It's recommended to set the request timeout period to 10 seconds.
        * Event notifications not pulled will be retained for up to 4 days and may be cleared after this period.
        * After the API returns an event, the caller must call the [ConfirmEvents](https://intl.cloud.tencent.com/document/product/266/34184) API within <font color="red">30 seconds</font> to confirm that the event notification has been processed. Otherwise, the event notification will be pulled again after <font color="red">30 seconds</font>.
        * This API can get up to 16 event notifications at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "PullEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullUpload(
            self,
            request: models.PullUploadRequest,
            opts: Dict = None,
    ) -> models.PullUploadResponse:
        """
        This API is used to pull a video on the internet to the VOD platform.
        """
        
        kwargs = {}
        kwargs["action"] = "PullUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PushUrlCache(
            self,
            request: models.PushUrlCacheRequest,
            opts: Dict = None,
    ) -> models.PushUrlCacheResponse:
        """
        1. This API is used to prefetch a list of specified URLs.
        2. The URL domain names must have already been registered with VOD.
        3. Up to 20 URLs can be specified in one request.
        4. By default, the maximum number of URLs that can be refreshed per day is 10,000.
        """
        
        kwargs = {}
        kwargs["action"] = "PushUrlCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PushUrlCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebuildMedia(
            self,
            request: models.RebuildMediaRequest,
            opts: Dict = None,
    ) -> models.RebuildMediaResponse:
        """
        Initiate rebuild media
        """
        
        kwargs = {}
        kwargs["action"] = "RebuildMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebuildMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebuildMediaByTemplate(
            self,
            request: models.RebuildMediaByTemplateRequest,
            opts: Dict = None,
    ) -> models.RebuildMediaByTemplateResponse:
        """
        Rebuild media by template.
        """
        
        kwargs = {}
        kwargs["action"] = "RebuildMediaByTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebuildMediaByTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshUrlCache(
            self,
            request: models.RefreshUrlCacheRequest,
            opts: Dict = None,
    ) -> models.RefreshUrlCacheResponse:
        """
        1. This API is used to purge URLs.
        2. The URL domain names must have already been registered with VOD.
        3. Up to 20 URLs can be specified in one request.
        4. By default, the maximum number of URLs allowed for purge per day is 100,000.
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshUrlCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshUrlCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveWatermark(
            self,
            request: models.RemoveWatermarkRequest,
            opts: Dict = None,
    ) -> models.RemoveWatermarkResponse:
        """
        This API is used to remove watermarks from a video.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetProcedureTemplate(
            self,
            request: models.ResetProcedureTemplateRequest,
            opts: Dict = None,
    ) -> models.ResetProcedureTemplateResponse:
        """
        This API is used to modify a custom task flow template.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetProcedureTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetProcedureTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreMedia(
            self,
            request: models.RestoreMediaRequest,
            opts: Dict = None,
    ) -> models.RestoreMediaResponse:
        """
        This API is used to restore files from ARCHIVE or DEEP ARCHIVE. Files stored in ARCHIVE or DEEP ARCHIVE must be restored before they can be accessed. Restored files are available for a limited period of time.
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReviewAudioVideo(
            self,
            request: models.ReviewAudioVideoRequest,
            opts: Dict = None,
    ) -> models.ReviewAudioVideoResponse:
        """
        This API is used to start a moderation task on a file stored in VOD to detect non-compliant content in images, text, speech, and voice.

        If event notifications are used, the event type is [ReviewAudioVideoComplete](https://intl.cloud.tencent.com/document/product/266/81258?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ReviewAudioVideo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReviewAudioVideoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReviewImage(
            self,
            request: models.ReviewImageRequest,
            opts: Dict = None,
    ) -> models.ReviewImageResponse:
        """
        This API is used to moderate an image stored in VOD (detect pornographic and terrorist content).><li>The image file must be smaller than 5 MB.</li> ><li>To ensure the accuracy of moderation results, the image resolution must be higher than 256 x 256 px.</li> ><li>The format must be PNG, JPG, JPEG, BMP, GIF, or WEBP.</li>
        """
        
        kwargs = {}
        kwargs["action"] = "ReviewImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReviewImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchMedia(
            self,
            request: models.SearchMediaRequest,
            opts: Dict = None,
    ) -> models.SearchMediaResponse:
        """
        Search media information, support multiple conditions filter criteria, and sort returned results, filter, and other features. This includes:
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
        """
        
        kwargs = {}
        kwargs["action"] = "SearchMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchMediaBySemantics(
            self,
            request: models.SearchMediaBySemanticsRequest,
            opts: Dict = None,
    ) -> models.SearchMediaBySemanticsResponse:
        """
        This API is used to conduct semantic search on media using natural language.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchMediaBySemantics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchMediaBySemanticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetDrmKeyProviderInfo(
            self,
            request: models.SetDrmKeyProviderInfoRequest,
            opts: Dict = None,
    ) -> models.SetDrmKeyProviderInfoResponse:
        """
        This API is used to configure DRM key information.
        """
        
        kwargs = {}
        kwargs["action"] = "SetDrmKeyProviderInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetDrmKeyProviderInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetVodDomainCertificate(
            self,
            request: models.SetVodDomainCertificateRequest,
            opts: Dict = None,
    ) -> models.SetVodDomainCertificateResponse:
        """
        Set Vod Domain Certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "SetVodDomainCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetVodDomainCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SimpleHlsClip(
            self,
            request: models.SimpleHlsClipRequest,
            opts: Dict = None,
    ) -> models.SimpleHlsClipResponse:
        """
        This API is used to crop an HLS video by time period and generate a new real-time HLS video. Developers can share it immediately or preserve it for long-term.

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
        """
        
        kwargs = {}
        kwargs["action"] = "SimpleHlsClip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SimpleHlsClipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SplitMedia(
            self,
            request: models.SplitMediaRequest,
            opts: Dict = None,
    ) -> models.SplitMediaResponse:
        """
        Split the video into strips to generate multiple new videos.
        """
        
        kwargs = {}
        kwargs["action"] = "SplitMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SplitMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCDNDomain(
            self,
            request: models.StartCDNDomainRequest,
            opts: Dict = None,
    ) -> models.StartCDNDomainResponse:
        """
        This API is used for enabling/disabling the CDN acceleration domain.
        """
        
        kwargs = {}
        kwargs["action"] = "StartCDNDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartCDNDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyDomainRecord(
            self,
            request: models.VerifyDomainRecordRequest,
            opts: Dict = None,
    ) -> models.VerifyDomainRecordResponse:
        """
        This API is used to verify the domain name resolution value.
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyDomainRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyDomainRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)