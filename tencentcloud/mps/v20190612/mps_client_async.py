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
from tencentcloud.mps.v20190612 import models
from typing import Dict


class MpsClient(AbstractClient):
    _apiVersion = '2019-06-12'
    _endpoint = 'mps.intl.tencentcloudapi.com'
    _service = 'mps'

    async def BatchProcessMedia(
            self,
            request: models.BatchProcessMediaRequest,
            opts: Dict = None,
    ) -> models.BatchProcessMediaResponse:
        """
        This API is used to initiate batch processing tasks for URL video links, with features including:
        Smart subtitle (full speech, speech hotword, and speech translation)
        """
        
        kwargs = {}
        kwargs["action"] = "BatchProcessMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchProcessMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIAnalysisTemplate(
            self,
            request: models.CreateAIAnalysisTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAIAnalysisTemplateResponse:
        """
        This API is used to create a custom content analysis template. Up to 50 templates can be created.
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
        This API is used to create a custom content recognition template. Up to 50 templates can be created.
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
        This API is used to create an adaptive bitrate streaming template. Up up to 100 such templates can be created.
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
        
    async def CreateAsrHotwords(
            self,
            request: models.CreateAsrHotwordsRequest,
            opts: Dict = None,
    ) -> models.CreateAsrHotwordsResponse:
        """
        This API is used to create a smart subtitle hotword lexicon.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAsrHotwords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAsrHotwordsResponse
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
        
    async def CreateContentReviewTemplate(
            self,
            request: models.CreateContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateContentReviewTemplateResponse:
        """
        This API is used to create a custom content moderation template. Up to 50 templates can be created in total.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateContentReviewTemplateResponse
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
        
    async def CreateLiveRecordTemplate(
            self,
            request: models.CreateLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveRecordTemplateResponse:
        """
        This API is used to create a live recording template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePersonSample(
            self,
            request: models.CreatePersonSampleRequest,
            opts: Dict = None,
    ) -> models.CreatePersonSampleResponse:
        """
        This API is used to create image samples for video processing operations such as content recognition and inappropriate information detection with the help of technologies such as facial feature positioning.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProcessImageTemplate(
            self,
            request: models.CreateProcessImageTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateProcessImageTemplateResponse:
        """
        This API is used to create an image processing template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProcessImageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProcessImageTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateQualityControlTemplate(
            self,
            request: models.CreateQualityControlTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateQualityControlTemplateResponse:
        """
        This API is used to create a media quality inspection template. Up to 50 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateQualityControlTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateQualityControlTemplateResponse
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
        
    async def CreateSchedule(
            self,
            request: models.CreateScheduleRequest,
            opts: Dict = None,
    ) -> models.CreateScheduleResponse:
        """
        This API is used to set processing rules for uploaded media files under the specified Bucket directory in COS, including:.
        This API is used to transcode videos with watermarks.
        This API is used to generate animated images.
        This API is used to take screenshots at specified time points.
        This API is used to take sampled screenshots from videos.
        This API is used to take sprite screenshots of videos.
        This API is used to transcode to adaptive bitrate streaming.
        This API is used to perform intelligent content moderation, including porn detection and sensitive information detection.
        This API is used to perform intelligent content analysis (tag, category, cover, frame tagging).
        This API is used to perform intelligent content identification (human face, full text, text keyword, full speech, speech keyword).
        10. Media quality inspection (live stream format diagnosis, audio and video content detection (jitter, blur, low light, overexposure, black and white edges, black and white screens, screen glitch, noise, mosaic, QR code, and more), and no-reference scoring).

        11. Smart subtitle (full speech, speech hotword, and speech translation).

        This API is used to perform intelligent erasure (watermark removal, subtitle removal, privacy protection).

        This API is used to create an orchestration, which is in disable status by default and requires manual enablement.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSmartEraseTemplate(
            self,
            request: models.CreateSmartEraseTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSmartEraseTemplateResponse:
        """
        This API is used to create a custom smart erasing template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSmartEraseTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSmartEraseTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSmartSubtitleTemplate(
            self,
            request: models.CreateSmartSubtitleTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSmartSubtitleTemplateResponse:
        """
        This API is used to create a custom smart subtitle template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSmartSubtitleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSmartSubtitleTemplateResponse
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
        
    async def CreateTranscodeTemplate(
            self,
            request: models.CreateTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateTranscodeTemplateResponse:
        """
        This API is used to create a custom transcoding template. Up to 1,000 templates can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTranscodeTemplateResponse
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
        This API is used to create keyword samples in batches for video processing operations such as content recognition and inappropriate information detection with the help of the OCR and ASR technologies.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWordSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWordSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflow(
            self,
            request: models.CreateWorkflowRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowResponse:
        """
        This API is used to create a workflow for media files uploaded to a specified COS bucket. A workflow may include the following tasks:
        1. Video transcoding (with watermark)
        2. Animated image generating
        3. Time point screencapturing
        4. Sampled screencapturing
        5. Image sprite generating
        6. Adaptive bitrate streaming
        7. Intelligent content moderation (detection of pornographic and sensitive content)
        8. Intelligent content analysis (labeling, categorization, thumbnail generation, frame-specific labeling)
        9. Intelligent content recognition (face, full text, text keyword, full speech, and speech keyword)

        Note: A workflow is disabled upon creation. You need to manually enable it.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIAnalysisTemplate(
            self,
            request: models.DeleteAIAnalysisTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAIAnalysisTemplateResponse:
        """
        This API is used to delete a custom content analysis template.

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
        This API is used to delete a custom content recognition template.
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
        
    async def DeleteAsrHotwords(
            self,
            request: models.DeleteAsrHotwordsRequest,
            opts: Dict = None,
    ) -> models.DeleteAsrHotwordsResponse:
        """
        This API is used to delete a smart subtitle hotword lexicon.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAsrHotwords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAsrHotwordsResponse
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
        
    async def DeleteContentReviewTemplate(
            self,
            request: models.DeleteContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteContentReviewTemplateResponse:
        """
        This API is used to delete a custom content moderation template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteContentReviewTemplateResponse
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
        
    async def DeleteLiveRecordTemplate(
            self,
            request: models.DeleteLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveRecordTemplateResponse:
        """
        This API is used to delete a live recording template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePersonSample(
            self,
            request: models.DeletePersonSampleRequest,
            opts: Dict = None,
    ) -> models.DeletePersonSampleResponse:
        """
        This API is used to delete image samples by image ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProcessImageTemplate(
            self,
            request: models.DeleteProcessImageTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteProcessImageTemplateResponse:
        """
        This API is used to delete an image processing template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProcessImageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProcessImageTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteQualityControlTemplate(
            self,
            request: models.DeleteQualityControlTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteQualityControlTemplateResponse:
        """
        This API is used to delete a media quality inspection template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteQualityControlTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteQualityControlTemplateResponse
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
        
    async def DeleteSchedule(
            self,
            request: models.DeleteScheduleRequest,
            opts: Dict = None,
    ) -> models.DeleteScheduleResponse:
        """
        This API is used to delete a scheme.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSmartEraseTemplate(
            self,
            request: models.DeleteSmartEraseTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSmartEraseTemplateResponse:
        """
        This API is used to delete a user-defined smart erasing template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmartEraseTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmartEraseTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSmartSubtitleTemplate(
            self,
            request: models.DeleteSmartSubtitleTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSmartSubtitleTemplateResponse:
        """
        This API is used to delete a user-defined smart subtitle template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmartSubtitleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmartSubtitleTemplateResponse
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
        
    async def DeleteWorkflow(
            self,
            request: models.DeleteWorkflowRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowResponse:
        """
        This API is used to delete a workflow. An enabled workflow must be disabled before it can be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisTemplates(
            self,
            request: models.DescribeAIAnalysisTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisTemplatesResponse:
        """
        This API is used to get the list of content analysis templates based on unique template ID. The returned result includes all eligible custom and preset video content analysis templates.
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
        This API is used to get the list of content recognition templates based on unique template ID. The return result includes all eligible custom and preset content recognition templates.
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
        This API is used to query the list of adaptive bitrate streaming templates and supports paginated queries by filters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAdaptiveDynamicStreamingTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAdaptiveDynamicStreamingTemplatesResponse
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
        
    async def DescribeAsrHotwords(
            self,
            request: models.DescribeAsrHotwordsRequest,
            opts: Dict = None,
    ) -> models.DescribeAsrHotwordsResponse:
        """
        This API is used to query a smart subtitle hotword lexicon.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsrHotwords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsrHotwordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsrHotwordsList(
            self,
            request: models.DescribeAsrHotwordsListRequest,
            opts: Dict = None,
    ) -> models.DescribeAsrHotwordsListResponse:
        """
        This API is used to obtain the hotword lexicon list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsrHotwordsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsrHotwordsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchTaskDetail(
            self,
            request: models.DescribeBatchTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchTaskDetailResponse:
        """
        This API is used to query the details of the task execution status and results by task ID (tasks submitted within the last 7 days can be queried).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlindWatermarkTemplates(
            self,
            request: models.DescribeBlindWatermarkTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeBlindWatermarkTemplatesResponse:
        """
        This API is used to query a user-defined digital watermark template, and the pagination query is supported based on conditions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlindWatermarkTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlindWatermarkTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContentReviewTemplates(
            self,
            request: models.DescribeContentReviewTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeContentReviewTemplatesResponse:
        """
        This API is used to query content moderation templates by template ID. Both custom and preset templates that match the template IDs passed in will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContentReviewTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContentReviewTemplatesResponse
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
        
    async def DescribeImageTaskDetail(
            self,
            request: models.DescribeImageTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeImageTaskDetailResponse:
        """
        This API is used to query the details of the task execution status and results by task ID (tasks submitted within the last 7 days can be queried).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveRecordTemplates(
            self,
            request: models.DescribeLiveRecordTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveRecordTemplatesResponse:
        """
        This API is used to get a live recording template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveRecordTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveRecordTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMediaMetaData(
            self,
            request: models.DescribeMediaMetaDataRequest,
            opts: Dict = None,
    ) -> models.DescribeMediaMetaDataResponse:
        """
        This API is used to get the metadata of media, such as video image width/height, codec, length, and frame rate.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMediaMetaData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMediaMetaDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePersonSamples(
            self,
            request: models.DescribePersonSamplesRequest,
            opts: Dict = None,
    ) -> models.DescribePersonSamplesResponse:
        """
        This API is used to query the information of image samples. It supports paginated queries by image ID, name, and tag.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePersonSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePersonSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessImageTemplates(
            self,
            request: models.DescribeProcessImageTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessImageTemplatesResponse:
        """
        This API is used to query the list of image processing templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessImageTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessImageTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityControlTemplates(
            self,
            request: models.DescribeQualityControlTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityControlTemplatesResponse:
        """
        This API is used to query custom media quality inspection templates, supporting paged queries by conditions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityControlTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityControlTemplatesResponse
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
        
    async def DescribeSchedules(
            self,
            request: models.DescribeSchedulesRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulesResponse:
        """
        This API is used to query a scheme.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmartEraseTemplates(
            self,
            request: models.DescribeSmartEraseTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSmartEraseTemplatesResponse:
        """
        This API is used to obtain the list of smart erasing template details based on the unique identifier of the template. The returned result includes all matching user-defined smart erasing templates and system preset smart erasing templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmartEraseTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmartEraseTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmartSubtitleTemplates(
            self,
            request: models.DescribeSmartSubtitleTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSmartSubtitleTemplatesResponse:
        """
        This API is used to obtain the list of smart subtitle templates based on template unique identifier. The returned result includes all matching user-defined smart subtitle templates and system preset smart subtitle templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmartSubtitleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmartSubtitleTemplatesResponse
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
        
    async def DescribeStreamLinkSecurityGroup(
            self,
            request: models.DescribeStreamLinkSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkSecurityGroupResponse:
        """
        This API is used to query a security group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkSecurityGroupResponse
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
        * This API is used to query tasks.
        * If the data is large, one API call may not be able to obtain all the tasks in the query. You can use the `ScrollToken` parameter to query tasks with multiple calls.
        * Only tasks in the last seven days (168 hours) can be queried.
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
        
    async def DescribeUsageData(
            self,
            request: models.DescribeUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeUsageDataResponse:
        """
        This API is used to return the daily Media Processing Service (MPS) usage information within the specified query time range.
           1. MPS statistical data from the last 365 days can be queried.
           2. The query time span should not exceed 90 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsageDataResponse
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
        This API is used to perform paged queries of keyword sample information by use case, keyword, and tag.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWordSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWordSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflows(
            self,
            request: models.DescribeWorkflowsRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowsResponse:
        """
        This API is used to get the list of workflow details by workflow ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableSchedule(
            self,
            request: models.DisableScheduleRequest,
            opts: Dict = None,
    ) -> models.DisableScheduleResponse:
        """
        This API is used to disable a scheme.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableWorkflow(
            self,
            request: models.DisableWorkflowRequest,
            opts: Dict = None,
    ) -> models.DisableWorkflowResponse:
        """
        This API is used to disable a workflow.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditMedia(
            self,
            request: models.EditMediaRequest,
            opts: Dict = None,
    ) -> models.EditMediaResponse:
        """
        This API is used to edit a video to generate a new one. Editing features include:


        1. **Editing task**: simple video editing, such as clipping and splicing.
        1) Edit a file to generate a new video.
        2) Splice multiple files to generate a new video.
        3) Edit multiple files and then splice them to generate a new video.

        2. **Compositing task**: Generate a new video by describing information through APIs.
        1) Multi-track (video, audio, and subtitles) and multi-type elements (video, image, audio, text, and empty).
        2) Image level: mapping, zoom in/out, arbitrary rotation, mirroring, and more.
        3) Audio level: volume control, fade in/out, mixing, and more.
        4) Video level: transition, playback speed adjustment, splicing, clipping, subtitles, picture-in-picture, audio-video separation, entrance and exit animations, and more.
        """
        
        kwargs = {}
        kwargs["action"] = "EditMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableSchedule(
            self,
            request: models.EnableScheduleRequest,
            opts: Dict = None,
    ) -> models.EnableScheduleResponse:
        """
        This API is used to enable a scheme.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableWorkflow(
            self,
            request: models.EnableWorkflowRequest,
            opts: Dict = None,
    ) -> models.EnableWorkflowResponse:
        """
        This API is used to enable a workflow.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteFunction(
            self,
            request: models.ExecuteFunctionRequest,
            opts: Dict = None,
    ) -> models.ExecuteFunctionResponse:
        """
        This API is reserved for special circumstances. Do not use it unless you are directed to use it by technical support.
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
        This API is used to modify a custom content analysis template.

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
        This API is used to modify a custom content recognition template.
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
        
    async def ModifyAsrHotwords(
            self,
            request: models.ModifyAsrHotwordsRequest,
            opts: Dict = None,
    ) -> models.ModifyAsrHotwordsResponse:
        """
        This API is used to update a smart subtitle hotword lexicon.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAsrHotwords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAsrHotwordsResponse
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
        
    async def ModifyContentReviewTemplate(
            self,
            request: models.ModifyContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyContentReviewTemplateResponse:
        """
        This API is used to modify a custom content moderation template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContentReviewTemplateResponse
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
        
    async def ModifyLiveRecordTemplate(
            self,
            request: models.ModifyLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveRecordTemplateResponse:
        """
        This API is used to modify a live recording template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPersonSample(
            self,
            request: models.ModifyPersonSampleRequest,
            opts: Dict = None,
    ) -> models.ModifyPersonSampleResponse:
        """
        This API is used to modify image samples by image ID. You can use it to modify the name and description of an image sample and add/delete/reset facial features or tags. There must be at least one image left after the deletion of facial features; otherwise, please reset instead of delete the facial features.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProcessImageTemplate(
            self,
            request: models.ModifyProcessImageTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyProcessImageTemplateResponse:
        """
        This API is used to modify an image processing template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProcessImageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProcessImageTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyQualityControlTemplate(
            self,
            request: models.ModifyQualityControlTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyQualityControlTemplateResponse:
        """
        This API is used to modify a media quality inspection template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyQualityControlTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyQualityControlTemplateResponse
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
        
    async def ModifySchedule(
            self,
            request: models.ModifyScheduleRequest,
            opts: Dict = None,
    ) -> models.ModifyScheduleResponse:
        """
        This API is used to modify a scheme.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySmartEraseTemplate(
            self,
            request: models.ModifySmartEraseTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifySmartEraseTemplateResponse:
        """
        This API is used to modify a user-defined smart erasing template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySmartEraseTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySmartEraseTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySmartSubtitleTemplate(
            self,
            request: models.ModifySmartSubtitleTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifySmartSubtitleTemplateResponse:
        """
        This API is used to modify a user-defined smart subtitle template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySmartSubtitleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySmartSubtitleTemplateResponse
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
        
    async def ParseLiveStreamProcessNotification(
            self,
            request: models.ParseLiveStreamProcessNotificationRequest,
            opts: Dict = None,
    ) -> models.ParseLiveStreamProcessNotificationResponse:
        """
        This API is used to parse the content of an MPS live stream processing event notification from the `msgBody` field in the message received from CMQ.
        Instead of initiating a video processing task, this API is used to help generate SDKs for various programming languages. You can parse the event notification based on the analytic function of the SDKs.
        """
        
        kwargs = {}
        kwargs["action"] = "ParseLiveStreamProcessNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseLiveStreamProcessNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseNotification(
            self,
            request: models.ParseNotificationRequest,
            opts: Dict = None,
    ) -> models.ParseNotificationResponse:
        """
        This API is used to parse the content of an MPS event notification from the `msgBody` field in the message received from CMQ.
        Instead of initiating a video processing task, this API is used to help generate SDKs for various programming languages. You can parse the event notification based on the analytic function of the SDKs.
        """
        
        kwargs = {}
        kwargs["action"] = "ParseNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessImage(
            self,
            request: models.ProcessImageRequest,
            opts: Dict = None,
    ) -> models.ProcessImageResponse:
        """
        This API is used to initiate image processing, with features including:
        1. Format conversion.
        2. Image enhancement.
        3. Image erasure.
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessLiveStream(
            self,
            request: models.ProcessLiveStreamRequest,
            opts: Dict = None,
    ) -> models.ProcessLiveStreamResponse:
        """
        This API is used to initiate live stream processing tasks. Such tasks may include the following:

        * Intelligent content moderation (detection of pornographic content in images and audio, detection of sensitive information)
        * Intelligent content recognition (face, full text, text keyword, full speech, speech keyword, real-time speech translation, object recognition, game event tracking)
        * Intelligent content analysis (real-time news splitting)
        * Quality control, including recognizing live stream format, checking audio/video content for flickering, blur, low light, overexposure, black bars, white bars, black screen, white screen, noise, pixelation, QR code, etc., and no-reference scoring.
        * Recording

        HTTP callbacks are supported for live stream processing events. Notifications can also be written in real time to and read from a CMQ queue. The output files of processing tasks are saved to the storage you specify.
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMedia(
            self,
            request: models.ProcessMediaRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaResponse:
        """
        This API is used to initiate a processing task for video URLs or media files in Cloud Object Storage (COS). Features include:
        - Audio/Video transcoding (such as standard transcoding, top speed codec (TSC) transcoding, audio/video enhancement, visible watermark addition, and digital watermark addition).
        - Adaptive bitrate streaming conversion for audios/videos.
        - Video-to-GIF conversion.
        - Time point screenshot of videos.
        - Sampled screenshot of videos.
        - Image sprite of video screenshots.
        - Media quality inspection (such as media format diagnosis, audio/video content detection, and scoring without reference, where audio/video content detection mainly covers jitter, blur, low light, overexposure, screen glitches, noise, mosaic, QR code, and other issues).
        - Smart subtitle (such as subtitle generation and translation).
        - Smart erasing (such as watermark removal, subtitle removal, and privacy protection).
        - Smart content moderation (such as pornography detection and sensitive information detection).
        - Smart content analysis (such as tags, classifications, covers, frame tags, video splitting, highlights, opening and ending clips, and marking points for games).
        - Smart content recognition (such as human faces, full texts, text keywords, full speech, speech keywords, speech translation, and object recognition).
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetWorkflow(
            self,
            request: models.ResetWorkflowRequest,
            opts: Dict = None,
    ) -> models.ResetWorkflowResponse:
        """
        This API is used to reset an existing workflow that is disabled.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)