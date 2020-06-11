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


class DescribeCallDetailRequest(AbstractModel):
    """DescribeCallDetail request structure.

    """

    def __init__(self):
        """
        :param CommId: Call ID (unique call ID): sdkappid_roomgString (room ID)_createTime (room creation time in UNIX timestamp in seconds). You can get the parameter value through the `DescribeRoomInformation` API which is used to query the room list.
        :type CommId: str
        :param StartTime: Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 5 days.
        :type StartTime: int
        :param EndTime: Query end time in the format of local UNIX timestamp, such as 1588031999s.
        :type EndTime: int
        :param SdkAppId: User `sdkappid`
        :type SdkAppId: str
        :param UserIds: User array to query, which contains up to 6 users. If it is left empty, 6 users will be returned by default.
        :type UserIds: list of str
        :param DataType: Metric to query. The user list will be returned if it is left empty; all metrics will be returned if its value is `all`.
appCpu: CPU utilization of application;
sysCpu: CPU utilization of system;
aBit: upstream/downstream audio bitrate;
aBlock: audio lag duration;
vBit: upstream/downstream video bitrate;
vCapFps: video capturing frame rate;
vEncFps: video sending frame rate;
vDecFps: rendering frame rate;
vBlock: video lag duration;
aLoss: upstream/downstream audio packet loss;
vLoss: upstream/downstream video packet loss;
vWidth: upstream/downstream resolution in width;
vHeight: upstream/downstream resolution in height.
        :type DataType: list of str
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.UserIds = None
        self.DataType = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.UserIds = params.get("UserIds")
        self.DataType = params.get("DataType")


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
        :param StartTime: Query start time in the format of local UNIX timestamp, such as 1588031999s, which is a point in time in the last 24 hours.
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
        :param PageNumber: Page index. If it is left empty, 10 entries will be returned by default.
        :type PageNumber: str
        :param PageSize: Page size. Maximum value: 100. If it is left empty, 10 entries will be returned by default.
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
        :param UserNumber: Number of users in room
        :type UserNumber: int
        :param UserCount: Number of times a room has been entered
        :type UserCount: int
        :param RoomNumbers: Number of rooms.
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


class TimeValue(AbstractModel):
    """Returned quality data in the format of time:value

    """

    def __init__(self):
        """
        :param Time: Time
        :type Time: int
        :param Value: Current time value in the format of UNIX timestamp
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class UserInformation(AbstractModel):
    """User information, including when the user enters/exits a room, etc.

    """

    def __init__(self):
        """
        :param RoomStr: Room ID of string type.
        :type RoomStr: str
        :param UserId: User ID
        :type UserId: str
        :param JoinTs: The time when the user enters the room
        :type JoinTs: int
        :param LeaveTs: The time when the user exits the room
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