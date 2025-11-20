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
        This API is used to create a custom video content analysis template. Up to 50 templates can be created.
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
        Initiate an adaptive bitrate streaming processing task, with the following features:
        1. Output HLS and MPEG-DASH adaptive streams based on the specified templates;
        2. DRM options for the adaptive bitrate streaming include no encryption, Widevine, or FairPlay.
        3. The output adaptive bitrate streaming can include multiple audio streams in different languages, with each language sourced from different media files.
        4. The output adaptive stream can also include multiple subtitle streams in different languages.

        **Notes:**
        1. When using opening/closing credits, the video stream in the opening credit must be synchronized with the audio stream; otherwise, it will result in audio and video desynchronization in the output content.
        2. If the output adaptive bitrate streaming needs to include audio from the main media, the FileId of the main media must be specified in the AudioSet parameter.
        3. Subtitles must be added to the main media beforehand, which can be done through the ModifyMediaInfo API interface or the Video Management page in the console.
        4. Support for TESHD transcoding and watermarking is currently not available.
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
        Create HeadTail Template.
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
        This API is used to query CDN bandwidth, traffic, and other data of VOD domain names.
        * The query period is up to 90 days.
        * You can query data of different service regions.
        * You can query data of Chinese mainland by region and ISP.
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
        This API is used to query the CDN statistics of VOD such as traffic and bandwidth.
           1. Only CDN usage data for the last 365 days can be queried.
           2. The query time range cannot be more than 90 days.
           3. The time granularity of usage data can be specified, including 5-minute, 1-hour, and 1-day.
           4. Traffic refers to the total traffic within the query time granularity, while bandwidth the peak bandwidth.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCDNUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCDNUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnLogs(
            self,
            request: models.DescribeCdnLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnLogsResponse:
        """
        This API is used to query the download links of CDN access logs of a VOD domain name.
            1. Only download links of CDN logs for the last 30 days can be queried.
            2. By default, CDN generates a log file every hour. If there is no CDN access for a certain hour, no log file will be generated for the hour.
            3. A CDN log download link is valid for 24 hours.
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
        This API is used to query the download links of playback statistics files.
        * You can query the download links of playback statistics files in the past year. The start and end dates for query cannot be more than 90 days apart.
        * Every day, VOD will analyze CDN request logs of the previous day and then generate a playback statistics file.
        * A playback statistics file includes playback times and traffic of media files.
        * Notes on playback times:
            1. HLS file: VOD counts playback times when M3U8 files are accessed, but not when TS files are accessed.
            2. Other files (MP4 files for example): VOD does not count playback times when the playback request carries the `range` parameter and the `start` parameter in `range` is not `0`. In other cases, VOD counts playback times.
        * Statistics on playback devices: VOD counts playback times on mobile clients when the playback request carries the `UserAgent` parameter which includes an identifier such as `Android` or `iPhone`. In other cases, VOD counts playback times on PC clients.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDailyPlayStatFileList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDailyPlayStatFileListResponse
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
        Tencent Cloud VOD provides customers with services such as media upload, media management, and media processing. During or after the execution of these services, Tencent Cloud VOD also offers various corresponding event notifications to facilitate developers' awareness of the service processing status and to perform subsequent business operations. Developers can use this interface to query the current configuration of event notification reception methods, reception addresses, and which events have callback notification reception enabled.
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
        This API is used to query the playback statistics of a media file at the specified granularity.
        * You can query playback statistics in the past year.
        * If the granularity is an hour, the start and end time cannot be more than seven days apart.
        * If the granularity is a day, the start and end time cannot be more than 90 days apart.
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
        This API is used to query the information of video processing usage within the specified time range.
           1. Statistics on video processing for the last 365 days can be queried.
           2. The query time range cannot be more than 90 days.
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
        This API is used to query VOD storage usage in bytes within the query period.
            1. You can only query storage usage for the last 365 days.
            2. The query period is up to 90 days.
            3. The query period at minute-level granularity is up to 7 days.
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
        
    async def ExtractCopyRightWatermark(
            self,
            request: models.ExtractCopyRightWatermarkRequest,
            opts: Dict = None,
    ) -> models.ExtractCopyRightWatermarkResponse:
        """
        Extract CopyRight Watermark.
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
        This API is used to extract the user ID of a user that distributed a video containing a digital watermark.
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
        Implement quick concatenation and quick clipping for Tencent Cloud VOD's HLS videos to generate new media in HLS format. The video generated by quick concatenation or clipping will produce a new FileId and undergo solidification. After successful solidification, the new video file exists independently of the original input video and is not affected by deletions or other actions on the original video. <font color='red'>Note:</font> Enable the reception of persistence completed event notifications through the ModifyEvent config interface, and a PersistenceComplete type event notification will be received after successful solidification. Before receiving this event notification, operations such as deletion or cooling down of the original input video should not be performed, otherwise, abnormal playback may occur in the video generated by the concatenation and clipping.
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
        * After a media file is forbidden, except previewing it in the VOD Console, accessing the URLs of its various resources (such as source file, output files, and screenshots) in other scenarios will return error 403.
          It takes about 5-10 minutes for a forbidding/unblocking operation to take effect across the entire network.
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
        
    async def LiveRealTimeClip(
            self,
            request: models.LiveRealTimeClipRequest,
            opts: Dict = None,
    ) -> models.LiveRealTimeClipResponse:
        """
        Live broadcast real-time editing means that during the live broadcast process (that is, before the live broadcast has ended), customers can select a section of past live broadcast content to generate a new video (HLS format) in real time. Developers can share it immediately, or permanently Save it.

        Tencent Cloud VOD supports two real-time editing modes:
        - Editing and solidification: Save the edited video as an independent video with an independent FileId; suitable for scenes where the highlight clips are saved for a long time;
        - Editing is not solidified: the edited video is attached to the live broadcast recording file and does not have an independent FileId; it is suitable for scenarios where highlight clips are **temporarily shared**.

        Notice:
        - The prerequisite for using the live broadcast real-time editing function is that the target live stream has the [Time Shift Replay](https://intl.cloud.tencent.com/document/product/267/32742?from_cn_redirect=1) function enabled.
        - Live broadcast real-time editing is based on the m3u8 file generated by live broadcast recording, so its minimum editing accuracy is one ts slice, and it is impossible to achieve second-level or more precise editing accuracy.
        - Since the stream may be interrupted during the live broadcast, the actual video duration generated by editing may be inconsistent with expectations. For example, the time interval for editing a live stream is from 2018-09-20T10:30:00Z to 2018-09-20T10:40:00Z. If the stream is interrupted during this time interval, the duration of the returned media asset file will be Less than 10 minutes, in which case it can be sensed via the output parameter <a href="#p_segmentset">SegmentSet</a>.

        ### Clip solidification
        Clip solidification means saving the clipped video into an independent video (with an independent FileId). Its life cycle is not affected by the original live broadcast recording video (even if the original recording video is deleted, the editing results will not be affected in any way); it can also be subjected to secondary processing such as transcoding.

        For example: for a complete football match, the original video recorded live may be as long as 2 hours. To save costs, the customer can store this video for 2 months, but for the "highlight moment" video that is edited in real time during the live broadcast However, you can specify a longer storage period, and at the same time, you can separately transcode the "highlight moments" video and other on-demand operations. At this time, you can choose the solution of real-time editing and solidification of the live broadcast.

        The advantage of editing and curing is that its life cycle is independent of the original recorded video, and can be managed independently and stored for a long time.

        <font color='red'>Notice:</font> If solidification is specified during clipping, enable the reception of persistence completed event notifications through the ModifyEventConfig interface. After successful solidification, an event notification of type PersistenceComplete will be received. Before receiving this event notification, operations such as deletion or cooling down of live recording videos should not be performed, otherwise, abnormal playback may occur in the video generated by the clipping.

        ### Clips are not solidified
        The editing is not solidified, which means that the result of editing (m3u8 file) and the live recording video share the same ts fragment. The newly generated video is not an independent and complete video (no independent FileId, only playback URL), and its validity period is the same as the live broadcast. The validity period of the complete recorded video is the same. Once the video recorded during the live broadcast is deleted, the clip will also become unplayable.

        The clip is not solidified. Because the clip result is not an independent video, it will not be included in on-demand media asset video management (for example, the total number of videos in the console will not count this clip), and this clip cannot be transcoded separately. Video processing operations.

        The advantage of not solidifying editing is that its editing operation is very "lightweight" and does not generate additional storage overhead. However, its disadvantage is that the life cycle is the same as the original recorded video, and further video processing such as transcoding cannot be performed.
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
        
    async def ProcessMedia(
            self,
            request: models.ProcessMediaRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaResponse:
        """
        Initiate processing tasks for media file in VOD, including:
        1. Video transcoding (with Watermark);
        2. Video to animated image;
        3. Screencapturing the video at specified Time point;
        4. Sampled screenshot of the video;
        5. Generated Image sprite template from the video;
        6. Generated a cover image from the video;
        7. Adaptive Bitrate Streaming for the video (with encryption);
        8. Content Moderation (offensive Information, unsafe Information, inappropriate Information), it is <font color=red>not recommended</font> to use this API, recommend using [Video moderation(ReviewAudioVideo)](https://www.tencentcloud.com/document/api/266/50634) or [Image moderation(ReviewImage)](https://www.tencentcloud.com/document/api/266/47138);
        9. Content analysis (tag, category, cover, frame-by-frame tag);
        10. Content recognition (video intro and outro, face, Text, keyword, voice, Key object).

        If using event notification, the event notification type is [task flow status change](https://www.tencentcloud.com/document/product/266/33953).
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
        This API is used to utilize the media processing capability of Media Processing Service (MPS) to initiate media processing for videos on VOD. When the task is initiated, relevant MPS parameters must be filled in the MPSProcessMediaParams parameter in JSON format. For detailed task parameter configuration, please refer to the [ProcessMedia API](https://www.tencentcloud.com/document/product/1041/33640).
        Currently supported MPS features:
        1. [Smart Erase](https://www.tencentcloud.com/document/product/1041/58269): This function blurs, de-blurs, or removes traces of logos, subtitles, faces, and license plates in the video, facilitating content dissemination and sharing. The new media generated by this task will be stored in a new FileId within the sub-application of VOD.
        > Media processing tasks initiated in this way:
        > 1. Task status and results are still queried on the on-demand platform. Use [DescribeTaskDetail](https://www.tencentcloud.com/document/product/266/34129) or [DescribeTasks](https://www.tencentcloud.com/document/product/266/37559) to query the task.
        > 2. Usage and billing for related functions will be provided on the MPS platform. Therefore, you must activate MPS service before using this feature.
        > 3. This feature is currently in internal testing. If you would like to test it, please contact us for support.
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
        Search for media information, supporting multiple condition filtering, as well as sorting and filtering of returned results. This includes:
        - Specify a collection of file IDs (FileIds) to return media with any ID in the collection.
        - Fuzzy search based on multiple media file names (Names) or description information (Descriptions).
        - Search based on multiple file name prefixes (NamePrefixes).
        - Specify a collection of categories (ClassIds, see input parameters) to return media that meets any category in the collection. For example, media categories include movies, TV shows, variety shows, etc., and there are subcategories such as historical films, action films, and romance films under the movie category. If ClassIds specifies movies and TV shows, all subcategories under movies and TV shows will be returned; if ClassIds specifies historical films and action films, only media under these two subcategories will be returned.
        - Specify a collection of tags (Tags, see input parameters) to return media that meets any tag in the collection. For example, media tags include ACG, palace fighting, and ghost animal. If Tags specifies ACG and ghost animal, media that meets any of these two tags will be retrieved.
        - Specify a collection of file types (Categories, see input parameters) to return media that meets any type in the collection. For example, file types include Video (video), Audio (audio), and Image (image). If Categories specifies Video and Audio, media that meets these types will be retrieved.
        - Specify a collection of sources (SourceTypes, see input parameters) to return media that meets any source in the collection. For example, media sources include Record (live recording) and Upload (upload). If SourceTypes specifies Record and Upload, media that meets these sources will be retrieved.
        - Specify a collection of file container formats (MediaTypes, see input parameters) to return media that meets any container format in the collection. For example, container formats include MP4, AVI, MP3, etc. If MediaTypes specifies MP4 and MP3, media that meets these container formats will be retrieved.
        - Specify a collection of file statuses (Status, see input parameters) to return media that meets any status in the collection. For example, file statuses include Normal (normal), SystemForbidden (platform ban), and Forbidden (active ban). If Status specifies Normal and Forbidden, media that meets these statuses will be retrieved.
        - Specify a collection of file moderation results (ReviewResults, see input parameters) to return media that meets any status in the collection. For example, file moderation results include pass (passed) and block (not compliant). If ReviewResults specifies pass and block, media that meets these moderation results will be retrieved.
        - Filter live recorded media by specifying a collection of live streaming codes (StreamIds, see input parameters).
        - Filter media by specifying the creation time range of the media.
        - Filter media by specifying a collection of TRTC application IDs.
        - Filter media by specifying a collection of TRTC room IDs.

        - The above parameters can be combined in any way to search. For example, filter media created between 12:00:00 on December 1, 2018, and 12:00:00 on December 8, 2018, categorized as movies or TV shows, and tagged with palace fighting and suspense. Note that the search logic for elements of any parameter that supports array input is 'or'. The logical relationship between all parameters is 'and'

        - Allow to control the type of media information returned through Filters (default to return all information). Optional inputs include:
            1. Basic information (basicInfo): including media name, category, playback URL, cover image, etc.
            2. Metadata (metaData): including size, duration, video stream information, audio stream information, etc.
            3. Transcoding result information (transcodeInfo): including the media addresses, video stream parameters, audio stream parameters, etc., generated by transcoding the media into various specifications.
            4.  Animated image result information (animatedGraphicsInfo): information on the animated image (such as gif) generated after converting the video.
            Sampled screenshot information (sampleSnapshotInfo): screenshot information after sampling the video.
            6. Image sprite information (imageSpriteInfo): image sprite information after generating the sprite from the video.
            7. Specified time point screenshot information (snapshotByTimeOffsetInfo): screenshot information after capturing the video at specified time points.
            8. Video timestamp info (keyFrameDescInfo): timestamp information set for the video.
            9. Adaptive Bitrate Streaming information (adaptiveDynamicStreamingInfo): including specifications, encryption types, muxing formats, and other relevant information.

        - Allow sorting the results by creation time and returning them in pages. Pagination is controlled by Offset and Limit (see input parameters).

        <div id="maxResultsDesc">API result count limitation:</div>
        - <b><a href="#p_offset">Offset</a> and <a href="#p_limit">Limit</a> both affect the number of results returned in a single page query. Please pay special attention: when both of these values are missing, this API will return a maximum of 10 query results.</b>
        - <b>Supports up to 5,000 search results, and queries beyond this limit are not supported. If the search result volume is too large, it is recommended to use more refined filtering conditions to reduce search results.</b>

        <br>Not recommended for conditional filtering:
        - (Not recommended: use Names, NamePrefixes, or Descriptions instead) Fuzzy search for media file names or description information with a single text (Text).
        - (Not recommended: use SourceTypes instead) Search for media files with a single source (SourceType).
        - (Not recommended: use StreamIds instead) Search for media files with a single live streaming code (StreamId).
        - (Not recommended: use CreateTime instead) Search for media files with a single start creation time (StartTime).
        - (Not recommended: use CreateTime instead) Search for media files with a single end creation time (EndTime).
        """
        
        kwargs = {}
        kwargs["action"] = "SearchMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchMediaResponse
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
        This API is used to cut a clip from an HLS video to generate a new video (in HLS format). You can either share the new video or save it.

        VOD supports two types of clipping:
        - Clipping for persistent storage: The video clip is saved as an independent video file with its own `FileId`.
        - Clipping for temporary sharing: The video clip shares `FileId` with the input file.

        Notes:
        - Clipping is based on the M3U8 file that contains a list of TS segments, so the smallest clipping unit is one TS segment instead of a second or less.


        ### Clipping for persistent storage
        In this mode, a video clip is saved as an independent video file with a `FileId`, and its lifecycle is not subject to the input video. Even if the source video is deleted, the video clip still exists. Moreover, the video clip can be transcoded, published on WeChat, and processed in other ways.

        Suppose you recorded a two-hour football match. You want to save the full video for only two months to save costs, but want to save the highlights for a longer time and perhaps transcode and publish the highlight clip to WeChat. In this case, you can choose clipping for persistent storage.

        The advantage of clipping for persistent storage is that the video clip has a lifecycle independent of the input video and can be managed independently and stored persistently.

        <font color='red'>Notice:</font> If solidification is specified during clipping, enable the reception of persistence completed event notifications through the ModifyEventConfig interface. After successful solidification, an event notification of type PersistenceComplete will be received. Before receiving this event notification, operations such as deletion or cooling down of live recording videos should not be performed, otherwise, abnormal playback may occur in the video generated by the clipping.

        ### Clipping for temporary sharing
        The video clip (an M3U8 file) shares the same TS segments with the input video instead of being an independent video. It only has a playback URL but has no `FileId`, and its validity period is the same as that of the input video. Once the input video is deleted, the video clip cannot be played back.

        Because the video clip is not an independent video, it's not displayed as a media asset in the VOD console, and cannot be transcoded or published to WeChat.

        Clipping for temporary sharing is lightweight and incurs no additional storage fees. However, the video clip has the same lifecycle as the source recording video and cannot be transcoded or processed in other ways.
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