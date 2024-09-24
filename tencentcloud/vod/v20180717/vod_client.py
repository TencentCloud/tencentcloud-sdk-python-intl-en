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
from tencentcloud.vod.v20180717 import models


class VodClient(AbstractClient):
    _apiVersion = '2018-07-17'
    _endpoint = 'vod.tencentcloudapi.com'
    _service = 'vod'


    def ApplyUpload(self, request):
        """* This API is used to apply for uploading a media file (and cover file) to VOD and obtain the metadata of file storage (including upload path and upload signature) for subsequent use by the uploading API.
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
        """This API is used to associate/disassociate subtitles with/from a media file of a specific adaptive bitrate streaming template ID.

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
        """Clone CDN Domain.

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
        """This API is used to confirm the result of uploading a media file (and cover file) to VOD, store the media information, and return the playback address and ID of the file.

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
        """This API is used to compose a media file. You can use it to do the following:

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
        """* After the `PullEvents` API is called to get an event, this API must be called to confirm that the message has been received;
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
        """This API is used to create a custom video content analysis template. Up to 50 templates can be created.

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
        """This API is used to create a custom video content recognition template. Up to 50 templates can be created.

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
        """This API is used to create an adaptive bitrate streaming template. Up to 100 templates can be created.

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


    def CreateAnimatedGraphicsTemplate(self, request):
        """This API is used to create a custom animated image generating template. Up to 16 templates can be created.

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


    def CreateCDNDomain(self, request):
        """This API is used for adding domain names to VOD. A user can add up to 20 domain names. 1. After the domain name is added successfully, VOD will carry out the deployment of the domain name. It takes approximately 2 minutes for the domain name to change from the deployment status to the online status.

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
        """* This API is used to categorize media assets for management;
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


    def CreateContentReviewTemplate(self, request):
        """We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [CreateReviewTemplate](https://intl.cloud.tencent.com/document/api/266/84391?from_cn_redirect=1).
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
        """This API is used for generating a subdomain resolution, prompting the customer to add it to the domain name resolution, used for wildcard domain and domain name retrieval verification of ownership.

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
        """Create enhance media template.

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
        """Create HeadTail Template.

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
        """This API is used to create a custom image processing template. A template can include at most 10 operations, for example, crop-scale-crop-blur-scale-crop-scale-crop-blur-scale. You can have up to 16 image processing templates.

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
        """This API is used to create a custom image sprite generating template. Up to 16 templates can be created.

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
        """Create Just In Time Transcode Template.

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


    def CreatePersonSample(self, request):
        """This API is used to create samples for using facial features positioning and other technologies to perform video processing operations such as content recognition and inappropriate information recognition.

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
        """This API is used to create a custom task flow template. Up to 50 templates can be created.

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


    def CreateQualityInspectTemplate(self, request):
        """Creates media quality inspection template.

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
        """Create rebuild media template.

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
        """This API is used to create a custom moderation template. Up to 50 templates can be created in total.
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
        """This API is used to create a playlist. You can create at most 100 playlists.
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
        """This API is used to create a custom sampled screencapturing template. Up to 16 templates can be created.

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


    def CreateSnapshotByTimeOffsetTemplate(self, request):
        """This API is used to create a custom time point screencapturing template. Up to 16 templates can be created.

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
        """This API is used to enable storage in a region.
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
        """This API is used to create a VOD subapplication.

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
        """We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
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
        """This API is used to create a custom transcoding template. Up to 100 templates can be created.

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
        """This API is used to add an acceleration domain name to VOD. One user can add up to 20 domain names.
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
        """This API is used to create a custom watermarking template. Up to 1,000 templates can be created.

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
        """This API is used to create keyword samples in batches for using OCR and ASR technologies to perform video processing operations such as content recognition and inappropriate information recognition.

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
        """This API is used to delete a custom video content analysis template.

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
        """This API is used to delete a custom video content recognition template.

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
        """This API is used to delete an adaptive bitrate streaming template.

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


    def DeleteAnimatedGraphicsTemplate(self, request):
        """This API is used to delete a custom animated image generating template.

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


    def DeleteCDNDomain(self, request):
        """Delete CDN Domain

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
        """* A category can be deleted only if it has no subcategories and associated media files;
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
        """We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [DeleteReviewTemplate](https://intl.cloud.tencent.com/document/api/266/84390?from_cn_redirect=1).
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
        """Delete Enhance Media template

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
        """Delete HeadTail Template

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
        """This API is used to delete an image processing template.

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
        """This API is used to delete an image sprite generating template.

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
        """Delete Just In Time Transcode Template.

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


    def DeleteMedia(self, request):
        """* This API is used to delete a media file and its processed files, such as the transcoded video files, image sprites, screenshots, and videos for publishing on WeChat.
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
        """This API is used to delete samples according to sample IDs.

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
        """Delete user-created task flow templates.

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


    def DeleteQualityInspectTemplate(self, request):
        """Deletes media quality inspection template.

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
        """Delete rebuild media template.

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
        """This API is used to delete a custom moderation template.
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
        """This API is used to delete a playlist.

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
        """This API is used to delete a custom sampled screencapturing template.

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
        """This API is used to delete a custom time point screencapturing template.

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
        """We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
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
        """This API is used to delete a custom transcoding template.

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
        """This API is used to delete an acceleration domain name from VOD.
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
        """This API is used to delete a custom watermarking template.

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
        """This API is used to delete keyword samples in batches.

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
        """This API is used to get the list of video content analysis templates based on unique template ID. The returned result includes all eligible custom and [preset video content analysis templates](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.88.86.E6.9E.90.E6.A8.A1.E6.9D.BF).

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
        """This API is used to get the list of video content recognition templates based on unique template ID. The return result includes all eligible custom and [preset video content recognition templates](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E8.AF.86.E5.88.AB.E6.A8.A1.E6.9D.BF).

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
        """This API is used to query the list of transcoding to adaptive bitrate streaming templates and supports paged queries by filters.

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


    def DescribeAllClass(self, request):
        """* This API is used to get the information of all categories.

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
        """This API is used to query the list of animated image generating templates and supports paged queries by filters.

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


    def DescribeCDNDomains(self, request):
        """Describe CDN Domains

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
        """This API is used to query CDN bandwidth, traffic, and other data of VOD domain names.
        * The query period is up to 90 days.
        * You can query data of different service regions.
        * You can query data of Chinese mainland by region and ISP.

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
        """This API is used to query the CDN statistics of VOD such as traffic and bandwidth.
           1. Only CDN usage data for the last 365 days can be queried.
           2. The query time range cannot be more than 90 days.
           3. The time granularity of usage data can be specified, including 5-minute, 1-hour, and 1-day.
           4. Traffic refers to the total traffic within the query time granularity, while bandwidth the peak bandwidth.

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
        """This API is used to query the download links of CDN access logs of a VOD domain name.
            1. Only download links of CDN logs for the last 30 days can be queried.
            2. By default, CDN generates a log file every hour. If there is no CDN access for a certain hour, no log file will be generated for the hour.
            3. A CDN log download link is valid for 24 hours.

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
        """This interface returns client upload acceleration statistics within the query time range.
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
        """We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [DescribeReviewTemplates](https://intl.cloud.tencent.com/document/api/266/84389?from_cn_redirect=1).
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


    def DescribeDailyPlayStatFileList(self, request):
        """This API is used to query the download links of playback statistics files.
        * You can query the download links of playback statistics files in the past year. The start and end dates for query cannot be more than 90 days apart.
        * Every day, VOD will analyze CDN request logs of the previous day and then generate a playback statistics file.
        * A playback statistics file includes playback times and traffic of media files.
        * Notes on playback times:
            1. HLS file: VOD counts playback times when M3U8 files are accessed, but not when TS files are accessed.
            2. Other files (MP4 files for example): VOD does not count playback times when the playback request carries the `range` parameter and the `start` parameter in `range` is not `0`. In other cases, VOD counts playback times.
        * Statistics on playback devices: VOD counts playback times on mobile clients when the playback request carries the `UserAgent` parameter which includes an identifier such as `Android` or `iPhone`. In other cases, VOD counts playback times on PC clients.

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
        """This API is used to query DRM key information.

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
        """Describe Enhance Media Templates.

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
        """Tencent Cloud VOD provides customers with services such as media upload, media management, and media processing. During or after the execution of these services, Tencent Cloud VOD also offers various corresponding event notifications to facilitate developers' awareness of the service processing status and to perform subsequent business operations. Developers can use this interface to query the current configuration of event notification reception methods, reception addresses, and which events have callback notification reception enabled.

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
        """This API is used to get file attributes asynchronously.
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
        """Describe HeadTail Templates.

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
        """This API is used to query image processing templates. You can specify the filters as well as the offset to start returning records from.

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
        """This interface returns the image review usage information used every day within the query time range.
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
        """This API is used to query the list of image sprite generating templates and supports paged queries by filters.

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
        """Describe Just In Time Transcode Templates.

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


    def DescribeLicenseUsageData(self, request):
        """This interface returns information about the number of license requests per day within the query time range.
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


    def DescribeMediaInfos(self, request):
        """1. This API is used to get the information of multiple media files. Specifically, the information returned is as follows:
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
        """This API is used to query the playback statistics of a media file at the specified granularity.
        * You can query playback statistics in the past year.
        * If the granularity is an hour, the start and end time cannot be more than seven days apart.
        * If the granularity is a day, the start and end time cannot be more than 90 days apart.

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
        """This API is used to query the information of video processing usage within the specified time range.
           1. Statistics on video processing for the last 365 days can be queried.
           2. The query time range cannot be more than 90 days.

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
        """This API is used to query the information of samples and supports paginated queries by sample ID, name, and tag.

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
        """This API is used to get the list of task flow template details by task flow template name.

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


    def DescribeQualityInspectTemplates(self, request):
        """Get media quality inspection Template List.

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
        """Describe Rebuild Media Templates

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
        """<b>This API is disused and replaced by [DescribeMediaProcessUsageData](https://intl.cloud.tencent.com/document/product/266/41464?from_cn_redirect=1).</b>

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
        """This API is used to get the information of moderation templates.
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
        """This API is used to query playlists.

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
        """This API is used to query the list of sampled screencapturing templates and supports paged queries by filters.

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
        """This API is used to query the list of time point screencapturing templates and supports paged queries by filters.

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
        """This API is used to query the storage capacity usage and number of files.

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
        """This API is used to query VOD storage usage in bytes within the query period.
            1. You can only query storage usage for the last 365 days.
            2. The query period is up to 90 days.
            3. The query period at minute-level granularity is up to 7 days.

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
        """This API is used to query the following information:
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
        """This API is used to query the list of the primary application and subapplications of the current account.

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
        """We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
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
        """This API is used to query the details of execution status and result of a task submitted in the last 3 days by task ID.

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
        """* This API is used to query the task list;
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
        """This API is used to get the list of transcoding templates based on unique template ID. The return result includes all eligible custom and [preset transcoding templates](https://intl.cloud.tencent.com/document/product/266/33476?from_cn_redirect=1#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF).

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
        """This API is used to query the list of VOD domain names.

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
        """This API is used to query custom watermarking templates and supports paged queries by filters.

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
        """This API is used to perform paginated queries of keyword sample information by use case, keyword, and tag.

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
        """Edit the video (cut, splice, etc.) to generate a new video. The editing functions include:

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
        """Enhance Media By Template.

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
        """Initiate a Remaster task for audio and video media in VOD

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
        """This API is only used in special scenarios of custom development. Unless requested by VOD customer service, please do not call it.

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


    def ExtractCopyRightWatermark(self, request):
        """Extract CopyRight Watermark.

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
        """This API is used to extract the user ID of a user that distributed a video containing a digital watermark.

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
        """Implement quick concatenation and quick clipping for Tencent Cloud VOD's HLS videos to generate new media in HLS format. The video generated by quick concatenation or clipping will produce a new FileId and undergo solidification. After successful solidification, the new video file exists independently of the original input video and is not affected by deletions or other actions on the original video. <font color='red'>Note:</font> Enable the reception of persistence completed event notifications through the ModifyEvent config interface, and a PersistenceComplete type event notification will be received after successful solidification. Before receiving this event notification, operations such as deletion or cooling down of the original input video should not be performed, otherwise, abnormal playback may occur in the video generated by the concatenation and clipping.

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
        """* After a media file is forbidden, except previewing it in the VOD Console, accessing the URLs of its various resources (such as source file, output files, and screenshots) in other scenarios will return error 403.
          It takes about 5-10 minutes for a forbidding/unblocking operation to take effect across the entire network.

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


    def InspectMediaQuality(self, request):
        """Initiate media quality inspection task.

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


    def LiveRealTimeClip(self, request):
        """Live broadcast real-time editing means that during the live broadcast process (that is, before the live broadcast has ended), customers can select a section of past live broadcast content to generate a new video (HLS format) in real time. Developers can share it immediately, or permanently Save it.

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
        """This API is used to manage initiated tasks.

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
        """This API is used to modify a custom video content analysis template.

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
        """This API is used to modify a custom video content recognition template.

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
        """This API is used to modify an adaptive bitrate streaming template.

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
        """This API is used to modify a custom animated image generating template.

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


    def ModifyCDNDomainConfig(self, request):
        """Modify CDN Domain Config.

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
        """This API is used to modify the category of a media file.

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
        """We have <font color=red>stopped updating</font> this API. Our new moderation templates can moderate audio/video as well as images. For details, see [ModifyReviewTemplate](https://intl.cloud.tencent.com/document/api/266/84388?from_cn_redirect=1).
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
        """This API is used to set the default storage region. A file will be stored in the default region if no region is specified for file upload.

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
        """Modify enhance media template.

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
        """Tencent Cloud VOD provides customers with media upload, media management, media processing and other services. During or at the end of the execution of these services, Tencent Cloud On-Demand also provides various corresponding event notifications to facilitate developers to perceive the service processing status and Do the next business operation.

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
        """Modify HeadTail Template.

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
        """This API is used to modify a custom image sprite generating template.

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
        """Modify Just In Time Transcode Template.

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


    def ModifyMediaInfo(self, request):
        """This API is used to modify the attributes of a media file, including category, name, description, tag, expiration time, timestamp information, video thumbnail, and subtitle information.

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
        """This API is used to modify the storage class of media files.
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
        """This API is used to modify sample information according to the sample ID. You can modify the name and description, add, delete, and reset facial features or tags. Leave at least one image after deleting facial features. To leave no image, please use the reset operation.

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


    def ModifyQualityInspectTemplate(self, request):
        """Modifies media quality inspection template.

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
        """Modify Rebuild Media Template.

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
        """This API is used to modify a custom moderation template.
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
        """This API is used to modify a playlist.
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
        """This API is used to modify a custom sampled screencapturing template.

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
        """This API is used to modify a custom time point screencapturing template.

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
        """This API is used to modify subapplication information, but it is not allowed to modify primary application information.

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
        """This API is used to enable/disable a subapplication. After a subapplication is disabled, its corresponding domain name will be blocked and its access to the console will be restricted.

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
        """We have <font color='red'>stopped updating</font> this API. Currently, you no longer need a player configuration to use player signatures. For details, see [Player Signature](https://intl.cloud.tencent.com/document/product/266/45554?from_cn_redirect=1).
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
        """This API is used to modify a custom transcoding template.

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
        """This API is used to modify the acceleration region of a domain name on VOD.
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
        """This API is used to modify domain name settings, such as the hotlink protection configuration.
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
        """This API is used to modify a custom watermarking template. The watermark type cannot be modified.

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
        """This API is used to modify the use case and tag of a keyword. The keyword itself cannot be modified, but you can delete it and create another one if needed.

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
        """This API is used to parse the index file content and return the list of segment files to be uploaded when an HLS video is uploaded. A segment file path must be a relative path of the current directory or subdirectory instead of a URL or absolute path.

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


    def ProcessMedia(self, request):
        """Initiate processing tasks for media file in VOD, including:
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


    def ProcessMediaByProcedure(self, request):
        """This API is used to start a task flow on a video.
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
        """This API is <font color='red'>disused</font>, please use [ProcessMedia](https://intl.cloud.tencent.com/document/product/862/37578?from_cn_redirect=1) API of MPS, with the input parameter `InputInfo.UrlInputInfo.Url` set to a video URL.

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
        """* This API is used to get event notifications from the business server through [reliable callback](https://intl.cloud.tencent.com/document/product/266/33948).
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
        """This API is used to pull a video on the internet to the VOD platform.

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
        """1. This API is used to prefetch a list of specified URLs.
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
        """Initiate rebuild media

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
        """Rebuild media by template.

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
        """1. This API is used to purge URLs.
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
        """This API is used to remove watermarks from a video.

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
        """This API is used to modify a custom task flow template.

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
        """This API is used to restore files from ARCHIVE or DEEP ARCHIVE. Files stored in ARCHIVE or DEEP ARCHIVE must be restored before they can be accessed. Restored files are available for a limited period of time.

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
        """This API is used to start a moderation task on a file stored in VOD to detect non-compliant content in images, text, speech, and voice.

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
        """This API is used to moderate an image stored in VOD (detect pornographic and terrorist content).><li>The image file must be smaller than 5 MB.</li> ><li>To ensure the accuracy of moderation results, the image resolution must be higher than 256 x 256 px.</li> ><li>The format must be PNG, JPG, JPEG, BMP, GIF, or WEBP.</li>

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
        """Search for media information, supporting multiple condition filtering, as well as sorting and filtering of returned results. This includes:
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


    def SetDrmKeyProviderInfo(self, request):
        """This API is used to configure DRM key information.

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
        """Set Vod Domain Certificate.

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
        """This API is used to cut a clip from an HLS video to generate a new video (in HLS format). You can either share the new video or save it.

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
        """Split the video into strips to generate multiple new videos.

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
        """This API is used for enabling/disabling the CDN acceleration domain.

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
        """This API is used to verify the domain name resolution value.

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