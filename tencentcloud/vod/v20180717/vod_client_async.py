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
        We strongly recommend that you use the [server-side upload SDK](https://www.tencentcloud.comhttps://www.tencentcloud.com/document/product/266/9759?from_cn_redirect=1?from_cn_redirect=1#1.-.E5.8F.91.E8.B5.B7.E4.B8.8A.E4.BC.A0) provided by VOD to upload files. Directly invoking the API for upload is significantly more difficult and involves a much larger workload than using the SDK.
        * This API is used to apply for uploading media files (and cover files), obtain the meta-information for uploading files to VOD (including upload path and upload signature), for subsequent upload APIs.
        For the upload process, see [Server-Side Upload Overview](https://www.tencentcloud.com/document/product/266/9759?from_cn_redirect=1).
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
        Associate a media asset subtitle with the media output file corresponding to the adaptive bitrate streaming template ID (or disassociate it).
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
        Clone a CDN domain.
        """
        
        kwargs = {}
        kwargs["action"] = "CloneCDNDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneCDNDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneVoiceAsync(
            self,
            request: models.CloneVoiceAsyncRequest,
            opts: Dict = None,
    ) -> models.CloneVoiceAsyncResponse:
        """
        This API is used to trigger a voice cloning task. It clones a reference audio to generate an exclusive voice, which can be used for subsequent text to speech. Voice cloning is an asynchronous task. The voice ID and audio audition are generated after task completion.
        """
        
        kwargs = {}
        kwargs["action"] = "CloneVoiceAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneVoiceAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneVoiceSync(
            self,
            request: models.CloneVoiceSyncRequest,
            opts: Dict = None,
    ) -> models.CloneVoiceSyncResponse:
        """
        This API is used to trigger a voice cloning task. It clones a reference audio to generate an exclusive voice, which can be used for subsequent text to speech.
        """
        
        kwargs = {}
        kwargs["action"] = "CloneVoiceSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneVoiceSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitUpload(
            self,
            request: models.CommitUploadRequest,
            opts: Dict = None,
    ) -> models.CommitUploadResponse:
        """
        This API is used to confirm the upload result of media files and cover files to Tencent Cloud VOD, store media information, and return the playback address and file ID.
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
        This API is used to compose media files to achieve the following effects:

        1. **Image rotation**: rotates the image of a video or picture by a certain degree, or flips it in a certain direction.
        2. **Audio control**: Increase or reduce the volume of sound in video or audio, or mute the video.
        3. **Screen Overlay**: Overlay frames from videos and images in sequence, for example, to achieve a Picture-in-Picture effect.
        4. **Audio mixing**: Mix the sound in video and audio together.
        5. **Audio extraction**: Extract audio from the video (visuals are not retained).
        6. **Crop**: Crop a specified time period from video or audio.
        7. **Splicing**: Splice videos, audio, and images in chronological order.
        8. **Transitions**: When stitching multiple videos or images, you can add transition effects between paragraphs.

        The muxing format of the composed media can be MP4 (video) or MP3 (audio). If event notification is used, the event notification type is video synthesis completed (https://www.tencentcloud.com/document/product/266/43000?from_cn_redirect=1).
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
        * Developers call event notification pull to obtain events, and then must call this API to ACK message received.
        * After the developer obtains the event handler, the validity time for pending confirmation is 30 seconds. If it exceeds 30 seconds, a parameter error (4000) will be reported.
        * For more references on reliable callback of event notification, see [Reliable Callback](https://www.tencentcloud.com/document/product/266/33779?from_cn_redirect=1#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83).
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
        This API is used to create user-defined audio and video content analysis templates. Maximum number: 50. HLS format is not supported currently.
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
        This API is used to create user-defined audio and video content recognition templates. Maximum number: 50.
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
        Create an adaptive bitrate streaming template. Max: 100.
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
        This API is used to create a Token for AIGC API calls. Data sync has a delay once created. It can be queried or deleted after about 30 seconds.
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
        This API is used to create AIGC voice replication. Note that calling this API incurs fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).
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
        Call this API to create a subject for a specified model.
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
        This API is used to create AIGC custom voice types. Note that calling this API incurs a fee for creating custom voice types. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#5e5217e8-29fc-467e-ac2d-853648f988b7).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcCustomVoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcCustomVoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcHunyuan3DTask(
            self,
            request: models.CreateAigcHunyuan3DTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAigcHunyuan3DTaskResponse:
        """
        This API is used to create AIGC Hunyuan 3D tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcHunyuan3DTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcHunyuan3DTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcImageTask(
            self,
            request: models.CreateAigcImageTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAigcImageTaskResponse:
        """
        This API is used to [generate AIGC images](https://www.tencentcloud.com/document/product/266/124473?from_cn_redirect=1). The default limit is 1 concurrent processing. API calls will incur actual fees. Refer to the VOD [AIGC image generation billing documentation](https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#9c4dc6ff-4b3f-4b25-bf2d-393889dfb9ac). The settlement mode for the feature is [pay-as-you-go](https://www.tencentcloud.com/document/product/266/2838?from_cn_redirect=1). For daily billing customers, usage on the day is billed on the second day. For monthly settlement customers, the previous month's usage fees are billed on the 1st of the next month.
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
        This API is used to create and enable AIGC quota configuration. Quota usage starts accumulating from the enablement of the quota feature. Once the quota is reached, AIGC features will no longer be usable.

        If the quota is deleted and re-enabled, the amount will be cleared and recalculated.

        Since AGC content generation is an asynchronous task, real-time usage data cannot be obtained. Therefore, quota limits may result in some errors, and completely precise control over the set limit cannot be achieved.
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
        This API is used to create AIGC custom subjects (Vidu). Note that calling this API incurs fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).
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
        This API is used to generate AIGC videos. API calls incur actual fees. Refer to the VOD AIGC video generation billing documentation. The feature uses postpaid settlement. For daily billing customers, usage on the day is billed on the second day. For monthly billing customers, the previous month's usage fees are billed on the 1st of the next month.
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
        This API is used to generate AIGC videos. The default limit is 1 concurrent processing. API calls incur actual fees. Refer to the VOD AIGC video generation billing documentation. The settlement mode for this feature is pay-as-you-go. For daily billing customers, usage on the day is billed on the second day. For monthly billing customers, the previous month's usage fees are billed on the 1st of the next month.
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
        This API is used to create a user-customized animated image generating template. Maximum number: 16.
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
        This API is used to add domain names to VOD. A user can add up to 20 domain names. After the domain name is successfully added, VOD will deploy the domain. It takes about 2 minutes for the domain to change from the deployment state to the online status.
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
        Create a logset via VOD.
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
        This API is used to create a CLS log topic under VOD.
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
        * Used to categorize and manage media;
        * This API does not affect the existing media category. To modify the media category, call the [ModifyMediaInfo](https://www.tencentcloud.com/document/product/266/31762?from_cn_redirect=1) API.
        * The classification hierarchy cannot exceed 4 levels.
        * The number of subcategories in each category must not exceed 500.
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
        Initiate complex adaptive bitstream processing tasks. Features include:
        1. Output HLS and DASH adaptive bitrate streams based on the specified adaptive bitrate template;
        2. The content protection solution for adaptive bitrate streams is selectable as unencrypted, Widevine, or FairPlay.
        3. Support adding opening and ending segments;
        4. The output adaptive bitrate stream can contain multilingual audio streams, each language comes from a different media file;
        5. The output adaptive bitrate stream can contain multilingual subtitle streams.

        Notes:
        1. When using an opening scene, the video stream in the opening scene media needs to align with the audio stream; otherwise, it will cause audio and video synchronization issues in the output content.
        2. If the output adaptive bitrate stream needs to include the audio of the main media, specify the FileId of the main media in the AudioSet parameter.
        3. To use subtitles, add them to the main media first via the ModifyMediaInfo API or the audio and video details page in the console.
        4. Top speed Codec and watermark are not currently supported.
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
        This API is <font color=red>no longer maintained</font>. The new version moderation template supports audio/video moderation and image moderation. For details, please see [Create Moderation Template](https://www.tencentcloud.com/document/api/266/84391?from_cn_redirect=1).
        This API is used to create a user-customized audio/video moderation template. Up to 50 templates can be created.
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
        This API is used to generate a subdomain name resolution and prompt the customer to add it to the domain name resolution for wildcard domain name and domain name retrieval ownership verification.
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
        This API is no longer maintained. The new version of the [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        Create an audio and video quality rebirth template.
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
        -Maximum supported template quantity: 100.
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
        Create a user-defined image processing template. Maximum quantity: 16. Supports up to ten operations, for example: crop - thumbnail - crop - blur - thumbnail - crop - thumbnail - crop - blur - thumbnail.
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
        This API is used to create a user-customized image sprite template. Maximum number: 16.
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
        This API is used to create a just in time transcoding template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKnowledgeBase(
            self,
            request: models.CreateKnowledgeBaseRequest,
            opts: Dict = None,
    ) -> models.CreateKnowledgeBaseResponse:
        """
        Create a knowledge base. This API is used to create a new knowledge base for Intelligent Media Assets. Each user can create up to 20 knowledge bases.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKnowledgeBase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKnowledgeBaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLLMComprehendTemplate(
            self,
            request: models.CreateLLMComprehendTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLLMComprehendTemplateResponse:
        """
        Create a large model parsing template.
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
        This API is used to create custom templates for partial features of the ProcessMediaByMPS API.
        When creating a template, fill in the MPS related parameters in JSON format in the MPSCreateTemplateParams parameter. For specific task parameter configuration methods, see the MPS task template related documentation.
        Currently supported MPS features for creating custom templates:
        1. [Audio and video enhancement](https://www.tencentcloud.com/document/product/862/118703?from_cn_redirect=1).
        2. [Media AI](https://www.tencentcloud.com/document/product/862/113756?from_cn_redirect=1)

        > Template for tasks created with this method:
        > 1. Template management is still done in the VOD platform.
        > 2. The feature is currently in beta test. If needed, you can contact us for support.
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
        This API is used to create material samples for video processing such as content recognition and inappropriate video recognition through facial feature positioning technology.
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
        This API is used to create user-defined task flow templates. Template capacity limit: 50.
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
        This API is used to create user-customized image asynchronous processing templates. Maximum number: 50. HLS format is not supported currently.
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
        This API is used to create an audio-visual quality inspection template.
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
        This API is no longer maintained. The new version of the [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        This API is used to create a video rebirth template.
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
        This API is used to create user-customized moderation templates. Maximum number: 50.
        >Template is applicable only to the ReviewAudioVideo (https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) and ReviewImage (https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1) APIs.
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
        This API is used to create a carousel playlist. Maximum quantity: 100.
        Each file in the carousel playlist can specify a source file or a transcoded file.
        The designated file must be in hls format. All playlist files should preferably maintain the same bitrate and resolution.
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
        This API is used to create a user-customized sampled screenshot template, with a maximum of 16.
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
        This API is used to generate scenario-based AIGC images. API calls incur actual fees. Refer to the VOD AIGC image generation billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#9c4dc6ff-4b3f-4b25-bf2d-393889dfb9ac). The feature uses postpaid settlement. For daily billing customers, usage on the day is billed on the second day. For monthly billing customers, the previous month's usage fees are billed on the 1st of the next month.
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
        This API is used to generate scenario-based AIGC images. <b>The API is in beta. If needed, please [contact us](https://www.tencentcloud.com/online?from_cn_redirect=1-service?from=sales_sales&source=PRESALE). API calls will incur actual fees.</b>
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
        This API is used to create user-customized specified time point screenshot templates. Maximum quantity: 16.
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
        1. When a user enables the VOD service, storage in partial regions is enabled by default. If necessary, the user can use this API to enable storage in other regions.
        2. The DescribeStorageRegions API can query all storage regions and opened regions.
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
        This API is used to create a VOD application.
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
        This API is <font color='red'>no longer maintained</font>. The new version of player signature no longer uses player configuration templates. For details, please see [Player Signature](https://www.tencentcloud.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to create player configurations. Maximum number: 100.
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
        This API is used to create custom transcoding templates. Maximum quantity: 100.
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
        This API is used to add acceleration domain names to VOD. A user can add up to 20 acceleration domain names.
        1. After the domain name is successfully added, VOD will deploy the domain name. It takes about 2 minutes for the domain name to change from deployment status to online status.
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
        This API is used to create a user-defined watermark template with an upper limit of 1000.
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
        This API is used to create keyword samples in batches. Samples are used for video processing such as inappropriate content recognition and content recognition through OCR and ASR technology.
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
        This API is used to delete a user-defined audio and video content analysis template.

        Note: Templates with IDs below 10000 are preset templates and cannot be deleted.
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
        This API is used to delete a user-defined audio and video content recognition template.
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
        Deletes an adaptive bitrate streaming template
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
        This API is used to delete advanced custom AIGC subjects.
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
        Deletes an AIGC API Token. The AIGC quota associated with the Token will also be deleted.
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
        This API is used to delete AIGC quota configurations. Once deleted, AIGC task initiation will no longer be limited.

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
        Delete a CDN domain
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
        Delete the log topic enabled for VOD.
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
        * A category can be deleted only when it has no subcategories and no media association.
        * Otherwise, execute [delete media](https://www.tencentcloud.com/document/product/266/31764?from_cn_redirect=1) and subcategories first, then delete the category;
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
        This API is <font color=red>no longer maintained</font>. The new version of the moderation template supports video moderation and image moderation. For details, please see [Delete Moderation Template](https://www.tencentcloud.com/document/api/266/84390?from_cn_redirect=1).
        Delete a user-customized audio/video moderation template.
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
        This API is <font color=red>no longer maintained</font>. The new version of [Audio and Video Quality Rebirth](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) interface uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        This API is used to delete an audio and video quality rebirth template.
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
        This API is used to delete a title and trailer template.
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
        This API is used to delete a user-customized image processing template.
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
        This API is used to delete an image sprite template.
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
        This API is used to delete a just in time transcoding template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteKnowledgeBase(
            self,
            request: models.DeleteKnowledgeBaseRequest,
            opts: Dict = None,
    ) -> models.DeleteKnowledgeBaseResponse:
        """
        Delete a knowledge base.
        After the API is called, the knowledge base will be in the "Deleting" status, and the deletion operation will be performed in the backend.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteKnowledgeBase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteKnowledgeBaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLLMComprehendTemplate(
            self,
            request: models.DeleteLLMComprehendTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLLMComprehendTemplateResponse:
        """
        Delete a customized large model parsing template.

        Note: Templates with IDs below 10000 are system-preset templates and cannot be deleted.
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
        * Delete media and its corresponding video processing files (raw files, such as transcoded videos, sprite sheets, screenshots, WeChat video releases, etc.);
        * You can individually delete the source file, transcoded video, or WeChat video release under a specified video file ID.
        * Note: After the original file is deleted, you cannot initiate any video processing operations such as transcoding or WeChat publishing.
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
        This API is used to delete material samples based on figure IDs.
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
        This API is used to delete a user-defined task flow template.
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
        This API is used to delete a user-customized image asynchronous processing template.

        Note: Templates with IDs below 10000 are system-preset templates and cannot be deleted.
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
        This API is used to delete an audio-visual quality inspection template.
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
        This API is <font color=red>no longer maintained</font>. The new version of [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        Deletes a video rebirth template.
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
        Delete a user-customized moderation template.
        >Template is applicable only to the ReviewAudioVideo (https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) and ReviewImage (https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1) APIs.
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
        This API is used to delete a carousel playlist.
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
        This API is used to delete a user-customized sampled screenshot template.
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
        This API is used to delete a user-customized specified time point screenshot template.
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
        This API is <font color='red'>no longer maintained</font>. The new version of player signature no longer uses player configuration templates. For details, please see [Player Signature](https://www.tencentcloud.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to delete a player configuration.
        *Note: The system preset player configuration cannot be deleted.*
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
        This API is used to delete VOD acceleration domains.
        1. Before domain deletion, acceleration in all regions must be disabled.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVodDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVodDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVoice(
            self,
            request: models.DeleteVoiceRequest,
            opts: Dict = None,
    ) -> models.DeleteVoiceResponse:
        """
        Delete a specified voice by voice ID. This operation cannot be undone, and the voice cannot be used for subsequent APIs. Only voices for this account can be deleted. System preset voices cannot be deleted.

        Note: Newly designed or cloned voice types cannot be deleted before activation (not found means non-operational). They are activated only after the new voice type is used for TTS once.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWatermarkTemplate(
            self,
            request: models.DeleteWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteWatermarkTemplateResponse:
        """
        This API is used to delete a user-customized watermark template.
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
        This API is used to get the detail list of audio and video content analysis templates based on their unique identifiers. The returned results include all eligible user-defined audio and video content analysis templates and [system preset audio/video content analysis templates](https://www.tencentcloud.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.88.86.E6.9E.90.E6.A8.A1.E6.9D.BF).
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
        This API is used to get the list of details of audio/video content recognition templates based on their unique IDs. The returned results include all eligible user-defined audio/video content recognition templates and system preset audio/video content recognition templates.
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
        This API is used to query adaptive bitrate streaming templates, and the pagination query is supported based on conditions.
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
        This API is used to retrieve advanced custom AIGC subjects.
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
        This API is used to query the list of AIGC API Tokens. Data sync has a delay after creation or deletion. The latest data can be queried after about 30 seconds.
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
        This API is used to retrieve AIGC face information. Note that calling this API incurs face recognition fees. Refer to the billing documentation (https://www.tencentcloud.com/document/product/266/95125?from_cn_redirect=1#96b3b59a-f9e1-49e9-966a-bedb70a4bf12).
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
        This API is used to query AIGC quota configurations.
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
        This API is used to return AIGC statistical information within a specified time range.
        1. AIGC statistical data from the last 365 days can be queried.
           2. The query time span should not exceed 90 days.
        3. If the query time span exceeds 1 day, the data returned is at day granularity. Otherwise, the data returned is at 5-minute granularity.
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
        * Obtain all classification information of the user.
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
        This API is used to query the list of rotating image templates based on conditions with paging.
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
        This API is used to query user-customized digit watermark templates.
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
        Queries an on-demand domain name.
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
        This API is used to query CDN bandwidth, traffic, and other stats for a VOD domain.
        * The time span between the query start time and end time should not exceed 90 days.
        * You can query data in different service regions.
        * Statistical data support is available for querying specified regions and carriers within the Chinese mainland.
        * Playback statistics only target VOD domains, excluding EdgeOne domain distribution.
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
        This API is used to query VOD CDN traffic, bandwidth, and other stats.
        1. CDN usage data is retained on the system side for 13 months. You can only query usage data from the most recent 365 days through the API. To retrieve historical usage data beyond 365 days, contact us.
           2. The query time span should not exceed 90 days.
        3. You can specify the time granularity of usage data, supporting 5-minute, 1-hour, and 1-day granularities.
        4. Traffic is the total traffic within the query time granularity, and bandwidth is the peak bandwidth within the query time granularity.
        5. Playback statistics only target VOD domains, excluding EdgeOne domain distribution.
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
        Queries CLS log sets created by VOD.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSLogsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSLogsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCLSPushTargets(
            self,
            request: models.DescribeCLSPushTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeCLSPushTargetsResponse:
        """
        Queries the destination topic for log delivery under an on-demand domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSPushTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSPushTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCLSTopics(
            self,
            request: models.DescribeCLSTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeCLSTopicsResponse:
        """
        Queries the list of CLS log topics created by VOD.
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
        This API is used to query the download URL of CDN access logs for VOD domains, excluding EdgeOne origin-pull to VOD domains.
        1. This API is used to query CDN log download links for the most recent 30 days.
        2. By default, CDN generates a log file per hour. If there is no CDN access in an hour, no log file is generated.
        3. The CDN log download link has a validity of 24 hours.
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
        This API returns client upload acceleration statistics within a specified time range.
        1. Can query client upload acceleration statistics data for the most recent 365 days.
           2. The query time span should not exceed 90 days.
        3. If the query time span exceeds 1 day, the data is returned at a granularity of 1 day. Otherwise, the data is returned at a granularity of 5 minutes.
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
        This API is <font color=red>no longer maintained</font>. The new moderation template supports audio/video moderation and image moderation. For details, please see [Query Moderation Template List](https://www.tencentcloud.com/document/api/266/84389?from_cn_redirect=1).
        This API is used to retrieve the list of details of audio/video moderation templates based on their unique identifiers. The returned results include all eligible custom templates and system preset content review templates (https://www.tencentcloud.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.AE.A1.E6.A0.B8.E6.A8.A1.E6.9D.BF).
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
        Query the carousel current playlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCurrentPlaylist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCurrentPlaylistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDailyMediaPlayStat(
            self,
            request: models.DescribeDailyMediaPlayStatRequest,
            opts: Dict = None,
    ) -> models.DescribeDailyMediaPlayStatResponse:
        """
        This API is used to query the daily playback statistics within a specified date range.
        * Playback statistics for the past one year can be queried.
        * The time span between the start date and end date can be up to 90 days.
        * Playback statistics only target VOD domains (i.e., distribution from EdgeOne domain names is not included in playback statistics).
        * Due to data delay, you are advised to query the usage data of the previous day after 12:00 noon the next day.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDailyMediaPlayStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDailyMediaPlayStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDailyMostPlayedStat(
            self,
            request: models.DescribeDailyMostPlayedStatRequest,
            opts: Dict = None,
    ) -> models.DescribeDailyMostPlayedStatResponse:
        """
        This API is used to query daily playback statistics of the Top 100 media files.
        * Playback statistics from the past one year can be queried.
        * You can query by playback times or traffic volume.
        * Statistical description of the number of plays:
        1. HLS file: The number of plays is counted when an M3U8 file is accessed, but not when a TS file is accessed.
        2. Other files (for example, MP4 files): If a playback request includes the range parameter and the start parameter of range is not equal to 0, the number of plays is not counted. In other cases, the number of plays is counted.
        * Playback statistics only target VOD domains (i.e., distribution from EdgeOne domain names is not included in playback statistics).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDailyMostPlayedStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDailyMostPlayedStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDailyPlayStatFileList(
            self,
            request: models.DescribeDailyPlayStatFileListRequest,
            opts: Dict = None,
    ) -> models.DescribeDailyPlayStatFileListResponse:
        """
        This API is used to query the download address of playback statistics files.
        * Can query the playback statistics file download link for the past one year. The time span between the start date and end date of the query is no more than 90 days.
        VOD analyzes and processes the CDN request logs of the previous day to generate playback statistics files.
        The playback statistics file contains statistical information such as the number of plays and total traffic of media files.
        * Statistical description of the number of plays:
        1. HLS file: The number of plays is counted when an M3U8 file is accessed, but not when a TS file is accessed.
        2. Other files (for example, MP4 files): If a playback request includes the range parameter and the start parameter of range is not equal to 0, the number of plays is not counted. In other cases, the number of plays is counted.
        * Statistics of playback devices: If a playback request includes the UserAgent parameter and the UserAgent contains identifiers such as Android or iPhone, it is counted as a mobile playback. Otherwise, it is counted as a PC playback.
        * Playback statistics only target VOD domains (i.e., distribution from EdgeOne domain names is not included in playback statistics).
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
        * Distribution domain name and protocol, i.e., the domain name and protocol in the media file distribution URL. Media files are distributed based on the default distribution configuration.
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
        This API is used to query DRM key provider information.
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
        This API is <font color=red>no longer maintained</font>. The new version of [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        This API is used to obtain the audio and video quality regeneration template list.
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
        Tencent Cloud Video on Demand (VOD) provides customers with media upload, media management, media processing, and other services. During or after these services are executed, VOD also provides various event notifications, helping developers detect service processing status and perform next business operations.

        Developers can use this API to query the current configuration of the event notification receiving method, recipient address, and which events have callback notification enabled.

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
        Used to get file attributes asynchronously.
        -Currently only support getting the Md5 and Sha1 of the source file.
        -For HLS or DASH input files, only the attributes of index files are retrieved.
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
        This API is used to search for title and trailer template lists.
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
        This API is used to query the list of image processing templates based on conditions with paging.
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
        This API is used to return the daily image review usage information within the specified query time range.
        1. Image moderation statistics data from the last 365 days can be queried.
           2. The query time span should not exceed 90 days.
        3. If the query time span exceeds 1 day, data at a day granularity is returned. Otherwise, data at a 5-minute granularity is returned.
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
        Query image sprite templates based on conditions with paging.
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
        This API is used to search the instant transcoding template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJustInTimeTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJustInTimeTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKnowledgeBases(
            self,
            request: models.DescribeKnowledgeBasesRequest,
            opts: Dict = None,
    ) -> models.DescribeKnowledgeBasesResponse:
        """
        Queries the knowledge base list. Returns all knowledge base information under the specified user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKnowledgeBases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKnowledgeBasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLLMComprehendTemplates(
            self,
            request: models.DescribeLLMComprehendTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLLMComprehendTemplatesResponse:
        """
        According to the unique identifier of the large model parsing template, retrieve the large model parsing template detail list. The returned results include all user-customized large model parsing templates that meet the conditions.
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
        This API is used to return the daily License request count within the specified query time range.
        1. License request count statistics from the last 365 days can be queried.
           2. The query time span should not exceed 90 days.
        3. If the query time span exceeds 1 day, data is returned at a daily granularity. Otherwise, data is returned at a 5-minute granularity.
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
        This API is used to query user-customized media processing service task templates.
        To query the template list, fill in the MPS related parameters in MPSDescribeTemplateParams in JSON format. For specific task parameter configuration methods, see the MPS task template documentation.
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
        1. This API can obtain multiple types of info of multiple media files, including:
        1. basicInfo: including media name, category, playback address, cover image, etc.
        2. Meta information (metaData): including size, duration, video stream information, audio stream information, etc.
        3. Transcoding result information (transcodeInfo): including media addresses, video stream parameters, and audio stream parameters of various specifications generated for this media.
        4. Animated graphics info (animatedGraphicsInfo): the animated graphics info after converting a video to GIF (for example, gif).
        5. sampleSnapshotInfo: Screenshot information after sampling a video.
        6. Sprite image information (imageSpriteInfo): the sprite image information after capturing sprite images from a video.
        7. snapshotByTimeOffsetInfo: screenshot information after taking screenshots of the video at specified time points.
        8. Video timestamp information (keyFrameDescInfo): Dotting information set for the video.
        9. Adaptive Bitrate Streaming information (adaptiveDynamicStreamingInfo): including specification, encryption type, packaging format and other related information.
        10. Review information (reviewInfo): includes media moderation and media cover review information.
        2. You can specify to only return partial information in the response.
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
        This API is used to query playback data of media files by specified time granularity.
        * Playback statistics for the past one year can be queried.
        Time granularity: hr. The max span between the end time and start time is 7 days.
        Time granularity is day, and the maximum span between the end time and start time is 90 days.
        * Playback statistics only target VOD domains, excluding EdgeOne domain distribution.
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
        1. Video processing usage data is retained for 13 months in the data system. You can only query usage data from the most recent 365 days through the interface. To retrieve historical usage data beyond 365 days, contact us.
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
        This API is used to query material sample information by material ID, name, or tag with paging.
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
        This API is used to search the task flow template detail list based on the task flow template name.
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
        This API is used to obtain the template details list for asynchronous image processing based on the Template Unique Identifier. The returned results include all eligible user-customized asynchronous image processing templates.
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
        This API is used to query the audio and video quality detection template list.
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
        This API is <font color=red>no longer maintained</font>. The new version of the [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        This API is used to query the video rebirth template list.
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
        <b>This API is not recommended. Use [DescribeMediaProcessUsageData](https://www.tencentcloud.com/document/product/266/41464?from_cn_redirect=1) as an alternative.</b>

        This API is used to return the daily duration data of video content intelligent identification within the specified query time range. Measurement unit: seconds.

        1. Intelligent video content identification duration statistics from the last 365 days can be queried.
        2. The query time span should not exceed 90 days.
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
        This API is used to get the moderation template list.
        >Template is applicable only to the [ReviewAudioVideo](https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) and [ReviewImage](https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1) APIs.
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
        This API is used to get the carousel playlist list.
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
        This API is used to query sampled screenshot templates based on conditions with paging.
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
        This API is used to query specified time point screenshot templates based on conditions with paging.
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
        Queries storage space usage and number of files.
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
        This API is used to return the VOD storage space used within a specified time range, in bytes.
        1. Storage usage data is reserved on the system side for 13 months. You can only query usage data from the most recent 365 days through the API. If you need to retrieve historical usage data beyond 365 days, contact us;
        2. The query time span should not exceed 90 days.
        3. The query span at a minute granularity should not exceed 7 days;
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
        This API is used to:
        1. Query the list of all storage campuses available for on-demand activation.
        2. Query the list of opened parks.
        3. Query the storage campus used by default.
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
        This API is used to get the application list of the current account.
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
        This API is <font color='red'>no longer maintained</font>. The new version of player signature no longer uses player configuration templates. For details, please see [Player Signature](https://www.tencentcloud.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to query player configurations based on conditions with paging.
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
        This API is used to query the details of the task execution status and results by task ID (tasks submitted within the last 3 days can be queried).
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
        * This API is used to query the task list.
        * When the list contains a large amount of data, a single API call cannot pull the entire list. You can use the ScrollToken parameter to pull in batches.
        * Only tasks from the last three days (72 hours) can be queried.
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
        This API is used to retrieve the transcoding template detail list based on the transcoding template unique identifier. The returned results include all eligible custom templates and [system preset transcoding templates](https://www.tencentcloud.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF).
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
        This API is used to query the list of on-demand video domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVodDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVodDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVoices(
            self,
            request: models.DescribeVoicesRequest,
            opts: Dict = None,
    ) -> models.DescribeVoicesResponse:
        """
        Queries the available timbre list under the current account, supporting filtering by optional conditions such as voice ID, type, name, gender, age, language, tag, and scenario.

        Note: Newly designed or cloned voice types cannot be queried before activation. They are activated only after the new voice type is used for TTS once.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVoices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVoicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWatermarkTemplates(
            self,
            request: models.DescribeWatermarkTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeWatermarkTemplatesResponse:
        """
        This API is used to query user-customized watermark templates, and the pagination query is supported based on conditions.
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
        This API is used to paging query keyword sample info by scenario, keyword, and tag.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWordSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWordSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DesignVoiceAsync(
            self,
            request: models.DesignVoiceAsyncRequest,
            opts: Dict = None,
    ) -> models.DesignVoiceAsyncResponse:
        """
        This API is used to trigger a voice design task. It generates a custom voice based on a natural language description. You can specify a voice profile at the same time, such as name, gender, age, language, tag, and scenario. If trial text is attached during submission, an audio audition is generated after task completion. Voice design is an asynchronous task. The voice ID is generated after task completion.
        """
        
        kwargs = {}
        kwargs["action"] = "DesignVoiceAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DesignVoiceAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditMedia(
            self,
            request: models.EditMediaRequest,
            opts: Dict = None,
    ) -> models.EditMediaResponse:
        """
        This API is used to edit a video, such as clipping and splicing, to generate a new on-demand video. Editing features include:

        1) Edit a file in VOD to generate a new video.
        2) Splice multiple on-demand files to generate a new video.
        3) Edit multiple files in on-demand video and then splice them to generate a new video;
        4. Directly generate a new video for one of the streams in VOD;
        5. Edit one of the on-demand streams to generate a new video;
        6) Splice multiple on-demand streams to generate a new video.
        7) Edit multiple streams in VOD and then splice them to generate a new video.

        For the generated new video, you can also specify whether to execute task flow on the generated video.

        When editing or splicing a live stream, please ensure the stream has ended before operating. Otherwise, the generated video may be incomplete.

        If event notification is used, its type is [video editing completed](https://www.tencentcloud.com/document/product/266/33794?from_cn_redirect=1).
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
        This API is <font color=red>no longer maintained</font>. Please use the new version of APIs [audio and video quality revival](https://www.tencentcloud.com/document/api/266/102571?from_cn_redirect=1).
        Use a template to initiate audio and video quality revival.
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
        This API is used to trigger an audio and video quality regeneration task for on-demand audio-video media.
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
        This API is only used for special scenarios of customized development. Do not call this API unless VOD customer service proactively informs you that you need to use it.
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
        If you need source tracing for piracy, see Ghost Watermark (https://www.tencentcloud.com/document/product/266/94228?from_cn_redirect=1).
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
        If source tracing for piracy is required, ghost watermark is recommended for use (https://www.tencentcloud.com/document/product/266/94228?from_cn_redirect=1).
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
        Quickly splice and edit HLS videos in VOD to generate new media in HLS format.

        Quickly splice or edit the generated video to generate a new FileId and solidify it. After successful solidification, the new video file exists independent of the original input video and is not affected by the deletion of the original video.

        <font color='red'>Note:</font> Enable reception of editing solidification event notifications through the ModifyEventConfig API. After successful solidification, you will receive a PersistenceComplete event notification. Before receiving this event notification, you should not delete or transition the original input video to colder storage. Otherwise, playback of the video generated by splicing and clipping may encounter exceptions.
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
        * After media blocking, except for VOD console preview, accessing URLs of various video resources (raw files, transcoding output files, screenshots, etc.) for other scenarios will return 403.
        It takes about 5 to 10 minutes for the ban/unban operation to take effect across the entire network.
        * Note: Media blocking can only be performed on media stored in standard storage and infrequent storage. Media in infrequent storage must be stored for at least 30 days. If deleted early or changed to another storage class, it is still billed for 30 days. If you block media in infrequent storage and its infrequent storage duration is less than 30 days, early deletion fees will occur. At the same time, after blocking, the infrequent storage duration of the media restarts from the current time. If the media is deleted or changed to another storage class before reaching 30 days, early deletion fees will also occur. For example, media 001 has been in infrequent storage for 10 days. If you block 001 at this point, infrequent storage is still billed for 30 days (early deletion billing duration: 30 - 10 = 20 days). After blocking, the infrequent storage duration of 001 restarts. If 001 is deleted on day 5 after blocking, infrequent storage is still billed for 30 days (early deletion billing duration: 30 - 5 = 25 days). The actual infrequent storage duration of 001 is 10 + 5 = 15 days, while the billed infrequent storage duration is 10 + 20 (early deletion billing) + 5 + 25 (early deletion billing) = 60 days.
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
        Perform operations on the carousel current playlist. Supported operations: <li> Insert: Insert a program into the current playlist.</li><li> Delete: Delete a program in the playlist.</li>
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
        Used to import AI analysis results into the knowledge base.
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
        This API is used to trigger an audio and video quality inspection task for on-demand audio-video media.
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

        **This API is only available in "FileID+Path" mode.**
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
        Live streaming instant editing means that during live streaming (i.e., before the live stream has ended), customers can select a segment from the live stream content and generate a new video (in HLS format) in real time. Developers can share it instantly or save it for long-term preservation.

        Tencent Cloud VOD supports two instant clipping modes:
        - Clip solidification: Save the edited video as a standalone video with an independent FileId; suitable for long-term preservation of highlights.
        - Editing is not solidified: The edited video is attached to the live streaming recording file and has no standalone FileId. It is suitable for scenarios where highlight clips are shared temporarily.

        Note:
        - The premise for using the live stream clipping feature is that the target live stream has [time shifting](https://www.tencentcloud.com/document/product/267/32742?from_cn_redirect=1) enabled.
        -Live streaming Instant Editing is based on the m3u8 file generated by live recording, so its minimum editing precision is one ts slicing. Second-level or more precise editing precision cannot be achieved.
        -Since stream disconnection may occur during live streaming, the actual video duration generated by editing might not be the same as expected. For example, if you edit a live stream from 2018-09-20T10:30:00Z to 2018-09-20T10:40:00Z, and a stream disconnection occurred during this time interval, the duration of the returned media asset file will be less than 10 minutes. In such cases, you can perceive it through the output parameter <a href="#p_segmentset">SegmentSet</a>.

        ### Edit solidification
        Editing solidification refers to saving an edited video as an independent video (with an independent FileId). Its lifecycle is not subject to any impact from the original live recorded video (even if the original recorded video is deleted, the clipping result will not be affected). It can also be transcoded, published on WeChat, or undergo other secondary processing.

        For example, a complete football match may have a live recording of over 2 hours. For cost savings, the customer can store the original video for 2 months, but can specify longer storage for the highlight reel from live stream clipping. You can also perform additional on-demand operations on the highlight reel, such as transcoding and publishing on WeChat. In this case, you can choose the live stream clipping and persistence solution.

        The advantage of solidified editing is that its lifecycle is independent of the original recorded video, allowing for separate management and long-term preservation.

        <font color='red'>Note:</font> If solidification is specified when editing, enable reception of editing solidification event notifications through the ModifyEventConfig API. After successful solidification, you will receive a PersistenceComplete event notification. Before receiving this event notification, you should not delete or archive the live video recording. Otherwise, playback of the generated video may be abnormal.

        ### Editing is not solidified
        The so-called "editing is not solidified" means that the result of editing (m3u8 file) shares the same TS segments with the live video recording. The newly generated video is not an independent and complete video (no standalone FileId, only a playback URL), and its valid period is consistent with that of the full video from live recording. Once the video from live recording is deleted, the clip will also become unplayable.

        Editing is not solidified. Since the clipping result is not an independent video, it is not included in the video management of on-demand media assets. For example, the total number of videos in the console does not count this video clip. It is also unable to separately perform any video processing operation on this clip, such as transcoding or publishing on WeChat.

        The advantage of editing not being solidified is that the editing operation is relatively "lightweight" and will not generate additional storage overhead. However, its shortcoming is that the lifecycle is identical to the original recorded video, and it cannot be further transcoded for video processing.
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
        Manage initiated tasks.
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
        This API is used to modify a user-defined audio and video content analysis template.

        Note: Templates with IDs below 10000 are preset templates and are not allowed to be modified.
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
        This API is used to modify a user-defined audio and video content recognition template.
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
        Modifying an Adaptive Bitrate Streaming Template
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
        This API is used to edit AIGC quota configuration. Quota usage starts accumulating when the quota feature is enabled. Once the quota is reached, AIGC features will no longer be usable.

        Since AGC content generation is an async task, real-time usage data cannot be obtained. Therefore, quota limits result in some errors, and precise control over the set limit cannot be achieved.
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
        Modify a custom animated image generating template.
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
        This API is used to modify CDN domain configuration.
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
        Modifies media classification attributes.
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
        This API is no longer maintained. The new version of the moderation template supports video and image moderation. For details, please see [Modify Moderation Template](https://www.tencentcloud.com/document/API/266/84388?from_cn_redirect=1).
        Modify a user-customized audio/video moderation template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContentReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDefaultDistributionConfig(
            self,
            request: models.ModifyDefaultDistributionConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDefaultDistributionConfigResponse:
        """
        This API is used to modify the default distribution configuration.
        * Distribution domain name and distribution protocol, which are the domain name and protocol in the media file distribution URL. Media files are distributed based on the default distribution configuration.
        Playback key, used to calculate player signature.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDefaultDistributionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDefaultDistributionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDefaultStorageRegion(
            self,
            request: models.ModifyDefaultStorageRegionRequest,
            opts: Dict = None,
    ) -> models.ModifyDefaultStorageRegionResponse:
        """
        This API is used to set the default storage region. If no region is specified during file upload, files are uploaded to the default region.
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
        This API is <font color=red>no longer maintained</font>. The new version of the [audio and video quality revival](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        Modify an audio and video quality rebirth template.
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
        Tencent Cloud VOD provides customers with media upload, media management, media processing, and other services. During or after the execution of these services, Tencent Cloud VOD also provides various event notifications, allowing developers to sense the service processing status and perform the next business operation.

        Developers can call this API to:
        - Set the type for receiving callback notifications. There are two types: [HTTP callback notification](https://www.tencentcloud.com/document/product/266/33779?from_cn_redirect=1) and [Reliable Notification Based on Message Queue](https://www.tencentcloud.com/document/product/266/33779?from_cn_redirect=1).
        - For [HTTP callback notification](https://www.tencentcloud.com/document/product/266/33779?from_cn_redirect=1), you can set the address for 3.0 format callback. For details on 3.0 format callback, see [Historical format callback](https://www.tencentcloud.com/document/product/266/33796?from_cn_redirect=1).
        -Select receipt or ignore settings for notification events of a specific event service.
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
        Modify a title and trailer template.
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
        Modify a user-customized image sprite template.
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
        Modify an instant transcoding template.
        -Note: Once a just in time transcoding template is created, modification is not recommended. If parameter modification is needed, adding a new template is recommended.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyKnowledgeBase(
            self,
            request: models.ModifyKnowledgeBaseRequest,
            opts: Dict = None,
    ) -> models.ModifyKnowledgeBaseResponse:
        """
        Modify a knowledge base. The name and/or description of the knowledge base can be modified. At least one of the Name or Description fields is required.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyKnowledgeBase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyKnowledgeBaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLLMComprehendTemplate(
            self,
            request: models.ModifyLLMComprehendTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLLMComprehendTemplateResponse:
        """
        Modifies a large model parsing template
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
        When modifying a template, fill in the MPS related parameters in JSON format into the MPSModifyTemplateParams parameter. For task parameter configuration methods, refer to the MPS task template documentation.
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
        This API is used to modify the attributes of a media file, including category, name, description, tag, expiration time, dotting information, video cover, and subtitle information.
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
        Modify the storage type of media files.
        When the file storage type is standard storage, it can be modified to the following types:
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
        This API is used to modify material sample information based on the material ID, including the modification of the name and description, as well as the addition, deletion, and reset of facial features and tags. The deletion of facial features must ensure at least 1 image remains. Otherwise, please use the reset operation.
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
        This API is used to modify a user-customized asynchronous image processing template.

        Note: Templates with IDs below 10000 are system-preset templates and are not allowed to be modified.
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
        Modifies an audio and video quality detection template.
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
        This API is <font color=red>no longer maintained</font>. The new version of the [Audio and Video Quality Rebirth](https://www.tencentcloud.com/document/product/266/102571?from_cn_redirect=1) API uses preset templates. For details, see [Audio and Video Quality Rebirth Template](https://www.tencentcloud.com/document/product/266/102586?from_cn_redirect=1#50604b3f-0286-4a10-a3f7-18218116aff7).
        Modify a video rebirth template.
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
        Modify a user-customized moderation template.
        >Template is applicable only to the [ReviewAudioVideo](https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) and [ReviewImage](https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1) APIs.
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
        This API is used to modify a carousel playlist.
        After modification, only new playback requests will take effect. Users already playing can still play the original playlist within 7 days.
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
        Modify a custom sampled screenshot template.
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
        Modify a user-customized specified time point screenshot template.
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
        This API is used to change application information, but the default application info is not allowed to be modified.
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
        This API is used to enable or disable an application. A disabled application will have its corresponding domain blocked and console access restricted.
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
        This API is <font color='red'>no longer maintained</font>. The new version of player signature no longer uses player configuration templates. For details, please see [Player Signature](https://www.tencentcloud.com/document/product/266/45554?from_cn_redirect=1).
        This API is used to modify player configurations.
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
        Modify the information of a custom transcoding template.
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
        This API is used to modify the acceleration region of a VOD domain.
        1. The acceleration region can be modified only when the domain name deployment state is Online.
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
        This API is used to modify domain name configuration, including hotlink protection configuration.
        1. The domain name configuration can be modified only when the domain name deployment state is Online.
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
        This API is used to modify a user-defined watermark template. The watermark type cannot be modified.
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
        This API is used to modify the scenario and tags of a keyword. The keyword itself cannot be modified. If modification is needed, delete and rebuild it.
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
        When uploading HLS videos, this API parses the index file content and returns a list of shard files to be uploaded. The shard file path must be a relative path in the current directory or subdirectory. It cannot be a URL or an absolute path.
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
        This API is used to process image processing tasks.
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
        This API is used to initiate processing tasks for audio-video media in VOD, with features including:
        1. Video transcoding (watermarked);
        2. Animated image generating;
        3. Screenshot taking at specified time points;
        4. Sampled screenshot taking;
        5. Capture CSS sprites for videos;
        6. Capture a frame from a video as the cover.
        7. Transcoding to adaptive bitrate streaming and encrypting;
        8. Content review (offensive content, unsafe information, inappropriate information). It is <font color=red>not recommended</font> to use this API to initiate it. [Audio/Video Moderation (ReviewAudioVideo)](https://www.tencentcloud.com/document/api/266/80283?from_cn_redirect=1) or [Image Moderation (ReviewImage)](https://www.tencentcloud.com/document/api/266/73217?from_cn_redirect=1) is recommended.
        9. Content analysis (tag, categorization, cover, frame tagging) is not supported for HLS format currently.
        10. Content recognition (video intro and outro, human face, full text, text keyword, full speech, speech keyword, object).

        If event notification is used, the event notification type is task flow status change (https://www.tencentcloud.com/document/product/266/9636?from_cn_redirect=1).
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
        Use the media processing capability of the media processing service (MPS) to initiate media processing for videos in video-on-demand.
        Currently supported MPS features:
        1. Smart subtitling: This feature supports processing offline audio files, video files, and live streams. It can extract source language captions from videos through ASR speech recognition or OCR text recognition, and implement multilingual translation. View details in the Access Guide (https://www.tencentcloud.com/document/product/266/131210?from_cn_redirect=1).
        2. Intelligent erasure: It can blur, mosaic, or seamlessly process elements such as logos, subtitles, human faces, and license plates in video footage, making it easy to spread and share content. The new video generated by this task will be assigned a new FileId and stored in a sub-application of the VOD platform. View details in the Access Guide (https://www.tencentcloud.com/document/product/266/131211?from_cn_redirect=1).
        3. AI analysis: This feature supports one-stop translation (https://www.tencentcloud.com/document/product/266/131212?from_cn_redirect=1), highlights (https://www.tencentcloud.com/document/product/266/131213?from_cn_redirect=1), LLM video summary (https://www.tencentcloud.com/document/product/266/131214?from_cn_redirect=1), LLM audio/video understanding (https://www.tencentcloud.com/document/product/266/131215?from_cn_redirect=1), intelligent splitting (https://www.tencentcloud.com/document/product/266/131216?from_cn_redirect=1), intelligent landscape-to-portrait (https://www.tencentcloud.com/document/product/266/131217?from_cn_redirect=1), video deduplication (https://www.tencentcloud.com/document/product/266/131218?from_cn_redirect=1), and other features.


        > Video processing task initiated this method:
        > 1. Query task status and results on the VOD platform. Use [DescribeTaskDetail](https://www.tencentcloud.com/document/product/266/33431?from_cn_redirect=1) or [DescribeTasks](https://www.tencentcloud.com/document/product/266/33430?from_cn_redirect=1) to query tasks.
        > 2. The usage and bills of related features will be provided on the PS platform. Before using this feature, start by enabling Media Processing Service (MPS) in the console. For the activation method, see the preliminary operations in the access documentation.
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
        Use a task flow template to initiate processing tasks for videos in VOD.
        There are two ways to create a task flow template:
        1. Create and modify a task flow template in the console;
        2. Create a task flow template through the task flow template API.

        If event notification is used, the type of event notification for tasks other than audio/video moderation tasks is task flow status change (https://www.tencentcloud.com/document/product/266/9636?from_cn_redirect=1); the type of event notification for audio/video moderation tasks is audio/video moderation completed (https://www.tencentcloud.com/document/product/266/81258?from_cn_redirect=1).
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
        This API is <font color='red'>no longer maintained</font>. Please use the [ProcessMedia](https://www.tencentcloud.com/document/product/862/37578?from_cn_redirect=1) API of MPS and specify the video URL in the input parameter InputInfo.UrlInputInfo.Url.
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
        * This API is used for the business server to get event notifications via reliable callback (https://www.tencentcloud.com/document/product/266/33779?from_cn_redirect=1#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83).
        * The API uses long polling mode. If there are unconsumed events on the server, they will be returned to the requester immediately. If there are no unconsumed events, the request will be suspended in the background until a new event occurs.
        * The request can be suspended for up to 5 seconds. It is advisable to set the timeout to 10 seconds for the requester;
        * Event notifications that are not pulled are retained for up to 4 days. Notifications exceeding this time limit may be purged.
        * If this API returns an event, the caller must call the [Confirm Event Notification](https://www.tencentcloud.com/document/product/266/33434?from_cn_redirect=1) API within <font color="red">30 seconds</font> to confirm that the event notification has been processed. Otherwise, the event notification will be pulled again after <font color="red">30 seconds</font>.
        * Currently, a maximum of 16 event notifications can be obtained per API call.
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
        This API is used to pull a video from the network to the VOD platform.
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
        1. Preheat a specified URL list.
        2. The domain name of the URL must be registered in VOD.
        3. A single request can specify up to 20 URLs.
        4. The default prefetch quota is 10,000 URLs per day.
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
        The API is <font color=red>no longer maintained</font>. Please use the new version of APIs [Audio and Video Quality Revival](https://www.tencentcloud.com/document/api/266/102571?from_cn_redirect=1).
        This API is used to initiate audio and video quality revival.
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
        This API is <font color=red>no longer maintained</font>. Please use the new version of APIs [audio and video quality revival](https://www.tencentcloud.com/document/api/266/102571?from_cn_redirect=1).
        Use a template to initiate video rebirth.
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
        1. Refreshes a specified URL list.
        2. The domain name of the URL must be registered in VOD.
        3. A maximum of 20 URLs can be specified per request.
        4. The default refresh quota is 100,000 URLs per day.
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
        Removes watermarks intelligently
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
        Reset the content of the user-defined task flow template.
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
        When the storage type of a media file is archive storage or deep archive storage, it is inaccessible. If you need access, call this API to unfreeze it. The unfrozen media file is temporarily accessible and becomes inaccessible after the validity period expires.
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
        This API is used to initiate moderation tasks for on-demand audio-video media, intelligently detecting violative content in video footage, text in images, text in speech, and sounds.

        If event notification is used, its type is [audio/video moderation completed](https://www.tencentcloud.com/document/product/266/81258?from_cn_redirect=1).
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
        Initiate a review task for image files in on-demand video for offensive, unsafe, and inappropriate information.

        <li>Supported image file size: file < 5M;</li>
        <li>Supported image file resolution: recommended resolution above 256x256, otherwise review effectiveness may be affected;</li>
        <li>Image file formats supported: PNG, JPG, JPEG, BMP, GIF, WEBP.</li>
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
        This API is used to search media information with multiple filter criteria, sort and filter returned results, and other features. This includes:
        -Specify the file ID collection FileIds to return media matching any ID in the collection.
        -Do fuzzy search based on multiple media file Names or Descriptions.
        -Search by multiple filename prefixes NamePrefixes.
        - Specify the category collection ClassIds (see input parameters), and media that meet any category in the collection will be returned. For example, media categories include movies, TV series, and variety shows. The movie category has subcategories such as historical films, action films, and romance films. If ClassIds specifies movies and TV series, all subcategories under movies and TV series will be returned. If ClassIds specifies historical films and action films, only media under these two subcategories will be returned.
        - Specify tag collection Tags (see input parameters) to return media that meets any tag in the collection. For example, if media tags include ACG, palace intrigue, and parody remix, and Tags specifies ACG and parody remix, any media that matches either of these two tags will be retrieved.
        -Specify a collection of file types in Categories (see input parameters) to return media that meets any type in the collection. For example, file types include Video, Audio, and Image. If Categories specifies Video and Audio, media that meets these types will be retrieved.
        -Specify the source collection SourceTypes (see input parameters) to return media that meets any source in the collection. For example, media sources include Record (live recording), Upload, and so on. If SourceTypes specifies Record and Upload, media that meets these sources will be retrieved.
        -Specify the file muxing format set MediaTypes (see input parameters), and return media that meet any muxing format in the collection. For example, muxing formats include MP4, AVI, MP3, and so on. If MediaTypes specifies MP4 and MP3, media that comply with these muxing formats will be retrieved.
        -Specify the file status collection Status (see input parameters) to return media that meets any status in the collection. For example, file statuses include Normal, SystemForbidden (Platform Ban), and Forbidden (proactive ban). If Status specifies Normal and Forbidden, media that meets these statuses will be retrieved.
        -Specify the file moderation result set ReviewResults (see input parameters) to return media that meet any status in the collection. For example, file moderation results include pass and block. If ReviewResults specifies pass and block, media that meet these review results will be retrieved.
        -Filter the media of live recording service by the specified collection of live streaming codes StreamIds (see input parameter).
        -Filter media by the create time range of the specified media.
        -Specify a TRTC application ID collection to filter media.
        -Specify a TRTC room ID collection to filter media.

        -The above parameters can be combined in any way for search. For example, filter media with a creation time between 2018-12-01 12:00:00 and 2018-12-08 12:00:00, categorized as movie or TV series, and tagged with palace intrigue and suspense. Note that for any parameter that supports array input, the search logic between its elements is "OR". The logical relationship between all parameters is "AND".

        -Allow passage of Filters to control the type of media information returned (default return all information). Selectable inputs include:
        1. Basic information (basicInfo): including media name, category, playback address, cover image, etc.
        2. Meta information (metaData): including size, duration, video stream information, and audio stream information.
        3. Transcode result information (transcodeInfo): includes media addresses, video stream parameters, and audio stream parameters of various specifications generated for the transcoded media.
        4. animatedGraphicsInfo: The animated graphics info after converting a video to GIF (for example, gif).
        5. sampleSnapshotInfo: Screenshot information after video sampling.
        6. Sprite image information (imageSpriteInfo): sprite image information after capturing sprite images from a video.
        7. snapshotByTimeOffsetInfo: screenshot information after taking screenshots at specified time points.
        8. Video timestamp information (keyFrameDescInfo): Dotting information set for the video.
        9. Adaptive Bitrate Streaming information (adaptiveDynamicStreamingInfo): includes specification, encryption type, packaging format and other related information.

        -Allow sorting results by creation time and return them in pages. Use Offset and Limit (see input parameters) to control pagination.

        <div id="maxResultsDesc">API return result count limit:</div>

        - <b><a href="#p_offset">Offset</a> and <a href="#p_limit">Limit</a> both parameters impact the number of results per pagination query. Special attention: When both values are not specified, this interface returns up to 10 query results only.</b>
        -<b>It supports returning up to 5000 search results. Results beyond this limit are no longer queryable. If the search result volume is too large, use more granular criteria to reduce the search results.</b>

        <br>Not recommended conditional filtering:
        -(Not recommended: use Names, NamePrefixes, or Descriptions instead) Specify a single Text to do fuzzy search on media file Names or Descriptions.
        -(Not recommended: use SourceTypes instead) Specify a single media file source SourceType for search.
        -(Not recommended: use StreamIds instead) Specify single push stream live code StreamId for search.
        -(Not recommended: use CreateTime instead) Specify a single starting creation time StartTime to search.
        -(Not recommended: use CreateTime instead) Specify a single ending creation time EndTime to search.
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
        Use natural language to conduct semantic search on media.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchMediaBySemantics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchMediaBySemanticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetCLSPushTarget(
            self,
            request: models.SetCLSPushTargetRequest,
            opts: Dict = None,
    ) -> models.SetCLSPushTargetResponse:
        """
        Set a delivery target for the VOD domain in CLS.
        """
        
        kwargs = {}
        kwargs["action"] = "SetCLSPushTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetCLSPushTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetDrmKeyProviderInfo(
            self,
            request: models.SetDrmKeyProviderInfoRequest,
            opts: Dict = None,
    ) -> models.SetDrmKeyProviderInfoResponse:
        """
        Sets DRM key provider information.
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
        Set the HTTPS certificate for a vod domain.
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
        Crop an HLS video by time period to generate a new HLS video in real time. Developers can share it immediately or store it for long-term preservation.

        Tencent Cloud VOD supports two editing modes:
        -Edit and save: Save the edited video as an independent video with an independent FileId. This is suitable for long-term preservation of highlights.
        - Editing is not solidified: The edited video is attached to the input file and has no standalone FileId. This is suitable for scenarios where highlight clips are shared temporarily.

        This API is used to crop an m3u8 file based on input. Its minimum editing precision is one ts slice, so second-level or more precise editing precision cannot be achieved.

        ### Edit solidification
        Editing solidification refers to saving an edited video as an independent video with its own FileId. Its lifecycle is not subject to the original input video. Even if the original input video is deleted, the clipping result is not impacted. You can also transcode it or publish it on WeChat.

        For example, a complete football match raw video may last for 2 hours. For cost savings, a customer can store this video for 2 months, but can specify longer storage for the edited "highlights" video. You can also separately transcode the "highlights" video, publish it on WeChat, and perform other additional on-demand operations. In this case, you can choose the edit and solidify solution.

        The advantage of edit solidification is that its lifecycle is independent of the original input video, allowing separate management and long-term preservation.

        <font color='red'>Note:</font> If solidification is specified when editing, enable reception of editing solidification event notifications through the ModifyEventConfig API. After successful solidification, you will receive a PersistenceComplete event notification. Before receiving this event notification, you should not delete or reduce the storage class of the original input video. Otherwise, playback of the generated video may be abnormal.

        ### Editing is not solidified
        Editing is not solidified, which means the result of editing (m3u8 file) shares the same TS segments with the original input video. The generated video is not an independent and complete video (no independent FileId, only a playback URL), and its valid period is consistent with that of the original input full video. Once the original input video is deleted, the clip will also become unplayable.

        Editing is not solidified. Since the clipping result is not an independent video, it is not included in video management of on-demand media assets (for example, the total number of videos in the console does not count this video clip), and no video processing operation such as transcoding or WeChat publishing can be performed on this video clip separately.

        The advantage of non-solidified editing is that the editing operation is Relatively "lightweight" and will not generate additional storage overhead. However, its shortcoming is that the lifecycle is identical to the original recorded video, and it is unable to further perform video processing such as transcoding.
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
        This API is used to split an on-demand video and generate multiple new on-demand videos.
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
        This API is used to enable or disable a CDN acceleration domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "StartCDNDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartCDNDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextToSpeechAsync(
            self,
            request: models.TextToSpeechAsyncRequest,
            opts: Dict = None,
    ) -> models.TextToSpeechAsyncResponse:
        """
        This API is used to initiate a text to speech task, synthesizing text into speech for long text scenarios (up to 200,000 characters). It supports specifying voice tone and synthesis parameters such as speaking rate, volume, pitch, sampling rate, and output format. Text to speech is an asynchronous task, and audio is generated upon completion.
        """
        
        kwargs = {}
        kwargs["action"] = "TextToSpeechAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextToSpeechAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextToSpeechSync(
            self,
            request: models.TextToSpeechSyncRequest,
            opts: Dict = None,
    ) -> models.TextToSpeechSyncResponse:
        """
        Initiate a text to speech task to convert text into speech.
        """
        
        kwargs = {}
        kwargs["action"] = "TextToSpeechSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextToSpeechSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAigcApiToken(
            self,
            request: models.UpdateAigcApiTokenRequest,
            opts: Dict = None,
    ) -> models.UpdateAigcApiTokenResponse:
        """
        Creates a Token for invoking AIGC APIs. Data sync has a delay once created. It can be queried or deleted after about 30 seconds.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAigcApiToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAigcApiTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateVoice(
            self,
            request: models.UpdateVoiceRequest,
            opts: Dict = None,
    ) -> models.UpdateVoiceResponse:
        """
        This API is used to update the profile information of a voice by voice ID, including name, description, gender, age, language, tags, and scenarios, and return the complete voice information after the update. Only voices under this account can be updated. System preset voices do not support update.

        Note: Newly designed or cloned voice types cannot be updated before activation. They are activated only after the new voice type is used for TTS once.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateVoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateVoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyDomainRecord(
            self,
            request: models.VerifyDomainRecordRequest,
            opts: Dict = None,
    ) -> models.VerifyDomainRecordResponse:
        """
        This API is used to verify domain name resolution values.
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyDomainRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyDomainRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)