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
            if "Error" not in response["Response"]:
                model = models.ApplyUploadResponse()
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
            if "Error" not in response["Response"]:
                model = models.AttachMediaSubtitlesResponse()
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
            if "Error" not in response["Response"]:
                model = models.CommitUploadResponse()
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
            if "Error" not in response["Response"]:
                model = models.ComposeMediaResponse()
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
            if "Error" not in response["Response"]:
                model = models.ConfirmEventsResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateAIAnalysisTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateAIRecognitionTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateAdaptiveDynamicStreamingTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateAnimatedGraphicsTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateClassResponse()
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


    def CreateContentReviewTemplate(self, request):
        """This API is used to create custom intelligent video content recognition templates. Up to 50 templates can be created.

        :param request: Request instance for CreateContentReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateContentReviewTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateContentReviewTemplateResponse()
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


    def CreateImageProcessingTemplate(self, request):
        """This API is used to create a custom image processing template. You can create up to 16 templates, and each template can contain up to three operations, for example, cropping, scaling, and cropping again.

        :param request: Request instance for CreateImageProcessingTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateImageProcessingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateImageProcessingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageProcessingTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImageProcessingTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateImageSpriteTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreatePersonSampleResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateProcedureTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateSampleSnapshotTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateSnapshotByTimeOffsetTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateStorageRegionResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateSubAppIdResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateSuperPlayerConfigResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateTranscodeTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateVodDomainResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateWatermarkTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateWordSamplesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteAIAnalysisTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteAIRecognitionTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteAdaptiveDynamicStreamingTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteAnimatedGraphicsTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteClassResponse()
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


    def DeleteContentReviewTemplate(self, request):
        """This API is used to delete custom intelligent video content recognition templates.

        :param request: Request instance for DeleteContentReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteContentReviewTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteContentReviewTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteImageProcessingTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteImageSpriteTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteMediaResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeletePersonSampleResponse()
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


    def DeleteProcedureTemplate(self, request):
        """This API is used to delete a custom task flow template.

        :param request: Request instance for DeleteProcedureTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteProcedureTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProcedureTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProcedureTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteSampleSnapshotTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteSnapshotByTimeOffsetTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteSuperPlayerConfigResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteTranscodeTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteVodDomainResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteWatermarkTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteWordSamplesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeAIAnalysisTemplatesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeAIRecognitionTemplatesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeAdaptiveDynamicStreamingTemplatesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeAllClassResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeAnimatedGraphicsTemplatesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeCDNStatDetailsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeCDNUsageDataResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeCdnLogsResponse()
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


    def DescribeClientUploadAccelerationUsageData(self, request):
        """This API is used to query the usage of the client upload acceleration service in a specific time period.
           1. You can query the usage of client upload acceleration in the last 365 days.
           2. The maximum time period allowed for query is 90 days.
           3. If the period specified is longer than one day, the statistics returned will be on a daily basis; otherwise, they will be on a 5-minute basis.

        :param request: Request instance for DescribeClientUploadAccelerationUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeClientUploadAccelerationUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeClientUploadAccelerationUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientUploadAccelerationUsageData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClientUploadAccelerationUsageDataResponse()
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


    def DescribeContentReviewTemplates(self, request):
        """This API is used to get the list of intelligent video content recognition template details according to unique template IDs. The return result includes all eligible custom and [preset intelligent video content recognition templates](https://intl.cloud.tencent.com/document/product/266/33932).

        :param request: Request instance for DescribeContentReviewTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeContentReviewTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeContentReviewTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentReviewTemplates", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContentReviewTemplatesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeDailyPlayStatFileListResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeDrmKeyProviderInfoResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeImageProcessingTemplatesResponse()
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


    def DescribeImageReviewUsageData(self, request):
        """This API is used to query your daily usage of the image recognition feature in a specified time period.
           1. You can query statistics from the last 365 days.
           2. The maximum query period is 90 days.
           3. If the period specified is longer than one day, the statistics returned will be on a daily basis; otherwise, they will be on a 5-minute basis.

        :param request: Request instance for DescribeImageReviewUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeImageReviewUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeImageReviewUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageReviewUsageData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageReviewUsageDataResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeImageSpriteTemplatesResponse()
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


    def DescribeLicenseUsageData(self, request):
        """This API is used to query daily playback license requests in a specified time period.
           1. You can query statistics from the last 365 days.
           2. The maximum query period is 90 days.
           3. If the period specified is longer than one day, the statistics returned will be on a daily basis; otherwise, they will be on a 5-minute basis.

        :param request: Request instance for DescribeLicenseUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeLicenseUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeLicenseUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseUsageData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLicenseUsageDataResponse()
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


    def DescribeMediaInfos(self, request):
        """1. This API can get multiple types of information of multiple media files, including:
            1. Basic information (basicInfo): media name, category, playback address, cover image, etc.
            2. Metadata (metaData): size, duration, video stream information, audio stream information, etc.
            3. Information of the transcoding result (transcodeInfo): addresses, video stream parameters, and audio stream parameters of the media files with various specifications generated by transcoding a media file.
            4. Information of the animated image generating result (animatedGraphicsInfo): information of an animated image (such as .gif) generated from a video.
            5. Information of a sampled screenshot (sampleSnapshotInfo): information of a sampled screenshot of a video.
            6. Information of an image sprite (imageSpriteInfo): information of an image sprite generated from a video.
            7. Information of a time point screenshot (snapshotByTimeOffsetInfo): information of a time point screenshot of a video.
            8. Information of a timestamp (keyFrameDescInfo): information of a timestamp set for a video.
            9. Information of transcoding to adaptive bitrate streaming (adaptiveDynamicStreamingInfo): specification, encryption type, container format, etc.
        2. The return packet can be configured to only contain certain information.

        :param request: Request instance for DescribeMediaInfos.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeMediaInfosRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeMediaInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMediaInfos", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaInfosResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeMediaPlayStatDetailsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeMediaProcessUsageDataResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribePersonSamplesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeProcedureTemplatesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeReviewDetailsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeSampleSnapshotTemplatesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeSnapshotByTimeOffsetTemplatesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeStorageDataResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeStorageDetailsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeStorageRegionsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeSubAppIdsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeSuperPlayerConfigsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeTranscodeTemplatesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeVodDomainsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeWatermarkTemplatesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeWordSamplesResponse()
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
            if "Error" not in response["Response"]:
                model = models.ExecuteFunctionResponse()
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
            if "Error" not in response["Response"]:
                model = models.ExtractTraceWatermarkResponse()
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
            if "Error" not in response["Response"]:
                model = models.ForbidMediaDistributionResponse()
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


    def LiveRealTimeClip(self, request):
        """Live clipping means that during a live broadcast (before it ends), you can select a segment of previous live broadcast content to generate a new video (in HLS format) in real time and share it immediately or store it persistently.

        VOD supports two live clipping modes:
        - Persistent clipping: in this mode, the clipped video is saved as an independent video file with a `FileId`, which is suitable for **persistently storing** highlights;
        - Temporary clipping: in this mode, the clipped video is part of the LVB recording file with no `FileId`, which is suitable for **temporarily sharing** highlights;

        Note:
        - The live clipping feature can be used only when [time shifting](https://intl.cloud.tencent.com/document/product/267/32742?from_cn_redirect=1) has been enabled for the target live stream.
        - Live clipping is performed based on the m3u8 file generated by LVB recording, so its minimum clipping granularity is one ts segment rather than at or below the second level.


        ### Persistent clipping
        In persistent clipping mode, the clipped video is saved as an independent video file with a `FileId`, and its lifecycle is not subject to the source LVB recording video (even if the source video is deleted, the clipped video will not be affected in any way). It can be further processed (transcoded, published on WeChat, etc.).

        An example is as follows: for a complete football match, the source LVB recording video may be up to 2 hours in length. You want to store this video for only 2 months for the purpose of cost savings. However, you want to specify a longer retention period for the "highlights" video created by live clipping and perform additional VOD operations on it such as transcoding and release on WeChat. In this case, you need to choose the persistent clipping mode of live clipping.

        The advantage of persistent clipping is that the clipped video has a lifecycle independent of the source recording video and can be managed independently and stored persistently.

        ### Temporary clipping
        In temporary clipping mode, the clipped video (m3u8 file) shares the same ts segments with the LVB recording video instead of being an independent video. It only has a playback URL but has no `FileId`, and its validity period is the same as that of the LVB recording video; therefore, if the LVB recording video is deleted, it cannot be played back.

        For temporary clipping, as the clipping result is not an independent video, it will not be included in VOD's media asset management (for example, it will not be counted in the total videos in the console), and no video processing operations can be separately performed on it, such as transcoding and release on WeChat.

        The advantage of temporary clipping is that the clipping operation is very "lightweight" and does not incur additional storage fees. However, the clipped video has the same lifecycle as the source recording video and cannot be further transcoded or processed.

        :param request: Request instance for LiveRealTimeClip.
        :type request: :class:`tencentcloud.vod.v20180717.models.LiveRealTimeClipRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.LiveRealTimeClipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LiveRealTimeClip", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LiveRealTimeClipResponse()
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
            if "Error" not in response["Response"]:
                model = models.ManageTaskResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyAIAnalysisTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyAIRecognitionTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyAdaptiveDynamicStreamingTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyAnimatedGraphicsTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyClassResponse()
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


    def ModifyContentReviewTemplate(self, request):
        """This API is used to modify custom intelligent video content recognition templates.

        :param request: Request instance for ModifyContentReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyContentReviewTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyContentReviewTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyDefaultStorageRegionResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyImageSpriteTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyMediaInfoResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyMediaStorageClassResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyPersonSampleResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifySampleSnapshotTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifySnapshotByTimeOffsetTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifySubAppIdInfoResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifySubAppIdStatusResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifySuperPlayerConfigResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyTranscodeTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyVodDomainAccelerateConfigResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyVodDomainConfigResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyWatermarkTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyWordSampleResponse()
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
            if "Error" not in response["Response"]:
                model = models.ParseStreamingManifestResponse()
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


    def ProcessMedia(self, request):
        """This API is used to initiate a media processing task on a VOD file. The task may include:
        1. Video transcoding (with watermark)
        2. Animated image generating
        3. Time point screenshot
        4. Sampled screenshot
        5. Image sprite generating
        6. Taking a screenshot to use as the thumbnail
        7. Adaptive bitrate streaming and encryption
        8. Detecting pornographic, terrorist, and politically sensitive content
        9. Content analysis for labeling, categorization, thumbnail generation, or frame-specific labeling
        10. Recognition of opening and closing segments, faces, full text, text keywords, full speech, speech keywords, and objects

        If event notifications are used, the event type is [ProcedureStateChanged](https://intl.cloud.tencent.com/document/product/266/9636?from_cn_redirect=1).

        :param request: Request instance for ProcessMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMedia", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ProcessMediaResponse()
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


    def ProcessMediaByProcedure(self, request):
        """This API is used to initiate a processing task for a VOD video with a task flow template.
        There are two ways to create a task flow template:
        1. Create and modify a task flow template in the console;
        2. Create a task flow template through the task flow template API.

        :param request: Request instance for ProcessMediaByProcedure.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByProcedureRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByProcedureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMediaByProcedure", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ProcessMediaByProcedureResponse()
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
            if "Error" not in response["Response"]:
                model = models.ProcessMediaByUrlResponse()
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


    def PullEvents(self, request):
        """* This API is used to get event notifications from the business server through [reliable callback](https://intl.cloud.tencent.com/document/product/266/33948).
        * The API gets event data through long polling. That is, if there is any unconsumed event on the server, the event notification will be returned to the requester immediately. If there is no unconsumed event on the server, the request will be suspended in the backend until a new event is generated.
        * The request can be suspended for up to 5 seconds. It’s recommended to set the request timeout period to 10 seconds.
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
            if "Error" not in response["Response"]:
                model = models.PullEventsResponse()
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
            if "Error" not in response["Response"]:
                model = models.PullUploadResponse()
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
            if "Error" not in response["Response"]:
                model = models.PushUrlCacheResponse()
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
            if "Error" not in response["Response"]:
                model = models.RefreshUrlCacheResponse()
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
            if "Error" not in response["Response"]:
                model = models.RemoveWatermarkResponse()
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


    def ResetProcedureTemplate(self, request):
        """This API is used to reset a custom task flow template.

        :param request: Request instance for ResetProcedureTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ResetProcedureTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ResetProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetProcedureTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetProcedureTemplateResponse()
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
            if "Error" not in response["Response"]:
                model = models.RestoreMediaResponse()
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
            if "Error" not in response["Response"]:
                model = models.ReviewAudioVideoResponse()
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


    def SearchMedia(self, request):
        """This API is used to search for media files by specific criteria. You can sort the results and specify the information to return.
        - Specify a list of file IDs (`FileIds`). Any file that matches one of the IDs will be returned.
        - Specify one or multiple keywords for `Names` or `Descriptions` for fuzzy search by filename or description.
        - Specify multiple filename prefixes (`NamePrefixes`).
        - Specify a list of categories (`ClassIds`). Any file that matches one of the categories will be returned. For example, assume that there are categories `Movies`, `TV Series`, and `Variety Shows`, and `Movies` has subcategories including `History`, `Action`, and `Romance`. If `ClassIds` is set to `Movies` and `TV Series`, all media files in `Movies` (including its subcategories) and `TV Series` will be returned. If `ClassIds` is set to `History` and `Action`, only the files in those two subcategories will be returned.
        - Specify a list of tags (`Tags`). Any file that matches one or more of the tags will be returned. For example, assume that there are tags `ACG`, `Drama`, and `YTPMV`. If `Tags` is set to `ACG` and `YTPMV`, any media file with either tag will be returned.
        - Specify the types (`Categories`) of media files. Any file that matches one of the types will be returned. There are three file types: `Video`, `Audio`, and `Image`. If `Categories` is set to `Video` and `Audio`, all audio and video files will be returned.
        - Specify the source types (`SourceTypes`). Any file that matches one of the source types specified will be returned. For example, if you set `SourceTypes` to `Record` (live recording) and `Upload` (upload), all recording files and uploaded files will be returned.
        - Specify the stream IDs (`StreamIds`) of live recording files.
        - Specify a time range for search by file creation time.
        - Specify the TRTC application IDs.
        - Specify the TRTC room IDs.
        - Specify one keyword for `Text` for fuzzy search by filename or description. (This is not recommended. Please use `Names`, `NamePrefixes` or `Descriptions` instead.)
        - Specify one source (`SourceType`). (This is not recommended. Please use `SourceTypes` instead.)
        - Specify one stream ID (`StreamId`). (This is not recommended. Please use `StreamIds` instead.)
        - Specify the start (`StartTime`) of the time range to search by creation time. (This is not recommended. Please use `CreateTime` instead.)
        - Specify the end (`EndTime`) of the time range to search by creation time. (This is not recommended. Please use `CreateTime` instead.)
        - You can search by any combination of the parameters above. For example, you can search for media files with the tag "Drama" or "Suspense" in the category of "Movies" and "TV Series" created between 12:00:00, December 1, 2018 and 12:00:00, December 8, 2018. Note that for parameters whose data type is array, the search logic between their elements is "OR". The search logic between parameters is "AND".

        - You can sort the results by creation time and return them in multiple pages by specifying `Offset` and `Limit`.
        - You can use `Filters` to specify the types of file information to return (all types are returned by default). Valid values:
            1. `basicInfo`: The file name, category, playback URL, thumbnail, etc.
            2. `metaData`: The file size, duration, video stream information, audio stream information, etc.
            3. `transcodeInfo`: The URLs, video stream parameters, and audio stream parameters of transcoding outputs.
            4. `animatedGraphicsInfo`: The information of the animated images (such as GIF images) generated.
            5. `sampleSnapshotInfo`: The information of the sampled screenshots generated.
            6. `imageSpriteInfo`: The information of the image sprites generated.
            7. `snapshotByTimeOffsetInfo`: The information of the time point screenshots generated.
            8. `keyFrameDescInfo`: The video timestamp information.
            9. `adaptiveDynamicStreamingInfo`: The specification, encryption type, format, etc.

        <div id="maxResultsDesc">Limits for returned records:</div>
        - The <b><a href="#p_offset">Offset</a> and <a href="#p_limit">Limit</a> parameters determine the number of records per page. If neither parameter is passed, this API will return up to 10 records.</b>
        - <b>Up to 5,000 records can be returned. If a request returns too many records, we recommend you use more specific search criteria to narrow down the results.</b>

        :param request: Request instance for SearchMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.SearchMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SearchMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchMedia", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchMediaResponse()
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
            if "Error" not in response["Response"]:
                model = models.SetDrmKeyProviderInfoResponse()
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

        ### Clipping for temporary sharing
        The video clip (an M3U8 file) shares the same TS segments with the input video instead of being an independent video. It only has a playback URL but has no `FileId`, and its validity period is the same as that of the input video. Once the input video is deleted, the video clip cannot be played back.

        Because the video clip is not an independent video, it’s not displayed as a media asset in the VOD console, and cannot be transcoded or published to WeChat.

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
            if "Error" not in response["Response"]:
                model = models.SimpleHlsClipResponse()
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