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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AIAnalysisTemplateItem(AbstractModel):
    """AI-based intelligent analysis template details

    """

    def __init__(self):
        """
        :param Definition: Unique ID of intelligent analysis template.\n        :type Definition: int\n        :param Name: Intelligent analysis template name.\n        :type Name: str\n        :param Comment: Intelligent analysis template description.\n        :type Comment: str\n        :param ClassificationConfigure: Control parameter of intelligent categorization task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClassificationConfigure: :class:`tencentcloud.vod.v20180717.models.ClassificationConfigureInfo`\n        :param TagConfigure: Control parameter of intelligent tagging task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TagConfigure: :class:`tencentcloud.vod.v20180717.models.TagConfigureInfo`\n        :param CoverConfigure: Control parameter of intelligent cover generating task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CoverConfigure: :class:`tencentcloud.vod.v20180717.models.CoverConfigureInfo`\n        :param FrameTagConfigure: Control parameter of intelligent frame-specific tagging task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FrameTagConfigure: :class:`tencentcloud.vod.v20180717.models.FrameTagConfigureInfo`\n        :param HighlightConfigure: Control parameter of an intelligent highlight generating task.\n        :type HighlightConfigure: :class:`tencentcloud.vod.v20180717.models.HighlightsConfigureInfo`\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.HighlightConfigure = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        if params.get("HighlightConfigure") is not None:
            self.HighlightConfigure = HighlightsConfigureInfo()
            self.HighlightConfigure._deserialize(params.get("HighlightConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIRecognitionTemplateItem(AbstractModel):
    """Video content recognition template details

    """

    def __init__(self):
        """
        :param Definition: Unique ID of video content recognition template.\n        :type Definition: int\n        :param Name: Video content recognition template name.\n        :type Name: str\n        :param Comment: Video content recognition template description.\n        :type Comment: str\n        :param HeadTailConfigure: Control parameter of opening and closing credits recognition.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HeadTailConfigure: :class:`tencentcloud.vod.v20180717.models.HeadTailConfigureInfo`\n        :param SegmentConfigure: Control parameter of splitting recognition.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SegmentConfigure: :class:`tencentcloud.vod.v20180717.models.SegmentConfigureInfo`\n        :param FaceConfigure: Face recognition control parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FaceConfigure: :class:`tencentcloud.vod.v20180717.models.FaceConfigureInfo`\n        :param OcrFullTextConfigure: Full text recognition control parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OcrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.OcrFullTextConfigureInfo`\n        :param OcrWordsConfigure: Text keyword recognition control parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OcrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.OcrWordsConfigureInfo`\n        :param AsrFullTextConfigure: Full speech recognition control parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.AsrFullTextConfigureInfo`\n        :param AsrWordsConfigure: Speech keyword recognition control parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.AsrWordsConfigureInfo`\n        :param ObjectConfigure: Control parameter of object recognition.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ObjectConfigure: :class:`tencentcloud.vod.v20180717.models.ObjectConfigureInfo`\n        :param ScreenshotInterval: Screencapturing interval in seconds.\n        :type ScreenshotInterval: float\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.HeadTailConfigure = None
        self.SegmentConfigure = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.ObjectConfigure = None
        self.ScreenshotInterval = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("HeadTailConfigure") is not None:
            self.HeadTailConfigure = HeadTailConfigureInfo()
            self.HeadTailConfigure._deserialize(params.get("HeadTailConfigure"))
        if params.get("SegmentConfigure") is not None:
            self.SegmentConfigure = SegmentConfigureInfo()
            self.SegmentConfigure._deserialize(params.get("SegmentConfigure"))
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        if params.get("ObjectConfigure") is not None:
            self.ObjectConfigure = ObjectConfigureInfo()
            self.ObjectConfigure._deserialize(params.get("ObjectConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccelerateAreaInfo(AbstractModel):
    """Acceleration region information of the domain name

    """

    def __init__(self):
        """
        :param Area: Acceleration region. Valid values:
<li>Chinese Mainland</li>
<li>Outside Chinese Mainland</li>\n        :type Area: str\n        :param TencentDisableReason: Reason why acceleration is disabled by Tencent Cloud. Valid values:
<li>ForLegalReasons: legal reasons</li>
<li>ForOverdueBills: overdue payment</li>\n        :type TencentDisableReason: str\n        :param TencentEdgeDomain: CNAME of the acceleration domain name\n        :type TencentEdgeDomain: str\n        """
        self.Area = None
        self.TencentDisableReason = None
        self.TencentEdgeDomain = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        self.TencentDisableReason = params.get("TencentDisableReason")
        self.TencentEdgeDomain = params.get("TencentEdgeDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingInfoItem(AbstractModel):
    """Adaptive bitrate streaming information

    """

    def __init__(self):
        """
        :param Definition: Adaptive bitrate streaming specification.\n        :type Definition: int\n        :param Package: Container format. Valid values: hls, dash.\n        :type Package: str\n        :param DrmType: Encryption type.\n        :type DrmType: str\n        :param Url: Playback address.\n        :type Url: str\n        """
        self.Definition = None
        self.Package = None
        self.DrmType = None
        self.Url = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Package = params.get("Package")
        self.DrmType = params.get("DrmType")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingTaskInput(AbstractModel):
    """Input parameter type of adaptive bitrate streaming

    """

    def __init__(self):
        """
        :param Definition: Adaptive bitrate streaming template ID.\n        :type Definition: int\n        :param WatermarkSet: List of up to 10 image or text watermarks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WatermarkSet: list of WatermarkInput\n        :param SubtitleSet: List of subtitle IDs (maximum: 16)\n        :type SubtitleSet: list of str\n        """
        self.Definition = None
        self.WatermarkSet = None
        self.SubtitleSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        self.SubtitleSet = params.get("SubtitleSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingTemplate(AbstractModel):
    """Details of a transcoding to adaptive bitrate streaming template

    """

    def __init__(self):
        """
        :param Definition: Unique ID of a transcoding to adaptive bitrate streaming template.\n        :type Definition: int\n        :param Type: Template type. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param Name: Name of a transcoding to adaptive bitrate streaming template.\n        :type Name: str\n        :param Comment: Description of a transcoding to adaptive bitrate streaming template.\n        :type Comment: str\n        :param Format: Adaptive bitstream format. Valid value:
<li>HLS.</li>\n        :type Format: str\n        :param DrmType: DRM type. Valid values:
<li>FairPlay;</li>
<li>SimpleAES;</li>
<li>Widevine.</li>
If this field is a blank string, DRM will not be performed on the video.\n        :type DrmType: str\n        :param StreamInfos: Parameter information of input stream for adaptive bitrate streaming. Up to 10 streams can be input.\n        :type StreamInfos: list of AdaptiveStreamTemplate\n        :param DisableHigherVideoBitrate: Whether to prohibit transcoding from low bitrate to high bitrate. Valid values:
<li>0: no,</li>
<li>1: yes.</li>\n        :type DisableHigherVideoBitrate: int\n        :param DisableHigherVideoResolution: Whether to prohibit transcoding from low resolution to high resolution. Valid values:
<li>0: no,</li>
<li>1: yes.</li>\n        :type DisableHigherVideoResolution: int\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Format = None
        self.DrmType = None
        self.StreamInfos = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Format = params.get("Format")
        self.DrmType = params.get("DrmType")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveStreamTemplate(AbstractModel):
    """Adaptive bitrate streaming parameter template

    """

    def __init__(self):
        """
        :param Video: Video parameter information.\n        :type Video: :class:`tencentcloud.vod.v20180717.models.VideoTemplateInfo`\n        :param Audio: Audio parameter information.\n        :type Audio: :class:`tencentcloud.vod.v20180717.models.AudioTemplateInfo`\n        :param RemoveAudio: Whether to remove audio stream. Valid values:
<li>0: no,</li>
<li>1: yes.</li>\n        :type RemoveAudio: int\n        :param RemoveVideo: Whether to remove a video stream. Valid values:
<li>0: no</li>
<li>1: yes</li>\n        :type RemoveVideo: int\n        """
        self.Video = None
        self.Audio = None
        self.RemoveAudio = None
        self.RemoveVideo = None


    def _deserialize(self, params):
        if params.get("Video") is not None:
            self.Video = VideoTemplateInfo()
            self.Video._deserialize(params.get("Video"))
        if params.get("Audio") is not None:
            self.Audio = AudioTemplateInfo()
            self.Audio._deserialize(params.get("Audio"))
        self.RemoveAudio = params.get("RemoveAudio")
        self.RemoveVideo = params.get("RemoveVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisResult(AbstractModel):
    """Intelligent analysis result

    """

    def __init__(self):
        """
        :param Type: Task type. Valid values:
<li>Classification: intelligent categorization</li>
<li>Cover: intelligent cover generating</li>
<li>Tag: intelligent tagging</li>
<li>FrameTag: intelligent frame tagging</li>
<li>Highlight: intelligent highlight generating</li>\n        :type Type: str\n        :param ClassificationTask: Query result of intelligent categorization task in video content analysis, which is valid if task type is `Classification`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClassificationTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskClassificationResult`\n        :param CoverTask: Query result of intelligent cover generating task in video content analysis, which is valid if task type is `Cover`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CoverTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskCoverResult`\n        :param TagTask: Query result of intelligent tagging task in video content analysis, which is valid if task type is `Tag`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TagTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskTagResult`\n        :param FrameTagTask: Query result of intelligent frame-specific tagging task in video content analysis, which is valid if task type is `FrameTag`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FrameTagTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskFrameTagResult`\n        :param HighlightTask: Query result of an intelligent highlight generating task in video content analysis, which is valid when task type is `Highlight`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HighlightTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskHighlightResult`\n        """
        self.Type = None
        self.ClassificationTask = None
        self.CoverTask = None
        self.TagTask = None
        self.FrameTagTask = None
        self.HighlightTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("ClassificationTask") is not None:
            self.ClassificationTask = AiAnalysisTaskClassificationResult()
            self.ClassificationTask._deserialize(params.get("ClassificationTask"))
        if params.get("CoverTask") is not None:
            self.CoverTask = AiAnalysisTaskCoverResult()
            self.CoverTask._deserialize(params.get("CoverTask"))
        if params.get("TagTask") is not None:
            self.TagTask = AiAnalysisTaskTagResult()
            self.TagTask._deserialize(params.get("TagTask"))
        if params.get("FrameTagTask") is not None:
            self.FrameTagTask = AiAnalysisTaskFrameTagResult()
            self.FrameTagTask._deserialize(params.get("FrameTagTask"))
        if params.get("HighlightTask") is not None:
            self.HighlightTask = AiAnalysisTaskHighlightResult()
            self.HighlightTask._deserialize(params.get("HighlightTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationInput(AbstractModel):
    """Input type of intelligent categorization task

    """

    def __init__(self):
        """
        :param Definition: Intelligent video categorization template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationOutput(AbstractModel):
    """Result information of intelligent categorization

    """

    def __init__(self):
        """
        :param ClassificationSet: List of intelligently generated video categories.\n        :type ClassificationSet: list of MediaAiAnalysisClassificationItem\n        """
        self.ClassificationSet = None


    def _deserialize(self, params):
        if params.get("ClassificationSet") is not None:
            self.ClassificationSet = []
            for item in params.get("ClassificationSet"):
                obj = MediaAiAnalysisClassificationItem()
                obj._deserialize(item)
                self.ClassificationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationResult(AbstractModel):
    """Result type of intelligent categorization task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input of intelligent categorization task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskClassificationInput`\n        :param Output: Output of intelligent categorization task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskClassificationOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskClassificationInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskClassificationOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverInput(AbstractModel):
    """Input type of intelligent categorization task

    """

    def __init__(self):
        """
        :param Definition: Intelligent video cover generating template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverOutput(AbstractModel):
    """Result information of intelligent cover generating

    """

    def __init__(self):
        """
        :param CoverSet: List of intelligently generated covers.\n        :type CoverSet: list of MediaAiAnalysisCoverItem\n        """
        self.CoverSet = None


    def _deserialize(self, params):
        if params.get("CoverSet") is not None:
            self.CoverSet = []
            for item in params.get("CoverSet"):
                obj = MediaAiAnalysisCoverItem()
                obj._deserialize(item)
                self.CoverSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverResult(AbstractModel):
    """Result type of intelligent cover generating task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input of intelligent cover generating task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskCoverInput`\n        :param Output: Output of intelligent cover generating task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskCoverOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskCoverInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskCoverOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagInput(AbstractModel):
    """Input type of intelligent frame-specific tagging task

    """

    def __init__(self):
        """
        :param Definition: Intelligent frame-specific video tagging template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagOutput(AbstractModel):
    """Result information of intelligent frame-specific tagging

    """

    def __init__(self):
        """
        :param SegmentSet: List of frame-specific video tags.\n        :type SegmentSet: list of MediaAiAnalysisFrameTagSegmentItem\n        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaAiAnalysisFrameTagSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagResult(AbstractModel):
    """Result type of intelligent frame-specific tagging

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input of intelligent frame-specific tagging task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskFrameTagInput`\n        :param Output: Output of intelligent frame-specific tagging task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskFrameTagOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskFrameTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskFrameTagOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskHighlightInput(AbstractModel):
    """Input type of an intelligent highlight generating task

    """

    def __init__(self):
        """
        :param Definition: ID of an intelligent highlight generating template.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskHighlightOutput(AbstractModel):
    """Information of the intelligent highlight generating result

    """

    def __init__(self):
        """
        :param HighlightSet: List of intelligently generated highlights.\n        :type HighlightSet: list of MediaAiAnalysisHighlightItem\n        """
        self.HighlightSet = None


    def _deserialize(self, params):
        if params.get("HighlightSet") is not None:
            self.HighlightSet = []
            for item in params.get("HighlightSet"):
                obj = MediaAiAnalysisHighlightItem()
                obj._deserialize(item)
                self.HighlightSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskHighlightResult(AbstractModel):
    """Result type of an intelligent highlight generating task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input for an intelligent highlight generating task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskHighlightInput`\n        :param Output: Output of an intelligent highlight generating task.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskHighlightOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskHighlightInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskHighlightOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskInput(AbstractModel):
    """Input parameter type of AI-based intelligent video analysis

    """

    def __init__(self):
        """
        :param Definition: Video content analysis template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagInput(AbstractModel):
    """Input type of intelligent tagging task

    """

    def __init__(self):
        """
        :param Definition: Intelligent video tagging template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagOutput(AbstractModel):
    """Result information of intelligent tagging

    """

    def __init__(self):
        """
        :param TagSet: List of intelligently generated video tags.\n        :type TagSet: list of MediaAiAnalysisTagItem\n        """
        self.TagSet = None


    def _deserialize(self, params):
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagResult(AbstractModel):
    """Result type of intelligent tagging task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input of intelligent tagging task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskTagInput`\n        :param Output: Output of intelligent tagging task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskTagOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskTagOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiContentReviewResult(AbstractModel):
    """Content audit result

    """

    def __init__(self):
        """
        :param Type: Task type. Valid values:
<li>Porn: porn information detection in image</li>
<li>Terrorism: terrorism information detection in image</li>
<li>Political: politically sensitive information detection in image</li>
<li>Porn.Asr: ASR-based porn information detection in speech</li>
<li>Porn.Ocr: OCR-based porn information detection in text</li>
<li>Political.Asr: ASR-based politically sensitive information detection in speech</li>
<li>Political.Ocr: OCR-based politically sensitive information detection in text</li>
<li>Terrorism.Ocr: OCR-based terrorism information in text</li>
<li>Prohibited.Asr: ASR-based prohibited information detection in speech</li>
<li>Prohibited.Ocr: OCR-based prohibited information detection in text</li>\n        :type Type: str\n        :param PornTask: Query result of intelligent porn information detection in video image task in video content audit, which is valid when task type is `Porn`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PornTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPornResult`\n        :param TerrorismTask: Query result of intelligent terrorism information detection in video image task in video content audit, which is valid when task type is `Terrorism`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TerrorismTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskTerrorismResult`\n        :param PoliticalTask: Query result of intelligent politically sensitive information detection in video image task in video content audit, which is valid when task type is `Political`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PoliticalTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPoliticalResult`\n        :param PornAsrTask: Query result of ASR-based porn information detection in speech task in video content audit, which is valid when task type is `Porn.Asr`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PornAsrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPornAsrResult`\n        :param PornOcrTask: Query result of OCR-based porn information detection in text task in video content audit, which is valid when task type is `Porn.Ocr`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PornOcrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPornOcrResult`\n        :param PoliticalAsrTask: Query result of ASR-based politically sensitive information detection in speech task in video content audit, which is valid when task type is `Political.Asr`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PoliticalAsrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPoliticalAsrResult`\n        :param PoliticalOcrTask: Query result of OCR-based politically sensitive information detection in text task in video content audit, which is valid when task type is `Political.Ocr`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PoliticalOcrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPoliticalOcrResult`\n        :param TerrorismOcrTask: Query result of OCR-based terrorism information detection in text task in video content audit, which is valid when task type is `Terrorism.Ocr`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TerrorismOcrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskTerrorismOcrResult`\n        :param ProhibitedAsrTask: Query result of ASR-based prohibited information detection in speech task in video content audit, which is valid when task type is `Prohibited.Asr`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProhibitedAsrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskProhibitedAsrResult`\n        :param ProhibitedOcrTask: Query result of OCR-based prohibited information detection in text task in video content audit, which is valid when task type is `Prohibited.Ocr`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProhibitedOcrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskProhibitedOcrResult`\n        """
        self.Type = None
        self.PornTask = None
        self.TerrorismTask = None
        self.PoliticalTask = None
        self.PornAsrTask = None
        self.PornOcrTask = None
        self.PoliticalAsrTask = None
        self.PoliticalOcrTask = None
        self.TerrorismOcrTask = None
        self.ProhibitedAsrTask = None
        self.ProhibitedOcrTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("PornTask") is not None:
            self.PornTask = AiReviewTaskPornResult()
            self.PornTask._deserialize(params.get("PornTask"))
        if params.get("TerrorismTask") is not None:
            self.TerrorismTask = AiReviewTaskTerrorismResult()
            self.TerrorismTask._deserialize(params.get("TerrorismTask"))
        if params.get("PoliticalTask") is not None:
            self.PoliticalTask = AiReviewTaskPoliticalResult()
            self.PoliticalTask._deserialize(params.get("PoliticalTask"))
        if params.get("PornAsrTask") is not None:
            self.PornAsrTask = AiReviewTaskPornAsrResult()
            self.PornAsrTask._deserialize(params.get("PornAsrTask"))
        if params.get("PornOcrTask") is not None:
            self.PornOcrTask = AiReviewTaskPornOcrResult()
            self.PornOcrTask._deserialize(params.get("PornOcrTask"))
        if params.get("PoliticalAsrTask") is not None:
            self.PoliticalAsrTask = AiReviewTaskPoliticalAsrResult()
            self.PoliticalAsrTask._deserialize(params.get("PoliticalAsrTask"))
        if params.get("PoliticalOcrTask") is not None:
            self.PoliticalOcrTask = AiReviewTaskPoliticalOcrResult()
            self.PoliticalOcrTask._deserialize(params.get("PoliticalOcrTask"))
        if params.get("TerrorismOcrTask") is not None:
            self.TerrorismOcrTask = AiReviewTaskTerrorismOcrResult()
            self.TerrorismOcrTask._deserialize(params.get("TerrorismOcrTask"))
        if params.get("ProhibitedAsrTask") is not None:
            self.ProhibitedAsrTask = AiReviewTaskProhibitedAsrResult()
            self.ProhibitedAsrTask._deserialize(params.get("ProhibitedAsrTask"))
        if params.get("ProhibitedOcrTask") is not None:
            self.ProhibitedOcrTask = AiReviewTaskProhibitedOcrResult()
            self.ProhibitedOcrTask._deserialize(params.get("ProhibitedOcrTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiContentReviewTaskInput(AbstractModel):
    """Task type of intelligent content audit

    """

    def __init__(self):
        """
        :param Definition: Video content audit template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionResult(AbstractModel):
    """Intelligent recognition result.

    """

    def __init__(self):
        """
        :param Type: Task type. Valid values:
<li>FaceRecognition: face recognition,</li>
<li>AsrWordsRecognition: speech keyword recognition,</li>
<li>OcrWordsRecognition: text keyword recognition,</li>
<li>AsrFullTextRecognition: full speech recognition,</li>
<li>OcrFullTextRecognition: full text recognition,</li>
<li>HeadTailRecognition: video opening and ending credits recognition,</li>
<li>ObjectRecognition: object recognition.</li>\n        :type Type: str\n        :param HeadTailTask: Video opening and ending credits recognition result, which is valid when `Type` is
 `HeadTailRecognition`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HeadTailTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskHeadTailResult`\n        :param SegmentTask: Video splitting recognition result, which is valid when `Type` is
 `SegmentRecognition`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SegmentTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskSegmentResult`\n        :param FaceTask: Face recognition result, which is valid when `Type` is 
 `FaceRecognition`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FaceTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskFaceResult`\n        :param AsrWordsTask: Speech keyword recognition result, which is valid when `Type` is
 `AsrWordsRecognition`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsrWordsTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResult`\n        :param AsrFullTextTask: Full speech recognition result, which is valid when `Type` is
 `AsrFullTextRecognition`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsrFullTextTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrFullTextResult`\n        :param OcrWordsTask: Text keyword recognition result, which is valid when `Type` is
 `OcrWordsRecognition`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OcrWordsTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResult`\n        :param OcrFullTextTask: Full text recognition result, which is valid when `Type` is
 `OcrFullTextRecognition`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OcrFullTextTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrFullTextResult`\n        :param ObjectTask: Object recognition result, which is valid when `Type` is
 `ObjectRecognition`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ObjectTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskObjectResult`\n        """
        self.Type = None
        self.HeadTailTask = None
        self.SegmentTask = None
        self.FaceTask = None
        self.AsrWordsTask = None
        self.AsrFullTextTask = None
        self.OcrWordsTask = None
        self.OcrFullTextTask = None
        self.ObjectTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("HeadTailTask") is not None:
            self.HeadTailTask = AiRecognitionTaskHeadTailResult()
            self.HeadTailTask._deserialize(params.get("HeadTailTask"))
        if params.get("SegmentTask") is not None:
            self.SegmentTask = AiRecognitionTaskSegmentResult()
            self.SegmentTask._deserialize(params.get("SegmentTask"))
        if params.get("FaceTask") is not None:
            self.FaceTask = AiRecognitionTaskFaceResult()
            self.FaceTask._deserialize(params.get("FaceTask"))
        if params.get("AsrWordsTask") is not None:
            self.AsrWordsTask = AiRecognitionTaskAsrWordsResult()
            self.AsrWordsTask._deserialize(params.get("AsrWordsTask"))
        if params.get("AsrFullTextTask") is not None:
            self.AsrFullTextTask = AiRecognitionTaskAsrFullTextResult()
            self.AsrFullTextTask._deserialize(params.get("AsrFullTextTask"))
        if params.get("OcrWordsTask") is not None:
            self.OcrWordsTask = AiRecognitionTaskOcrWordsResult()
            self.OcrWordsTask._deserialize(params.get("OcrWordsTask"))
        if params.get("OcrFullTextTask") is not None:
            self.OcrFullTextTask = AiRecognitionTaskOcrFullTextResult()
            self.OcrFullTextTask._deserialize(params.get("OcrFullTextTask"))
        if params.get("ObjectTask") is not None:
            self.ObjectTask = AiRecognitionTaskObjectResult()
            self.ObjectTask._deserialize(params.get("ObjectTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResult(AbstractModel):
    """Full speech recognition result.

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input information of full speech recognition task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrFullTextResultInput`\n        :param Output: Output information of full speech recognition task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrFullTextResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResultInput(AbstractModel):
    """Input of full speech recognition.

    """

    def __init__(self):
        """
        :param Definition: Full speech recognition template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResultOutput(AbstractModel):
    """Full speech recognition result.

    """

    def __init__(self):
        """
        :param SegmentSet: List of full speech recognition segments.\n        :type SegmentSet: list of AiRecognitionTaskAsrFullTextSegmentItem\n        :param SubtitleUrl: Subtitles file URL.\n        :type SubtitleUrl: str\n        """
        self.SegmentSet = None
        self.SubtitleUrl = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        self.SubtitleUrl = params.get("SubtitleUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextSegmentItem(AbstractModel):
    """Full speech recognition segment.

    """

    def __init__(self):
        """
        :param Confidence: Confidence of recognized segment. Value range: 0-100.\n        :type Confidence: float\n        :param StartTimeOffset: Start time offset of recognized segment in seconds.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of recognition segment in seconds.\n        :type EndTimeOffset: float\n        :param Text: Recognized text.\n        :type Text: str\n        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResult(AbstractModel):
    """Speech keyword recognition result.

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input information of speech keyword recognition task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResultInput`\n        :param Output: Output information of speech keyword recognition task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultInput(AbstractModel):
    """Input of speech keyword recognition.

    """

    def __init__(self):
        """
        :param Definition: Speech keyword recognition template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultItem(AbstractModel):
    """Speech keyword recognition result.

    """

    def __init__(self):
        """
        :param Word: Speech keyword.\n        :type Word: str\n        :param SegmentSet: List of time segments that contain the speech keyword.\n        :type SegmentSet: list of AiRecognitionTaskAsrWordsSegmentItem\n        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultOutput(AbstractModel):
    """Output of speech keyword recognition.

    """

    def __init__(self):
        """
        :param ResultSet: Speech keyword recognition result set.\n        :type ResultSet: list of AiRecognitionTaskAsrWordsResultItem\n        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskAsrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsSegmentItem(AbstractModel):
    """Speech recognition segment.

    """

    def __init__(self):
        """
        :param StartTimeOffset: Start time offset of recognized segment in seconds.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of recognition segment in seconds.\n        :type EndTimeOffset: float\n        :param Confidence: Confidence of recognized segment. Value range: 0-100.\n        :type Confidence: float\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResult(AbstractModel):
    """Face recognition result.

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input information of face recognition task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskFaceResultInput`\n        :param Output: Output information of face recognition task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskFaceResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskFaceResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskFaceResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultInput(AbstractModel):
    """Face recognition input.

    """

    def __init__(self):
        """
        :param Definition: Face recognition template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultItem(AbstractModel):
    """Face recognition result

    """

    def __init__(self):
        """
        :param Id: Unique ID of figure.\n        :type Id: str\n        :param Type: Figure library type, indicating to which figure library the recognized figure belongs:
<li>Default: default figure library;</li>
<li>UserDefine: custom figure library.</li>\n        :type Type: str\n        :param Name: Figure name.\n        :type Name: str\n        :param SegmentSet: Result set of segments that contain a figure.\n        :type SegmentSet: list of AiRecognitionTaskFaceSegmentItem\n        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskFaceSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultOutput(AbstractModel):
    """Output of intelligent face recognition.

    """

    def __init__(self):
        """
        :param ResultSet: Intelligent face recognition result set.\n        :type ResultSet: list of AiRecognitionTaskFaceResultItem\n        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskFaceResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceSegmentItem(AbstractModel):
    """Face recognition result segment

    """

    def __init__(self):
        """
        :param StartTimeOffset: Start time offset of recognized segment in seconds.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of recognition segment in seconds.\n        :type EndTimeOffset: float\n        :param Confidence: Confidence of recognized segment. Value range: 0-100.\n        :type Confidence: float\n        :param AreaCoordSet: Zone coordinates of recognition result. The array contains four elements: [x1,y1,x2,y2], i.e., the horizontal and vertical coordinates of the top-left and bottom-right corners.\n        :type AreaCoordSet: list of int\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskHeadTailResult(AbstractModel):
    """Video opening and ending credits recognition result.

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input information of video opening and ending credits recognition task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskHeadTailResultInput`\n        :param Output: Output information of video opening and ending credits recognition task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskHeadTailResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskHeadTailResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskHeadTailResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskHeadTailResultInput(AbstractModel):
    """Input of video opening and ending credits recognition.

    """

    def __init__(self):
        """
        :param Definition: Video opening and ending credits recognition template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskHeadTailResultOutput(AbstractModel):
    """Output of video opening and ending credits recognition.

    """

    def __init__(self):
        """
        :param HeadConfidence: Confidence of recognized opening credits. Value range: 0-100.\n        :type HeadConfidence: float\n        :param HeadTimeOffset: End time point of video opening credits in seconds.\n        :type HeadTimeOffset: float\n        :param TailConfidence: Confidence of recognized closing credits. Value range: 0-100.\n        :type TailConfidence: float\n        :param TailTimeOffset: Start time point of video closing credits in seconds.\n        :type TailTimeOffset: float\n        """
        self.HeadConfidence = None
        self.HeadTimeOffset = None
        self.TailConfidence = None
        self.TailTimeOffset = None


    def _deserialize(self, params):
        self.HeadConfidence = params.get("HeadConfidence")
        self.HeadTimeOffset = params.get("HeadTimeOffset")
        self.TailConfidence = params.get("TailConfidence")
        self.TailTimeOffset = params.get("TailTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskInput(AbstractModel):
    """Input parameter type of video content recognition

    """

    def __init__(self):
        """
        :param Definition: Intelligent video recognition template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskObjectResult(AbstractModel):
    """Object recognition result.

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input information of object recognition task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskObjectResultInput`\n        :param Output: Output information of object recognition task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskObjectResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskObjectResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskObjectResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskObjectResultInput(AbstractModel):
    """Input type of object recognition task.

    """

    def __init__(self):
        """
        :param Definition: Object recognition template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskObjectResultItem(AbstractModel):
    """Single-object recognition result.

    """

    def __init__(self):
        """
        :param Name: Name of recognized object.\n        :type Name: str\n        :param SegmentSet: List of segments that contain an object.\n        :type SegmentSet: list of AiRecognitionTaskObjectSeqmentItem\n        """
        self.Name = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskObjectSeqmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskObjectResultOutput(AbstractModel):
    """Output of intelligent object recognition.

    """

    def __init__(self):
        """
        :param ResultSet: Result set of intelligent object recognition.\n        :type ResultSet: list of AiRecognitionTaskObjectResultItem\n        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskObjectResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskObjectSeqmentItem(AbstractModel):
    """Object recognition result segment.

    """

    def __init__(self):
        """
        :param StartTimeOffset: Start time offset of recognized segment in seconds.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of recognition segment in seconds.\n        :type EndTimeOffset: float\n        :param Confidence: Confidence of recognized segment. Value range: 0-100.\n        :type Confidence: float\n        :param AreaCoordSet: Zone coordinates of recognition result. The array contains four elements: [x1,y1,x2,y2], i.e., the horizontal and vertical coordinates of the top-left and bottom-right corners.\n        :type AreaCoordSet: list of int\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResult(AbstractModel):
    """Full text recognition result.

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input information of full text recognition task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrFullTextResultInput`\n        :param Output: Output information of full text recognition task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrFullTextResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResultInput(AbstractModel):
    """Input of full text recognition.

    """

    def __init__(self):
        """
        :param Definition: Full text recognition template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResultOutput(AbstractModel):
    """Output of full text recognition.

    """

    def __init__(self):
        """
        :param SegmentSet: Full text recognition result set.\n        :type SegmentSet: list of AiRecognitionTaskOcrFullTextSegmentItem\n        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextSegmentItem(AbstractModel):
    """Full text recognition segment.

    """

    def __init__(self):
        """
        :param StartTimeOffset: Start time offset of recognized segment in seconds.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of recognition segment in seconds.\n        :type EndTimeOffset: float\n        :param TextSet: Recognition segment result set.\n        :type TextSet: list of AiRecognitionTaskOcrFullTextSegmentTextItem\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TextSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TextSet") is not None:
            self.TextSet = []
            for item in params.get("TextSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentTextItem()
                obj._deserialize(item)
                self.TextSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextSegmentTextItem(AbstractModel):
    """Full text recognition segment.

    """

    def __init__(self):
        """
        :param Confidence: Confidence of recognized segment. Value range: 0-100.\n        :type Confidence: float\n        :param AreaCoordSet: Zone coordinates of recognition result. The array contains four elements: [x1,y1,x2,y2], i.e., the horizontal and vertical coordinates of the top-left and bottom-right corners.\n        :type AreaCoordSet: list of int\n        :param Text: Recognized text.\n        :type Text: str\n        """
        self.Confidence = None
        self.AreaCoordSet = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResult(AbstractModel):
    """Text keyword recognition result.

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input information of text keyword recognition task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResultInput`\n        :param Output: Output information of text keyword recognition task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultInput(AbstractModel):
    """Input of text keyword recognition.

    """

    def __init__(self):
        """
        :param Definition: Text keyword recognition template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultItem(AbstractModel):
    """Text keyword recognition result.

    """

    def __init__(self):
        """
        :param Word: Text keyword.\n        :type Word: str\n        :param SegmentSet: List of segments that contain a text keyword.\n        :type SegmentSet: list of AiRecognitionTaskOcrWordsSegmentItem\n        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultOutput(AbstractModel):
    """Output of text keyword recognition.

    """

    def __init__(self):
        """
        :param ResultSet: Text keyword recognition result set.\n        :type ResultSet: list of AiRecognitionTaskOcrWordsResultItem\n        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskOcrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsSegmentItem(AbstractModel):
    """Text recognition segment.

    """

    def __init__(self):
        """
        :param StartTimeOffset: Start time offset of recognized segment in seconds.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of recognition segment in seconds.\n        :type EndTimeOffset: float\n        :param Confidence: Confidence of recognized segment. Value range: 0-100.\n        :type Confidence: float\n        :param AreaCoordSet: Zone coordinates of recognition result. The array contains four elements: [x1,y1,x2,y2], i.e., the horizontal and vertical coordinates of the top-left and bottom-right corners.\n        :type AreaCoordSet: list of int\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskSegmentResult(AbstractModel):
    """Video splitting results.

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input information of video splitting task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskSegmentResultInput`\n        :param Output: Output information of video splitting task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskSegmentResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskSegmentResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskSegmentResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskSegmentResultInput(AbstractModel):
    """Input of video splitting.

    """

    def __init__(self):
        """
        :param Definition: Video splitting template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskSegmentResultOutput(AbstractModel):
    """Output of video splitting.

    """

    def __init__(self):
        """
        :param SegmentSet: List of split video segments.\n        :type SegmentSet: list of AiRecognitionTaskSegmentSegmentItem\n        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskSegmentSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskSegmentSegmentItem(AbstractModel):
    """Split video segment.

    """

    def __init__(self):
        """
        :param FileId: File ID, which is valid only when a VOD file is processed and the subsegments generated through segmentation are also VOD files.\n        :type FileId: str\n        :param SegmentUrl: Split video segment URL.\n        :type SegmentUrl: str\n        :param Confidence: Confidence of split segment. Value range: 0-100.\n        :type Confidence: float\n        :param StartTimeOffset: Start time offset of split segment in seconds.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of split segment in seconds.\n        :type EndTimeOffset: float\n        :param CovImgUrl: Split cover image URL.\n        :type CovImgUrl: str\n        :param SpecialInfo: Special field, which should be ignored.\n        :type SpecialInfo: str\n        """
        self.FileId = None
        self.SegmentUrl = None
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.CovImgUrl = None
        self.SpecialInfo = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.SegmentUrl = params.get("SegmentUrl")
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.CovImgUrl = params.get("CovImgUrl")
        self.SpecialInfo = params.get("SpecialInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalAsrTaskInput(AbstractModel):
    """Input parameter type of ASR-based politically sensitive information detection in speech task in content audit

    """

    def __init__(self):
        """
        :param Definition: Politically sensitive information detection template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalAsrTaskOutput(AbstractModel):
    """ASR-detected politically sensitive information in speech

    """

    def __init__(self):
        """
        :param Confidence: Score of ASR-detected politically sensitive information in speech between 0 and 100.\n        :type Confidence: float\n        :param Suggestion: Suggestion for ASR-detected politically sensitive information in speech. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>\n        :type Suggestion: str\n        :param SegmentSet: List of video segments that contain ASR-detected politically sensitive information in speech.\n        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalOcrTaskInput(AbstractModel):
    """Input parameter type of OCR-based politically sensitive information detection in text task in content audit

    """

    def __init__(self):
        """
        :param Definition: Politically sensitive information detection template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalOcrTaskOutput(AbstractModel):
    """OCR-detected politically sensitive information in text

    """

    def __init__(self):
        """
        :param Confidence: Score of OCR-detected politically sensitive information in text between 0 and 100.\n        :type Confidence: float\n        :param Suggestion: Suggestion for OCR-detected politically sensitive information in text. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>\n        :type Suggestion: str\n        :param SegmentSet: List of video segments that contain OCR-detected politically sensitive information in text.\n        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalTaskInput(AbstractModel):
    """Input parameter type of politically sensitive information detection task in content audit

    """

    def __init__(self):
        """
        :param Definition: Politically sensitive information detection template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalTaskOutput(AbstractModel):
    """Politically sensitive information

    """

    def __init__(self):
        """
        :param Confidence: Score of detected politically sensitive information in video between 0 and 100.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Confidence: float\n        :param Suggestion: Suggestion for detected politically sensitive information. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Suggestion: str\n        :param Label: Tags for the results of video politically sensitive information detection. The relationship between the `LabelSet` parameter in the content audit template [controlling tasks of video politically sensitive information detection](https://intl.cloud.tencent.com/document/api/266/31773?from_cn_redirect=1#PoliticalImgReviewTemplateInfo) and this parameter is as follows:
violation_photo:
<li>violation_photo: violating photo.</li>
Other values (politician/entertainment/sport/entrepreneur/scholar/celebrity/military):
<li>politician: political figure.</li>\n        :type Label: str\n        :param SegmentSet: List of video segments that contain the detected politically sensitive information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SegmentSet: list of MediaContentReviewPoliticalSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewPoliticalSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornAsrTaskInput(AbstractModel):
    """Input parameter type of ASR-based porn information detection in speech task in content audit

    """

    def __init__(self):
        """
        :param Definition: Porn information detection template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornAsrTaskOutput(AbstractModel):
    """ASR-detected porn information in speech

    """

    def __init__(self):
        """
        :param Confidence: Score of ASR-detected porn information in speech between 0 and 100.\n        :type Confidence: float\n        :param Suggestion: Suggestion for ASR-detected porn information in speech. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>\n        :type Suggestion: str\n        :param SegmentSet: List of video segments that contain the ASR-detected porn information in speech.\n        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornOcrTaskInput(AbstractModel):
    """Input parameter type of OCR-based porn information detection in text task in content audit

    """

    def __init__(self):
        """
        :param Definition: Porn information detection template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornOcrTaskOutput(AbstractModel):
    """OCR-detected porn information in text

    """

    def __init__(self):
        """
        :param Confidence: Score of OCR-detected porn information in text between 0 and 100.\n        :type Confidence: float\n        :param Suggestion: Suggestion for OCR-detected porn information in text. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>\n        :type Suggestion: str\n        :param SegmentSet: List of video segments that contain the OCR-detected porn information in text.\n        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornTaskInput(AbstractModel):
    """Input parameter type of porn information detection task in content audit

    """

    def __init__(self):
        """
        :param Definition: Porn information detection template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornTaskOutput(AbstractModel):
    """Result information of porn information detection

    """

    def __init__(self):
        """
        :param Confidence: Score of detected porn information in video between 0 and 100.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Confidence: float\n        :param Suggestion: Suggestion for detected porn information. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Suggestion: str\n        :param Label: Tag of detected porn information in video. Valid values:
<li>porn: porn.</li>
<li>sexy: sexiness.</li>
<li>vulgar: vulgarity.</li>
<li>intimacy: intimacy.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Label: str\n        :param SegmentSet: List of video segments that contain the detected porn information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SegmentSet: list of MediaContentReviewSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedAsrTaskInput(AbstractModel):
    """Input parameter type of ASR-based prohibited information detection in speech task in content audit

    """

    def __init__(self):
        """
        :param Definition: Prohibited information detection template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedAsrTaskOutput(AbstractModel):
    """ASR-detected prohibited information in speech

    """

    def __init__(self):
        """
        :param Confidence: Score of ASR-detected prohibited information in speech between 0 and 100.\n        :type Confidence: float\n        :param Suggestion: Suggestion for ASR-detected prohibited information in speech. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>\n        :type Suggestion: str\n        :param SegmentSet: List of video segments that contain the ASR-detected prohibited information in speech.\n        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedOcrTaskInput(AbstractModel):
    """Input parameter type of OCR-based prohibited information detection in text task in content audit

    """

    def __init__(self):
        """
        :param Definition: Prohibited information detection template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedOcrTaskOutput(AbstractModel):
    """OCR-detected prohibited information in text

    """

    def __init__(self):
        """
        :param Confidence: Score of OCR-detected prohibited information in text between 0 and 100.\n        :type Confidence: float\n        :param Suggestion: Suggestion for OCR-detected prohibited information in text. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>\n        :type Suggestion: str\n        :param SegmentSet: List of video segments that contain the OCR-detected prohibited information in text.\n        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalAsrResult(AbstractModel):
    """Result type of ASR-based politically sensitive information detection in speech task in content audit

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of ASR-based politically sensitive information detection in speech task in content audit.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalAsrTaskInput`\n        :param Output: Output of ASR-based politically sensitive information detection in speech task in content audit.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalAsrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalOcrResult(AbstractModel):
    """Result type of OCR-based politically sensitive information detection in text task in content audit

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of OCR-based politically sensitive information detection in text task in content audit.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalOcrTaskInput`\n        :param Output: Output of OCR-based politically sensitive information detection in text task in content audit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalOcrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalResult(AbstractModel):
    """Result type of politically sensitive information detection task in content audit

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of politically sensitive information detection task in content audit.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalTaskInput`\n        :param Output: Output of politically sensitive information detection task in content audit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornAsrResult(AbstractModel):
    """Result type of ASR-based porn information detection in speech task in content audit

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of ASR-based porn information detection in speech task in content audit.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPornAsrTaskInput`\n        :param Output: Output of ASR-based porn information detection in speech task in content audit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPornAsrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornOcrResult(AbstractModel):
    """Result type of OCR-based porn information detection in text task in content audit

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of OCR-based porn information detection in text task in content audit.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPornOcrTaskInput`\n        :param Output: Output of OCR-based porn information detection in text task in content audit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPornOcrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornResult(AbstractModel):
    """Result type of porn information detection task in content audit

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of porn information detection task in content audit.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPornTaskInput`\n        :param Output: Output of porn information detection task in content audit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPornTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskProhibitedAsrResult(AbstractModel):
    """Result type of ASR-based prohibited information detection in speech task in content audit

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input of ASR-based prohibited information detection in speech task in content audit\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewProhibitedAsrTaskInput`\n        :param Output: Output of ASR-based prohibited information detection in speech task in content audit
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewProhibitedAsrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskProhibitedOcrResult(AbstractModel):
    """Result type of OCR-based prohibited information detection in text task in content audit

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input of OCR-based prohibited information detection in text task in content audit\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewProhibitedOcrTaskInput`\n        :param Output: Output of OCR-based prohibited information detection in text task in content audit
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewProhibitedOcrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskTerrorismOcrResult(AbstractModel):
    """Result type of OCR-based terrorism information detection in text task in content audit

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input of OCR-based terrorism information detection in text task in content audit.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewTerrorismOcrTaskInput`\n        :param Output: Output of OCR-based terrorism information detection in text task in content audit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewTerrorismOcrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskTerrorismResult(AbstractModel):
    """Result type of terrorism information detection task in content audit

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of terrorism information detection task in content audit.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewTerrorismTaskInput`\n        :param Output: Output of terrorism information detection task in content audit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewTerrorismTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismOcrTaskInput(AbstractModel):
    """Input parameter type of OCR-based terrorism information detection in text task in content audit

    """

    def __init__(self):
        """
        :param Definition: Terrorism information detection template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismOcrTaskOutput(AbstractModel):
    """OCR-detected terrorism information in text

    """

    def __init__(self):
        """
        :param Confidence: Score of OCR-detected terrorism information in text between 0 and 100.\n        :type Confidence: float\n        :param Suggestion: Suggestion for OCR-detected terrorism information in text. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>\n        :type Suggestion: str\n        :param SegmentSet: List of video segments that contain OCR-detected terrorism information in text.\n        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismTaskInput(AbstractModel):
    """Input parameter type of terrorism information detection task in content audit

    """

    def __init__(self):
        """
        :param Definition: Terrorism information detection template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismTaskOutput(AbstractModel):
    """Terrorism information

    """

    def __init__(self):
        """
        :param Confidence: Score of detected terrorism information in a video between 0 and 100.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Confidence: float\n        :param Suggestion: Suggestion for detected terrorism information. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Suggestion: str\n        :param Label: Tag of the detected terrorism information in a video. Valid values:
<li>`guns`: weapons and guns</li>
<li>`crowd`: crowds</li>
<li>`police`: police forces</li>
<li>`bloody`: bloody images</li>
<li>`banners`: terrorism flags</li>
<li>`militant`: militants</li>
<li>`explosion`: explosions and fires</li>
<li>`terrorists`: terrorists</li>
<li>`scenario`: terrorism images</li>\n        :type Label: str\n        :param SegmentSet: List of video segments that contain the detected terrorism information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SegmentSet: list of MediaContentReviewSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFaceInfo(AbstractModel):
    """AI-based sample management - face information.

    """

    def __init__(self):
        """
        :param FaceId: Face image ID.\n        :type FaceId: str\n        :param Url: Face image address.\n        :type Url: str\n        """
        self.FaceId = None
        self.Url = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFaceOperation(AbstractModel):
    """AI-based sample management - face data operation.

    """

    def __init__(self):
        """
        :param Type: Operation type. Valid values: add, delete, reset. The `reset` operation will clear the existing face data of a figure and add `FaceContents` as the specified face data.\n        :type Type: str\n        :param FaceIds: Face ID set, which is required if `Type` is `delete`.\n        :type FaceIds: list of str\n        :param FaceContents: String set generated by [Base64-encoding](https://tools.ietf.org/html/rfc4648) the face image.
<li>This field is required if `Type` is `add` or `reset`;</li>
<li>Array length limit: 5 images.</li>
Note: the image must be a relatively clear full-face photo of a figure in at least 200 * 200 px.\n        :type FaceContents: list of str\n        """
        self.Type = None
        self.FaceIds = None
        self.FaceContents = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.FaceIds = params.get("FaceIds")
        self.FaceContents = params.get("FaceContents")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFailFaceInfo(AbstractModel):
    """AI-based sample management - face information failed to be processed.

    """

    def __init__(self):
        """
        :param Index: It corresponds to incorrect image subscripts in the `FaceContents` input parameter, starting from 0.\n        :type Index: int\n        :param ErrCode: Error code. Valid values:
<li>0: success;</li>
<li>Other values: failure.</li>\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        """
        self.Index = None
        self.ErrCode = None
        self.Message = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSamplePerson(AbstractModel):
    """AI-based sample management - figure information.

    """

    def __init__(self):
        """
        :param PersonId: Figure ID.\n        :type PersonId: str\n        :param Name: Figure name.\n        :type Name: str\n        :param Description: Figure description.\n        :type Description: str\n        :param FaceInfoSet: Face information.\n        :type FaceInfoSet: list of AiSampleFaceInfo\n        :param TagSet: Figure tag.\n        :type TagSet: list of str\n        :param UsageSet: Use case.\n        :type UsageSet: list of str\n        :param CreateTime: Creation time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.FaceInfoSet = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = AiSampleFaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleTagOperation(AbstractModel):
    """AI-based sample management - tag operation.

    """

    def __init__(self):
        """
        :param Type: Operation type. Valid values: add, delete, reset.\n        :type Type: str\n        :param Tags: Tag. Length limit: 128 characters.\n        :type Tags: list of str\n        """
        self.Type = None
        self.Tags = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleWord(AbstractModel):
    """AI-based sample management - keyword output information.

    """

    def __init__(self):
        """
        :param Keyword: Keyword.\n        :type Keyword: str\n        :param TagSet: Keyword tag.\n        :type TagSet: list of str\n        :param UsageSet: Keyword use case.\n        :type UsageSet: list of str\n        :param CreateTime: Creation time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        """
        self.Keyword = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleWordInfo(AbstractModel):
    """AI-based sample management - keyword input information.

    """

    def __init__(self):
        """
        :param Keyword: Keyword. Length limit: 20 characters.\n        :type Keyword: str\n        :param Tags: Keyword tag
<li>Array length limit: 20 tags;</li>
<li>Tag length limit: 128 characters.</li>\n        :type Tags: list of str\n        """
        self.Keyword = None
        self.Tags = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnimatedGraphicTaskInput(AbstractModel):
    """Animated image generating task type

    """

    def __init__(self):
        """
        :param Definition: Animated image generating template ID\n        :type Definition: int\n        :param StartTimeOffset: Start time offset of an animated image in the video, in seconds.
<li>If this parameter is left empty or set to 0, the animated image will start at the same time as the video.</li>
<li>If this parameter is set to a positive number (n for example), the animated image will start at the nth second of the video.</li>
<li>If this parameter is set to a negative number (-n for example), the animated image will start at the nth second before the end of the video.</li>\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of an animated image in the video, in seconds.
<li>If this parameter is left empty or set to 0, the animated image will end at the same time as the video.</li>
<li>If this parameter is set to a positive number (n for example), the animated image will end at the nth second of the video.</li>
<li>If this parameter is set to a negative number (-n for example), the animated image will end at the nth second before the end of the video.</li>\n        :type EndTimeOffset: float\n        """
        self.Definition = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnimatedGraphicsTemplate(AbstractModel):
    """Details of an animated image generating template.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an animated image generating template.\n        :type Definition: int\n        :param Type: Template type. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param Name: Name of an animated image generating template.\n        :type Name: str\n        :param Comment: Description of an animated image generating template.\n        :type Comment: str\n        :param Width: Maximum value of the width (or long side) of an animated image in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of an animated image in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param Format: Animated image format.\n        :type Format: str\n        :param Fps: Frame rate.\n        :type Fps: int\n        :param Quality: Image quality.\n        :type Quality: float\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyUploadRequest(AbstractModel):
    """ApplyUpload request structure.

    """

    def __init__(self):
        """
        :param MediaType: Media type. For the detailed valid values, please see [Upload Overview](https://intl.cloud.tencent.com/document/product/266/9760?from_cn_redirect=1#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B).\n        :type MediaType: str\n        :param MediaName: Media name.\n        :type MediaName: str\n        :param CoverType: Cover type. For the detailed valid values, please see [Upload Overview](https://intl.cloud.tencent.com/document/product/266/9760?from_cn_redirect=1#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B).\n        :type CoverType: str\n        :param Procedure: Subsequent task operation on a media file, i.e., after a media file is uploaded, task flow operations will be initiated automatically. This parameter value is a task flow template name. VOD supports [creating task flow templates](https://intl.cloud.tencent.com/document/product/266/33819?from_cn_redirect=1) and naming the templates.\n        :type Procedure: str\n        :param ExpireTime: Expiration time of a media file in ISO 8601 format. For more information, please see [Notes on ISO Date Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).\n        :type ExpireTime: str\n        :param StorageRegion: Specifies upload region. This is only applicable to users that have special requirements for the upload region.\n        :type StorageRegion: str\n        :param ClassId: Category ID, which is used to categorize the media for management. A category can be created and its ID can be obtained by using the [category creating](https://intl.cloud.tencent.com/document/product/266/7812?from_cn_redirect=1) API.
<li>Default value: 0, which means "Other".</li>\n        :type ClassId: int\n        :param SourceContext: Source context, which is used to pass through the user request information. The [upload callback](https://intl.cloud.tencent.com/document/product/266/7830?from_cn_redirect=1) API will return the value of this field. It can contain up to 250 characters.\n        :type SourceContext: str\n        :param SessionContext: Session context, which is used to pass through the user request information. If the `Procedure` parameter is specified, the [task flow status change callback](https://intl.cloud.tencent.com/document/product/266/9636?from_cn_redirect=1) API will return the value of this field. It can contain up to 1,000 characters.\n        :type SessionContext: str\n        :param ExtInfo: Reserved parameter for special purposes.\n        :type ExtInfo: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.MediaType = None
        self.MediaName = None
        self.CoverType = None
        self.Procedure = None
        self.ExpireTime = None
        self.StorageRegion = None
        self.ClassId = None
        self.SourceContext = None
        self.SessionContext = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.MediaType = params.get("MediaType")
        self.MediaName = params.get("MediaName")
        self.CoverType = params.get("CoverType")
        self.Procedure = params.get("Procedure")
        self.ExpireTime = params.get("ExpireTime")
        self.StorageRegion = params.get("StorageRegion")
        self.ClassId = params.get("ClassId")
        self.SourceContext = params.get("SourceContext")
        self.SessionContext = params.get("SessionContext")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyUploadResponse(AbstractModel):
    """ApplyUpload response structure.

    """

    def __init__(self):
        """
        :param StorageBucket: Storage bucket, which is used as the `bucket_name` in the URL of the upload API.\n        :type StorageBucket: str\n        :param StorageRegion: Storage region, which is used as the `Region` in the `Host` of the upload API.\n        :type StorageRegion: str\n        :param VodSessionKey: VOD session, which is used to confirm the `VodSessionKey` parameter of the upload API.\n        :type VodSessionKey: str\n        :param MediaStoragePath: Media storage path, which is used as the `Key` of the stored media of the upload API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MediaStoragePath: str\n        :param CoverStoragePath: Cover storage path, which is used as the `Key` of the stored cover of the upload API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CoverStoragePath: str\n        :param TempCertificate: Temporary credential, which is used for authentication of the upload API.\n        :type TempCertificate: :class:`tencentcloud.vod.v20180717.models.TempCertificate`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.StorageBucket = None
        self.StorageRegion = None
        self.VodSessionKey = None
        self.MediaStoragePath = None
        self.CoverStoragePath = None
        self.TempCertificate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StorageBucket = params.get("StorageBucket")
        self.StorageRegion = params.get("StorageRegion")
        self.VodSessionKey = params.get("VodSessionKey")
        self.MediaStoragePath = params.get("MediaStoragePath")
        self.CoverStoragePath = params.get("CoverStoragePath")
        if params.get("TempCertificate") is not None:
            self.TempCertificate = TempCertificate()
            self.TempCertificate._deserialize(params.get("TempCertificate"))
        self.RequestId = params.get("RequestId")


class AsrFullTextConfigureInfo(AbstractModel):
    """Control parameter of full speech recognition task.

    """

    def __init__(self):
        """
        :param Switch: Switch of full speech recognition task. Valid values:
<li>ON: enables intelligent full speech recognition task;</li>
<li>OFF: disables intelligent full speech recognition task.</li>\n        :type Switch: str\n        :param SubtitleFormat: Format of generated subtitles file. If this parameter is left empty or a blank string is entered, no subtitles files will be generated. Valid value:
<li>vtt: generates a WebVTT subtitles file.</li>\n        :type SubtitleFormat: str\n        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrFullTextConfigureInfoForUpdate(AbstractModel):
    """Control parameter of full speech recognition task.

    """

    def __init__(self):
        """
        :param Switch: Switch of full speech recognition task. Valid values:
<li>ON: enables intelligent full speech recognition task;</li>
<li>OFF: disables intelligent full speech recognition task.</li>\n        :type Switch: str\n        :param SubtitleFormat: Format of generated subtitles file. If an empty string is entered, no subtitles files will be generated. Valid values:
<li>vtt: generates a WebVTT subtitles file.</li>\n        :type SubtitleFormat: str\n        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrWordsConfigureInfo(AbstractModel):
    """Speech keyword recognition control parameter.

    """

    def __init__(self):
        """
        :param Switch: Switch of speech keyword recognition task. Valid values:
<li>ON: enables speech keyword recognition task;</li>
<li>OFF: disables speech keyword recognition task.</li>\n        :type Switch: str\n        :param LabelSet: Keyword filter tag, which specifies the keyword tag that needs to be returned. If this parameter is left empty, all results will be returned.
There can be up to 10 tags, each with a length limit of 16 characters.\n        :type LabelSet: list of str\n        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrWordsConfigureInfoForUpdate(AbstractModel):
    """Control parameter of speech keyword recognition.

    """

    def __init__(self):
        """
        :param Switch: Switch of speech keyword recognition task. Valid values:
<li>ON: enables speech keyword recognition task;</li>
<li>OFF: disables speech keyword recognition task.</li>\n        :type Switch: str\n        :param LabelSet: Keyword filter tag, which specifies the keyword tag that needs to be returned. If this parameter is left empty or a blank value is entered, all results will be returned.
There can be up to 10 tags, each with a length limit of 16 characters.\n        :type LabelSet: list of str\n        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachMediaSubtitlesRequest(AbstractModel):
    """AttachMediaSubtitles request structure.

    """

    def __init__(self):
        """
        :param FileId: Unique ID of the media file\n        :type FileId: str\n        :param Operation: Operation. Valid values:
<li>`Attach`: associates subtitles.</li>
<li>`Detach`: disassociates subtitles.</li>\n        :type Operation: str\n        :param AdaptiveDynamicStreamingDefinition: [Adaptive bitrate streaming template ID](https://intl.cloud.tencent.com/document/product/266/34071?from_cn_redirect=1#zsy)\n        :type AdaptiveDynamicStreamingDefinition: int\n        :param SubtitleIds: Unique IDs of the subtitles\n        :type SubtitleIds: list of str\n        :param SubAppId: VOD [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID. If you need to access the resources in a subapplication, set this parameter to the subapplication ID; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.FileId = None
        self.Operation = None
        self.AdaptiveDynamicStreamingDefinition = None
        self.SubtitleIds = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.Operation = params.get("Operation")
        self.AdaptiveDynamicStreamingDefinition = params.get("AdaptiveDynamicStreamingDefinition")
        self.SubtitleIds = params.get("SubtitleIds")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachMediaSubtitlesResponse(AbstractModel):
    """AttachMediaSubtitles response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AudioTemplateInfo(AbstractModel):
    """Audio stream configuration parameter

    """

    def __init__(self):
        """
        :param Codec: Audio stream encoder.
When the outer `Container` parameter is `mp3`, the valid value is:
<li>libmp3lame.</li>
When the outer `Container` parameter is `ogg` or `flac`, the valid value is:
<li>flac.</li>
When the outer `Container` parameter is `m4a`, the valid values include:
<li>libfdk_aac;</li>
<li>libmp3lame;</li>
<li>ac3.</li>
When the outer `Container` parameter is `mp4` or `flv`, the valid values include:
<li>libfdk_aac: more suitable for mp4;</li>
<li>libmp3lame: More suitable for flv;</li>
<li>mp2.</li>
When the outer `Container` parameter is `hls`, the valid values include:
<li>libfdk_aac;</li>
<li>libmp3lame.</li>\n        :type Codec: str\n        :param Bitrate: Audio stream bitrate in Kbps. Value range: 0 and [26, 256].
If the value is 0, the bitrate of the audio stream will be the same as that of the original audio.\n        :type Bitrate: int\n        :param SampleRate: Audio stream sample rate. Valid values:
<li>32,000</li>
<li>44,100</li>
<li>48,000</li>
In Hz.\n        :type SampleRate: int\n        :param AudioChannel: Audio channel system. Valid values:
<li>1: mono-channel</li>
<li>2: dual-channel</li>
<li>6: stereo</li>
You cannot set the sound channel as stereo for media files in container formats for audios (FLAC, OGG, MP3, M4A).
Default value: 2\n        :type AudioChannel: int\n        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTemplateInfoForUpdate(AbstractModel):
    """Audio stream configuration parameter

    """

    def __init__(self):
        """
        :param Codec: Audio stream encoder.
When the outer `Container` parameter is `mp3`, the valid value is:
<li>libmp3lame.</li>
When the outer `Container` parameter is `ogg` or `flac`, the valid value is:
<li>flac.</li>
When the outer `Container` parameter is `m4a`, the valid values include:
<li>libfdk_aac;</li>
<li>libmp3lame;</li>
<li>ac3.</li>
When the outer `Container` parameter is `mp4` or `flv`, the valid values include:
<li>libfdk_aac: more suitable for mp4;</li>
<li>libmp3lame: More suitable for flv;</li>
<li>mp2.</li>
When the outer `Container` parameter is `hls`, the valid values include:
<li>libfdk_aac;</li>
<li>libmp3lame.</li>\n        :type Codec: str\n        :param Bitrate: Audio stream bitrate in Kbps. Value range: 0 and [26, 256]. If the value is 0, the bitrate of the audio stream will be the same as that of the original audio.\n        :type Bitrate: int\n        :param SampleRate: Audio stream sample rate. Valid values:
<li>32,000</li>
<li>44,100</li>
<li>48,000</li>
In Hz.\n        :type SampleRate: int\n        :param AudioChannel: Audio channel system. Valid values:
<li>1: mono-channel</li>
<li>2: dual-channel</li>
<li>6: stereo</li>
You cannot set the sound channel as stereo for media files in container formats for audios (FLAC, OGG, MP3, M4A).\n        :type AudioChannel: int\n        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTrackItem(AbstractModel):
    """Audio segment information of audio track.

    """

    def __init__(self):
        """
        :param SourceMedia: Source of media material for audio segment, which can be:
<li>ID of VOD media files</li>
<li>Download URL of other media files</li>
Note: when a download URL of other media files is used as the material source and access control (such as hotlink protection) is enabled, the URL needs to carry access control parameters (such as hotlink protection signature).\n        :type SourceMedia: str\n        :param SourceMediaStartTime: Start time of audio segment in material file in seconds. Default value: 0, which means to start capturing from the beginning position of the material.\n        :type SourceMediaStartTime: float\n        :param Duration: Audio segment duration in seconds. By default, the length of the material will be used, which means that the entire material will be captured.\n        :type Duration: float\n        :param AudioOperations: Operation on audio segment, such as volume adjustment.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioOperations: list of AudioTransform\n        """
        self.SourceMedia = None
        self.SourceMediaStartTime = None
        self.Duration = None
        self.AudioOperations = None


    def _deserialize(self, params):
        self.SourceMedia = params.get("SourceMedia")
        self.SourceMediaStartTime = params.get("SourceMediaStartTime")
        self.Duration = params.get("Duration")
        if params.get("AudioOperations") is not None:
            self.AudioOperations = []
            for item in params.get("AudioOperations"):
                obj = AudioTransform()
                obj._deserialize(item)
                self.AudioOperations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTransform(AbstractModel):
    """Audio operation

    """

    def __init__(self):
        """
        :param Type: Audio operation type. Valid values:
<li>Volume: volume adjustment.</li>\n        :type Type: str\n        :param VolumeParam: Volume adjustment parameter, which is valid if `Type` is `Volume`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VolumeParam: :class:`tencentcloud.vod.v20180717.models.AudioVolumeParam`\n        """
        self.Type = None
        self.VolumeParam = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("VolumeParam") is not None:
            self.VolumeParam = AudioVolumeParam()
            self.VolumeParam._deserialize(params.get("VolumeParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioVolumeParam(AbstractModel):
    """Audio gain adjustment parameter

    """

    def __init__(self):
        """
        :param Mute: Whether to mute. Valid values: 0, 1.
<li>0: not muted.</li>
<li>1: muted.</li>
Default value: 0.\n        :type Mute: int\n        :param Gain: Audio gain. Value range: 0-10.
<li>If the value is greater than 1, the volume will be increased.</li>
<li>If the value is smaller than 1, the volume will be decreased.</li>
<li>0 and 1: no change.</li>
Default value: 0.\n        :type Gain: float\n        """
        self.Mute = None
        self.Gain = None


    def _deserialize(self, params):
        self.Mute = params.get("Mute")
        self.Gain = params.get("Gain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Canvas(AbstractModel):
    """Canvas information. When a video is composed, if the source material (video or image) cannot fill the output video window, the background will be drawn with the set canvas.

    """

    def __init__(self):
        """
        :param Color: Background color. Valid values:
<li>Black: black background</li>
<li>White: white background</li>
Default value: Black.\n        :type Color: str\n        :param Width: Canvas width, which is the width of the output video. Value range: 0-4096 px.
Default value: 0, which means that the value is the same as the video width of the first video segment in the first video track.\n        :type Width: int\n        :param Height: Canvas height, which is the height (or long side) of the output video. Value range: 0-4096 px.
Default value: 0, which means that the value is the same as the video height of the first video segment in the first video track.\n        :type Height: int\n        """
        self.Color = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Color = params.get("Color")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnLogInfo(AbstractModel):
    """CDN log information

    """

    def __init__(self):
        """
        :param Date: Log date in the format of `yyyy-MM-dd`, such as 2018-03-01.\n        :type Date: str\n        :param Name: Log name in the format of date and time-domain name,
such as 2018120101-test.vod2.mqcloud.com.\n        :type Name: str\n        :param Url: Log download link, which is valid for 24 hours.\n        :type Url: str\n        :param StartTime: Log start time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?lang=en&pg=)\n        :type StartTime: str\n        :param EndTime: Log end time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?lang=en&pg=)\n        :type EndTime: str\n        """
        self.Date = None
        self.Name = None
        self.Url = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Name = params.get("Name")
        self.Url = params.get("Url")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationConfigureInfo(AbstractModel):
    """Control parameter of intelligent categorization task

    """

    def __init__(self):
        """
        :param Switch: Switch of intelligent categorization task. Valid values:
<li>ON: enables intelligent categorization task;</li>
<li>OFF: disables intelligent categorization task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationConfigureInfoForUpdate(AbstractModel):
    """Control parameter of intelligent categorization task

    """

    def __init__(self):
        """
        :param Switch: Switch of intelligent categorization task. Valid values:
<li>ON: enables intelligent categorization task;</li>
<li>OFF: disables intelligent categorization task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClipFileInfo2017(AbstractModel):
    """Information of file generated by video clipping (v2017)

    """

    def __init__(self):
        """
        :param ErrCode: Error code
<li>0: success;</li>
<li>Other values: failure.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ErrCode: int\n        :param Message: Error description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param FileId: Output target file ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: str\n        :param FileUrl: Output target file address.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileUrl: str\n        :param FileType: Output target file type.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileType: str\n        """
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileUrl = None
        self.FileType = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")
        self.FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClipTask2017(AbstractModel):
    """Video clipping task information. This structure is only used for tasks initiated by the [ClipVideo](https://intl.cloud.tencent.com/document/product/266/10156?from_cn_redirect=1) API in v2017.

    """

    def __init__(self):
        """
        :param TaskId: Video clipping task ID.\n        :type TaskId: str\n        :param SrcFileId: ID of source file for video clipping task.\n        :type SrcFileId: str\n        :param FileInfo: Information of file output by video clipping.\n        :type FileInfo: :class:`tencentcloud.vod.v20180717.models.ClipFileInfo2017`\n        """
        self.TaskId = None
        self.SrcFileId = None
        self.FileInfo = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.SrcFileId = params.get("SrcFileId")
        if params.get("FileInfo") is not None:
            self.FileInfo = ClipFileInfo2017()
            self.FileInfo._deserialize(params.get("FileInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitUploadRequest(AbstractModel):
    """CommitUpload request structure.

    """

    def __init__(self):
        """
        :param VodSessionKey: VOD session, which takes the returned value (VodSessionKey) of the `ApplyUpload` API.\n        :type VodSessionKey: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.VodSessionKey = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.VodSessionKey = params.get("VodSessionKey")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitUploadResponse(AbstractModel):
    """CommitUpload response structure.

    """

    def __init__(self):
        """
        :param FileId: Unique ID of media file.\n        :type FileId: str\n        :param MediaUrl: Media playback address.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MediaUrl: str\n        :param CoverUrl: Media cover address.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CoverUrl: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FileId = None
        self.MediaUrl = None
        self.CoverUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.MediaUrl = params.get("MediaUrl")
        self.CoverUrl = params.get("CoverUrl")
        self.RequestId = params.get("RequestId")


class ComposeMediaOutput(AbstractModel):
    """Information of output media file.

    """

    def __init__(self):
        """
        :param FileName: Filename of up to 64 characters.\n        :type FileName: str\n        :param Description: Description, which can contain up to 128 characters.\n        :type Description: str\n        :param ClassId: Category ID, which is used to categorize the media for management. A category can be created and its ID can be obtained by using the [category creating](https://intl.cloud.tencent.com/document/product/266/7812?from_cn_redirect=1) API.
<li>Default value: 0, which means "Other".</li>\n        :type ClassId: int\n        :param ExpireTime: Expiration time of output media file in ISO 8601 format, after which the file will be deleted. Files will never expire by default. For more information, please see [Notes on ISO Date Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type ExpireTime: str\n        :param Container: Container. Valid values: mp4, mp3. mp3 is for audio files.\n        :type Container: str\n        :param VideoStream: Information of output video.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VideoStream: :class:`tencentcloud.vod.v20180717.models.OutputVideoStream`\n        :param AudioStream: Information of output audio.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioStream: :class:`tencentcloud.vod.v20180717.models.OutputAudioStream`\n        :param RemoveVideo: Whether to remove video data. Valid values:
<li>0: retain</li>
<li>1: remove</li>
Default value: 0.\n        :type RemoveVideo: int\n        :param RemoveAudio: Whether to remove audio data. Valid values:
<li>0: retain</li>
<li>1: remove</li>
Default value: 0.\n        :type RemoveAudio: int\n        """
        self.FileName = None
        self.Description = None
        self.ClassId = None
        self.ExpireTime = None
        self.Container = None
        self.VideoStream = None
        self.AudioStream = None
        self.RemoveVideo = None
        self.RemoveAudio = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Description = params.get("Description")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")
        self.Container = params.get("Container")
        if params.get("VideoStream") is not None:
            self.VideoStream = OutputVideoStream()
            self.VideoStream._deserialize(params.get("VideoStream"))
        if params.get("AudioStream") is not None:
            self.AudioStream = OutputAudioStream()
            self.AudioStream._deserialize(params.get("AudioStream"))
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComposeMediaRequest(AbstractModel):
    """ComposeMedia request structure.

    """

    def __init__(self):
        """
        :param Tracks: List of input media tracks, i.e., information of multiple tracks composed of video, audio, image, and other materials. <li>Multiple input tracks are aligned with the output media file on the time axis. </li><li>The materials of each track at the same time point on the time axis will be superimposed. Specifically, videos or images will be superimposed for video image by track order, where a material with a higher track order will be more on top, while audio materials will be mixed. </li><li>Up to 10 tracks are supported for each type (video, audio, or image).</li>\n        :type Tracks: list of MediaTrack\n        :param Output: Information of output media file.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.ComposeMediaOutput`\n        :param Canvas: Canvas used for composing video file.\n        :type Canvas: :class:`tencentcloud.vod.v20180717.models.Canvas`\n        :param SessionContext: Used to pass through user request information. `ComposeMediaComplete` callback will return the value of this parameter. It contains up to 1,000 characters.\n        :type SessionContext: str\n        :param SessionId: Used to identify duplicate requests. After you send a request, if any request with the same `SessionId` has already been sent in the last three days (72 hours), an error message will be returned. `SessionId` contains up to 50 characters. If this parameter is not carried or is an empty string, no deduplication will be performed.\n        :type SessionId: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Tracks = None
        self.Output = None
        self.Canvas = None
        self.SessionContext = None
        self.SessionId = None
        self.SubAppId = None


    def _deserialize(self, params):
        if params.get("Tracks") is not None:
            self.Tracks = []
            for item in params.get("Tracks"):
                obj = MediaTrack()
                obj._deserialize(item)
                self.Tracks.append(obj)
        if params.get("Output") is not None:
            self.Output = ComposeMediaOutput()
            self.Output._deserialize(params.get("Output"))
        if params.get("Canvas") is not None:
            self.Canvas = Canvas()
            self.Canvas._deserialize(params.get("Canvas"))
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComposeMediaResponse(AbstractModel):
    """ComposeMedia response structure.

    """

    def __init__(self):
        """
        :param TaskId: Media file composing task ID, which can be used to query the status of composing task (with task type being `MakeMedia`).\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ComposeMediaTask(AbstractModel):
    """Media file composing task information

    """

    def __init__(self):
        """
        :param TaskId: Task ID.\n        :type TaskId: str\n        :param Status: Task flow status. Valid values:
<li>PROCESSING: processing;</li>
<li>FINISH: completed.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: str\n        :param ErrCode: Error code
<li>0: success;</li>
<li>Other values: failure.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of media file composing task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.ComposeMediaTaskInput`\n        :param Output: Output of media file composing task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.ComposeMediaTaskOutput`\n        :param MetaData: Metadata of a source video.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`\n        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this parameter. It can contain up to 1000 characters.\n        :type SessionContext: str\n        :param SessionId: ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is not carried or is left empty, no deduplication will be performed.\n        :type SessionId: str\n        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None
        self.MetaData = None
        self.SessionContext = None
        self.SessionId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = ComposeMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = ComposeMediaTaskOutput()
            self.Output._deserialize(params.get("Output"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComposeMediaTaskInput(AbstractModel):
    """Input of media file composing task.

    """

    def __init__(self):
        """
        :param Tracks: List of input media tracks, i.e., information of multiple tracks composed of video, audio, image, and other materials.\n        :type Tracks: list of MediaTrack\n        :param Canvas: Canvas used for composing video file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Canvas: :class:`tencentcloud.vod.v20180717.models.Canvas`\n        :param Output: Information of output media file.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.ComposeMediaOutput`\n        """
        self.Tracks = None
        self.Canvas = None
        self.Output = None


    def _deserialize(self, params):
        if params.get("Tracks") is not None:
            self.Tracks = []
            for item in params.get("Tracks"):
                obj = MediaTrack()
                obj._deserialize(item)
                self.Tracks.append(obj)
        if params.get("Canvas") is not None:
            self.Canvas = Canvas()
            self.Canvas._deserialize(params.get("Canvas"))
        if params.get("Output") is not None:
            self.Output = ComposeMediaOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComposeMediaTaskOutput(AbstractModel):
    """Output of media file composing task.

    """

    def __init__(self):
        """
        :param FileType: File type, such as mp4 and mp3.\n        :type FileType: str\n        :param FileId: Media file ID.\n        :type FileId: str\n        :param FileUrl: Media file playback address.\n        :type FileUrl: str\n        :param MediaName: Filename of up to 64 characters.\n        :type MediaName: str\n        :param ClassId: Category ID, which is used to categorize the media for management. A category can be created and its ID can be obtained by using the [category creating](https://intl.cloud.tencent.com/document/product/266/7812?from_cn_redirect=1) API.
<li>Default value: 0, which means "Other".</li>\n        :type ClassId: int\n        :param ExpireTime: Expiration time of output media file in ISO 8601 format, after which the file will be deleted. Files will never expire by default. For more information, please see [Notes on ISO Date Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type ExpireTime: str\n        """
        self.FileType = None
        self.FileId = None
        self.FileUrl = None
        self.MediaName = None
        self.ClassId = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.FileType = params.get("FileType")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")
        self.MediaName = params.get("MediaName")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConcatFileInfo2017(AbstractModel):
    """Information of source file for video splicing (v2017)

    """

    def __init__(self):
        """
        :param ErrCode: Error code
<li>0: success;</li>
<li>Other values: failure.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param FileId: ID of source file for video splicing.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: str\n        :param FileUrl: Address of source file for video splicing.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileUrl: str\n        :param FileType: Format of source file for video splicing.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileType: str\n        """
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileUrl = None
        self.FileType = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")
        self.FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConcatTask2017(AbstractModel):
    """Video splicing task information. This structure is only used for tasks initiated by the [ConcatVideo](https://intl.cloud.tencent.com/document/product/266/7821?from_cn_redirect=1) API in v2017.

    """

    def __init__(self):
        """
        :param TaskId: Video splicing task ID.\n        :type TaskId: str\n        :param FileInfoSet: Information of source file for video splicing.\n        :type FileInfoSet: list of ConcatFileInfo2017\n        """
        self.TaskId = None
        self.FileInfoSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = ConcatFileInfo2017()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfirmEventsRequest(AbstractModel):
    """ConfirmEvents request structure.

    """

    def __init__(self):
        """
        :param EventHandles: Event handler, i.e., the `EventSet. EventHandle` field in the output parameters of the [event notification pulling](https://intl.cloud.tencent.com/document/product/266/33433?from_cn_redirect=1) API.
Array length limit: 16.\n        :type EventHandles: list of str\n        :param ExtInfo: Reserved field for special purposes.\n        :type ExtInfo: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.EventHandles = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.EventHandles = params.get("EventHandles")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfirmEventsResponse(AbstractModel):
    """ConfirmEvents response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ContentReviewTemplateItem(AbstractModel):
    """Content audit template details

    """

    def __init__(self):
        """
        :param Definition: Unique ID of content audit template.\n        :type Definition: int\n        :param Name: Content audit template name. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Content audit template description. Length limit: 256 characters.\n        :type Comment: str\n        :param PornConfigure: Porn information detection control parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PornConfigure: :class:`tencentcloud.vod.v20180717.models.PornConfigureInfo`\n        :param TerrorismConfigure: Terrorism information detection control parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TerrorismConfigure: :class:`tencentcloud.vod.v20180717.models.TerrorismConfigureInfo`\n        :param PoliticalConfigure: Politically sensitive information detection control parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PoliticalConfigure: :class:`tencentcloud.vod.v20180717.models.PoliticalConfigureInfo`\n        :param ProhibitedConfigure: Control parameter of prohibited information detection. Prohibited information includes:
<li>Abusive;</li>
<li>Drug-related.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProhibitedConfigure: :class:`tencentcloud.vod.v20180717.models.ProhibitedConfigureInfo`\n        :param UserDefineConfigure: Custom content audit control parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UserDefineConfigure: :class:`tencentcloud.vod.v20180717.models.UserDefineConfigureInfo`\n        :param ReviewWallSwitch: Switch controlling whether to add audit result to review list (for human review).
<li>ON: yes;</li>
<li>OFF: no.</li>\n        :type ReviewWallSwitch: str\n        :param ScreenshotInterval: Frame capturing interval in seconds. If this parameter is left empty, 1 second will be used by default. Minimum value: 0.5 seconds.\n        :type ScreenshotInterval: float\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None
        self.ReviewWallSwitch = None
        self.ScreenshotInterval = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.ReviewWallSwitch = params.get("ReviewWallSwitch")
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverBySnapshotTaskInput(AbstractModel):
    """Input parameter type of cover generating task

    """

    def __init__(self):
        """
        :param Definition: Time point screencapturing template ID.\n        :type Definition: int\n        :param PositionType: Screencapturing mode. Valid values:
<li>Time: screencaptures by time point</li>
<li>Percent: screencaptures by percentage</li>\n        :type PositionType: str\n        :param PositionValue: Screenshot position:
<li>For time point screencapturing, this means to take a screenshot at a specified time point (in seconds) and use it as the cover</li>
<li>For percentage screencapturing, this value means to take a screenshot at a specified percentage of the video duration and use it as the cover</li>\n        :type PositionValue: float\n        :param WatermarkSet: List of up to 10 image or text watermarks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WatermarkSet: list of WatermarkInput\n        """
        self.Definition = None
        self.PositionType = None
        self.PositionValue = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.PositionType = params.get("PositionType")
        self.PositionValue = params.get("PositionValue")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverBySnapshotTaskOutput(AbstractModel):
    """Output type of cover generating task

    """

    def __init__(self):
        """
        :param CoverUrl: Cover URL.\n        :type CoverUrl: str\n        """
        self.CoverUrl = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverConfigureInfo(AbstractModel):
    """Control parameter of intelligent cover generating task

    """

    def __init__(self):
        """
        :param Switch: Switch of intelligent cover generating task. Valid values:
<li>ON: enables intelligent cover generating task;</li>
<li>OFF: disables intelligent cover generating task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverConfigureInfoForUpdate(AbstractModel):
    """Control parameter of intelligent cover generating task

    """

    def __init__(self):
        """
        :param Switch: Switch of intelligent cover generating task. Valid values:
<li>ON: enables intelligent cover generating task;</li>
<li>OFF: disables intelligent cover generating task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAnalysisTemplateRequest(AbstractModel):
    """CreateAIAnalysisTemplate request structure.

    """

    def __init__(self):
        """
        :param Name: Video content analysis template name. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Video content analysis template description. Length limit: 256 characters.\n        :type Comment: str\n        :param ClassificationConfigure: Control parameter of intelligent categorization task.\n        :type ClassificationConfigure: :class:`tencentcloud.vod.v20180717.models.ClassificationConfigureInfo`\n        :param TagConfigure: Control parameter of intelligent tagging task.\n        :type TagConfigure: :class:`tencentcloud.vod.v20180717.models.TagConfigureInfo`\n        :param CoverConfigure: Control parameter of intelligent cover generating task.\n        :type CoverConfigure: :class:`tencentcloud.vod.v20180717.models.CoverConfigureInfo`\n        :param FrameTagConfigure: Control parameter of intelligent frame-specific tagging task.\n        :type FrameTagConfigure: :class:`tencentcloud.vod.v20180717.models.FrameTagConfigureInfo`\n        :param HighlightConfigure: Control parameter of an intelligent highlight generating task.\n        :type HighlightConfigure: :class:`tencentcloud.vod.v20180717.models.HighlightsConfigureInfo`\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.HighlightConfigure = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        if params.get("HighlightConfigure") is not None:
            self.HighlightConfigure = HighlightsConfigureInfo()
            self.HighlightConfigure._deserialize(params.get("HighlightConfigure"))
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAnalysisTemplateResponse(AbstractModel):
    """CreateAIAnalysisTemplate response structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of video content analysis template.\n        :type Definition: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAIRecognitionTemplateRequest(AbstractModel):
    """CreateAIRecognitionTemplate request structure.

    """

    def __init__(self):
        """
        :param Name: Video content recognition template name. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Description of video content recognition template. Length limit: 256 characters.\n        :type Comment: str\n        :param HeadTailConfigure: Control parameter of video opening and ending credits recognition.\n        :type HeadTailConfigure: :class:`tencentcloud.vod.v20180717.models.HeadTailConfigureInfo`\n        :param SegmentConfigure: Control parameter of video splitting recognition.\n        :type SegmentConfigure: :class:`tencentcloud.vod.v20180717.models.SegmentConfigureInfo`\n        :param FaceConfigure: Control parameter of face recognition.\n        :type FaceConfigure: :class:`tencentcloud.vod.v20180717.models.FaceConfigureInfo`\n        :param OcrFullTextConfigure: Control parameter of full text recognition.\n        :type OcrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.OcrFullTextConfigureInfo`\n        :param OcrWordsConfigure: Control parameter of text keyword recognition.\n        :type OcrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.OcrWordsConfigureInfo`\n        :param AsrFullTextConfigure: Control parameter of full speech recognition.\n        :type AsrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.AsrFullTextConfigureInfo`\n        :param AsrWordsConfigure: Control parameter of speech keyword recognition.\n        :type AsrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.AsrWordsConfigureInfo`\n        :param ObjectConfigure: Control parameter of object recognition.\n        :type ObjectConfigure: :class:`tencentcloud.vod.v20180717.models.ObjectConfigureInfo`\n        :param ScreenshotInterval: Frame capturing interval in seconds. If this parameter is left empty, 1 second will be used by default. Minimum value: 0.5 seconds.\n        :type ScreenshotInterval: float\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Name = None
        self.Comment = None
        self.HeadTailConfigure = None
        self.SegmentConfigure = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.ObjectConfigure = None
        self.ScreenshotInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("HeadTailConfigure") is not None:
            self.HeadTailConfigure = HeadTailConfigureInfo()
            self.HeadTailConfigure._deserialize(params.get("HeadTailConfigure"))
        if params.get("SegmentConfigure") is not None:
            self.SegmentConfigure = SegmentConfigureInfo()
            self.SegmentConfigure._deserialize(params.get("SegmentConfigure"))
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        if params.get("ObjectConfigure") is not None:
            self.ObjectConfigure = ObjectConfigureInfo()
            self.ObjectConfigure._deserialize(params.get("ObjectConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIRecognitionTemplateResponse(AbstractModel):
    """CreateAIRecognitionTemplate response structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of video content recognition template.\n        :type Definition: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """CreateAdaptiveDynamicStreamingTemplate request structure.

    """

    def __init__(self):
        """
        :param Format: Adaptive bitstream format. Valid values:
<li>HLS.</li>\n        :type Format: str\n        :param StreamInfos: Parameter information of output substream for adaptive bitrate streaming. Up to 10 substreams can be output.
Note: the frame rate of all substreams must be the same; otherwise, the frame rate of the first substream will be used as the output frame rate.\n        :type StreamInfos: list of AdaptiveStreamTemplate\n        :param Name: Template name. Length limit: 64 characters.\n        :type Name: str\n        :param DrmType: DRM scheme type. Valid values:
<li>SimpleAES.</li>
If this field is an empty string, DRM will not be performed on the video.\n        :type DrmType: str\n        :param DisableHigherVideoBitrate: Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values:
<li>0: no,</li>
<li>1: yes.</li>
Default value: no.\n        :type DisableHigherVideoBitrate: int\n        :param DisableHigherVideoResolution: Whether to prohibit transcoding from low resolution to high resolution. Valid values:
<li>0: no,</li>
<li>1: yes.</li>
Default value: no.\n        :type DisableHigherVideoResolution: int\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Format = None
        self.StreamInfos = None
        self.Name = None
        self.DrmType = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Name = params.get("Name")
        self.DrmType = params.get("DrmType")
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """CreateAdaptiveDynamicStreamingTemplate response structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of adaptive bitrate streaming template.\n        :type Definition: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAnimatedGraphicsTemplateRequest(AbstractModel):
    """CreateAnimatedGraphicsTemplate request structure.

    """

    def __init__(self):
        """
        :param Fps: Video frame rate in Hz. Value range: [1, 30].\n        :type Fps: int\n        :param Width: Maximum value of the width (or long side) of an animated image in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of an animated image in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param Format: Animated image format. Valid values: gif; webp. Default value: gif.\n        :type Format: str\n        :param Quality: Image quality. Value range: [1, 100]. Default value: 75.\n        :type Quality: float\n        :param Name: Name of an animated image generating template. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Fps = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Quality = None
        self.Name = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Quality = params.get("Quality")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAnimatedGraphicsTemplateResponse(AbstractModel):
    """CreateAnimatedGraphicsTemplate response structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an animated image generating template.\n        :type Definition: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateClassRequest(AbstractModel):
    """CreateClass request structure.

    """

    def __init__(self):
        """
        :param ParentId: Parent category ID. For a first-level category, enter `-1`.\n        :type ParentId: int\n        :param ClassName: Category name. Length limit: 1-64 characters.\n        :type ClassName: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.ParentId = None
        self.ClassName = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ParentId = params.get("ParentId")
        self.ClassName = params.get("ClassName")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClassResponse(AbstractModel):
    """CreateClass response structure.

    """

    def __init__(self):
        """
        :param ClassId: Category ID\n        :type ClassId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ClassId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.RequestId = params.get("RequestId")


class CreateContentReviewTemplateRequest(AbstractModel):
    """CreateContentReviewTemplate request structure.

    """

    def __init__(self):
        """
        :param ReviewWallSwitch: Whether to allow the recognition result to enter the intelligent recognition platform (for human recognition).
<li>ON: yes</li>
<li>OFF: no</li>\n        :type ReviewWallSwitch: str\n        :param Name: Name of an intelligent content recognition template. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Description of an intelligent content recognition template. Length limit: 256 characters.\n        :type Comment: str\n        :param PornConfigure: Control parameter for porn information.\n        :type PornConfigure: :class:`tencentcloud.vod.v20180717.models.PornConfigureInfo`\n        :param TerrorismConfigure: Control parameter for terrorism information.\n        :type TerrorismConfigure: :class:`tencentcloud.vod.v20180717.models.TerrorismConfigureInfo`\n        :param PoliticalConfigure: Control parameter for politically sensitive information.\n        :type PoliticalConfigure: :class:`tencentcloud.vod.v20180717.models.PoliticalConfigureInfo`\n        :param ProhibitedConfigure: Control parameter of prohibited information detection. Prohibited information includes:
<li>Abusive;</li>
<li>Drug-related.</li>\n        :type ProhibitedConfigure: :class:`tencentcloud.vod.v20180717.models.ProhibitedConfigureInfo`\n        :param UserDefineConfigure: Control parameter for custom intelligent content recognition.\n        :type UserDefineConfigure: :class:`tencentcloud.vod.v20180717.models.UserDefineConfigureInfo`\n        :param ScreenshotInterval: Frame capturing interval in seconds. If this parameter is left empty, 1 second will be used by default. Minimum value: 0.5 seconds.\n        :type ScreenshotInterval: float\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.ReviewWallSwitch = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None
        self.ScreenshotInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ReviewWallSwitch = params.get("ReviewWallSwitch")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContentReviewTemplateResponse(AbstractModel):
    """CreateContentReviewTemplate response structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an intelligent recognition template.\n        :type Definition: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateImageSpriteTask2017(AbstractModel):
    """Image sprite generating task. This structure is only used for tasks initiated by the [CreateImageSprite](https://intl.cloud.tencent.com/document/product/266/8101?from_cn_redirect=1) API in v2017.

    """

    def __init__(self):
        """
        :param TaskId: Image sprite generating task ID.\n        :type TaskId: str\n        :param ErrCode: Error code
<li>0: success;</li>
<li>Other values: failure.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param FileId: ID of generated image sprite file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: str\n        :param Definition: Image sprite specification. For more information, please see [Image Sprite Generating Template](https://intl.cloud.tencent.com/document/product/266/33480?from_cn_redirect=1#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Definition: int\n        :param TotalCount: Total number of subimages in image sprite.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param ImageSpriteUrlSet: Address of output image sprite.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageSpriteUrlSet: list of str\n        :param WebVttUrl: Address of WebVtt file for the position-time relationship among subimages in an image sprite.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WebVttUrl: str\n        """
        self.TaskId = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.Definition = None
        self.TotalCount = None
        self.ImageSpriteUrlSet = None
        self.WebVttUrl = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.Definition = params.get("Definition")
        self.TotalCount = params.get("TotalCount")
        self.ImageSpriteUrlSet = params.get("ImageSpriteUrlSet")
        self.WebVttUrl = params.get("WebVttUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageSpriteTemplateRequest(AbstractModel):
    """CreateImageSpriteTemplate request structure.

    """

    def __init__(self):
        """
        :param SampleType: Sampling type. Valid values:
<li>Percent: by percent.</li>
<li>Time: by time interval.</li>\n        :type SampleType: str\n        :param SampleInterval: Sampling interval.
<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>
<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>\n        :type SampleInterval: int\n        :param RowCount: Subimage row count of an image sprite.\n        :type RowCount: int\n        :param ColumnCount: Subimage column count of an image sprite.\n        :type ColumnCount: int\n        :param Name: Name of an image sprite generating template. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
Default value: black.\n        :type FillType: str\n        :param Width: Maximum value of the width (or long side) of a subimage in an image sprite in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of a subimage in an image sprite in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.Name = None
        self.Comment = None
        self.FillType = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageSpriteTemplateResponse(AbstractModel):
    """CreateImageSpriteTemplate response structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an image sprite generating template.\n        :type Definition: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreatePersonSampleRequest(AbstractModel):
    """CreatePersonSample request structure.

    """

    def __init__(self):
        """
        :param Name: Name of a sample. Length limit: 20 characters.\n        :type Name: str\n        :param Usages: Usage of a sample. Valid values:
1. Recognition: used for content recognition; equivalent to `Recognition.Face`
2. Review: used for inappropriate information recognition; equivalent to `Review.Face`
3. All: equivalent to 1+2.\n        :type Usages: list of str\n        :param Description: Description of a sample. Length limit: 1024 characters.\n        :type Description: str\n        :param FaceContents: String generated after the sample image is encoded by [Base64](https://tools.ietf.org/html/rfc4648). Only JPEG and PNG images are supported. Array length limit: 5 images.
Note: the image must be a relatively clear full-face photo of a person and has a resolution of no less than 200 x 200.\n        :type FaceContents: list of str\n        :param Tags: Tags of a sample
<li>Array length limit: 20 tags</li>
<li>Length limit of a tag: 128 characters</li>\n        :type Tags: list of str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Name = None
        self.Usages = None
        self.Description = None
        self.FaceContents = None
        self.Tags = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Usages = params.get("Usages")
        self.Description = params.get("Description")
        self.FaceContents = params.get("FaceContents")
        self.Tags = params.get("Tags")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonSampleResponse(AbstractModel):
    """CreatePersonSample response structure.

    """

    def __init__(self):
        """
        :param Person: Information of a sample.\n        :type Person: :class:`tencentcloud.vod.v20180717.models.AiSamplePerson`\n        :param FailFaceInfoSet: Information of samples that failed the verification by facial feature positioning.\n        :type FailFaceInfoSet: list of AiSampleFailFaceInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateProcedureTemplateRequest(AbstractModel):
    """CreateProcedureTemplate request structure.

    """

    def __init__(self):
        """
        :param Name: Task flow name (up to 20 characters).\n        :type Name: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param MediaProcessTask: Parameter of video processing task.\n        :type MediaProcessTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskInput`\n        :param AiContentReviewTask: Parameter of AI-based content audit task.\n        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`\n        :param AiAnalysisTask: Parameter of AI-based content analysis task.\n        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`\n        :param AiRecognitionTask: Type parameter of AI-based content recognition task.\n        :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Name = None
        self.Comment = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProcedureTemplateResponse(AbstractModel):
    """CreateProcedureTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSampleSnapshotTemplateRequest(AbstractModel):
    """CreateSampleSnapshotTemplate request structure.

    """

    def __init__(self):
        """
        :param SampleType: Sampled screencapturing type. Valid values:
<li>Percent: by percent.</li>
<li>Time: by time interval.</li>\n        :type SampleType: str\n        :param SampleInterval: Sampling interval.
<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>
<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>\n        :type SampleInterval: int\n        :param Name: Name of a sampled screencapturing template. Length limit: 64 characters.\n        :type Name: str\n        :param Width: Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param Format: Image format. Valid values: jpg, png. Default value: jpg.\n        :type Format: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.\n        :type FillType: str\n        """
        self.SampleType = None
        self.SampleInterval = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.SubAppId = None
        self.FillType = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSampleSnapshotTemplateResponse(AbstractModel):
    """CreateSampleSnapshotTemplate response structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of a sampled screencapturing template.\n        :type Definition: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate request structure.

    """

    def __init__(self):
        """
        :param Name: Name of a time point screencapturing template. Length limit: 64 characters.\n        :type Name: str\n        :param Width: Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param Format: Image format. Valid values: jpg, png. Default value: jpg.\n        :type Format: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.\n        :type FillType: str\n        """
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.SubAppId = None
        self.FillType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate response structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of a time point screencapturing template.\n        :type Definition: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateSubAppIdRequest(AbstractModel):
    """CreateSubAppId request structure.

    """

    def __init__(self):
        """
        :param Name: Subapplication name. Length limit: 40 characters.\n        :type Name: str\n        :param Description: Subapplication overview. Length limit: 300 characters.\n        :type Description: str\n        """
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubAppIdResponse(AbstractModel):
    """CreateSubAppId response structure.

    """

    def __init__(self):
        """
        :param SubAppId: ID of created subapplication.\n        :type SubAppId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SubAppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.RequestId = params.get("RequestId")


class CreateSuperPlayerConfigRequest(AbstractModel):
    """CreateSuperPlayerConfig request structure.

    """

    def __init__(self):
        """
        :param Name: Player configuration name, which can contain up to 64 letters, digits, underscores, and hyphens (such as test_ABC-123) and must be unique under a user.\n        :type Name: str\n        :param DrmSwitch: Switch of DRM-protected adaptive bitstream playback:
<li>ON: enabled, indicating to play back only output adaptive bitstreams protected by DRM;</li>
<li>OFF: disabled, indicating to play back unencrypted output adaptive bitstreams.</li>
Default value: OFF.\n        :type DrmSwitch: str\n        :param AdaptiveDynamicStreamingDefinition: ID of the unencrypted adaptive bitrate streaming template that allows output, which is required if `DrmSwitch` is `OFF`.\n        :type AdaptiveDynamicStreamingDefinition: int\n        :param DrmStreamingsInfo: Content of the DRM-protected adaptive bitrate streaming template that allows output, which is required if `DrmSwitch` is `ON`.\n        :type DrmStreamingsInfo: :class:`tencentcloud.vod.v20180717.models.DrmStreamingsInfo`\n        :param ImageSpriteDefinition: ID of the image sprite generating template that allows output.\n        :type ImageSpriteDefinition: int\n        :param ResolutionNames: Display name of player for substreams with different resolutions. If this parameter is left empty or an empty array, the default configuration will be used:
<li>MinEdgeLength: 240, Name: LD;</li>
<li>MinEdgeLength: 480, Name: SD;</li>
<li>MinEdgeLength: 720, Name: HD;</li>
<li>MinEdgeLength: 1080, Name: FHD;</li>
<li>MinEdgeLength: 1440, Name: 2K;</li>
<li>MinEdgeLength: 2160, Name: 4K;</li>
<li>MinEdgeLength: 4320, Name: 8K.</li>\n        :type ResolutionNames: list of ResolutionNameInfo\n        :param Domain: Domain name used for playback. If it is left empty or set to `Default`, the domain name configured in [Default Distribution Configuration](https://intl.cloud.tencent.com/document/product/266/33373?from_cn_redirect=1) will be used.\n        :type Domain: str\n        :param Scheme: Scheme used for playback. If it is left empty or set to `Default`, the scheme configured in [Default Distribution Configuration](https://intl.cloud.tencent.com/document/product/266/33373?from_cn_redirect=1) will be used. Other valid values:
<li>HTTP;</li>
<li>HTTPS.</li>\n        :type Scheme: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Name = None
        self.DrmSwitch = None
        self.AdaptiveDynamicStreamingDefinition = None
        self.DrmStreamingsInfo = None
        self.ImageSpriteDefinition = None
        self.ResolutionNames = None
        self.Domain = None
        self.Scheme = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DrmSwitch = params.get("DrmSwitch")
        self.AdaptiveDynamicStreamingDefinition = params.get("AdaptiveDynamicStreamingDefinition")
        if params.get("DrmStreamingsInfo") is not None:
            self.DrmStreamingsInfo = DrmStreamingsInfo()
            self.DrmStreamingsInfo._deserialize(params.get("DrmStreamingsInfo"))
        self.ImageSpriteDefinition = params.get("ImageSpriteDefinition")
        if params.get("ResolutionNames") is not None:
            self.ResolutionNames = []
            for item in params.get("ResolutionNames"):
                obj = ResolutionNameInfo()
                obj._deserialize(item)
                self.ResolutionNames.append(obj)
        self.Domain = params.get("Domain")
        self.Scheme = params.get("Scheme")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSuperPlayerConfigResponse(AbstractModel):
    """CreateSuperPlayerConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTranscodeTemplateRequest(AbstractModel):
    """CreateTranscodeTemplate request structure.

    """

    def __init__(self):
        """
        :param Container: Container. Valid values: mp4; flv; hls; mp3; flac; ogg; m4a. Among them, mp3, flac, ogg, and m4a are for audio files.\n        :type Container: str\n        :param Name: Transcoding template name. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param RemoveVideo: Whether to remove video data. Valid values:
<li>0: retain</li>
<li>1: remove</li>
Default value: 0.\n        :type RemoveVideo: int\n        :param RemoveAudio: Whether to remove audio data. Valid values:
<li>0: retain</li>
<li>1: remove</li>
Default value: 0.\n        :type RemoveAudio: int\n        :param VideoTemplate: Video stream configuration parameter. This field is required when `RemoveVideo` is 0.\n        :type VideoTemplate: :class:`tencentcloud.vod.v20180717.models.VideoTemplateInfo`\n        :param AudioTemplate: Audio stream configuration parameter. This field is required when `RemoveAudio` is 0.\n        :type AudioTemplate: :class:`tencentcloud.vod.v20180717.models.AudioTemplateInfo`\n        :param TEHDConfig: TESHD transcoding parameter.\n        :type TEHDConfig: :class:`tencentcloud.vod.v20180717.models.TEHDConfig`\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTranscodeTemplateResponse(AbstractModel):
    """CreateTranscodeTemplate response structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of transcoding template.\n        :type Definition: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateWatermarkTemplateRequest(AbstractModel):
    """CreateWatermarkTemplate request structure.

    """

    def __init__(self):
        """
        :param Type: Watermarking type. Valid values:
<li>image: image watermark;</li>
<li>text: text watermark;</li>
<li>svg: SVG watermark.</li>\n        :type Type: str\n        :param Name: Watermarking template name. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param CoordinateOrigin: Origin position. Valid values:
<li>TopLeft: the origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text;</li>
<li>TopRight: the origin of coordinates is in the top-right corner of the video, and the origin of the watermark is in the top-right corner of the image or text;</li>
<li>BottomLeft: the origin of coordinates is in the bottom-left corner of the video, and the origin of the watermark is in the bottom-left corner of the image or text;</li>
<li>BottomRight: the origin of coordinates is in the bottom-right corner of the video, and the origin of the watermark is in the bottom-right corner of the image or text.</li>
Default value: TopLeft.\n        :type CoordinateOrigin: str\n        :param XPos: The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `XPos` of the watermark will be the specified percentage of the video width; for example, `10%` means that `XPos` is 10% of the video width;</li>
<li>If the string ends in px, the `XPos` of the watermark will be the specified px; for example, `100px` means that `XPos` is 100 px.</li>
Default value: 0 px.\n        :type XPos: str\n        :param YPos: The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `YPos` of the watermark will be the specified percentage of the video height; for example, `10%` means that `YPos` is 10% of the video height;</li>
<li>If the string ends in px, the `YPos` of the watermark will be the specified px; for example, `100px` means that `YPos` is 100 px.</li>
Default value: 0 px.\n        :type YPos: str\n        :param ImageTemplate: Image watermarking template. This field is required when `Type` is `image` and is invalid when `Type` is `text`.\n        :type ImageTemplate: :class:`tencentcloud.vod.v20180717.models.ImageWatermarkInput`\n        :param TextTemplate: Text watermarking template. This field is required when `Type` is `text` and is invalid when `Type` is `image`.\n        :type TextTemplate: :class:`tencentcloud.vod.v20180717.models.TextWatermarkTemplateInput`\n        :param SvgTemplate: SVG watermarking template. This field is required when `Type` is `svg` and is invalid when `Type` is `image` or `text`.\n        :type SvgTemplate: :class:`tencentcloud.vod.v20180717.models.SvgWatermarkInput`\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Type = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWatermarkTemplateResponse(AbstractModel):
    """CreateWatermarkTemplate response structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of watermarking template.\n        :type Definition: int\n        :param ImageUrl: Watermark image address. This field is valid only when `Type` is `image`.\n        :type ImageUrl: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Definition = None
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class CreateWordSamplesRequest(AbstractModel):
    """CreateWordSamples request structure.

    """

    def __init__(self):
        """
        :param Usages: <b>Keyword usage. Valid values:</b>
1. Recognition.Ocr: OCR-based content recognition
2. Recognition.Asr: ASR-based content recognition
3. Review.Ocr: OCR-based inappropriate information recognition
4. Review.Asr: ASR-based inappropriate information recognition
<b>Valid values can also be:</b>
5. Recognition: ASR- and OCR-based content recognition; equivalent to 1+2
6. Review: ASR- and OCR-based inappropriate information recognition; equivalent to 3+4
7. All: ASR- and OCR-based content recognition and inappropriate information recognition; equivalent to 1+2+3+4\n        :type Usages: list of str\n        :param Words: Keyword. Array length limit: 100.\n        :type Words: list of AiSampleWordInfo\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Usages = None
        self.Words = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = AiSampleWordInfo()
                obj._deserialize(item)
                self.Words.append(obj)
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWordSamplesResponse(AbstractModel):
    """CreateWordSamples response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAIAnalysisTemplateRequest(AbstractModel):
    """DeleteAIAnalysisTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of video content analysis template.\n        :type Definition: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIAnalysisTemplateResponse(AbstractModel):
    """DeleteAIAnalysisTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAIRecognitionTemplateRequest(AbstractModel):
    """DeleteAIRecognitionTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of video content recognition template.\n        :type Definition: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIRecognitionTemplateResponse(AbstractModel):
    """DeleteAIRecognitionTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """DeleteAdaptiveDynamicStreamingTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of adaptive bitrate streaming template.\n        :type Definition: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """DeleteAdaptiveDynamicStreamingTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAnimatedGraphicsTemplateRequest(AbstractModel):
    """DeleteAnimatedGraphicsTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an animated image generating template.\n        :type Definition: int\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAnimatedGraphicsTemplateResponse(AbstractModel):
    """DeleteAnimatedGraphicsTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClassRequest(AbstractModel):
    """DeleteClass request structure.

    """

    def __init__(self):
        """
        :param ClassId: Category ID\n        :type ClassId: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.ClassId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClassResponse(AbstractModel):
    """DeleteClass response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteContentReviewTemplateRequest(AbstractModel):
    """DeleteContentReviewTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an intelligent content recognition template.\n        :type Definition: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteContentReviewTemplateResponse(AbstractModel):
    """DeleteContentReviewTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageSpriteTemplateRequest(AbstractModel):
    """DeleteImageSpriteTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an image sprite generating template.\n        :type Definition: int\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageSpriteTemplateResponse(AbstractModel):
    """DeleteImageSpriteTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMediaRequest(AbstractModel):
    """DeleteMedia request structure.

    """

    def __init__(self):
        """
        :param FileId: Unique media file ID.\n        :type FileId: str\n        :param DeleteParts: Content to be deleted. The default value is "[]", which indicates to delete the media file and all its corresponding files generated by video processing.\n        :type DeleteParts: list of MediaDeleteItem\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.FileId = None
        self.DeleteParts = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("DeleteParts") is not None:
            self.DeleteParts = []
            for item in params.get("DeleteParts"):
                obj = MediaDeleteItem()
                obj._deserialize(item)
                self.DeleteParts.append(obj)
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMediaResponse(AbstractModel):
    """DeleteMedia response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonSampleRequest(AbstractModel):
    """DeletePersonSample request structure.

    """

    def __init__(self):
        """
        :param PersonId: ID of a sample.\n        :type PersonId: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.PersonId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonSampleResponse(AbstractModel):
    """DeletePersonSample response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProcedureTemplateRequest(AbstractModel):
    """DeleteProcedureTemplate request structure.

    """

    def __init__(self):
        """
        :param Name: Task flow name.\n        :type Name: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Name = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProcedureTemplateResponse(AbstractModel):
    """DeleteProcedureTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSampleSnapshotTemplateRequest(AbstractModel):
    """DeleteSampleSnapshotTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of a sampled screencapturing template.\n        :type Definition: int\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSampleSnapshotTemplateResponse(AbstractModel):
    """DeleteSampleSnapshotTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of a specified time point screencapturing template.\n        :type Definition: int\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSuperPlayerConfigRequest(AbstractModel):
    """DeleteSuperPlayerConfig request structure.

    """

    def __init__(self):
        """
        :param Name: Player configuration name.\n        :type Name: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Name = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSuperPlayerConfigResponse(AbstractModel):
    """DeleteSuperPlayerConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTranscodeTemplateRequest(AbstractModel):
    """DeleteTranscodeTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of transcoding template.\n        :type Definition: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTranscodeTemplateResponse(AbstractModel):
    """DeleteTranscodeTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWatermarkTemplateRequest(AbstractModel):
    """DeleteWatermarkTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of watermarking template.\n        :type Definition: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWatermarkTemplateResponse(AbstractModel):
    """DeleteWatermarkTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWordSamplesRequest(AbstractModel):
    """DeleteWordSamples request structure.

    """

    def __init__(self):
        """
        :param Keywords: Keyword. Array length limit: 100 words.\n        :type Keywords: list of str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Keywords = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWordSamplesResponse(AbstractModel):
    """DeleteWordSamples response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAIAnalysisTemplatesRequest(AbstractModel):
    """DescribeAIAnalysisTemplates request structure.

    """

    def __init__(self):
        """
        :param Definitions: Unique ID filter of video content analysis templates. Array length limit: 100.\n        :type Definitions: list of int\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIAnalysisTemplatesResponse(AbstractModel):
    """DescribeAIAnalysisTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param AIAnalysisTemplateSet: List of video content analysis template details.\n        :type AIAnalysisTemplateSet: list of AIAnalysisTemplateItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AIAnalysisTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIAnalysisTemplateSet") is not None:
            self.AIAnalysisTemplateSet = []
            for item in params.get("AIAnalysisTemplateSet"):
                obj = AIAnalysisTemplateItem()
                obj._deserialize(item)
                self.AIAnalysisTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAIRecognitionTemplatesRequest(AbstractModel):
    """DescribeAIRecognitionTemplates request structure.

    """

    def __init__(self):
        """
        :param Definitions: Unique ID filter of video content recognition templates. Array length limit: 100.\n        :type Definitions: list of int\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIRecognitionTemplatesResponse(AbstractModel):
    """DescribeAIRecognitionTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param AIRecognitionTemplateSet: List of video content recognition template details.\n        :type AIRecognitionTemplateSet: list of AIRecognitionTemplateItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AIRecognitionTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIRecognitionTemplateSet") is not None:
            self.AIRecognitionTemplateSet = []
            for item in params.get("AIRecognitionTemplateSet"):
                obj = AIRecognitionTemplateItem()
                obj._deserialize(item)
                self.AIRecognitionTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAdaptiveDynamicStreamingTemplatesRequest(AbstractModel):
    """DescribeAdaptiveDynamicStreamingTemplates request structure.

    """

    def __init__(self):
        """
        :param Definitions: Unique ID filter of transcoding to adaptive bitrate streaming templates. Array length limit: 100.\n        :type Definitions: list of int non-negative\n        :param Offset: Paged offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Type: Template type filter. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAdaptiveDynamicStreamingTemplatesResponse(AbstractModel):
    """DescribeAdaptiveDynamicStreamingTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param AdaptiveDynamicStreamingTemplateSet: List of transcoding to adaptive bitrate streaming template details.\n        :type AdaptiveDynamicStreamingTemplateSet: list of AdaptiveDynamicStreamingTemplate\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AdaptiveDynamicStreamingTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AdaptiveDynamicStreamingTemplateSet") is not None:
            self.AdaptiveDynamicStreamingTemplateSet = []
            for item in params.get("AdaptiveDynamicStreamingTemplateSet"):
                obj = AdaptiveDynamicStreamingTemplate()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAllClassRequest(AbstractModel):
    """DescribeAllClass request structure.

    """

    def __init__(self):
        """
        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.SubAppId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllClassResponse(AbstractModel):
    """DescribeAllClass response structure.

    """

    def __init__(self):
        """
        :param ClassInfoSet: Category information set
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClassInfoSet: list of MediaClassInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ClassInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClassInfoSet") is not None:
            self.ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = MediaClassInfo()
                obj._deserialize(item)
                self.ClassInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAnimatedGraphicsTemplatesRequest(AbstractModel):
    """DescribeAnimatedGraphicsTemplates request structure.

    """

    def __init__(self):
        """
        :param Definitions: Unique ID filter of animated image generating templates. Array length limit: 100.\n        :type Definitions: list of int non-negative\n        :param Offset: Paged offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Type: Template type filter. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAnimatedGraphicsTemplatesResponse(AbstractModel):
    """DescribeAnimatedGraphicsTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param AnimatedGraphicsTemplateSet: List of animated image generating template details.\n        :type AnimatedGraphicsTemplateSet: list of AnimatedGraphicsTemplate\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AnimatedGraphicsTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AnimatedGraphicsTemplateSet") is not None:
            self.AnimatedGraphicsTemplateSet = []
            for item in params.get("AnimatedGraphicsTemplateSet"):
                obj = AnimatedGraphicsTemplate()
                obj._deserialize(item)
                self.AnimatedGraphicsTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCDNStatDetailsRequest(AbstractModel):
    """DescribeCDNStatDetails request structure.

    """

    def __init__(self):
        """
        :param Metric: Metrics to query. Valid values:
<li>`Traffic`: traffic in bytes</li>
<li>`Bandwidth`: bandwidth in bps</li>
<li>`Requests`: the number of requests</li>\n        :type Metric: str\n        :param StartTime: Start time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?lang=en&pg=).\n        :type StartTime: str\n        :param EndTime: End time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?lang=en&pg=).\n        :type EndTime: str\n        :param DomainNames: List of domain names. The usage data of up to 20 domain names can be queried at a time. The usage data of all domain names is returned by default.\n        :type DomainNames: list of str\n        :param Area: Service region. Valid values:
<li>Chinese Mainland</li>
<li>Asia Pacific Region 1: Hong Kong (China), Macao (China), Singapore, Vietnam, and Thailand</li>
<li>Asia Pacific Region 2: Taiwan (China), Japan, Malaysia, Indonesia, and South Korea</li>
<li>Asia Pacific Region 3: Philippines, India, Australia, and other Asia Pacific countries and regions</li>
<li>Middle East</li>
<li>Europe</li>
<li>North America</li>
<li>South America</li>
<li>Africa</li>
Default value: Chinese Mainland\n        :type Area: str\n        :param Districts: District where users are located. When `Area` is `Chinese Mainland`, valid values for `Districts` are as follows. Otherwise, `Districts` can be ignored.
<li>Beijing</li>
<li>Inner Mongolia</li>
<li>Shanxi</li>
<li>Hebei</li>
<li>Tianjin</li>
<li>Ningxia</li>
<li>Shaanxi</li>
<li>Gansu</li>
<li>Qinghai</li>
<li>Xinjiang</li>
<li>Heilongjiang</li>
<li>Jilin</li>
<li>Liaoning</li>
<li>Fujian</li>
<li>Jiangsu</li>
<li>Anhui</li>
<li>Shandong</li>
<li>Shanghai</li>
<li>Zhejiang</li>
<li>Henan</li>
<li>Hubei</li>
<li>Jiangxi</li>
<li>Hunan</li>
<li>Guizhou</li>
<li>Yunnan</li>
<li>Chongqing</li>
<li>Sichuan</li>
<li>Tibet</li>
<li>Guangdong</li>
<li>Guangxi</li>
<li>Hainan</li>
<li>Hong Kong, Macao and Taiwan</li>
<li>Outside Chinese Mainland</li>
<li>Other</li>\n        :type Districts: list of str\n        :param Isps: ISP of users. When `Area` is `Chinese Mainland`, valid values for `Isps` are as follows. Otherwise, `Isps` can be ignored.
<li>China Telecom</li>
<li>China Unicom</li>
<li>CERNET</li>
<li>Great Wall Broadband Network</li>
<li>China Mobile</li>
<li>China Mobile Tietong</li>
<li>ISPs outside Chinese Mainland</li>
<li>Other ISPs</li>\n        :type Isps: list of str\n        :param DataInterval: Time granularity of every piece of data in minutes. Valid values:
<li>5: 5-minute granularity. The data at 5-minute granularity in the query period will be returned.</li>
<li>1440: 1-day granularity. The data at 1-day granularity in the query period will be returned. If the query period is larger than 24 hours, only data at 1-day granularity can be queried.</li>
If the difference between `StartTime` and `EndTime` is larger than 24 hours, the default value of `DataInterval` is 1440.\n        :type DataInterval: int\n        :param SubAppId: VOD [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Metric = None
        self.StartTime = None
        self.EndTime = None
        self.DomainNames = None
        self.Area = None
        self.Districts = None
        self.Isps = None
        self.DataInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DomainNames = params.get("DomainNames")
        self.Area = params.get("Area")
        self.Districts = params.get("Districts")
        self.Isps = params.get("Isps")
        self.DataInterval = params.get("DataInterval")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCDNStatDetailsResponse(AbstractModel):
    """DescribeCDNStatDetails response structure.

    """

    def __init__(self):
        """
        :param DataInterval: Time granularity of every piece of data in minutes.\n        :type DataInterval: int\n        :param Data: CDN usage statistics.\n        :type Data: list of StatDataItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DataInterval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataInterval = params.get("DataInterval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StatDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCDNUsageDataRequest(AbstractModel):
    """DescribeCDNUsageData request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start date in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type StartTime: str\n        :param EndTime: End date in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I). The end date must be after the start date.\n        :type EndTime: str\n        :param DataType: CDN statistics type. Valid values:
<li>Flux: traffic in bytes.</li>
<li>Bandwidth: bandwidth in bps.</li>\n        :type DataType: str\n        :param DataInterval: Time granularity of usage data in minutes. Valid values:
<li>5: 5-minute granularity. The data at 5-minute granularity in the query period will be returned.</li>
<li>60: 1-hour granularity. The data at 1-hour granularity in the query period will be returned.</li>
<li>1440: 1-day granularity. The data at 1-day granularity in the query period will be returned.</li>
Default value: 1440. Data at 1-day granularity will be returned.\n        :type DataInterval: int\n        :param DomainNames: List of domain names. The usage data of up to 20 domain names can be queried at a time. You can specify multiple domain names and query their combined usage data. The usage data of all domain names will be returned by default.\n        :type DomainNames: list of str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
When the value of this field is 1, the total usage of all subapplications (including primary application) are queried by an admin. In this case, only 1-day granularity is supported.\n        :type SubAppId: int\n        """
        self.StartTime = None
        self.EndTime = None
        self.DataType = None
        self.DataInterval = None
        self.DomainNames = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DataType = params.get("DataType")
        self.DataInterval = params.get("DataInterval")
        self.DomainNames = params.get("DomainNames")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCDNUsageDataResponse(AbstractModel):
    """DescribeCDNUsageData response structure.

    """

    def __init__(self):
        """
        :param DataInterval: Time granularity in minutes.\n        :type DataInterval: int\n        :param Data: CDN statistics.\n        :type Data: list of StatDataItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DataInterval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataInterval = params.get("DataInterval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StatDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCdnLogsRequest(AbstractModel):
    """DescribeCdnLogs request structure.

    """

    def __init__(self):
        """
        :param DomainName: Domain name.\n        :type DomainName: str\n        :param StartTime: Start time for log acquisition in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).\n        :type StartTime: str\n        :param EndTime: End time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F), which must be after the start time.\n        :type EndTime: str\n        :param Limit: Maximum return results of pulling paginated queries. Default value: 100; maximum value: 1000\n        :type Limit: int\n        :param Offset: Page number offset from the beginning of paginated queries. Default value: 0\n        :type Offset: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.DomainName = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnLogsResponse(AbstractModel):
    """DescribeCdnLogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of log download links
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type TotalCount: int\n        :param OverseaCdnLogs: Log download list for CDN nodes outside Mainland China. If global acceleration is not enabled for the domain name, ignore this parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OverseaCdnLogs: list of CdnLogInfo\n        :param DomesticCdnLogs: Log download list for CDN nodes in Mainland China.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DomesticCdnLogs: list of CdnLogInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.OverseaCdnLogs = None
        self.DomesticCdnLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OverseaCdnLogs") is not None:
            self.OverseaCdnLogs = []
            for item in params.get("OverseaCdnLogs"):
                obj = CdnLogInfo()
                obj._deserialize(item)
                self.OverseaCdnLogs.append(obj)
        if params.get("DomesticCdnLogs") is not None:
            self.DomesticCdnLogs = []
            for item in params.get("DomesticCdnLogs"):
                obj = CdnLogInfo()
                obj._deserialize(item)
                self.DomesticCdnLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeContentReviewTemplatesRequest(AbstractModel):
    """DescribeContentReviewTemplates request structure.

    """

    def __init__(self):
        """
        :param Definitions: Unique IDs for filters of an intelligent content recognition template. Array length limit: 100.\n        :type Definitions: list of int\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContentReviewTemplatesResponse(AbstractModel):
    """DescribeContentReviewTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param ContentReviewTemplateSet: List of intelligent content recognition template details.\n        :type ContentReviewTemplateSet: list of ContentReviewTemplateItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ContentReviewTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ContentReviewTemplateSet") is not None:
            self.ContentReviewTemplateSet = []
            for item in params.get("ContentReviewTemplateSet"):
                obj = ContentReviewTemplateItem()
                obj._deserialize(item)
                self.ContentReviewTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDailyPlayStatFileListRequest(AbstractModel):
    """DescribeDailyPlayStatFileList request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start date in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?lang=en&pg=).\n        :type StartTime: str\n        :param EndTime: End date in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?lang=en&pg=).\n        :type EndTime: str\n        :param SubAppId: VOD [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.StartTime = None
        self.EndTime = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDailyPlayStatFileListResponse(AbstractModel):
    """DescribeDailyPlayStatFileList response structure.

    """

    def __init__(self):
        """
        :param PlayStatFileSet: List of playback statistics files.\n        :type PlayStatFileSet: list of PlayStatFileInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PlayStatFileSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayStatFileSet") is not None:
            self.PlayStatFileSet = []
            for item in params.get("PlayStatFileSet"):
                obj = PlayStatFileInfo()
                obj._deserialize(item)
                self.PlayStatFileSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageSpriteTemplatesRequest(AbstractModel):
    """DescribeImageSpriteTemplates request structure.

    """

    def __init__(self):
        """
        :param Definitions: Unique ID filter of image sprite generating templates. Array length limit: 100.\n        :type Definitions: list of int non-negative\n        :param Offset: Paged offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Type: Template type filter. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSpriteTemplatesResponse(AbstractModel):
    """DescribeImageSpriteTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param ImageSpriteTemplateSet: List of image sprite generating template details.\n        :type ImageSpriteTemplateSet: list of ImageSpriteTemplate\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ImageSpriteTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSpriteTemplateSet") is not None:
            self.ImageSpriteTemplateSet = []
            for item in params.get("ImageSpriteTemplateSet"):
                obj = ImageSpriteTemplate()
                obj._deserialize(item)
                self.ImageSpriteTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaInfosRequest(AbstractModel):
    """DescribeMediaInfos request structure.

    """

    def __init__(self):
        """
        :param FileIds: List of media file IDs. N starts from 0 and can be up to 19.\n        :type FileIds: list of str\n        :param Filters: Specifies information entry that needs to be returned by all media files. Multiple entries can be specified simultaneously. N starts from 0. If this field is left empty, all information entries will be returned by default. Valid values:
<li>basicInfo (basic video information).</li>
<li>metaData (video metadata).</li>
<li>transcodeInfo (result information of video transcoding).</li>
<li>animatedGraphicsInfo (result information of animated image generating task).</li>
<li>imageSpriteInfo (image sprite information).</li>
<li>snapshotByTimeOffsetInfo (time point screenshot information).</li>
<li>sampleSnapshotInfo (sampled screenshot information).</li>
<li>keyFrameDescInfo (timestamp information).</li>
<li>adaptiveDynamicStreamingInfo (information of adaptive bitrate streaming).</li>
<li>miniProgramReviewInfo (WeChat Mini Program audit information).</li>\n        :type Filters: list of str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.FileIds = None
        self.Filters = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.Filters = params.get("Filters")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaInfosResponse(AbstractModel):
    """DescribeMediaInfos response structure.

    """

    def __init__(self):
        """
        :param MediaInfoSet: Media file information list.\n        :type MediaInfoSet: list of MediaInfo\n        :param NotExistFileIdSet: List of IDs of files that do not exist.\n        :type NotExistFileIdSet: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MediaInfoSet = None
        self.NotExistFileIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MediaInfoSet") is not None:
            self.MediaInfoSet = []
            for item in params.get("MediaInfoSet"):
                obj = MediaInfo()
                obj._deserialize(item)
                self.MediaInfoSet.append(obj)
        self.NotExistFileIdSet = params.get("NotExistFileIdSet")
        self.RequestId = params.get("RequestId")


class DescribeMediaProcessUsageDataRequest(AbstractModel):
    """DescribeMediaProcessUsageData request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start date in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).\n        :type StartTime: str\n        :param EndTime: End date in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). The end date must be on or after the start date.\n        :type EndTime: str\n        :param Type: This API is used to query video processing task types. Valid values:
<li>Transcoding: basic transcoding</li>
<li>Transcoding-TESHD: TESHD transcoding</li>
<li>Editing: video editing</li>
<li>AdaptiveBitrateStreaming: adaptive bitrate streaming</li>
<li>ContentAudit: content moderation</li>
<li>Transcode: transcoding types, including basic transcoding, TESHD transcoding and video editing. This value is not recommended.</li>\n        :type Type: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.StartTime = None
        self.EndTime = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaProcessUsageDataResponse(AbstractModel):
    """DescribeMediaProcessUsageData response structure.

    """

    def __init__(self):
        """
        :param MediaProcessDataSet: Overview of video processing statistics, which displays the overview and details of queried tasks.\n        :type MediaProcessDataSet: list of TaskStatData\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MediaProcessDataSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MediaProcessDataSet") is not None:
            self.MediaProcessDataSet = []
            for item in params.get("MediaProcessDataSet"):
                obj = TaskStatData()
                obj._deserialize(item)
                self.MediaProcessDataSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonSamplesRequest(AbstractModel):
    """DescribePersonSamples request structure.

    """

    def __init__(self):
        """
        :param Type: Type of samples to pull. Valid values:
<li>UserDefine: custom sample library</li>
<li>Default: default sample library</li>

Default value: UserDefine. Samples in the custom sample library will be pulled.
Note: samples from the default library can only be pulled by providing the name or both the ID and name of a sample. Only one face image will be returned.\n        :type Type: str\n        :param PersonIds: IDs of samples. Array length limit: 100.\n        :type PersonIds: list of str\n        :param Names: Names of samples. Array length limit: 20.\n        :type Names: list of str\n        :param Tags: Tags of a sample. Array length limit: 20.\n        :type Tags: list of str\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of entries to be returned. Default value: 100. Maximum value: 100.\n        :type Limit: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Type = None
        self.PersonIds = None
        self.Names = None
        self.Tags = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PersonIds = params.get("PersonIds")
        self.Names = params.get("Names")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonSamplesResponse(AbstractModel):
    """DescribePersonSamples response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param PersonSet: Figure information.\n        :type PersonSet: list of AiSamplePerson\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.PersonSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonSet") is not None:
            self.PersonSet = []
            for item in params.get("PersonSet"):
                obj = AiSamplePerson()
                obj._deserialize(item)
                self.PersonSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProcedureTemplatesRequest(AbstractModel):
    """DescribeProcedureTemplates request structure.

    """

    def __init__(self):
        """
        :param Names: Name filter of task flow template. Array length limit: 100.\n        :type Names: list of str\n        :param Type: Filter of task flow template types. Valid values:
<li>Preset: preset task flow template;</li>
<li>Custom: custom task flow template.</li>\n        :type Type: str\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Names = None
        self.Type = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProcedureTemplatesResponse(AbstractModel):
    """DescribeProcedureTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param ProcedureTemplateSet: List of task flow template details.\n        :type ProcedureTemplateSet: list of ProcedureTemplate\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ProcedureTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProcedureTemplateSet") is not None:
            self.ProcedureTemplateSet = []
            for item in params.get("ProcedureTemplateSet"):
                obj = ProcedureTemplate()
                obj._deserialize(item)
                self.ProcedureTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReviewDetailsRequest(AbstractModel):
    """DescribeReviewDetails request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start date in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type StartTime: str\n        :param EndTime: End date in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I). The end date must be after the start date.\n        :type EndTime: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.StartTime = None
        self.EndTime = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReviewDetailsResponse(AbstractModel):
    """DescribeReviewDetails response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Times of initiating intelligent content recognition tasks.\n        :type TotalCount: int\n        :param TotalDuration: Duration of intelligent recognition content.\n        :type TotalDuration: int\n        :param Data: Data of intelligent recognition content duration. One piece of data is collected every day.\n        :type Data: list of StatDataItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TotalDuration = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.TotalDuration = params.get("TotalDuration")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StatDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSampleSnapshotTemplatesRequest(AbstractModel):
    """DescribeSampleSnapshotTemplates request structure.

    """

    def __init__(self):
        """
        :param Definitions: Unique ID filter of sampled screencapturing templates. Array length limit: 100.\n        :type Definitions: list of int non-negative\n        :param Offset: Paged offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Type: Template type filter. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleSnapshotTemplatesResponse(AbstractModel):
    """DescribeSampleSnapshotTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param SampleSnapshotTemplateSet: List of sampled screencapturing template details.\n        :type SampleSnapshotTemplateSet: list of SampleSnapshotTemplate\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SampleSnapshotTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SampleSnapshotTemplateSet") is not None:
            self.SampleSnapshotTemplateSet = []
            for item in params.get("SampleSnapshotTemplateSet"):
                obj = SampleSnapshotTemplate()
                obj._deserialize(item)
                self.SampleSnapshotTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotByTimeOffsetTemplatesRequest(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates request structure.

    """

    def __init__(self):
        """
        :param Definitions: Unique ID filter of time point screencapturing templates. Array length limit: 100.\n        :type Definitions: list of int non-negative\n        :param Offset: Paged offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Type: Template type filter. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotByTimeOffsetTemplatesResponse(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param SnapshotByTimeOffsetTemplateSet: List of time point screencapturing template details.\n        :type SnapshotByTimeOffsetTemplateSet: list of SnapshotByTimeOffsetTemplate\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SnapshotByTimeOffsetTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotByTimeOffsetTemplateSet") is not None:
            self.SnapshotByTimeOffsetTemplateSet = []
            for item in params.get("SnapshotByTimeOffsetTemplateSet"):
                obj = SnapshotByTimeOffsetTemplate()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStorageDataRequest(AbstractModel):
    """DescribeStorageData request structure.

    """

    def __init__(self):
        """
        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.SubAppId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStorageDataResponse(AbstractModel):
    """DescribeStorageData response structure.

    """

    def __init__(self):
        """
        :param MediaCount: Total number of current media files.\n        :type MediaCount: int\n        :param TotalStorage: Total current storage capacity in bytes.\n        :type TotalStorage: int\n        :param InfrequentStorage: Current Standard_IA storage capacity in bytes.\n        :type InfrequentStorage: int\n        :param StandardStorage: Current Standard storage capacity in bytes.\n        :type StandardStorage: int\n        :param StorageStat: Storage usage by billing region.\n        :type StorageStat: list of StorageStatData\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MediaCount = None
        self.TotalStorage = None
        self.InfrequentStorage = None
        self.StandardStorage = None
        self.StorageStat = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MediaCount = params.get("MediaCount")
        self.TotalStorage = params.get("TotalStorage")
        self.InfrequentStorage = params.get("InfrequentStorage")
        self.StandardStorage = params.get("StandardStorage")
        if params.get("StorageStat") is not None:
            self.StorageStat = []
            for item in params.get("StorageStat"):
                obj = StorageStatData()
                obj._deserialize(item)
                self.StorageStat.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStorageDetailsRequest(AbstractModel):
    """DescribeStorageDetails request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time in ISO 8601 format. For more information, please see [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?lang=en&pg=).\n        :type StartTime: str\n        :param EndTime: End time in ISO 8601 format, which should be larger than the start time. For more information, please see [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?lang=en&pg=).\n        :type EndTime: str\n        :param Interval: Time granularity. Valid values:
<li>Minute: 5-minute granularity</li>
<li>Day: 1-day granularity</li>
The value is set according to query period length by default. 5-minute granularity is set for periods no longer than 1 day, and 1-day granularity is set for periods longer than 1 day.\n        :type Interval: str\n        :param StorageType: Storage class to query. Valid values:
<li>`TotalStorage`: total storage usage in classes of STANDARD, STANDARD_IA, ARCHIVE, and DEEP ARCHIVE, excluding the storage usage for data deleted in advance.</li>
<li>`StandardStorage`: STANDARD</li>
<li>`InfrequentStorage`: STANDARD_IA</li>
<li>`ArchiveStorage`: ARCHIVE</li>
<li>`DeepArchiveStorage`: DEEP ARCHIVE</li>
<li>`DeletedArchiveStorage`: ARCHIVE data deleted in advance</li>
<li>`DeletedDeepArchiveStorage`: DEEP ARCHIVE data deleted in advance</li>
<li>`ArchiveStandardRetrieval`: ARCHIVE data retrieved using standard retrievals</li>
<li>`ArchiveExpeditedRetrieval`: ARCHIVE data retrieved using expedited retrievals</li>
<li>`ArchiveBulkRetrieval`: ARCHIVE data retrieved using bulk retrievals</li>
<li>`DeepArchiveStandardRetrieval`: DEEP ARCHIVE data retrieved using standard retrievals</li>
<li>`DeepArchiveBulkRetrieval`: DEEP ARCHIVE data retrieved using bulk retrievals</li>
Default value: `TotalStorage`\n        :type StorageType: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
When the value of this field is 1, the total usage of all subapplications (including primary application) are queried by an admin.\n        :type SubAppId: int\n        :param Area: Storage region to query. Valid values:
<li>Chinese Mainland</li>
<li>Outside Chinese Mainland</li>
Default value: Chinese Mainland\n        :type Area: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.StorageType = None
        self.SubAppId = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Interval = params.get("Interval")
        self.StorageType = params.get("StorageType")
        self.SubAppId = params.get("SubAppId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStorageDetailsResponse(AbstractModel):
    """DescribeStorageDetails response structure.

    """

    def __init__(self):
        """
        :param Data: Storage statistics with one piece of data for every 5 minutes or 1 day.\n        :type Data: list of StatDataItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StatDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubAppIdsRequest(AbstractModel):
    """DescribeSubAppIds request structure.

    """

    def __init__(self):
        """
        :param Name: Subapplication name.\n        :type Name: str\n        :param Tags: Tag information. You can query the list of subapplications with specified tags.\n        :type Tags: list of ResourceTag\n        :param Offset: Page number offset from the beginning of paginated queries. Default value: 0.\n        :type Offset: int\n        :param Limit: Maximum return results of pulling paginated queries. Default: 200; maximum: 200.\n        :type Limit: int\n        """
        self.Name = None
        self.Tags = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubAppIdsResponse(AbstractModel):
    """DescribeSubAppIds response structure.

    """

    def __init__(self):
        """
        :param SubAppIdInfoSet: Subapplication information set.\n        :type SubAppIdInfoSet: list of SubAppIdInfo\n        :param TotalCount: Total number of subapplications.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SubAppIdInfoSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubAppIdInfoSet") is not None:
            self.SubAppIdInfoSet = []
            for item in params.get("SubAppIdInfoSet"):
                obj = SubAppIdInfo()
                obj._deserialize(item)
                self.SubAppIdInfoSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSuperPlayerConfigsRequest(AbstractModel):
    """DescribeSuperPlayerConfigs request structure.

    """

    def __init__(self):
        """
        :param Names: Player configuration name filter. Array length limit: 100.\n        :type Names: list of str\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of entries to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Type: Player configuration type filter. Valid values:
<li>Preset: preset configuration;</li>
<li>Custom: custom configuration.</li>\n        :type Type: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Names = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSuperPlayerConfigsResponse(AbstractModel):
    """DescribeSuperPlayerConfigs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param PlayerConfigSet: Player configuration array.\n        :type PlayerConfigSet: list of PlayerConfig\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.PlayerConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PlayerConfigSet") is not None:
            self.PlayerConfigSet = []
            for item in params.get("PlayerConfigSet"):
                obj = PlayerConfig()
                obj._deserialize(item)
                self.PlayerConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail request structure.

    """

    def __init__(self):
        """
        :param TaskId: Video processing task ID.\n        :type TaskId: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.TaskId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail response structure.

    """

    def __init__(self):
        """
        :param TaskType: Task type. Valid values:
<li>Procedure: video processing task</li>
<li>EditMedia: video editing task</li>
<li>SplitMedia: video splitting task</li>
<li>ComposeMedia: media file producing task</li>
<li>WechatPublish: WeChat publishing task</li>
<li>WechatMiniProgramPublish: video publishing on WeChat Mini Program</li>
<li>PullUpload: pulling media files for upload</li>

Support v2017 task types:
<li>Transcode: transcoding task</li>
<li>SnapshotByTimeOffset: screencapturing task</li>
<li>Concat: video splicing task</li>
<li>Clip: video clipping task</li>
<li>ImageSprites: image sprite generating task</li>\n        :type TaskType: str\n        :param Status: Task status. Valid values:
<li>WAITING: waiting;</li>
<li>PROCESSING: processing;</li>
<li>FINISH: completed.</li>\n        :type Status: str\n        :param CreateTime: Creation time of task in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param BeginProcessTime: Start time of task execution in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type BeginProcessTime: str\n        :param FinishTime: End time of task execution in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type FinishTime: str\n        :param ProcedureTask: Video processing task information. This field has a value only when `TaskType` is `Procedure`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProcedureTask: :class:`tencentcloud.vod.v20180717.models.ProcedureTask`\n        :param EditMediaTask: Video editing task information. This field has a value only when `TaskType` is `EditMedia`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EditMediaTask: :class:`tencentcloud.vod.v20180717.models.EditMediaTask`\n        :param WechatPublishTask: Release on WeChat task information. This field has a value only when `TaskType` is `WechatPublish`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WechatPublishTask: :class:`tencentcloud.vod.v20180717.models.WechatPublishTask`\n        :param ComposeMediaTask: Media file composing task information. This field has a value only when `TaskType` is `ComposeMedia`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ComposeMediaTask: :class:`tencentcloud.vod.v20180717.models.ComposeMediaTask`\n        :param SplitMediaTask: Video splitting task information. This field has a value only when `TaskType` is `EditMedia`.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SplitMediaTask: :class:`tencentcloud.vod.v20180717.models.SplitMediaTask`\n        :param WechatMiniProgramPublishTask: Release on WeChat Mini Program task information. This field has a value only when `TaskType` is `WechatMiniProgramPublish`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WechatMiniProgramPublishTask: :class:`tencentcloud.vod.v20180717.models.WechatMiniProgramPublishTask`\n        :param PullUploadTask: Media file pulling for upload task information. This field has a value only when `TaskType` is `PullUpload`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PullUploadTask: :class:`tencentcloud.vod.v20180717.models.PullUploadTask`\n        :param TranscodeTask: Video transcoding task information. This field has a value only when `TaskType` is `Transcode`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TranscodeTask: :class:`tencentcloud.vod.v20180717.models.TranscodeTask2017`\n        :param ConcatTask: Video splicing task information. This field has a value only when `TaskType` is `Concat`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ConcatTask: :class:`tencentcloud.vod.v20180717.models.ConcatTask2017`\n        :param ClipTask: Video clipping task information. This field has a value only when `TaskType` is `Clip`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClipTask: :class:`tencentcloud.vod.v20180717.models.ClipTask2017`\n        :param CreateImageSpriteTask: Image sprite creating task information. This field has a value only when `TaskType` is `ImageSprite`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateImageSpriteTask: :class:`tencentcloud.vod.v20180717.models.CreateImageSpriteTask2017`\n        :param SnapshotByTimeOffsetTask: Time point screencapturing task information. This field has a value only when `TaskType` is `SnapshotByTimeOffset`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SnapshotByTimeOffsetTask: :class:`tencentcloud.vod.v20180717.models.SnapshotByTimeOffsetTask2017`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskType = None
        self.Status = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.ProcedureTask = None
        self.EditMediaTask = None
        self.WechatPublishTask = None
        self.ComposeMediaTask = None
        self.SplitMediaTask = None
        self.WechatMiniProgramPublishTask = None
        self.PullUploadTask = None
        self.TranscodeTask = None
        self.ConcatTask = None
        self.ClipTask = None
        self.CreateImageSpriteTask = None
        self.SnapshotByTimeOffsetTask = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("ProcedureTask") is not None:
            self.ProcedureTask = ProcedureTask()
            self.ProcedureTask._deserialize(params.get("ProcedureTask"))
        if params.get("EditMediaTask") is not None:
            self.EditMediaTask = EditMediaTask()
            self.EditMediaTask._deserialize(params.get("EditMediaTask"))
        if params.get("WechatPublishTask") is not None:
            self.WechatPublishTask = WechatPublishTask()
            self.WechatPublishTask._deserialize(params.get("WechatPublishTask"))
        if params.get("ComposeMediaTask") is not None:
            self.ComposeMediaTask = ComposeMediaTask()
            self.ComposeMediaTask._deserialize(params.get("ComposeMediaTask"))
        if params.get("SplitMediaTask") is not None:
            self.SplitMediaTask = SplitMediaTask()
            self.SplitMediaTask._deserialize(params.get("SplitMediaTask"))
        if params.get("WechatMiniProgramPublishTask") is not None:
            self.WechatMiniProgramPublishTask = WechatMiniProgramPublishTask()
            self.WechatMiniProgramPublishTask._deserialize(params.get("WechatMiniProgramPublishTask"))
        if params.get("PullUploadTask") is not None:
            self.PullUploadTask = PullUploadTask()
            self.PullUploadTask._deserialize(params.get("PullUploadTask"))
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = TranscodeTask2017()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("ConcatTask") is not None:
            self.ConcatTask = ConcatTask2017()
            self.ConcatTask._deserialize(params.get("ConcatTask"))
        if params.get("ClipTask") is not None:
            self.ClipTask = ClipTask2017()
            self.ClipTask._deserialize(params.get("ClipTask"))
        if params.get("CreateImageSpriteTask") is not None:
            self.CreateImageSpriteTask = CreateImageSpriteTask2017()
            self.CreateImageSpriteTask._deserialize(params.get("CreateImageSpriteTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = SnapshotByTimeOffsetTask2017()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks request structure.

    """

    def __init__(self):
        """
        :param Status: Filter: Task status. Valid values: WAITING (waiting), PROCESSING (processing), FINISH (completed).\n        :type Status: str\n        :param FileId: Filter: file ID.\n        :type FileId: str\n        :param CreateTime: Filter: task creation time.\n        :type CreateTime: :class:`tencentcloud.vod.v20180717.models.TimeRange`\n        :param FinishTime: Filter: task end time.\n        :type FinishTime: :class:`tencentcloud.vod.v20180717.models.TimeRange`\n        :param Sort: Sort field. Valid values:
<li>`CreateTime`: task creation time</li>
<li>`FinishTime`: task end time</li>\n        :type Sort: :class:`tencentcloud.vod.v20180717.models.SortBy`\n        :param Limit: Number of entries to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param ScrollToken: Scrolling identifier which is used for pulling in batches. If a single request cannot pull all the data entries, the API will return `ScrollToken`, and if the next request carries it, the next pull will start from the next entry.\n        :type ScrollToken: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Status = None
        self.FileId = None
        self.CreateTime = None
        self.FinishTime = None
        self.Sort = None
        self.Limit = None
        self.ScrollToken = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.FileId = params.get("FileId")
        if params.get("CreateTime") is not None:
            self.CreateTime = TimeRange()
            self.CreateTime._deserialize(params.get("CreateTime"))
        if params.get("FinishTime") is not None:
            self.FinishTime = TimeRange()
            self.FinishTime._deserialize(params.get("FinishTime"))
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        self.Limit = params.get("Limit")
        self.ScrollToken = params.get("ScrollToken")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks response structure.

    """

    def __init__(self):
        """
        :param TaskSet: Task overview list.\n        :type TaskSet: list of TaskSimpleInfo\n        :param ScrollToken: Scrolling identifier. If a request does not return all the data entries, this field indicates the ID of the next entry. If this field is empty, there is no more data.\n        :type ScrollToken: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskSet = None
        self.ScrollToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskSimpleInfo()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.ScrollToken = params.get("ScrollToken")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeTemplatesRequest(AbstractModel):
    """DescribeTranscodeTemplates request structure.

    """

    def __init__(self):
        """
        :param Definitions: Unique ID filter of transcoding templates. Array length limit: 100.\n        :type Definitions: list of int\n        :param Type: Template type filter. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param ContainerType: Container filter. Valid values:
<li>Video: video container that can contain both video stream and audio stream;</li>
<li>PureAudio: audio container that can contain only audio stream.</li>\n        :type ContainerType: str\n        :param TEHDType: TESHD filter, which is used to filter common transcoding or ultra-fast HD transcoding templates. Valid values:
<li>Common: Common transcoding template;</li>
<li>TEHD: TESHD template.</li>\n        :type TEHDType: str\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definitions = None
        self.Type = None
        self.ContainerType = None
        self.TEHDType = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.ContainerType = params.get("ContainerType")
        self.TEHDType = params.get("TEHDType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeTemplatesResponse(AbstractModel):
    """DescribeTranscodeTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param TranscodeTemplateSet: List of transcoding template details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TranscodeTemplateSet: list of TranscodeTemplate\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TranscodeTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TranscodeTemplateSet") is not None:
            self.TranscodeTemplateSet = []
            for item in params.get("TranscodeTemplateSet"):
                obj = TranscodeTemplate()
                obj._deserialize(item)
                self.TranscodeTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVodDomainsRequest(AbstractModel):
    """DescribeVodDomains request structure.

    """

    def __init__(self):
        """
        :param Domains: List of domain names. If this parameter is left empty, all domain names will be listed.
<li>Maximum number of domain names listed: 20</li>\n        :type Domains: list of str\n        :param Limit: Maximum results to return for pulling paginated queries. Default value: 20\n        :type Limit: int\n        :param Offset: Page number offset from the beginning of paginated queries. Default value: 0\n        :type Offset: int\n        :param SubAppId: VOD [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID. If you need to access a resource in a subapplication, set this parameter to the subapplication ID; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Domains = None
        self.Limit = None
        self.Offset = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVodDomainsResponse(AbstractModel):
    """DescribeVodDomains response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of domain names\n        :type TotalCount: int\n        :param DomainSet: Domain name information list\n        :type DomainSet: list of DomainDetailInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.DomainSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DomainSet") is not None:
            self.DomainSet = []
            for item in params.get("DomainSet"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self.DomainSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWatermarkTemplatesRequest(AbstractModel):
    """DescribeWatermarkTemplates request structure.

    """

    def __init__(self):
        """
        :param Definitions: Unique ID filter of watermarking templates. Array length limit: 100.\n        :type Definitions: list of int\n        :param Type: Watermark type filter. Valid values:
<li>image: image watermark;</li>
<li>text: text watermark.</li>\n        :type Type: str\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of returned entries
<li>Default value: 10;</li>
<li>Maximum value: 100.</li>\n        :type Limit: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definitions = None
        self.Type = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWatermarkTemplatesResponse(AbstractModel):
    """DescribeWatermarkTemplates response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param WatermarkTemplateSet: List of watermarking template details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WatermarkTemplateSet: list of WatermarkTemplate\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.WatermarkTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WatermarkTemplateSet") is not None:
            self.WatermarkTemplateSet = []
            for item in params.get("WatermarkTemplateSet"):
                obj = WatermarkTemplate()
                obj._deserialize(item)
                self.WatermarkTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWordSamplesRequest(AbstractModel):
    """DescribeWordSamples request structure.

    """

    def __init__(self):
        """
        :param Usages: <b>Keyword usage. Valid values:</b>
1. Recognition.Ocr: OCR-based content recognition
2. Recognition.Asr: ASR-based content recognition
3. Review.Ocr: OCR-based inappropriate information recognition
4. Review.Asr: ASR-based inappropriate information recognition
<b>Valid values can also be:</b>
5. Recognition: ASR- and OCR-based content recognition; equivalent to 1+2
6. Review: ASR- and OCR-based inappropriate information recognition; equivalent to 3+4
You can select multiple elements, which are connected by OR logic. If a use case contains any element in this parameter, the keyword sample will be used.\n        :type Usages: list of str\n        :param Keywords: Keyword filter. Array length limit: 100 words.\n        :type Keywords: list of str\n        :param Tags: Tag filter. Array length limit: 20 words.\n        :type Tags: list of str\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of entries to be returned. Default value: 100. Maximum value: 100.\n        :type Limit: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Usages = None
        self.Keywords = None
        self.Tags = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        self.Keywords = params.get("Keywords")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWordSamplesResponse(AbstractModel):
    """DescribeWordSamples response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.\n        :type TotalCount: int\n        :param WordSet: Keyword information.\n        :type WordSet: list of AiSampleWord\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.WordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WordSet") is not None:
            self.WordSet = []
            for item in params.get("WordSet"):
                obj = AiSampleWord()
                obj._deserialize(item)
                self.WordSet.append(obj)
        self.RequestId = params.get("RequestId")


class DomainDetailInfo(AbstractModel):
    """Domain name information

    """

    def __init__(self):
        """
        :param Domain: Domain name\n        :type Domain: str\n        :param AccelerateAreaInfos: Acceleration region information
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type AccelerateAreaInfos: list of AccelerateAreaInfo\n        :param DeployStatus: Deployment status. Valid values:
<li>Online</li>
<li>Deploying</li>
<li>Locked: you cannot change the deployment status of locked domain names</li>\n        :type DeployStatus: str\n        :param HTTPSConfig: HTTPS configuration information
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type HTTPSConfig: :class:`tencentcloud.vod.v20180717.models.DomainHTTPSConfig`\n        :param UrlSignatureAuthPolicy: [Key hotlink protection](https://intl.cloud.tencent.com/document/product/266/33986) configuration
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type UrlSignatureAuthPolicy: :class:`tencentcloud.vod.v20180717.models.UrlSignatureAuthPolicy`\n        :param RefererAuthPolicy: [Referer hotlink protection](https://intl.cloud.tencent.com/document/product/266/33985) configuration
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type RefererAuthPolicy: :class:`tencentcloud.vod.v20180717.models.RefererAuthPolicy`\n        :param CreateTime: The time when the domain name was added in the VOD system
<li>The time is in [ISO 8601 date format](https://intl.cloud.tencent.com/document/product/266/11732).</li>\n        :type CreateTime: str\n        """
        self.Domain = None
        self.AccelerateAreaInfos = None
        self.DeployStatus = None
        self.HTTPSConfig = None
        self.UrlSignatureAuthPolicy = None
        self.RefererAuthPolicy = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("AccelerateAreaInfos") is not None:
            self.AccelerateAreaInfos = []
            for item in params.get("AccelerateAreaInfos"):
                obj = AccelerateAreaInfo()
                obj._deserialize(item)
                self.AccelerateAreaInfos.append(obj)
        self.DeployStatus = params.get("DeployStatus")
        if params.get("HTTPSConfig") is not None:
            self.HTTPSConfig = DomainHTTPSConfig()
            self.HTTPSConfig._deserialize(params.get("HTTPSConfig"))
        if params.get("UrlSignatureAuthPolicy") is not None:
            self.UrlSignatureAuthPolicy = UrlSignatureAuthPolicy()
            self.UrlSignatureAuthPolicy._deserialize(params.get("UrlSignatureAuthPolicy"))
        if params.get("RefererAuthPolicy") is not None:
            self.RefererAuthPolicy = RefererAuthPolicy()
            self.RefererAuthPolicy._deserialize(params.get("RefererAuthPolicy"))
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainHTTPSConfig(AbstractModel):
    """HTTPS configuration information of the domain name

    """

    def __init__(self):
        """
        :param CertExpireTime: Time when the certificate expires
<li>The time is in [ISO 8601 date format](https://intl.cloud.tencent.com/document/product/266/11732).</li>\n        :type CertExpireTime: str\n        """
        self.CertExpireTime = None


    def _deserialize(self, params):
        self.CertExpireTime = params.get("CertExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmStreamingsInfo(AbstractModel):
    """DRM-protected adaptive bitstream playback information

    """

    def __init__(self):
        """
        :param SimpleAesDefinition: ID of the adaptive bitrate streaming template whose protection type is SimpleAES.\n        :type SimpleAesDefinition: int\n        """
        self.SimpleAesDefinition = None


    def _deserialize(self, params):
        self.SimpleAesDefinition = params.get("SimpleAesDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmStreamingsInfoForUpdate(AbstractModel):
    """Modification object of DRM-protected adaptive bitstream playback information

    """

    def __init__(self):
        """
        :param SimpleAesDefinition: ID of the adaptive bitrate streaming template whose protection type is SimpleAES.\n        :type SimpleAesDefinition: int\n        """
        self.SimpleAesDefinition = None


    def _deserialize(self, params):
        self.SimpleAesDefinition = params.get("SimpleAesDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaFileInfo(AbstractModel):
    """VOD video file editing information

    """

    def __init__(self):
        """
        :param FileId: Video ID.\n        :type FileId: str\n        :param StartTimeOffset: Start time offset of video clipping in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of video clipping in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EndTimeOffset: float\n        """
        self.FileId = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaOutputConfig(AbstractModel):
    """Result file output of video editing.

    """

    def __init__(self):
        """
        :param MediaName: Output filename of up to 64 characters, which is generated by the system by default.\n        :type MediaName: str\n        :param Type: Output file format. Valid values: mp4, hls. Default value: mp4.\n        :type Type: str\n        :param ClassId: Category ID, which is used to categorize the media for management. A category can be created and its ID can be obtained by using the [category creating](https://intl.cloud.tencent.com/document/product/266/7812?from_cn_redirect=1) API.
<li>Default value: 0, which means "Other".</li>\n        :type ClassId: int\n        :param ExpireTime: Expiration time of output media file in ISO 8601 format, after which the file will be deleted. Files will never expire by default. For more information, please see [Notes on ISO Date Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type ExpireTime: str\n        """
        self.MediaName = None
        self.Type = None
        self.ClassId = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.MediaName = params.get("MediaName")
        self.Type = params.get("Type")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaRequest(AbstractModel):
    """EditMedia request structure.

    """

    def __init__(self):
        """
        :param InputType: Input video type. Valid values: File, Stream.\n        :type InputType: str\n        :param FileInfos: Information of input video file, which is required if `InputType` is `File`.\n        :type FileInfos: list of EditMediaFileInfo\n        :param StreamInfos: Input stream information, which is required if `InputType` is `Stream`.\n        :type StreamInfos: list of EditMediaStreamInfo\n        :param Definition: Editing template ID. Valid values: 10, 20. If this parameter is left empty, template 10 will be used.
<li>10: the input with the highest resolution will be used as the benchmark;</li>
<li>20: the input with the highest bitrate will be used as the benchmark;</li>\n        :type Definition: int\n        :param ProcedureName: [Task flow template](https://intl.cloud.tencent.com/document/product/266/11700?from_cn_redirect=1#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF) name, which should be entered if you want to perform a task flow on the generated new video.\n        :type ProcedureName: str\n        :param OutputConfig: Configuration of file generated after editing.\n        :type OutputConfig: :class:`tencentcloud.vod.v20180717.models.EditMediaOutputConfig`\n        :param SessionContext: Identifies the source context which is used to pass through the user request information. The `EditMediaComplete` callback and task flow status change callback will return the value of this field. It can contain up to 1,000 characters.\n        :type SessionContext: str\n        :param TasksPriority: Task priority. The higher the value, the higher the priority. Value range: -10-10. If this parameter is left empty, 0 will be used.\n        :type TasksPriority: int\n        :param SessionId: Used to identify duplicate requests. After you send a request, if any request with the same `SessionId` has already been sent in the last three days (72 hours), an error message will be returned. `SessionId` contains up to 50 characters. If this parameter is not carried or is an empty string, no deduplication will be performed.\n        :type SessionId: str\n        :param ExtInfo: Reserved field for special purposes.\n        :type ExtInfo: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.InputType = None
        self.FileInfos = None
        self.StreamInfos = None
        self.Definition = None
        self.ProcedureName = None
        self.OutputConfig = None
        self.SessionContext = None
        self.TasksPriority = None
        self.SessionId = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.InputType = params.get("InputType")
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = EditMediaStreamInfo()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Definition = params.get("Definition")
        self.ProcedureName = params.get("ProcedureName")
        if params.get("OutputConfig") is not None:
            self.OutputConfig = EditMediaOutputConfig()
            self.OutputConfig._deserialize(params.get("OutputConfig"))
        self.SessionContext = params.get("SessionContext")
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaResponse(AbstractModel):
    """EditMedia response structure.

    """

    def __init__(self):
        """
        :param TaskId: Video editing task ID, which can be used to query the status of editing task (with task type being `EditMedia`).\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EditMediaStreamInfo(AbstractModel):
    """Video stream editing information

    """

    def __init__(self):
        """
        :param StreamId: ID of recorded stream\n        :type StreamId: str\n        :param StartTime: Start time of stream clipping in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StartTime: str\n        :param EndTime: End time of stream clipping in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EndTime: str\n        """
        self.StreamId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaTask(AbstractModel):
    """Video editing task information

    """

    def __init__(self):
        """
        :param TaskId: Task ID.\n        :type TaskId: str\n        :param Status: Task flow status. Valid values:
<li>PROCESSING: processing;</li>
<li>FINISH: completed.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: str\n        :param ErrCode: Error code. 0: success; other values: failure.
<li>40000: invalid input parameter. Please check it;</li>
<li>60000: invalid source file (e.g., video data is corrupted). Please check whether the source file is normal;</li>
<li>70000: internal service error. Please try again.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ErrCode: int\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of video editing task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.EditMediaTaskInput`\n        :param Output: Output of video editing task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.EditMediaTaskOutput`\n        :param ProcedureTaskId: If a video processing flow is specified when a video editing task is initiated, this field will be the ID of the task flow.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProcedureTaskId: str\n        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SessionContext: str\n        :param SessionId: The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SessionId: str\n        :param MetaData: Metadata of a source video\n        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`\n        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.ErrCodeExt = None
        self.Message = None
        self.Input = None
        self.Output = None
        self.ProcedureTaskId = None
        self.SessionContext = None
        self.SessionId = None
        self.MetaData = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = EditMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = EditMediaTaskOutput()
            self.Output._deserialize(params.get("Output"))
        self.ProcedureTaskId = params.get("ProcedureTaskId")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaTaskInput(AbstractModel):
    """Input of video editing task.

    """

    def __init__(self):
        """
        :param InputType: Input video source type. Valid values: File, Stream.\n        :type InputType: str\n        :param FileInfoSet: Information of input video file. This field has a value only when `InputType` is `File`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileInfoSet: list of EditMediaFileInfo\n        :param StreamInfoSet: Input stream information. This field has a value only when `InputType` is `Stream`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StreamInfoSet: list of EditMediaStreamInfo\n        """
        self.InputType = None
        self.FileInfoSet = None
        self.StreamInfoSet = None


    def _deserialize(self, params):
        self.InputType = params.get("InputType")
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)
        if params.get("StreamInfoSet") is not None:
            self.StreamInfoSet = []
            for item in params.get("StreamInfoSet"):
                obj = EditMediaStreamInfo()
                obj._deserialize(item)
                self.StreamInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaTaskOutput(AbstractModel):
    """Output of video editing task

    """

    def __init__(self):
        """
        :param FileType: File type, such as mp4 and flv.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileType: str\n        :param FileUrl: Media file playback address.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileUrl: str\n        :param FileId: Media file ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: str\n        :param MediaName: Output filename of up to 64 characters, which is generated by the system by default.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MediaName: str\n        :param ClassId: Category ID, which is used to categorize the media for management. A category can be created and its ID can be obtained by using the [category creating](https://intl.cloud.tencent.com/document/product/266/7812?from_cn_redirect=1) API.
<li>Default value: 0, which means "Other".</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClassId: int\n        :param ExpireTime: Expiration time of output media file in ISO 8601 format, after which the file will be deleted. Files will never expire by default. For more information, please see [Notes on ISO Date Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExpireTime: str\n        """
        self.FileType = None
        self.FileUrl = None
        self.FileId = None
        self.MediaName = None
        self.ClassId = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.FileType = params.get("FileType")
        self.FileUrl = params.get("FileUrl")
        self.FileId = params.get("FileId")
        self.MediaName = params.get("MediaName")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmptyTrackItem(AbstractModel):
    """Empty track segment used as placeholder on time axis. If you want a period of silence between two audio segments, you can use `EmptyTrackItem` to hold the place.

    """

    def __init__(self):
        """
        :param Duration: Duration in seconds.\n        :type Duration: float\n        """
        self.Duration = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventContent(AbstractModel):
    """Event notification content, where TranscodeCompleteEvent, ConcatCompleteEvent, ClipCompleteEvent, CreateImageSpriteCompleteEvent, and SnapshotByTimeOffsetCompleteEvent are event notifications for tasks that are initiated by v2017-compatible APIs.

    """

    def __init__(self):
        """
        :param EventHandle: Event handler. The caller must call `ConfirmEvents` to confirm that the message has been received, and the confirmation is valid for 30 seconds. After the confirmation expires, the event can be obtained again.\n        :type EventHandle: str\n        :param EventType: <b>Supported event types:</b>
<li>NewFileUpload: finished video upload</li>
<li>ProcedureStateChanged: task flow status changed</li>
<li>FileDeleted: finished video deletion</li>
<li>PullComplete: finished pulling for upload</li>
<li>EditMediaComplete: finished video editing</li>
<li>SplitMediaComplete: finished video splitting</li>
<li>WechatPublishComplete: finished publishing on WeChat</li>
<li>ComposeMediaComplete: finished producing the media file</li>
<li>WechatMiniProgramPublishComplete: finished publishing on WeChat Mini Program</li>
<b>Support v2017 task types:</b>
<li>TranscodeComplete: finished video transcoding</li>
<li>ConcatComplete: finished video splicing</li>
<li>ClipComplete: finished video clipping</li>
<li>CreateImageSpriteComplete: finished image sprite generation</li>
<li>CreateSnapshotByTimeOffsetComplete: finished point-in-time screencapturing</li>\n        :type EventType: str\n        :param FileUploadEvent: Video upload completion event, which is valid if the event type is `NewFileUpload`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileUploadEvent: :class:`tencentcloud.vod.v20180717.models.FileUploadTask`\n        :param ProcedureStateChangeEvent: Task flow status change event, which is valid if the event type is `ProcedureStateChanged`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProcedureStateChangeEvent: :class:`tencentcloud.vod.v20180717.models.ProcedureTask`\n        :param FileDeleteEvent: File deletion event, which is valid if the event type is `FileDeleted`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileDeleteEvent: :class:`tencentcloud.vod.v20180717.models.FileDeleteTask`\n        :param PullCompleteEvent: Video pull for upload completion event, which is valid if the event type is `PullComplete`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PullCompleteEvent: :class:`tencentcloud.vod.v20180717.models.PullUploadTask`\n        :param EditMediaCompleteEvent: Video editing completion event, which is valid if the event type is `EditMediaComplete`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EditMediaCompleteEvent: :class:`tencentcloud.vod.v20180717.models.EditMediaTask`\n        :param SplitMediaCompleteEvent: Video splitting completion event, which is valid if the event type is `EditMediaComplete`.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SplitMediaCompleteEvent: :class:`tencentcloud.vod.v20180717.models.SplitMediaTask`\n        :param ComposeMediaCompleteEvent: Media file composing task completion event, which is valid when the event type is `ComposeMediaComplete`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ComposeMediaCompleteEvent: :class:`tencentcloud.vod.v20180717.models.ComposeMediaTask`\n        :param ClipCompleteEvent: Video clipping completion event, which is valid if the event type is `ClipComplete`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClipCompleteEvent: :class:`tencentcloud.vod.v20180717.models.ClipTask2017`\n        :param TranscodeCompleteEvent: Video transcoding completion event, which is valid if the event type is `TranscodeComplete`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TranscodeCompleteEvent: :class:`tencentcloud.vod.v20180717.models.TranscodeTask2017`\n        :param CreateImageSpriteCompleteEvent: Image sprite generating completion event, which is valid if the event type is `CreateImageSpriteComplete`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateImageSpriteCompleteEvent: :class:`tencentcloud.vod.v20180717.models.CreateImageSpriteTask2017`\n        :param ConcatCompleteEvent: Video splicing completion event, which is valid if the event type is `ConcatComplete`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ConcatCompleteEvent: :class:`tencentcloud.vod.v20180717.models.ConcatTask2017`\n        :param SnapshotByTimeOffsetCompleteEvent: Time point screencapturing completion event, which is valid when the event type is `CreateSnapshotByTimeOffsetComplete`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SnapshotByTimeOffsetCompleteEvent: :class:`tencentcloud.vod.v20180717.models.SnapshotByTimeOffsetTask2017`\n        :param WechatPublishCompleteEvent: Release on WeChat completion event, which is valid if the event type is `WechatPublishComplete`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WechatPublishCompleteEvent: :class:`tencentcloud.vod.v20180717.models.WechatPublishTask`\n        :param WechatMiniProgramPublishCompleteEvent: Release on WeChat Mini Program task completion event, which is valid if the event type is `WechatMiniProgramPublishComplete`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WechatMiniProgramPublishCompleteEvent: :class:`tencentcloud.vod.v20180717.models.WechatMiniProgramPublishTask`\n        """
        self.EventHandle = None
        self.EventType = None
        self.FileUploadEvent = None
        self.ProcedureStateChangeEvent = None
        self.FileDeleteEvent = None
        self.PullCompleteEvent = None
        self.EditMediaCompleteEvent = None
        self.SplitMediaCompleteEvent = None
        self.ComposeMediaCompleteEvent = None
        self.ClipCompleteEvent = None
        self.TranscodeCompleteEvent = None
        self.CreateImageSpriteCompleteEvent = None
        self.ConcatCompleteEvent = None
        self.SnapshotByTimeOffsetCompleteEvent = None
        self.WechatPublishCompleteEvent = None
        self.WechatMiniProgramPublishCompleteEvent = None


    def _deserialize(self, params):
        self.EventHandle = params.get("EventHandle")
        self.EventType = params.get("EventType")
        if params.get("FileUploadEvent") is not None:
            self.FileUploadEvent = FileUploadTask()
            self.FileUploadEvent._deserialize(params.get("FileUploadEvent"))
        if params.get("ProcedureStateChangeEvent") is not None:
            self.ProcedureStateChangeEvent = ProcedureTask()
            self.ProcedureStateChangeEvent._deserialize(params.get("ProcedureStateChangeEvent"))
        if params.get("FileDeleteEvent") is not None:
            self.FileDeleteEvent = FileDeleteTask()
            self.FileDeleteEvent._deserialize(params.get("FileDeleteEvent"))
        if params.get("PullCompleteEvent") is not None:
            self.PullCompleteEvent = PullUploadTask()
            self.PullCompleteEvent._deserialize(params.get("PullCompleteEvent"))
        if params.get("EditMediaCompleteEvent") is not None:
            self.EditMediaCompleteEvent = EditMediaTask()
            self.EditMediaCompleteEvent._deserialize(params.get("EditMediaCompleteEvent"))
        if params.get("SplitMediaCompleteEvent") is not None:
            self.SplitMediaCompleteEvent = SplitMediaTask()
            self.SplitMediaCompleteEvent._deserialize(params.get("SplitMediaCompleteEvent"))
        if params.get("ComposeMediaCompleteEvent") is not None:
            self.ComposeMediaCompleteEvent = ComposeMediaTask()
            self.ComposeMediaCompleteEvent._deserialize(params.get("ComposeMediaCompleteEvent"))
        if params.get("ClipCompleteEvent") is not None:
            self.ClipCompleteEvent = ClipTask2017()
            self.ClipCompleteEvent._deserialize(params.get("ClipCompleteEvent"))
        if params.get("TranscodeCompleteEvent") is not None:
            self.TranscodeCompleteEvent = TranscodeTask2017()
            self.TranscodeCompleteEvent._deserialize(params.get("TranscodeCompleteEvent"))
        if params.get("CreateImageSpriteCompleteEvent") is not None:
            self.CreateImageSpriteCompleteEvent = CreateImageSpriteTask2017()
            self.CreateImageSpriteCompleteEvent._deserialize(params.get("CreateImageSpriteCompleteEvent"))
        if params.get("ConcatCompleteEvent") is not None:
            self.ConcatCompleteEvent = ConcatTask2017()
            self.ConcatCompleteEvent._deserialize(params.get("ConcatCompleteEvent"))
        if params.get("SnapshotByTimeOffsetCompleteEvent") is not None:
            self.SnapshotByTimeOffsetCompleteEvent = SnapshotByTimeOffsetTask2017()
            self.SnapshotByTimeOffsetCompleteEvent._deserialize(params.get("SnapshotByTimeOffsetCompleteEvent"))
        if params.get("WechatPublishCompleteEvent") is not None:
            self.WechatPublishCompleteEvent = WechatPublishTask()
            self.WechatPublishCompleteEvent._deserialize(params.get("WechatPublishCompleteEvent"))
        if params.get("WechatMiniProgramPublishCompleteEvent") is not None:
            self.WechatMiniProgramPublishCompleteEvent = WechatMiniProgramPublishTask()
            self.WechatMiniProgramPublishCompleteEvent._deserialize(params.get("WechatMiniProgramPublishCompleteEvent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteFunctionRequest(AbstractModel):
    """ExecuteFunction request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of called backend API.\n        :type FunctionName: str\n        :param FunctionArg: API parameter. For specific parameter format, negotiate with the backend before calling.\n        :type FunctionArg: str\n        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.\n        :type SessionContext: str\n        :param SessionId: The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed.\n        :type SessionId: str\n        :param ExtInfo: Reserved field for special purposes.\n        :type ExtInfo: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.FunctionName = None
        self.FunctionArg = None
        self.SessionContext = None
        self.SessionId = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.FunctionArg = params.get("FunctionArg")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteFunctionResponse(AbstractModel):
    """ExecuteFunction response structure.

    """

    def __init__(self):
        """
        :param Result: String generated by packaging processing result. For specifications, negotiate with the backend.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class FaceConfigureInfo(AbstractModel):
    """Control parameter of face recognition task

    """

    def __init__(self):
        """
        :param Switch: Switch of face recognition task. Valid values:
<li>ON: enables intelligent face recognition task;</li>
<li>OFF: disables intelligent face recognition task.</li>\n        :type Switch: str\n        :param Score: Face recognition filter score. If this score is reached or exceeded, a recognition result will be returned. Value range: 0–100. Default value: 95.\n        :type Score: float\n        :param DefaultLibraryLabelSet: Default figure filter tag, which specifies the default figure tag that needs to be returned. If this parameter is left empty or a blank value is entered, all results of the default figures will be returned. Valid values:
<li>entertainment: entertainment celebrity;</li>
<li>sport: sports celebrity;</li>
<li>politician: politically sensitive figure.</li>\n        :type DefaultLibraryLabelSet: list of str\n        :param UserDefineLibraryLabelSet: Custom face labels for filtering. After you specify a label, callbacks of face images without this label will be returned. If this parameter is not specified or left empty, callbacks of all face images will be returned.
You can specify up to 100 labels, with each containing up to 16 characters.\n        :type UserDefineLibraryLabelSet: list of str\n        :param FaceLibrary: Figure library. Valid values:
<li>Default: default figure library;</li>
<li>UserDefine: custom figure library.</li>
<li>All: both default and custom figure libraries will be used.</li>
Default value: All (both default and custom figure libraries will be used.)\n        :type FaceLibrary: str\n        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceConfigureInfoForUpdate(AbstractModel):
    """Control parameter of face recognition task

    """

    def __init__(self):
        """
        :param Switch: Switch of face recognition task. Valid values:
<li>ON: enables intelligent face recognition task;</li>
<li>OFF: disables intelligent face recognition task.</li>\n        :type Switch: str\n        :param Score: Face recognition filter score. If this score is reached or exceeded, a recognition result will be returned. Value range: 0–100.\n        :type Score: float\n        :param DefaultLibraryLabelSet: Default figure filter tag, which specifies the default figure tag that needs to be returned. If this parameter is left empty or a blank value is entered, all results of the default figures will be returned. Valid values:
<li>entertainment: entertainment celebrity;</li>
<li>sport: sports celebrity;</li>
<li>politician: politically sensitive figure.</li>\n        :type DefaultLibraryLabelSet: list of str\n        :param UserDefineLibraryLabelSet: Custom face labels for filtering. After you specify a label, callbacks of face images without this label will be returned. If this parameter is not specified or left empty, callbacks of all face images will be returned.
You can specify up to 100 labels, with each containing up to 16 characters.\n        :type UserDefineLibraryLabelSet: list of str\n        :param FaceLibrary: Figure library. Valid values:
<li>Default: default figure library;</li>
<li>UserDefine: custom figure library.</li>
<li>All: both default and custom figure libraries will be used.</li>\n        :type FaceLibrary: str\n        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileDeleteTask(AbstractModel):
    """File deleting task

    """

    def __init__(self):
        """
        :param FileIdSet: List of IDs of deleted files.\n        :type FileIdSet: list of str\n        """
        self.FileIdSet = None


    def _deserialize(self, params):
        self.FileIdSet = params.get("FileIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileUploadTask(AbstractModel):
    """File upload task information

    """

    def __init__(self):
        """
        :param FileId: Unique file ID.\n        :type FileId: str\n        :param MediaBasicInfo: Basic information of media file generated after upload is completed.\n        :type MediaBasicInfo: :class:`tencentcloud.vod.v20180717.models.MediaBasicInfo`\n        :param ProcedureTaskId: If a video processing flow is specified when a video is uploaded, this field will be the ID of the task flow.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProcedureTaskId: str\n        :param MetaData: Metadata, such as size, duration, video stream information, audio stream information, etc.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`\n        """
        self.FileId = None
        self.MediaBasicInfo = None
        self.ProcedureTaskId = None
        self.MetaData = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("MediaBasicInfo") is not None:
            self.MediaBasicInfo = MediaBasicInfo()
            self.MediaBasicInfo._deserialize(params.get("MediaBasicInfo"))
        self.ProcedureTaskId = params.get("ProcedureTaskId")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidMediaDistributionRequest(AbstractModel):
    """ForbidMediaDistribution request structure.

    """

    def __init__(self):
        """
        :param FileIds: List of media files. Up to 20 ones can be submitted at a time.\n        :type FileIds: list of str\n        :param Operation: forbid: forbids, recover: unblocks.\n        :type Operation: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.FileIds = None
        self.Operation = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.Operation = params.get("Operation")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidMediaDistributionResponse(AbstractModel):
    """ForbidMediaDistribution response structure.

    """

    def __init__(self):
        """
        :param NotExistFileIdSet: List of IDs of files that do not exist.\n        :type NotExistFileIdSet: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.NotExistFileIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotExistFileIdSet = params.get("NotExistFileIdSet")
        self.RequestId = params.get("RequestId")


class FrameTagConfigureInfo(AbstractModel):
    """Control parameter of intelligent frame-specific tagging task

    """

    def __init__(self):
        """
        :param Switch: Switch of intelligent frame-specific tagging task. Valid values:
<li>ON: enables intelligent frame-specific tagging task;</li>
<li>OFF: disables intelligent frame-specific tagging task.</li>\n        :type Switch: str\n        :param ScreenshotInterval: Frame capturing interval in seconds. If this parameter is left empty, 1 second will be used by default. Minimum value: 0.5 seconds.\n        :type ScreenshotInterval: float\n        """
        self.Switch = None
        self.ScreenshotInterval = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagConfigureInfoForUpdate(AbstractModel):
    """Control parameter of intelligent frame-specific tagging task

    """

    def __init__(self):
        """
        :param Switch: Switch of intelligent frame-specific tagging task. Valid values:
<li>ON: enables intelligent frame-specific tagging task;</li>
<li>OFF: disables intelligent frame-specific tagging task.</li>\n        :type Switch: str\n        :param ScreenshotInterval: Frame capturing interval in seconds. Minimum value: 0.5 seconds.\n        :type ScreenshotInterval: float\n        """
        self.Switch = None
        self.ScreenshotInterval = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeadTailConfigureInfo(AbstractModel):
    """Control parameter of video opening and ending credits recognition task.

    """

    def __init__(self):
        """
        :param Switch: Switch of video opening and ending credits recognition task. Valid values:
<li>ON: enables video opening and ending credits recognition task;</li>
<li>OFF: disables video opening and ending credits recognition task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeadTailConfigureInfoForUpdate(AbstractModel):
    """Control parameter of video opening and ending credits recognition task.

    """

    def __init__(self):
        """
        :param Switch: Switch of video opening and ending credits recognition task. Valid values:
<li>ON: enables video opening and ending credits recognition task;</li>
<li>OFF: disables video opening and ending credits recognition task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeadTailTaskInput(AbstractModel):
    """Input parameters for a video opening/closing credits generation task

    """

    def __init__(self):
        """
        :param Definition: Video opening/closing credits configuration template ID\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightSegmentItem(AbstractModel):
    """List of intelligently generated highlights.

    """

    def __init__(self):
        """
        :param Confidence: Confidence.\n        :type Confidence: float\n        :param StartTimeOffset: Start time offset of a segment.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of a segment.\n        :type EndTimeOffset: float\n        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsConfigureInfo(AbstractModel):
    """Control parameter of an intelligent highlight generating task

    """

    def __init__(self):
        """
        :param Switch: Switch of an intelligent highlight generating task. Valid values:
<li>ON: enable an intelligent highlight generating task;</li>
<li>OFF: disable an intelligent highlight generating task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightsConfigureInfoForUpdate(AbstractModel):
    """Control parameter of an intelligent highlight generating task

    """

    def __init__(self):
        """
        :param Switch: Switch of an intelligent highlight generating task. Valid values:
<li>ON: enable an intelligent highlight generating task;</li>
<li>OFF: disable an intelligent highlight generating task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSpriteTaskInput(AbstractModel):
    """Input parameter type of image sprite generating task

    """

    def __init__(self):
        """
        :param Definition: Image sprite generating template ID.\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSpriteTemplate(AbstractModel):
    """Details of an image sprite generating template

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an image sprite generating template.\n        :type Definition: int\n        :param Type: Template type. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param Name: Name of an image sprite generating template.\n        :type Name: str\n        :param Width: Maximum value of the width (or long side) of a subimage in an image sprite in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of a subimage in an image sprite in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param SampleType: Sampling type.\n        :type SampleType: str\n        :param SampleInterval: Sampling interval.\n        :type SampleInterval: int\n        :param RowCount: Subimage row count of an image sprite.\n        :type RowCount: int\n        :param ColumnCount: Subimage column count of an image sprite.\n        :type ColumnCount: int\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
Default value: black.\n        :type FillType: str\n        :param Comment: Template description.\n        :type Comment: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTransform(AbstractModel):
    """Operation such as image rotation and flipping

    """

    def __init__(self):
        """
        :param Type: Type. Valid values:
<li> Rotate: image rotation.</li>
<li> Flip: image flipping.</li>\n        :type Type: str\n        :param RotateAngle: Rotation angle of image with its center point as origin. Value range: 0-360. This parameter is valid if `Type` is `Rotate`.\n        :type RotateAngle: float\n        :param Flip: Image flipping action. Valid values:
<li>Horizental: horizontal flipping, i.e., horizontally mirrored.</li>
<li>Vertical: vertical flipping, i.e., vertically mirrored.</li>
This is valid if `Type` is `Flip`.\n        :type Flip: str\n        """
        self.Type = None
        self.RotateAngle = None
        self.Flip = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.RotateAngle = params.get("RotateAngle")
        self.Flip = params.get("Flip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkInput(AbstractModel):
    """Input parameter of image watermarking template

    """

    def __init__(self):
        """
        :param ImageContent: String generated by [Base64-encoding](https://tools.ietf.org/html/rfc4648) a watermark image. JPEG and PNG images are supported.\n        :type ImageContent: str\n        :param Width: Watermark width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the watermark will be the specified percentage of the video width. For example, `10%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in px, the `Width` of the watermark will be in pixels. For example, `100px` means that `Width` is 100 pixels. Value range: [8, 4096].</li>
Default value: 10%.\n        :type Width: str\n        :param Height: Watermark height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the watermark will be the specified percentage of the video height; for example, `10%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in px, the `Height` of the watermark will be in px; for example, `100px` means that `Height` is 100 px. Valid values: 0 or [8,4096].</li>
Default value: 0 px, which means that `Height` will be proportionally scaled according to the aspect ratio of the original watermark image.\n        :type Height: str\n        :param RepeatType: Repeat type of an animated watermark. Valid values:
<li>once: no longer appears after watermark playback ends.</li>
<li>repeat_last_frame: stays on the last frame after watermark playback ends.</li>
<li>repeat (default): repeats the playback until the video ends.</li>\n        :type RepeatType: str\n        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkInputForUpdate(AbstractModel):
    """Input parameter of image watermarking template

    """

    def __init__(self):
        """
        :param ImageContent: String generated by [Base64-encoding](https://tools.ietf.org/html/rfc4648) a watermark image. JPEG and PNG images are supported.\n        :type ImageContent: str\n        :param Width: Watermark width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the watermark will be the specified percentage of the video width. For example, `10%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in px, the `Width` of the watermark will be in pixels. For example, `100px` means that `Width` is 100 pixels. Value range: [8, 4096].</li>\n        :type Width: str\n        :param Height: Watermark height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the watermark will be the specified percentage of the video height; for example, `10%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in px, the `Height` of the watermark will be in px; for example, `100px` means that `Height` is 100 px. Valid values: 0 or [8,4096].</li>\n        :type Height: str\n        :param RepeatType: Repeat type of an animated watermark. Valid values:
<li>once: no longer appears after watermark playback ends.</li>
<li>repeat_last_frame: stays on the last frame after watermark playback ends.</li>
<li>repeat (default): repeats the playback until the video ends.</li>\n        :type RepeatType: str\n        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkTemplate(AbstractModel):
    """Image watermarking template

    """

    def __init__(self):
        """
        :param ImageUrl: Watermark image address.\n        :type ImageUrl: str\n        :param Width: Watermark width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the watermark will be the specified percentage of the video width; for example, `10%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in px, the `Width` of the watermark will be in px; for example, `100px` means that `Width` is 100 px.</li>\n        :type Width: str\n        :param Height: Watermark height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the watermark will be the specified percentage of the video height; for example, `10%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in px, the `Height` of the watermark will be in px; for example, `100px` means that `Height` is 100 px;</li>
`0px` means that `Height` will be proportionally scaled according to the video width.\n        :type Height: str\n        :param RepeatType: Repeat type of an animated watermark. Valid values:
<li>once: no longer appears after watermark playback ends.</li>
<li>repeat_last_frame: stays on the last frame after watermark playback ends.</li>
<li>repeat (default): repeats the playback until the video ends.</li>\n        :type RepeatType: str\n        """
        self.ImageUrl = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveRealTimeClipRequest(AbstractModel):
    """LiveRealTimeClip request structure.

    """

    def __init__(self):
        """
        :param StreamId: [LVB code](https://intl.cloud.tencent.com/document/product/267/5959?from_cn_redirect=1) of a stream.\n        :type StreamId: str\n        :param StartTime: Start time of stream clipping in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type StartTime: str\n        :param EndTime: End time of stream clipping in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type EndTime: str\n        :param IsPersistence: Whether to clip persistently. 0: no, 1: yes. Default: no.\n        :type IsPersistence: int\n        :param ExpireTime: Storage expiration time of video generated by persistent clipping in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I). `9999-12-31T23:59:59Z` means `never expire`. After the expiration, the media file and its related resources (such as transcoding results and image sprites) will be permanently deleted. This parameter will be valid only when `IsPersistence` is 1. By default, the video will never expire.\n        :type ExpireTime: str\n        :param Procedure: VOD task flow processing for video generated by persistent clipping. For more information, please see [Specifying Task Flow After Upload](https://intl.cloud.tencent.com/document/product/266/9759?from_cn_redirect=1). This parameter will be valid only when `IsPersistence` is 1.\n        :type Procedure: str\n        :param MetaDataRequired: Whether the metadata of clipped video needs to be returned. 0: no, 1: yes. Default value: no.\n        :type MetaDataRequired: int\n        :param Host: Domain name used for live clipping. Time shifting must be enabled in LVB.\n        :type Host: str\n        :param ExtInfo: Reserved field. Do not enter a value for it.\n        :type ExtInfo: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.StreamId = None
        self.StartTime = None
        self.EndTime = None
        self.IsPersistence = None
        self.ExpireTime = None
        self.Procedure = None
        self.MetaDataRequired = None
        self.Host = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsPersistence = params.get("IsPersistence")
        self.ExpireTime = params.get("ExpireTime")
        self.Procedure = params.get("Procedure")
        self.MetaDataRequired = params.get("MetaDataRequired")
        self.Host = params.get("Host")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveRealTimeClipResponse(AbstractModel):
    """LiveRealTimeClip response structure.

    """

    def __init__(self):
        """
        :param Url: Playback URL of clipped video.\n        :type Url: str\n        :param FileId: Unique media file ID of video generated by persistent clipping.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: str\n        :param VodTaskId: Task flow ID of video generated by persistent clipping.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VodTaskId: str\n        :param MetaData: Metadata of clipped video.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Url = None
        self.FileId = None
        self.VodTaskId = None
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileId = params.get("FileId")
        self.VodTaskId = params.get("VodTaskId")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class ManageTaskRequest(AbstractModel):
    """ManageTask request structure.

    """

    def __init__(self):
        """
        :param TaskId: Video processing task ID.\n        :type TaskId: str\n        :param OperationType: Operation type. Valid value:
<li>Abort: terminate a task. You can only terminate initiated tasks in `WAITING` status.</li>\n        :type OperationType: str\n        :param SubAppId: VOD [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.TaskId = None
        self.OperationType = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.OperationType = params.get("OperationType")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageTaskResponse(AbstractModel):
    """ManageTask response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MediaAdaptiveDynamicStreamingInfo(AbstractModel):
    """Adaptive bitrate streaming information

    """

    def __init__(self):
        """
        :param AdaptiveDynamicStreamingSet: Information array of adaptive bitrate streaming.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AdaptiveDynamicStreamingSet: list of AdaptiveDynamicStreamingInfoItem\n        """
        self.AdaptiveDynamicStreamingSet = None


    def _deserialize(self, params):
        if params.get("AdaptiveDynamicStreamingSet") is not None:
            self.AdaptiveDynamicStreamingSet = []
            for item in params.get("AdaptiveDynamicStreamingSet"):
                obj = AdaptiveDynamicStreamingInfoItem()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisClassificationItem(AbstractModel):
    """Intelligent categorization result

    """

    def __init__(self):
        """
        :param Classification: Name of intelligently generated category.\n        :type Classification: str\n        :param Confidence: Confidence of intelligently generated category between 0 and 100.\n        :type Confidence: float\n        """
        self.Classification = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Classification = params.get("Classification")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisCoverItem(AbstractModel):
    """Information of intelligently generated cover

    """

    def __init__(self):
        """
        :param CoverUrl: Address of intelligently generated cover.\n        :type CoverUrl: str\n        :param Confidence: Confidence of intelligently generated cover between 0 and 100.\n        :type Confidence: float\n        """
        self.CoverUrl = None
        self.Confidence = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisFrameTagItem(AbstractModel):
    """Result information of intelligent frame-specific tagging

    """

    def __init__(self):
        """
        :param Tag: Frame-specific tag name.\n        :type Tag: str\n        :param CategorySet: Category list of frame-specific tag names. `CategorySet.N` indicates the N+1-level category.
For example, if the `Tag` is "tower", and `CategorySet` contains two elements (`CategorySet.0` is "scene", and `CategorySet.1` is "architecture"), then the frame-specific tag is "tower", the first-level category is "scene", and the second-level category is "architecture".\n        :type CategorySet: list of str\n        :param Confidence: Confidence of intelligently generated frame-specific tag between 0 and 100.\n        :type Confidence: float\n        """
        self.Tag = None
        self.CategorySet = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.CategorySet = params.get("CategorySet")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisFrameTagSegmentItem(AbstractModel):
    """List of frame-specific tag segments

    """

    def __init__(self):
        """
        :param StartTimeOffset: Start time offset of frame-specific tag.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of frame-specific tag.\n        :type EndTimeOffset: float\n        :param TagSet: List of tags in time period.\n        :type TagSet: list of MediaAiAnalysisFrameTagItem\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TagSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisFrameTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisHighlightItem(AbstractModel):
    """Information of an intelligently generated highlight

    """

    def __init__(self):
        """
        :param HighlightUrl: Address of an intelligently generated highlight.\n        :type HighlightUrl: str\n        :param CovImgUrl: Address of an intelligently generated highlight cover.\n        :type CovImgUrl: str\n        :param Confidence: Confidence of an intelligently generated highlight between 0 and 100.\n        :type Confidence: float\n        :param Duration: Duration of an intelligently generated highlight.\n        :type Duration: float\n        :param SegmentSet: List of intelligently generated highlight subsegments, which together form a highlight.\n        :type SegmentSet: list of HighlightSegmentItem\n        """
        self.HighlightUrl = None
        self.CovImgUrl = None
        self.Confidence = None
        self.Duration = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.HighlightUrl = params.get("HighlightUrl")
        self.CovImgUrl = params.get("CovImgUrl")
        self.Confidence = params.get("Confidence")
        self.Duration = params.get("Duration")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = HighlightSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisTagItem(AbstractModel):
    """Result information of intelligent tagging

    """

    def __init__(self):
        """
        :param Tag: Tag name.\n        :type Tag: str\n        :param Confidence: Confidence of tag between 0 and 100.\n        :type Confidence: float\n        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAnimatedGraphicsInfo(AbstractModel):
    """Result information of animated image generating in VOD file

    """

    def __init__(self):
        """
        :param AnimatedGraphicsSet: Result information of animated image generating task
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AnimatedGraphicsSet: list of MediaAnimatedGraphicsItem\n        """
        self.AnimatedGraphicsSet = None


    def _deserialize(self, params):
        if params.get("AnimatedGraphicsSet") is not None:
            self.AnimatedGraphicsSet = []
            for item in params.get("AnimatedGraphicsSet"):
                obj = MediaAnimatedGraphicsItem()
                obj._deserialize(item)
                self.AnimatedGraphicsSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAnimatedGraphicsItem(AbstractModel):
    """Result information of animated image generating task

    """

    def __init__(self):
        """
        :param Url: Address of generated animated image.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Url: str\n        :param Definition: Animated image generating template ID. For more information, please see [Animated Image Generating Parameter Template](https://intl.cloud.tencent.com/document/product/266/33481?from_cn_redirect=1#.3Cspan-id-.3D-.22zdt.22.3E.3C.2Fspan.3E.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Definition: int\n        :param Container: Animated image format, such as gif.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Container: str\n        :param Height: Height of animated image in px.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Height: int\n        :param Width: Width of animated image in px.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Width: int\n        :param Bitrate: Bitrate of animated image in bps.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Bitrate: int\n        :param Size: Size of animated image in bytes.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Size: int\n        :param Md5: MD5 value of an animated image.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Md5: str\n        :param StartTimeOffset: Start time offset of animated image in video in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of animated image in video in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EndTimeOffset: float\n        """
        self.Url = None
        self.Definition = None
        self.Container = None
        self.Height = None
        self.Width = None
        self.Bitrate = None
        self.Size = None
        self.Md5 = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Bitrate = params.get("Bitrate")
        self.Size = params.get("Size")
        self.Md5 = params.get("Md5")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAudioStreamItem(AbstractModel):
    """Information of audio stream in VOD file

    """

    def __init__(self):
        """
        :param Bitrate: Bitrate of audio stream in bps.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Bitrate: int\n        :param SamplingRate: Sample rate of audio stream in Hz.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SamplingRate: int\n        :param Codec: Audio stream encoder, such as aac.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Codec: str\n        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaBasicInfo(AbstractModel):
    """Basic information of VOD media file

    """

    def __init__(self):
        """
        :param Name: Media filename.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Name: str\n        :param Description: Media file description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Description: str\n        :param CreateTime: Creation time of media file in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateTime: str\n        :param UpdateTime: Last update time of media file (by an operation that triggers updating of media file information such as modifying video attributes or initiating video processing) in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UpdateTime: str\n        :param ExpireTime: Expiration time of media file in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I). After the expiration, the media file and its related resources (such as transcoding results and image sprites) will be permanently deleted. `9999-12-31T23:59:59Z` means "never expire".
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExpireTime: str\n        :param ClassId: Category ID of media file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClassId: int\n        :param ClassName: Category name of media file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClassName: str\n        :param ClassPath: Category path to media file separated by "-", such as "new first-level category - new second-level category".
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClassPath: str\n        :param CoverUrl: Cover image address of media file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CoverUrl: str\n        :param Type: Media file container, such as mp4 and flv.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Type: str\n        :param MediaUrl: URL of source media file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MediaUrl: str\n        :param SourceInfo: Source information of media file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SourceInfo: :class:`tencentcloud.vod.v20180717.models.MediaSourceData`\n        :param StorageRegion: Regions where media files are stored, such as `ap-chongqing`. For more regions, see [Storage Region](https://intl.cloud.tencent.com/document/product/266/9760).\n        :type StorageRegion: str\n        :param TagSet: Tag information of media file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TagSet: list of str\n        :param Vid: Unique ID of an LVB recording file.\n        :type Vid: str\n        :param Category: File type:
<li>Video: video file</li>
<li>Audio: audio file</li>
<li>Image: image file</li>\n        :type Category: str\n        :param Status: File status. Valid values: Normal, Forbidden.

*Note: this field is not supported yet.\n        :type Status: str\n        :param StorageClass: Storage class of a media file:
<li>STANDARD</li>
<li>STANDARD_IA</li>\n        :type StorageClass: str\n        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExpireTime = None
        self.ClassId = None
        self.ClassName = None
        self.ClassPath = None
        self.CoverUrl = None
        self.Type = None
        self.MediaUrl = None
        self.SourceInfo = None
        self.StorageRegion = None
        self.TagSet = None
        self.Vid = None
        self.Category = None
        self.Status = None
        self.StorageClass = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ClassId = params.get("ClassId")
        self.ClassName = params.get("ClassName")
        self.ClassPath = params.get("ClassPath")
        self.CoverUrl = params.get("CoverUrl")
        self.Type = params.get("Type")
        self.MediaUrl = params.get("MediaUrl")
        if params.get("SourceInfo") is not None:
            self.SourceInfo = MediaSourceData()
            self.SourceInfo._deserialize(params.get("SourceInfo"))
        self.StorageRegion = params.get("StorageRegion")
        self.TagSet = params.get("TagSet")
        self.Vid = params.get("Vid")
        self.Category = params.get("Category")
        self.Status = params.get("Status")
        self.StorageClass = params.get("StorageClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaClassInfo(AbstractModel):
    """Category information description

    """

    def __init__(self):
        """
        :param ClassId: Category ID\n        :type ClassId: int\n        :param ParentId: Parent category ID, which is -1 for a first-level category.\n        :type ParentId: int\n        :param ClassName: Category name\n        :type ClassName: str\n        :param Level: Category level. 0 for first-level category, up to 3, i.e., up to 4 levels of categories are allowed.\n        :type Level: int\n        :param SubClassIdSet: Set of IDs of the immediate subcategories in current category\n        :type SubClassIdSet: list of int\n        """
        self.ClassId = None
        self.ParentId = None
        self.ClassName = None
        self.Level = None
        self.SubClassIdSet = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.ParentId = params.get("ParentId")
        self.ClassName = params.get("ClassName")
        self.Level = params.get("Level")
        self.SubClassIdSet = params.get("SubClassIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewAsrTextSegmentItem(AbstractModel):
    """Suspected segment identified during ASR-based speech audit in content audit

    """

    def __init__(self):
        """
        :param StartTimeOffset: Start time offset of suspected segment in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of suspected segment in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EndTimeOffset: float\n        :param Confidence: Confidence of suspected segment.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Confidence: float\n        :param Suggestion: Suggestion for suspected segment audit. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Suggestion: str\n        :param KeywordSet: List of suspected keywords.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeywordSet: list of str\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewOcrTextSegmentItem(AbstractModel):
    """Suspected segment identified during OCR-based text audit in content audit

    """

    def __init__(self):
        """
        :param StartTimeOffset: Start time offset of suspected segment in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of suspected segment in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EndTimeOffset: float\n        :param Confidence: Confidence of suspected segment.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Confidence: float\n        :param Suggestion: Suggestion for suspected segment audit. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Suggestion: str\n        :param KeywordSet: List of suspected keywords.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeywordSet: list of str\n        :param AreaCoordSet: Zone coordinates (at the pixel level) of suspected text: [x1, y1, x2, y2], i.e., the coordinates of the top-left and bottom-right corners.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AreaCoordSet: list of int\n        :param Url: URL of a suspected image (which will not be permanently stored
and will be deleted after `PicUrlExpireTime`).\n        :type Url: str\n        :param PicUrlExpireTime: Expiration time of suspected image URL in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type PicUrlExpireTime: str\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None
        self.AreaCoordSet = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewPoliticalSegmentItem(AbstractModel):
    """Suspected politically sensitive segment identified in content audit

    """

    def __init__(self):
        """
        :param StartTimeOffset: Start time offset of a suspected segment in seconds.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of a suspected segment in seconds.\n        :type EndTimeOffset: float\n        :param Confidence: Score of a suspected politically sensitive segment.\n        :type Confidence: float\n        :param Suggestion: Suggestion for politically sensitive information detection of a suspected segment. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>\n        :type Suggestion: str\n        :param Name: Name of a politically sensitive figure or violating photo.\n        :type Name: str\n        :param Label: Tags for the results of politically sensitive information detection of suspected video segments. The relationship between the `LabelSet` parameter in the content audit template [controlling tasks of video politically sensitive information detection](https://intl.cloud.tencent.com/document/api/266/31773?from_cn_redirect=1#PoliticalImgReviewTemplateInfo) and this parameter is as follows:
violation_photo:
<li>violation_photo: violating photo.</li>
politician:
<li>nation_politician: head of state/government;</li>
<li>province_politician: province/state leader;</li>
<li>bureau_politician: ministry leader;</li>
<li>county_politician: county/city leader;</li>
<li>rural_politician: town leader;</li>
<li>sensitive_politician: politically sensitive figure;</li>
<li>foreign_politician: head of a foreign country/government.</li>
entertainment:
<li>sensitive_entertainment: sensitive entertainment celebrity.</li>
sport:
<li>sensitive_sport: sensitive sports figure.</li>
entrepreneur:
<li>sensitive_entrepreneur: sensitive business figure.</li>
scholar:
<li>sensitive_scholar: sensitive educator.</li>
celebrity:
<li>sensitive_celebrity: sensitive well-known figure;</li>
<li>historical_celebrity: well-known historical figures.</li>
military:
<li>sensitive_military: militarily sensitive figure.</li>\n        :type Label: str\n        :param Url: URL of a suspected image (which will not be permanently stored
 and will be deleted after `PicUrlExpireTime`).\n        :type Url: str\n        :param AreaCoordSet: Zone coordinates (at the pixel level) of a politically sensitive figure or violating photo: [x1, y1, x2, y2], i.e., the coordinates of the top-left and bottom-right corners.\n        :type AreaCoordSet: list of int\n        :param PicUrlExpireTimeStamp: This field has been disused. Please use `PicUrlExpireTime`.\n        :type PicUrlExpireTimeStamp: int\n        :param PicUrlExpireTime: Expiration time of suspected image URL in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type PicUrlExpireTime: str\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.Name = None
        self.Label = None
        self.Url = None
        self.AreaCoordSet = None
        self.PicUrlExpireTimeStamp = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Name = params.get("Name")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewSegmentItem(AbstractModel):
    """Suspected porn/terrorism segment identified in content audit

    """

    def __init__(self):
        """
        :param StartTimeOffset: Start time offset of a suspected segment in seconds.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of a suspected segment in seconds.\n        :type EndTimeOffset: float\n        :param Confidence: Score of a suspected porn segment.\n        :type Confidence: float\n        :param Label: Tag of porn information detection result of a suspected segment.\n        :type Label: str\n        :param Suggestion: Suggestion for porn information detection of a suspected segment. Valid values:
<li>pass.</li>
<li>review.</li>
<li>block.</li>\n        :type Suggestion: str\n        :param Url: URL of a suspected image (which will not be permanently stored
 and will be deleted after `PicUrlExpireTime`).\n        :type Url: str\n        :param PicUrlExpireTimeStamp: This field has been disused. Please use `PicUrlExpireTime`.\n        :type PicUrlExpireTimeStamp: int\n        :param PicUrlExpireTime: Expiration time of suspected image URL in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type PicUrlExpireTime: str\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Label = None
        self.Suggestion = None
        self.Url = None
        self.PicUrlExpireTimeStamp = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Url = params.get("Url")
        self.PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaDeleteItem(AbstractModel):
    """Content to be deleted when a VOD video is deleted

    """

    def __init__(self):
        """
        :param Type: Type of the content to be deleted. If this field is left empty, the parameter will be invalid. Valid values:
<li>TranscodeFiles: deletes transcoded files.</li>
<li>WechatPublishFiles: deletes files published on WeChat.</li>\n        :type Type: str\n        :param Definition: ID of the template for which to delete the videos of the type specified by the `Type` parameter. For the template definition, please see [Transcoding Template](https://intl.cloud.tencent.com/document/product/266/33478?from_cn_redirect=1#.3Cspan-id-.3D-.22zm.22-.3E.3C.2Fspan.3E.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF).
Default value: 0, which indicates to delete all videos of the type specified by the `Type` parameter.\n        :type Definition: int\n        """
        self.Type = None
        self.Definition = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaImageSpriteInfo(AbstractModel):
    """Image sprite information of VOD file

    """

    def __init__(self):
        """
        :param ImageSpriteSet: Information set of image sprites with specified specifications. Each element represents a set of image sprites with the same specification.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageSpriteSet: list of MediaImageSpriteItem\n        """
        self.ImageSpriteSet = None


    def _deserialize(self, params):
        if params.get("ImageSpriteSet") is not None:
            self.ImageSpriteSet = []
            for item in params.get("ImageSpriteSet"):
                obj = MediaImageSpriteItem()
                obj._deserialize(item)
                self.ImageSpriteSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaImageSpriteItem(AbstractModel):
    """Image sprite information

    """

    def __init__(self):
        """
        :param Definition: Image sprite specification. For more information, please see [Image Sprite Parameter Template](https://intl.cloud.tencent.com/document/product/266/33480?from_cn_redirect=1#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Definition: int\n        :param Height: Subimage height of image sprite.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Height: int\n        :param Width: Subimage width of image sprite.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Width: int\n        :param TotalCount: Total number of subimages in each image sprite.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param ImageUrlSet: Address of each image sprite.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageUrlSet: list of str\n        :param WebVttUrl: Address of WebVtt file for the position-time relationship among subimages in an image sprite. The WebVtt file indicates the corresponding time points of each subimage and their coordinates in the image sprite, which is typically used by the player for implementing preview.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WebVttUrl: str\n        """
        self.Definition = None
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImageUrlSet = None
        self.WebVttUrl = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImageUrlSet = params.get("ImageUrlSet")
        self.WebVttUrl = params.get("WebVttUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInfo(AbstractModel):
    """VOD file information

    """

    def __init__(self):
        """
        :param BasicInfo: Basic information, such as video name, category, playback address, and cover image.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BasicInfo: :class:`tencentcloud.vod.v20180717.models.MediaBasicInfo`\n        :param MetaData: Metadata, such as size, duration, video stream information, and audio stream information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`\n        :param TranscodeInfo: Result information of transcoding, such as address, specification, bitrate, and resolution of the videos in various bitrates generated by transcoding a video.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TranscodeInfo: :class:`tencentcloud.vod.v20180717.models.MediaTranscodeInfo`\n        :param AnimatedGraphicsInfo: Result information of animated image generating, i.e., relevant information of an animated image (such as .gif) generated from a video.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AnimatedGraphicsInfo: :class:`tencentcloud.vod.v20180717.models.MediaAnimatedGraphicsInfo`\n        :param SampleSnapshotInfo: Sampled screenshot information, i.e., relevant information of a sampled screenshot generated from a video.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SampleSnapshotInfo: :class:`tencentcloud.vod.v20180717.models.MediaSampleSnapshotInfo`\n        :param ImageSpriteInfo: Image sprite information, i.e., relevant information of image sprite generated from video.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageSpriteInfo: :class:`tencentcloud.vod.v20180717.models.MediaImageSpriteInfo`\n        :param SnapshotByTimeOffsetInfo: Time point screenshot information, i.e., information of each time point screenshot generated from a video.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SnapshotByTimeOffsetInfo: :class:`tencentcloud.vod.v20180717.models.MediaSnapshotByTimeOffsetInfo`\n        :param KeyFrameDescInfo: Timestamp information, i.e., information of each timestamp set for a video.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyFrameDescInfo: :class:`tencentcloud.vod.v20180717.models.MediaKeyFrameDescInfo`\n        :param AdaptiveDynamicStreamingInfo: Adaptive bitrate streaming information, such as specification, encryption type, and container format.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AdaptiveDynamicStreamingInfo: :class:`tencentcloud.vod.v20180717.models.MediaAdaptiveDynamicStreamingInfo`\n        :param MiniProgramReviewInfo: WeChat Mini Program audit information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MiniProgramReviewInfo: :class:`tencentcloud.vod.v20180717.models.MediaMiniProgramReviewInfo`\n        :param SubtitleInfo: Subtitle information
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type SubtitleInfo: :class:`tencentcloud.vod.v20180717.models.MediaSubtitleInfo`\n        :param FileId: Unique ID of media file.\n        :type FileId: str\n        """
        self.BasicInfo = None
        self.MetaData = None
        self.TranscodeInfo = None
        self.AnimatedGraphicsInfo = None
        self.SampleSnapshotInfo = None
        self.ImageSpriteInfo = None
        self.SnapshotByTimeOffsetInfo = None
        self.KeyFrameDescInfo = None
        self.AdaptiveDynamicStreamingInfo = None
        self.MiniProgramReviewInfo = None
        self.SubtitleInfo = None
        self.FileId = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = MediaBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("TranscodeInfo") is not None:
            self.TranscodeInfo = MediaTranscodeInfo()
            self.TranscodeInfo._deserialize(params.get("TranscodeInfo"))
        if params.get("AnimatedGraphicsInfo") is not None:
            self.AnimatedGraphicsInfo = MediaAnimatedGraphicsInfo()
            self.AnimatedGraphicsInfo._deserialize(params.get("AnimatedGraphicsInfo"))
        if params.get("SampleSnapshotInfo") is not None:
            self.SampleSnapshotInfo = MediaSampleSnapshotInfo()
            self.SampleSnapshotInfo._deserialize(params.get("SampleSnapshotInfo"))
        if params.get("ImageSpriteInfo") is not None:
            self.ImageSpriteInfo = MediaImageSpriteInfo()
            self.ImageSpriteInfo._deserialize(params.get("ImageSpriteInfo"))
        if params.get("SnapshotByTimeOffsetInfo") is not None:
            self.SnapshotByTimeOffsetInfo = MediaSnapshotByTimeOffsetInfo()
            self.SnapshotByTimeOffsetInfo._deserialize(params.get("SnapshotByTimeOffsetInfo"))
        if params.get("KeyFrameDescInfo") is not None:
            self.KeyFrameDescInfo = MediaKeyFrameDescInfo()
            self.KeyFrameDescInfo._deserialize(params.get("KeyFrameDescInfo"))
        if params.get("AdaptiveDynamicStreamingInfo") is not None:
            self.AdaptiveDynamicStreamingInfo = MediaAdaptiveDynamicStreamingInfo()
            self.AdaptiveDynamicStreamingInfo._deserialize(params.get("AdaptiveDynamicStreamingInfo"))
        if params.get("MiniProgramReviewInfo") is not None:
            self.MiniProgramReviewInfo = MediaMiniProgramReviewInfo()
            self.MiniProgramReviewInfo._deserialize(params.get("MiniProgramReviewInfo"))
        if params.get("SubtitleInfo") is not None:
            self.SubtitleInfo = MediaSubtitleInfo()
            self.SubtitleInfo._deserialize(params.get("SubtitleInfo"))
        self.FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInputInfo(AbstractModel):
    """Information, name, and customer ID of the source video to be processed

    """

    def __init__(self):
        """
        :param Url: Video URL.\n        :type Url: str\n        :param Name: Video name.\n        :type Name: str\n        :param Id: Custom video ID.\n        :type Id: str\n        """
        self.Url = None
        self.Name = None
        self.Id = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaKeyFrameDescInfo(AbstractModel):
    """Video timestamp information

    """

    def __init__(self):
        """
        :param KeyFrameDescSet: Information array of video timestamps.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyFrameDescSet: list of MediaKeyFrameDescItem\n        """
        self.KeyFrameDescSet = None


    def _deserialize(self, params):
        if params.get("KeyFrameDescSet") is not None:
            self.KeyFrameDescSet = []
            for item in params.get("KeyFrameDescSet"):
                obj = MediaKeyFrameDescItem()
                obj._deserialize(item)
                self.KeyFrameDescSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaKeyFrameDescItem(AbstractModel):
    """Video timestamp information

    """

    def __init__(self):
        """
        :param TimeOffset: Offset time of video timestamp in seconds.\n        :type TimeOffset: float\n        :param Content: Content string of timestamp containing 1-128 characters.\n        :type Content: str\n        """
        self.TimeOffset = None
        self.Content = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaMetaData(AbstractModel):
    """VOD media file metadata

    """

    def __init__(self):
        """
        :param Size: Size of uploaded media file in bytes (which is the sum of size of m3u8 and ts files if the video is in HLS format).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Size: int\n        :param Container: Container, such as m4a and mp4.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Container: str\n        :param Bitrate: Sum of the average bitrate of a video stream and that of an audio stream in bps.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Bitrate: int\n        :param Height: Maximum value of the height of a video stream in px.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Height: int\n        :param Width: Maximum value of the width of a video stream in px.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Width: int\n        :param Duration: Video duration in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Duration: float\n        :param Rotate: Selected angle during video recording in degrees.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Rotate: int\n        :param VideoStreamSet: Video stream information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VideoStreamSet: list of MediaVideoStreamItem\n        :param AudioStreamSet: Audio stream information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioStreamSet: list of MediaAudioStreamItem\n        :param VideoDuration: Video duration in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VideoDuration: float\n        :param AudioDuration: Audio duration in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioDuration: float\n        """
        self.Size = None
        self.Container = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.Rotate = None
        self.VideoStreamSet = None
        self.AudioStreamSet = None
        self.VideoDuration = None
        self.AudioDuration = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Container = params.get("Container")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        self.Rotate = params.get("Rotate")
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        self.VideoDuration = params.get("VideoDuration")
        self.AudioDuration = params.get("AudioDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaMiniProgramReviewElem(AbstractModel):
    """Summary metadata of WeChat Mini Program audit.

    """

    def __init__(self):
        """
        :param Type: Audit type. 
<li>Porn: porn image,</li>
<li>Porn.Ocr: porn text,</li>
<li>Porn.Asr: porn speech,</li>
<li>Terrorism: terrorism image,</li>
<li>Political: politically sensitive image,</li>
<li>Political.Ocr: politically sensitive text</li>
<li>Political.Asr: politically sensitive speech</li>\n        :type Type: str\n        :param Suggestion: Audit suggestion.
<li>pass: normal,</li>
<li>block: violating,</li>
<li>review: suspected of violation.</li>\n        :type Suggestion: str\n        :param Confidence: Confidence of audit result between 0 and 100.\n        :type Confidence: float\n        """
        self.Type = None
        self.Suggestion = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaMiniProgramReviewInfo(AbstractModel):
    """WeChat Mini Program audit information

    """

    def __init__(self):
        """
        :param MiniProgramReviewList: Audit information list.\n        :type MiniProgramReviewList: list of MediaMiniProgramReviewInfoItem\n        """
        self.MiniProgramReviewList = None


    def _deserialize(self, params):
        if params.get("MiniProgramReviewList") is not None:
            self.MiniProgramReviewList = []
            for item in params.get("MiniProgramReviewList"):
                obj = MediaMiniProgramReviewInfoItem()
                obj._deserialize(item)
                self.MiniProgramReviewList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaMiniProgramReviewInfoItem(AbstractModel):
    """WeChat Mini Program audit information unit

    """

    def __init__(self):
        """
        :param Definition: Template ID, which is the ID of the transcoding template corresponding to the video published on WeChat Mini Program. 0 represents the source video.\n        :type Definition: int\n        :param MetaData: Video metadata.\n        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`\n        :param Url: Video playback address for WeChat Mini Program audit
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Url: str\n        :param ReviewResult: Status of video release on WeChat Mini Program
<li>Pass: succeeded.</li>
<li>Rejected: rejected.</li>\n        :type ReviewResult: str\n        :param ReviewSummary: WeChat Mini Program audit element.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReviewSummary: list of MediaMiniProgramReviewElem\n        """
        self.Definition = None
        self.MetaData = None
        self.Url = None
        self.ReviewResult = None
        self.ReviewSummary = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.Url = params.get("Url")
        self.ReviewResult = params.get("ReviewResult")
        if params.get("ReviewSummary") is not None:
            self.ReviewSummary = []
            for item in params.get("ReviewSummary"):
                obj = MediaMiniProgramReviewElem()
                obj._deserialize(item)
                self.ReviewSummary.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaOutputInfo(AbstractModel):
    """Information parameter of file output by video processing

    """

    def __init__(self):
        """
        :param Region: Region of the bucket where an output file is stored, such as ap-guangzhou.\n        :type Region: str\n        :param Bucket: Bucket of output file.\n        :type Bucket: str\n        :param Dir: Path to output file, which must end in "/".\n        :type Dir: str\n        """
        self.Region = None
        self.Bucket = None
        self.Dir = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.Dir = params.get("Dir")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskAdaptiveDynamicStreamingResult(AbstractModel):
    """Result type of adaptive bitrate streaming task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param Input: Input of adaptive bitrate streaming task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AdaptiveDynamicStreamingTaskInput`\n        :param Output: Output of adaptive bitrate streaming task.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.AdaptiveDynamicStreamingInfoItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AdaptiveDynamicStreamingTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AdaptiveDynamicStreamingInfoItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskAnimatedGraphicResult(AbstractModel):
    """Result type of animated image generating task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of animated image generating task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.AnimatedGraphicTaskInput`\n        :param Output: Output of animated image generating task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaAnimatedGraphicsItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AnimatedGraphicTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaAnimatedGraphicsItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskCoverBySnapshotResult(AbstractModel):
    """Result type of cover generating task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of cover generating task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.CoverBySnapshotTaskInput`\n        :param Output: Output of cover generating task.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.CoverBySnapshotTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = CoverBySnapshotTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = CoverBySnapshotTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskImageSpriteResult(AbstractModel):
    """Result type of image sprite generating task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of image sprite generating task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.ImageSpriteTaskInput`\n        :param Output: Output of image sprite generating task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaImageSpriteItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = ImageSpriteTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaImageSpriteItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskInput(AbstractModel):
    """Video processing task type

    """

    def __init__(self):
        """
        :param TranscodeTaskSet: List of transcoding tasks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TranscodeTaskSet: list of TranscodeTaskInput\n        :param AnimatedGraphicTaskSet: List of animated image generating tasks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AnimatedGraphicTaskSet: list of AnimatedGraphicTaskInput\n        :param SnapshotByTimeOffsetTaskSet: List of time point screencapturing tasks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SnapshotByTimeOffsetTaskSet: list of SnapshotByTimeOffsetTaskInput\n        :param SampleSnapshotTaskSet: List of sampled screencapturing tasks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SampleSnapshotTaskSet: list of SampleSnapshotTaskInput\n        :param ImageSpriteTaskSet: List of image sprite generating tasks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageSpriteTaskSet: list of ImageSpriteTaskInput\n        :param CoverBySnapshotTaskSet: List of cover generating tasks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CoverBySnapshotTaskSet: list of CoverBySnapshotTaskInput\n        :param AdaptiveDynamicStreamingTaskSet: List of adaptive bitrate streaming tasks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AdaptiveDynamicStreamingTaskSet: list of AdaptiveDynamicStreamingTaskInput\n        """
        self.TranscodeTaskSet = None
        self.AnimatedGraphicTaskSet = None
        self.SnapshotByTimeOffsetTaskSet = None
        self.SampleSnapshotTaskSet = None
        self.ImageSpriteTaskSet = None
        self.CoverBySnapshotTaskSet = None
        self.AdaptiveDynamicStreamingTaskSet = None


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self.TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskInput()
                obj._deserialize(item)
                self.TranscodeTaskSet.append(obj)
        if params.get("AnimatedGraphicTaskSet") is not None:
            self.AnimatedGraphicTaskSet = []
            for item in params.get("AnimatedGraphicTaskSet"):
                obj = AnimatedGraphicTaskInput()
                obj._deserialize(item)
                self.AnimatedGraphicTaskSet.append(obj)
        if params.get("SnapshotByTimeOffsetTaskSet") is not None:
            self.SnapshotByTimeOffsetTaskSet = []
            for item in params.get("SnapshotByTimeOffsetTaskSet"):
                obj = SnapshotByTimeOffsetTaskInput()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTaskSet.append(obj)
        if params.get("SampleSnapshotTaskSet") is not None:
            self.SampleSnapshotTaskSet = []
            for item in params.get("SampleSnapshotTaskSet"):
                obj = SampleSnapshotTaskInput()
                obj._deserialize(item)
                self.SampleSnapshotTaskSet.append(obj)
        if params.get("ImageSpriteTaskSet") is not None:
            self.ImageSpriteTaskSet = []
            for item in params.get("ImageSpriteTaskSet"):
                obj = ImageSpriteTaskInput()
                obj._deserialize(item)
                self.ImageSpriteTaskSet.append(obj)
        if params.get("CoverBySnapshotTaskSet") is not None:
            self.CoverBySnapshotTaskSet = []
            for item in params.get("CoverBySnapshotTaskSet"):
                obj = CoverBySnapshotTaskInput()
                obj._deserialize(item)
                self.CoverBySnapshotTaskSet.append(obj)
        if params.get("AdaptiveDynamicStreamingTaskSet") is not None:
            self.AdaptiveDynamicStreamingTaskSet = []
            for item in params.get("AdaptiveDynamicStreamingTaskSet"):
                obj = AdaptiveDynamicStreamingTaskInput()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTaskSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskResult(AbstractModel):
    """Query result type of task

    """

    def __init__(self):
        """
        :param Type: Task type. Valid values:
<li>Transcode: transcoding</li>
<li>AnimatedGraphics: animated image generating</li>
<li>SnapshotByTimeOffset: time point screencapturing</li>
<li>SampleSnapshot: sampled screencapturing</li>
<li>ImageSprites: image sprite generating</li>
<li>CoverBySnapshot: Screencapturing for cover image</li>
<li>AdaptiveDynamicStreaming: adaptive bitrate streaming</li>\n        :type Type: str\n        :param TranscodeTask: Query result of transcoding task, which is valid when task type is `Transcode`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TranscodeTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskTranscodeResult`\n        :param AnimatedGraphicTask: Query result of animated image generating task, which is valid when task type is `AnimatedGraphics`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AnimatedGraphicTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskAnimatedGraphicResult`\n        :param SnapshotByTimeOffsetTask: Query result of time point screencapturing task, which is valid when task type is `SnapshotByTimeOffset`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SnapshotByTimeOffsetTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskSnapshotByTimeOffsetResult`\n        :param SampleSnapshotTask: Query result of sampled screencapturing task, which is valid when task type is `SampleSnapshot`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SampleSnapshotTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskSampleSnapshotResult`\n        :param ImageSpriteTask: Query result of image sprite generating task, which is valid when task type is `ImageSprite`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageSpriteTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskImageSpriteResult`\n        :param CoverBySnapshotTask: Query result of cover generating task, which is valid if task type is `CoverBySnapshot`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CoverBySnapshotTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskCoverBySnapshotResult`\n        :param AdaptiveDynamicStreamingTask: Query result of adaptive bitrate streaming, which is valid if task type is `AdaptiveDynamicStreaming`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AdaptiveDynamicStreamingTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskAdaptiveDynamicStreamingResult`\n        """
        self.Type = None
        self.TranscodeTask = None
        self.AnimatedGraphicTask = None
        self.SnapshotByTimeOffsetTask = None
        self.SampleSnapshotTask = None
        self.ImageSpriteTask = None
        self.CoverBySnapshotTask = None
        self.AdaptiveDynamicStreamingTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = MediaProcessTaskTranscodeResult()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("AnimatedGraphicTask") is not None:
            self.AnimatedGraphicTask = MediaProcessTaskAnimatedGraphicResult()
            self.AnimatedGraphicTask._deserialize(params.get("AnimatedGraphicTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = MediaProcessTaskSnapshotByTimeOffsetResult()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        if params.get("SampleSnapshotTask") is not None:
            self.SampleSnapshotTask = MediaProcessTaskSampleSnapshotResult()
            self.SampleSnapshotTask._deserialize(params.get("SampleSnapshotTask"))
        if params.get("ImageSpriteTask") is not None:
            self.ImageSpriteTask = MediaProcessTaskImageSpriteResult()
            self.ImageSpriteTask._deserialize(params.get("ImageSpriteTask"))
        if params.get("CoverBySnapshotTask") is not None:
            self.CoverBySnapshotTask = MediaProcessTaskCoverBySnapshotResult()
            self.CoverBySnapshotTask._deserialize(params.get("CoverBySnapshotTask"))
        if params.get("AdaptiveDynamicStreamingTask") is not None:
            self.AdaptiveDynamicStreamingTask = MediaProcessTaskAdaptiveDynamicStreamingResult()
            self.AdaptiveDynamicStreamingTask._deserialize(params.get("AdaptiveDynamicStreamingTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskSampleSnapshotResult(AbstractModel):
    """Result type of sampled screencapturing task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of sampled screencapturing task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.SampleSnapshotTaskInput`\n        :param Output: Output of sampled screencapturing task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaSampleSnapshotItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SampleSnapshotTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSampleSnapshotItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskSnapshotByTimeOffsetResult(AbstractModel):
    """Result type of time point screencapturing task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of time point screencapturing task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.SnapshotByTimeOffsetTaskInput`\n        :param Output: Output of time point screencapturing task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaSnapshotByTimeOffsetItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SnapshotByTimeOffsetTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSnapshotByTimeOffsetItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskTranscodeResult(AbstractModel):
    """Result type of transcoding task

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: PROCESSING, SUCCESS, FAIL.\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You’re not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param Input: Input of transcoding task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.TranscodeTaskInput`\n        :param Output: Output of transcoding task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaTranscodeItem`\n        :param Progress: Transcoding progress. Value range: 0-100.\n        :type Progress: int\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None
        self.Progress = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = TranscodeTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaTranscodeItem()
            self.Output._deserialize(params.get("Output"))
        self.Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSampleSnapshotInfo(AbstractModel):
    """Information of sampled screenshot of VOD file

    """

    def __init__(self):
        """
        :param SampleSnapshotSet: Information set of sampled screenshots with the specified specifications. Each element represents a set of sampled screenshots with the same specification.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SampleSnapshotSet: list of MediaSampleSnapshotItem\n        """
        self.SampleSnapshotSet = None


    def _deserialize(self, params):
        if params.get("SampleSnapshotSet") is not None:
            self.SampleSnapshotSet = []
            for item in params.get("SampleSnapshotSet"):
                obj = MediaSampleSnapshotItem()
                obj._deserialize(item)
                self.SampleSnapshotSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSampleSnapshotItem(AbstractModel):
    """Sampled screenshot information

    """

    def __init__(self):
        """
        :param Definition: Sampled screenshot specification ID. For more information, please see [Sampled Screencapturing Parameter Template](https://intl.cloud.tencent.com/document/product/266/33480?from_cn_redirect=1#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Definition: int\n        :param SampleType: Sample type. Valid values:
<li>Percent: samples at a specified percentage interval.</li>
<li>Time: samples at a specified time interval.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SampleType: str\n        :param Interval: Sampling interval
<li>If `SampleType` is `Percent`, this value means taking a screenshot at an interval of the specified percentage.</li>
<li>If `SampleType` is `Time`, this value means taking a screenshot at an interval of the specified time (in seconds). The first screenshot is always the first video frame.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Interval: int\n        :param ImageUrlSet: List of URLs of generated screenshots.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageUrlSet: list of str\n        :param WaterMarkDefinition: List of watermarking template IDs if the screenshots are watermarked.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WaterMarkDefinition: list of int\n        """
        self.Definition = None
        self.SampleType = None
        self.Interval = None
        self.ImageUrlSet = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SampleType = params.get("SampleType")
        self.Interval = params.get("Interval")
        self.ImageUrlSet = params.get("ImageUrlSet")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSnapshotByTimeOffsetInfo(AbstractModel):
    """Information of time point screenshot in VOD file

    """

    def __init__(self):
        """
        :param SnapshotByTimeOffsetSet: Information set of time point screenshots with a specified specification. Currently, there can be only one set of screenshots for each specification.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SnapshotByTimeOffsetSet: list of MediaSnapshotByTimeOffsetItem\n        """
        self.SnapshotByTimeOffsetSet = None


    def _deserialize(self, params):
        if params.get("SnapshotByTimeOffsetSet") is not None:
            self.SnapshotByTimeOffsetSet = []
            for item in params.get("SnapshotByTimeOffsetSet"):
                obj = MediaSnapshotByTimeOffsetItem()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSnapshotByTimeOffsetItem(AbstractModel):
    """Information of time point screenshot in VOD file

    """

    def __init__(self):
        """
        :param Definition: Specification of a time point screenshot. For more information, please see [Parameter Template for Time Point Screencapturing](https://intl.cloud.tencent.com/document/product/266/33480?from_cn_redirect=1#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Definition: int\n        :param PicInfoSet: Information set of screenshots of the same specification. Each element represents a screenshot.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PicInfoSet: list of MediaSnapshotByTimePicInfoItem\n        """
        self.Definition = None
        self.PicInfoSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("PicInfoSet") is not None:
            self.PicInfoSet = []
            for item in params.get("PicInfoSet"):
                obj = MediaSnapshotByTimePicInfoItem()
                obj._deserialize(item)
                self.PicInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSnapshotByTimePicInfoItem(AbstractModel):
    """Time point screenshot information

    """

    def __init__(self):
        """
        :param TimeOffset: Time offset corresponding to the screenshot in the video in <font color=red>milliseconds</font>.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TimeOffset: float\n        :param Url: Screenshot URL.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Url: str\n        :param WaterMarkDefinition: List of watermarking template IDs if the screenshots are watermarked.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WaterMarkDefinition: list of int\n        """
        self.TimeOffset = None
        self.Url = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Url = params.get("Url")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSourceData(AbstractModel):
    """Source file information

    """

    def __init__(self):
        """
        :param SourceType: Source category of media file:
<li>Record: recording, such as LVB recording and LVB time shifting recording.</li>
<li>Upload: upload, such as pull for upload, upload from server, and UCG upload from client.</li>
<li>VideoProcessing: video processing, such as video splicing and video clipping.</li>
<li>Unknown: unknown source.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SourceType: str\n        :param SourceContext: Field passed through when a file is created.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SourceContext: str\n        """
        self.SourceType = None
        self.SourceContext = None


    def _deserialize(self, params):
        self.SourceType = params.get("SourceType")
        self.SourceContext = params.get("SourceContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSubtitleInfo(AbstractModel):
    """Subtitle information

    """

    def __init__(self):
        """
        :param SubtitleSet: Subtitle information list\n        :type SubtitleSet: list of MediaSubtitleItem\n        """
        self.SubtitleSet = None


    def _deserialize(self, params):
        if params.get("SubtitleSet") is not None:
            self.SubtitleSet = []
            for item in params.get("SubtitleSet"):
                obj = MediaSubtitleItem()
                obj._deserialize(item)
                self.SubtitleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSubtitleInput(AbstractModel):
    """Input parameters of subtile information

    """

    def __init__(self):
        """
        :param Name: Subtitle name. Length limit: 64 characters\n        :type Name: str\n        :param Language: Subtitle language. Common values:
<li>`cn`: Chinese</li>
<li>`ja`: Japanese</li>
<li>`en-US`: English</li>
For other valid values, see [RFC 5646](https://tools.ietf.org/html/rfc5646).\n        :type Language: str\n        :param Format: Subtitle format. Valid value:
<li>vtt</li>\n        :type Format: str\n        :param Content: Subtitle content, which is [Base64-encoded](https://tools.ietf.org/html/rfc4648) strings\n        :type Content: str\n        :param Id: Subtitle ID. Its length cannot exceed 16 characters. Uppercase and lowercase letters, numbers, underscores (_), and hyphens (-) are supported. It cannot be the same as the IDs of the existing subtitles in the media file.\n        :type Id: str\n        """
        self.Name = None
        self.Language = None
        self.Format = None
        self.Content = None
        self.Id = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Language = params.get("Language")
        self.Format = params.get("Format")
        self.Content = params.get("Content")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSubtitleItem(AbstractModel):
    """Subtitle information

    """

    def __init__(self):
        """
        :param Id: Unique subtitle ID\n        :type Id: str\n        :param Name: Subtitle name\n        :type Name: str\n        :param Language: Subtitle language. Common values:
<li>`cn`: Chinese</li>
<li>`ja`: Japanese</li>
<li>`en-US`: English</li>
For other values, see [RFC 5646](https://tools.ietf.org/html/rfc5646).\n        :type Language: str\n        :param Format: Subtitle format. Valid value:
<li>vtt</li>\n        :type Format: str\n        :param Url: Subtitle URL\n        :type Url: str\n        """
        self.Id = None
        self.Name = None
        self.Language = None
        self.Format = None
        self.Url = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Language = params.get("Language")
        self.Format = params.get("Format")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTrack(AbstractModel):
    """Track information

    """

    def __init__(self):
        """
        :param Type: Track type. Valid values:
<ul>
<li>Video: video track, which is composed of the following items: <ul><li>VideoTrackItem</li><li>MediaTransitionItem</li> <li>EmptyTrackItem</li></ul> </li>
<li>Audio: audio track, which is composed of the following items: <ul><li>AudioTrackItem</li><li>MediaTransitionItem</li><li>EmptyTrackItem</li></ul></li>
<li>Sticker: sticker track, which is composed of the following items: <ul><li> StickerTrackItem</li><li>EmptyTrackItem</li></ul></li>	
</ul>\n        :type Type: str\n        :param TrackItems: List of media segments on track.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TrackItems: list of MediaTrackItem\n        """
        self.Type = None
        self.TrackItems = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TrackItems") is not None:
            self.TrackItems = []
            for item in params.get("TrackItems"):
                obj = MediaTrackItem()
                obj._deserialize(item)
                self.TrackItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTrackItem(AbstractModel):
    """Segment information of media track

    """

    def __init__(self):
        """
        :param Type: Segment type. Valid values:
<li>Video: video segment.</li>
<li>Audio: audio segment.</li>
<li>Sticker: sticker segment.</li>
<li>Transition: transition.</li>
<li>Empty: empty segment.</li>\n        :type Type: str\n        :param VideoItem: Video segment, which is valid if `Type` is `Video`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VideoItem: :class:`tencentcloud.vod.v20180717.models.VideoTrackItem`\n        :param AudioItem: Audio segment, which is valid if `Type` is `Audio`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioItem: :class:`tencentcloud.vod.v20180717.models.AudioTrackItem`\n        :param StickerItem: Sticker segment, which is valid if `Type` is `Sticker`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StickerItem: :class:`tencentcloud.vod.v20180717.models.StickerTrackItem`\n        :param TransitionItem: Transition, which is valid if `Type` is `Transition`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TransitionItem: :class:`tencentcloud.vod.v20180717.models.MediaTransitionItem`\n        :param EmptyItem: Empty segment, which is valid if `Type` is `Empty`. It is used as placeholder on time axis. <li>If you want a period of silence between two audio segments, you can use `EmptyTrackItem` to hold the place.</li>
<li>Use `EmptyTrackItem` as a placeholder to locate an item.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EmptyItem: :class:`tencentcloud.vod.v20180717.models.EmptyTrackItem`\n        """
        self.Type = None
        self.VideoItem = None
        self.AudioItem = None
        self.StickerItem = None
        self.TransitionItem = None
        self.EmptyItem = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("VideoItem") is not None:
            self.VideoItem = VideoTrackItem()
            self.VideoItem._deserialize(params.get("VideoItem"))
        if params.get("AudioItem") is not None:
            self.AudioItem = AudioTrackItem()
            self.AudioItem._deserialize(params.get("AudioItem"))
        if params.get("StickerItem") is not None:
            self.StickerItem = StickerTrackItem()
            self.StickerItem._deserialize(params.get("StickerItem"))
        if params.get("TransitionItem") is not None:
            self.TransitionItem = MediaTransitionItem()
            self.TransitionItem._deserialize(params.get("TransitionItem"))
        if params.get("EmptyItem") is not None:
            self.EmptyItem = EmptyTrackItem()
            self.EmptyItem._deserialize(params.get("EmptyItem"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTranscodeInfo(AbstractModel):
    """Transcoding information of VOD file

    """

    def __init__(self):
        """
        :param TranscodeSet: Information set of transcoding with each specification. Each element represents a result of transcoding with a specification.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TranscodeSet: list of MediaTranscodeItem\n        """
        self.TranscodeSet = None


    def _deserialize(self, params):
        if params.get("TranscodeSet") is not None:
            self.TranscodeSet = []
            for item in params.get("TranscodeSet"):
                obj = MediaTranscodeItem()
                obj._deserialize(item)
                self.TranscodeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTranscodeItem(AbstractModel):
    """Transcoding information

    """

    def __init__(self):
        """
        :param Url: Address of output video file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Url: str\n        :param Definition: Transcoding specification ID. For more information, please see [Transcoding Parameter Template](https://intl.cloud.tencent.com/document/product/266/33478?from_cn_redirect=1#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Definition: int\n        :param Bitrate: Sum of the average bitrate of a video stream and that of an audio stream in bps.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Bitrate: int\n        :param Height: Maximum value of the height of a video stream in px.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Height: int\n        :param Width: Maximum value of the width of a video stream in px.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Width: int\n        :param Size: Total size of a media file in bytes (which is the sum of size of m3u8 and ts files if the video is in HLS format).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Size: int\n        :param Duration: Video duration in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Duration: float\n        :param Container: Container, such as m4a and mp4.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Container: str\n        :param Md5: MD5 value of video.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Md5: str\n        :param AudioStreamSet: Audio stream information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioStreamSet: list of MediaAudioStreamItem\n        :param VideoStreamSet: Video stream information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VideoStreamSet: list of MediaVideoStreamItem\n        """
        self.Url = None
        self.Definition = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Size = None
        self.Duration = None
        self.Container = None
        self.Md5 = None
        self.AudioStreamSet = None
        self.VideoStreamSet = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Size = params.get("Size")
        self.Duration = params.get("Duration")
        self.Container = params.get("Container")
        self.Md5 = params.get("Md5")
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTransitionItem(AbstractModel):
    """Transition information

    """

    def __init__(self):
        """
        :param Duration: Transition duration in seconds. For two media segments that use a transition, the start time of the second segment on the track will be automatically set to the end time of the first segment minus the transition duration.\n        :type Duration: float\n        :param Transitions: List of transition operations. Up to one video image or audio transition operation is supported.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Transitions: list of TransitionOpertion\n        """
        self.Duration = None
        self.Transitions = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        if params.get("Transitions") is not None:
            self.Transitions = []
            for item in params.get("Transitions"):
                obj = TransitionOpertion()
                obj._deserialize(item)
                self.Transitions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaVideoStreamItem(AbstractModel):
    """Information of video stream in VOD file

    """

    def __init__(self):
        """
        :param Bitrate: Bitrate of video stream in bps.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Bitrate: int\n        :param Height: Height of video stream in px.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Height: int\n        :param Width: Width of video stream in px.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Width: int\n        :param Codec: Video stream encoder, such as h264.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Codec: str\n        :param Fps: Frame rate in Hz.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Fps: int\n        """
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Codec = None
        self.Fps = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIAnalysisTemplateRequest(AbstractModel):
    """ModifyAIAnalysisTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of video content analysis template.\n        :type Definition: int\n        :param Name: Video content analysis template name. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Video content analysis template description. Length limit: 256 characters.\n        :type Comment: str\n        :param ClassificationConfigure: Control parameter of intelligent categorization task.\n        :type ClassificationConfigure: :class:`tencentcloud.vod.v20180717.models.ClassificationConfigureInfoForUpdate`\n        :param TagConfigure: Control parameter of intelligent tagging task.\n        :type TagConfigure: :class:`tencentcloud.vod.v20180717.models.TagConfigureInfoForUpdate`\n        :param CoverConfigure: Control parameter of intelligent cover generating task.\n        :type CoverConfigure: :class:`tencentcloud.vod.v20180717.models.CoverConfigureInfoForUpdate`\n        :param FrameTagConfigure: Control parameter of intelligent frame-specific tagging task.\n        :type FrameTagConfigure: :class:`tencentcloud.vod.v20180717.models.FrameTagConfigureInfoForUpdate`\n        :param HighlightConfigure: Control parameter of an intelligent highlight generating task.\n        :type HighlightConfigure: :class:`tencentcloud.vod.v20180717.models.HighlightsConfigureInfoForUpdate`\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.HighlightConfigure = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfoForUpdate()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfoForUpdate()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfoForUpdate()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfoForUpdate()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        if params.get("HighlightConfigure") is not None:
            self.HighlightConfigure = HighlightsConfigureInfoForUpdate()
            self.HighlightConfigure._deserialize(params.get("HighlightConfigure"))
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIAnalysisTemplateResponse(AbstractModel):
    """ModifyAIAnalysisTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAIRecognitionTemplateRequest(AbstractModel):
    """ModifyAIRecognitionTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of video content recognition template.\n        :type Definition: int\n        :param Name: Video content recognition template name. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Description of video content recognition template. Length limit: 256 characters.\n        :type Comment: str\n        :param HeadTailConfigure: Control parameter of video opening and ending credits recognition.\n        :type HeadTailConfigure: :class:`tencentcloud.vod.v20180717.models.HeadTailConfigureInfoForUpdate`\n        :param SegmentConfigure: Control parameter of video splitting recognition.\n        :type SegmentConfigure: :class:`tencentcloud.vod.v20180717.models.SegmentConfigureInfoForUpdate`\n        :param FaceConfigure: Control parameter of face recognition.\n        :type FaceConfigure: :class:`tencentcloud.vod.v20180717.models.FaceConfigureInfoForUpdate`\n        :param OcrFullTextConfigure: Control parameter of full text recognition.\n        :type OcrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.OcrFullTextConfigureInfoForUpdate`\n        :param OcrWordsConfigure: Control parameter of text keyword recognition.\n        :type OcrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.OcrWordsConfigureInfoForUpdate`\n        :param AsrFullTextConfigure: Control parameter of full speech recognition.\n        :type AsrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.AsrFullTextConfigureInfoForUpdate`\n        :param AsrWordsConfigure: Control parameter of speech keyword recognition.\n        :type AsrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.AsrWordsConfigureInfoForUpdate`\n        :param ObjectConfigure: Control parameter of object recognition.\n        :type ObjectConfigure: :class:`tencentcloud.vod.v20180717.models.ObjectConfigureInfoForUpdate`\n        :param ScreenshotInterval: Frame capturing interval in seconds. Minimum value: 0.5 seconds.\n        :type ScreenshotInterval: float\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.HeadTailConfigure = None
        self.SegmentConfigure = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.ObjectConfigure = None
        self.ScreenshotInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("HeadTailConfigure") is not None:
            self.HeadTailConfigure = HeadTailConfigureInfoForUpdate()
            self.HeadTailConfigure._deserialize(params.get("HeadTailConfigure"))
        if params.get("SegmentConfigure") is not None:
            self.SegmentConfigure = SegmentConfigureInfoForUpdate()
            self.SegmentConfigure._deserialize(params.get("SegmentConfigure"))
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfoForUpdate()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfoForUpdate()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfoForUpdate()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfoForUpdate()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfoForUpdate()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        if params.get("ObjectConfigure") is not None:
            self.ObjectConfigure = ObjectConfigureInfoForUpdate()
            self.ObjectConfigure._deserialize(params.get("ObjectConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIRecognitionTemplateResponse(AbstractModel):
    """ModifyAIRecognitionTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """ModifyAdaptiveDynamicStreamingTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of adaptive bitrate streaming template.\n        :type Definition: int\n        :param Name: Template name. Length limit: 64 characters.\n        :type Name: str\n        :param Format: Adaptive bitstream format. Valid values:
<li>HLS.</li>\n        :type Format: str\n        :param DisableHigherVideoBitrate: Whether to prohibit transcoding video from low bitrate to high bitrate. Valid values:
<li>0: no,</li>
<li>1: yes.</li>\n        :type DisableHigherVideoBitrate: int\n        :param DisableHigherVideoResolution: Whether to prohibit transcoding from low resolution to high resolution. Valid values:
<li>0: no,</li>
<li>1: yes.</li>\n        :type DisableHigherVideoResolution: int\n        :param StreamInfos: Parameter information of input stream for adaptive bitrate streaming. Up to 10 streams can be input.
Note: the frame rate of all streams must be the same; otherwise, the frame rate of the first stream will be used as the output frame rate.\n        :type StreamInfos: list of AdaptiveStreamTemplate\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.Name = None
        self.Format = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.StreamInfos = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Format = params.get("Format")
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """ModifyAdaptiveDynamicStreamingTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAnimatedGraphicsTemplateRequest(AbstractModel):
    """ModifyAnimatedGraphicsTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an animated image generating template.\n        :type Definition: int\n        :param Name: Name of an animated image generating template. Length limit: 64 characters.\n        :type Name: str\n        :param Width: Maximum value of the width (or long side) of an animated image in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of an animated image in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param Format: Animated image format. Valid values: gif, webp.\n        :type Format: str\n        :param Fps: Video frame rate in Hz. Value range: [1, 30].\n        :type Fps: int\n        :param Quality: Image quality. Value range: [1, 100]. Default value: 75.\n        :type Quality: float\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAnimatedGraphicsTemplateResponse(AbstractModel):
    """ModifyAnimatedGraphicsTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClassRequest(AbstractModel):
    """ModifyClass request structure.

    """

    def __init__(self):
        """
        :param ClassId: Category ID\n        :type ClassId: int\n        :param ClassName: Category name, which can contain 1–64 characters.\n        :type ClassName: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.ClassId = None
        self.ClassName = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.ClassName = params.get("ClassName")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClassResponse(AbstractModel):
    """ModifyClass response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyContentReviewTemplateRequest(AbstractModel):
    """ModifyContentReviewTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an intelligent content recognition template.\n        :type Definition: int\n        :param Name: Name of an intelligent content recognition template. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Description of an intelligent content recognition template. Length limit: 256 characters.\n        :type Comment: str\n        :param TerrorismConfigure: Control parameter for terrorism information.\n        :type TerrorismConfigure: :class:`tencentcloud.vod.v20180717.models.TerrorismConfigureInfoForUpdate`\n        :param PornConfigure: Control parameter for porn information.\n        :type PornConfigure: :class:`tencentcloud.vod.v20180717.models.PornConfigureInfoForUpdate`\n        :param PoliticalConfigure: Control parameter for politically sensitive information.\n        :type PoliticalConfigure: :class:`tencentcloud.vod.v20180717.models.PoliticalConfigureInfoForUpdate`\n        :param ProhibitedConfigure: Control parameter of prohibited information detection. Prohibited information includes:
<li>Abusive;</li>
<li>Drug-related.</li>\n        :type ProhibitedConfigure: :class:`tencentcloud.vod.v20180717.models.ProhibitedConfigureInfoForUpdate`\n        :param UserDefineConfigure: Control parameter for custom intelligent content recognition tasks.\n        :type UserDefineConfigure: :class:`tencentcloud.vod.v20180717.models.UserDefineConfigureInfoForUpdate`\n        :param ScreenshotInterval: Frame capturing interval in seconds. Minimum value: 0.5 seconds.\n        :type ScreenshotInterval: float\n        :param ReviewWallSwitch: Whether to allow the recognition result to enter the intelligent recognition platform (for human recognition).
<li>ON: yes</li>
<li>OFF: no</li>\n        :type ReviewWallSwitch: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.TerrorismConfigure = None
        self.PornConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None
        self.ScreenshotInterval = None
        self.ReviewWallSwitch = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfoForUpdate()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfoForUpdate()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfoForUpdate()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfoForUpdate()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfoForUpdate()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.ReviewWallSwitch = params.get("ReviewWallSwitch")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyContentReviewTemplateResponse(AbstractModel):
    """ModifyContentReviewTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageSpriteTemplateRequest(AbstractModel):
    """ModifyImageSpriteTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of an image sprite generating template.\n        :type Definition: int\n        :param Name: Name of an image sprite generating template. Length limit: 64 characters.\n        :type Name: str\n        :param Width: Subimage width of an image sprite in px. Value range: [128, 4,096].\n        :type Width: int\n        :param Height: Subimage height of an image sprite in px. Value range: [128, 4,096].\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param SampleType: Sampling type. Valid values:
<li>Percent: by percent.</li>
<li>Time: by time interval.</li>\n        :type SampleType: str\n        :param SampleInterval: Sampling interval.
<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>
<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>\n        :type SampleInterval: int\n        :param RowCount: Subimage row count of an image sprite.\n        :type RowCount: int\n        :param ColumnCount: Subimage column count of an image sprite.\n        :type ColumnCount: int\n        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
Default value: black.\n        :type FillType: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.FillType = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageSpriteTemplateResponse(AbstractModel):
    """ModifyImageSpriteTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMediaInfoRequest(AbstractModel):
    """ModifyMediaInfo request structure.

    """

    def __init__(self):
        """
        :param FileId: Unique media file ID.\n        :type FileId: str\n        :param Name: Media filename, which can contain up to 64 characters.\n        :type Name: str\n        :param Description: Media file description, which can contain up to 128 characters.\n        :type Description: str\n        :param ClassId: Media file category ID.\n        :type ClassId: int\n        :param ExpireTime: Media file expiration time in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I). The value `9999-12-31T23:59:59Z` indicates that the media file never expires. After the expiration, the media file and its related resources (such as transcoding results and image sprites) will be permanently deleted.\n        :type ExpireTime: str\n        :param CoverData: String generated by [Base64-encoding](https://tools.ietf.org/html/rfc4648) the video cover image file (such as .jpeg or .png file). Only .gif, .jpeg, and .png image formats are supported.\n        :type CoverData: str\n        :param AddKeyFrameDescs: Set of video timestamps to be added. If a timestamp already exists at an offset time point, it will be overwritten. Up to 100 timestamps can be added to one media file. In the same request, the time offset parameters of `AddKeyFrameDescs` must be different from those of `DeleteKeyFrameDescs`.\n        :type AddKeyFrameDescs: list of MediaKeyFrameDescItem\n        :param DeleteKeyFrameDescs: Time offset of the set of video timestamps to be deleted in seconds. In the same request, the time offset parameters of `AddKeyFrameDescs` must be different from those of `DeleteKeyFrameDescs`.\n        :type DeleteKeyFrameDescs: list of float\n        :param ClearKeyFrameDescs: The value `1` indicates to delete all timestamps in the video. Other values are meaningless.
In the same request, `ClearKeyFrameDescs` and `AddKeyFrameDescs` cannot be present at the same time.\n        :type ClearKeyFrameDescs: int\n        :param AddTags: Set of tags to be added. Up to 16 tags can be added to one media file, and one tag can contain up to 16 characters. In the same request, the parameters of `AddTags` must be different from those of `DeleteTags`.\n        :type AddTags: list of str\n        :param DeleteTags: Set of tags to be deleted. In the same request, the parameters of `AddTags` must be different from those of `DeleteTags`.\n        :type DeleteTags: list of str\n        :param ClearTags: The value `1` indicates to delete all tags of the media file. Other values are meaningless.
In the same request, `ClearTags` and `AddTags` cannot be present at the same time.\n        :type ClearTags: int\n        :param AddSubtitles: Information of multiple subtitles to be added. A single media file can have up to 16 subtitles. In the same request, the subtitle IDs specified in `AddSubtitles` must be different from those in `DeleteSubtitleIds`.\n        :type AddSubtitles: list of MediaSubtitleInput\n        :param DeleteSubtitleIds: Unique IDs of the subtitles to be deleted. In the same request, the subtitle IDs specified in `AddSubtitles` must be different from those in `DeleteSubtitleIds`.\n        :type DeleteSubtitleIds: list of str\n        :param ClearSubtitles: The value `1` indicates to delete all subtitle information of the media file. Other values are meaningless.
`ClearSubtitles` and `AddSubtitles` cannot co-exist in the same request.\n        :type ClearSubtitles: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.FileId = None
        self.Name = None
        self.Description = None
        self.ClassId = None
        self.ExpireTime = None
        self.CoverData = None
        self.AddKeyFrameDescs = None
        self.DeleteKeyFrameDescs = None
        self.ClearKeyFrameDescs = None
        self.AddTags = None
        self.DeleteTags = None
        self.ClearTags = None
        self.AddSubtitles = None
        self.DeleteSubtitleIds = None
        self.ClearSubtitles = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")
        self.CoverData = params.get("CoverData")
        if params.get("AddKeyFrameDescs") is not None:
            self.AddKeyFrameDescs = []
            for item in params.get("AddKeyFrameDescs"):
                obj = MediaKeyFrameDescItem()
                obj._deserialize(item)
                self.AddKeyFrameDescs.append(obj)
        self.DeleteKeyFrameDescs = params.get("DeleteKeyFrameDescs")
        self.ClearKeyFrameDescs = params.get("ClearKeyFrameDescs")
        self.AddTags = params.get("AddTags")
        self.DeleteTags = params.get("DeleteTags")
        self.ClearTags = params.get("ClearTags")
        if params.get("AddSubtitles") is not None:
            self.AddSubtitles = []
            for item in params.get("AddSubtitles"):
                obj = MediaSubtitleInput()
                obj._deserialize(item)
                self.AddSubtitles.append(obj)
        self.DeleteSubtitleIds = params.get("DeleteSubtitleIds")
        self.ClearSubtitles = params.get("ClearSubtitles")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMediaInfoResponse(AbstractModel):
    """ModifyMediaInfo response structure.

    """

    def __init__(self):
        """
        :param CoverUrl: URL of new video cover.
* Note: this returned value is valid only if the request carries `CoverData`.*\n        :type CoverUrl: str\n        :param AddedSubtitleSet: Added subtitle information\n        :type AddedSubtitleSet: list of MediaSubtitleItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CoverUrl = None
        self.AddedSubtitleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
        if params.get("AddedSubtitleSet") is not None:
            self.AddedSubtitleSet = []
            for item in params.get("AddedSubtitleSet"):
                obj = MediaSubtitleItem()
                obj._deserialize(item)
                self.AddedSubtitleSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyPersonSampleRequest(AbstractModel):
    """ModifyPersonSample request structure.

    """

    def __init__(self):
        """
        :param PersonId: ID of a sample.\n        :type PersonId: str\n        :param Name: Name. Length limit: 128 characters.\n        :type Name: str\n        :param Description: Description. Length limit: 1,024 characters.\n        :type Description: str\n        :param Usages: Sample usage. Valid values:
1. Recognition: used for content recognition; equivalent to `Recognition.Face`
2. Review: used for inappropriate information recognition; equivalent to `Review.Face`
3. All: used for content recognition and inappropriate information recognition; equivalent to 1+2\n        :type Usages: list of str\n        :param FaceOperationInfo: Information of operations on facial features.\n        :type FaceOperationInfo: :class:`tencentcloud.vod.v20180717.models.AiSampleFaceOperation`\n        :param TagOperationInfo: Tag operation information.\n        :type TagOperationInfo: :class:`tencentcloud.vod.v20180717.models.AiSampleTagOperation`\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.Usages = None
        self.FaceOperationInfo = None
        self.TagOperationInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Usages = params.get("Usages")
        if params.get("FaceOperationInfo") is not None:
            self.FaceOperationInfo = AiSampleFaceOperation()
            self.FaceOperationInfo._deserialize(params.get("FaceOperationInfo"))
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonSampleResponse(AbstractModel):
    """ModifyPersonSample response structure.

    """

    def __init__(self):
        """
        :param Person: Information of a sample.\n        :type Person: :class:`tencentcloud.vod.v20180717.models.AiSamplePerson`\n        :param FailFaceInfoSet: Information of samples that failed the verification by facial feature positioning.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type FailFaceInfoSet: list of AiSampleFailFaceInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifySampleSnapshotTemplateRequest(AbstractModel):
    """ModifySampleSnapshotTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of a sampled screencapturing template.\n        :type Definition: int\n        :param Name: Name of a sampled screencapturing template. Length limit: 64 characters.\n        :type Name: str\n        :param Width: Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param SampleType: Sampled screencapturing type. Valid values:
<li>Percent: by percent.</li>
<li>Time: by time interval.</li>\n        :type SampleType: str\n        :param SampleInterval: Sampling interval.
<li>If `SampleType` is `Percent`, sampling will be performed at an interval of the specified percentage.</li>
<li>If `SampleType` is `Time`, sampling will be performed at the specified time interval in seconds.</li>\n        :type SampleInterval: int\n        :param Format: Image format. Valid values: jpg, png.\n        :type Format: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.\n        :type FillType: str\n        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.Format = None
        self.Comment = None
        self.SubAppId = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySampleSnapshotTemplateResponse(AbstractModel):
    """ModifySampleSnapshotTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of a specified time point screencapturing template.\n        :type Definition: int\n        :param Name: Name of a time point screencapturing template. Length limit: 64 characters.\n        :type Name: str\n        :param Width: Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param Format: Image format. Valid values: jpg, png.\n        :type Format: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: ID of a [subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.\n        :type FillType: str\n        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.SubAppId = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubAppIdInfoRequest(AbstractModel):
    """ModifySubAppIdInfo request structure.

    """

    def __init__(self):
        """
        :param SubAppId: Subapplication ID.\n        :type SubAppId: int\n        :param Name: Subapplication name. Length limit: 40 characters.\n        :type Name: str\n        :param Description: Subapplication overview. Length limit: 300 characters.\n        :type Description: str\n        """
        self.SubAppId = None
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubAppIdInfoResponse(AbstractModel):
    """ModifySubAppIdInfo response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubAppIdStatusRequest(AbstractModel):
    """ModifySubAppIdStatus request structure.

    """

    def __init__(self):
        """
        :param SubAppId: Subapplication ID.\n        :type SubAppId: int\n        :param Status: Subapplication status. Valid values:
<li>On: enabled</li>
<li>Off: disabled</li>
<li>Destroyed: terminated</li>
You cannot enable a subapplication whose status is “Destroying”. You can enable it after it was terminated.\n        :type Status: str\n        """
        self.SubAppId = None
        self.Status = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubAppIdStatusResponse(AbstractModel):
    """ModifySubAppIdStatus response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySuperPlayerConfigRequest(AbstractModel):
    """ModifySuperPlayerConfig request structure.

    """

    def __init__(self):
        """
        :param Name: Player configuration name.\n        :type Name: str\n        :param DrmSwitch: Switch of DRM-protected adaptive bitstream playback:
<li>ON: enabled, indicating to play back only output adaptive bitstreams protected by DRM;</li>
<li>OFF: disabled, indicating to play back unencrypted output adaptive bitstreams.</li>\n        :type DrmSwitch: str\n        :param AdaptiveDynamicStreamingDefinition: ID of the unencrypted adaptive bitrate streaming template that allows output.\n        :type AdaptiveDynamicStreamingDefinition: int\n        :param DrmStreamingsInfo: Content of the DRM-protected adaptive bitrate streaming template that allows output.\n        :type DrmStreamingsInfo: :class:`tencentcloud.vod.v20180717.models.DrmStreamingsInfoForUpdate`\n        :param ImageSpriteDefinition: ID of the image sprite generating template that allows output.\n        :type ImageSpriteDefinition: int\n        :param ResolutionNames: Display name of player for substreams with different resolutions.\n        :type ResolutionNames: list of ResolutionNameInfo\n        :param Domain: Domain name used for playback. If its value is `Default`, the domain name configured in [Default Distribution Configuration](https://intl.cloud.tencent.com/document/product/266/33373?from_cn_redirect=1) will be used.\n        :type Domain: str\n        :param Scheme: Scheme used for playback. Valid values:
<li>Default: the scheme configured in [Default Distribution Configuration](https://intl.cloud.tencent.com/document/product/266/33373?from_cn_redirect=1) will be used;</li>
<li>HTTP;</li>
<li>HTTPS.</li>\n        :type Scheme: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Name = None
        self.DrmSwitch = None
        self.AdaptiveDynamicStreamingDefinition = None
        self.DrmStreamingsInfo = None
        self.ImageSpriteDefinition = None
        self.ResolutionNames = None
        self.Domain = None
        self.Scheme = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DrmSwitch = params.get("DrmSwitch")
        self.AdaptiveDynamicStreamingDefinition = params.get("AdaptiveDynamicStreamingDefinition")
        if params.get("DrmStreamingsInfo") is not None:
            self.DrmStreamingsInfo = DrmStreamingsInfoForUpdate()
            self.DrmStreamingsInfo._deserialize(params.get("DrmStreamingsInfo"))
        self.ImageSpriteDefinition = params.get("ImageSpriteDefinition")
        if params.get("ResolutionNames") is not None:
            self.ResolutionNames = []
            for item in params.get("ResolutionNames"):
                obj = ResolutionNameInfo()
                obj._deserialize(item)
                self.ResolutionNames.append(obj)
        self.Domain = params.get("Domain")
        self.Scheme = params.get("Scheme")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySuperPlayerConfigResponse(AbstractModel):
    """ModifySuperPlayerConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTranscodeTemplateRequest(AbstractModel):
    """ModifyTranscodeTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of transcoding template.\n        :type Definition: int\n        :param Container: Container. Valid values: mp4; flv; hls; mp3; flac; ogg; m4a. Among them, mp3, flac, ogg, and m4a are for audio files.\n        :type Container: str\n        :param Name: Transcoding template name. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param RemoveVideo: Whether to remove video data. Valid values:
<li>0: retain</li>
<li>1: remove</li>\n        :type RemoveVideo: int\n        :param RemoveAudio: Whether to remove audio data. Valid values:
<li>0: retain</li>
<li>1: remove</li>\n        :type RemoveAudio: int\n        :param VideoTemplate: Video stream configuration parameter.\n        :type VideoTemplate: :class:`tencentcloud.vod.v20180717.models.VideoTemplateInfoForUpdate`\n        :param AudioTemplate: Audio stream configuration parameter.\n        :type AudioTemplate: :class:`tencentcloud.vod.v20180717.models.AudioTemplateInfoForUpdate`\n        :param TEHDConfig: TESHD transcoding parameter.\n        :type TEHDConfig: :class:`tencentcloud.vod.v20180717.models.TEHDConfigForUpdate`\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfoForUpdate()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfoForUpdate()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfigForUpdate()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTranscodeTemplateResponse(AbstractModel):
    """ModifyTranscodeTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWatermarkTemplateRequest(AbstractModel):
    """ModifyWatermarkTemplate request structure.

    """

    def __init__(self):
        """
        :param Definition: Unique ID of watermarking template.\n        :type Definition: int\n        :param Name: Watermarking template name. Length limit: 64 characters.\n        :type Name: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param CoordinateOrigin: Origin position. Valid values:
<li>TopLeft: the origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text;</li>
<li>TopRight: the origin of coordinates is in the top-right corner of the video, and the origin of the watermark is in the top-right corner of the image or text;</li>
<li>BottomLeft: the origin of coordinates is in the bottom-left corner of the video, and the origin of the watermark is in the bottom-left corner of the image or text;</li>
<li>BottomRight: the origin of coordinates is in the bottom-right corner of the video, and the origin of the watermark is in the bottom-right corner of the image or text.</li>\n        :type CoordinateOrigin: str\n        :param XPos: The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `XPos` of the watermark will be the specified percentage of the video width; for example, `10%` means that `XPos` is 10% of the video width;</li>
<li>If the string ends in px, the `XPos` of the watermark will be the specified px; for example, `100px` means that `XPos` is 100 px.</li>\n        :type XPos: str\n        :param YPos: The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `YPos` of the watermark will be the specified percentage of the video height; for example, `10%` means that `YPos` is 10% of the video height;</li>
<li>If the string ends in px, the `YPos` of the watermark will be the specified px; for example, `100px` means that `YPos` is 100 px.</li>\n        :type YPos: str\n        :param ImageTemplate: Image watermarking template. This field is valid only for image watermarking templates.\n        :type ImageTemplate: :class:`tencentcloud.vod.v20180717.models.ImageWatermarkInputForUpdate`\n        :param TextTemplate: Text watermarking template. This field is valid only for text watermarking templates.\n        :type TextTemplate: :class:`tencentcloud.vod.v20180717.models.TextWatermarkTemplateInputForUpdate`\n        :param SvgTemplate: SVG watermarking template. This field is only valid for SVG watermarking templates.\n        :type SvgTemplate: :class:`tencentcloud.vod.v20180717.models.SvgWatermarkInputForUpdate`\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInputForUpdate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInputForUpdate()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInputForUpdate()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWatermarkTemplateResponse(AbstractModel):
    """ModifyWatermarkTemplate response structure.

    """

    def __init__(self):
        """
        :param ImageUrl: Image watermark address. This field has a value only when `ImageTemplate.ImageContent` is not empty.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageUrl: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class ModifyWordSampleRequest(AbstractModel):
    """ModifyWordSample request structure.

    """

    def __init__(self):
        """
        :param Keyword: Keyword. Length limit: 128 characters.\n        :type Keyword: str\n        :param Usages: <b>Keyword usage. Valid values:</b>
1. Recognition.Ocr: OCR-based content recognition
2. Recognition.Asr: ASR-based content recognition
3. Review.Ocr: OCR-based inappropriate information recognition
4. Review.Asr: ASR-based inappropriate information recognition
<b>Valid values can also be:</b>
5. Recognition: ASR- and OCR-based content recognition; equivalent to 1+2
6. Review: ASR- and OCR-based inappropriate information recognition; equivalent to 3+4
7. All: equivalent to 1+2+3+4\n        :type Usages: list of str\n        :param TagOperationInfo: Tag operation information.\n        :type TagOperationInfo: :class:`tencentcloud.vod.v20180717.models.AiSampleTagOperation`\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Keyword = None
        self.Usages = None
        self.TagOperationInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Usages = params.get("Usages")
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWordSampleResponse(AbstractModel):
    """ModifyWordSample response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MosaicInput(AbstractModel):
    """Blur parameter type of video processing task

    """

    def __init__(self):
        """
        :param CoordinateOrigin: Origin position, which currently can only be:
<li>TopLeft: the origin of coordinates is in the top-left corner of the video, and the origin of the blur is in the top-left corner of the image or text.</li>
Default value: TopLeft.\n        :type CoordinateOrigin: str\n        :param XPos: The horizontal position of the origin of the blur relative to the origin of coordinates of the video. % and px formats are supported:
<li>If the string ends in %, the `XPos` of the blur will be the specified percentage of the video width; for example, `10%` means that `XPos` is 10% of the video width;</li>
<li>If the string ends in px, the `XPos` of the blur will be the specified px; for example, `100px` means that `XPos` is 100 px.</li>
Default value: 0 px.\n        :type XPos: str\n        :param YPos: Vertical position of the origin of blur relative to the origin of coordinates of video. % and px formats are supported:
<li>If the string ends in %, the `YPos` of the blur will be the specified percentage of the video height; for example, `10%` means that `YPos` is 10% of the video height;</li>
<li>If the string ends in px, the `YPos` of the blur will be the specified px; for example, `100px` means that `YPos` is 100 px.</li>
Default value: 0 px.\n        :type YPos: str\n        :param Width: Blur width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the blur will be the specified percentage of the video width; for example, `10%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in px, the `Width` of the blur will be in px; for example, `100px` means that `Width` is 100 px.</li>
Default value: 10%.\n        :type Width: str\n        :param Height: Blur height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the blur will be the specified percentage of the video height; for example, `10%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in px, the `Height` of the blur will be in px; for example, `100px` means that `Height` is 100 px.</li>
Default value: 10%.\n        :type Height: str\n        :param StartTimeOffset: Start time offset of blur in seconds. If this parameter is left empty or 0 is entered, the blur will appear upon the first video frame.
<li>If this parameter is left empty or 0 is entered, the blur will appear upon the first video frame;</li>
<li>If this value is greater than 0 (e.g., n), the blur will appear at second n after the first video frame;</li>
<li>If this value is smaller than 0 (e.g., -n), the blur will appear at second n before the last video frame.</li>\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of blur in seconds.
<li>If this parameter is left empty or 0 is entered, the blur will exist till the last video frame;</li>
<li>If this value is greater than 0 (e.g., n), the blur will exist till second n;</li>
<li>If this value is smaller than 0 (e.g., -n), the blur will exist till second n before the last video frame.</li>\n        :type EndTimeOffset: float\n        """
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectConfigureInfo(AbstractModel):
    """Control parameter of object recognition task

    """

    def __init__(self):
        """
        :param Switch: Switch of object recognition task. Valid values:
<li>ON: enables intelligent object recognition task;</li>
<li>OFF: disables intelligent object recognition task.</li>\n        :type Switch: str\n        :param ObjectLibrary: Object library. Valid values:
<li>Default: default object library;</li>
<li>UserDefine: custom object library.</li>
<li>All: both default and custom object libraries will be used.</li>
Default value: All, i.e., both default and custom object libraries will be used.\n        :type ObjectLibrary: str\n        """
        self.Switch = None
        self.ObjectLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ObjectLibrary = params.get("ObjectLibrary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectConfigureInfoForUpdate(AbstractModel):
    """Control parameter of object recognition task

    """

    def __init__(self):
        """
        :param Switch: Switch of object recognition task. Valid values:
<li>ON: enables intelligent object recognition task;</li>
<li>OFF: disables intelligent object recognition task.</li>\n        :type Switch: str\n        :param ObjectLibrary: Object library. Valid values:
<li>Default: default object library;</li>
<li>UserDefine: custom object library.</li>
<li>All: both default and custom object libraries will be used.</li>\n        :type ObjectLibrary: str\n        """
        self.Switch = None
        self.ObjectLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ObjectLibrary = params.get("ObjectLibrary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrFullTextConfigureInfo(AbstractModel):
    """Control parameter of full text recognition task

    """

    def __init__(self):
        """
        :param Switch: Switch of full text recognition task. Valid values:
<li>ON: enables intelligent full text recognition task;</li>
<li>OFF: disables intelligent full text recognition task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrFullTextConfigureInfoForUpdate(AbstractModel):
    """Control parameter of full text recognition task

    """

    def __init__(self):
        """
        :param Switch: Switch of full text recognition task. Valid values:
<li>ON: enables intelligent full text recognition task;</li>
<li>OFF: disables intelligent full text recognition task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrWordsConfigureInfo(AbstractModel):
    """Text keyword recognition control parameter.

    """

    def __init__(self):
        """
        :param Switch: Switch of text keyword recognition task. Valid values:
<li>ON: enables text keyword recognition task;</li>
<li>OFF: disables text keyword recognition task.</li>\n        :type Switch: str\n        :param LabelSet: Keyword filter tag, which specifies the keyword tag that needs to be returned. If this parameter is left empty, all results will be returned.
There can be up to 10 tags, each with a length limit of 16 characters.\n        :type LabelSet: list of str\n        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrWordsConfigureInfoForUpdate(AbstractModel):
    """Control parameter of text keyword recognition.

    """

    def __init__(self):
        """
        :param Switch: Switch of text keyword recognition task. Valid values:
<li>ON: enables text keyword recognition task;</li>
<li>OFF: disables text keyword recognition task.</li>\n        :type Switch: str\n        :param LabelSet: Keyword filter tag, which specifies the keyword tag that needs to be returned. If this parameter is left empty or a blank value is entered, all results will be returned.
There can be up to 10 tags, each with a length limit of 16 characters.\n        :type LabelSet: list of str\n        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputAudioStream(AbstractModel):
    """Information of output audio stream

    """

    def __init__(self):
        """
        :param Codec: Audio stream encoder. Valid values:
<li>libfdk_aac: suitable for mp4 files.</li>
Default value: libfdk_aac.\n        :type Codec: str\n        :param SampleRate: Audio stream sample rate. Valid values:
<li>16,000</li>
<li>32,000</li>
<li>44,100</li>
<li>48,000</li>
In Hz.
Default value: 16,000.\n        :type SampleRate: int\n        :param AudioChannel: Number of sound channels. Valid values:
<li>1: mono.</li>
<li>2: dual</li>
Default value: 2.\n        :type AudioChannel: int\n        """
        self.Codec = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputVideoStream(AbstractModel):
    """Information of output video stream

    """

    def __init__(self):
        """
        :param Codec: Video stream encoder. Valid values:
<li>libx264: H.264</li>
Default value: libx264.\n        :type Codec: str\n        :param Fps: Video frame rate in Hz. Value range: [0, 60].
Default value: 0, which means that the value is the same as the video frame rate of the first video segment in the first video track.\n        :type Fps: int\n        """
        self.Codec = None
        self.Fps = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseStreamingManifestRequest(AbstractModel):
    """ParseStreamingManifest request structure.

    """

    def __init__(self):
        """
        :param MediaManifestContent: Index file content to be parsed.\n        :type MediaManifestContent: str\n        :param ManifestType: Video index file format, which is `m3u8` by default.
<li>m3u8</li>
<li>mpd</li>\n        :type ManifestType: str\n        """
        self.MediaManifestContent = None
        self.ManifestType = None


    def _deserialize(self, params):
        self.MediaManifestContent = params.get("MediaManifestContent")
        self.ManifestType = params.get("ManifestType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseStreamingManifestResponse(AbstractModel):
    """ParseStreamingManifest response structure.

    """

    def __init__(self):
        """
        :param MediaSegmentSet: Segment file list.\n        :type MediaSegmentSet: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MediaSegmentSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MediaSegmentSet = params.get("MediaSegmentSet")
        self.RequestId = params.get("RequestId")


class PlayStatFileInfo(AbstractModel):
    """Information of a playback statistics file

    """

    def __init__(self):
        """
        :param Date: Date of playback statistics in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?lang=en&pg=).\n        :type Date: str\n        :param Url: URL of a playback statistics file, including the following contents:
<li> date: playback date</li>
<li> file_id: video file ID</li>
<li> ip_count: number of client IPs after deduplication</li>
<li> flux: playback traffic in bytes</li>
<li> play_times: total playback times</li>
<li> pc_play_times: playback times on PC clients</li>
<li> mobile_play_times: playback times on mobile clients</li>
<li> iphone_play_times: playback times on iPhone</li>
<li> android_play_times: playback times on Android</li>
<li> host_name: domain name</li>\n        :type Url: str\n        """
        self.Date = None
        self.Url = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerConfig(AbstractModel):
    """Player configuration details

    """

    def __init__(self):
        """
        :param Name: Player configuration name.\n        :type Name: str\n        :param Type: Player configuration type. Valid values:
<li>Preset: preset configuration;</li>
<li>Custom: custom configuration.</li>\n        :type Type: str\n        :param DrmSwitch: Switch of DRM-protected adaptive bitstream playback:
<li>ON: enabled, indicating to play back only output adaptive bitstreams protected by DRM;</li>
<li>OFF: disabled, indicating to play back unencrypted output adaptive bitstreams.</li>\n        :type DrmSwitch: str\n        :param AdaptiveDynamicStreamingDefinition: ID of the unencrypted adaptive bitrate streaming template that allows output.\n        :type AdaptiveDynamicStreamingDefinition: int\n        :param DrmStreamingsInfo: Content of the DRM-protected adaptive bitrate streaming template that allows output.\n        :type DrmStreamingsInfo: :class:`tencentcloud.vod.v20180717.models.DrmStreamingsInfo`\n        :param ImageSpriteDefinition: ID of the image sprite generating template that allows output.\n        :type ImageSpriteDefinition: int\n        :param ResolutionNameSet: Display name of player for substreams with different resolutions.\n        :type ResolutionNameSet: list of ResolutionNameInfo\n        :param CreateTime: Creation time of player configuration in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of player configuration in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).\n        :type UpdateTime: str\n        :param Domain: Domain name used for playback. If its value is `Default`, the domain name configured in [Default Distribution Configuration](https://intl.cloud.tencent.com/document/product/266/33373?from_cn_redirect=1) will be used.\n        :type Domain: str\n        :param Scheme: Scheme used for playback. Valid values:
<li>Default: the scheme configured in [Default Distribution Configuration](https://intl.cloud.tencent.com/document/product/266/33373?from_cn_redirect=1) will be used;</li>
<li>HTTP;</li>
<li>HTTPS.</li>\n        :type Scheme: str\n        :param Comment: Template description.\n        :type Comment: str\n        """
        self.Name = None
        self.Type = None
        self.DrmSwitch = None
        self.AdaptiveDynamicStreamingDefinition = None
        self.DrmStreamingsInfo = None
        self.ImageSpriteDefinition = None
        self.ResolutionNameSet = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Domain = None
        self.Scheme = None
        self.Comment = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.DrmSwitch = params.get("DrmSwitch")
        self.AdaptiveDynamicStreamingDefinition = params.get("AdaptiveDynamicStreamingDefinition")
        if params.get("DrmStreamingsInfo") is not None:
            self.DrmStreamingsInfo = DrmStreamingsInfo()
            self.DrmStreamingsInfo._deserialize(params.get("DrmStreamingsInfo"))
        self.ImageSpriteDefinition = params.get("ImageSpriteDefinition")
        if params.get("ResolutionNameSet") is not None:
            self.ResolutionNameSet = []
            for item in params.get("ResolutionNameSet"):
                obj = ResolutionNameInfo()
                obj._deserialize(item)
                self.ResolutionNameSet.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Domain = params.get("Domain")
        self.Scheme = params.get("Scheme")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalAsrReviewTemplateInfo(AbstractModel):
    """Control parameter of politically sensitive information detection in speech task

    """

    def __init__(self):
        """
        :param Switch: Switch of politically sensitive information detection in speech task. Valid values:
<li>ON: enables politically sensitive information detection in speech task;</li>
<li>OFF: disables politically sensitive information detection in speech task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalAsrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of politically sensitive information detection in speech task.

    """

    def __init__(self):
        """
        :param Switch: Switch of politically sensitive information detection in speech task. Valid values:
<li>ON: enables politically sensitive information detection in speech task;</li>
<li>OFF: disables politically sensitive information detection in speech task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalConfigureInfo(AbstractModel):
    """Control parameter of politically sensitive information detection task

    """

    def __init__(self):
        """
        :param ImgReviewInfo: Control parameter of politically sensitive information detection in video image.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalImgReviewTemplateInfo`\n        :param AsrReviewInfo: Control parameter of politically sensitive information detection in speech.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalAsrReviewTemplateInfo`\n        :param OcrReviewInfo: Control parameter of politically sensitive information detection in text.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalOcrReviewTemplateInfo`\n        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalConfigureInfoForUpdate(AbstractModel):
    """Control parameter of politically sensitive information detection task.

    """

    def __init__(self):
        """
        :param ImgReviewInfo: Control parameter of politically sensitive information detection in video image.\n        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalImgReviewTemplateInfoForUpdate`\n        :param AsrReviewInfo: Control parameter of politically sensitive information detection in speech.\n        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalAsrReviewTemplateInfoForUpdate`\n        :param OcrReviewInfo: Control parameter of politically sensitive information detection in text.\n        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalOcrReviewTemplateInfoForUpdate`\n        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalImgReviewTemplateInfo(AbstractModel):
    """Control parameter of politically sensitive information detection in video image task

    """

    def __init__(self):
        """
        :param Switch: Switch of politically sensitive information detection in video image task. Valid values:
<li>ON: enables politically sensitive information detection in video image task;</li>
<li>OFF: disables politically sensitive information detection in video image task.</li>\n        :type Switch: str\n        :param LabelSet: Filter tags for politically sensitive information detection of video images. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. Valid values:
<li>violation_photo: violating photo;</li>
<li>politician: political figure;</li>
<li>entertainment: entertainment celebrity;</li>
<li>sport: sports figure;</li>
<li>entrepreneur: business figure;</li>
<li>scholar: educator;</li>
<li>celebrity: well-known figure;</li>
<li>military: military figure.</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 97 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 95 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalImgReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of politically sensitive information detection in video image task.

    """

    def __init__(self):
        """
        :param Switch: Switch of politically sensitive information detection in video image task. Valid values:
<li>ON: enables politically sensitive information detection in video image task;</li>
<li>OFF: disables politically sensitive information detection in video image task.</li>\n        :type Switch: str\n        :param LabelSet: Filter tags for politically sensitive information detection of video images. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. Valid values:
<li>violation_photo: violating photo;</li>
<li>politician: political figure;</li>
<li>entertainment: entertainment celebrity;</li>
<li>sport: sports figure;</li>
<li>entrepreneur: business figure;</li>
<li>scholar: educator;</li>
<li>celebrity: well-known figure;</li>
<li>military: military figure.</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalOcrReviewTemplateInfo(AbstractModel):
    """Control parameter of politically sensitive information detection in text task

    """

    def __init__(self):
        """
        :param Switch: Switch of politically sensitive information detection in text task. Valid values:
<li>ON: enables politically sensitive information detection in text task;</li>
<li>OFF: disables politically sensitive information detection in text task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalOcrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of politically sensitive information detection in text task.

    """

    def __init__(self):
        """
        :param Switch: Switch of politically sensitive information detection in text task. Valid values:
<li>ON: enables politically sensitive information detection in text task;</li>
<li>OFF: disables politically sensitive information detection in text task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornAsrReviewTemplateInfo(AbstractModel):
    """Control parameter of porn information detection in speech task

    """

    def __init__(self):
        """
        :param Switch: Switch of porn information detection in speech task. Valid values:
<li>ON: enables porn information detection in speech task;</li>
<li>OFF: disables porn information detection in speech task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornAsrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of porn detection in speech task.

    """

    def __init__(self):
        """
        :param Switch: Switch of porn detection in speech task. Valid values:
<li>ON: enables porn detection in speech task;</li>
<li>OFF: disables porn detection in speech task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornConfigureInfo(AbstractModel):
    """Control parameter of porn information detection task

    """

    def __init__(self):
        """
        :param ImgReviewInfo: Control parameter of porn information detection in video image.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornImgReviewTemplateInfo`\n        :param AsrReviewInfo: Control parameter of porn information detection in speech.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornAsrReviewTemplateInfo`\n        :param OcrReviewInfo: Control parameter of porn information detection in text.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornOcrReviewTemplateInfo`\n        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornConfigureInfoForUpdate(AbstractModel):
    """Control parameter of porn detection task.

    """

    def __init__(self):
        """
        :param ImgReviewInfo: Control parameter of porn detection in video image.\n        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornImgReviewTemplateInfoForUpdate`\n        :param AsrReviewInfo: Control parameter of porn detection in speech.\n        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornAsrReviewTemplateInfoForUpdate`\n        :param OcrReviewInfo: Control parameter of porn detection in text.\n        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornOcrReviewTemplateInfoForUpdate`\n        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornImgReviewTemplateInfo(AbstractModel):
    """Control parameter of porn information detection in video image task

    """

    def __init__(self):
        """
        :param Switch: Switch of porn information detection in video image task. Valid values:
<li>ON: enables porn information detection in video image task;</li>
<li>OFF: disables porn information detection in video image task.</li>\n        :type Switch: str\n        :param LabelSet: Filter tag for porn information detection in video image. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. Valid values:
<li>porn: porn;</li>
<li>vulgar: vulgarity;</li>
<li>intimacy: intimacy;</li>
<li>sexy: sexiness.</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 90 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 0 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornImgReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of porn detection in video image task.

    """

    def __init__(self):
        """
        :param Switch: Switch of porn detection in video image task. Valid values:
<li>ON: enables porn detection in video image task;</li>
<li>OFF: disables porn detection in video image task.</li>\n        :type Switch: str\n        :param LabelSet: Filter tag for porn detection in video image. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. Valid values:
<li>porn: porn;</li>
<li>vulgar: vulgarity;</li>
<li>intimacy: intimacy;</li>
<li>sexy: sexiness.</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornOcrReviewTemplateInfo(AbstractModel):
    """Control parameter of porn information detection in text task

    """

    def __init__(self):
        """
        :param Switch: Switch of porn information detection in text task. Valid values:
<li>ON: enables porn information detection in text task;</li>
<li>OFF: disables porn information detection in text task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornOcrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of porn detection in text task.

    """

    def __init__(self):
        """
        :param Switch: Switch of porn detection in text task. Valid values:
<li>ON: enables porn detection in text task;</li>
<li>OFF: disables porn detection in text task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcedureTask(AbstractModel):
    """Video processing task information

    """

    def __init__(self):
        """
        :param TaskId: Video processing task ID.\n        :type TaskId: str\n        :param Status: Task flow status. Valid values:
<li>PROCESSING: processing;</li>
<li>FINISH: completed.</li>\n        :type Status: str\n        :param ErrCode: Disused. Please use `ErrCode` of each specific task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ErrCode: int\n        :param Message: Disused. Please use `Message` of each specific task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param FileId: Media file ID.
<li>If the task flow is initiated by [ProcessMedia](https://cloud.tencent.com/document/product/266/33427), this field means the `FileId` in [MediaInfo](https://cloud.tencent.com/document/product/266/31773#MediaInfo);</li>
<li>If the task flow is initiated by [ProcessMediaByUrl](https://cloud.tencent.com/document/product/266/33426), this field means the `Id` in [MediaInputInfo](https://cloud.tencent.com/document/product/266/31773#MediaInputInfo).</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: str\n        :param FileName: Media filename
<li>If the task flow is initiated by [ProcessMedia](https://cloud.tencent.com/document/product/266/33427), this field means the `BasicInfo.Name` in [MediaInfo](https://cloud.tencent.com/document/product/266/31773#MediaInfo);</li>
<li>If the task flow is initiated by [ProcessMediaByUrl](https://cloud.tencent.com/document/product/266/33426), this field means the `Name` in [MediaInputInfo](https://cloud.tencent.com/document/product/266/31773#MediaInputInfo).</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileName: str\n        :param FileUrl: Media file address
<li>If the task flow is initiated by [ProcessMedia](https://cloud.tencent.com/document/product/266/33427), this field means the `BasicInfo.MediaUrl` in [MediaInfo](https://cloud.tencent.com/document/product/266/31773#MediaInfo);</li>
<li>If the task flow is initiated by [ProcessMediaByUrl](https://cloud.tencent.com/document/product/266/33426), this field means the `Url` in [MediaInputInfo](https://cloud.tencent.com/document/product/266/31773#MediaInputInfo).</li>\n        :type FileUrl: str\n        :param MetaData: Source video metadata.\n        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`\n        :param MediaProcessResultSet: Execution status and result of video processing task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MediaProcessResultSet: list of MediaProcessTaskResult\n        :param AiContentReviewResultSet: Execution status and result of video content audit task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AiContentReviewResultSet: list of AiContentReviewResult\n        :param AiAnalysisResultSet: Execution status and result of video content analysis task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AiAnalysisResultSet: list of AiAnalysisResult\n        :param AiRecognitionResultSet: Execution status and result of video content recognition task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AiRecognitionResultSet: list of AiRecognitionResult\n        :param TasksPriority: Task flow priority. Value range: [-10, 10].
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TasksPriority: int\n        :param TasksNotifyMode: Notification mode for change in task flow status.
<li>Finish: an event notification will be initiated only after the task flow is completely executed;</li>
<li>Change: an event notification will be initiated as soon as the status of a subtask in the task flow changes; </li>
<li>None: no callback for the task flow will be accepted.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TasksNotifyMode: str\n        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SessionContext: str\n        :param SessionId: The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SessionId: str\n        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileName = None
        self.FileUrl = None
        self.MetaData = None
        self.MediaProcessResultSet = None
        self.AiContentReviewResultSet = None
        self.AiAnalysisResultSet = None
        self.AiRecognitionResultSet = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.FileUrl = params.get("FileUrl")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("MediaProcessResultSet") is not None:
            self.MediaProcessResultSet = []
            for item in params.get("MediaProcessResultSet"):
                obj = MediaProcessTaskResult()
                obj._deserialize(item)
                self.MediaProcessResultSet.append(obj)
        if params.get("AiContentReviewResultSet") is not None:
            self.AiContentReviewResultSet = []
            for item in params.get("AiContentReviewResultSet"):
                obj = AiContentReviewResult()
                obj._deserialize(item)
                self.AiContentReviewResultSet.append(obj)
        if params.get("AiAnalysisResultSet") is not None:
            self.AiAnalysisResultSet = []
            for item in params.get("AiAnalysisResultSet"):
                obj = AiAnalysisResult()
                obj._deserialize(item)
                self.AiAnalysisResultSet.append(obj)
        if params.get("AiRecognitionResultSet") is not None:
            self.AiRecognitionResultSet = []
            for item in params.get("AiRecognitionResultSet"):
                obj = AiRecognitionResult()
                obj._deserialize(item)
                self.AiRecognitionResultSet.append(obj)
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcedureTemplate(AbstractModel):
    """Task flow template details

    """

    def __init__(self):
        """
        :param Name: Task flow name.\n        :type Name: str\n        :param Type: Type of a task flow template. Valid values:
<li>Preset: preset task flow template;</li>
<li>Custom: custom task flow template.</li>\n        :type Type: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param MediaProcessTask: Parameter of video processing task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MediaProcessTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskInput`\n        :param AiContentReviewTask: Parameter of AI-based content audit task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`\n        :param AiAnalysisTask: Parameter of AI-based content analysis task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`\n        :param AiRecognitionTask: Type parameter of AI-based content recognition task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`\n        :param MiniProgramPublishTask: Parameter of a release on WeChat Mini Program task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MiniProgramPublishTask: :class:`tencentcloud.vod.v20180717.models.WechatMiniProgramPublishTaskInput`\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        """
        self.Name = None
        self.Type = None
        self.Comment = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.MiniProgramPublishTask = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("MiniProgramPublishTask") is not None:
            self.MiniProgramPublishTask = WechatMiniProgramPublishTaskInput()
            self.MiniProgramPublishTask._deserialize(params.get("MiniProgramPublishTask"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessMediaByProcedureRequest(AbstractModel):
    """ProcessMediaByProcedure request structure.

    """

    def __init__(self):
        """
        :param FileId: Media file ID.\n        :type FileId: str\n        :param ProcedureName: [Task flow template](https://intl.cloud.tencent.com/document/product/266/11700?from_cn_redirect=1#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF) name.\n        :type ProcedureName: str\n        :param TasksPriority: Task flow priority. The higher the value, the higher the priority. Value range: -10-10. If this parameter is left empty, 0 will be used.\n        :type TasksPriority: int\n        :param TasksNotifyMode: Notification mode for task flow status change. Valid values: Finish, Change, None. If this parameter is left empty, `Finish` will be used.\n        :type TasksNotifyMode: str\n        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.\n        :type SessionContext: str\n        :param SessionId: Used to identify duplicate requests. After you send a request, if any request with the same `SessionId` has already been sent in the last three days (72 hours), an error message will be returned. `SessionId` contains up to 50 characters. If this parameter is not carried or is an empty string, no deduplication will be performed.\n        :type SessionId: str\n        :param ExtInfo: Reserved field for special purposes.\n        :type ExtInfo: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.FileId = None
        self.ProcedureName = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.ProcedureName = params.get("ProcedureName")
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessMediaByProcedureResponse(AbstractModel):
    """ProcessMediaByProcedure response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProcessMediaByUrlRequest(AbstractModel):
    """ProcessMediaByUrl request structure.

    """

    def __init__(self):
        """
        :param InputInfo: This API is<font color='red'>disused</font>. You are advised to use an alternative API. For more information, see API overview.\n        :type InputInfo: :class:`tencentcloud.vod.v20180717.models.MediaInputInfo`\n        :param OutputInfo: Information of COS path to output file.\n        :type OutputInfo: :class:`tencentcloud.vod.v20180717.models.MediaOutputInfo`\n        :param AiContentReviewTask: Type parameter of video content audit task.\n        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`\n        :param AiAnalysisTask: Video content analysis task parameter.\n        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`\n        :param AiRecognitionTask: Type parameter of video content recognition task.\n        :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`\n        :param TasksPriority: Task flow priority. The higher the value, the higher the priority. Value range: -10-10. If this parameter is left empty, 0 will be used.\n        :type TasksPriority: int\n        :param TasksNotifyMode: Notification mode for task flow status change. Valid values: Finish, Change, None. If this parameter is left empty, `Finish` will be used.\n        :type TasksNotifyMode: str\n        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.\n        :type SessionContext: str\n        :param SessionId: Used to identify duplicate requests. After you send a request, if any request with the same `SessionId` has already been sent in the last three days (72 hours), an error message will be returned. `SessionId` contains up to 50 characters. If this parameter is not carried or is an empty string, no deduplication will be performed.\n        :type SessionId: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.InputInfo = None
        self.OutputInfo = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None
        self.SubAppId = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("OutputInfo") is not None:
            self.OutputInfo = MediaOutputInfo()
            self.OutputInfo._deserialize(params.get("OutputInfo"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessMediaByUrlResponse(AbstractModel):
    """ProcessMediaByUrl response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProcessMediaRequest(AbstractModel):
    """ProcessMedia request structure.

    """

    def __init__(self):
        """
        :param FileId: Media file ID, i.e., the globally unique ID of a file in VOD assigned by the VOD backend after successful upload. This field can be obtained through the [video upload completion event notification](https://intl.cloud.tencent.com/document/product/266/7830?from_cn_redirect=1) or [VOD Console](https://console.cloud.tencent.com/vod/media).\n        :type FileId: str\n        :param MediaProcessTask: Parameter of video processing task.\n        :type MediaProcessTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskInput`\n        :param AiContentReviewTask: Type parameter of video content audit task.\n        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`\n        :param AiAnalysisTask: Video content analysis task parameter.\n        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`\n        :param AiRecognitionTask: Type parameter of video content recognition task.\n        :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`\n        :param TasksPriority: Task flow priority. The higher the value, the higher the priority. Value range: -10-10. If this parameter is left empty, 0 will be used.\n        :type TasksPriority: int\n        :param TasksNotifyMode: Notification mode for task flow status change. Valid values: Finish, Change, None. If this parameter is left empty, `Finish` will be used.\n        :type TasksNotifyMode: str\n        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.\n        :type SessionContext: str\n        :param SessionId: Used to identify duplicate requests. After you send a request, if any request with the same `SessionId` has already been sent in the last three days (72 hours), an error message will be returned. `SessionId` contains up to 50 characters. If this parameter is not carried or is an empty string, no deduplication will be performed.\n        :type SessionId: str\n        :param ExtInfo: Reserved field for special purposes.\n        :type ExtInfo: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.FileId = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessMediaResponse(AbstractModel):
    """ProcessMedia response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProhibitedAsrReviewTemplateInfo(AbstractModel):
    """Control parameter of prohibited information detection in speech task

    """

    def __init__(self):
        """
        :param Switch: Switch of prohibited information detection in speech task. Valid values:
<li>ON: enables prohibited information detection in speech task;</li>
<li>OFF: disables prohibited information detection in speech task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedAsrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of prohibited information detection in speech task

    """

    def __init__(self):
        """
        :param Switch: Switch of prohibited information detection in speech task. Valid values:
<li>ON: enables prohibited information detection in speech task;</li>
<li>OFF: disables prohibited information detection in speech task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedConfigureInfo(AbstractModel):
    """Control parameter of prohibited information detection task

    """

    def __init__(self):
        """
        :param AsrReviewInfo: Control parameter of prohibited information detection in speech.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.ProhibitedAsrReviewTemplateInfo`\n        :param OcrReviewInfo: Control parameter of prohibited information detection in text.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.ProhibitedOcrReviewTemplateInfo`\n        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedConfigureInfoForUpdate(AbstractModel):
    """Control parameter of prohibited information detection task

    """

    def __init__(self):
        """
        :param AsrReviewInfo: Control parameter of prohibited information detection in speech.\n        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.ProhibitedAsrReviewTemplateInfoForUpdate`\n        :param OcrReviewInfo: Control parameter of prohibited information detection in text.\n        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.ProhibitedOcrReviewTemplateInfoForUpdate`\n        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedOcrReviewTemplateInfo(AbstractModel):
    """Control parameter of prohibited information detection in text task

    """

    def __init__(self):
        """
        :param Switch: Switch of prohibited information detection in text task. Valid values:
<li>ON: enables prohibited information detection in text task;</li>
<li>OFF: disables prohibited information detection in text task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedOcrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of prohibited information detection in text task

    """

    def __init__(self):
        """
        :param Switch: Switch of prohibited information detection in text task. Valid values:
<li>ON: enables prohibited information detection in text task;</li>
<li>OFF: disables prohibited information detection in text task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullEventsRequest(AbstractModel):
    """PullEvents request structure.

    """

    def __init__(self):
        """
        :param ExtInfo: Reserved field for special purposes.\n        :type ExtInfo: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullEventsResponse(AbstractModel):
    """PullEvents response structure.

    """

    def __init__(self):
        """
        :param EventSet: List of events.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EventSet: list of EventContent\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.EventSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = EventContent()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullUploadRequest(AbstractModel):
    """PullUpload request structure.

    """

    def __init__(self):
        """
        :param MediaUrl: URL of the media to be pulled. Supported media format: HLS; unsupported media format: DASH.
For more information about supported extensions, please see [Media Types](https://intl.cloud.tencent.com/document/product/266/9760?from_cn_redirect=1#.E5.AA.92.E4.BD.93.E7.B1.BB.E5.9E.8B).\n        :type MediaUrl: str\n        :param MediaName: Media name.\n        :type MediaName: str\n        :param CoverUrl: URL of video cover to be pulled. Only gif, jpeg, and png formats are supported.\n        :type CoverUrl: str\n        :param Procedure: Subsequent task for media. For more information, please see [Specifying Task Flow After Upload](https://intl.cloud.tencent.com/document/product/266/9759?from_cn_redirect=1).\n        :type Procedure: str\n        :param ExpireTime: Expiration time of media file in ISO 8601 format. For more information, please see [Notes on ISO Date Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type ExpireTime: str\n        :param StorageRegion: Specifies upload region. This is only applicable to users that have special requirements for the upload region:
<li>If it is left empty, the upload region is your [default region](https://intl.cloud.tencent.com/document/product/266/14059?from=11329?from_cn_redirect=1#.E5.AD.98.E5.82.A8.E5.9C.B0.E5.9F.9F.E6.AD.A5.E9.AA.A4);</li>
<li>If it is specified, please make sure that the upload region has been [enabled for storage](https://intl.cloud.tencent.com/document/product/266/14059?from=11329?from_cn_redirect=1#.E5.AD.98.E5.82.A8.E5.9C.B0.E5.9F.9F.E6.AD.A5.E9.AA.A4).</li>\n        :type StorageRegion: str\n        :param ClassId: Category ID, which is used to categorize the media for management. A category can be created and its ID can be obtained by using the [CreateClass](https://intl.cloud.tencent.com/document/product/266/7812?from_cn_redirect=1) API.\n        :type ClassId: int\n        :param SessionContext: The source context which is used to pass through the user request information. After `Procedure` is specified, the task flow status change callback will return the value of this field. It can contain up to 1,000 characters.\n        :type SessionContext: str\n        :param SessionId: Used to identify duplicate requests. After you send a request, if any request with the same `SessionId` has already been sent in the last three days (72 hours), an error message will be returned. `SessionId` contains up to 50 characters. If this parameter is not carried or is an empty string, no deduplication will be performed.\n        :type SessionId: str\n        :param ExtInfo: Reserved field for special purposes.\n        :type ExtInfo: str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        :param SourceContext: Source context, which is used to pass through the user request information. The [upload callback](https://intl.cloud.tencent.com/document/product/266/7830?from_cn_redirect=1) API will return the value of this field. It can contain up to 250 characters.\n        :type SourceContext: str\n        """
        self.MediaUrl = None
        self.MediaName = None
        self.CoverUrl = None
        self.Procedure = None
        self.ExpireTime = None
        self.StorageRegion = None
        self.ClassId = None
        self.SessionContext = None
        self.SessionId = None
        self.ExtInfo = None
        self.SubAppId = None
        self.SourceContext = None


    def _deserialize(self, params):
        self.MediaUrl = params.get("MediaUrl")
        self.MediaName = params.get("MediaName")
        self.CoverUrl = params.get("CoverUrl")
        self.Procedure = params.get("Procedure")
        self.ExpireTime = params.get("ExpireTime")
        self.StorageRegion = params.get("StorageRegion")
        self.ClassId = params.get("ClassId")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")
        self.SourceContext = params.get("SourceContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullUploadResponse(AbstractModel):
    """PullUpload response structure.

    """

    def __init__(self):
        """
        :param TaskId: Video pull for upload task ID, which can be used to query the status of pull for upload task.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PullUploadTask(AbstractModel):
    """Video pull for upload task information

    """

    def __init__(self):
        """
        :param TaskId: Pull for upload task ID.\n        :type TaskId: str\n        :param Status: Task flow status. Valid values:
<li>PROCESSING: processing;</li>
<li>FINISH: completed.</li>\n        :type Status: str\n        :param ErrCode: Error code. 0: success; other values: failure.
<li>40000: invalid input parameter. Please check it;</li>
<li>60000: invalid source file (e.g., video data is corrupted). Please check whether the source file is normal;</li>
<li>70000: internal service error. Please try again.</li>\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param FileId: ID of video generated after pull for upload is completed.\n        :type FileId: str\n        :param MediaBasicInfo: Basic information of media file generated after pull for upload is completed.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MediaBasicInfo: :class:`tencentcloud.vod.v20180717.models.MediaBasicInfo`\n        :param MetaData: Metadata of a source video\n        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`\n        :param FileUrl: Playback address generated after pull for upload is completed.\n        :type FileUrl: str\n        :param ProcedureTaskId: If a video processing flow is specified when a video is pulled for upload, this parameter will be the ID of the task flow.\n        :type ProcedureTaskId: str\n        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1,000 characters.\n        :type SessionContext: str\n        :param SessionId: The ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or a blank string is entered, no deduplication will be performed.\n        :type SessionId: str\n        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.MediaBasicInfo = None
        self.MetaData = None
        self.FileUrl = None
        self.ProcedureTaskId = None
        self.SessionContext = None
        self.SessionId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        if params.get("MediaBasicInfo") is not None:
            self.MediaBasicInfo = MediaBasicInfo()
            self.MediaBasicInfo._deserialize(params.get("MediaBasicInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.FileUrl = params.get("FileUrl")
        self.ProcedureTaskId = params.get("ProcedureTaskId")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlCacheRequest(AbstractModel):
    """PushUrlCache request structure.

    """

    def __init__(self):
        """
        :param Urls: List of prefetched URLs. Up to 20 ones can be specified at a time.\n        :type Urls: list of str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Urls = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlCacheResponse(AbstractModel):
    """PushUrlCache response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RefererAuthPolicy(AbstractModel):
    """Referer hotlink protection configuration

    """

    def __init__(self):
        """
        :param Status: [Referer hotlink protection](https://intl.cloud.tencent.com/document/product/266/33985) status. Valid values:
<li>Enabled</li>
<li>Disabled</li>\n        :type Status: str\n        :param AuthType: Referer authentication method. Valid values:
<li>`Black`: blocklist</li>
<li>`White`: allowlist</li>\n        :type AuthType: str\n        :param Referers: List for referer authentication\n        :type Referers: list of str\n        :param BlankRefererAllowed: Whether to allow requests with empty referer to access this domain name. Valid values:
<li>Yes</li>
<li>No</li>\n        :type BlankRefererAllowed: str\n        """
        self.Status = None
        self.AuthType = None
        self.Referers = None
        self.BlankRefererAllowed = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.AuthType = params.get("AuthType")
        self.Referers = params.get("Referers")
        self.BlankRefererAllowed = params.get("BlankRefererAllowed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetProcedureTemplateRequest(AbstractModel):
    """ResetProcedureTemplate request structure.

    """

    def __init__(self):
        """
        :param Name: Task flow name\n        :type Name: str\n        :param Comment: Template description. Length limit: 256 characters.\n        :type Comment: str\n        :param MediaProcessTask: Parameter of video processing task.\n        :type MediaProcessTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskInput`\n        :param AiContentReviewTask: Parameter of AI-based content audit task.\n        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`\n        :param AiAnalysisTask: Parameter of AI-based content analysis task.\n        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`\n        :param AiRecognitionTask: Type parameter of AI-based content recognition task.\n        :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Name = None
        self.Comment = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetProcedureTemplateResponse(AbstractModel):
    """ResetProcedureTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResolutionNameInfo(AbstractModel):
    """Player substream name information

    """

    def __init__(self):
        """
        :param MinEdgeLength: Length of video short side in px.\n        :type MinEdgeLength: int\n        :param Name: Display name.\n        :type Name: str\n        """
        self.MinEdgeLength = None
        self.Name = None


    def _deserialize(self, params):
        self.MinEdgeLength = params.get("MinEdgeLength")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceTag(AbstractModel):
    """Tag key value. For details, see [Tags](https://intl.cloud.tencent.com/document/product/651?from_cn_redirect=1).

    """

    def __init__(self):
        """
        :param TagKey: Tag key.\n        :type TagKey: str\n        :param TagValue: Tag value.\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SampleSnapshotTaskInput(AbstractModel):
    """Input parameter type of sampling screencapturing task

    """

    def __init__(self):
        """
        :param Definition: Sampled screencapturing template ID.\n        :type Definition: int\n        :param WatermarkSet: List of up to 10 image or text watermarks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WatermarkSet: list of WatermarkInput\n        """
        self.Definition = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SampleSnapshotTemplate(AbstractModel):
    """Details of a sampled screencapturing template

    """

    def __init__(self):
        """
        :param Definition: Unique ID of a sampled screencapturing template.\n        :type Definition: int\n        :param Type: Template type. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param Name: Name of a sampled screencapturing template.\n        :type Name: str\n        :param Comment: Template description.\n        :type Comment: str\n        :param Width: Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param Format: Image format.\n        :type Format: str\n        :param SampleType: Sampled screencapturing type.\n        :type SampleType: str\n        :param SampleInterval: Sampling interval.\n        :type SampleInterval: int\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.\n        :type FillType: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.SampleType = None
        self.SampleInterval = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchMediaRequest(AbstractModel):
    """SearchMedia request structure.

    """

    def __init__(self):
        """
        :param FileIds: File ID set. Any element in the set can be matched.
<li>Array length limit: 10.</li>
<li>ID length limit: 40 characters.</li>\n        :type FileIds: list of str\n        :param Names: Filename set. Filenames of media files are fuzzily matched. The higher the match rate, the higher-ranked the result.
<li>Filename length limit: 40 characters.</li>
<li>Array length limit: 10.</li>\n        :type Names: list of str\n        :param NamePrefixes: Filename prefix, which matches the filenames of media files.
<li>Filename prefix length limit: 20 characters.</li>
<li>Array length limit: 10.</li>\n        :type NamePrefixes: list of str\n        :param Descriptions: File description set. Media file descriptions are fuzzily matched. The higher the match rate, the higher-ranked the result.
<li>Length limit for a single description: 100 characters</li>
<li>Array length limit: 10</li>\n        :type Descriptions: list of str\n        :param ClassIds: Category ID set. The categories of the specified IDs and all subcategories in the set are matched.
<li>Array length limit: 10.</li>\n        :type ClassIds: list of int\n        :param Tags: Tag set, which matches any element in the set.
<li>Tag length limit: 8 characters.</li>
<li>Array length limit: 10.</li>\n        :type Tags: list of str\n        :param Categories: File type. Any element in the set can be matched.
<li>Video: video file</li>
<li>Audio: audio file</li>
<li>Image: image file</li>\n        :type Categories: list of str\n        :param SourceTypes: Media file source set. For valid values, please see [SourceType](https://intl.cloud.tencent.com/document/product/266/31773?from_cn_redirect=1#MediaSourceData).
<li>Array length limit: 10.</li>\n        :type SourceTypes: list of str\n        :param StreamIds: [Stream ID](https://intl.cloud.tencent.com/document/product/267/5959?from_cn_redirect=1) set. Any element in the set can be matched.
<li>Array length limit: 10.</li>\n        :type StreamIds: list of str\n        :param Vids: Unique ID of LVB recording file. Any element in the set can be matched.
<li>Array length limit: 10.</li>\n        :type Vids: list of str\n        :param CreateTime: Matches files created within the time period.
<li>Includes specified start and end points in time.</li>\n        :type CreateTime: :class:`tencentcloud.vod.v20180717.models.TimeRange`\n        :param Sort: Sorting order.
<li>Valid value of `Sort.Field`: CreateTime.</li>
<li>If `Text`, `Names`, or `Descriptions` is not empty, the `Sort.Field` field will not take effect, and the search results will be sorted by match rate.</li>\n        :type Sort: :class:`tencentcloud.vod.v20180717.models.SortBy`\n        :param Offset: <div id="p_offset">Start offset of a paged return. Default value: 0. Entries from No. "Offset" to No. "Offset + Limit - 1" will be returned.
<li>Value range: "Offset + Limit" cannot be more than 5,000. (For more information, please see <a href="#maxResultsDesc">Limit on the Number of Results Returned by API</a>)</li></div>\n        :type Offset: int\n        :param Limit: <div id="p_limit">Number of entries returned by a paged query. Default value: 10. Entries from No. "Offset" to No. "Offset + Limit - 1" will be returned.
<li>Value range: "Offset + Limit" cannot be more than 5,000. (For more information, please see <a href="#maxResultsDesc">Limit on the Number of Results Returned by API</a>)</li></div>\n        :type Limit: int\n        :param Filters: Specifies information entry that needs to be returned for all media files. Multiple entries can be specified simultaneously. N starts from 0. If this field is left empty, all information entries will be returned by default. Valid values:
<li>basicInfo (basic video information).</li>
<li>metaData (video metadata).</li>
<li>transcodeInfo (result information of video transcoding).</li>
<li>animatedGraphicsInfo (result information of animated image generating task).</li>
<li>imageSpriteInfo (image sprite information).</li>
<li>snapshotByTimeOffsetInfo (point-in-time screenshot information).</li>
<li>sampleSnapshotInfo (sampled screenshot information).</li>
<li>keyFrameDescInfo (timestamp information).</li>
<li>adaptiveDynamicStreamingInfo (information of adaptive bitrate streaming).</li>
<li>miniProgramReviewInfo (WeChat Mini Program audit information).</li>\n        :type Filters: list of str\n        :param StorageRegions: Regions where media files are stored, such as `ap-chongqing`. For more regions, see [Storage Regions](https://intl.cloud.tencent.com/document/product/266/9760?from_cn_redirect=1#.E5.B7.B2.E6.94.AF.E6.8C.81.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8).
<li>Length limit for a single region: 20 characters</li>
<li>Array length limit: 20</li>\n        :type StorageRegions: list of str\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        :param Text: (This is not recommended. `Names`, `NamePrefixes`, or `Descriptions` should be used instead)
Search text, which fuzzily matches the media file name or description. The more matching items and the higher the match rate, the higher-ranked the result. It can contain up to 64 characters.\n        :type Text: str\n        :param SourceType: (This is not recommended. `SourceTypes` should be used instead)
Media file source. For valid values, please see [SourceType](https://intl.cloud.tencent.com/document/product/266/31773?from_cn_redirect=1#MediaSourceData).\n        :type SourceType: str\n        :param StreamId: (This is not recommended. `StreamIds` should be used instead)
[Stream ID](https://intl.cloud.tencent.com/document/product/267/5959?from_cn_redirect=1).\n        :type StreamId: str\n        :param Vid: (This is not recommended. `Vids` should be used instead)
Unique ID of LVB recording file.\n        :type Vid: str\n        :param StartTime: (This is not recommended. `CreateTime` should be used instead)
Start time in the creation time range.
<li>After or at the start time.</li>
<li>If `CreateTime.After` also exists, it will be used first.</li>
<li>In ISO 8601 format. For more information, please see [ISO Date Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).</li>\n        :type StartTime: str\n        :param EndTime: (This is not recommended. `CreateTime` should be used instead)
End time in the creation time range.
<li>Before the end time.</li>
<li>If `CreateTime.Before` also exists, it will be used first.</li>
<li>In ISO 8601 format. For more information, please see [ISO Date Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).</li>\n        :type EndTime: str\n        """
        self.FileIds = None
        self.Names = None
        self.NamePrefixes = None
        self.Descriptions = None
        self.ClassIds = None
        self.Tags = None
        self.Categories = None
        self.SourceTypes = None
        self.StreamIds = None
        self.Vids = None
        self.CreateTime = None
        self.Sort = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.StorageRegions = None
        self.SubAppId = None
        self.Text = None
        self.SourceType = None
        self.StreamId = None
        self.Vid = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.Names = params.get("Names")
        self.NamePrefixes = params.get("NamePrefixes")
        self.Descriptions = params.get("Descriptions")
        self.ClassIds = params.get("ClassIds")
        self.Tags = params.get("Tags")
        self.Categories = params.get("Categories")
        self.SourceTypes = params.get("SourceTypes")
        self.StreamIds = params.get("StreamIds")
        self.Vids = params.get("Vids")
        if params.get("CreateTime") is not None:
            self.CreateTime = TimeRange()
            self.CreateTime._deserialize(params.get("CreateTime"))
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Filters = params.get("Filters")
        self.StorageRegions = params.get("StorageRegions")
        self.SubAppId = params.get("SubAppId")
        self.Text = params.get("Text")
        self.SourceType = params.get("SourceType")
        self.StreamId = params.get("StreamId")
        self.Vid = params.get("Vid")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchMediaResponse(AbstractModel):
    """SearchMedia response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible entries.
<li>Maximum value: 5000. If the number of eligible entries is greater than 5,000, this field will return 5,000 instead of the actual number.</li>\n        :type TotalCount: int\n        :param MediaInfoSet: Media file information list\n        :type MediaInfoSet: list of MediaInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.MediaInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MediaInfoSet") is not None:
            self.MediaInfoSet = []
            for item in params.get("MediaInfoSet"):
                obj = MediaInfo()
                obj._deserialize(item)
                self.MediaInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class SegmentConfigureInfo(AbstractModel):
    """Control parameter of video splitting recognition task

    """

    def __init__(self):
        """
        :param Switch: Switch of video splitting recognition task. Valid values:
<li>ON: enables intelligent video splitting recognition task;</li>
<li>OFF: disables intelligent video splitting recognition task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentConfigureInfoForUpdate(AbstractModel):
    """Control parameter of video splitting recognition task

    """

    def __init__(self):
        """
        :param Switch: Switch of video splitting recognition task. Valid values:
<li>ON: enables intelligent video splitting recognition task;</li>
<li>OFF: disables intelligent video splitting recognition task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleHlsClipRequest(AbstractModel):
    """SimpleHlsClip request structure.

    """

    def __init__(self):
        """
        :param Url: URL of the HLS video in VOD that needs to be clipped.\n        :type Url: str\n        :param StartTimeOffset: Start offset time of clipping in seconds. Default value: 0, which means to clip from the beginning of the video. A negative number indicates how many seconds from the end of the video clipping will start at. For example, -10 means that clipping will start at the 10th second from the end.\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End offset time of clipping in seconds. Default value: 0, which means to clip till the end of the video. A negative number indicates how many seconds from the end of the video clipping will end. For example, -10 means that clipping will end at the 10th second from the end.\n        :type EndTimeOffset: float\n        :param IsPersistence: Whether to store the video clip persistently. 0: no (default), 1: yes.\n        :type IsPersistence: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.Url = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.IsPersistence = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.IsPersistence = params.get("IsPersistence")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleHlsClipResponse(AbstractModel):
    """SimpleHlsClip response structure.

    """

    def __init__(self):
        """
        :param Url: Address of clipped video.\n        :type Url: str\n        :param MetaData: Metadata of clipped video. Currently, `Size`, `Rotate`, `VideoDuration`, and `AudioDuration` fields use default value with no actual data.\n        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`\n        :param FileId: Unique ID of a video clip for persistent storage.\n        :type FileId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Url = None
        self.MetaData = None
        self.FileId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.FileId = params.get("FileId")
        self.RequestId = params.get("RequestId")


class SnapshotByTimeOffset2017(AbstractModel):
    """Screencapturing output information (v2017)

    """

    def __init__(self):
        """
        :param ErrCode: Error code
<li>0: success;</li>
<li>Other values: failure.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ErrCode: int\n        :param TimeOffset: Specific time point of screenshot in milliseconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TimeOffset: int\n        :param Url: Address of output screenshot file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Url: str\n        """
        self.ErrCode = None
        self.TimeOffset = None
        self.Url = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.TimeOffset = params.get("TimeOffset")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotByTimeOffsetTask2017(AbstractModel):
    """Time point screencapturing task information. This structure is only used for tasks initiated by the [CreateSnapshotByTimeOffset](https://intl.cloud.tencent.com/document/product/266/8102?from_cn_redirect=1) API in v2017.

    """

    def __init__(self):
        """
        :param TaskId: Screencapturing task ID.\n        :type TaskId: str\n        :param FileId: Screenshot file ID.\n        :type FileId: str\n        :param Definition: screenshot specification. For more information, please see [Parameter Template for Time Point Screencapturing](https://intl.cloud.tencent.com/document/product/266/33480?from_cn_redirect=1#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF).\n        :type Definition: int\n        :param SnapshotInfoSet: Result information of screencapturing.\n        :type SnapshotInfoSet: list of SnapshotByTimeOffset2017\n        """
        self.TaskId = None
        self.FileId = None
        self.Definition = None
        self.SnapshotInfoSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.FileId = params.get("FileId")
        self.Definition = params.get("Definition")
        if params.get("SnapshotInfoSet") is not None:
            self.SnapshotInfoSet = []
            for item in params.get("SnapshotInfoSet"):
                obj = SnapshotByTimeOffset2017()
                obj._deserialize(item)
                self.SnapshotInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotByTimeOffsetTaskInput(AbstractModel):
    """Input parameter type of time point screencapturing task

    """

    def __init__(self):
        """
        :param Definition: Time point screencapturing template ID.\n        :type Definition: int\n        :param ExtTimeOffsetSet: The list of screenshot time points. “s” and “%” formats are supported:
<li>When a time point string ends with “s”, its unit is second. For example, “3.5s” means the 3.5th second of the video.</li>
<li>When a time point string ends with “%”, it represents the percentage of the video’s duration. For example, “10%” means that the time point is at the 10% of the video’s entire duration.</li>\n        :type ExtTimeOffsetSet: list of str\n        :param TimeOffsetSet: List of time points for screencapturing in <font color=red>milliseconds</font>.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TimeOffsetSet: list of float\n        :param WatermarkSet: List of up to 10 image or text watermarks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WatermarkSet: list of WatermarkInput\n        """
        self.Definition = None
        self.ExtTimeOffsetSet = None
        self.TimeOffsetSet = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ExtTimeOffsetSet = params.get("ExtTimeOffsetSet")
        self.TimeOffsetSet = params.get("TimeOffsetSet")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotByTimeOffsetTemplate(AbstractModel):
    """Details of a specified time point screencapturing template

    """

    def __init__(self):
        """
        :param Definition: Unique ID of a specified time point screencapturing template.\n        :type Definition: int\n        :param Type: Template type. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param Name: Name of a specified time point screencapturing template.\n        :type Name: str\n        :param Comment: Template description.\n        :type Comment: str\n        :param Width: Maximum value of the width (or long side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of a screenshot in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.\n        :type Height: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.\n        :type ResolutionAdaptive: str\n        :param Format: Image format.\n        :type Format: str\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. The following fill types are supported:
<li> stretch: stretch. The screenshot will be stretched frame by frame to match the aspect ratio of the source video, which may make the screenshot "shorter" or "longer";</li>
<li>black: fill with black. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with black color blocks.</li>
<li>white: fill with white. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with white color blocks.</li>
<li>gauss: fill with Gaussian blur. This option retains the aspect ratio of the source video for the screenshot and fills the unmatched area with Gaussian blur.</li>
Default value: black.\n        :type FillType: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortBy(AbstractModel):
    """Sort by criterion

    """

    def __init__(self):
        """
        :param Field: Sort by field\n        :type Field: str\n        :param Order: Sorting order. Valid values: Asc (ascending), Desc (descending)\n        :type Order: str\n        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecificationDataItem(AbstractModel):
    """Statistics of task with specified specification.

    """

    def __init__(self):
        """
        :param Specification: Task specification.\n        :type Specification: str\n        :param Data: Statistics.\n        :type Data: list of TaskStatDataItem\n        """
        self.Specification = None
        self.Data = None


    def _deserialize(self, params):
        self.Specification = params.get("Specification")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TaskStatDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitMediaOutputConfig(AbstractModel):
    """Information of video splitting output files.

    """

    def __init__(self):
        """
        :param MediaName: Name of an output file. This parameter can contain up to 64 characters, and will be generated by the system if it is left empty.\n        :type MediaName: str\n        :param Type: Output file format. Valid values: mp4 (default), hls.\n        :type Type: str\n        :param ClassId: Category ID, which is used to categorize the media file for management. You can use [CreateClass](https://intl.cloud.tencent.com/document/product/266/7812?from_cn_redirect=1) API to create a category and get the category ID.
<li>Default value: 0, which means other categories.</li>\n        :type ClassId: int\n        :param ExpireTime: Expiration time of an output file. After passing the expiration time, the file will be deleted. There is no expiration time set for a file by default. The time is in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?lang=en&pg=).\n        :type ExpireTime: str\n        """
        self.MediaName = None
        self.Type = None
        self.ClassId = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.MediaName = params.get("MediaName")
        self.Type = params.get("Type")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitMediaTask(AbstractModel):
    """Video splitting task information. This field has a value only when `TaskType` is `SplitMedia`.

    """

    def __init__(self):
        """
        :param TaskId: Task ID.\n        :type TaskId: str\n        :param Status: Task flow status. Valid values:
<li>PROCESSING: processing</li>
<li>FINISH: finished</li>\n        :type Status: str\n        :param ErrCodeExt: Error code. An empty string indicates the task is successful; other values indicate failure. For details, see [Video Processing Error Codes](https://intl.cloud.tencent.com/zh/document/product/266/39145).\n        :type ErrCodeExt: str\n        :param ErrCode: Error code. 0 indicates the task is successful; other values indicate failure. You're not recommended to use this parameter, but to use the new parameter `ErrCodeExt`.\n        :type ErrCode: int\n        :param Message: Error information.\n        :type Message: str\n        :param FileInfoSet: List of video splitting task details.\n        :type FileInfoSet: list of SplitMediaTaskSegmentInfo\n        :param SessionContext: The source context which is used to pass through the user request information. The task flow status change callback will return the value of this field. It can contain up to 1000 characters.\n        :type SessionContext: str\n        :param SessionId: ID used for deduplication. If there was a request with the same ID in the last seven days, the current request will return an error. The ID can contain up to 50 characters. If this parameter is left empty or set to an empty string, no deduplication will be performed.\n        :type SessionId: str\n        """
        self.TaskId = None
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.FileInfoSet = None
        self.SessionContext = None
        self.SessionId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = SplitMediaTaskSegmentInfo()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitMediaTaskInput(AbstractModel):
    """Input information of a video splitting task.

    """

    def __init__(self):
        """
        :param FileId: Video ID.\n        :type FileId: str\n        :param StartTimeOffset: Offset of the video splitting start time in seconds.
<li>If this parameter is left empty or set to 0, the transcoded video will start at the same time as the original video.</li>
<li>If this parameter is set to a positive number (n for example), the transcoded video will start at the nth second of the original video.</li>
<li>If this parameter is set to a negative number (-n for example), the transcoded video will start at the nth second before the end of the original video.</li>\n        :type StartTimeOffset: float\n        :param EndTimeOffset: Offset of the video splitting end time in seconds.
<li>If this parameter is left empty or set to 0, the transcoded video will end at the same time as the original video.</li>
<li>If this parameter is set to a positive number (n for example), the transcoded video will end at the nth second of the original video.</li>
<li>If this parameter is set to a negative number (-n for example), the transcoded video will end at the nth second before the end of the original video.</li>\n        :type EndTimeOffset: float\n        :param ProcedureName: [Task flow template](https://intl.cloud.tencent.com/document/product/266/33931?lang=en&pg=) name, which should be entered if you want to perform a task flow on the generated new video.\n        :type ProcedureName: str\n        :param OutputConfig: Output information of a video splitting task.\n        :type OutputConfig: :class:`tencentcloud.vod.v20180717.models.SplitMediaOutputConfig`\n        """
        self.FileId = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.ProcedureName = None
        self.OutputConfig = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.ProcedureName = params.get("ProcedureName")
        if params.get("OutputConfig") is not None:
            self.OutputConfig = SplitMediaOutputConfig()
            self.OutputConfig._deserialize(params.get("OutputConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitMediaTaskSegmentInfo(AbstractModel):
    """Information of a video splitting task.

    """

    def __init__(self):
        """
        :param Input: Input information of a video splitting task.\n        :type Input: :class:`tencentcloud.vod.v20180717.models.SplitMediaTaskInput`\n        :param Output: Output information of a video splitting task.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Output: :class:`tencentcloud.vod.v20180717.models.TaskOutputMediaInfo`\n        :param ProcedureTaskId: If a video processing flow is specified when a video splitting task is initiated, this field will be the task flow ID.\n        :type ProcedureTaskId: str\n        """
        self.Input = None
        self.Output = None
        self.ProcedureTaskId = None


    def _deserialize(self, params):
        if params.get("Input") is not None:
            self.Input = SplitMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = TaskOutputMediaInfo()
            self.Output._deserialize(params.get("Output"))
        self.ProcedureTaskId = params.get("ProcedureTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatDataItem(AbstractModel):
    """Statistics

    """

    def __init__(self):
        """
        :param Time: Start time of data time range in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I). For example, if the time granularity is 1-day, `2018-12-01T00:00:00+08:00` represents the time range between December 1, 2018 (inclusive) and December 2, 2018 (not inclusive).
<li>For data at hourly level, `2019-08-22T00:00:00+08:00` indicates the statistics between 00:00 and 01:00 AM on August 22, 2019.</li>
<li>For data at daily level, `2019-08-22T00:00:00+08:00` indicates statistics on August 22, 2019.</li>\n        :type Time: str\n        :param Value: Data size.
<li>Storage capacity in bytes.</li>
<li>Transcoding duration in seconds.</li>
<li>Traffic in bytes.</li>
<li>Bandwidth in bps.</li>\n        :type Value: int\n        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StickerTrackItem(AbstractModel):
    """Information of sticker on sticker track.

    """

    def __init__(self):
        """
        :param SourceMedia: Source of media material for sticker segment, which can be:
<li>ID of VOD media files</li>
<li>Download URL of other media files</li>
Note: when a download URL of other media files is used as the material source and access control (such as hotlink protection) is enabled, the URL needs to carry access control parameters (such as hotlink protection signature).\n        :type SourceMedia: str\n        :param Duration: Sticker duration in seconds.\n        :type Duration: float\n        :param StartTime: Start time of sticker on track in seconds.\n        :type StartTime: float\n        :param CoordinateOrigin: Origin position. Valid values:
<li> Center: the origin of coordinates is the center position, such as the center of canvas.</li>
Default value: Center.\n        :type CoordinateOrigin: str\n        :param XPos: The horizontal position of the origin of the sticker relative to the origin of the canvas. % and px formats are supported:
<li>If the string ends in %, the `XPos` of the sticker will be at the position of the specified percentage of the canvas width; for example, `10%` means that `XPos` is 10% of the canvas width.</li><li>If the string ends in px, the `XPos` of the sticker will be in px; for example, `100px` means that `XPos` is 100 px.</li>
Default value: 0 px.\n        :type XPos: str\n        :param YPos: The vertical position of the origin of the sticker relative to the origin of the canvas. % and px formats are supported:
<li>If the string ends in %, the `YPos` of the sticker will be at the position of the specified percentage of the canvas height; for example, `10%` means that `YPos` is 10% of the canvas height.</li>
<li>If the string ends in px, the `YPos` of the sticker will be in px; for example, `100px` means that `YPos` is 100 px.</li>
Default value: 0 px.\n        :type YPos: str\n        :param Width: Sticker width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the sticker will be the specified percentage of the canvas width; for example, `10%` means that `Width` is 10% of the canvas width.</li>
<li>If the string ends in px, the `Width` of the sticker will be in px; for example, `100px` means that `Width` is 100 px.</li>
<li>If both `Width` and `Height` are empty, then they will be the `Width` and `Height` of the sticker material, respectively.</li>
<li>If `Width` is empty (0), but `Height` is not empty, `Width` will be proportionally scaled.</li>
<li>If `Width` is not empty, but `Height` is empty, `Height` will be proportionally scaled.</li>\n        :type Width: str\n        :param Height: Sticker height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the sticker will be the specified percentage of the canvas height; for example, `10%` means that `Height` is 10% of the canvas height.</li>
<li>If the string ends in px, the `Height` of the sticker will be in px; for example, `100px` means that `Height` is 100 px.</li>
<li>If both `Width` and `Height` are empty, then they will be the `Width` and `Height` of the sticker material, respectively.</li>
<li>If `Width` is empty, but `Height` is not empty, `Width` will be proportionally scaled.</li>
<li>If `Width` is not empty, but `Height` is empty, `Height` will be proportionally scaled.</li>\n        :type Height: str\n        :param ImageOperations: Operation on sticker such as image rotation.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageOperations: list of ImageTransform\n        """
        self.SourceMedia = None
        self.Duration = None
        self.StartTime = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.ImageOperations = None


    def _deserialize(self, params):
        self.SourceMedia = params.get("SourceMedia")
        self.Duration = params.get("Duration")
        self.StartTime = params.get("StartTime")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("ImageOperations") is not None:
            self.ImageOperations = []
            for item in params.get("ImageOperations"):
                obj = ImageTransform()
                obj._deserialize(item)
                self.ImageOperations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageStatData(AbstractModel):
    """VOD storage usage by region.

    """

    def __init__(self):
        """
        :param Area: VOD storage billing region. Valid values:
<li>Chinese Mainland</li>
<li>Outside Chinese Mainland</li>\n        :type Area: str\n        :param TotalStorage: Current total storage capacity in bytes.\n        :type TotalStorage: int\n        :param InfrequentStorage: Current STANDARD_IA storage capacity in bytes.\n        :type InfrequentStorage: int\n        :param StandardStorage: Current STANDARD storage capacity in bytes.\n        :type StandardStorage: int\n        :param ArchiveStorage: Current ARCHIVE storage usage in bytes\n        :type ArchiveStorage: int\n        :param DeepArchiveStorage: Current DEEP ARCHIVE storage usage in bytes\n        :type DeepArchiveStorage: int\n        """
        self.Area = None
        self.TotalStorage = None
        self.InfrequentStorage = None
        self.StandardStorage = None
        self.ArchiveStorage = None
        self.DeepArchiveStorage = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        self.TotalStorage = params.get("TotalStorage")
        self.InfrequentStorage = params.get("InfrequentStorage")
        self.StandardStorage = params.get("StandardStorage")
        self.ArchiveStorage = params.get("ArchiveStorage")
        self.DeepArchiveStorage = params.get("DeepArchiveStorage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAppIdInfo(AbstractModel):
    """Subapplication information.

    """

    def __init__(self):
        """
        :param SubAppId: Subapplication ID.\n        :type SubAppId: int\n        :param Name: Subapplication name.\n        :type Name: str\n        :param Description: Subapplication overview.\n        :type Description: str\n        :param CreateTime: Subapplication creation time of task in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param Status: Subapplication status. Valid values:
<li>On: enabled</li>
<li>Off: disabled</li>
<li>Destroying: terminating</li>
<li>Destroyed: terminated</li>\n        :type Status: str\n        """
        self.SubAppId = None
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.Status = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SvgWatermarkInput(AbstractModel):
    """Input parameter of SVG watermarking template

    """

    def __init__(self):
        """
        :param Width: Watermark width, which supports six formats of px, %, W%, H%, S%, and L%:
<li>If the string ends in px, the `Width` of the watermark will be in px; for example, `100px` means that `Width` is 100 px; if `0px` is entered
 and `Height` is not `0px`, the watermark width will be proportionally scaled based on the source SVG image; if `0px` is entered for both `Width` and `Height`, the watermark width will be the width of the source SVG image;</li>
<li>If the string ends in `W%`, the `Width` of the watermark will be the specified percentage of the video width; for example, `10W%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in `H%`, the `Width` of the watermark will be the specified percentage of the video height; for example, `10H%` means that `Width` is 10% of the video height;</li>
<li>If the string ends in `S%`, the `Width` of the watermark will be the specified percentage of the short side of the video; for example, `10S%` means that `Width` is 10% of the short side of the video;</li>
<li>If the string ends in `L%`, the `Width` of the watermark will be the specified percentage of the long side of the video; for example, `10L%` means that `Width` is 10% of the long side of the video;</li>
<li>If the string ends in %, the meaning is the same as `W%`.</li>
Default value: 10W%.\n        :type Width: str\n        :param Height: Watermark height, which supports six formats of px, %, W%, H%, S%, and L%:
<li>If the string ends in px, the `Height` of the watermark will be in px; for example, `100px` means that `Height` is 100 px; if `0px` is entered
 and `Width` is not `0px`, the watermark height will be proportionally scaled based on the source SVG image; if `0px` is entered for both `Width` and `Height`, the watermark height will be the height of the source SVG image;</li>
<li>If the string ends in `W%`, the `Height` of the watermark will be the specified percentage of the video width; for example, `10W%` means that `Height` is 10% of the video width;</li>
<li>If the string ends in `H%`, the `Height` of the watermark will be the specified percentage of the video height; for example, `10H%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in `S%`, the `Height` of the watermark will be the specified percentage of the short side of the video; for example, `10S%` means that `Height` is 10% of the short side of the video;</li>
<li>If the string ends in `L%`, the `Height` of the watermark will be the specified percentage of the long side of the video; for example, `10L%` means that `Height` is 10% of the long side of the video;</li>
<li>If the string ends in %, the meaning is the same as `H%`.</li>
Default value: 0 px.\n        :type Height: str\n        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SvgWatermarkInputForUpdate(AbstractModel):
    """Input parameter of SVG watermarking template

    """

    def __init__(self):
        """
        :param Width: Watermark width, which supports six formats of px, %, W%, H%, S%, and L%:
<li>If the string ends in px, the `Width` of the watermark will be in px; for example, `100px` means that `Width` is 100 px; if `0px` is entered
 and `Height` is not `0px`, the watermark width will be proportionally scaled based on the source SVG image; if `0px` is entered for both `Width` and `Height`, the watermark width will be the width of the source SVG image;</li>
<li>If the string ends in `W%`, the `Width` of the watermark will be the specified percentage of the video width; for example, `10W%` means that `Width` is 10% of the video width;</li>
<li>If the string ends in `H%`, the `Width` of the watermark will be the specified percentage of the video height; for example, `10H%` means that `Width` is 10% of the video height;</li>
<li>If the string ends in `S%`, the `Width` of the watermark will be the specified percentage of the short side of the video; for example, `10S%` means that `Width` is 10% of the short side of the video;</li>
<li>If the string ends in `L%`, the `Width` of the watermark will be the specified percentage of the long side of the video; for example, `10L%` means that `Width` is 10% of the long side of the video;</li>
<li>If the string ends in %, the meaning is the same as `W%`.</li>
Default value: 10W%.\n        :type Width: str\n        :param Height: Watermark height, which supports six formats of px, %, W%, H%, S%, and L%:
<li>If the string ends in px, the `Height` of the watermark will be in px; for example, `100px` means that `Height` is 100 px; if `0px` is entered
 and `Width` is not `0px`, the watermark height will be proportionally scaled based on the source SVG image; if `0px` is entered for both `Width` and `Height`, the watermark height will be the height of the source SVG image;</li>
<li>If the string ends in `W%`, the `Height` of the watermark will be the specified percentage of the video width; for example, `10W%` means that `Height` is 10% of the video width;</li>
<li>If the string ends in `H%`, the `Height` of the watermark will be the specified percentage of the video height; for example, `10H%` means that `Height` is 10% of the video height;</li>
<li>If the string ends in `S%`, the `Height` of the watermark will be the specified percentage of the short side of the video; for example, `10S%` means that `Height` is 10% of the short side of the video;</li>
<li>If the string ends in `L%`, the `Height` of the watermark will be the specified percentage of the long side of the video; for example, `10L%` means that `Height` is 10% of the long side of the video;</li>
<li>If the string ends in %, the meaning is the same as `H%`.
Default value: 0 px.\n        :type Height: str\n        :param CycleConfig: Watermark cycle configuration, which is used to configure watermarks so that they will be displayed and hidden periodically.
Primary use case: watermarks can be added at various positions in a video, which are displayed and hidden periodically to prevent them from being covered.
For example, watermarks A, B, C, and D are set in the top-left corner, top-right corner, bottom-right corner, and bottom-left corner of a video, respectively. After the first video frame, { A will be displayed for 5s -> B for 5s -> C for 5s -> D for 5s } -> A for 5s -> B for 5s -> ... Only one watermark will be visible at any time.
Within the braces ({}) is a major cycle composed of four watermarks, namely, A, B, C, and D, which lasts for 20 seconds in a cycle.
Watermarks A, B, C, and D are displayed periodically for 5 seconds and hidden for 15 seconds each in a fixed order.
This configuration item is used to describe the cycle configuration of a single watermark.\n        :type CycleConfig: :class:`tencentcloud.vod.v20180717.models.WatermarkCycleConfigForUpdate`\n        """
        self.Width = None
        self.Height = None
        self.CycleConfig = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("CycleConfig") is not None:
            self.CycleConfig = WatermarkCycleConfigForUpdate()
            self.CycleConfig._deserialize(params.get("CycleConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TEHDConfig(AbstractModel):
    """TESHD parameter configuration.

    """

    def __init__(self):
        """
        :param Type: TESHD type. Valid values:
<li>TEHD-100: TESHD-100.</li>
If this parameter is left blank, TESHD will not be enabled.\n        :type Type: str\n        :param MaxVideoBitrate: Maximum bitrate, which is valid when `Type` is `TESHD`.
If this parameter is left blank or 0 is entered, there will be no upper limit for bitrate.\n        :type MaxVideoBitrate: int\n        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TEHDConfigForUpdate(AbstractModel):
    """TESHD parameter configuration.

    """

    def __init__(self):
        """
        :param Type: TESHD type. Valid values:
<li>TEHD-100: TESHD-100.</li>
If this parameter is left blank, no modification will be made.\n        :type Type: str\n        :param MaxVideoBitrate: Maximum bitrate. If this parameter is left blank, no modification will be made.\n        :type MaxVideoBitrate: int\n        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagConfigureInfo(AbstractModel):
    """Control parameter of intelligent tagging task

    """

    def __init__(self):
        """
        :param Switch: Switch of intelligent tagging task. Valid values:
<li>ON: enables intelligent tagging task;</li>
<li>OFF: disables intelligent tagging task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagConfigureInfoForUpdate(AbstractModel):
    """Control parameter of intelligent tagging task

    """

    def __init__(self):
        """
        :param Switch: Switch of intelligent tagging task. Valid values:
<li>ON: enables intelligent tagging task;</li>
<li>OFF: disables intelligent tagging task.</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOutputMediaInfo(AbstractModel):
    """Output media file information of a video processing task.

    """

    def __init__(self):
        """
        :param FileId: Media file ID.\n        :type FileId: str\n        :param MediaBasicInfo: \n        :type MediaBasicInfo: :class:`tencentcloud.vod.v20180717.models.MediaBasicInfo`\n        """
        self.FileId = None
        self.MediaBasicInfo = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("MediaBasicInfo") is not None:
            self.MediaBasicInfo = MediaBasicInfo()
            self.MediaBasicInfo._deserialize(params.get("MediaBasicInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSimpleInfo(AbstractModel):
    """Task overview information

    """

    def __init__(self):
        """
        :param TaskId: Task ID.\n        :type TaskId: str\n        :param Status: Task status. Valid values: `WAITING` (waiting), `PROCESSING` (processing), `FINISH` (completed)\n        :type Status: str\n        :param FileId: Video ID\n        :type FileId: str\n        :param TaskType: Task type. Valid values:
<li>Procedure: video processing task;</li>
<li>EditMedia: video editing task</li>
<li>WechatDistribute: release on WeChat task.</li>
Task types compatible with v2017:
<li>Transcode: transcoding task;</li>
<li>SnapshotByTimeOffset: video screencapturing task</li>
<li>Concat: video splicing task;</li>
<li>Clip: video clipping task;</li>
<li>ImageSprites: image sprite generating task.</li>\n        :type TaskType: str\n        :param CreateTime: Creation time of task in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param BeginProcessTime: Start time of task execution in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I). If the task has not been started yet, this field will be empty.\n        :type BeginProcessTime: str\n        :param FinishTime: End time of task in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I). If the task has not been completed yet, this field will be empty.\n        :type FinishTime: str\n        :param SessionId: ID used for deduplication if there was a request with the same ID in the last seven days.\n        :type SessionId: str\n        :param SessionContext: Source context, which is used to pass through the user request information.\n        :type SessionContext: str\n        """
        self.TaskId = None
        self.Status = None
        self.FileId = None
        self.TaskType = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.FileId = params.get("FileId")
        self.TaskType = params.get("TaskType")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStatData(AbstractModel):
    """Video processing task statistics.

    """

    def __init__(self):
        """
        :param TaskType: Task type.
<li>Transcoding: basic transcoding</li>
<li>Transcoding-TESHD: TESHD transcoding</li>
<li>Editing: video editing</li>
<li>AdaptiveBitrateStreaming: adaptive bitrate streaming</li>
<li>ContentAudit: content moderation</li>
<li>Transcode: transcoding types, including basic transcoding, TESHD transcoding and video editing. This value is not recommended.</li>\n        :type TaskType: str\n        :param Summary: Task statistics overview (usage unit: second).\n        :type Summary: list of TaskStatDataItem\n        :param Details: Detailed statistics of tasks with different specifications.
Transcoding specification:
<li>Remuxing: remuxing</li>
<li>Audio: audio transcoding</li>
<li>Standard.H264.SD: H.264 SD transcoding</li>
<li>Standard.H264.HD: H.264 HD transcoding</li>
<li>Standard.H264.FHD: H.264 FHD transcoding</li>
<li>Standard.H264.2K: H.264 2K transcoding</li>
<li>Standard.H264.4K: H.264 4K transcoding</li>
<li>Standard.H265.SD: H.265 SD transcoding</li>
<li>Standard.H265.HD: H.265 HD transcoding</li>
<li>Standard.H265.FHD: H.265 FHD transcoding</li>
<li>Standard.H265.2K: H.265 2K transcoding</li>
<li>Standard.H265.4K: H.265 4K transcoding</li>
<li>TESHD-10.H264.SD: H.264 SD TESHD transcoding</li>
<li>TESHD-10.H264.HD: H.264 HD TESHD transcoding</li>
<li>TESHD-10.H264.FHD: H.264 FHD TESHD transcoding</li>
<li>TESHD-10.H264.2K: H.264 2K TESHD transcoding</li>
<li>TESHD-10.H264.4K: H.264 4K TESHD transcoding</li>
<li>TESHD-10.H265.SD: H.265 SD TESHD transcoding</li>
<li>TESHD-10.H265.HD: H.265 HD TESHD transcoding</li>
<li>TESHD-10.H265.FHD: H.265 FHD TESHD transcoding</li>
<li>TESHD-10.H265.2K: H.265 2K TESHD transcoding</li>
<li>TESHD-10.H265.4K: H.265 4K TESHD transcoding</li>
<li>Edit.Audio: audio editing</li>
<li>Edit.H264.SD: H.264 SD video editing</li>
<li>Edit.H264.HD: H.264 HD video editing</li>
<li>Edit.H264.FHD: H.264 FHD video editing</li>
<li>Edit.H264.2K: H.264 2K video editing</li>
<li>Edit.H264.4K: H.264 4K video editing</li>
<li>Edit.H265.SD: H.265 SD video editing</li>
<li>Edit.H265.HD: H.265 HD video editing</li>
<li>Edit.H265.FHD: H.265 FHD video editing</li>
<li>Edit.H265.2K: H.265 2K video editing</li>
<li>Edit.H265.4K: H.265 4K video editing</li>\n        :type Details: list of SpecificationDataItem\n        """
        self.TaskType = None
        self.Summary = None
        self.Details = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        if params.get("Summary") is not None:
            self.Summary = []
            for item in params.get("Summary"):
                obj = TaskStatDataItem()
                obj._deserialize(item)
                self.Summary.append(obj)
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = SpecificationDataItem()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStatDataItem(AbstractModel):
    """Task statistics, including number of tasks and usage.

    """

    def __init__(self):
        """
        :param Time: Start time of data time range in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). For example, if the time granularity is 1-day, `2018-12-01T00:00:00+08:00` represents the time range between December 1, 2018 (inclusive) and December 2, 2018 (not inclusive).\n        :type Time: str\n        :param Count: Number of tasks.\n        :type Count: int\n        :param Usage: Task usage.\n        :type Usage: int\n        """
        self.Time = None
        self.Count = None
        self.Usage = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Count = params.get("Count")
        self.Usage = params.get("Usage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TempCertificate(AbstractModel):
    """Temporary credential

    """

    def __init__(self):
        """
        :param SecretId: Temporary security certificate ID.\n        :type SecretId: str\n        :param SecretKey: Temporary security certificate `Key`.\n        :type SecretKey: str\n        :param Token: Token value.\n        :type Token: str\n        :param ExpiredTime: Certificate expiration time. A Unix timestamp will be returned which is accurate down to the second.\n        :type ExpiredTime: int\n        """
        self.SecretId = None
        self.SecretKey = None
        self.Token = None
        self.ExpiredTime = None


    def _deserialize(self, params):
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Token = params.get("Token")
        self.ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismConfigureInfo(AbstractModel):
    """Control parameter of terrorism information detection task

    """

    def __init__(self):
        """
        :param ImgReviewInfo: Control parameter of terrorism information detection in video image task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.TerrorismImgReviewTemplateInfo`\n        :param OcrReviewInfo: Control parameter of terrorism information detection in text task.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.TerrorismOcrReviewTemplateInfo`\n        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismConfigureInfoForUpdate(AbstractModel):
    """Control parameter of terrorism information detection task.

    """

    def __init__(self):
        """
        :param ImgReviewInfo: Control parameter of terrorism information detection in video image task.\n        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.TerrorismImgReviewTemplateInfoForUpdate`\n        :param OcrReviewInfo: Control parameter of terrorism information detection in text task.\n        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.TerrorismOcrReviewTemplateInfoForUpdate`\n        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismImgReviewTemplateInfo(AbstractModel):
    """Control parameter of terrorism information detection in video image task

    """

    def __init__(self):
        """
        :param Switch: Switch of terrorism information detection in video image task. Valid values:
<li>ON: enables terrorism information detection in video image task;</li>
<li>OFF: disables terrorism information detection in video image task.</li>\n        :type Switch: str\n        :param LabelSet: Filter tags for terrorism information detection in images. If a moderation result contains a selected tag, it will be returned. If no filter tag is specified, all moderation results will be returned. Valid values:
<li>`guns`: weapons and guns</li>
<li>`crowd`: crowds</li>
<li>`bloody`: bloody images</li>
<li>`police`: police forces</li>
<li>`banners`: terrorism flags</li>
<li>`militant`: militants</li>
<li>`explosion`: explosions and fires</li>
<li>`terrorists`: terrorists</li>
<li>`scenario`: terrorism images</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 90 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 80 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismImgReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of terrorism information detection in video image task.

    """

    def __init__(self):
        """
        :param Switch: Switch of terrorism information detection in video image task. Valid values:
<li>ON: enables terrorism information detection in video image task;</li>
<li>OFF: disables terrorism information detection in video image task.</li>\n        :type Switch: str\n        :param LabelSet: Filter tags for terrorism information detection in images. If a moderation result contains a selected tag, it will be returned. If no filter tag is specified, all moderation results will be returned. Valid values:
<li>`guns`: weapons and guns</li>
<li>`crowd`: crowds</li>
<li>`bloody`: bloody images</li>
<li>`police`: police forces</li>
<li>`banners`: terrorism flags</li>
<li>`militant`: militants</li>
<li>`explosion`: explosions and fires</li>
<li>`terrorists`: terrorists</li>
<li>`scenario`: terrorism images</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismOcrReviewTemplateInfo(AbstractModel):
    """Control parameter of terrorism information detection in text task

    """

    def __init__(self):
        """
        :param Switch: Switch of terrorism information detection in text task. Valid values:
<li>ON: enables terrorism information detection in text task;</li>
<li>OFF: disables terrorism information detection in text task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismOcrReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of terrorism information detection in text task

    """

    def __init__(self):
        """
        :param Switch: Switch of terrorism information detection in text task. Valid values:
<li>ON: enables terrorism information detection in text task;</li>
<li>OFF: disables terrorism information detection in text task.</li>\n        :type Switch: str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWatermarkTemplateInput(AbstractModel):
    """Text watermarking template

    """

    def __init__(self):
        """
        :param FontType: Font type. Currently, two types are supported:
<li>simkai.ttf: both Chinese and English are supported;</li>
<li>arial.ttf: only English is supported.</li>\n        :type FontType: str\n        :param FontSize: Font size in Npx format where N is a numeric value.\n        :type FontSize: str\n        :param FontColor: Font color in 0xRRGGBB format. Default value: 0xFFFFFF (white).\n        :type FontColor: str\n        :param FontAlpha: Text transparency. Value range: (0, 1]
<li>0: completely transparent</li>
<li>1: completely opaque</li>
Default value: 1.\n        :type FontAlpha: float\n        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWatermarkTemplateInputForUpdate(AbstractModel):
    """Text watermarking template

    """

    def __init__(self):
        """
        :param FontType: Font type. Currently, two types are supported:
<li>simkai.ttf: both Chinese and English are supported;</li>
<li>arial.ttf: only English is supported.</li>\n        :type FontType: str\n        :param FontSize: Font size in Npx format where N is a numeric value.\n        :type FontSize: str\n        :param FontColor: Font color in 0xRRGGBB format. Default value: 0xFFFFFF (white).\n        :type FontColor: str\n        :param FontAlpha: Text transparency. Value range: (0, 1]
<li>0: completely transparent</li>
<li>1: completely opaque</li>\n        :type FontAlpha: float\n        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeRange(AbstractModel):
    """General data type used to describe a time period.

    """

    def __init__(self):
        """
        :param After: <li>After or at this time (start time).</li>
<li>In ISO 8601 format. For more information, please see [ISO Date Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).</li>\n        :type After: str\n        :param Before: <li>Earlier than this time (end time).</li>
<li>In ISO 8601 format. For more information, please see [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).</li>\n        :type Before: str\n        """
        self.After = None
        self.Before = None


    def _deserialize(self, params):
        self.After = params.get("After")
        self.Before = params.get("Before")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodePlayInfo2017(AbstractModel):
    """Video transcoding playback information (v2017)

    """

    def __init__(self):
        """
        :param Url: Playback address.\n        :type Url: str\n        :param Definition: Transcoding specification ID. For more information, please see [Transcoding Parameter Template](https://intl.cloud.tencent.com/document/product/266/33478?from_cn_redirect=1#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF).\n        :type Definition: int\n        :param Bitrate: Sum of the average bitrate of a video stream and that of an audio stream in bps.\n        :type Bitrate: int\n        :param Height: Maximum value of the height of a video stream in px.\n        :type Height: int\n        :param Width: Maximum value of the width of a video stream in px.\n        :type Width: int\n        """
        self.Url = None
        self.Definition = None
        self.Bitrate = None
        self.Height = None
        self.Width = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTask2017(AbstractModel):
    """Video transcoding task information. This structure is only used for tasks initiated by the [ConvertVodFile](https://intl.cloud.tencent.com/document/product/266/7822?from_cn_redirect=1) API in v2017.

    """

    def __init__(self):
        """
        :param TaskId: Transcoding task ID.\n        :type TaskId: str\n        :param ErrCode: Error code
<li>0: success;</li>
<li>Other values: failure.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param FileId: ID of transcoded file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: str\n        :param FileName: Name of transcoded file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileName: str\n        :param Duration: Video duration in seconds.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Duration: int\n        :param CoverUrl: Cover address.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CoverUrl: str\n        :param PlayInfoSet: Playback information generated after video transcoding.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PlayInfoSet: list of TranscodePlayInfo2017\n        """
        self.TaskId = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileName = None
        self.Duration = None
        self.CoverUrl = None
        self.PlayInfoSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.Duration = params.get("Duration")
        self.CoverUrl = params.get("CoverUrl")
        if params.get("PlayInfoSet") is not None:
            self.PlayInfoSet = []
            for item in params.get("PlayInfoSet"):
                obj = TranscodePlayInfo2017()
                obj._deserialize(item)
                self.PlayInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskInput(AbstractModel):
    """Input parameter type of transcoding task

    """

    def __init__(self):
        """
        :param Definition: Video transcoding template ID.\n        :type Definition: int\n        :param WatermarkSet: List of up to 10 image or text watermarks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WatermarkSet: list of WatermarkInput\n        :param MosaicSet: List of blurs. Up to 10 ones can be supported.\n        :type MosaicSet: list of MosaicInput\n        :param HeadTailSet: List of video opening/closing credits configuration template IDs. You can enter up to 10 IDs.\n        :type HeadTailSet: list of HeadTailTaskInput\n        :param StartTimeOffset: Start time offset of a transcoded video, in seconds.
<li>If this parameter is left empty or set to 0, the transcoded video will start at the same time as the original video.</li>
<li>If this parameter is set to a positive number (n for example), the transcoded video will start at the nth second of the original video.</li>
<li>If this parameter is set to a negative number (-n for example), the transcoded video will start at the nth second before the end of the original video.</li>\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of a transcoded video, in seconds.
<li>If this parameter is left empty or set to 0, the transcoded video will end at the same time as the original video.</li>
<li>If this parameter is set to a positive number (n for example), the transcoded video will end at the nth second of the original video.</li>
<li>If this parameter is set to a negative number (-n for example), the transcoded video will end at the nth second before the end of the original video.</li>\n        :type EndTimeOffset: float\n        """
        self.Definition = None
        self.WatermarkSet = None
        self.MosaicSet = None
        self.HeadTailSet = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("MosaicSet") is not None:
            self.MosaicSet = []
            for item in params.get("MosaicSet"):
                obj = MosaicInput()
                obj._deserialize(item)
                self.MosaicSet.append(obj)
        if params.get("HeadTailSet") is not None:
            self.HeadTailSet = []
            for item in params.get("HeadTailSet"):
                obj = HeadTailTaskInput()
                obj._deserialize(item)
                self.HeadTailSet.append(obj)
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTemplate(AbstractModel):
    """Transcoding template details

    """

    def __init__(self):
        """
        :param Definition: Unique ID of transcoding template.\n        :type Definition: str\n        :param Container: Container. Valid values: mp4, flv, hls, mp3, flac, ogg.\n        :type Container: str\n        :param Name: Transcoding template name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Name: str\n        :param Comment: Template description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Comment: str\n        :param Type: Template type. Valid values:
<li>Preset: preset template;</li>
<li>Custom: custom template.</li>\n        :type Type: str\n        :param RemoveVideo: Whether to remove video data. Valid values:
<li>0: retain;</li>
<li>1: remove.</li>\n        :type RemoveVideo: int\n        :param RemoveAudio: Whether to remove audio data. Valid values:
<li>0: retain;</li>
<li>1: remove.</li>\n        :type RemoveAudio: int\n        :param VideoTemplate: Video stream configuration parameter. This field is valid only when `RemoveVideo` is 0.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VideoTemplate: :class:`tencentcloud.vod.v20180717.models.VideoTemplateInfo`\n        :param AudioTemplate: Audio stream configuration parameter. This field is valid only when `RemoveAudio` is 0.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioTemplate: :class:`tencentcloud.vod.v20180717.models.AudioTemplateInfo`\n        :param TEHDConfig: TESHD transcoding parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TEHDConfig: :class:`tencentcloud.vod.v20180717.models.TEHDConfig`\n        :param ContainerType: Container filter. Valid values:
<li>Video: video container that can contain both video stream and audio stream;</li>
<li>PureAudio: audio container that can contain only audio stream.</li>\n        :type ContainerType: str\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.Type = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.ContainerType = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Type = params.get("Type")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        self.ContainerType = params.get("ContainerType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransitionOpertion(AbstractModel):
    """Transition operation

    """

    def __init__(self):
        """
        :param Type: Transition type. Valid values:
<ul>
<li>Video image transition operation, which is used for transition with video image between two video segments:
<ul>
<li>ImageFadeInFadeOut: video image fade-in/fade-out.</li>
<li>BowTieHorizontal: horizontal bow.</li>
<li>BowTieVertical: vertical bow.</li>
<li>ButterflyWaveScrawler: waggling.</li>
<li>Cannabisleaf: maple leaf.</li>
<li> Circle: curved circling.</li>
<li>CircleCrop: circle gathering.</li>
<li>Circleopen: elliptic gathering.</li>
<li>Crosswarp: horizontal warping.</li>
<li>Cube: cube.</li>
<li>DoomScreenTransition: curtain.</li>
<li>Doorway: doorway.</li>
<li>Dreamy: wave.</li>
<li>DreamyZoom: horizontal gathering.</li>
<li>FilmBurn: evening glow.</li>
<li>GlitchMemories: joggling.</li>
<li>Heart: heart.</li>
<li>InvertedPageCurl: page turning.</li>
<li>Luma: corroding.</li>
<li>Mosaic: grid.</li>
<li>Pinwheel: pinwheel.</li>
<li>PolarFunction: elliptic diffusing.</li>
<li>PolkaDotsCurtain: curved diffusing.</li>
<li>Radial: radar scan.</li>
<li>RotateScaleFade: vertical rotating.</li>
<li>Squeeze: vertical gathering.</li>
<li>Swap: zooming in.</li>
<li>Swirl: swirling.</li>
<li>UndulatingBurnOutSwirl: water spreading.</li>
<li>Windowblinds: blinds.</li>
<li>WipeDown: collapsing down.</li>
<li>WipeLeft: collapsing to the left.</li>
<li>WipeRight: collapsing to the right.</li>
<li>WipeUp: collapsing up.</li>
<li>ZoomInCircles: ripples.</li>
</ul>
</li>
<li>Audio transition operation, which is used for transition between two audio segments:
<ul>
<li>AudioFadeInFadeOut: audio fade-in/fade-out.</li>
</ul>
</li>
</ul>\n        :type Type: str\n        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlSignatureAuthPolicy(AbstractModel):
    """Key hotlink protection information for generating the signature

    """

    def __init__(self):
        """
        :param Status: [Key hotlink protection](https://intl.cloud.tencent.com/document/product/266/33986) status. Valid values:
<li>Enabled</li>
<li>Disabled</li>\n        :type Status: str\n        :param EncryptedKey: The key for generating the signature of [key hotlink protection](https://intl.cloud.tencent.com/document/product/266/33986)\n        :type EncryptedKey: str\n        """
        self.Status = None
        self.EncryptedKey = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.EncryptedKey = params.get("EncryptedKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineAsrTextReviewTemplateInfo(AbstractModel):
    """Control parameter of custom speech audit task

    """

    def __init__(self):
        """
        :param Switch: Switch of custom speech audit task. Valid values:
<li>ON: enables custom speech audit task;</li>
<li>OFF: disables custom speech audit task.</li>\n        :type Switch: str\n        :param LabelSet: Custom speech filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for custom speech keywords.
There can be up to 10 tags, each with a length limit of 16 characters.\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineAsrTextReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of custom speech audit task

    """

    def __init__(self):
        """
        :param Switch: Switch of custom speech audit task. Valid values:
<li>ON: enables custom speech audit task;</li>
<li>OFF: disables custom speech audit task.</li>\n        :type Switch: str\n        :param LabelSet: Custom speech filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for custom speech keywords.
There can be up to 10 tags, each with a length limit of 16 characters.\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineConfigureInfo(AbstractModel):
    """Control parameter of custom audit task

    """

    def __init__(self):
        """
        :param FaceReviewInfo: Control parameter of custom figure audit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FaceReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineFaceReviewTemplateInfo`\n        :param AsrReviewInfo: Control parameter of custom speech audit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineAsrTextReviewTemplateInfo`\n        :param OcrReviewInfo: Control parameter of custom text audit.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineOcrTextReviewTemplateInfo`\n        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfo()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineConfigureInfoForUpdate(AbstractModel):
    """Control parameter of custom audit task.

    """

    def __init__(self):
        """
        :param FaceReviewInfo: Control parameter of custom figure audit.\n        :type FaceReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineFaceReviewTemplateInfoForUpdate`\n        :param AsrReviewInfo: Control parameter of custom speech audit.\n        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineAsrTextReviewTemplateInfoForUpdate`\n        :param OcrReviewInfo: Control parameter of custom text audit.\n        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineOcrTextReviewTemplateInfoForUpdate`\n        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfoForUpdate()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineFaceReviewTemplateInfo(AbstractModel):
    """Control parameter of custom figure audit task

    """

    def __init__(self):
        """
        :param Switch: Switch of custom figure audit task. Valid values:
<li>ON: enables custom figure audit task;</li>
<li>OFF: disables custom figure audit task.</li>\n        :type Switch: str\n        :param LabelSet: Custom figure filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for the custom figure library.
There can be up to 10 tags, each with a length limit of 16 characters.\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 97 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 95 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineFaceReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of custom figure audit task.

    """

    def __init__(self):
        """
        :param Switch: Switch of custom figure audit task. Valid values:
<li>ON: enables custom figure audit task;</li>
<li>OFF: disables custom figure audit task.</li>\n        :type Switch: str\n        :param LabelSet: Custom figure filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for the custom figure library.
There can be up to 10 tags, each with a length limit of 16 characters.\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineOcrTextReviewTemplateInfo(AbstractModel):
    """Control parameter of custom text audit task

    """

    def __init__(self):
        """
        :param Switch: Switch of custom text audit task. Valid values:
<li>ON: enables custom text audit task;</li>
<li>OFF: disables custom text audit task.</li>\n        :type Switch: str\n        :param LabelSet: Custom text filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for custom text keywords.
There can be up to 10 tags, each with a length limit of 16 characters.\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. If this parameter is left empty, 100 will be used by default. Value range: 0-100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. If this parameter is left empty, 75 will be used by default. Value range: 0-100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineOcrTextReviewTemplateInfoForUpdate(AbstractModel):
    """Control parameter of custom text audit task.

    """

    def __init__(self):
        """
        :param Switch: Switch of custom text audit task. Valid values:
<li>ON: enables custom text audit task;</li>
<li>OFF: disables custom text audit task.</li>\n        :type Switch: str\n        :param LabelSet: Custom text filter tag. If an audit result contains the selected tag, it will be returned; if the filter tag is empty, all audit results will be returned. To use the tag filtering feature, you need to add the corresponding tag when adding materials for custom text keywords.
There can be up to 10 tags, each with a length limit of 16 characters.\n        :type LabelSet: list of str\n        :param BlockConfidence: Threshold score for violation. If this score is reached or exceeded during intelligent audit, it will be deemed that a suspected violation has occurred. Value range: 0–100.\n        :type BlockConfidence: int\n        :param ReviewConfidence: Threshold score for human audit. If this score is reached or exceeded during intelligent audit, human audit will be considered necessary. Value range: 0–100.\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTemplateInfo(AbstractModel):
    """Video stream configuration parameter

    """

    def __init__(self):
        """
        :param Codec: Video stream encoder. Valid values:
<li>libx264: H.264</li>
<li>libx265: H.265</li>
<li>av1: AOMedia Video 1</li>
Currently, a resolution within 640x480 must be specified for H.265. and the `av1` container only supports mp4.\n        :type Codec: str\n        :param Fps: Video frame rate in Hz. Value range: [0,100].
If the value is 0, the frame rate will be the same as that of the source video.\n        :type Fps: int\n        :param Bitrate: Bitrate of video stream in Kbps. Value range: 0 and [128, 35,000].
If the value is 0, the bitrate of the video will be the same as that of the source video.\n        :type Bitrate: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>
Default value: open.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResolutionAdaptive: str\n        :param Width: Maximum value of the width (or long side) of a video stream in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of a video stream in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>
Default value: 0.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Height: int\n        :param FillType: Fill type, the way of processing a screenshot when the configured aspect ratio is different from that of the source video. Valid values:
<li>stretch: stretches the video image frame by frame to fill the screen. The video image may become "squashed" or "stretched" after transcoding.</li>
<li>black: fills the uncovered area with black color, without changing the image's aspect ratio.</li>
<li>white: fills the uncovered area with white color, without changing the image's aspect ratio.</li>
<li>gauss: applies Gaussian blur to the uncovered area, without changing the image's aspect ratio.</li>
Default value: black\n        :type FillType: str\n        :param Vcrf: Video Constant Rate Factor (CRF). Value range: 1-51.
If this parameter is specified, CRF will be used to control video bitrate for transcoding and the original video bitrate will not be used.
We don’t recommend specifying this parameter unless you have special requirements.\n        :type Vcrf: int\n        :param Gop: I-frame interval in frames. Valid values: 0 and 1-100000.
When this parameter is set to 0 or left empty, `Gop` will be automatically set.\n        :type Gop: int\n        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.FillType = None
        self.Vcrf = None
        self.Gop = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.FillType = params.get("FillType")
        self.Vcrf = params.get("Vcrf")
        self.Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTemplateInfoForUpdate(AbstractModel):
    """Video stream configuration parameter

    """

    def __init__(self):
        """
        :param Codec: Video stream encoder. Valid values:
<li>libx264: H.264</li>
<li>libx265: H.265</li>
<li>av1: AOMedia Video 1</li>
Currently, a resolution within 640x480 must be specified for H.265. and the `av1` container only supports mp4.\n        :type Codec: str\n        :param Fps: Video frame rate in Hz. Value range: [0,100].
If the value is 0, the frame rate will be the same as that of the source video.\n        :type Fps: int\n        :param Bitrate: Bitrate of video stream in Kbps. Value range: 0 and [128, 35,000].
If the value is 0, the bitrate of the video will be the same as that of the source video.\n        :type Bitrate: int\n        :param ResolutionAdaptive: Resolution adaption. Valid values:
<li>open: enabled. In this case, `Width` represents the long side of a video, while `Height` the short side;</li>
<li>close: disabled. In this case, `Width` represents the width of a video, while `Height` the height.</li>\n        :type ResolutionAdaptive: str\n        :param Width: Maximum value of the width (or long side) of a video stream in px. Value range: 0 and [128, 4,096].
<li>If both `Width` and `Height` are 0, the resolution will be the same as that of the source video;</li>
<li>If `Width` is 0, but `Height` is not 0, `Width` will be proportionally scaled;</li>
<li>If `Width` is not 0, but `Height` is 0, `Height` will be proportionally scaled;</li>
<li>If both `Width` and `Height` are not 0, the custom resolution will be used.</li>\n        :type Width: int\n        :param Height: Maximum value of the height (or short side) of a video stream in px. Value range: 0 and [128, 4,096].\n        :type Height: int\n        :param FillType: Fill type. "Fill" refers to the way of processing a screenshot when its aspect ratio is different from that of the source video. Valid values:
<li>stretch: stretches video image frame by frame to fill the screen. The video image may become "squashed" or "stretched" after transcoding.</li>
<li>black: fills the uncovered area with black color, without changing the image's aspect ratio.</li>
<li>white: fills the uncovered area with white color, without changing the image's aspect ratio.</li>
<li>gauss: applies Gaussian blur to the uncovered area, without changing the image's aspect ratio.</li>\n        :type FillType: str\n        :param Vcrf: Video Constant Rate Factor (CRF). Value range: 0-51. This parameter will be disabled if you enter 0.
We don’t recommend specifying this parameter unless you have special requirements.\n        :type Vcrf: int\n        :param Gop: I-frame interval in frames. Valid values: 0 and 1-100000.
When this parameter is set to 0 or left empty, `Gop` will be automatically set.\n        :type Gop: int\n        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.FillType = None
        self.Vcrf = None
        self.Gop = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.FillType = params.get("FillType")
        self.Vcrf = params.get("Vcrf")
        self.Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTrackItem(AbstractModel):
    """Video segment information of video track.

    """

    def __init__(self):
        """
        :param SourceMedia: Source of media material for video segment, which can be:
<li>ID of VOD media files</li>
<li>Download URL of other media files.</li>
Note: when a download URL of other media files is used as the material source and access control (such as hotlink protection) is enabled, the URL needs to carry access control parameters (such as hotlink protection signature).\n        :type SourceMedia: str\n        :param SourceMediaStartTime: Start time of video segment in material file in seconds. Default value: 0.\n        :type SourceMediaStartTime: float\n        :param Duration: Video segment duration in seconds. By default, the length of the video material will be used, which means that the entire material will be captured. If the source file is an image, `Duration` needs to be greater than 0.\n        :type Duration: float\n        :param CoordinateOrigin: Video origin position. Valid values:
<li> Center: the origin of coordinates is the center position, such as the center of canvas.</li>
Default value: Center.\n        :type CoordinateOrigin: str\n        :param XPos: The horizontal position of the origin of the video segment relative to the origin of the canvas. % and px formats are supported:
<li>If the string ends in %, the `XPos` of the video segment will be at the position of the specified percentage of the canvas width; for example, `10%` means that `XPos` is 10% of the canvas width.</li>
<li>If the string ends in px, the `XPos` of the video segment will be in px; for example, `100px` means that `XPos` is 100 px.</li>
Default value: 0 px.\n        :type XPos: str\n        :param YPos: The vertical position of the origin of the video segment relative to the origin of the canvas. % and px formats are supported:
<li>If the string ends in %, the `YPos` of the video segment will be at the position of the specified percentage of the canvas height; for example, `10%` means that `YPos` is 10% of the canvas height.</li>
<li>If the string ends in px, the `YPos` of the video segment will be in px; for example, `100px` means that `YPos` is 100 px.</li>
Default value: 0 px.\n        :type YPos: str\n        :param Width: Video segment width. % and px formats are supported:
<li>If the string ends in %, the `Width` of the video segment will be the specified percentage of the canvas width; for example, `10%` means that `Width` is 10% of the canvas width.</li>
<li>If the string ends in px, the `Width` of the video segment will be in px; for example, `100px` means that `Width` is 100 px.</li>
<li>If both `Width` and `Height` are empty, then they will be the `Width` and `Height` of the video material, respectively.</li>
<li>If `Width` is empty, but `Height` is not empty, `Width` will be proportionally scaled.</li>
<li>If `Width` is not empty, but `Height` is empty, `Height` will be proportionally scaled.</li>\n        :type Width: str\n        :param Height: Video segment height. % and px formats are supported:
<li>If the string ends in %, the `Height` of the video segment will be the specified percentage of the canvas height; for example, `10%` means that `Height` is 10% of the canvas height;
</li><li>If the string ends in px, the `Height` of the video segment will be in px; for example, `100px` means that `Height` is 100 px.</li>
<li>If both `Width` and `Height` are empty, then they will be the `Width` and `Height` of the video material, respectively.</li>
<li>If `Width` is empty, but `Height` is not empty, `Width` will be proportionally scaled.</li>
<li>If `Width` is not empty, but `Height` is empty, `Height` will be proportionally scaled.</li>\n        :type Height: str\n        :param ImageOperations: Operation on video image such as image rotation.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageOperations: list of ImageTransform\n        :param AudioOperations: Operation on audio such as muting.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioOperations: list of AudioTransform\n        """
        self.SourceMedia = None
        self.SourceMediaStartTime = None
        self.Duration = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.ImageOperations = None
        self.AudioOperations = None


    def _deserialize(self, params):
        self.SourceMedia = params.get("SourceMedia")
        self.SourceMediaStartTime = params.get("SourceMediaStartTime")
        self.Duration = params.get("Duration")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("ImageOperations") is not None:
            self.ImageOperations = []
            for item in params.get("ImageOperations"):
                obj = ImageTransform()
                obj._deserialize(item)
                self.ImageOperations.append(obj)
        if params.get("AudioOperations") is not None:
            self.AudioOperations = []
            for item in params.get("AudioOperations"):
                obj = AudioTransform()
                obj._deserialize(item)
                self.AudioOperations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkCycleConfigForUpdate(AbstractModel):
    """Watermark cycle configuration.

    """

    def __init__(self):
        """
        :param StartTime: Playback time point in seconds when a watermark appears in a video for the first time.\n        :type StartTime: float\n        :param DisplayDuration: Display duration of a watermark in a watermark cycle in seconds.\n        :type DisplayDuration: float\n        :param CycleDuration: Duration of a watermark cycle in seconds.
If 0 is entered, a watermark will last for only one cycle (i.e., visible for `DisplayDuration` seconds throughout the video).\n        :type CycleDuration: float\n        """
        self.StartTime = None
        self.DisplayDuration = None
        self.CycleDuration = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.DisplayDuration = params.get("DisplayDuration")
        self.CycleDuration = params.get("CycleDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkInput(AbstractModel):
    """Watermark parameter type of video processing task

    """

    def __init__(self):
        """
        :param Definition: Watermarking template ID.\n        :type Definition: int\n        :param TextContent: Text content, which contains up to 100 characters. Set this parameter only when the watermark type is text.
VOD does not support adding text watermarks on screenshots.\n        :type TextContent: str\n        :param SvgContent: SVG content, which contains up to 2,000,000 characters. Set this parameter only when the watermark type is SVG.
VOD does not support adding SVG watermarks on screenshots.\n        :type SvgContent: str\n        :param StartTimeOffset: Start time offset of a watermark in seconds. If this parameter is left blank or 0 is entered, the watermark will appear upon the first video frame.
<li>If this parameter is left blank or 0 is entered, the watermark will appear upon the first video frame;</li>
<li>If this value is greater than 0 (e.g., n), the watermark will appear at second n after the first video frame;</li>
<li>If this value is smaller than 0 (e.g., -n), the watermark will appear at second n before the last video frame.</li>\n        :type StartTimeOffset: float\n        :param EndTimeOffset: End time offset of a watermark in seconds.
<li>If this parameter is left blank or 0 is entered, the watermark will exist till the last video frame;</li>
<li>If this value is greater than 0 (e.g., n), the watermark will exist till second n;</li>
<li>If this value is smaller than 0 (e.g., -n), the watermark will exist till second n before the last video frame.</li>\n        :type EndTimeOffset: float\n        """
        self.Definition = None
        self.TextContent = None
        self.SvgContent = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.TextContent = params.get("TextContent")
        self.SvgContent = params.get("SvgContent")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkTemplate(AbstractModel):
    """Watermarking template details

    """

    def __init__(self):
        """
        :param Definition: Unique ID of watermarking template.\n        :type Definition: int\n        :param Type: Watermark type. Valid values:
<li>image: image watermark;</li>
<li>text: text watermark.</li>\n        :type Type: str\n        :param Name: Watermarking template name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Name: str\n        :param Comment: Template description.\n        :type Comment: str\n        :param XPos: Horizontal position of the origin of the watermark image relative to the origin of the video.
<li>If the string ends in %, the `Left` edge of the watermark will be at the position of the specified percentage of the video width; for example, `10%` means that the `Left` edge is at 10% of the video width;</li>
<li>If the string ends in px, the `Left` edge of the watermark will be at the position of the specified px of the video width; for example, `100px` means that the `Left` edge is at the position of 100 px.</li>\n        :type XPos: str\n        :param YPos: Vertical position of the origin of the watermark image relative to the origin of the video.
<li>If the string ends in %, the `Top` edge of the watermark will beat the position of the specified percentage of the video height; for example, `10%` means that the `Top` edge is at 10% of the video height;</li>
<li>If the string ends in px, the `Top` edge of the watermark will be at the position of the specified px of the video height; for example, `100px` means that the `Top` edge is at the position of 100 px.</li>\n        :type YPos: str\n        :param ImageTemplate: Image watermarking template. This field is valid only when `Type` is `image`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ImageTemplate: :class:`tencentcloud.vod.v20180717.models.ImageWatermarkTemplate`\n        :param TextTemplate: Text watermarking template. This field is valid only when `Type` is `text`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TextTemplate: :class:`tencentcloud.vod.v20180717.models.TextWatermarkTemplateInput`\n        :param SvgTemplate: SVG watermarking template. This field is valid when `Type` is `svg`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SvgTemplate: :class:`tencentcloud.vod.v20180717.models.SvgWatermarkInput`\n        :param CreateTime: Creation time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of template in [ISO date format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I).\n        :type UpdateTime: str\n        :param CoordinateOrigin: Origin position. Valid values:
<li>topLeft: the origin of coordinates is in the top-left corner of the video, and the origin of the watermark is in the top-left corner of the image or text;</li>
<li>topRight: the origin of coordinates is in the top-right corner of the video, and the origin of the watermark is in the top-right corner of the image or text;</li>
<li>bottomLeft: the origin of coordinates is in the bottom-left corner of the video, and the origin of the watermark is in the bottom-left corner of the image or text;</li>
<li>bottomRight: the origin of coordinates is in the bottom-right corner of the video, and the origin of the watermark is in the bottom-right corner of the image or text.</li>\n        :type CoordinateOrigin: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CoordinateOrigin = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkTemplate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeChatMiniProgramPublishRequest(AbstractModel):
    """WeChatMiniProgramPublish request structure.

    """

    def __init__(self):
        """
        :param FileId: Media file ID.\n        :type FileId: str\n        :param SourceDefinition: ID of the transcoding template corresponding to the published video. 0 represents the source video.\n        :type SourceDefinition: int\n        :param SubAppId: [Subapplication](https://intl.cloud.tencent.com/document/product/266/14574?from_cn_redirect=1) ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.\n        :type SubAppId: int\n        """
        self.FileId = None
        self.SourceDefinition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.SourceDefinition = params.get("SourceDefinition")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeChatMiniProgramPublishResponse(AbstractModel):
    """WeChatMiniProgramPublish response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class WechatMiniProgramPublishTask(AbstractModel):
    """Release on WeChat Mini Program task information

    """

    def __init__(self):
        """
        :param TaskId: Task ID.\n        :type TaskId: str\n        :param Status: Task status. Valid values:
WAITING: waiting;
PROCESSING: processing;
FINISH: completed.\n        :type Status: str\n        :param ErrCode: Error code
<li>0: success;</li>
<li>Other values: failure.</li>\n        :type ErrCode: int\n        :param Message: Error message.\n        :type Message: str\n        :param FileId: ID of published video file.\n        :type FileId: str\n        :param SourceDefinition: ID of the transcoding template corresponding to the published video. 0 represents the source video.\n        :type SourceDefinition: int\n        :param PublishResult: Status of video release on WeChat Mini Program. Valid values:
<li>Pass: successfully published;</li>
<li>Failed: failed to publish;</li>
<li>Rejected: rejected.</li>\n        :type PublishResult: str\n        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.SourceDefinition = None
        self.PublishResult = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.SourceDefinition = params.get("SourceDefinition")
        self.PublishResult = params.get("PublishResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WechatMiniProgramPublishTaskInput(AbstractModel):
    """Type of a release on WeChat Mini Program task

    """

    def __init__(self):
        """
        :param SourceDefinition: ID of the transcoding template corresponding to the published video. 0 represents the source video.\n        :type SourceDefinition: int\n        """
        self.SourceDefinition = None


    def _deserialize(self, params):
        self.SourceDefinition = params.get("SourceDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WechatPublishTask(AbstractModel):
    """Release on WeChat task information

    """

    def __init__(self):
        """
        :param TaskId: Task ID.\n        :type TaskId: str\n        :param Status: Task status. Valid values:
WAITING: waiting;
PROCESSING: processing;
FINISH: completed.\n        :type Status: str\n        :param ErrCode: Error code
<li>0: success;</li>
<li>Other values: failure.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ErrCode: int\n        :param Message: Error message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        :param FileId: ID of published video file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FileId: str\n        :param Definition: Release on WeChat template ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Definition: int\n        :param SourceDefinition: ID of the transcoding template corresponding to the published video. 0 represents the source video.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SourceDefinition: int\n        :param WechatStatus: Release on WeChat status. Valid values:
<li>FAIL: failure;</li>
<li>SUCCESS: success;</li>
<li>AUDITNOTPASS: rejected</li>
<li>NOTTRIGGERED: release on WeChat not initiated yet.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WechatStatus: str\n        :param WechatVid: WeChat `Vid`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WechatVid: str\n        :param WechatUrl: WeChat address.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WechatUrl: str\n        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.Definition = None
        self.SourceDefinition = None
        self.WechatStatus = None
        self.WechatVid = None
        self.WechatUrl = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.Definition = params.get("Definition")
        self.SourceDefinition = params.get("SourceDefinition")
        self.WechatStatus = params.get("WechatStatus")
        self.WechatVid = params.get("WechatVid")
        self.WechatUrl = params.get("WechatUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        