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


class ApplicationItem(AbstractModel):
    """Whiteboard application.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param AppName: Application name.
        :type AppName: str
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param TagList: Tag list.
        :type TagList: list of Tag
        """
        self.SdkAppId = None
        self.AppName = None
        self.CreateTime = None
        self.TagList = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.AppName = params.get("AppName")
        self.CreateTime = params.get("CreateTime")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyTiwTrialRequest(AbstractModel):
    """ApplyTiwTrial request structure.

    """


class ApplyTiwTrialResponse(AbstractModel):
    """ApplyTiwTrial response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AuthParam(AbstractModel):
    """Authentication parameters.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param UserId: User ID.
        :type UserId: str
        :param UserSig: Signature corresponding to the user ID.
        :type UserSig: str
        """
        self.SdkAppId = None
        self.UserId = None
        self.UserSig = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.UserId = params.get("UserId")
        self.UserSig = params.get("UserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class CreateApplicationRequest(AbstractModel):
    """CreateApplication request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param AppName: Application name.
        :type AppName: str
        :param SKey: SKey required for creating an IM application.
        :type SKey: str
        :param TinyId: TinyId required for creating an IM application.
        :type TinyId: str
        :param TagList: List of tags to be bound.
        :type TagList: list of Tag
        """
        self.SdkAppId = None
        self.AppName = None
        self.SKey = None
        self.TinyId = None
        self.TagList = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.AppName = params.get("AppName")
        self.SKey = params.get("SKey")
        self.TinyId = params.get("TinyId")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationResponse(AbstractModel):
    """CreateApplication response structure.

    """

    def __init__(self):
        r"""
        :param AppId: AppId of the customer.
        :type AppId: int
        :param AppName: Application name.
        :type AppName: str
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AppId = None
        self.AppName = None
        self.SdkAppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.AppName = params.get("AppName")
        self.SdkAppId = params.get("SdkAppId")
        self.RequestId = params.get("RequestId")


class CreateOfflineRecordRequest(AbstractModel):
    """CreateOfflineRecord request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param RoomId: Room ID corresponding to the recording task.
        :type RoomId: int
        :param GroupId: Group ID corresponding to the recording task.
        :type GroupId: str
        :param MixStream: Stream mixing parameters.
The Custom parameter is not supported for offline recording tasks.
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param Whiteboard: Whiteboard parameters.
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        """
        self.SdkAppId = None
        self.RoomId = None
        self.GroupId = None
        self.MixStream = None
        self.Whiteboard = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        if params.get("MixStream") is not None:
            self.MixStream = MixStream()
            self.MixStream._deserialize(params.get("MixStream"))
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOfflineRecordResponse(AbstractModel):
    """CreateOfflineRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSnapshotTaskRequest(AbstractModel):
    """CreateSnapshotTask request structure.

    """

    def __init__(self):
        r"""
        :param Whiteboard: Whiteboard parameters.
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.SnapshotWhiteboard`
        :param SdkAppId: `SdkAppId` of the whiteboard application.
        :type SdkAppId: int
        :param RoomId: Whiteboard room ID.
        :type RoomId: int
        :param CallbackURL: Callback URL to which the whiteboard snapshot result is to be sent.
        :type CallbackURL: str
        :param COS: `COS` bucket in which the generated whiteboard snapshot file is to be stored. If you leave this parameter empty, the generated file will be stored in the public bucket and retained for only three days.
        :type COS: :class:`tencentcloud.tiw.v20190919.models.SnapshotCOS`
        :param SnapshotMode: Whiteboard snapshot mode. Default value: `AllMarks`. Valid values:

`AllMarks`: Full mode. In this mode, a snapshot image is generated based on each whiteboard snapshot mark that is added by calling the `addSnapshotMark` API on the client.

`LatestMarksOnly`: Single-page deduplication mode. In this mode, a snapshot image is generated based only on the latest whiteboard snapshot mark that is added by calling the `addSnapshotMark` API on the client if the API is called multiple times for the same whiteboard snapshot.

**Note: The `LatestMarksOnly` mode takes effect only when the `addSnapshotMark` API is called by using Tencent Interactive Whiteboard SDK v2.6.8 or later. Otherwise, even if this parameter is set to `LatestMarksOnly`, the default `AllMarks` mode is used.**
        :type SnapshotMode: str
        """
        self.Whiteboard = None
        self.SdkAppId = None
        self.RoomId = None
        self.CallbackURL = None
        self.COS = None
        self.SnapshotMode = None


    def _deserialize(self, params):
        if params.get("Whiteboard") is not None:
            self.Whiteboard = SnapshotWhiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.CallbackURL = params.get("CallbackURL")
        if params.get("COS") is not None:
            self.COS = SnapshotCOS()
            self.COS._deserialize(params.get("COS"))
        self.SnapshotMode = params.get("SnapshotMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotTaskResponse(AbstractModel):
    """CreateSnapshotTask response structure.

    """

    def __init__(self):
        r"""
        :param TaskID: ID of the whiteboard snapshot task. This parameter is returned only if a task is created successfully.
        :type TaskID: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.RequestId = params.get("RequestId")


class CreateTranscodeRequest(AbstractModel):
    """CreateTranscode request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param Url: URL of the transcoded document after URL encoding. URL encoding converts characters into a format that can be transmitted over the Internet. For example, URL encoding can convert the document URL http://example.com/Test.pdf into http://example.com/%E6%B5%8B%E8%AF%95.pdf. To improve the success rate of URL parsing, use URL encoding.
        :type Url: str
        :param IsStaticPPT: Whether the PowerPoint file is static. The default value is False.
If IsStaticPPT is False, documents with the .ppt or .pptx extension will be dynamically transcoded to HTML5 pages, and documents with other extensions will be statically transcoded to images. If IsStaticPPT is True, documents with any extensions will be statically transcoded to images.
        :type IsStaticPPT: bool
        :param MinResolution: Note: This parameter is disused. Use the MinScaleResolution parameter to pass in a resolution. For more information, see [CreateTranscode](https://intl.cloud.tencent.com/document/api/1137/40060?from_cn_redirect=1#SDK).

Minimum resolution of the transcoded document. If no value or null is specified for it or the resolution format is invalid, the original document resolution is used.

Example: 1280x720. Note that the character between the numbers is the letter x.
        :type MinResolution: str
        :param ThumbnailResolution: Resolution of the thumbnail generated for the dynamically transcoded PowerPoint file. If no value or null is specified for it or the resolution format is invalid, no thumbnail will be generated. The resolution format is the same as that of MinResolution.

For static transcoding, this parameter does not work.
        :type ThumbnailResolution: str
        :param CompressFileType: Compression format of the transcoded file. If no value or null is specified for it or the specified format is invalid, no compression file will be generated. Currently, the following compression formats are supported:

`zip`: generates a .zip compression package.
`tar.gz: generates a .tar.gz compression package.
        :type CompressFileType: str
        :param ExtraData: Internal parameter.
        :type ExtraData: str
        :param Priority: Document transcoding priority. This parameter takes effect only for PowerPoint dynamic transcoding. Valid values:<br/>
- low: Low transcoding priority. The task can transcode at most 500 MB of data or a 2000-page document, with a download timeout no longer than 10 minutes. Due to resource limits, these tasks may have to queue for a long period of time. Consider this before you use this feature.
- null: Normal transcoding priority. The task can transcode at most 200 MB of data or a 500-page document, with a download timeout no longer than 2 minutes.
<br/>
Note: For static transcoding such as PDF transcoding, each task can transcode at most 200 MB of data regardless of the transcoding priority.
        :type Priority: str
        :param MinScaleResolution: Minimum resolution of the transcoded document. If no value or null is specified for it or the resolution format is invalid, the original document resolution is used.
Higher resolution brings clearer visual effect, but also means larger size of the transcoded image resources and longer loading time of the transcoded file. Set this parameter appropriately based on your actual scenario.

Example: 1280x720. Note that the character between the numbers is the letter x.
        :type MinScaleResolution: str
        :param AutoHandleUnsupportedElement: Specifies whether to enable auto handling of unsupported elements. By default, this feature is disabled.

If auto handling is enabled, the following processes are performed:
1. Inkblots: Remove unsupported inkblots, such as those drawn by using WPS.
2. Auto page flip: Clear the auto page clip settings in the PowerPoint file and set the page flip mode to mouse click.
3. Corrupted audio/videos: Remove the references to corrupted audio/videos in the PowerPoint file.
        :type AutoHandleUnsupportedElement: bool
        """
        self.SdkAppId = None
        self.Url = None
        self.IsStaticPPT = None
        self.MinResolution = None
        self.ThumbnailResolution = None
        self.CompressFileType = None
        self.ExtraData = None
        self.Priority = None
        self.MinScaleResolution = None
        self.AutoHandleUnsupportedElement = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Url = params.get("Url")
        self.IsStaticPPT = params.get("IsStaticPPT")
        self.MinResolution = params.get("MinResolution")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileType = params.get("CompressFileType")
        self.ExtraData = params.get("ExtraData")
        self.Priority = params.get("Priority")
        self.MinScaleResolution = params.get("MinScaleResolution")
        self.AutoHandleUnsupportedElement = params.get("AutoHandleUnsupportedElement")
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


class CreateVideoGenerationTaskRequest(AbstractModel):
    """CreateVideoGenerationTask request structure.

    """

    def __init__(self):
        r"""
        :param OnlineRecordTaskId: ID of the recording task.
        :type OnlineRecordTaskId: str
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param Whiteboard: Whiteboard parameters of the recording video generation task, such as the width and height of the whiteboard.

This parameter conflicts with the Whiteboard parameter in the API for starting a recording task. If the two Whiteboard parameters are both specified, the Whiteboard parameter in this API takes priority for recording video generation. If the Whiteboard parameter in this API is not specified, the Whiteboard parameter specified in the API for starting a recording task is used for recording video generation.
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param Concat: Video splicing parameters.

This parameter conflicts with the Concat parameter in the API for starting a recording task. If the two Concat parameters are both specified, the Concat parameter in this API takes priority for video splicing. If the Concat parameter in this API is not specified, the Concat parameter specified in the API for starting a recording task is used for video splicing.
        :type Concat: :class:`tencentcloud.tiw.v20190919.models.Concat`
        :param MixStream: Video stream mixing parameters.

This parameter conflicts with the MixStream parameter in the API for starting a recording task. If the two MixStream parameters are both specified, the MixStream parameter in this API takes priority for video stream mixing. If the MixStream parameter in this API is not specified, the MixStream parameter specified in the API for starting a recording task is used for video stream mixing.
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param RecordControl: A group of video generation parameters. It specifies the streams to be generated, whether to disable audio recording for a stream, and whether to record only low-resolution videos, etc.

This parameter conflicts with the RecordControl parameter in the API for starting a recording task. If the two RecordControl parameters are both specified, the RecordControl parameter in this API takes priority for video generation control. If the RecordControl parameter in this API is not specified, the RecordControl parameter specified in the API for starting a recording task is used for video generation control.
        :type RecordControl: :class:`tencentcloud.tiw.v20190919.models.RecordControl`
        :param ExtraData: Internal parameter.
        :type ExtraData: str
        """
        self.OnlineRecordTaskId = None
        self.SdkAppId = None
        self.Whiteboard = None
        self.Concat = None
        self.MixStream = None
        self.RecordControl = None
        self.ExtraData = None


    def _deserialize(self, params):
        self.OnlineRecordTaskId = params.get("OnlineRecordTaskId")
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("Concat") is not None:
            self.Concat = Concat()
            self.Concat._deserialize(params.get("Concat"))
        if params.get("MixStream") is not None:
            self.MixStream = MixStream()
            self.MixStream._deserialize(params.get("MixStream"))
        if params.get("RecordControl") is not None:
            self.RecordControl = RecordControl()
            self.RecordControl._deserialize(params.get("RecordControl"))
        self.ExtraData = params.get("ExtraData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoGenerationTaskResponse(AbstractModel):
    """CreateVideoGenerationTask response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: ID of the video generation task.
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
        


class DataItem(AbstractModel):
    """Chart data, including the time, values, and details.

    """

    def __init__(self):
        r"""
        :param Time: Time. The following formats are supported:
yyyy-mm
yyyy-mm-dd
yyyy-mm-dd HH:MM:SS
        :type Time: str
        :param Value: Values required for drawing charts.
        :type Value: int
        :param Details: Details of the values.
        :type Details: list of Detail
        """
        self.Time = None
        self.Value = None
        self.Details = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = Detail()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIServiceRequest(AbstractModel):
    """DescribeAPIService request structure.

    """

    def __init__(self):
        r"""
        :param Service: Supported services are cos:GetService and cdn:DescribeDomainsConfig.
        :type Service: str
        :param Data: Request parameters in JSON format.
        :type Data: str
        """
        self.Service = None
        self.Data = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIServiceResponse(AbstractModel):
    """DescribeAPIService response structure.

    """

    def __init__(self):
        r"""
        :param ResponseData: Response data in JSON format.
        :type ResponseData: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResponseData = params.get("ResponseData")
        self.RequestId = params.get("RequestId")


class DescribeApplicationInfosRequest(AbstractModel):
    """DescribeApplicationInfos request structure.

    """


class DescribeApplicationInfosResponse(AbstractModel):
    """DescribeApplicationInfos response structure.

    """

    def __init__(self):
        r"""
        :param ApplicationInfos: Application list.
        :type ApplicationInfos: list of ApplicationItem
        :param AllOption: Specifies whether all applications are included. The value 0 indicates no and 1 indicates yes.
        :type AllOption: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ApplicationInfos = None
        self.AllOption = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApplicationInfos") is not None:
            self.ApplicationInfos = []
            for item in params.get("ApplicationInfos"):
                obj = ApplicationItem()
                obj._deserialize(item)
                self.ApplicationInfos.append(obj)
        self.AllOption = params.get("AllOption")
        self.RequestId = params.get("RequestId")


class DescribeApplicationUsageRequest(AbstractModel):
    """DescribeApplicationUsage request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: Start time of the query period. The start time point is included in the query period.
        :type BeginTime: str
        :param EndTime: End time of the query period. The end time point is not included in the query period.
        :type EndTime: str
        :param SubProduct: Subproduct name.
        :type SubProduct: str
        :param TimeLevel: Unit of time increment.
- MONTHLY: month
- DAILY: day
- MINUTELY: minute
        :type TimeLevel: str
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param IsWeighted: true: Returns the weighted sum of raw usage data.
false: Returns the raw usage data.
        :type IsWeighted: bool
        """
        self.BeginTime = None
        self.EndTime = None
        self.SubProduct = None
        self.TimeLevel = None
        self.SdkAppId = None
        self.IsWeighted = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.SubProduct = params.get("SubProduct")
        self.TimeLevel = params.get("TimeLevel")
        self.SdkAppId = params.get("SdkAppId")
        self.IsWeighted = params.get("IsWeighted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationUsageResponse(AbstractModel):
    """DescribeApplicationUsage response structure.

    """

    def __init__(self):
        r"""
        :param Data: Usage data required for drawing charts.
        :type Data: list of DataItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBoardSDKLogRequest(AbstractModel):
    """DescribeBoardSDKLog request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param RoomId: Room ID to be used to query logs.
        :type RoomId: str
        :param UserId: User ID to be used to query logs.
        :type UserId: str
        :param TimeRange: Query period, which consists of two Unix timestamps in milliseconds. The first indicates the start time and the second the end time.
        :type TimeRange: list of int
        :param AggregationInterval: Interval for aggregating log number queries. Example values: `5m`, `1h`, `4h`
        :type AggregationInterval: str
        :param Query: Extra query conditions.
        :type Query: str
        :param Ascending: Specifies whether to sort results in ascending order of time.
        :type Ascending: bool
        :param Context: Context key used for recursive extraction. Obtain this parameter in the response to the last request.
        :type Context: str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserId = None
        self.TimeRange = None
        self.AggregationInterval = None
        self.Query = None
        self.Ascending = None
        self.Context = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserId = params.get("UserId")
        self.TimeRange = params.get("TimeRange")
        self.AggregationInterval = params.get("AggregationInterval")
        self.Query = params.get("Query")
        self.Ascending = params.get("Ascending")
        self.Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBoardSDKLogResponse(AbstractModel):
    """DescribeBoardSDKLog response structure.

    """

    def __init__(self):
        r"""
        :param Total: Number of logs queried.
        :type Total: int
        :param Sources: Log details.
        :type Sources: list of str
        :param Buckets: Number of logs queried within each time range after aggregation based on the time range.
        :type Buckets: list of str
        :param Context: Context key used for recursive extraction. This parameter can be used in the next request.
        :type Context: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Sources = None
        self.Buckets = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Sources = params.get("Sources")
        self.Buckets = params.get("Buckets")
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class DescribeIMApplicationsRequest(AbstractModel):
    """DescribeIMApplications request structure.

    """


class DescribeIMApplicationsResponse(AbstractModel):
    """DescribeIMApplications response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeOfflineRecordCallbackRequest(AbstractModel):
    """DescribeOfflineRecordCallback request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
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
        


class DescribeOfflineRecordCallbackResponse(AbstractModel):
    """DescribeOfflineRecordCallback response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeOfflineRecordRequest(AbstractModel):
    """DescribeOfflineRecord request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param TaskId: ID of the offline recording task.
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
        


class DescribeOfflineRecordResponse(AbstractModel):
    """DescribeOfflineRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
- AUTO: Recording automatically stops because no upstream audio/video or whiteboard operation occurs in the room for a long time.
- USER_CALL: The API for stopping recording is called.
- EXCEPTION: An exception occurred.
- FORCE_STOP: Recording is forcibly stopped, which is usually because the recording has been paused for more than 90 minutes or has lasted for more than 24 hours.
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
        :param ReplayUrl: 
        :type ReplayUrl: str
        :param Interrupts: Number of video stream interruptions during recording.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Interrupts: list of Interrupt
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
        self.ReplayUrl = None
        self.Interrupts = None
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
        self.ReplayUrl = params.get("ReplayUrl")
        if params.get("Interrupts") is not None:
            self.Interrupts = []
            for item in params.get("Interrupts"):
                obj = Interrupt()
                obj._deserialize(item)
                self.Interrupts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePostpaidUsageRequest(AbstractModel):
    """DescribePostpaidUsage request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: Start time of the query period.
        :type BeginTime: str
        :param EndTime: End time of the query period.
        :type EndTime: str
        """
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePostpaidUsageResponse(AbstractModel):
    """DescribePostpaidUsage response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeQualityMetricsRequest(AbstractModel):
    """DescribeQualityMetrics request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param StartTime: Start time, which is a Unix timestamp in seconds. The time length cannot exceed seven days.
        :type StartTime: int
        :param EndTime: End time, which is a Unix timestamp in seconds. The time length cannot exceed seven days.
        :type EndTime: int
        :param Metric: Metrics to be queried. Valid values:
  - image_load_total_count: The number of image loads.
  - image_load_fail_count: The number of image load failures.
  - image_load_success_rate: The success rate of image loading, in percentage.
  - ppt_load_total_count: The number of PowerPoint file loads.
  - ppt_load_fail_count: The number of PowerPoint file load failures.
  - ppt_load_success_rate: The success rate of PowerPoint file loading, in percentage.
  - verify_sdk_total_count: The number of SDK verifications.
  - verify_sdk_fail_count: The number of SDK verification failures.
  - verify_sdk_success_rate: The success rate of SDK verification, in percentage.
  - verify_sdk_in_one_second_rate: The rate of SDK verification completed within one second, in percentage.
  - verify_sdk_cost_avg: The average time taken by each SDK verification, in milliseconds.
        :type Metric: str
        :param Interval: Aggregation interval. Valid value: `1h`.
        :type Interval: str
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Interval = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQualityMetricsResponse(AbstractModel):
    """DescribeQualityMetrics response structure.

    """

    def __init__(self):
        r"""
        :param Metric: Query metrics.
        :type Metric: str
        :param Content: Time series.
        :type Content: list of TimeValue
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Metric = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordSearchRequest(AbstractModel):
    """DescribeRecordSearch request structure.

    """


class DescribeRecordSearchResponse(AbstractModel):
    """DescribeRecordSearch response structure.

    """

    def __init__(self):
        r"""
        :param RecordTaskSet: The set of queried recording tasks.
        :type RecordTaskSet: list of RecordTaskSearchResult
        :param TotalCount: Number of recording tasks.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RecordTaskSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordTaskSet") is not None:
            self.RecordTaskSet = []
            for item in params.get("RecordTaskSet"):
                obj = RecordTaskSearchResult()
                obj._deserialize(item)
                self.RecordTaskSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRoomListRequest(AbstractModel):
    """DescribeRoomList request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param TimeRange: Query period, which consists of two Unix timestamps in milliseconds. The first indicates the start time and the second the end time.
        :type TimeRange: list of int
        :param Query: Extra query conditions.
        :type Query: str
        :param MaxSize: Maximum number of data entries to be returned. Default value: 1000.
        :type MaxSize: int
        """
        self.SdkAppId = None
        self.TimeRange = None
        self.Query = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TimeRange = params.get("TimeRange")
        self.Query = params.get("Query")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomListResponse(AbstractModel):
    """DescribeRoomList response structure.

    """

    def __init__(self):
        r"""
        :param RoomList: List of rooms of the whiteboard.
        :type RoomList: list of RoomListItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoomList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RoomList") is not None:
            self.RoomList = []
            for item in params.get("RoomList"):
                obj = RoomListItem()
                obj._deserialize(item)
                self.RoomList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotTaskRequest(AbstractModel):
    """DescribeSnapshotTask request structure.

    """

    def __init__(self):
        r"""
        :param TaskID: ID of the query task.
        :type TaskID: str
        :param SdkAppId: SdkAppId of the task.
        :type SdkAppId: int
        """
        self.TaskID = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotTaskResponse(AbstractModel):
    """DescribeSnapshotTask response structure.

    """

    def __init__(self):
        r"""
        :param TaskID: Task ID.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type TaskID: str
        :param Status: Task status.
Running: The task is running.
Finished: The task is finished.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param CreateTime: Creation time of the task. Unit: seconds.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param FinishTime: Completion time of the task. Unit: seconds.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type FinishTime: int
        :param Result: Task result information.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.tiw.v20190919.models.SnapshotResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskID = None
        self.Status = None
        self.CreateTime = None
        self.FinishTime = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("Result") is not None:
            self.Result = SnapshotResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTIWDailyUsageRequest(AbstractModel):
    """DescribeTIWDailyUsage request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param SubProduct: Subproduct usage to be queried. The following parameters are supported:
- sp_tiw_board: The duration of use of whiteboards, in minutes.
- sp_tiw_dt: The number of pages dynamically transcoded.
- sp_tiw_st: The number of pages statically transcoded.
- sp_tiw_ric: The duration of real-time recording, in minutes.

Note: Dynamic transcoding multiplies the number of pages of a document by eight times. Static transcoding does not change the number of pages of a document.
        :type SubProduct: str
        :param StartTime: Start date in the format of YYYY-MM-DD. The start date is included in the query period.
        :type StartTime: str
        :param EndTime: End date in the format of YYYY-MM-DD. The end date is included in the query period. The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        """
        self.SdkAppId = None
        self.SubProduct = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.SubProduct = params.get("SubProduct")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTIWDailyUsageResponse(AbstractModel):
    """DescribeTIWDailyUsage response structure.

    """

    def __init__(self):
        r"""
        :param Usages: Usage summary of a specified product during a specified query period.
        :type Usages: list of UsageDataItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Usages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = UsageDataItem()
                obj._deserialize(item)
                self.Usages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTIWRoomDailyUsageRequest(AbstractModel):
    """DescribeTIWRoomDailyUsage request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param SubProduct: Subproduct usage to be queried. The following parameters are supported:
- sp_tiw_board: The duration of use of whiteboards, in minutes.
- sp_tiw_ric: The duration of real-time recording, in minutes.
        :type SubProduct: str
        :param StartTime: Start date in the format of YYYY-MM-DD. The start date is included in the query period.
        :type StartTime: str
        :param EndTime: End date in the format of YYYY-MM-DD. The end date is included in the query period. The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        :param RoomIDs: Room IDs to be queried. If you leave this parameter empty, all room IDs are queried.
        :type RoomIDs: list of int non-negative
        :param Offset: Offset for query. Default value: `0`.
        :type Offset: int
        :param Limit: Maximum number of entries returned per query. Default value: `20`.
        :type Limit: int
        """
        self.SdkAppId = None
        self.SubProduct = None
        self.StartTime = None
        self.EndTime = None
        self.RoomIDs = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.SubProduct = params.get("SubProduct")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RoomIDs = params.get("RoomIDs")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTIWRoomDailyUsageResponse(AbstractModel):
    """DescribeTIWRoomDailyUsage response structure.

    """

    def __init__(self):
        r"""
        :param Usages: Usage of the specified product per room during the specified query period.
        :type Usages: list of RoomUsageDataItem
        :param Total: Number of usage data entries.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Usages = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = RoomUsageDataItem()
                obj._deserialize(item)
                self.Usages.append(obj)
        self.Total = params.get("Total")
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
        :param ResourceListUrl: Download URL (for trial) of the resource list.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type ResourceListUrl: str
        :param Ext: Document generation mode (for trial).
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Ext: str
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
        self.ResourceListUrl = None
        self.Ext = None
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
        self.ResourceListUrl = params.get("ResourceListUrl")
        self.Ext = params.get("Ext")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeSearchRequest(AbstractModel):
    """DescribeTranscodeSearch request structure.

    """


class DescribeTranscodeSearchResponse(AbstractModel):
    """DescribeTranscodeSearch response structure.

    """

    def __init__(self):
        r"""
        :param TranscodeTaskSet: The set of queried transcoding tasks.
        :type TranscodeTaskSet: list of TranscodeTaskSearchResult
        :param TotalCount: Number of transcoding tasks.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TranscodeTaskSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self.TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskSearchResult()
                obj._deserialize(item)
                self.TranscodeTaskSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUsageSummaryRequest(AbstractModel):
    """DescribeUsageSummary request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: Start time of the query period.
        :type BeginTime: str
        :param EndTime: End time of the query period.
        :type EndTime: str
        :param SubProducts: Subproducts whose usage you want to query.
        :type SubProducts: list of str
        :param IsWeighted: true: Returns weighted data.
false: Returns raw data.
        :type IsWeighted: bool
        """
        self.BeginTime = None
        self.EndTime = None
        self.SubProducts = None
        self.IsWeighted = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.SubProducts = params.get("SubProducts")
        self.IsWeighted = params.get("IsWeighted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageSummaryResponse(AbstractModel):
    """DescribeUsageSummary response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeUserListRequest(AbstractModel):
    """DescribeUserList request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param RoomId: Room ID to be used to query users.
        :type RoomId: str
        :param TimeRange: Query period, which consists of two Unix timestamps in milliseconds. The first indicates the start time and the second the end time.
        :type TimeRange: list of int
        :param Query: Extra query conditions.
        :type Query: str
        :param MaxSize: Maximum number of data entries to be returned. Default value: `1000`.
        :type MaxSize: int
        """
        self.SdkAppId = None
        self.RoomId = None
        self.TimeRange = None
        self.Query = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.TimeRange = params.get("TimeRange")
        self.Query = params.get("Query")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListResponse(AbstractModel):
    """DescribeUserList response structure.

    """

    def __init__(self):
        r"""
        :param UserList: User list of the room.
        :type UserList: list of UserListItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserListItem()
                obj._deserialize(item)
                self.UserList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserResourcesRequest(AbstractModel):
    """DescribeUserResources request structure.

    """


class DescribeUserResourcesResponse(AbstractModel):
    """DescribeUserResources response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeUserStatusRequest(AbstractModel):
    """DescribeUserStatus request structure.

    """


class DescribeUserStatusResponse(AbstractModel):
    """DescribeUserStatus response structure.

    """

    def __init__(self):
        r"""
        :param AppId: AppId of the customer.
        :type AppId: int
        :param IsTiwUser: Specifies whether the whiteboard service of the trial or official edition is activated before.

0: The whiteboard service is not activated.
1: The whiteboard service is activated.
        :type IsTiwUser: int
        :param IsSaaSUser: Specifies whether the interactive class feature of the trial or official edition is activated before.
        :type IsSaaSUser: int
        :param IsTiwOfflineRecordUser: Specifies whether the user uses the offline recording feature of the whiteboard service.
        :type IsTiwOfflineRecordUser: int
        :param IsAuthenticated: Specifies whether the user is authenticated.
        :type IsAuthenticated: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AppId = None
        self.IsTiwUser = None
        self.IsSaaSUser = None
        self.IsTiwOfflineRecordUser = None
        self.IsAuthenticated = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.IsTiwUser = params.get("IsTiwUser")
        self.IsSaaSUser = params.get("IsSaaSUser")
        self.IsTiwOfflineRecordUser = params.get("IsTiwOfflineRecordUser")
        self.IsAuthenticated = params.get("IsAuthenticated")
        self.RequestId = params.get("RequestId")


class DescribeVideoGenerationTaskCallbackRequest(AbstractModel):
    """DescribeVideoGenerationTaskCallback request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
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
        


class DescribeVideoGenerationTaskCallbackResponse(AbstractModel):
    """DescribeVideoGenerationTaskCallback response structure.

    """

    def __init__(self):
        r"""
        :param Callback: Callback URL for recording video generation.
        :type Callback: str
        :param CallbackKey: Callback authentication key for recording video generation.
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


class DescribeVideoGenerationTaskRequest(AbstractModel):
    """DescribeVideoGenerationTask request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param TaskId: ID of the recording video generation task.
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
        


class DescribeVideoGenerationTaskResponse(AbstractModel):
    """DescribeVideoGenerationTask response structure.

    """

    def __init__(self):
        r"""
        :param GroupId: Group ID corresponding to the task.
        :type GroupId: str
        :param RoomId: Room ID corresponding to the task.
        :type RoomId: int
        :param TaskId: Task ID.
        :type TaskId: str
        :param Progress: Disused.
        :type Progress: int
        :param Status: Status of the recording video generation task. Valid values:
- QUEUED: Queuing.
- PROCESSING: Video generation in progress.
- FINISHED: Video generation finished. (To determine whether the task succeeded or failed, check the error code and message.)
        :type Status: str
        :param TotalTime: Total video playback duration. Unit: milliseconds.
        :type TotalTime: int
        :param VideoInfos: Disused. Use the `VideoInfoList` parameter.
        :type VideoInfos: :class:`tencentcloud.tiw.v20190919.models.VideoInfo`
        :param VideoInfoList: List of videos generated by the recording video generation tasks.
        :type VideoInfoList: list of VideoInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.RoomId = None
        self.TaskId = None
        self.Progress = None
        self.Status = None
        self.TotalTime = None
        self.VideoInfos = None
        self.VideoInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RoomId = params.get("RoomId")
        self.TaskId = params.get("TaskId")
        self.Progress = params.get("Progress")
        self.Status = params.get("Status")
        self.TotalTime = params.get("TotalTime")
        if params.get("VideoInfos") is not None:
            self.VideoInfos = VideoInfo()
            self.VideoInfos._deserialize(params.get("VideoInfos"))
        if params.get("VideoInfoList") is not None:
            self.VideoInfoList = []
            for item in params.get("VideoInfoList"):
                obj = VideoInfo()
                obj._deserialize(item)
                self.VideoInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardApplicationConfigRequest(AbstractModel):
    """DescribeWhiteboardApplicationConfig request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param TaskTypes: Task types to be queried.
recording: Real-time recording.
transcode: Document transcoding.
        :type TaskTypes: list of str
        :param SdkAppIds: SdkAppIds to be used to query configurations.
        :type SdkAppIds: list of int
        """
        self.SdkAppId = None
        self.TaskTypes = None
        self.SdkAppIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskTypes = params.get("TaskTypes")
        self.SdkAppIds = params.get("SdkAppIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardApplicationConfigResponse(AbstractModel):
    """DescribeWhiteboardApplicationConfig response structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param Configs: Task-related configurations of the whiteboard application.
        :type Configs: list of WhiteboardApplicationConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SdkAppId = None
        self.Configs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = WhiteboardApplicationConfig()
                obj._deserialize(item)
                self.Configs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardBucketConfigRequest(AbstractModel):
    """DescribeWhiteboardBucketConfig request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param TaskType: Task type to be queried.
recording: Real-time recording.
transcode: Document transcoding.
        :type TaskType: str
        """
        self.SdkAppId = None
        self.TaskType = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardBucketConfigResponse(AbstractModel):
    """DescribeWhiteboardBucketConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardPushCallbackRequest(AbstractModel):
    """DescribeWhiteboardPushCallback request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
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
        


class DescribeWhiteboardPushCallbackResponse(AbstractModel):
    """DescribeWhiteboardPushCallback response structure.

    """

    def __init__(self):
        r"""
        :param Callback: Callback URL of the whiteboard push event. If no callback URL is set, this parameter is null.
        :type Callback: str
        :param CallbackKey: Callback authentication key for whiteboard push.
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


class DescribeWhiteboardPushRequest(AbstractModel):
    """DescribeWhiteboardPush request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param TaskId: ID of the whiteboard push task.
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
        


class DescribeWhiteboardPushResponse(AbstractModel):
    """DescribeWhiteboardPush response structure.

    """

    def __init__(self):
        r"""
        :param FinishReason: Reason for push stop.
- AUTO: Pushing automatically stops because no upstream audio/video or whiteboard operation occurs in the room for a long time.
- USER_CALL: The API for stopping pushing is called.
- EXCEPTION: An exception occurred.
        :type FinishReason: str
        :param TaskId: ID of the whiteboard push task.
        :type TaskId: str
        :param Status: Status of the push task.
- PREPARED: Push in preparation (including entering the room and starting the push service).
- PUSHING: Pushing in progress.
- STOPPED: Pushing stopped.
        :type Status: str
        :param RoomId: Room ID.
        :type RoomId: int
        :param GroupId: Group ID of the whiteboard.
        :type GroupId: str
        :param PushUserId: User ID of the push task.
        :type PushUserId: str
        :param PushStartTime: Actual push start time, which is a Unix timestamp in seconds.
        :type PushStartTime: int
        :param PushStopTime: Actual push stop time, which is a Unix timestamp in seconds.
        :type PushStopTime: int
        :param ExceptionCnt: Number of exceptions during push.
        :type ExceptionCnt: int
        :param IMSyncTime: IM timestamp corresponding to the first frame of the whiteboard push video. The timestamp is used for time synchronization between IM messages and the whiteboard push video during playback.
        :type IMSyncTime: int
        :param Backup: Result information of the backup push task.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Backup: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FinishReason = None
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.GroupId = None
        self.PushUserId = None
        self.PushStartTime = None
        self.PushStopTime = None
        self.ExceptionCnt = None
        self.IMSyncTime = None
        self.Backup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.PushUserId = params.get("PushUserId")
        self.PushStartTime = params.get("PushStartTime")
        self.PushStopTime = params.get("PushStopTime")
        self.ExceptionCnt = params.get("ExceptionCnt")
        self.IMSyncTime = params.get("IMSyncTime")
        self.Backup = params.get("Backup")
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardPushSearchRequest(AbstractModel):
    """DescribeWhiteboardPushSearch request structure.

    """


class DescribeWhiteboardPushSearchResponse(AbstractModel):
    """DescribeWhiteboardPushSearch response structure.

    """

    def __init__(self):
        r"""
        :param WhiteboardPushTaskSet: The set of queried push tasks.
        :type WhiteboardPushTaskSet: list of WhiteboardPushTaskSearchResult
        :param TotalCount: Number of push tasks.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.WhiteboardPushTaskSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WhiteboardPushTaskSet") is not None:
            self.WhiteboardPushTaskSet = []
            for item in params.get("WhiteboardPushTaskSet"):
                obj = WhiteboardPushTaskSearchResult()
                obj._deserialize(item)
                self.WhiteboardPushTaskSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Detail(AbstractModel):
    """Detailed metric data with different tags in billable usage data.

    """

    def __init__(self):
        r"""
        :param TagName: Usage metric.
        :type TagName: str
        :param Weight: Usage weight.
        :type Weight: float
        :param Value: Usage value.
        :type Value: float
        """
        self.TagName = None
        self.Weight = None
        self.Value = None


    def _deserialize(self, params):
        self.TagName = params.get("TagName")
        self.Weight = params.get("Weight")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Interrupt(AbstractModel):
    """Number of video stream interruptions during real-time recording.

    """

    def __init__(self):
        r"""
        :param UserId: User ID.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param Count: Number of video stream interruptions.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Count: int
        """
        self.UserId = None
        self.Count = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class ModifyApplicationRequest(AbstractModel):
    """ModifyApplication request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param AppName: Application name.
        :type AppName: str
        """
        self.SdkAppId = None
        self.AppName = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationResponse(AbstractModel):
    """ModifyApplication response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param SubProduct: Subproduct ID. To obtain this ID, call the `DescribeUserResources` API and find the subproduct ID of the monthly feature package with the level 1. Usually the value is `sp_tiw_package`.
        :type SubProduct: str
        :param ResourceId: Resource ID. To obtain this ID, call the `DescribeUserResources` API and find the resource ID of the monthly feature package with the level 1.
        :type ResourceId: str
        :param AutoRenewFlag: Renewal mode. Valid values: `0` (default mode, which is auto-renewal), `1` (auto-renewal), `2` (manual renewal, which is specified by users). If no renewal is required, set it to `0`.
        :type AutoRenewFlag: int
        """
        self.SubProduct = None
        self.ResourceId = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.SubProduct = params.get("SubProduct")
        self.ResourceId = params.get("ResourceId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWhiteboardApplicationConfigRequest(AbstractModel):
    """ModifyWhiteboardApplicationConfig request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param Configs: Task-related configurations of the whiteboard application.
        :type Configs: list of WhiteboardApplicationConfig
        """
        self.SdkAppId = None
        self.Configs = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = WhiteboardApplicationConfig()
                obj._deserialize(item)
                self.Configs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWhiteboardApplicationConfigResponse(AbstractModel):
    """ModifyWhiteboardApplicationConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWhiteboardBucketConfigRequest(AbstractModel):
    """ModifyWhiteboardBucketConfig request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param TaskType: Task type to be queried.
recording: Real-time recording.
transcode: Document transcoding.
        :type TaskType: str
        :param BucketName: Name of the COS bucket.
        :type BucketName: str
        :param BucketLocation: Region of the COS bucket.
        :type BucketLocation: str
        :param BucketPrefix: Resource prefix of the bucket.
        :type BucketPrefix: str
        :param ResultDomain: Domain name of the URL of the bucket.
        :type ResultDomain: str
        """
        self.SdkAppId = None
        self.TaskType = None
        self.BucketName = None
        self.BucketLocation = None
        self.BucketPrefix = None
        self.ResultDomain = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskType = params.get("TaskType")
        self.BucketName = params.get("BucketName")
        self.BucketLocation = params.get("BucketLocation")
        self.BucketPrefix = params.get("BucketPrefix")
        self.ResultDomain = params.get("ResultDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWhiteboardBucketConfigResponse(AbstractModel):
    """ModifyWhiteboardBucketConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
        


class RecordTaskResult(AbstractModel):
    """Real-time recording result.

    """

    def __init__(self):
        r"""
        :param FinishReason: `AUTO`: Recording automatically stops. `USER_CALL`: The API for stopping recording is called.
        :type FinishReason: str
        :param ExceptionCnt: Number of exceptions.
        :type ExceptionCnt: int
        :param RoomId: Room ID.
        :type RoomId: int
        :param GroupId: Group ID.
        :type GroupId: str
        :param RecordStartTime: Actual recording start time.
        :type RecordStartTime: int
        :param RecordStopTime: Recording end time.
        :type RecordStopTime: int
        :param TotalTime: Recording duration.
        :type TotalTime: int
        :param VideoInfos: List of video information.
        :type VideoInfos: list of VideoInfo
        :param OmittedDurations: Omitted video durations.
        :type OmittedDurations: list of OmittedDuration
        :param Details: Details.
        :type Details: str
        :param ErrorCode: Task execution error code.
        :type ErrorCode: int
        :param ErrorMsg: Error message.
        :type ErrorMsg: str
        """
        self.FinishReason = None
        self.ExceptionCnt = None
        self.RoomId = None
        self.GroupId = None
        self.RecordStartTime = None
        self.RecordStopTime = None
        self.TotalTime = None
        self.VideoInfos = None
        self.OmittedDurations = None
        self.Details = None
        self.ErrorCode = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.ExceptionCnt = params.get("ExceptionCnt")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.RecordStartTime = params.get("RecordStartTime")
        self.RecordStopTime = params.get("RecordStopTime")
        self.TotalTime = params.get("TotalTime")
        if params.get("VideoInfos") is not None:
            self.VideoInfos = []
            for item in params.get("VideoInfos"):
                obj = VideoInfo()
                obj._deserialize(item)
                self.VideoInfos.append(obj)
        if params.get("OmittedDurations") is not None:
            self.OmittedDurations = []
            for item in params.get("OmittedDurations"):
                obj = OmittedDuration()
                obj._deserialize(item)
                self.OmittedDurations.append(obj)
        self.Details = params.get("Details")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTaskSearchResult(AbstractModel):
    """Real-time recording task query results.

    """

    def __init__(self):
        r"""
        :param TaskId: Unique task ID.
        :type TaskId: str
        :param Status: Status of the real-time recording task.
- PAUSED: Recording paused.
- PREPARED: Recording in preparation.
- RECORDING: Recording in progress.
- STOPPED: Recording stopped.
- FINISHED: Recording finished.
        :type Status: str
        :param RoomId: Room ID of the real-time recording task.
        :type RoomId: int
        :param CreateTime: Creation time of the task.
        :type CreateTime: str
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param Result: Real-time recording result.
        :type Result: :class:`tencentcloud.tiw.v20190919.models.RecordTaskResult`
        """
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.CreateTime = None
        self.SdkAppId = None
        self.Result = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.CreateTime = params.get("CreateTime")
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self.Result = RecordTaskResult()
            self.Result._deserialize(params.get("Result"))
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


class RoomListItem(AbstractModel):
    """Whiteboard room data returned for log queries.

    """

    def __init__(self):
        r"""
        :param RoomId: Room ID.
        :type RoomId: str
        :param StartTime: The first time when the room ID appeared during the queried period, which is a Unix timestamp in milliseconds.
        :type StartTime: int
        :param EndTime: The last time when the room ID appeared during the queried period, which is a Unix timestamp in milliseconds.
        :type EndTime: int
        :param UserNumber: Number of users in the room.
        :type UserNumber: int
        """
        self.RoomId = None
        self.StartTime = None
        self.EndTime = None
        self.UserNumber = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserNumber = params.get("UserNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoomUsageDataItem(AbstractModel):
    """Usage information of the room.

    """

    def __init__(self):
        r"""
        :param Time: Start date in the format of YYYY-MM-DD.
        :type Time: str
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param SubProduct: Subproduct usage information, which is consistent with the corresponding request parameters.
- sp_tiw_board: The duration of use of whiteboards.
- sp_tiw_ric: The duration of real-time recording.
        :type SubProduct: str
        :param Value: Usage values.
- The unit of sp_tiw_board and sp_tiw_ric is minutes.
        :type Value: float
        :param RoomID: 
        :type RoomID: int
        """
        self.Time = None
        self.SdkAppId = None
        self.SubProduct = None
        self.Value = None
        self.RoomID = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.SdkAppId = params.get("SdkAppId")
        self.SubProduct = params.get("SubProduct")
        self.Value = params.get("Value")
        self.RoomID = params.get("RoomID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOfflineRecordCallbackRequest(AbstractModel):
    """SetOfflineRecordCallback request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param Callback: Callback URL of the offline recording task result. If it is specified as null, the set callback URL is deleted. The callback URL only supports the HTTP or HTTPS protocol, and therefore the callback URL must start with `http://` or `https://`.
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
        


class SetOfflineRecordCallbackResponse(AbstractModel):
    """SetOfflineRecordCallback response structure.

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


class SetVideoGenerationTaskCallbackKeyRequest(AbstractModel):
    """SetVideoGenerationTaskCallbackKey request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param CallbackKey: Callback authentication key for recording video generation. It is a string that can have up to 64 characters. If an empty string is passed in, the existing callback authentication key is deleted.
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
        


class SetVideoGenerationTaskCallbackKeyResponse(AbstractModel):
    """SetVideoGenerationTaskCallbackKey response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetVideoGenerationTaskCallbackRequest(AbstractModel):
    """SetVideoGenerationTaskCallback request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param Callback: Callback URL of the offline recording task result. If it is specified as null, the set callback URL is deleted. The callback URL only supports the HTTP or HTTPS protocol, and therefore the callback URL must start with `http://` or `https://`.
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
        


class SetVideoGenerationTaskCallbackResponse(AbstractModel):
    """SetVideoGenerationTaskCallback response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetWhiteboardPushCallbackKeyRequest(AbstractModel):
    """SetWhiteboardPushCallbackKey request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param CallbackKey: Callback authentication key for whiteboard push. It is a string that can have up to 64 characters. If an empty string is passed in, the existing callback authentication key is deleted. For more information, see [Event Notification](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1).
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
        


class SetWhiteboardPushCallbackKeyResponse(AbstractModel):
    """SetWhiteboardPushCallbackKey response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetWhiteboardPushCallbackRequest(AbstractModel):
    """SetWhiteboardPushCallback request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param Callback: Callback URL of the whiteboard push task result. If an empty string is passed in, the existing callback URL is deleted. The callback URL only supports the HTTP or HTTPS protocol, and therefore the callback URL must start with `http://` or `https://`. For the callback format, see [Event Notification](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1).
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
        


class SetWhiteboardPushCallbackResponse(AbstractModel):
    """SetWhiteboardPushCallback response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SnapshotCOS(AbstractModel):
    """COS bucket parameters for storing whiteboard snapshots.

    """

    def __init__(self):
        r"""
        :param Uin: UIN of the Tencent Cloud account.
        :type Uin: int
        :param Region: COS region.
        :type Region: str
        :param Bucket: COS bucket name.
        :type Bucket: str
        :param TargetDir: Root directory for storing whiteboard snapshots.
        :type TargetDir: str
        :param Domain: CDN acceleration domain name.
        :type Domain: str
        """
        self.Uin = None
        self.Region = None
        self.Bucket = None
        self.TargetDir = None
        self.Domain = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.TargetDir = params.get("TargetDir")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotResult(AbstractModel):
    """Result of the whiteboard snapshot task.

    """

    def __init__(self):
        r"""
        :param ErrorCode: Task execution error code.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type ErrorCode: str
        :param ErrorMessage: Task execution error message.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type ErrorMessage: str
        :param Total: Number of generated snapshot images.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param Snapshots: List of URLs of the snapshot images.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Snapshots: list of str
        """
        self.ErrorCode = None
        self.ErrorMessage = None
        self.Total = None
        self.Snapshots = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        self.Total = params.get("Total")
        self.Snapshots = params.get("Snapshots")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotWhiteboard(AbstractModel):
    """Whiteboard parameters of the whiteboard snapshot task, such as the width and height of the whiteboard.

    """

    def __init__(self):
        r"""
        :param Width: Whiteboard width. Valid range: [0,2560]. Default value: 1280.
        :type Width: int
        :param Height: Whiteboard height. Valid range: [0,2560]. Default value: 720.
        :type Height: int
        :param InitParams: Escaped JSON string of the whiteboard initial parameters, which is passed through to the Tencent Interactive Whiteboard SDK.
        :type InitParams: str
        """
        self.Width = None
        self.Height = None
        self.InitParams = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.InitParams = params.get("InitParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartOnlineRecordRequest(AbstractModel):
    """StartOnlineRecord request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the customer
        :type SdkAppId: int
        :param RoomId: ID of the room for recording. Value range: (1, 4294967295)
        :type RoomId: int
        :param RecordUserId: User ID used by the recording service for entering a room. The ID cannot exceed 60 bytes in length. Its format is `tic_record_user_${RoomId}_${Random}`, where `${RoomId}` indicates the ID of the room for recording and `${Random}` is a random string.
The ID must be an unused ID in the SDK. The recording service uses the user ID to enter the room for audio, video, and whiteboard recording. If this ID is already used in the SDK, the SDK and recording service will conflict, affecting the recording operation.
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
        :param RecordMode: 
        :type RecordMode: str
        :param ChatGroupId: 
        :type ChatGroupId: str
        :param AutoStopTimeout: Recording timeout. Unit: seconds. Valid range: [300,86400]. Default value: 300.

If no upstream audio/video exists or no operation is performed on the whiteboard for the specified period of time, the recording service automatically stops the recording task.
        :type AutoStopTimeout: int
        :param ExtraData: Internal parameter. You can ignore this parameter.
        :type ExtraData: str
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
        self.RecordMode = None
        self.ChatGroupId = None
        self.AutoStopTimeout = None
        self.ExtraData = None


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
        self.RecordMode = params.get("RecordMode")
        self.ChatGroupId = params.get("ChatGroupId")
        self.AutoStopTimeout = params.get("AutoStopTimeout")
        self.ExtraData = params.get("ExtraData")
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


class StartWhiteboardPushRequest(AbstractModel):
    """StartWhiteboardPush request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param RoomId: Room ID of the whiteboard push task. Valid range: (1,4294967295).

1. By default, the whiteboard push task uses the RoomId string as the GroupID of the IM group. For example, if the RoomId string is 1234, the GroupID of the IM group is also 1234. Message synchronization requires joining a group. Make sure that an IM group is created before the push starts. Otherwise, the push fails.
2. If neither TRTCRoomId nor TRTCRoomIdStr is specified, the value of RoomId is used as the Tencent Real-Time Communication (TRTC) room ID for the whiteboard push task.
        :type RoomId: int
        :param PushUserId: User ID used by the whiteboard push service for entering the whiteboard room. If `IMAuthParam`and `TRTCAuthParam` are not specified, this user ID is used for operations such as logging in to the IM application, joining an IM group, and entering the room for TRTC whiteboard push.
The ID cannot exceed 60 bytes in length and must be an unused ID. The whiteboard push service uses the user ID to enter the room for whiteboard audio/video push. If this ID is already used in another scenario, the other scenario and whiteboard push service will conflict, affecting the pushing operation.
        :type PushUserId: str
        :param PushUserSig: User's IM signature corresponding to the PushUserId.
        :type PushUserSig: str
        :param Whiteboard: Whiteboard parameters, such as the width, height, and background color of the whiteboard.
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param AutoStopTimeout: Whiteboard push timeout. Unit: seconds. Valid range: [300,259200]. Default value: 1800.

If no operation is performed on the whiteboard for the specified period of time, the whiteboard push service automatically stops whiteboard push.
        :type AutoStopTimeout: int
        :param AutoManageBackup: Specifies whether to synchronize operations on the primary whiteboard push task to the backup task.
        :type AutoManageBackup: bool
        :param Backup: Parameters of the backup whiteboard push task.

After the backup parameters are specified, the whiteboard push service adds a relayed video stream. That is, there are two video streams on the whiteboard in the same room.
        :type Backup: :class:`tencentcloud.tiw.v20190919.models.WhiteboardPushBackupParam`
        :param PrivateMapKey: Advanced permission control parameter in TRTC. If the advanced permission control feature is enabled in TRTC, this parameter is required.
        :type PrivateMapKey: str
        :param VideoFPS: Frame rate of the whiteboard push video. Valid range: [0,30]. Default value: 20. Unit: fps.
        :type VideoFPS: int
        :param VideoBitrate: Whiteboard push bitrate. Valid range: [0,2000]. Default value: 1200. Unit: kbps.

The bitrate specified here is a reference value. During actual push, a dynamic bitrate is used. The actual bitrate does not remain the specified value but rather fluctuates around it.
        :type VideoBitrate: int
        :param AutoRecord: Specifies whether to automatically record the whiteboard push when the recording mode in TRTC is set to `SubscribeStreamUserIds`.

Default value: `false`. If you need to enable automatic whiteboard push recording, set this parameter to `true`.

If the recording mode in TRTC is set to `Global Auto Recording`, ignore this parameter.
        :type AutoRecord: bool
        :param UserDefinedRecordId: ID of the whiteboard push recording. The ID is filled in the `userdefinerecordid` parameter in the callback message after cloud recording is complete in TRTC, helping you identify the recording callback and locate the video file in VOD media resource management.

The value can be up to 64 bytes in length and contain letters (a-z and A-Z), digits (0-9), underscores (_), and hyphens (-).

After this parameter is set, automatic whiteboard push recording is enabled regardless of the value of the `AutoRecord` parameter.

Default RecordId generation rule:
urlencode(SdkAppID_RoomID_PushUserID)

Example:
SdkAppID = 12345678，RoomID = 12345，PushUserID = push_user_1
Therefore: RecordId = 12345678_12345_push_user_1
        :type UserDefinedRecordId: str
        :param AutoPublish: Specifies whether to enable automatic relay whiteboard push when the relay push mode in TRTC is set to `SubscribeRelayUserIds`.

Default value: `false`. If you need to enable automatic relay whiteboard push, set this parameter to `true`.

If the recording mode in TRTC is set to `Global Auto Relay`, ignore this parameter.
        :type AutoPublish: bool
        :param UserDefinedStreamId: Stream ID used by TRTC for relay whiteboard push. With this ID, you can stream the user’s audio/video by using the domain name and standard streaming solution (FLV or HLS) in TRTC.

The value can be up to 64 bytes in length and contain letters (a-z and A-Z), digits (0-9), underscores (_), and hyphens (-).

After this parameter is set, automatic relay whiteboard push is enabled regardless of the value of the `AutoPublish` parameter.

Default StreamID generation rule:
urlencode(SdkAppID_RoomID_PushUserID_main)

Example:
SdkAppID = 12345678，RoomID = 12345，PushUserID = push_user_1
Therefore, StreamID = 12345678_12345_push_user_1_main
        :type UserDefinedStreamId: str
        :param ExtraData: Internal parameter. You can ignore this parameter.
        :type ExtraData: str
        :param TRTCRoomId: TRTC room ID of the numeric type. Valid range: (1,4294967295).

If RoomId and TRTCRoomId are both specified, the value of TRTCRoomId takes priority as the room ID for TRTC whiteboard push.

If the TRTCRoomIdStr parameter is specified, this parameter is ignored.
        :type TRTCRoomId: int
        :param TRTCRoomIdStr: TRTC room ID of the string type.

If TRTCRoomIdStr is specified, its value takes priority as the room ID for TRTC whiteboard push.
        :type TRTCRoomIdStr: str
        :param IMAuthParam: IM authentication parameters.
If the ID of the IM application used by whiteboard messages is different from SdkAppId of the whiteboard application, specify this parameter to provide authentication information of the IM application.

If this parameter is specified, the whiteboard push service preferably uses the SdkAppId value in this parameter as the transmission channel for whiteboard messages. If this parameter is left empty, the SdkAppId value in the common parameters is used.
        :type IMAuthParam: :class:`tencentcloud.tiw.v20190919.models.AuthParam`
        :param TRTCAuthParam: TRTC authentication parameters, used for room entrance authentication for TRTC push.
If the ID of the TRTC application to which the target TRTC room belongs is different from SdkAppId of the whiteboard application, specify this parameter to provide authentication information of the TRTC application.

If this parameter is specified, the whiteboard push service preferably uses the SdkAppId value in this parameter as the ID of the target TRTC application. If this parameter is left empty, the SdkAppId value in the common parameters is used.
        :type TRTCAuthParam: :class:`tencentcloud.tiw.v20190919.models.AuthParam`
        :param TRTCEnterRoomMode: This parameter is available only to users in the allowlist for trial.

TRTC room entrance mode for whiteboard push. Default value: `TRTCAppSceneVideoCall`.

`TRTCAppSceneVideoCall`: This scenario is most suitable when there are two or more people on a video call. The internal encoders and network protocols are optimized for video smoothness to reduce call latency and lagging.
`TRTCAppSceneLIVE`: This scenario is most suitable when there is only one person speaking or performing for an online audience, and occasionally multiple people interact with one another through video. The internal encoders and network protocols are optimized for performance and compatibility to deliver better performance and video clarity.
        :type TRTCEnterRoomMode: str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.PushUserId = None
        self.PushUserSig = None
        self.Whiteboard = None
        self.AutoStopTimeout = None
        self.AutoManageBackup = None
        self.Backup = None
        self.PrivateMapKey = None
        self.VideoFPS = None
        self.VideoBitrate = None
        self.AutoRecord = None
        self.UserDefinedRecordId = None
        self.AutoPublish = None
        self.UserDefinedStreamId = None
        self.ExtraData = None
        self.TRTCRoomId = None
        self.TRTCRoomIdStr = None
        self.IMAuthParam = None
        self.TRTCAuthParam = None
        self.TRTCEnterRoomMode = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.PushUserId = params.get("PushUserId")
        self.PushUserSig = params.get("PushUserSig")
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        self.AutoStopTimeout = params.get("AutoStopTimeout")
        self.AutoManageBackup = params.get("AutoManageBackup")
        if params.get("Backup") is not None:
            self.Backup = WhiteboardPushBackupParam()
            self.Backup._deserialize(params.get("Backup"))
        self.PrivateMapKey = params.get("PrivateMapKey")
        self.VideoFPS = params.get("VideoFPS")
        self.VideoBitrate = params.get("VideoBitrate")
        self.AutoRecord = params.get("AutoRecord")
        self.UserDefinedRecordId = params.get("UserDefinedRecordId")
        self.AutoPublish = params.get("AutoPublish")
        self.UserDefinedStreamId = params.get("UserDefinedStreamId")
        self.ExtraData = params.get("ExtraData")
        self.TRTCRoomId = params.get("TRTCRoomId")
        self.TRTCRoomIdStr = params.get("TRTCRoomIdStr")
        if params.get("IMAuthParam") is not None:
            self.IMAuthParam = AuthParam()
            self.IMAuthParam._deserialize(params.get("IMAuthParam"))
        if params.get("TRTCAuthParam") is not None:
            self.TRTCAuthParam = AuthParam()
            self.TRTCAuthParam._deserialize(params.get("TRTCAuthParam"))
        self.TRTCEnterRoomMode = params.get("TRTCEnterRoomMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartWhiteboardPushResponse(AbstractModel):
    """StartWhiteboardPush response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Push task ID.
        :type TaskId: str
        :param Backup: Result parameters of the backup task.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Backup: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.Backup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Backup = params.get("Backup")
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


class StopWhiteboardPushRequest(AbstractModel):
    """StopWhiteboardPush request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param TaskId: ID of the whiteboard push task to be stopped.
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
        


class StopWhiteboardPushResponse(AbstractModel):
    """StopWhiteboardPush response structure.

    """

    def __init__(self):
        r"""
        :param Backup: Parameters of the backup task.
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Backup: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Backup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Backup = params.get("Backup")
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
        


class Tag(AbstractModel):
    """Tag information.

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key.
        :type TagKey: str
        :param TagValue: Tag value.
        :type TagValue: str
        """
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
        


class TimeValue(AbstractModel):
    """Time series returned for the queried metric.

    """

    def __init__(self):
        r"""
        :param Time: Unix timestamp in seconds.
        :type Time: int
        :param Value: Current value of the queried metric.
        :type Value: float
        """
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
        


class TranscodeTaskResult(AbstractModel):
    """Transcoding task result.

    """

    def __init__(self):
        r"""
        :param ResultUrl: Transcoding result URL.
        :type ResultUrl: str
        :param Resolution: Target resolution.
        :type Resolution: str
        :param Title: Title (usually the document name).
        :type Title: str
        :param Pages: Number of transcoded pages.
        :type Pages: int
        :param ThumbnailUrl: URL prefix of the thumbnail. If the URL prefix is `http://example.com/g0jb42ps49vtebjshilb/`, the thumbnail URL for the first page of the dynamically transcoded PowerPoint file is
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`, and so on.

If the document transcoding request carries the ThumbnailResolution parameter and the transcoding type is dynamic transcoding, this parameter is not null. In other cases, this parameter is null.
        :type ThumbnailUrl: str
        :param ThumbnailResolution: Resolution of the thumbnail generated for dynamic transcoding
        :type ThumbnailResolution: str
        :param CompressFileUrl: URL for downloading the transcoded and compressed file. If `CompressFileType` carried in the document transcoding request is null or is not a supported compression format, this parameter is null.
        :type CompressFileUrl: str
        :param ErrorCode: Task execution error code.
        :type ErrorCode: int
        :param ErrorMsg: Task execution error message.
        :type ErrorMsg: str
        """
        self.ResultUrl = None
        self.Resolution = None
        self.Title = None
        self.Pages = None
        self.ThumbnailUrl = None
        self.ThumbnailResolution = None
        self.CompressFileUrl = None
        self.ErrorCode = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.ResultUrl = params.get("ResultUrl")
        self.Resolution = params.get("Resolution")
        self.Title = params.get("Title")
        self.Pages = params.get("Pages")
        self.ThumbnailUrl = params.get("ThumbnailUrl")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileUrl = params.get("CompressFileUrl")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskSearchResult(AbstractModel):
    """Transcoding task query results.

    """

    def __init__(self):
        r"""
        :param CreateTime: Creation time of the task.
        :type CreateTime: str
        :param TaskId: Unique task ID.
        :type TaskId: str
        :param Status: Current task status.
- QUEUED: Queuing for transcoding.
- PROCESSING: Transcoding in progress.
- FINISHED: Transcoding finished.
        :type Status: str
        :param OriginalFilename: Original name of the transcoded document.
        :type OriginalFilename: str
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param Result: Transcoding task result.
        :type Result: :class:`tencentcloud.tiw.v20190919.models.TranscodeTaskResult`
        :param IsStatic: Specifies whether the transcoding is static.
        :type IsStatic: bool
        """
        self.CreateTime = None
        self.TaskId = None
        self.Status = None
        self.OriginalFilename = None
        self.SdkAppId = None
        self.Result = None
        self.IsStatic = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.OriginalFilename = params.get("OriginalFilename")
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self.Result = TranscodeTaskResult()
            self.Result._deserialize(params.get("Result"))
        self.IsStatic = params.get("IsStatic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDataItem(AbstractModel):
    """Tencent Interactive Whiteboard usage information.

    """

    def __init__(self):
        r"""
        :param Time: Start date in the format of YYYY-MM-DD.
        :type Time: str
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param SubProduct: Subproduct usage information, which is consistent with the corresponding request parameters.
- sp_tiw_board: The duration of use of whiteboards.
- sp_tiw_dt: The number of pages dynamically transcoded.
- sp_tiw_st: The number of pages statically transcoded.
- sp_tiw_ric: The duration of real-time recording.
        :type SubProduct: str
        :param Value: Usage values.
- The unit of sp_tiw_dt and sp_tiw_st is pages.
- The unit of sp_tiw_board and sp_tiw_ric is minutes.
        :type Value: float
        """
        self.Time = None
        self.SdkAppId = None
        self.SubProduct = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.SdkAppId = params.get("SdkAppId")
        self.SubProduct = params.get("SubProduct")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserListItem(AbstractModel):
    """Whiteboard user data returned for log queries.

    """

    def __init__(self):
        r"""
        :param UserId: User ID in the room.
        :type UserId: str
        :param StartTime: The first time when the user ID appeared during the queried period, which is a Unix timestamp in milliseconds.
        :type StartTime: int
        :param EndTime: The last time when the user ID appeared during the queried period, which is a Unix timestamp in milliseconds.
        :type EndTime: int
        """
        self.UserId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
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
        :param Width: Whiteboard video width in the real-time recording result. The value must be equal to or greater than 2. Default value: 1280.
        :type Width: int
        :param Height: Whiteboard video height in the real-time recording result. The value must be equal to or greater than 2. Default value: 960.
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
        


class WhiteboardApplicationConfig(AbstractModel):
    """Whiteboard application configuration, including the resource bucket, domain name, callback URL, and callback key.

    """

    def __init__(self):
        r"""
        :param TaskType: Task type.

recording: Real-time recording.
transcode: Document transcoding.
        :type TaskType: str
        :param BucketName: Bucket name.
        :type BucketName: str
        :param BucketLocation: Region of the bucket.
        :type BucketLocation: str
        :param BucketPrefix: Resource prefix of the bucket.
        :type BucketPrefix: str
        :param ResultDomain: Destination CDN domain name.
        :type ResultDomain: str
        :param Callback: Callback URL.
        :type Callback: str
        :param CallbackKey: Callback authentication key.
        :type CallbackKey: str
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param AdminUserId: IM admin user ID.
        :type AdminUserId: str
        :param AdminUserSig: IM admin user signature.
        :type AdminUserSig: str
        """
        self.TaskType = None
        self.BucketName = None
        self.BucketLocation = None
        self.BucketPrefix = None
        self.ResultDomain = None
        self.Callback = None
        self.CallbackKey = None
        self.SdkAppId = None
        self.AdminUserId = None
        self.AdminUserSig = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.BucketName = params.get("BucketName")
        self.BucketLocation = params.get("BucketLocation")
        self.BucketPrefix = params.get("BucketPrefix")
        self.ResultDomain = params.get("ResultDomain")
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.SdkAppId = params.get("SdkAppId")
        self.AdminUserId = params.get("AdminUserId")
        self.AdminUserSig = params.get("AdminUserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushBackupParam(AbstractModel):
    """Backup-related request parameters of the whiteboard push task.

    """

    def __init__(self):
        r"""
        :param PushUserId: User ID used by the whiteboard push service for entering a room,
The ID must be an unused ID in the SDK. The whiteboard push service uses the user ID to enter the room for whiteboard push. If this ID is already used in the SDK, the SDK and recording service will conflict, affecting the pushing operation.
        :type PushUserId: str
        :param PushUserSig: Signature corresponding to the PushUserId ID.
        :type PushUserSig: str
        """
        self.PushUserId = None
        self.PushUserSig = None


    def _deserialize(self, params):
        self.PushUserId = params.get("PushUserId")
        self.PushUserSig = params.get("PushUserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushResult(AbstractModel):
    """Whiteboard push task result.

    """

    def __init__(self):
        r"""
        :param FinishReason: `AUTO`: Pushing automatically stops. `USER_CALL`: The API for stopping pushing is called.
        :type FinishReason: str
        :param ExceptionCnt: Number of exceptions.
        :type ExceptionCnt: int
        :param RoomId: Room ID.
        :type RoomId: int
        :param GroupId: IM group ID.
        :type GroupId: str
        :param PushStartTime: Actual push start time.
        :type PushStartTime: int
        :param PushStopTime: Push end time.
        :type PushStopTime: int
        :param IMSyncTime: IM timestamp corresponding to the first frame of the whiteboard push video. The timestamp is used for time synchronization between IM messages and the whiteboard push video during playback.
        :type IMSyncTime: int
        :param ErrorCode: Task execution error code.
        :type ErrorCode: int
        :param ErrorMsg: Error message.
        :type ErrorMsg: str
        """
        self.FinishReason = None
        self.ExceptionCnt = None
        self.RoomId = None
        self.GroupId = None
        self.PushStartTime = None
        self.PushStopTime = None
        self.IMSyncTime = None
        self.ErrorCode = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.ExceptionCnt = params.get("ExceptionCnt")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.PushStartTime = params.get("PushStartTime")
        self.PushStopTime = params.get("PushStopTime")
        self.IMSyncTime = params.get("IMSyncTime")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushTaskSearchResult(AbstractModel):
    """Real-time recording task query results.

    """

    def __init__(self):
        r"""
        :param TaskId: Unique task ID.
        :type TaskId: str
        :param Status: Status of the whiteboard push task.
- PREPARED: Push in preparation.
- PUSHING: Pushing in progress.
- STOPPED: Pushing stopped.
        :type Status: str
        :param RoomId: Room ID of the whiteboard push task.
        :type RoomId: int
        :param CreateTime: Creation time of the task.
        :type CreateTime: str
        :param SdkAppId: SdkAppId of the whiteboard application.
        :type SdkAppId: int
        :param Result: Whiteboard push result.
        :type Result: :class:`tencentcloud.tiw.v20190919.models.WhiteboardPushResult`
        :param PushUserId: User ID of the whiteboard push task.
        :type PushUserId: str
        """
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.CreateTime = None
        self.SdkAppId = None
        self.Result = None
        self.PushUserId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.CreateTime = params.get("CreateTime")
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self.Result = WhiteboardPushResult()
            self.Result._deserialize(params.get("Result"))
        self.PushUserId = params.get("PushUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        