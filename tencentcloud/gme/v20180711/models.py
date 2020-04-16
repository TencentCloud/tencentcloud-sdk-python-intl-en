# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AppStatisticsItem(AbstractModel):
    """Application usage statistics

    """

    def __init__(self):
        """
        :param RealtimeSpeechStatisticsItem: Voice chat statistics
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealtimeSpeechStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealTimeSpeechStatisticsItem`
        :param VoiceMessageStatisticsItem: Voice messaging statistics
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoiceMessageStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceMessageStatisticsItem`
        :param VoiceFilterStatisticsItem: Phrase filtering statistics
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoiceFilterStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceFilterStatisticsItem`
        :param Date: Statistical period
        :type Date: str
        """
        self.RealtimeSpeechStatisticsItem = None
        self.VoiceMessageStatisticsItem = None
        self.VoiceFilterStatisticsItem = None
        self.Date = None


    def _deserialize(self, params):
        if params.get("RealtimeSpeechStatisticsItem") is not None:
            self.RealtimeSpeechStatisticsItem = RealTimeSpeechStatisticsItem()
            self.RealtimeSpeechStatisticsItem._deserialize(params.get("RealtimeSpeechStatisticsItem"))
        if params.get("VoiceMessageStatisticsItem") is not None:
            self.VoiceMessageStatisticsItem = VoiceMessageStatisticsItem()
            self.VoiceMessageStatisticsItem._deserialize(params.get("VoiceMessageStatisticsItem"))
        if params.get("VoiceFilterStatisticsItem") is not None:
            self.VoiceFilterStatisticsItem = VoiceFilterStatisticsItem()
            self.VoiceFilterStatisticsItem._deserialize(params.get("VoiceFilterStatisticsItem"))
        self.Date = params.get("Date")


class CreateAppRequest(AbstractModel):
    """CreateApp request structure.

    """

    def __init__(self):
        """
        :param AppName: Application name
        :type AppName: str
        :param ProjectId: Tencent Cloud project ID. Default value: 0, which means the default project
        :type ProjectId: int
        :param EngineList: List of engines to be supported. All values are selected by default.
        :type EngineList: list of str
        :param RegionList: Service region list. All values are selected by default.
        :type RegionList: list of str
        :param RealtimeSpeechConf: Configuration information of voice chat
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param VoiceMessageConf: Configuration information of voice messaging and speech-to-text
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param VoiceFilterConf: Configuration information of phrase analysis
        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        :param Tags: List of tags to be added
        :type Tags: list of Tag
        """
        self.AppName = None
        self.ProjectId = None
        self.EngineList = None
        self.RegionList = None
        self.RealtimeSpeechConf = None
        self.VoiceMessageConf = None
        self.VoiceFilterConf = None
        self.Tags = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.ProjectId = params.get("ProjectId")
        self.EngineList = params.get("EngineList")
        self.RegionList = params.get("RegionList")
        if params.get("RealtimeSpeechConf") is not None:
            self.RealtimeSpeechConf = RealtimeSpeechConf()
            self.RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self.VoiceMessageConf = VoiceMessageConf()
            self.VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self.VoiceFilterConf = VoiceFilterConf()
            self.VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateAppResponse(AbstractModel):
    """CreateApp output parameters

    """

    def __init__(self):
        """
        :param BizId: Application ID, which is automatically generated by the backend.
        :type BizId: int
        :param AppName: Application name, which is passed through from the `AppName` input parameter
        :type AppName: str
        :param ProjectId: Project ID, which is passed through from the entered `ProjectId`
        :type ProjectId: int
        :param SecretKey: Application key, which is used when the GME SDK is initialized
        :type SecretKey: str
        :param CreateTime: Service creation timestamp
        :type CreateTime: int
        :param RealtimeSpeechConf: Configuration information of voice chat
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param VoiceMessageConf: Configuration information of voice messaging and speech-to-text
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param VoiceFilterConf: Configuration information of phrase analysis
        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        """
        self.BizId = None
        self.AppName = None
        self.ProjectId = None
        self.SecretKey = None
        self.CreateTime = None
        self.RealtimeSpeechConf = None
        self.VoiceMessageConf = None
        self.VoiceFilterConf = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.AppName = params.get("AppName")
        self.ProjectId = params.get("ProjectId")
        self.SecretKey = params.get("SecretKey")
        self.CreateTime = params.get("CreateTime")
        if params.get("RealtimeSpeechConf") is not None:
            self.RealtimeSpeechConf = RealtimeSpeechConf()
            self.RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self.VoiceMessageConf = VoiceMessageConf()
            self.VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self.VoiceFilterConf = VoiceFilterConf()
            self.VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))


class DescribeAppStatisticsRequest(AbstractModel):
    """DescribeAppStatistics request structure.

    """

    def __init__(self):
        """
        :param BizId: GME application ID
        :type BizId: int
        :param StartDate: Data start date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13
        :type StartDate: str
        :param EndDate: Data end date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13
        :type EndDate: str
        :param Services: List of services to be queried. Valid values: RealTimeSpeech, VoiceMessage, VoiceFilter
        :type Services: list of str
        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None
        self.Services = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Services = params.get("Services")


class DescribeAppStatisticsResponse(AbstractModel):
    """Gets application usage statistics output parameters

    """

    def __init__(self):
        """
        :param AppStatistics: Application usage statistics
        :type AppStatistics: list of AppStatisticsItem
        """
        self.AppStatistics = None


    def _deserialize(self, params):
        if params.get("AppStatistics") is not None:
            self.AppStatistics = []
            for item in params.get("AppStatistics"):
                obj = AppStatisticsItem()
                obj._deserialize(item)
                self.AppStatistics.append(obj)


class DescribeScanResult(AbstractModel):
    """Returned speech detection result

    """

    def __init__(self):
        """
        :param Code: Business return code
        :type Code: int
        :param DataId: Unique data ID
        :type DataId: str
        :param ScanFinishTime: Detection completion timestamp
        :type ScanFinishTime: int
        :param HitFlag: Whether non-compliant information is detected
        :type HitFlag: bool
        :param Live: Whether it is a stream
        :type Live: bool
        :param Msg: Business return description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param ScanPiece: Detection result, which will be returned if `Code` is 0
Note: this field may return null, indicating that no valid values can be obtained.
        :type ScanPiece: list of ScanPiece
        :param ScanStartTime: Detection task submission timestamp
        :type ScanStartTime: int
        :param Scenes: Speech detection scenario, which corresponds to the `Scene` at the time of request
        :type Scenes: list of str
        :param TaskId: Speech detection task ID, which is assigned by the backend
        :type TaskId: str
        :param Url: File or stream address
        :type Url: str
        :param Status: Detection task execution result task. Valid values:
<li>Start: task started</li>
<li>Success: task ended successfully</li>
<li>Error: exceptional</li>
        :type Status: str
        """
        self.Code = None
        self.DataId = None
        self.ScanFinishTime = None
        self.HitFlag = None
        self.Live = None
        self.Msg = None
        self.ScanPiece = None
        self.ScanStartTime = None
        self.Scenes = None
        self.TaskId = None
        self.Url = None
        self.Status = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.DataId = params.get("DataId")
        self.ScanFinishTime = params.get("ScanFinishTime")
        self.HitFlag = params.get("HitFlag")
        self.Live = params.get("Live")
        self.Msg = params.get("Msg")
        if params.get("ScanPiece") is not None:
            self.ScanPiece = []
            for item in params.get("ScanPiece"):
                obj = ScanPiece()
                obj._deserialize(item)
                self.ScanPiece.append(obj)
        self.ScanStartTime = params.get("ScanStartTime")
        self.Scenes = params.get("Scenes")
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")


class DescribeScanResultListRequest(AbstractModel):
    """DescribeScanResultList request structure.

    """

    def __init__(self):
        """
        :param BizId: Application ID, which is the `AppID` obtained when you create an application in the [console](https://console.cloud.tencent.com/gamegme)
        :type BizId: int
        :param TaskIdList: List of IDs of the tasks to be queried. Up to 100 entries can be added in the ID list.
        :type TaskIdList: list of str
        :param Limit: Number of task results to be returned. Default value: 10. Maximum value: 500. This parameter will be ignored for large file tasks where all results will be returned
        :type Limit: int
        """
        self.BizId = None
        self.TaskIdList = None
        self.Limit = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.TaskIdList = params.get("TaskIdList")
        self.Limit = params.get("Limit")


class DescribeScanResultListResponse(AbstractModel):
    """DescribeScanResultList response structure.

    """

    def __init__(self):
        """
        :param Data: Result of the speech detection task to be queried
Note: this field may return null, indicating that no valid values can be obtained.
        :type Data: list of DescribeScanResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DescribeScanResult()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyAppStatusRequest(AbstractModel):
    """ModifyAppStatus request structure.

    """

    def __init__(self):
        """
        :param BizId: Application ID, which is generated and returned by the backend after application creation.
        :type BizId: int
        :param Status: Application status. Valid values: open, close
        :type Status: str
        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")


class ModifyAppStatusResponse(AbstractModel):
    """ModifyAppStatus API output parameters

    """

    def __init__(self):
        """
        :param BizId: GME application ID
        :type BizId: int
        :param Status: Application status. Valid values: open, close
        :type Status: str
        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")


class RealTimeSpeechStatisticsItem(AbstractModel):
    """Voice chat usage statistics

    """

    def __init__(self):
        """
        :param MainLandDau: DAU in Mainland China
        :type MainLandDau: int
        :param MainLandPcu: PCU in Mainland China
        :type MainLandPcu: int
        :param MainLandDuration: Total duration of use in Mainland China in minutes
        :type MainLandDuration: int
        :param OverseaDau: DAU outside Mainland China
        :type OverseaDau: int
        :param OverseaPcu: PCU outside Mainland China
        :type OverseaPcu: int
        :param OverseaDuration: Total duration of use outside Mainland China in minutes
        :type OverseaDuration: int
        """
        self.MainLandDau = None
        self.MainLandPcu = None
        self.MainLandDuration = None
        self.OverseaDau = None
        self.OverseaPcu = None
        self.OverseaDuration = None


    def _deserialize(self, params):
        self.MainLandDau = params.get("MainLandDau")
        self.MainLandPcu = params.get("MainLandPcu")
        self.MainLandDuration = params.get("MainLandDuration")
        self.OverseaDau = params.get("OverseaDau")
        self.OverseaPcu = params.get("OverseaPcu")
        self.OverseaDuration = params.get("OverseaDuration")


class RealtimeSpeechConf(AbstractModel):
    """Configuration information of voice chat

    """

    def __init__(self):
        """
        :param Status: Voice chat status. Valid values: open, close
        :type Status: str
        :param Quality: Voice chat sound quality type. Valid values: high (HD), ordinary (SD). Default value: high. SD sound quality is only available to whitelisted users. To try it out, please contact your Tencent Cloud rep.
        :type Quality: str
        """
        self.Status = None
        self.Quality = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Quality = params.get("Quality")


class ScanDetail(AbstractModel):
    """Speech detection details

    """

    def __init__(self):
        """
        :param Label: Violation scenario. For more information, please see the definition of <a href="https://cloud.tencent.com/document/product/607/37622#Label_Value">Label</a>
        :type Label: str
        :param Rate: Confidence score in scenario. Value range: [0.00,100.00]. The higher the score, the more likely the content is non-compliant
        :type Rate: str
        :param KeyWord: Non-compliant keyword
        :type KeyWord: str
        :param StartTime: Start time offset in milliseconds from 0 of keyword in audio
        :type StartTime: int
        :param EndTime: End time offset in milliseconds from 0 of keyword in audio
        :type EndTime: int
        """
        self.Label = None
        self.Rate = None
        self.KeyWord = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Rate = params.get("Rate")
        self.KeyWord = params.get("KeyWord")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ScanPiece(AbstractModel):
    """Speech detection result, which will be returned if `Code` is 0

    """

    def __init__(self):
        """
        :param DumpUrl: Audio retention address, which will be returned for stream detection. The audio will be retained for 30 minutes
Note: this field may return null, indicating that no valid values can be obtained.
        :type DumpUrl: str
        :param HitFlag: Whether non-compliant information is detected
        :type HitFlag: bool
        :param MainType: Main non-compliant content type
Note: this field may return null, indicating that no valid values can be obtained.
        :type MainType: str
        :param ScanDetail: Speech detection details
        :type ScanDetail: list of ScanDetail
        :param RoomId: GME voice chat room ID, which is the `RoomId` passed through when the task was submitted
Note: this field may return null, indicating that no valid values can be obtained.
        :type RoomId: str
        :param OpenId: GME voice chat user ID, which is the `OpenId` passed through when the task was submitted
Note: this field may return null, indicating that no valid values can be obtained.
        :type OpenId: str
        :param Info: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Info: str
        :param Offset: Offset time in milliseconds of segment in stream during stream detection
Note: this field may return null, indicating that no valid values can be obtained.
        :type Offset: int
        :param Duration: Segment duration during stream detection
Note: this field may return null, indicating that no valid values can be obtained.
        :type Duration: int
        :param PieceStartTime: Segment detection start time
Note: this field may return null, indicating that no valid values can be obtained.
        :type PieceStartTime: int
        """
        self.DumpUrl = None
        self.HitFlag = None
        self.MainType = None
        self.ScanDetail = None
        self.RoomId = None
        self.OpenId = None
        self.Info = None
        self.Offset = None
        self.Duration = None
        self.PieceStartTime = None


    def _deserialize(self, params):
        self.DumpUrl = params.get("DumpUrl")
        self.HitFlag = params.get("HitFlag")
        self.MainType = params.get("MainType")
        if params.get("ScanDetail") is not None:
            self.ScanDetail = []
            for item in params.get("ScanDetail"):
                obj = ScanDetail()
                obj._deserialize(item)
                self.ScanDetail.append(obj)
        self.RoomId = params.get("RoomId")
        self.OpenId = params.get("OpenId")
        self.Info = params.get("Info")
        self.Offset = params.get("Offset")
        self.Duration = params.get("Duration")
        self.PieceStartTime = params.get("PieceStartTime")


class ScanVoiceRequest(AbstractModel):
    """ScanVoice request structure.

    """

    def __init__(self):
        """
        :param BizId: Application ID, which is the `AppID` obtained when you create an application in [Console > Service Management](https://console.cloud.tencent.com/gamegme)
        :type BizId: int
        :param Scenes: Speech detection scenario. The value of this parameter is currently required to be `default`. Preset scenarios: abusive, pornographic, politically sensitive, advertising, terrorism, and prohibited scenarios. For specific values, please see the <a href="#Label_Value">Label description</a> above.
        :type Scenes: list of str
        :param Live: Whether it is a live stream. false: audio file detection, true: audio stream detection.
        :type Live: bool
        :param Tasks: Speech detection task list. Up to 100 tasks can be added in the list. The structure contains:
<li>DataId: unique data ID</li>
<li>Url: URL-encoded data file URL, which is a pull address if the detected speech is a stream</li>
        :type Tasks: list of Task
        :param Callback: Async callback address for detection result. For more information, please see the <a href="#Callback_Declare">callback description</a> above. (Note: if this field is empty, the detection result can only be obtained by calling the `DescribeScanResultList` API.)
        :type Callback: str
        """
        self.BizId = None
        self.Scenes = None
        self.Live = None
        self.Tasks = None
        self.Callback = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Scenes = params.get("Scenes")
        self.Live = params.get("Live")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Callback = params.get("Callback")


class ScanVoiceResponse(AbstractModel):
    """ScanVoice response structure.

    """

    def __init__(self):
        """
        :param Data: Speech detection return. The `Data` field is a JSON array where each element contains: <li>DataId: corresponding `DataId` in request.</li>
<li>TaskID: detection task ID, which is used to poll the speech detection result.</li>
        :type Data: list of ScanVoiceResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ScanVoiceResult()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ScanVoiceResult(AbstractModel):
    """Returned result of speech detection

    """

    def __init__(self):
        """
        :param DataId: Data ID
        :type DataId: str
        :param TaskId: Task ID
        :type TaskId: str
        """
        self.DataId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.TaskId = params.get("TaskId")


class Tag(AbstractModel):
    """Tag list

    """

    def __init__(self):
        """
        :param TagKey: Tag key
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param TagValue: Tag value
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class Task(AbstractModel):
    """Speech detection task list

    """

    def __init__(self):
        """
        :param DataId: Unique data ID
        :type DataId: str
        :param Url: URL-encoded data file URL, which is a pull address if the detected speech is a stream
        :type Url: str
        :param RoomId: GME voice chat room ID, which is entered during speech detection by GME voice chat
        :type RoomId: str
        :param OpenId: GME voice chat user ID, which is entered during speech detection by GME voice chat
        :type OpenId: str
        """
        self.DataId = None
        self.Url = None
        self.RoomId = None
        self.OpenId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Url = params.get("Url")
        self.RoomId = params.get("RoomId")
        self.OpenId = params.get("OpenId")


class VoiceFilterConf(AbstractModel):
    """Configuration information of phrase filtering

    """

    def __init__(self):
        """
        :param Status: Phrase filtering status. Valid values: open, close
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")


class VoiceFilterStatisticsItem(AbstractModel):
    """Phrase filtering usage statistics

    """

    def __init__(self):
        """
        :param Duration: Total duration of phrase filtering
        :type Duration: int
        """
        self.Duration = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")


class VoiceMessageConf(AbstractModel):
    """Configuration information of voice messaging and speech-to-text

    """

    def __init__(self):
        """
        :param Status: Voice messaging and speech-to-text status. Valid values: open, close
        :type Status: str
        :param Language: Language supported for voice messaging and speech-to-text. Valid values: all (all languages), cnen (Chinese and English). Default value: cnen
        :type Language: str
        """
        self.Status = None
        self.Language = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Language = params.get("Language")


class VoiceMessageStatisticsItem(AbstractModel):
    """Voice messaging usage statistics

    """

    def __init__(self):
        """
        :param Dau: DAU of voice messaging and speech-to-text
        :type Dau: int
        """
        self.Dau = None


    def _deserialize(self, params):
        self.Dau = params.get("Dau")