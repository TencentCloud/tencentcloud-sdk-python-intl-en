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


class Canvas(AbstractModel):
    """Mixed stream canvas parameter

    """

    def __init__(self):
        r"""
        :param LayoutParams: Width and height of the mixed stream canvas
        :type LayoutParams: :class:`tencentcloud.tiw.v20190919.models.LayoutParams`
        :param BackgroundColor: Background color, which is black by default. Its format is RGB. for example, "#FF0000" for the red color.
        :type BackgroundColor: str
        """
        self.LayoutParams = None
        self.BackgroundColor = None


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        self.BackgroundColor = params.get("BackgroundColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Concat(AbstractModel):
    """Real-time recording video splicing parameter

    """

    def __init__(self):
        r"""
        :param Enabled: Whether to enable the video splicing feature
If the video splicing feature is enabled, the real-time recording service will splice multiple video clips resulting from the pause into one video.
        :type Enabled: bool
        :param Image: Download address of the padding image used during video splicing. If it is not specified, a pure black image is used by default.
        :type Image: str
        """
        self.Enabled = None
        self.Image = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTranscodeRequest(AbstractModel):
    """CreateTranscode request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param Url: Address of the file for transcoding
        :type Url: str
        :param IsStaticPPT: Whether the PowerPoint file is static. The default value is False.
If IsStaticPPT is False, documents with the .ppt or .pptx extension will be dynamically transcoded to HTML5 pages, and documents with other extensions will be statically transcoded to images. If IsStaticPPT is True, documents with any extensions will be statically transcoded to images.
        :type IsStaticPPT: bool
        :param MinResolution: Minimum resolution of the transcoded document. If no value or null is specified for it or the resolution format is invalid, the original document resolution is used.

 
        :type MinResolution: str
        :param ThumbnailResolution: Resolution of the thumbnail generated for the dynamically transcoded PowerPoint file. If no value or null is specified for it or the resolution format is invalid, no thumbnail will be generated. The resolution format is the same as that of MinResolution.

For static transcoding, this parameter does not work.
        :type ThumbnailResolution: str
        :param CompressFileType: Compression format of the transcoded file. If no value or null is specified for it or the specified format is invalid, no compression file will be generated. Currently, the following compression formats are supported:

`zip`: generates a .zip compression package.
`tar.gz: generates a .tar.gz compression package.
        :type CompressFileType: str
        """
        self.SdkAppId = None
        self.Url = None
        self.IsStaticPPT = None
        self.MinResolution = None
        self.ThumbnailResolution = None
        self.CompressFileType = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Url = params.get("Url")
        self.IsStaticPPT = params.get("IsStaticPPT")
        self.MinResolution = params.get("MinResolution")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileType = params.get("CompressFileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTranscodeResponse(AbstractModel):
    """CreateTranscode response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Unique ID of the document transcoding task, which is used to query the task progress and transcoding result
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CustomLayout(AbstractModel):
    """Custom mixed stream layout parameter

    """

    def __init__(self):
        r"""
        :param Canvas: Mixed stream canvas parameter
        :type Canvas: :class:`tencentcloud.tiw.v20190919.models.Canvas`
        :param InputStreamList: Stream layout. The layout of each stream cannot exceed the canvas area.
        :type InputStreamList: list of StreamLayout
        """
        self.Canvas = None
        self.InputStreamList = None


    def _deserialize(self, params):
        if params.get("Canvas") is not None:
            self.Canvas = Canvas()
            self.Canvas._deserialize(params.get("Canvas"))
        if params.get("InputStreamList") is not None:
            self.InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = StreamLayout()
                obj._deserialize(item)
                self.InputStreamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordCallbackRequest(AbstractModel):
    """DescribeOnlineRecordCallback request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the application
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordCallbackResponse(AbstractModel):
    """DescribeOnlineRecordCallback response structure.

    """

    def __init__(self):
        r"""
        :param Callback: Callback address of the real-time recording event. If no callback address is set, this field is null.
        :type Callback: str
        :param CallbackKey: Authentication key of the real-time recording callback
        :type CallbackKey: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeOnlineRecordRequest(AbstractModel):
    """DescribeOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param TaskId: ID of the real-time recording task
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordResponse(AbstractModel):
    """DescribeOnlineRecord response structure.

    """

    def __init__(self):
        r"""
        :param FinishReason: Recording stop reason
- AUTO: recording automatically stops because no upstream audio/video or whiteboard operation occurs in the room for a long time.
- USER_CALL: the API for stopping recording is called.
- EXCEPTION: an exception occurred during recording.
        :type FinishReason: str
        :param TaskId: ID of the recording task to be queried.
        :type TaskId: str
        :param Status: Recording task status
- PREPARED: preparing
- RECORDING: recording
- PAUSED: recording is paused.
- STOPPED: recording is stopped, and the recorded video is being processed and uploaded.
- FINISHED: the recorded video has been processed and uploaded, and the recording result is generated.
        :type Status: str
        :param RoomId: Room ID
        :type RoomId: int
        :param GroupId: Group ID of the whiteboard
        :type GroupId: str
        :param RecordUserId: ID of the recording user
        :type RecordUserId: str
        :param RecordStartTime: Actual recording start time, which is a UNIX timestamp in seconds
        :type RecordStartTime: int
        :param RecordStopTime: Actual recording stop time, which is a UNIX timestamp in seconds
        :type RecordStopTime: int
        :param TotalTime: Total video playback duration, in milliseconds
        :type TotalTime: int
        :param ExceptionCnt: Number of exceptions during recording
        :type ExceptionCnt: int
        :param OmittedDurations: Duration to be deleted in the spliced video. This parameter is valid only when the video splicing feature is enabled.
        :type OmittedDurations: list of OmittedDuration
        :param VideoInfos: List of recorded videos
        :type VideoInfos: list of VideoInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FinishReason = None
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.GroupId = None
        self.RecordUserId = None
        self.RecordStartTime = None
        self.RecordStopTime = None
        self.TotalTime = None
        self.ExceptionCnt = None
        self.OmittedDurations = None
        self.VideoInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.RecordUserId = params.get("RecordUserId")
        self.RecordStartTime = params.get("RecordStartTime")
        self.RecordStopTime = params.get("RecordStopTime")
        self.TotalTime = params.get("TotalTime")
        self.ExceptionCnt = params.get("ExceptionCnt")
        if params.get("OmittedDurations") is not None:
            self.OmittedDurations = []
            for item in params.get("OmittedDurations"):
                obj = OmittedDuration()
                obj._deserialize(item)
                self.OmittedDurations.append(obj)
        if params.get("VideoInfos") is not None:
            self.VideoInfos = []
            for item in params.get("VideoInfos"):
                obj = VideoInfo()
                obj._deserialize(item)
                self.VideoInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTranscodeCallbackRequest(AbstractModel):
    """DescribeTranscodeCallback request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the application
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeCallbackResponse(AbstractModel):
    """DescribeTranscodeCallback response structure.

    """

    def __init__(self):
        r"""
        :param Callback: Document transcoding callback address
        :type Callback: str
        :param CallbackKey: Authentication key of the document transcoding callback
        :type CallbackKey: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeRequest(AbstractModel):
    """DescribeTranscode request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param TaskId: Unique ID of the document transcoding task
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeResponse(AbstractModel):
    """DescribeTranscode response structure.

    """

    def __init__(self):
        r"""
        :param Pages: Total number of document pages
        :type Pages: int
        :param Progress: Transcoding progress. Value range: 0 to 100
        :type Progress: int
        :param Resolution: Document resolution
        :type Resolution: str
        :param ResultUrl: URL of the transcoding result
Dynamic transcoding: link of the HTML5 page transcoded from a PowerPoint file
Static transcoding: URL prefix of the image transcoded for each document page. For example, if the URL prefix is `http://example.com/g0jb42ps49vtebjshilb/`, the image URL of the first page is
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`, and so on.
        :type ResultUrl: str
        :param Status: Current task state
- QUEUED: queuing for transcoding
- PROCESSING: transcoding is in progress
- FINISHED: transcoded
        :type Status: str
        :param TaskId: Unique ID of the transcoding task
        :type TaskId: str
        :param Title: Document name
        :type Title: str
        :param ThumbnailUrl: URL prefix of the thumbnail. If the URL prefix is `http://example.com/g0jb42ps49vtebjshilb/ `, the thumbnail URL for the first page of the dynamically transcoded PowerPoint file is
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`, and so on.

If the document transcoding request carries the ThumbnailResolution parameter and the transcoding type is dynamic transcoding, this parameter is not null. In other cases, this parameter is null.
        :type ThumbnailUrl: str
        :param ThumbnailResolution: Resolution of the thumbnail generated for dynamic transcoding
        :type ThumbnailResolution: str
        :param CompressFileUrl: URL for downloading the transcoded and compressed file. If `CompressFileType` carried in the document transcoding request is null or is not a supported compression format, this parameter is null.
        :type CompressFileUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Pages = None
        self.Progress = None
        self.Resolution = None
        self.ResultUrl = None
        self.Status = None
        self.TaskId = None
        self.Title = None
        self.ThumbnailUrl = None
        self.ThumbnailResolution = None
        self.CompressFileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Pages = params.get("Pages")
        self.Progress = params.get("Progress")
        self.Resolution = params.get("Resolution")
        self.ResultUrl = params.get("ResultUrl")
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        self.Title = params.get("Title")
        self.ThumbnailUrl = params.get("ThumbnailUrl")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileUrl = params.get("CompressFileUrl")
        self.RequestId = params.get("RequestId")


class LayoutParams(AbstractModel):
    """Custom mixed stream layout parameter

    """

    def __init__(self):
        r"""
        :param Width: Stream image width. Value range: [2,3000]
        :type Width: int
        :param Height: Stream image height. Value range: [2,3000]
        :type Height: int
        :param X: Offset of the top point in the upper-left corner of the current image to the X axis of the top point in the upper-left corner of the canvas. Default value: 0. Value range: [0,3000].
        :type X: int
        :param Y: Offset of the top point in the upper-left corner of the current image to the Y axis of the top point in the upper-left corner of the canvas. Default value: 0. Value range: [0,3000].
        :type Y: int
        :param ZOrder: Z-axis position of the image. The default value is 0.
The Z axis determines the overlap sequence of images. The image with the largest z-axis value is at the top layer.
        :type ZOrder: int
        """
        self.Width = None
        self.Height = None
        self.X = None
        self.Y = None
        self.ZOrder = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.ZOrder = params.get("ZOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixStream(AbstractModel):
    """Stream mixing configuration

    """

    def __init__(self):
        r"""
        :param Enabled: Whether stream mixing is enabled
        :type Enabled: bool
        :param DisableAudio: Whether audio stream mixing is disabled
        :type DisableAudio: bool
        :param ModelId: ID of the embedded mixed stream layout template. Valid values: 1 and 2. For more information on the differences of both values, see the sample embedded mixed stream layout template.
If the Custom field is not specified, ModelId is required.
        :type ModelId: int
        :param TeacherId: ID of a teacher account
This field is valid only when ModelId is specified.
If you specify TeacherID for a user, the user's video stream will be displayed in the first image of the embedded template.
        :type TeacherId: str
        :param Custom: Custom mixed stream layout parameter
If this parameter is available, the ModelId and TeacherId fields will be ignored.
        :type Custom: :class:`tencentcloud.tiw.v20190919.models.CustomLayout`
        """
        self.Enabled = None
        self.DisableAudio = None
        self.ModelId = None
        self.TeacherId = None
        self.Custom = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.DisableAudio = params.get("DisableAudio")
        self.ModelId = params.get("ModelId")
        self.TeacherId = params.get("TeacherId")
        if params.get("Custom") is not None:
            self.Custom = CustomLayout()
            self.Custom._deserialize(params.get("Custom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OmittedDuration(AbstractModel):
    """Duration to be ignored in the spliced video

    """

    def __init__(self):
        r"""
        :param VideoTime: Offset of the paused time in the spliced video, in milliseconds
        :type VideoTime: int
        :param PauseTime: Recording pause timestamp, in milliseconds
        :type PauseTime: int
        :param ResumeTime: Recording resumption timestamp, in milliseconds
        :type ResumeTime: int
        """
        self.VideoTime = None
        self.PauseTime = None
        self.ResumeTime = None


    def _deserialize(self, params):
        self.VideoTime = params.get("VideoTime")
        self.PauseTime = params.get("PauseTime")
        self.ResumeTime = params.get("ResumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOnlineRecordRequest(AbstractModel):
    """PauseOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param TaskId: ID of the real-time recording task
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOnlineRecordResponse(AbstractModel):
    """PauseOnlineRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RecordControl(AbstractModel):
    """It specifies the global recording parameters and the recording parameters over a specific stream. For example, you can specify the streams you want to record and whether to record low-resolution videos only.

    """

    def __init__(self):
        r"""
        :param Enabled: It specifies whether to enable RecordControl. Valid values: true (yes); false (no).
        :type Enabled: bool
        :param DisableRecord: A global parameter generally used in conjunction with `StreamControls` that specifies whether to disable recording. Valid values:

true: no stream is recorded.
false: all streams are recorded. Default value: false.

The setting in this parameter is applied to all streams. However, if `StreamControls` is passed in, the parameters in `StreamControls` will take precedence.
        :type DisableRecord: bool
        :param DisableAudio: A global parameter generally used in conjunction with `StreamControls` that specifies whether to disable audio recording over all streams. Valid values:

true: no audio recording of any streams.
false: audio recording of all streams. Default value: false.

The setting in this parameter is applied to all streams. However, if `StreamControls` is passed in, the parameters in `StreamControls` will take precedence.
        :type DisableAudio: bool
        :param PullSmallVideo: A global parameter generally used in conjunction with `StreamControls` that specifies whether to record low-resolution videos only. Valid values:

true: only records low-resolution videos for all streams. Please ensure that the up-streaming end pushes the low-resolution videos. Otherwise, the recorded video may be black.
false: high-resolution video recording of all streams. Default value: false.

The setting in this parameter is applied to all streams. However, if `StreamControls` is passed in, the parameters in `StreamControls` will take precedence.
        :type PullSmallVideo: bool
        :param StreamControls: Parameters over specific streams, which take priority over global configurations. If it’s empty, all streams are recorded according to the global configurations. 
        :type StreamControls: list of StreamControl
        """
        self.Enabled = None
        self.DisableRecord = None
        self.DisableAudio = None
        self.PullSmallVideo = None
        self.StreamControls = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.DisableRecord = params.get("DisableRecord")
        self.DisableAudio = params.get("DisableAudio")
        self.PullSmallVideo = params.get("PullSmallVideo")
        if params.get("StreamControls") is not None:
            self.StreamControls = []
            for item in params.get("StreamControls"):
                obj = StreamControl()
                obj._deserialize(item)
                self.StreamControls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeOnlineRecordRequest(AbstractModel):
    """ResumeOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param TaskId: ID of the resumed real-time recording task
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeOnlineRecordResponse(AbstractModel):
    """ResumeOnlineRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetOnlineRecordCallbackKeyRequest(AbstractModel):
    """SetOnlineRecordCallbackKey request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the application
        :type SdkAppId: int
        :param CallbackKey: Authentication key for the real-time recording callback. It is a string that can have up to 64 characters. If an empty string is passed in, the existing callback authentication key will be deleted. For more information, please [see here](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1).
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackKeyResponse(AbstractModel):
    """SetOnlineRecordCallbackKey response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetOnlineRecordCallbackRequest(AbstractModel):
    """SetOnlineRecordCallback request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param Callback: Callback address of the real-time recording task result. If an empty string is passed in, the existing callback address will be deleted. The callback address only supports the HTTP or HTTPS protocol, so the callback address must start with `http://` or `https://`. For the callback format, please [see here](https://intl.cloud.tencent.com/document/product/1137/40258?from_cn_redirect=1).
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackResponse(AbstractModel):
    """SetOnlineRecordCallback response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetTranscodeCallbackKeyRequest(AbstractModel):
    """SetTranscodeCallbackKey request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the application
        :type SdkAppId: int
        :param CallbackKey: Authentication key for the document transcoding callback. It is a string that can have up to 64 characters. If an empty string is passed in, the existing callback authentication key will be deleted. For more information about callback authentication, please [see here](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1).
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTranscodeCallbackKeyResponse(AbstractModel):
    """SetTranscodeCallbackKey response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetTranscodeCallbackRequest(AbstractModel):
    """SetTranscodeCallback request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param Callback: Callback address for the document transcoding progress. If an empty string is passed in, the existing callback address will be deleted. The callback address only supports the HTTP or HTTPS protocol, so the callback address must start with `http://` or `https://`.
For more information about the callback format, please [see here](https://intl.cloud.tencent.com/document/product/1137/40260?from_cn_redirect=1).
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTranscodeCallbackResponse(AbstractModel):
    """SetTranscodeCallback response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartOnlineRecordRequest(AbstractModel):
    """StartOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param RoomId: ID of the room for recording. Value range: (1, 4294967295)
        :type RoomId: int
        :param RecordUserId: User ID used by the real-time recording service for entering a room. Its format is `tic_record_user_${RoomId}_${Random}`, where `${RoomId}` indicates the ID of the room for recording and `${Random}` is a random string.
The ID must be an unused ID in the SDK. The real-time recording service uses the user ID to enter the room for audio, video, and whiteboard recording. If this ID is already used in the SDK, the SDK and recording service will conflict, affecting the recording operation.
        :type RecordUserId: str
        :param RecordUserSig: Signature corresponding to RecordUserId
        :type RecordUserSig: str
        :param GroupId: (Disused) IM group ID of the whiteboard. By default, it is the same as the room ID.
        :type GroupId: str
        :param Concat: Real-time recording video splicing parameter
        :type Concat: :class:`tencentcloud.tiw.v20190919.models.Concat`
        :param Whiteboard: Real-time recording whiteboard parameter, such as the whiteboard width and height
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param MixStream: Real-time recording stream mixing parameter
Notes:
1. The stream mixing feature needs to be enabled separately. If you need the feature, contact TIW customer service.
2. To use the stream mixing feature, the Extras parameter is required and must contain "MIX_STREAM".
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param Extras: List of advanced features used
List of possible values:
MIX_STREAM - Stream mixing feature
        :type Extras: list of str
        :param AudioFileNeeded: Whether to return the audio-only recording file of different streams in the result callback. The file format is mp3.
        :type AudioFileNeeded: bool
        :param RecordControl: A group of real-time recording parameters. It specifies the streams to be recorded, whether to disable the audio recording, and whether to record only low-resolution videos, etc.
        :type RecordControl: :class:`tencentcloud.tiw.v20190919.models.RecordControl`
        """
        self.SdkAppId = None
        self.RoomId = None
        self.RecordUserId = None
        self.RecordUserSig = None
        self.GroupId = None
        self.Concat = None
        self.Whiteboard = None
        self.MixStream = None
        self.Extras = None
        self.AudioFileNeeded = None
        self.RecordControl = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.RecordUserId = params.get("RecordUserId")
        self.RecordUserSig = params.get("RecordUserSig")
        self.GroupId = params.get("GroupId")
        if params.get("Concat") is not None:
            self.Concat = Concat()
            self.Concat._deserialize(params.get("Concat"))
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("MixStream") is not None:
            self.MixStream = MixStream()
            self.MixStream._deserialize(params.get("MixStream"))
        self.Extras = params.get("Extras")
        self.AudioFileNeeded = params.get("AudioFileNeeded")
        if params.get("RecordControl") is not None:
            self.RecordControl = RecordControl()
            self.RecordControl._deserialize(params.get("RecordControl"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartOnlineRecordResponse(AbstractModel):
    """StartOnlineRecord response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: ID of the real-time recording task
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class StopOnlineRecordRequest(AbstractModel):
    """StopOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param TaskId: ID of the recording task to stop
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopOnlineRecordResponse(AbstractModel):
    """StopOnlineRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamControl(AbstractModel):
    """A group of parameters for recording over specified streams. It specifies whether to disable the audio recording and whether to record high-resolution or low-resolution videos.

    """

    def __init__(self):
        r"""
        :param StreamId: Video stream ID
Description of the possible video stream ID values:
1. `tic_record_user`: the whiteboard video stream
2. `tic_substream`: the auxiliary video stream
3. Specific user ID: the video stream of the specified user

The actual recording uses the prefix match of the video stream ID. The real stream becomes the specified stream once its ID prefix matches with the stream ID.
        :type StreamId: str
        :param DisableRecord: Whether to disable recording over the stream.

true: does not record this stream. This stream will not be included in the final recording file.
false: records this stream. This stream will be included in the final recording file.

Default value: false
        :type DisableRecord: bool
        :param DisableAudio: Whether to disable the audio recording of the stream.

true: does not record the audio of the stream. In the final recording file, this stream will be soundless.
false: the stream has both video and audio recording.

Default value: false
        :type DisableAudio: bool
        :param PullSmallVideo: Whether to only record low-resolution stream videos.

true: records only low-resolution videos. In this case, please make sure that the client pushes low-resolution videos upstream. Otherwise, the recorded video may be black. 
false: records only high-resolution videos.

Default value: false
        :type PullSmallVideo: bool
        """
        self.StreamId = None
        self.DisableRecord = None
        self.DisableAudio = None
        self.PullSmallVideo = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.DisableRecord = params.get("DisableRecord")
        self.DisableAudio = params.get("DisableAudio")
        self.PullSmallVideo = params.get("PullSmallVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamLayout(AbstractModel):
    """Stream layout parameter

    """

    def __init__(self):
        r"""
        :param LayoutParams: Stream layout configuration
        :type LayoutParams: :class:`tencentcloud.tiw.v20190919.models.LayoutParams`
        :param InputStreamId: Video stream ID
Description of the possible video stream ID values:
1. tic_record_user: the current picture is used to display the whiteboard video stream.
2. tic_substream: the current picture is used to display the auxiliary video stream.
3. Specific user ID: the current picture is used to display the video stream of a specific user.
4.Left empty: the current picture is vacant for new video stream.
        :type InputStreamId: str
        :param BackgroundColor: Background color in RGB format, such as "#FF0000" for red. The default color is black. 
        :type BackgroundColor: str
        :param FillMode: Video filling mode.

0: self-adaption mode. Scales the video proportionally to completely display it in the specified area. In this mode, there may be black bars.
1: full-screen mode. Scales the video to make it fill the entire specified area. In this mode, no black bars will appear, but the video may not be displayed fully.
        :type FillMode: int
        """
        self.LayoutParams = None
        self.InputStreamId = None
        self.BackgroundColor = None
        self.FillMode = None


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        self.InputStreamId = params.get("InputStreamId")
        self.BackgroundColor = params.get("BackgroundColor")
        self.FillMode = params.get("FillMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoInfo(AbstractModel):
    """Video information

    """

    def __init__(self):
        r"""
        :param VideoPlayTime: Video playback start time, in milliseconds
        :type VideoPlayTime: int
        :param VideoSize: Video size, in bytes
        :type VideoSize: int
        :param VideoFormat: Video format
        :type VideoFormat: str
        :param VideoDuration: Video playback duration, in milliseconds
        :type VideoDuration: int
        :param VideoUrl: Video file URL
        :type VideoUrl: str
        :param VideoId: Video file ID
        :type VideoId: str
        :param VideoType: Video stream type - 0: camera video - 1: screen-sharing video - 2: whiteboard video - 3: mixed stream video - 4: audio-only (mp3)
        :type VideoType: int
        :param UserId: ID of the user to which the camera video or screen-sharing video belongs (whiteboard video: null, mixed stream video: tic_mixstream_<Room ID>_<Mixed stream layout type>, auxiliary video: tic_substream_user ID)
        :type UserId: str
        :param Width: Width of the video resolution.
        :type Width: int
        :param Height: Height of the video resolution.
        :type Height: int
        """
        self.VideoPlayTime = None
        self.VideoSize = None
        self.VideoFormat = None
        self.VideoDuration = None
        self.VideoUrl = None
        self.VideoId = None
        self.VideoType = None
        self.UserId = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.VideoPlayTime = params.get("VideoPlayTime")
        self.VideoSize = params.get("VideoSize")
        self.VideoFormat = params.get("VideoFormat")
        self.VideoDuration = params.get("VideoDuration")
        self.VideoUrl = params.get("VideoUrl")
        self.VideoId = params.get("VideoId")
        self.VideoType = params.get("VideoType")
        self.UserId = params.get("UserId")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Whiteboard(AbstractModel):
    """Real-time recording whiteboard parameter, such as the whiteboard width and height

    """

    def __init__(self):
        r"""
        :param Width: Whiteboard video width in the real-time recording result. The default value is 1280.
        :type Width: int
        :param Height: Whiteboard video height in the real-time recording result. The default value is 960.
        :type Height: int
        :param InitParam: Whiteboard initialization parameter, which is passed through to the whiteboard SDK
        :type InitParam: str
        """
        self.Width = None
        self.Height = None
        self.InitParam = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.InitParam = params.get("InitParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        