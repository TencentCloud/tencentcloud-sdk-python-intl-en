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


class AbnormalEvent(AbstractModel):
    """Types of exception events that can cause an exceptional experience

    """

    def __init__(self):
        """
        :param AbnormalEventId: Exception event ID. For specific values, please see Appendix. Exceptional Experience ID Mapping Table.
        :type AbnormalEventId: int
        :param PeerId: Remote user ID. If this parameter is left empty, it indicates that the exception event is not caused by the remote user.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeerId: str
        """
        self.AbnormalEventId = None
        self.PeerId = None


    def _deserialize(self, params):
        self.AbnormalEventId = params.get("AbnormalEventId")
        self.PeerId = params.get("PeerId")


class AbnormalExperience(AbstractModel):
    """Exceptional user experience and possible causes

    """

    def __init__(self):
        """
        :param UserId: User ID
        :type UserId: str
        :param ExperienceId: Exceptional experience ID
        :type ExperienceId: int
        :param RoomId: Room ID in string type
        :type RoomId: str
        :param AbnormalEventList: Exception event array
        :type AbnormalEventList: list of AbnormalEvent
        :param EventTime: Report time of the exception event
        :type EventTime: int
        """
        self.UserId = None
        self.ExperienceId = None
        self.RoomId = None
        self.AbnormalEventList = None
        self.EventTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.ExperienceId = params.get("ExperienceId")
        self.RoomId = params.get("RoomId")
        if params.get("AbnormalEventList") is not None:
            self.AbnormalEventList = []
            for item in params.get("AbnormalEventList"):
                obj = AbnormalEvent()
                obj._deserialize(item)
                self.AbnormalEventList.append(obj)
        self.EventTime = params.get("EventTime")


class CreateTroubleInfoRequest(AbstractModel):
    """CreateTroubleInfo request structure.

    """

    def __init__(self):
        """
        :param SdkAppId: Application ID
        :type SdkAppId: str
        :param RoomId: Room ID
        :type RoomId: str
        :param TeacherUserId: Teacher user ID
        :type TeacherUserId: str
        :param StudentUserId: Student user ID
        :type StudentUserId: str
        :param TroubleUserId: ID of the user (teacher or student) with exception.
        :type TroubleUserId: str
        :param TroubleType: Exception type.
1: exceptional video
2: exceptional audio
3: exceptional video and audio
5: exceptional room entry
4: course switch
6: help seeking
7: problem feedback
8: complaint
        :type TroubleType: int
        :param TroubleTime: UNIX timestamp when the exception occurred in seconds.
        :type TroubleTime: int
        :param TroubleMsg: Exception details
        :type TroubleMsg: str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.TeacherUserId = None
        self.StudentUserId = None
        self.TroubleUserId = None
        self.TroubleType = None
        self.TroubleTime = None
        self.TroubleMsg = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.TeacherUserId = params.get("TeacherUserId")
        self.StudentUserId = params.get("StudentUserId")
        self.TroubleUserId = params.get("TroubleUserId")
        self.TroubleType = params.get("TroubleType")
        self.TroubleTime = params.get("TroubleTime")
        self.TroubleMsg = params.get("TroubleMsg")


class CreateTroubleInfoResponse(AbstractModel):
    """CreateTroubleInfo response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAbnormalEventRequest(AbstractModel):
    """DescribeAbnormalEvent request structure.

    """

    def __init__(self):
        """
        :param SdkAppId: User `SDKAppID`, which can be used to query 20 exceptional experience events (in one or more rooms)
        :type SdkAppId: str
        :param StartTime: Query start time
        :type StartTime: int
        :param EndTime: Query end time
        :type EndTime: int
        :param RoomId: Room ID, which can be used to query up to 20 exceptional experience events in a specific room
        :type RoomId: str
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RoomId = params.get("RoomId")


class DescribeAbnormalEventResponse(AbstractModel):
    """DescribeAbnormalEvent response structure.

    """

    def __init__(self):
        """
        :param Total: Number of returned data entries.
        :type Total: int
        :param AbnormalExperienceList: Exceptional experience list.
        :type AbnormalExperienceList: list of AbnormalExperience
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.AbnormalExperienceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("AbnormalExperienceList") is not None:
            self.AbnormalExperienceList = []
            for item in params.get("AbnormalExperienceList"):
                obj = AbnormalExperience()
                obj._deserialize(item)
                self.AbnormalExperienceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCallDetailRequest(AbstractModel):
    """DescribeCallDetail request structure.

    """

    def __init__(self):
        """
        :param CommId: Unique ID of a call: sdkappid_roomgString_createTime. The `roomgString` refers to the room ID, and `createTime` refers to the creation time of a room in the format of UNIX timestamp in seconds, such as 1400353843_218695_1590065777. Its value can be obtained from the `DescribeRoomInformation` API (related document: https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1).
        :type CommId: str
        :param StartTime: Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 5 days.
        :type StartTime: int
        :param EndTime: Query end time in the format of local UNIX timestamp, such as 1588031999s.
        :type EndTime: int
        :param SdkAppId: User `SDKAppID`, such as 1400188366.
        :type SdkAppId: str
        :param UserIds: User array to query, which contains up to 6 users. If it is left empty, 6 users will be returned by default.
        :type UserIds: list of str
        :param DataType: Metric to query. The user list will be returned if it is left empty; all metrics will be returned if its value is `all`.
appCpu: CPU utilization of the application;
sysCpu: CPU utilization of the system;
aBit: upstream/downstream audio bitrate;
aBlock: audio lag duration;
bigvBit: upstream/downstream video bitrate;
bigvCapFps: frame rate for capturing videos;
bigvEncFps: frame rate for sending videos;
bigvDecFps: rendering frame rate;
bigvBlock: video lag duration;
aLoss: upstream/downstream audio packet loss;
bigvLoss: upstream/downstream video packet loss;
bigvWidth: upstream/downstream resolution in width;
bigvHeight: upstream/downstream resolution in height.
        :type DataType: list of str
        :param PageNumber: Page index starting from 0. If either `PageNumber` or `PageSize` is left empty, 6 data entries will be returned by default.
        :type PageNumber: str
        :param PageSize: Number of entries per page. If either `PageNumber` or `PageSize` is left empty, 6 data entries will be returned by default. When either `DataType` or `UserId` is not null, `PageSize` is up to 6. When `DataType` and `UserId` are null, `PageSize` is up to 100.
        :type PageSize: str
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.UserIds = None
        self.DataType = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.UserIds = params.get("UserIds")
        self.DataType = params.get("DataType")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")


class DescribeCallDetailResponse(AbstractModel):
    """DescribeCallDetail response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of returned users
        :type Total: int
        :param UserList: User information list
        :type UserList: list of UserInformation
        :param Data: Quality data
        :type Data: list of QualityData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.UserList = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self.UserList.append(obj)
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QualityData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDetailEventRequest(AbstractModel):
    """DescribeDetailEvent request structure.

    """

    def __init__(self):
        """
        :param CommId: Unique ID of a call: sdkappid_roomgString_createTime. The `roomgString` refers to the room ID, and `createTime` refers to the creation time of a room in the format of UNIX timestamp in seconds. Its value can be obtained from the `DescribeRoomInformation` API (related document: https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1).
        :type CommId: str
        :param StartTime: Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 5 days.
        :type StartTime: int
        :param EndTime: Query end time in the format of local UNIX timestamp, such as 1588031999s.
        :type EndTime: int
        :param UserId: User ID
        :type UserId: str
        :param RoomId: Room ID
        :type RoomId: str
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.UserId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserId = params.get("UserId")
        self.RoomId = params.get("RoomId")


class DescribeDetailEventResponse(AbstractModel):
    """DescribeDetailEvent response structure.

    """

    def __init__(self):
        """
        :param Data: List of returned events
        :type Data: list of EventList
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = EventList()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHistoryScaleRequest(AbstractModel):
    """DescribeHistoryScale request structure.

    """

    def __init__(self):
        """
        :param SdkAppId: User `sdkappid`
        :type SdkAppId: str
        :param StartTime: Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 5 days.
        :type StartTime: int
        :param EndTime: Query end time in the format of local UNIX timestamp, such as 1588031999s.
        :type EndTime: int
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeHistoryScaleResponse(AbstractModel):
    """DescribeHistoryScale response structure.

    """

    def __init__(self):
        """
        :param Total: Number of returned data entries
        :type Total: int
        :param ScaleList: Returned data
        :type ScaleList: list of ScaleInfomation
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.ScaleList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ScaleList") is not None:
            self.ScaleList = []
            for item in params.get("ScaleList"):
                obj = ScaleInfomation()
                obj._deserialize(item)
                self.ScaleList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeNetworkRequest(AbstractModel):
    """DescribeRealtimeNetwork request structure.

    """

    def __init__(self):
        """
        :param StartTime: Query start time in the format of UNIX timestamp, such as 1588031999s, which is a point in time in the last 24 hours.
        :type StartTime: int
        :param EndTime: Query end time in the format of local UNIX timestamp, such as 1588031999s.
        :type EndTime: int
        :param SdkAppId: User `sdkappid`
        :type SdkAppId: str
        :param DataType: Type of data to query
sendLossRateRaw: upstream packet loss rate;
recvLossRateRaw: downstream packet loss rate.
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeNetworkResponse(AbstractModel):
    """DescribeRealtimeNetwork response structure.

    """

    def __init__(self):
        """
        :param Data: Data returned by query
        :type Data: list of RealtimeData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeQualityRequest(AbstractModel):
    """DescribeRealtimeQuality request structure.

    """

    def __init__(self):
        """
        :param StartTime: Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 24 hours.
        :type StartTime: int
        :param EndTime: Query end time in the format of local UNIX timestamp, such as 1588031999s.
        :type EndTime: int
        :param SdkAppId: User `sdkappid`
        :type SdkAppId: str
        :param DataType: Type of data to query
enterTotalSuccPercent: room entry success rate;
fistFreamInSecRate: instant playback rate of the first frame;
blockPercent: video lag rate;
audioBlockPercent: audio lag rate.
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeQualityResponse(AbstractModel):
    """DescribeRealtimeQuality response structure.

    """

    def __init__(self):
        """
        :param Data: Type of returned data
        :type Data: list of RealtimeData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeScaleRequest(AbstractModel):
    """DescribeRealtimeScale request structure.

    """

    def __init__(self):
        """
        :param StartTime: Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 24 hours.
        :type StartTime: int
        :param EndTime: Query end time in the format of local UNIX timestamp, such as 1588031999s.
        :type EndTime: int
        :param SdkAppId: User `sdkappid`
        :type SdkAppId: str
        :param DataType: Type of data to query
`UserNum: number of users in call;
RoomNum: number of rooms.
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeScaleResponse(AbstractModel):
    """DescribeRealtimeScale response structure.

    """

    def __init__(self):
        """
        :param Data: Returned data array
        :type Data: list of RealtimeData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRoomInformationRequest(AbstractModel):
    """DescribeRoomInformation request structure.

    """

    def __init__(self):
        """
        :param SdkAppId: User `sdkappid`
        :type SdkAppId: str
        :param StartTime: Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 5 days.
        :type StartTime: int
        :param EndTime: Query end time in the format of local UNIX timestamp, such as 1588031999s.
        :type EndTime: int
        :param RoomId: Room ID of uint type
        :type RoomId: str
        :param PageNumber: Page index starting from 0 (if either `PageNumber` or `PageSize` is left empty, 10 data entries will be returned by default)
        :type PageNumber: str
        :param PageSize: Number of entries per page (if either `PageNumber` or `PageSize` is left empty, 10 data entries will be returned by default. Maximum value: 100)
        :type PageSize: str
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.RoomId = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RoomId = params.get("RoomId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")


class DescribeRoomInformationResponse(AbstractModel):
    """DescribeRoomInformation response structure.

    """

    def __init__(self):
        """
        :param Total: Total number of returned data entries.
        :type Total: int
        :param RoomList: Room information list
        :type RoomList: list of RoomState
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.RoomList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("RoomList") is not None:
            self.RoomList = []
            for item in params.get("RoomList"):
                obj = RoomState()
                obj._deserialize(item)
                self.RoomList.append(obj)
        self.RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    """DismissRoom request structure.

    """

    def __init__(self):
        """
        :param SdkAppId: `SDKAppId` of TRTC.
        :type SdkAppId: int
        :param RoomId: Room number.
        :type RoomId: int
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")


class DismissRoomResponse(AbstractModel):
    """DismissRoom response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EncodeParams(AbstractModel):
    """Output stream encoding parameters for MCU On-Cloud MixTranscoding

    """

    def __init__(self):
        """
        :param AudioSampleRate: Output stream audio sample rate for stream mix in Hz. Valid values: 48000, 44100, 32000, 24000, 16000, 12000, 8000.
        :type AudioSampleRate: int
        :param AudioBitrate: Output stream audio bitrate in Kbps for On-Cloud MixTranscoding. Value range: [8, 500].
        :type AudioBitrate: int
        :param AudioChannels: Number of output stream audio sound channels for On-Cloud MixTranscoding. Value range: [1, 2].
        :type AudioChannels: int
        :param VideoWidth: Output stream width in pixels for On-Cloud MixTranscoding, which is required for audio/video output. Value range: [0, 1920].
        :type VideoWidth: int
        :param VideoHeight: Output stream height in pixels for On-Cloud MixTranscoding, which is required for audio/video output. Value range: [0, 1080].
        :type VideoHeight: int
        :param VideoBitrate: Output stream bitrate in Kbps for On-Cloud MixTranscoding, which is required for audio/video output. Value range: [1, 10000].
        :type VideoBitrate: int
        :param VideoFramerate: Output stream frame rate for On-Cloud MixTranscoding, which is required for audio/video output. Value range: [6, 12, 15, 24, 30, 48, 60]. If the frame rate lies outside the valid value range, it will be automatically modified to a value within the range.
        :type VideoFramerate: int
        :param VideoGop: Output stream GOP in seconds for On-Cloud MixTranscoding, which is required for audio/video output. Value range: [1, 5].
        :type VideoGop: int
        :param BackgroundColor: Output stream background color for On-Cloud MixTranscoding.
        :type BackgroundColor: int
        :param BackgroundImageId: Output stream background image for stream mix. Its value is the ID of image uploaded through the TRTC Console.
        :type BackgroundImageId: int
        """
        self.AudioSampleRate = None
        self.AudioBitrate = None
        self.AudioChannels = None
        self.VideoWidth = None
        self.VideoHeight = None
        self.VideoBitrate = None
        self.VideoFramerate = None
        self.VideoGop = None
        self.BackgroundColor = None
        self.BackgroundImageId = None


    def _deserialize(self, params):
        self.AudioSampleRate = params.get("AudioSampleRate")
        self.AudioBitrate = params.get("AudioBitrate")
        self.AudioChannels = params.get("AudioChannels")
        self.VideoWidth = params.get("VideoWidth")
        self.VideoHeight = params.get("VideoHeight")
        self.VideoBitrate = params.get("VideoBitrate")
        self.VideoFramerate = params.get("VideoFramerate")
        self.VideoGop = params.get("VideoGop")
        self.BackgroundColor = params.get("BackgroundColor")
        self.BackgroundImageId = params.get("BackgroundImageId")


class EventList(AbstractModel):
    """List of SDK or WebRTC events.

    """

    def __init__(self):
        """
        :param Content: Data content
        :type Content: list of EventMessage
        :param PeerId: Sender `userId`
        :type PeerId: str
        """
        self.Content = None
        self.PeerId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = EventMessage()
                obj._deserialize(item)
                self.Content.append(obj)
        self.PeerId = params.get("PeerId")


class EventMessage(AbstractModel):
    """Event information, including event timestamp and event ID.

    """

    def __init__(self):
        """
        :param Type: Video stream type:
0: non-video event;
2: big image;
3: small image;
7: relayed stream image.
        :type Type: int
        :param Time: Event reporting time in the format of UNIX timestamp, such as 1589891188801ms
        :type Time: int
        :param EventId: Event ID. Events divide into SDK events and WebRTC events. For more information, please see Appendix - Event ID Mapping Table at https://intl.cloud.tencent.com/document/product/647/44916?from_cn_redirect=1
        :type EventId: int
        :param ParamOne: First event parameter, such as video resolution width
        :type ParamOne: int
        :param ParamTwo: Second event parameter, such as video resolution height
        :type ParamTwo: int
        """
        self.Type = None
        self.Time = None
        self.EventId = None
        self.ParamOne = None
        self.ParamTwo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Time = params.get("Time")
        self.EventId = params.get("EventId")
        self.ParamOne = params.get("ParamOne")
        self.ParamTwo = params.get("ParamTwo")


class LayoutParams(AbstractModel):
    """MCU On-Cloud MixTranscoding layout parameters

    """

    def __init__(self):
        """
        :param Template: On-cloud stream mix layout template ID. 0: floating template (default value); 1: grid template; 2: screen sharing template; 3: picture-in-picture template.
        :type Template: int
        :param MainVideoUserId: ID of the user in the big image, which takes effect in a screen sharing, floating, or picture-in-picture template.
        :type MainVideoUserId: str
        :param MainVideoStreamType: Stream type of the big image, which takes effect in a screen sharing, floating, or picture-in-picture template. 0: camera; 1: screen sharing. If a web user's stream is displayed in the big image on the left, enter 0 for this parameter.
        :type MainVideoStreamType: int
        :param SmallVideoLayoutParams: Layout parameter of the small image, which takes effect in a picture-in-picture template.
        :type SmallVideoLayoutParams: :class:`tencentcloud.trtc.v20190722.models.SmallVideoLayoutParams`
        :param MainVideoRightAlign: You can set the layout parameter as 1 or 0 in the screen sharing template. 1: big image on the right and small images on the left, 0: big image on the left and small images on the right. The default value is 0. 
        :type MainVideoRightAlign: int
        :param MixVideoUids: A user list, which takes effect for floating, grid, or screen sharing templates. When the user list has been set, the stream mix output for users in this user list will include both audio and video; the stream mix output for users not in the list will only include audio. Up to 16 users can be set.
        :type MixVideoUids: list of str
        """
        self.Template = None
        self.MainVideoUserId = None
        self.MainVideoStreamType = None
        self.SmallVideoLayoutParams = None
        self.MainVideoRightAlign = None
        self.MixVideoUids = None


    def _deserialize(self, params):
        self.Template = params.get("Template")
        self.MainVideoUserId = params.get("MainVideoUserId")
        self.MainVideoStreamType = params.get("MainVideoStreamType")
        if params.get("SmallVideoLayoutParams") is not None:
            self.SmallVideoLayoutParams = SmallVideoLayoutParams()
            self.SmallVideoLayoutParams._deserialize(params.get("SmallVideoLayoutParams"))
        self.MainVideoRightAlign = params.get("MainVideoRightAlign")
        self.MixVideoUids = params.get("MixVideoUids")


class OutputParams(AbstractModel):
    """MCU On-Cloud MixTranscoding output parameters

    """

    def __init__(self):
        """
        :param StreamId: Custom live stream ID, which must be different from the ID of relayed stream.
        :type StreamId: str
        :param PureAudioStream: Value range: [0, 1]. If it is 0, live streams are audio and video; if it is 1, live streams are only audio. Default value: 0.
        :type PureAudioStream: int
        :param RecordId: Custom recording file name
        :type RecordId: str
        :param RecordAudioOnly: Value range: [0, 1]. If it is 0, the recording template configured in the console will be used; if it is 1, streams are recorded as .mp3 files.
        :type RecordAudioOnly: int
        """
        self.StreamId = None
        self.PureAudioStream = None
        self.RecordId = None
        self.RecordAudioOnly = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.PureAudioStream = params.get("PureAudioStream")
        self.RecordId = params.get("RecordId")
        self.RecordAudioOnly = params.get("RecordAudioOnly")


class QualityData(AbstractModel):
    """Quality data returned by ES

    """

    def __init__(self):
        """
        :param Content: Data content
        :type Content: list of TimeValue
        :param UserId: User ID
        :type UserId: str
        :param PeerId: Peer ID. An empty value indicates that the returned data is upstream.
        :type PeerId: str
        :param DataType: Data type
        :type DataType: str
        """
        self.Content = None
        self.UserId = None
        self.PeerId = None
        self.DataType = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.UserId = params.get("UserId")
        self.PeerId = params.get("PeerId")
        self.DataType = params.get("DataType")


class RealtimeData(AbstractModel):
    """Returned data of seconds-level monitoring

    """

    def __init__(self):
        """
        :param Content: Returned data
        :type Content: list of TimeValue
        :param DataType: Data type field
        :type DataType: str
        """
        self.Content = None
        self.DataType = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.DataType = params.get("DataType")


class RemoveUserRequest(AbstractModel):
    """RemoveUser request structure.

    """

    def __init__(self):
        """
        :param SdkAppId: `SDKAppId` of TRTC.
        :type SdkAppId: int
        :param RoomId: Room number.
        :type RoomId: int
        :param UserIds: List of up to 10 users to be removed.
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")


class RemoveUserResponse(AbstractModel):
    """RemoveUser response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoomState(AbstractModel):
    """Room information list

    """

    def __init__(self):
        """
        :param CommId: Call ID (unique call ID)
        :type CommId: str
        :param RoomString: Room ID of string type
        :type RoomString: str
        :param CreateTime: Room creation time
        :type CreateTime: int
        :param DestroyTime: Room termination time
        :type DestroyTime: int
        :param IsFinished: Whether the room is terminated
        :type IsFinished: bool
        :param UserId: Room creator ID
        :type UserId: str
        """
        self.CommId = None
        self.RoomString = None
        self.CreateTime = None
        self.DestroyTime = None
        self.IsFinished = None
        self.UserId = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.RoomString = params.get("RoomString")
        self.CreateTime = params.get("CreateTime")
        self.DestroyTime = params.get("DestroyTime")
        self.IsFinished = params.get("IsFinished")
        self.UserId = params.get("UserId")


class ScaleInfomation(AbstractModel):
    """Historical scale information

    """

    def __init__(self):
        """
        :param Time: Start time for each day
        :type Time: int
        :param UserNumber: Number of users in room. If a user enters the room for multiple times, the user will be counted as one user.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserNumber: int
        :param UserCount: Number of room entries. Every time when a user enters the room, it will be counted as one room entry.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserCount: int
        :param RoomNumbers: Number of rooms under `sdkappid` on a day
Note: this field may return null, indicating that no valid values can be obtained.
        :type RoomNumbers: int
        """
        self.Time = None
        self.UserNumber = None
        self.UserCount = None
        self.RoomNumbers = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.UserNumber = params.get("UserNumber")
        self.UserCount = params.get("UserCount")
        self.RoomNumbers = params.get("RoomNumbers")


class SmallVideoLayoutParams(AbstractModel):
    """Layout parameter of the small image, which takes effect in a picture-in-picture template

    """

    def __init__(self):
        """
        :param UserId: ID of the user in the small image.
        :type UserId: str
        :param StreamType: Stream type of the small image. 0: camera; 1: screen sharing. If a web user's stream is displayed in the small image, enter 0 for this parameter.
        :type StreamType: int
        :param ImageWidth: Output width of the small image in pixels. If this parameter is left empty, 0 will be used by default.
        :type ImageWidth: int
        :param ImageHeight: Output height of the small image in pixels. If this parameter is left empty, 0 will be used by default.
        :type ImageHeight: int
        :param LocationX: Output X-axis offset of the small image in pixels. The sum of `LocationX` and `ImageWidth` cannot exceed the total width of the output mixed stream. If this parameter is left empty, 0 will be used by default.
        :type LocationX: int
        :param LocationY: Output Y-axis offset of the small image in pixels. The sum of `LocationY` and `ImageHeight` cannot exceed the total height of the output mixed stream. If this parameter is left empty, 0 will be used by default.
        :type LocationY: int
        """
        self.UserId = None
        self.StreamType = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.StreamType = params.get("StreamType")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")


class StartMCUMixTranscodeRequest(AbstractModel):
    """StartMCUMixTranscode request structure.

    """

    def __init__(self):
        """
        :param SdkAppId: `SDKAppId` of TRTC.
        :type SdkAppId: int
        :param RoomId: Room ID.
        :type RoomId: int
        :param OutputParams: On-Cloud MixTranscoding output control parameters.
        :type OutputParams: :class:`tencentcloud.trtc.v20190722.models.OutputParams`
        :param EncodeParams: On-Cloud MixTranscoding output encoding parameters.
        :type EncodeParams: :class:`tencentcloud.trtc.v20190722.models.EncodeParams`
        :param LayoutParams: On-Cloud MixTranscoding output layout parameters.
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.LayoutParams`
        """
        self.SdkAppId = None
        self.RoomId = None
        self.OutputParams = None
        self.EncodeParams = None
        self.LayoutParams = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        if params.get("OutputParams") is not None:
            self.OutputParams = OutputParams()
            self.OutputParams._deserialize(params.get("OutputParams"))
        if params.get("EncodeParams") is not None:
            self.EncodeParams = EncodeParams()
            self.EncodeParams._deserialize(params.get("EncodeParams"))
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))


class StartMCUMixTranscodeResponse(AbstractModel):
    """StartMCUMixTranscode response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMCUMixTranscodeRequest(AbstractModel):
    """StopMCUMixTranscode request structure.

    """

    def __init__(self):
        """
        :param SdkAppId: `SDKAppId` of TRTC.
        :type SdkAppId: int
        :param RoomId: Room ID.
        :type RoomId: int
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")


class StopMCUMixTranscodeResponse(AbstractModel):
    """StopMCUMixTranscode response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TimeValue(AbstractModel):
    """Returned quality data in the format of time:value

    """

    def __init__(self):
        """
        :param Time: Time in the format of UNIX timestamp, such as 1590065877s.
        :type Time: int
        :param Value: Parameter value returned in the current time. For example, if `bigvCapFps` is set to 0 when the current time is 1590065877s (UNIX timestamp), the value of this parameter is 0.
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class UserInformation(AbstractModel):
    """User information, including when the user enters/exits a room

    """

    def __init__(self):
        """
        :param RoomStr: Room ID
        :type RoomStr: str
        :param UserId: User ID
        :type UserId: str
        :param JoinTs: The time when the user enters the room
        :type JoinTs: int
        :param LeaveTs: The time when the user exits the room. If the user is still in the room, the current time will be returned
        :type LeaveTs: int
        :param DeviceType: Device type
        :type DeviceType: str
        :param SdkVersion: SDK version number
        :type SdkVersion: str
        :param ClientIp: Client IP
        :type ClientIp: str
        :param Finished: Determine whether a user has left the room
        :type Finished: bool
        """
        self.RoomStr = None
        self.UserId = None
        self.JoinTs = None
        self.LeaveTs = None
        self.DeviceType = None
        self.SdkVersion = None
        self.ClientIp = None
        self.Finished = None


    def _deserialize(self, params):
        self.RoomStr = params.get("RoomStr")
        self.UserId = params.get("UserId")
        self.JoinTs = params.get("JoinTs")
        self.LeaveTs = params.get("LeaveTs")
        self.DeviceType = params.get("DeviceType")
        self.SdkVersion = params.get("SdkVersion")
        self.ClientIp = params.get("ClientIp")
        self.Finished = params.get("Finished")