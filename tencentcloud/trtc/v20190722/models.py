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


class AbnormalEvent(AbstractModel):
    """Types of exception events that can cause an exceptional experience

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalExperience(AbstractModel):
    """Exceptional user experience and possible causes

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePictureRequest(AbstractModel):
    """CreatePicture request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: Application ID
        :type SdkAppId: int
        :param Content: Base64-encoded image content
        :type Content: str
        :param Suffix: Image file extension
        :type Suffix: str
        :param Height: Image height
        :type Height: int
        :param Width: Image width
        :type Width: int
        :param XPosition: X-axis value of the image’s position
        :type XPosition: int
        :param YPosition: Y-axis value of the image’s position
        :type YPosition: int
        """
        self.SdkAppId = None
        self.Content = None
        self.Suffix = None
        self.Height = None
        self.Width = None
        self.XPosition = None
        self.YPosition = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Content = params.get("Content")
        self.Suffix = params.get("Suffix")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePictureResponse(AbstractModel):
    """CreatePicture response structure.

    """

    def __init__(self):
        r"""
        :param PictureId: Image ID
        :type PictureId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PictureId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PictureId = params.get("PictureId")
        self.RequestId = params.get("RequestId")


class CreateTroubleInfoRequest(AbstractModel):
    """CreateTroubleInfo request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTroubleInfoResponse(AbstractModel):
    """CreateTroubleInfo response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePictureRequest(AbstractModel):
    """DeletePicture request structure.

    """

    def __init__(self):
        r"""
        :param PictureId: Image ID
        :type PictureId: int
        :param SdkAppId: Application ID
        :type SdkAppId: int
        """
        self.PictureId = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.PictureId = params.get("PictureId")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePictureResponse(AbstractModel):
    """DeletePicture response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param SdkAppId: User `SDKAppID`, which can be used to query 20 exceptional experience events (in one or more rooms)
        :type SdkAppId: str
        :param StartTime: Query start time (s) in the format of Unix timestamp, e.g., 1592448600
        :type StartTime: int
        :param EndTime: Query end time (s) in the format of Unix timestamp, e.g., 1592449080
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAbnormalEventResponse(AbstractModel):
    """DescribeAbnormalEvent response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param CommId: Unique ID of a call: sdkappid_roomgString_createTime. The `roomgString` refers to the room ID, and `createTime` refers to the creation time of a room in the format of UNIX timestamp in seconds, such as 1400353843_218695_1590065777. Its value can be obtained from the `DescribeRoomInformation` API (related document: https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1).
        :type CommId: str
        :param StartTime: Query start time (s) in the format of Unix timestamp (e.g., 1590065777), which must be a time point in the last 14 days. The start and end time for query must not be more than 1 hour apart.
        :type StartTime: int
        :param EndTime: Query end time (s) in the format of Unix timestamp, e.g., 1590065877
        :type EndTime: int
        :param SdkAppId: `SDKAppID` of the users to query, e.g., 1400353843
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallDetailResponse(AbstractModel):
    """DescribeCallDetail response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param CommId: Unique ID of a call: sdkappid_roomgString_createTime. The `roomgString` refers to the room ID, and `createTime` refers to the creation time of a room in the format of UNIX timestamp in seconds. Its value can be obtained from the `DescribeRoomInformation` API (related document: https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1).
        :type CommId: str
        :param StartTime: Query start time (s) in the format of Unix timestamp (e.g., 1588055615), which must be a time point in the last 14 days
        :type StartTime: int
        :param EndTime: Query end time (s) in the format of Unix timestamp, e.g., 1588058615
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDetailEventResponse(AbstractModel):
    """DescribeDetailEvent response structure.

    """

    def __init__(self):
        r"""
        :param Data: List of returned events. An empty array will be returned if no data can be found.
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
        r"""
        :param SdkAppId: `SDKAppID` of the users to query, e.g., 1400188366
        :type SdkAppId: str
        :param StartTime: Query start time (s) in the format of Unix timestamp (e.g., 1587571000), which must be a time point in the last 5 days
        :type StartTime: int
        :param EndTime: Query end time (s) in the format of Unix timestamp, e.g., 1588034999
        :type EndTime: int
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHistoryScaleResponse(AbstractModel):
    """DescribeHistoryScale response structure.

    """

    def __init__(self):
        r"""
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


class DescribePictureRequest(AbstractModel):
    """DescribePicture request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: Application ID
        :type SdkAppId: int
        :param PictureId: Image ID. If it is left empty, the IDs of all images under the application are returned.
        :type PictureId: int
        :param PageSize: Number of records per page. `10` is used if it is left empty.
        :type PageSize: int
        :param PageNo: Page number. `1` is used if it is left empty.
        :type PageNo: int
        """
        self.SdkAppId = None
        self.PictureId = None
        self.PageSize = None
        self.PageNo = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.PictureId = params.get("PictureId")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePictureResponse(AbstractModel):
    """DescribePicture response structure.

    """

    def __init__(self):
        r"""
        :param Total: Number of records returned
        :type Total: int
        :param PictureInfo: Image information list
        :type PictureInfo: list of PictureInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.PictureInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("PictureInfo") is not None:
            self.PictureInfo = []
            for item in params.get("PictureInfo"):
                obj = PictureInfo()
                obj._deserialize(item)
                self.PictureInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordStatisticRequest(AbstractModel):
    """DescribeRecordStatistic request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Query start date in the format of YYYY-MM-DD
        :type StartTime: str
        :param EndTime: Query end date in the format of YYYY-MM-DD
The period queried in a request cannot be longer than 31 days.
        :type EndTime: str
        :param SdkAppId: Application ID, which is optional. If it is specified, duration statistics for the specified application are returned; otherwise, the total durations of all applications are returned.
        :type SdkAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordStatisticResponse(AbstractModel):
    """DescribeRecordStatistic response structure.

    """

    def __init__(self):
        r"""
        :param SdkAppIdUsages: Duration statistics of the queried application(s)
        :type SdkAppIdUsages: list of SdkAppIdRecordUsage
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SdkAppIdUsages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SdkAppIdUsages") is not None:
            self.SdkAppIdUsages = []
            for item in params.get("SdkAppIdUsages"):
                obj = SdkAppIdRecordUsage()
                obj._deserialize(item)
                self.SdkAppIdUsages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRoomInformationRequest(AbstractModel):
    """DescribeRoomInformation request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: User `sdkappid`
        :type SdkAppId: str
        :param StartTime: Query start time (s) in the format of Unix timestamp (e.g., 1588031999), which must be a time point in the last 14 days
        :type StartTime: int
        :param EndTime: Query end time (s) in the format of Unix timestamp, e.g., 1588034999
        :type EndTime: int
        :param RoomId: Room ID in string type
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomInformationResponse(AbstractModel):
    """DescribeRoomInformation response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total number of data entries displayed on the current page
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


class DescribeTrtcInteractiveTimeRequest(AbstractModel):
    """DescribeTrtcInteractiveTime request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Query start date in the format of YYYY-MM-DD
        :type StartTime: str
        :param EndTime: Query end date in the format of YYYY-MM-DD
The period queried in a request cannot be longer than 31 days.
        :type EndTime: str
        :param SdkAppId: Application ID, which is optional. If it is specified, duration statistics for the specified application are returned; otherwise, the total durations of all applications are returned.
        :type SdkAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrtcInteractiveTimeResponse(AbstractModel):
    """DescribeTrtcInteractiveTime response structure.

    """

    def __init__(self):
        r"""
        :param Usages: Duration statistics of the queried application(s)
        :type Usages: list of OneSdkAppIdUsagesInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Usages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = OneSdkAppIdUsagesInfo()
                obj._deserialize(item)
                self.Usages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrtcMcuTranscodeTimeRequest(AbstractModel):
    """DescribeTrtcMcuTranscodeTime request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Query start date in the format of YYYY-MM-DD
        :type StartTime: str
        :param EndTime: Query end date in the format of YYYY-MM-DD
The period queried in a request cannot be longer than 31 days.
        :type EndTime: str
        :param SdkAppId: Application ID, which is optional. If it is specified, duration statistics for the specified application are returned; otherwise, the total durations of all applications are returned.
        :type SdkAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrtcMcuTranscodeTimeResponse(AbstractModel):
    """DescribeTrtcMcuTranscodeTime response structure.

    """

    def __init__(self):
        r"""
        :param Usages: Duration statistics of the queried application(s)
        :type Usages: list of OneSdkAppIdTranscodeTimeUsagesInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Usages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = OneSdkAppIdTranscodeTimeUsagesInfo()
                obj._deserialize(item)
                self.Usages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserInformationRequest(AbstractModel):
    """DescribeUserInformation request structure.

    """

    def __init__(self):
        r"""
        :param CommId: Unique ID of a call: sdkappid_roomgString_createTime. The `roomgString` refers to the room ID, and `createTime` refers to the creation time of a room in the format of UNIX timestamp in seconds, such as 1400353843_218695_1590065777. Its value can be obtained from the `DescribeRoomInformation` API (related document: https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1).
        :type CommId: str
        :param StartTime: Query start time (s) in the format of Unix timestamp (e.g., 1590065777), which must be a time point in the last 14 days
        :type StartTime: int
        :param EndTime: Query end time (s) in the format of Unix timestamp (e.g., 1590065877)
        :type EndTime: int
        :param SdkAppId: `SDKAppID` of the users to query, e.g., 1400353843
        :type SdkAppId: str
        :param UserIds: The array of user IDs for query. You can enter up to 6 user IDs. If it is left empty, data of 6 users will be returned.
        :type UserIds: list of str
        :param PageNumber: Page index starting from 0. If either `PageNumber` or `PageSize` is left empty, 6 data entries will be returned.
        :type PageNumber: str
        :param PageSize: Number of entries per page. If either `PageNumber` or `PageSize` is left empty, 6 data entries will be returned. `PageSize` is up to 100.
        :type PageSize: str
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.UserIds = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.UserIds = params.get("UserIds")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInformationResponse(AbstractModel):
    """DescribeUserInformation response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total number of users whose information will be returned
        :type Total: int
        :param UserList: User information list
Note: this field may return `null`, indicating that no valid value was found.
        :type UserList: list of UserInformation
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.UserList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self.UserList.append(obj)
        self.RequestId = params.get("RequestId")


class DismissRoomByStrRoomIdRequest(AbstractModel):
    """DismissRoomByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: `SDKAppId` of TRTC
        :type SdkAppId: int
        :param RoomId: Room ID
        :type RoomId: str
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomByStrRoomIdResponse(AbstractModel):
    """DismissRoomByStrRoomId response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    """DismissRoom request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomResponse(AbstractModel):
    """DismissRoom response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param AudioSampleRate: Output audio sample rate (Hz) for On-Cloud MixTranscoding. Valid values: 48000, 44100, 32000, 24000, 16000, 8000
        :type AudioSampleRate: int
        :param AudioBitrate: Output audio bitrate (Kbps) for On-Cloud MixTranscoding. Value range: 8-500
        :type AudioBitrate: int
        :param AudioChannels: Number of sound channels of output stream for On-Cloud MixTranscoding. Valid values: 1, 2. 1 represents mono-channel, and 2 represents dual-channel.
        :type AudioChannels: int
        :param VideoWidth: Output stream width in pixels for On-Cloud MixTranscoding, which is required for audio/video output. Value range: [0, 1920].
        :type VideoWidth: int
        :param VideoHeight: Output stream height in pixels for On-Cloud MixTranscoding, which is required for audio/video output. Value range: [0, 1080].
        :type VideoHeight: int
        :param VideoBitrate: Output bitrate (Kbps) for On-Cloud MixTranscoding, which is required for audio-video output. Value range: 1-10000
        :type VideoBitrate: int
        :param VideoFramerate: Output stream frame rate for On-Cloud MixTranscoding in FPS. This parameter is required for audio/video outputs. Value range: [1, 60].
        :type VideoFramerate: int
        :param VideoGop: Output stream GOP in seconds for On-Cloud MixTranscoding, which is required for audio/video output. Value range: [1, 5].
        :type VideoGop: int
        :param BackgroundColor: Output background color for On-Cloud MixTranscoding. Valid values: decimal integers. Commonly used colors include:
Red: 0xff0000, whose decimal number is 16724736
Yellow: 0xffff00, whose decimal number is 16776960
Green: 0x33cc00, whose decimal number is 3394560
Blue: 0x0066ff, whose decimal number is 26367
Black: 0x000000, whose decimal number is 0
White: 0xFFFFFF, whose decimal number is 16777215
Grey: 0x999999, whose decimal number is 10066329
        :type BackgroundColor: int
        :param BackgroundImageId: Output stream background image for stream mix. Its value is the ID of image uploaded through the TRTC Console.
        :type BackgroundImageId: int
        :param AudioCodec: Output audio codec for On-Cloud MixTranscoding. Valid values: 0, 1, 2. 0 (default): LC-AAC; 1: HE-AAC; 2: HE-AACv2. If this parameter is set to 2 (HE-AACv2), On-Cloud MixTranscoding can produce only dual-channel streams. If it is set to 1 (HE-AAC) or 2 (HE-AACv2), the valid values for the audio sample rate of output streams are 48000, 44100, 32000, 24000, and 16000.
        :type AudioCodec: int
        :param BackgroundImageUrl: URL of the background image for the mixed stream, which can be in PNG, JPG, JPEG, or BMP format and does not support the alpha channel. The URL must not exceed 512 bytes. When both `BackgroundImageUrl` and `BackgroundImageId` are specified, the former will be used. The background image must not exceed 10 MB.
        :type BackgroundImageUrl: str
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
        self.AudioCodec = None
        self.BackgroundImageUrl = None


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
        self.AudioCodec = params.get("AudioCodec")
        self.BackgroundImageUrl = params.get("BackgroundImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventList(AbstractModel):
    """List of SDK or WebRTC events.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventMessage(AbstractModel):
    """Event information, including event timestamp and event ID.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayoutParams(AbstractModel):
    """MCU On-Cloud MixTranscoding layout parameters

    """

    def __init__(self):
        r"""
        :param Template: On-cloud stream mix layout template ID. 0: floating template (default value); 1: grid template; 2: screen sharing template; 3: picture-in-picture template; 4: custom template.
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
        :param PresetLayoutConfig: Valid in custom template, used to specify the video image position of a user in mixed streams.
        :type PresetLayoutConfig: list of PresetLayoutConfig
        :param PlaceHolderMode: Valid in custom templates. 1: the placeholding feature is enabled; 0 (default): the feature is disabled. When the feature is enabled, but a user for whom a position is reserved is not sending video data, the position will show the corresponding placeholder image.
        :type PlaceHolderMode: int
        :param PureAudioHoldPlaceMode: Whether an audio-only stream occupies an image spot, which takes effect in a floating, grid, or screen sharing template. Valid values: 0 (default): when a floating or grid template is used, users sending audio only occupy image spots; when a screen sharing template is used, users (except the user whose screen is shared) sending audio only do not occupy image spots; 1: users sending audio only occupy image spots; 2: users sending audio only do not occupy image spots.
        :type PureAudioHoldPlaceMode: int
        :param WaterMarkParams: Watermark parameters
        :type WaterMarkParams: :class:`tencentcloud.trtc.v20190722.models.WaterMarkParams`
        """
        self.Template = None
        self.MainVideoUserId = None
        self.MainVideoStreamType = None
        self.SmallVideoLayoutParams = None
        self.MainVideoRightAlign = None
        self.MixVideoUids = None
        self.PresetLayoutConfig = None
        self.PlaceHolderMode = None
        self.PureAudioHoldPlaceMode = None
        self.WaterMarkParams = None


    def _deserialize(self, params):
        self.Template = params.get("Template")
        self.MainVideoUserId = params.get("MainVideoUserId")
        self.MainVideoStreamType = params.get("MainVideoStreamType")
        if params.get("SmallVideoLayoutParams") is not None:
            self.SmallVideoLayoutParams = SmallVideoLayoutParams()
            self.SmallVideoLayoutParams._deserialize(params.get("SmallVideoLayoutParams"))
        self.MainVideoRightAlign = params.get("MainVideoRightAlign")
        self.MixVideoUids = params.get("MixVideoUids")
        if params.get("PresetLayoutConfig") is not None:
            self.PresetLayoutConfig = []
            for item in params.get("PresetLayoutConfig"):
                obj = PresetLayoutConfig()
                obj._deserialize(item)
                self.PresetLayoutConfig.append(obj)
        self.PlaceHolderMode = params.get("PlaceHolderMode")
        self.PureAudioHoldPlaceMode = params.get("PureAudioHoldPlaceMode")
        if params.get("WaterMarkParams") is not None:
            self.WaterMarkParams = WaterMarkParams()
            self.WaterMarkParams._deserialize(params.get("WaterMarkParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPictureRequest(AbstractModel):
    """ModifyPicture request structure.

    """

    def __init__(self):
        r"""
        :param PictureId: Image ID
        :type PictureId: int
        :param SdkAppId: Application ID
        :type SdkAppId: int
        :param Height: Image height
        :type Height: int
        :param Width: Image width
        :type Width: int
        :param XPosition: X-axis value of the image’s position
        :type XPosition: int
        :param YPosition: Y-axis value of the image’s position
        :type YPosition: int
        """
        self.PictureId = None
        self.SdkAppId = None
        self.Height = None
        self.Width = None
        self.XPosition = None
        self.YPosition = None


    def _deserialize(self, params):
        self.PictureId = params.get("PictureId")
        self.SdkAppId = params.get("SdkAppId")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPictureResponse(AbstractModel):
    """ModifyPicture response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OneSdkAppIdTranscodeTimeUsagesInfo(AbstractModel):
    """Relaying and transcoding duration statistics

    """

    def __init__(self):
        r"""
        :param SdkAppIdTranscodeTimeUsages: Array of relaying and transcoding durations
        :type SdkAppIdTranscodeTimeUsages: list of SdkAppIdTrtcMcuTranscodeTimeUsage
        :param TotalNum: Number of records returned
        :type TotalNum: int
        :param SdkAppId: ID of the application queried. Its value may be an application ID or `total`, which indicates that the total durations of all applications are queried.
        :type SdkAppId: str
        """
        self.SdkAppIdTranscodeTimeUsages = None
        self.TotalNum = None
        self.SdkAppId = None


    def _deserialize(self, params):
        if params.get("SdkAppIdTranscodeTimeUsages") is not None:
            self.SdkAppIdTranscodeTimeUsages = []
            for item in params.get("SdkAppIdTranscodeTimeUsages"):
                obj = SdkAppIdTrtcMcuTranscodeTimeUsage()
                obj._deserialize(item)
                self.SdkAppIdTranscodeTimeUsages.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OneSdkAppIdUsagesInfo(AbstractModel):
    """Array of billable audio/video interaction durations of a specific application (`SdkAppId`) and array length

    """

    def __init__(self):
        r"""
        :param TotalNum: Number of records returned for the `SdkAppId`
        :type TotalNum: int
        :param SdkAppIdTrtcTimeUsages: Array of durations
        :type SdkAppIdTrtcTimeUsages: list of SdkAppIdTrtcUsage
        :param SdkAppId: Application ID
        :type SdkAppId: str
        """
        self.TotalNum = None
        self.SdkAppIdTrtcTimeUsages = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("SdkAppIdTrtcTimeUsages") is not None:
            self.SdkAppIdTrtcTimeUsages = []
            for item in params.get("SdkAppIdTrtcTimeUsages"):
                obj = SdkAppIdTrtcUsage()
                obj._deserialize(item)
                self.SdkAppIdTrtcTimeUsages.append(obj)
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputParams(AbstractModel):
    """MCU On-Cloud MixTranscoding output parameters

    """

    def __init__(self):
        r"""
        :param StreamId: Custom live stream ID, which must be different from the ID of relayed stream.
        :type StreamId: str
        :param PureAudioStream: Value range: [0, 1]. If it is 0, live streams are audio and video; if it is 1, live streams are only audio. Default value: 0.
        :type PureAudioStream: int
        :param RecordId: Prefix of custom recording file names. Please enable the recording feature in the TRTC console first. https://intl.cloud.tencent.com/document/product/647/50768?from_cn_redirect=1
        :type RecordId: str
        :param RecordAudioOnly: Whether to record audio only. Valid values: 0, 1. `0`: no meaning; `1`: records into MP3 files. This parameter is not recommended. Instead, you are advised to create an audio-only recording template in the TRTC console.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PictureInfo(AbstractModel):
    """Image information list

    """

    def __init__(self):
        r"""
        :param Height: Image height
        :type Height: int
        :param Width: Image width
        :type Width: int
        :param XPosition: X-axis value of the image’s position
        :type XPosition: int
        :param YPosition: Y-axis value of the image’s position
        :type YPosition: int
        :param SdkAppId: Application ID
        :type SdkAppId: int
        :param PictureId: Image ID
        :type PictureId: int
        """
        self.Height = None
        self.Width = None
        self.XPosition = None
        self.YPosition = None
        self.SdkAppId = None
        self.PictureId = None


    def _deserialize(self, params):
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.SdkAppId = params.get("SdkAppId")
        self.PictureId = params.get("PictureId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PresetLayoutConfig(AbstractModel):
    """Valid in custom template, used to specify the video image position of a user in mixed streams.

    """

    def __init__(self):
        r"""
        :param UserId: Used to assign users to preset positions; if not assigned, users will occupy the positions set in `PresetLayoutConfig` in room entry sequence.
        :type UserId: str
        :param StreamType: Stream type of the user when a specified user is assigned to the image. 0: camera; 1: screen sharing. Set this parameter to 0 when the small image is occupied by a web user.
        :type StreamType: int
        :param ImageWidth: Width of the output image in pixels. If this parameter is not set, 0 is used by default.
        :type ImageWidth: int
        :param ImageHeight: Height of the output image in pixels. If this parameter is not set, 0 is used by default.
        :type ImageHeight: int
        :param LocationX: X offset of the output image in pixels. The sum of `LocationX` and `ImageWidth` cannot exceed the total width of the mixed stream. If this parameter is not set, 0 is used by default.
        :type LocationX: int
        :param LocationY: Y offset of the output image in pixels. The sum of `LocationY` and `ImageHeight` cannot exceed the total height of the mixed stream. If this parameter is not set, 0 is used by default.
        :type LocationY: int
        :param ZOrder: Output order of the image. `0` is used if it is left empty.
        :type ZOrder: int
        :param RenderMode: Render mode of the output image. 0: cropping; 1: scaling; 2: scaling on a black background. If this parameter is not set, 0 is used by default.
        :type RenderMode: int
        :param MixInputType: Media type of the mixed stream of the user occupying the current position. 0 (default): audio and video; 1: audio; 2: video. You are advised to specify a user ID when using this parameter.
        :type MixInputType: int
        :param PlaceImageId: ID of the placeholder image. If the placeholding feature is enabled, and a user for whom an image position is reserved is not sending video data, the position will show the placeholder image. The ID is generated after the placeholder image is uploaded in the TRTC console. https://intl.cloud.tencent.com/document/product/647/50769?from_cn_redirect=1
        :type PlaceImageId: int
        """
        self.UserId = None
        self.StreamType = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None
        self.ZOrder = None
        self.RenderMode = None
        self.MixInputType = None
        self.PlaceImageId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.StreamType = params.get("StreamType")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.ZOrder = params.get("ZOrder")
        self.RenderMode = params.get("RenderMode")
        self.MixInputType = params.get("MixInputType")
        self.PlaceImageId = params.get("PlaceImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishCdnParams(AbstractModel):
    """Relayed push parameters of a non-Tencent Cloud CDN

    """

    def __init__(self):
        r"""
        :param BizId: Tencent Cloud LVB BizId
        :type BizId: int
        :param PublishCdnUrls: Destination of non-Tencent Cloud CDN relayed push. It is possible to push to only one non-Tencent Cloud CDN address at a time.
        :type PublishCdnUrls: list of str
        """
        self.BizId = None
        self.PublishCdnUrls = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.PublishCdnUrls = params.get("PublishCdnUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityData(AbstractModel):
    """Quality data returned by ES

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordUsage(AbstractModel):
    """Recording duration statistics

    """

    def __init__(self):
        r"""
        :param TimeKey: Time point for the statistics, e.g., `2020-09-07` or `2020-09-07 00:05:05`
        :type TimeKey: str
        :param Class1VideoTime: SD video duration (s)
        :type Class1VideoTime: int
        :param Class2VideoTime: HD video duration (s)
        :type Class2VideoTime: int
        :param Class3VideoTime: FHD video duration (s)
        :type Class3VideoTime: int
        :param AudioTime: Audio duration (s)
        :type AudioTime: int
        """
        self.TimeKey = None
        self.Class1VideoTime = None
        self.Class2VideoTime = None
        self.Class3VideoTime = None
        self.AudioTime = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.Class1VideoTime = params.get("Class1VideoTime")
        self.Class2VideoTime = params.get("Class2VideoTime")
        self.Class3VideoTime = params.get("Class3VideoTime")
        self.AudioTime = params.get("AudioTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdRequest(AbstractModel):
    """RemoveUserByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: `SDKAppId` of TRTC
        :type SdkAppId: int
        :param RoomId: Room ID
        :type RoomId: str
        :param UserIds: List of up to 10 users to be removed
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdResponse(AbstractModel):
    """RemoveUserByStrRoomId response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveUserRequest(AbstractModel):
    """RemoveUser request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserResponse(AbstractModel):
    """RemoveUser response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleInfomation(AbstractModel):
    """Historical scale information

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SdkAppIdRecordUsage(AbstractModel):
    """Recording duration statistics of a specific application (`SdkAppId`)

    """

    def __init__(self):
        r"""
        :param SdkAppId: Application ID
        :type SdkAppId: str
        :param Usages: Durations for the period queried
        :type Usages: list of RecordUsage
        """
        self.SdkAppId = None
        self.Usages = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = RecordUsage()
                obj._deserialize(item)
                self.Usages.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SdkAppIdTrtcMcuTranscodeTimeUsage(AbstractModel):
    """Billable relaying and transcoding duration statistics
    If the period queried is 1 day or shorter, the statistics returned are on a 5-minute basis. If the period queried is longer than 1 day, the statistics returned are on a daily basis.

    """

    def __init__(self):
        r"""
        :param TimeKey: Time point for the statistics. e.g., `2020-09-07` or `2020-09-07 00:05:05`
        :type TimeKey: str
        :param AudioTime: Audio duration (s)
        :type AudioTime: int
        :param VideoTimeSd: SD video duration (s)
        :type VideoTimeSd: int
        :param VideoTimeHd: HD video duration (s)
        :type VideoTimeHd: int
        :param VideoTimeFhd: FHD video duration (s)
        :type VideoTimeFhd: int
        """
        self.TimeKey = None
        self.AudioTime = None
        self.VideoTimeSd = None
        self.VideoTimeHd = None
        self.VideoTimeFhd = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.AudioTime = params.get("AudioTime")
        self.VideoTimeSd = params.get("VideoTimeSd")
        self.VideoTimeHd = params.get("VideoTimeHd")
        self.VideoTimeFhd = params.get("VideoTimeFhd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SdkAppIdTrtcUsage(AbstractModel):
    """Audio/Video interaction duration statistics
    If the period queried is 1 day or shorter, the statistics returned are on a 5-minute basis. If the period queried is longer than 1 day, the statistics returned are on a daily basis.

    """

    def __init__(self):
        r"""
        :param TimeKey: Time point for the statistics. e.g., `2020-09-07` or `2020-09-07 00:05:05`
        :type TimeKey: str
        :param AudioTime: Audio duration (s)
        :type AudioTime: int
        :param AudioVideoTime: Audio/Video duration (s)
This parameter is returned only for users who signed up before October 11, 2019 and have not switched to the [new billing standards](https://intl.cloud.tencent.com/document/product/647/17157?from_cn_redirect=1).
        :type AudioVideoTime: int
        :param VideoTimeSd: SD video duration (s)
        :type VideoTimeSd: int
        :param VideoTimeHd: HD video duration (s)
        :type VideoTimeHd: int
        :param VideoTimeHdp: FHD video duration (s)
        :type VideoTimeHdp: int
        """
        self.TimeKey = None
        self.AudioTime = None
        self.AudioVideoTime = None
        self.VideoTimeSd = None
        self.VideoTimeHd = None
        self.VideoTimeHdp = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.AudioTime = params.get("AudioTime")
        self.AudioVideoTime = params.get("AudioVideoTime")
        self.VideoTimeSd = params.get("VideoTimeSd")
        self.VideoTimeHd = params.get("VideoTimeHd")
        self.VideoTimeHdp = params.get("VideoTimeHdp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmallVideoLayoutParams(AbstractModel):
    """Layout parameter of the small image, which takes effect in a picture-in-picture template

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMCUMixTranscodeByStrRoomIdRequest(AbstractModel):
    """StartMCUMixTranscodeByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: `SDKAppId` of TRTC
        :type SdkAppId: int
        :param StrRoomId: Room ID in string type
        :type StrRoomId: str
        :param OutputParams: On-Cloud MixTranscoding output parameters
        :type OutputParams: :class:`tencentcloud.trtc.v20190722.models.OutputParams`
        :param EncodeParams: On-Cloud MixTranscoding output encoding parameters
        :type EncodeParams: :class:`tencentcloud.trtc.v20190722.models.EncodeParams`
        :param LayoutParams: On-Cloud MixTranscoding output layout parameters
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.LayoutParams`
        :param PublishCdnParams: Relayed push parameters of a non-Tencent Cloud CDN
        :type PublishCdnParams: :class:`tencentcloud.trtc.v20190722.models.PublishCdnParams`
        """
        self.SdkAppId = None
        self.StrRoomId = None
        self.OutputParams = None
        self.EncodeParams = None
        self.LayoutParams = None
        self.PublishCdnParams = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StrRoomId = params.get("StrRoomId")
        if params.get("OutputParams") is not None:
            self.OutputParams = OutputParams()
            self.OutputParams._deserialize(params.get("OutputParams"))
        if params.get("EncodeParams") is not None:
            self.EncodeParams = EncodeParams()
            self.EncodeParams._deserialize(params.get("EncodeParams"))
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        if params.get("PublishCdnParams") is not None:
            self.PublishCdnParams = PublishCdnParams()
            self.PublishCdnParams._deserialize(params.get("PublishCdnParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMCUMixTranscodeByStrRoomIdResponse(AbstractModel):
    """StartMCUMixTranscodeByStrRoomId response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartMCUMixTranscodeRequest(AbstractModel):
    """StartMCUMixTranscode request structure.

    """

    def __init__(self):
        r"""
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
        :param PublishCdnParams: Relayed push parameters of a non-Tencent Cloud CDN
        :type PublishCdnParams: :class:`tencentcloud.trtc.v20190722.models.PublishCdnParams`
        """
        self.SdkAppId = None
        self.RoomId = None
        self.OutputParams = None
        self.EncodeParams = None
        self.LayoutParams = None
        self.PublishCdnParams = None


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
        if params.get("PublishCdnParams") is not None:
            self.PublishCdnParams = PublishCdnParams()
            self.PublishCdnParams._deserialize(params.get("PublishCdnParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMCUMixTranscodeResponse(AbstractModel):
    """StartMCUMixTranscode response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMCUMixTranscodeByStrRoomIdRequest(AbstractModel):
    """StopMCUMixTranscodeByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: `SDKAppId` of TRTC
        :type SdkAppId: int
        :param StrRoomId: Room ID in string type
        :type StrRoomId: str
        """
        self.SdkAppId = None
        self.StrRoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StrRoomId = params.get("StrRoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMCUMixTranscodeByStrRoomIdResponse(AbstractModel):
    """StopMCUMixTranscodeByStrRoomId response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMCUMixTranscodeResponse(AbstractModel):
    """StopMCUMixTranscode response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInformation(AbstractModel):
    """User information, including when the user enters/exits a room

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkParams(AbstractModel):
    """Watermark parameters for On-Cloud MixTranscoding

    """

    def __init__(self):
        r"""
        :param WaterMarkId: Image ID of the watermark, which is generated after the image is uploaded to the TRTC console
        :type WaterMarkId: int
        :param WaterMarkWidth: Width (px) of the watermark for On-Cloud MixTranscoding
        :type WaterMarkWidth: int
        :param WaterMarkHeight: Height (px) of the watermark for On-Cloud MixTranscoding
        :type WaterMarkHeight: int
        :param LocationX: Horizontal offset (px) of the watermark
        :type LocationX: int
        :param LocationY: Vertical offset (px) of the watermark
        :type LocationY: int
        :param WaterMarkUrl: URL of the watermark image for the mixed stream, which can be in PNG, JPG, JPEG, or BMP format and does not support the alpha channel. The URL must not exceed 512 bytes. When both `WaterMarkUrl` and `WaterMarkId` are specified, the former will be used. The watermark image cannot exceed 10 MB.
        :type WaterMarkUrl: str
        """
        self.WaterMarkId = None
        self.WaterMarkWidth = None
        self.WaterMarkHeight = None
        self.LocationX = None
        self.LocationY = None
        self.WaterMarkUrl = None


    def _deserialize(self, params):
        self.WaterMarkId = params.get("WaterMarkId")
        self.WaterMarkWidth = params.get("WaterMarkWidth")
        self.WaterMarkHeight = params.get("WaterMarkHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.WaterMarkUrl = params.get("WaterMarkUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        