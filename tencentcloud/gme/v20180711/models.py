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


class AppStatisticsItem(AbstractModel):
    """Application usage statistics

    """

    def __init__(self):
        r"""
        :param RealtimeSpeechStatisticsItem: Voice Chat statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RealtimeSpeechStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealTimeSpeechStatisticsItem`
        :param VoiceMessageStatisticsItem: Voice Message statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VoiceMessageStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceMessageStatisticsItem`
        :param VoiceFilterStatisticsItem: Phrase Filtering statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VoiceFilterStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceFilterStatisticsItem`
        :param Date: Reference period
        :type Date: str
        :param AudioTextStatisticsItem: Recording-to-Text usage statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AudioTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.AudioTextStatisticsItem`
        :param StreamTextStatisticsItem: Stream-to-Text usage statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StreamTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.StreamTextStatisticsItem`
        :param OverseaTextStatisticsItem: Usage statistics of Voice-to-Text of outside-MLC requests
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OverseaTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.OverseaTextStatisticsItem`
        :param RealtimeTextStatisticsItem: Real-time Voice-to-Text usage statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RealtimeTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealtimeTextStatisticsItem`
        """
        self.RealtimeSpeechStatisticsItem = None
        self.VoiceMessageStatisticsItem = None
        self.VoiceFilterStatisticsItem = None
        self.Date = None
        self.AudioTextStatisticsItem = None
        self.StreamTextStatisticsItem = None
        self.OverseaTextStatisticsItem = None
        self.RealtimeTextStatisticsItem = None


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
        if params.get("AudioTextStatisticsItem") is not None:
            self.AudioTextStatisticsItem = AudioTextStatisticsItem()
            self.AudioTextStatisticsItem._deserialize(params.get("AudioTextStatisticsItem"))
        if params.get("StreamTextStatisticsItem") is not None:
            self.StreamTextStatisticsItem = StreamTextStatisticsItem()
            self.StreamTextStatisticsItem._deserialize(params.get("StreamTextStatisticsItem"))
        if params.get("OverseaTextStatisticsItem") is not None:
            self.OverseaTextStatisticsItem = OverseaTextStatisticsItem()
            self.OverseaTextStatisticsItem._deserialize(params.get("OverseaTextStatisticsItem"))
        if params.get("RealtimeTextStatisticsItem") is not None:
            self.RealtimeTextStatisticsItem = RealtimeTextStatisticsItem()
            self.RealtimeTextStatisticsItem._deserialize(params.get("RealtimeTextStatisticsItem"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationDataStatistics(AbstractModel):
    """Application statistics

    """

    def __init__(self):
        r"""
        :param BizId: Application ID
        :type BizId: int
        :param DauDataNum: Number of DAU metrics
        :type DauDataNum: int
        :param DauDataMainland: DAUs in the Chinese mainland
        :type DauDataMainland: list of StatisticsItem
        :param DauDataOversea: DAUs outside the Chinese mainland
        :type DauDataOversea: list of StatisticsItem
        :param DauDataSum: Total DAUs
        :type DauDataSum: list of StatisticsItem
        :param DurationDataNum: Number of Voice Chat metrics
        :type DurationDataNum: int
        :param DurationDataMainland: Duration of Voice Chat in the Chinese mainland (in minutes)
        :type DurationDataMainland: list of StatisticsItem
        :param DurationDataOversea: Duration of Voice Chat outside the Chinese mainland (in minutes)
        :type DurationDataOversea: list of StatisticsItem
        :param DurationDataSum: Total duration of Voice Chat (in minutes)
        :type DurationDataSum: list of StatisticsItem
        :param PcuDataNum: Number of PCU metrics
        :type PcuDataNum: int
        :param PcuDataMainland: PCUs in the Chinese mainland
        :type PcuDataMainland: list of StatisticsItem
        :param PcuDataOversea: PCUs outside the Chinese mainland
        :type PcuDataOversea: list of StatisticsItem
        :param PcuDataSum: Total PCUs
        :type PcuDataSum: list of StatisticsItem
        """
        self.BizId = None
        self.DauDataNum = None
        self.DauDataMainland = None
        self.DauDataOversea = None
        self.DauDataSum = None
        self.DurationDataNum = None
        self.DurationDataMainland = None
        self.DurationDataOversea = None
        self.DurationDataSum = None
        self.PcuDataNum = None
        self.PcuDataMainland = None
        self.PcuDataOversea = None
        self.PcuDataSum = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.DauDataNum = params.get("DauDataNum")
        if params.get("DauDataMainland") is not None:
            self.DauDataMainland = []
            for item in params.get("DauDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DauDataMainland.append(obj)
        if params.get("DauDataOversea") is not None:
            self.DauDataOversea = []
            for item in params.get("DauDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DauDataOversea.append(obj)
        if params.get("DauDataSum") is not None:
            self.DauDataSum = []
            for item in params.get("DauDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DauDataSum.append(obj)
        self.DurationDataNum = params.get("DurationDataNum")
        if params.get("DurationDataMainland") is not None:
            self.DurationDataMainland = []
            for item in params.get("DurationDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DurationDataMainland.append(obj)
        if params.get("DurationDataOversea") is not None:
            self.DurationDataOversea = []
            for item in params.get("DurationDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DurationDataOversea.append(obj)
        if params.get("DurationDataSum") is not None:
            self.DurationDataSum = []
            for item in params.get("DurationDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DurationDataSum.append(obj)
        self.PcuDataNum = params.get("PcuDataNum")
        if params.get("PcuDataMainland") is not None:
            self.PcuDataMainland = []
            for item in params.get("PcuDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.PcuDataMainland.append(obj)
        if params.get("PcuDataOversea") is not None:
            self.PcuDataOversea = []
            for item in params.get("PcuDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.PcuDataOversea.append(obj)
        if params.get("PcuDataSum") is not None:
            self.PcuDataSum = []
            for item in params.get("PcuDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.PcuDataSum.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTextStatisticsItem(AbstractModel):
    """Recording-to-Text usage statistics

    """

    def __init__(self):
        r"""
        :param Data: Statistical value (in seconds)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Data: float
        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppRequest(AbstractModel):
    """CreateApp request structure.

    """

    def __init__(self):
        r"""
        :param AppName: Application name
        :type AppName: str
        :param ProjectId: Tencent Cloud project ID. Default value: 0, which means that the default project is used.
        :type ProjectId: int
        :param EngineList: List of engines to be supported. All values are selected by default.
        :type EngineList: list of str
        :param RegionList: Service region list. All values are selected by default.
        :type RegionList: list of str
        :param RealtimeSpeechConf: Configuration information of Voice Chat
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param VoiceMessageConf: Configuration information of Voice Message Service
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param VoiceFilterConf: Configuration information of Voice Analysis Service
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResp(AbstractModel):
    """Output parameters of `CreateApp`

    """

    def __init__(self):
        r"""
        :param BizId: Application ID, automatically generated by the backend.
        :type BizId: int
        :param AppName: Application name, the input of `AppName`.
        :type AppName: str
        :param ProjectId: Project ID, the input of `ProjectId`.
        :type ProjectId: int
        :param SecretKey: Application key, used to initialize GME SDK.
        :type SecretKey: str
        :param CreateTime: Timestamp, indicating when the service is created.
        :type CreateTime: int
        :param RealtimeSpeechConf: Configuration information of Voice Chat
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param VoiceMessageConf: Configuration information of Voice Message Service
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param VoiceFilterConf: Configuration information of Voice Analysis Service
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResponse(AbstractModel):
    """CreateApp response structure.

    """

    def __init__(self):
        r"""
        :param Data: Returned data
        :type Data: :class:`tencentcloud.gme.v20180711.models.CreateAppResp`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CreateAppResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DeleteResult(AbstractModel):
    """Result of the operation to delete a room or remove members

    """

    def __init__(self):
        r"""
        :param Code: Status code. `0`: Succeeded. Others: Failed\
        :type Code: int
        :param ErrorMsg: Description
        :type ErrorMsg: str
        """
        self.Code = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomMemberRequest(AbstractModel):
    """DeleteRoomMember request structure.

    """

    def __init__(self):
        r"""
        :param RoomId: ID of the target room
        :type RoomId: str
        :param Uids: List of the members to remove
        :type Uids: list of str
        :param DeleteType: Operation type. `1`: Delete a room; `2`: Remove members
        :type DeleteType: int
        :param BizId: Application ID
        :type BizId: int
        """
        self.RoomId = None
        self.Uids = None
        self.DeleteType = None
        self.BizId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.Uids = params.get("Uids")
        self.DeleteType = params.get("DeleteType")
        self.BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomMemberResponse(AbstractModel):
    """DeleteRoomMember response structure.

    """

    def __init__(self):
        r"""
        :param DeleteResult: Result of the operation to delete a room or remove a member
        :type DeleteResult: :class:`tencentcloud.gme.v20180711.models.DeleteResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DeleteResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeleteResult") is not None:
            self.DeleteResult = DeleteResult()
            self.DeleteResult._deserialize(params.get("DeleteResult"))
        self.RequestId = params.get("RequestId")


class DescribeAppStatisticsRequest(AbstractModel):
    """DescribeAppStatistics request structure.

    """

    def __init__(self):
        r"""
        :param BizId: GME application ID
        :type BizId: int
        :param StartDate: Data start date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13.
        :type StartDate: str
        :param EndDate: Data end date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13.
        :type EndDate: str
        :param Services: List of services to be queried. Valid values: `RealTimeSpeech`, `VoiceMessage`, `VoiceFilter`, `SpeechToText`.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppStatisticsResp(AbstractModel):
    """Output parameters of application usage statistics

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppStatisticsResponse(AbstractModel):
    """DescribeAppStatistics response structure.

    """

    def __init__(self):
        r"""
        :param Data: Application usage statistics
        :type Data: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsResp`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeAppStatisticsResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationDataRequest(AbstractModel):
    """DescribeApplicationData request structure.

    """

    def __init__(self):
        r"""
        :param BizId: Application ID
        :type BizId: int
        :param StartDate: Data start date in the format of yyyy-mm-dd, such as 2018-07-13.
        :type StartDate: str
        :param EndDate: Data end date in the format of yyyy-mm-dd, such as 2018-07-13.
        :type EndDate: str
        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationDataResponse(AbstractModel):
    """DescribeApplicationData response structure.

    """

    def __init__(self):
        r"""
        :param Data: Application statistics
        :type Data: :class:`tencentcloud.gme.v20180711.models.ApplicationDataStatistics`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ApplicationDataStatistics()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRecordInfoRequest(AbstractModel):
    """DescribeRecordInfo request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: ID of the ongoing task, which is returned from the `StartRecord` API.
        :type TaskId: int
        :param BizId: Application ID.
        :type BizId: int
        """
        self.TaskId = None
        self.BizId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordInfoResponse(AbstractModel):
    """DescribeRecordInfo response structure.

    """

    def __init__(self):
        r"""
        :param RecordInfo: Information about the recording task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordInfo: list of RecordInfo
        :param RecordMode: Recording mode. Valid values: `1`: single stream; `2`: mixed streams; `3`: single stream and mixed streams.
        :type RecordMode: int
        :param RoomId: Room ID.
        :type RoomId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RecordInfo = None
        self.RecordMode = None
        self.RoomId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordInfo") is not None:
            self.RecordInfo = []
            for item in params.get("RecordInfo"):
                obj = RecordInfo()
                obj._deserialize(item)
                self.RecordInfo.append(obj)
        self.RecordMode = params.get("RecordMode")
        self.RoomId = params.get("RoomId")
        self.RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo request structure.

    """

    def __init__(self):
        r"""
        :param BizId: Application ID.
        :type BizId: int
        :param RoomId: Room ID.
        :type RoomId: str
        """
        self.BizId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: ID of the ongoing task, which is returned from the `StartRecord` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param RecordMode: Recording mode. Valid values: `1`: single stream; `2`: mixed streams; `3`: single stream and mixed streams.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordMode: int
        :param SubscribeRecordUserIds: Allowlist or blocklist for stream subscription.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubscribeRecordUserIds: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RecordMode = None
        self.SubscribeRecordUserIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RecordMode = params.get("RecordMode")
        if params.get("SubscribeRecordUserIds") is not None:
            self.SubscribeRecordUserIds = SubscribeRecordUserIds()
            self.SubscribeRecordUserIds._deserialize(params.get("SubscribeRecordUserIds"))
        self.RequestId = params.get("RequestId")


class ModifyAppStatusRequest(AbstractModel):
    """ModifyAppStatus request structure.

    """

    def __init__(self):
        r"""
        :param BizId: Application ID, which is generated and returned by the backend after the application creation.
        :type BizId: int
        :param Status: Application status. Valid values: `open`, `close`.
        :type Status: str
        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppStatusResp(AbstractModel):
    """Output parameters of `ModifyAppStatus`

    """

    def __init__(self):
        r"""
        :param BizId: GME application ID
        :type BizId: int
        :param Status: Application status. Valid values: `open`, `close`.
        :type Status: str
        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppStatusResponse(AbstractModel):
    """ModifyAppStatus response structure.

    """

    def __init__(self):
        r"""
        :param Data: Returned data
        :type Data: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusResp`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ModifyAppStatusResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ModifyRecordInfoRequest(AbstractModel):
    """ModifyRecordInfo request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: ID of the ongoing task, which is returned from the `StartRecord` API.
        :type TaskId: int
        :param RecordMode: Recording mode. Valid values: `1`: single stream; `2`: mixed streams; `3`: single stream and mixed streams.
        :type RecordMode: int
        :param BizId: Application ID.
        :type BizId: int
        :param SubscribeRecordUserIds: Allowlist or blocklist for stream subscription.
        :type SubscribeRecordUserIds: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        """
        self.TaskId = None
        self.RecordMode = None
        self.BizId = None
        self.SubscribeRecordUserIds = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RecordMode = params.get("RecordMode")
        self.BizId = params.get("BizId")
        if params.get("SubscribeRecordUserIds") is not None:
            self.SubscribeRecordUserIds = SubscribeRecordUserIds()
            self.SubscribeRecordUserIds._deserialize(params.get("SubscribeRecordUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordInfoResponse(AbstractModel):
    """ModifyRecordInfo response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OverseaTextStatisticsItem(AbstractModel):
    """Usage statistics of Voice-to-Text of outside-MLC requests

    """

    def __init__(self):
        r"""
        :param Data: Statistical value (in seconds)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Data: float
        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealTimeSpeechStatisticsItem(AbstractModel):
    """Voice Chat usage statistics

    """

    def __init__(self):
        r"""
        :param MainLandDau: DAUs in the Chinese mainland
        :type MainLandDau: int
        :param MainLandPcu: PCUs in the Chinese mainland
        :type MainLandPcu: int
        :param MainLandDuration: Total duration of use in the Chinese mainland (in minutes)
        :type MainLandDuration: int
        :param OverseaDau: DAUs outside the Chinese mainland
        :type OverseaDau: int
        :param OverseaPcu: PCUs outside the Chinese mainland
        :type OverseaPcu: int
        :param OverseaDuration: Total duration of use outside the Chinese mainland (in minutes)
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealtimeSpeechConf(AbstractModel):
    """Configuration information of Voice Chat

    """

    def __init__(self):
        r"""
        :param Status: Voice Chat status. Valid values: `open`, `close`.
        :type Status: str
        :param Quality: Voice Chat sound quality. Valid value: `high`.
        :type Quality: str
        """
        self.Status = None
        self.Quality = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Quality = params.get("Quality")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealtimeTextStatisticsItem(AbstractModel):
    """Real-time Voice-to-Text usage statistics

    """

    def __init__(self):
        r"""
        :param Data: Statistical value (in seconds)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Data: float
        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordInfo(AbstractModel):
    """Information about the recording task in a room.
    Note: This field may return null, indicating that no valid values can be obtained.

    """

    def __init__(self):
        r"""
        :param UserId: User ID. The value is `0` in mixed streams recording mode.
        :type UserId: str
        :param FileName: Recording filename.
        :type FileName: str
        :param RecordBeginTime: Recording start time, which is a Unix timestamp. Example: 1234567868.
        :type RecordBeginTime: int
        :param RecordStatus: Recording status. Valid values: `2`: recording; `10`: to be transcoded; `11`: transcoding; `12`: uploading; `13`: uploaded; `14`: user notified.
        :type RecordStatus: int
        """
        self.UserId = None
        self.FileName = None
        self.RecordBeginTime = None
        self.RecordStatus = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.FileName = params.get("FileName")
        self.RecordBeginTime = params.get("RecordBeginTime")
        self.RecordStatus = params.get("RecordStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartRecordRequest(AbstractModel):
    """StartRecord request structure.

    """

    def __init__(self):
        r"""
        :param BizId: Application ID.
        :type BizId: int
        :param RoomId: Room ID.
        :type RoomId: str
        :param RecordMode: Recording mode. Valid values: `1`: single stream; `2`: mixed streams; `3`: single stream and mixed streams.
        :type RecordMode: int
        :param SubscribeRecordUserIds: Allowlist or blocklist for stream subscription. If you do not specify this parameter, the audio streams of all the users in the room are subscribed to by default.
        :type SubscribeRecordUserIds: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        """
        self.BizId = None
        self.RoomId = None
        self.RecordMode = None
        self.SubscribeRecordUserIds = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.RoomId = params.get("RoomId")
        self.RecordMode = params.get("RecordMode")
        if params.get("SubscribeRecordUserIds") is not None:
            self.SubscribeRecordUserIds = SubscribeRecordUserIds()
            self.SubscribeRecordUserIds._deserialize(params.get("SubscribeRecordUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartRecordResponse(AbstractModel):
    """StartRecord response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID.
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class StatisticsItem(AbstractModel):
    """Usage data unit

    """

    def __init__(self):
        r"""
        :param StatDate: Date in the format of yyyy-mm-dd, such as 2018-07-13
        :type StatDate: str
        :param Data: Statistical value
        :type Data: int
        """
        self.StatDate = None
        self.Data = None


    def _deserialize(self, params):
        self.StatDate = params.get("StatDate")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRecordRequest(AbstractModel):
    """StopRecord request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID.
        :type TaskId: int
        :param BizId: Application ID.
        :type BizId: int
        """
        self.TaskId = None
        self.BizId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRecordResponse(AbstractModel):
    """StopRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamTextStatisticsItem(AbstractModel):
    """Stream-to-Text usage statistics

    """

    def __init__(self):
        r"""
        :param Data: Usage of the service (in seconds)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Data: float
        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeRecordUserIds(AbstractModel):
    """Allowlist or blocklist for stream subscription.

    """

    def __init__(self):
        r"""
        :param UnSubscribeUserIds: Blocklist for audio subscription. For example, `["1", "2", "3"]` means to not subscribe to the audio streams of users 1, 2, and 3. If this parameter is left empty, the audio streams of all users (max 20) in the room will not be subscribed to.
Note: You cannot specify `UnSubscribeAudioUserIds` and `SubscribeAudioUserIds` at the same time.
        :type UnSubscribeUserIds: list of str
        :param SubscribeUserIds: Allowlist for audio subscription. For example, `["1", "2", "3"]` means to subscribe to the audio streams of users 1, 2, and 3. If this parameter is left empty, the audio streams of all users (max 20) in the room will be subscribed to.
Note: You cannot specify `UnSubscribeAudioUserIds` and `SubscribeAudioUserIds` at the same time.
        :type SubscribeUserIds: list of str
        """
        self.UnSubscribeUserIds = None
        self.SubscribeUserIds = None


    def _deserialize(self, params):
        self.UnSubscribeUserIds = params.get("UnSubscribeUserIds")
        self.SubscribeUserIds = params.get("SubscribeUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag list

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TagKey: str
        :param TagValue: Tag value
Note: This field may return `null`, indicating that no valid values can be obtained.
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
        


class VoiceFilterConf(AbstractModel):
    """Configuration information of Phrase Filtering

    """

    def __init__(self):
        r"""
        :param Status: Phrase Filtering status. Valid values: `open`, `close`.
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterStatisticsItem(AbstractModel):
    """Phrase Filtering usage statistics

    """

    def __init__(self):
        r"""
        :param Duration: Total duration of phrase filtering (in minutes)
        :type Duration: int
        """
        self.Duration = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceMessageConf(AbstractModel):
    """Configuration information of Voice Message Service

    """

    def __init__(self):
        r"""
        :param Status: Voice Message Service status. Valid values: `open`, `close`.
        :type Status: str
        :param Language: Language supported for Voice Message Service. Valid values: `all` (all languages), `cnen` (Chinese and English). Default value: `cnen`.
        :type Language: str
        """
        self.Status = None
        self.Language = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceMessageStatisticsItem(AbstractModel):
    """Voice Message Service usage statistics

    """

    def __init__(self):
        r"""
        :param Dau: DAUs of Voice Message Service
        :type Dau: int
        """
        self.Dau = None


    def _deserialize(self, params):
        self.Dau = params.get("Dau")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        