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


class AppCustomContent(AbstractModel):
    """Custom application content

    """

    def __init__(self):
        r"""
        :param Scene: Multiple scenarios can be set for an application.
        :type Scene: str
        :param LogoUrl: Logo URL
        :type LogoUrl: str
        :param HomeUrl: Homepage URL, which can be used for redirection
        :type HomeUrl: str
        :param JsUrl: Custom JS URL
        :type JsUrl: str
        :param CssUrl: Custom CSS URL
        :type CssUrl: str
        """
        self.Scene = None
        self.LogoUrl = None
        self.HomeUrl = None
        self.JsUrl = None
        self.CssUrl = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.LogoUrl = params.get("LogoUrl")
        self.HomeUrl = params.get("HomeUrl")
        self.JsUrl = params.get("JsUrl")
        self.CssUrl = params.get("CssUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDocumentToRoomRequest(AbstractModel):
    """BindDocumentToRoom request structure.

    """

    def __init__(self):
        r"""
        :param RoomId: Room ID
        :type RoomId: int
        :param DocumentId: Document ID
        :type DocumentId: str
        :param BindType: Binding type. The default value is `0`. The backend passes through this parameter to clients so that the clients can implement business logic based on this parameter.
        :type BindType: int
        """
        self.RoomId = None
        self.DocumentId = None
        self.BindType = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.DocumentId = params.get("DocumentId")
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDocumentToRoomResponse(AbstractModel):
    """BindDocumentToRoom response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDocumentRequest(AbstractModel):
    """CreateDocument request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: LCIC SdkAppId
        :type SdkAppId: int
        :param DocumentUrl: Document URL	
        :type DocumentUrl: str
        :param DocumentName: Document name	
        :type DocumentName: str
        :param Owner: Document owner ID	
        :type Owner: str
        :param TranscodeType: Transcoding type. Valid values: `0`: No transcoding required (default); `1`: Documents that need to be transcoded: ppt, pptx, pdf, doc, docx; `2`: Videos that need to be transcoded: mp4, 3pg, mpeg, avi, flv, wmv, rm, h264, etc.; `2`: Audio that needs to be transcoded: mp3, wav, wma, aac, flac, opus
        :type TranscodeType: int
        :param Permission: Permission. Valid values: `0`: Private document (default); `1`: Public document
        :type Permission: int
        :param DocumentType: Document extension
        :type DocumentType: str
        :param DocumentSize: Document size, in bytes
        :type DocumentSize: int
        """
        self.SdkAppId = None
        self.DocumentUrl = None
        self.DocumentName = None
        self.Owner = None
        self.TranscodeType = None
        self.Permission = None
        self.DocumentType = None
        self.DocumentSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.DocumentUrl = params.get("DocumentUrl")
        self.DocumentName = params.get("DocumentName")
        self.Owner = params.get("Owner")
        self.TranscodeType = params.get("TranscodeType")
        self.Permission = params.get("Permission")
        self.DocumentType = params.get("DocumentType")
        self.DocumentSize = params.get("DocumentSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocumentResponse(AbstractModel):
    """CreateDocument response structure.

    """

    def __init__(self):
        r"""
        :param DocumentId: Document ID
        :type DocumentId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DocumentId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        self.RequestId = params.get("RequestId")


class CreateRoomRequest(AbstractModel):
    """CreateRoom request structure.

    """

    def __init__(self):
        r"""
        :param Name: Room name
        :type Name: str
        :param StartTime: Reserved room start time, in UNIX timestamp format
        :type StartTime: int
        :param EndTime: Reserved room end time, in UNIX timestamp format
        :type EndTime: int
        :param SdkAppId: LCIC SdkAppId
        :type SdkAppId: int
        :param Resolution: Resolution. Valid values: `1`: SD; `2`: HD; `3`: FHD
        :type Resolution: int
        :param MaxMicNumber: Maximum number of mic-on users (excluding teachers). Value range: [0, 16]	
        :type MaxMicNumber: int
        :param SubType: Room subtype. Valid values: `videodoc`: Document + Video; `video`: Video only; `coteaching`: Dual-teacher
        :type SubType: str
        :param TeacherId: Teacher ID, which is the `UserId` obtained by the `RegisterUser` API.
        :type TeacherId: str
        :param AutoMic: Whether to automatically turn the mic on when the user enters a room. Valid values: `0`: No (default value); `1`: Yes.
        :type AutoMic: int
        :param AudioQuality: Whether to enable the high audio quality mode. Valid values: `0`: No (default value); `1`: Yes.
        :type AudioQuality: int
        :param DisableRecord: Whether to disable auto recording. Valid values: `0`: No (default); `1`: Yes. If this parameter is `0`, recording will start when the class starts and stops when the class ends.
        :type DisableRecord: int
        :param Assistants: Teacher assistant IDs, which are the `UserId` obtained by the `RegisterUser` API.
        :type Assistants: list of str
        :param RecordLayout: Recording layout
        :type RecordLayout: int
        """
        self.Name = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.Resolution = None
        self.MaxMicNumber = None
        self.SubType = None
        self.TeacherId = None
        self.AutoMic = None
        self.AudioQuality = None
        self.DisableRecord = None
        self.Assistants = None
        self.RecordLayout = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.Resolution = params.get("Resolution")
        self.MaxMicNumber = params.get("MaxMicNumber")
        self.SubType = params.get("SubType")
        self.TeacherId = params.get("TeacherId")
        self.AutoMic = params.get("AutoMic")
        self.AudioQuality = params.get("AudioQuality")
        self.DisableRecord = params.get("DisableRecord")
        self.Assistants = params.get("Assistants")
        self.RecordLayout = params.get("RecordLayout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoomResponse(AbstractModel):
    """CreateRoom response structure.

    """

    def __init__(self):
        r"""
        :param RoomId: Room ID
        :type RoomId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoomId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.RequestId = params.get("RequestId")


class CreateSupervisorRequest(AbstractModel):
    """CreateSupervisor request structure.

    """


class CreateSupervisorResponse(AbstractModel):
    """CreateSupervisor response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoomRequest(AbstractModel):
    """DeleteRoom request structure.

    """

    def __init__(self):
        r"""
        :param RoomId: Room ID
        :type RoomId: int
        """
        self.RoomId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomResponse(AbstractModel):
    """DeleteRoom response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeRoomRequest(AbstractModel):
    """DescribeRoom request structure.

    """

    def __init__(self):
        r"""
        :param RoomId: Room ID	
        :type RoomId: int
        """
        self.RoomId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomResponse(AbstractModel):
    """DescribeRoom response structure.

    """

    def __init__(self):
        r"""
        :param Name: Room name	
        :type Name: str
        :param StartTime: Reserved room start time, in UNIX timestamp format	
        :type StartTime: int
        :param EndTime: Reserved room end time, in UNIX timestamp format	
        :type EndTime: int
        :param TeacherId: Teacher ID	
        :type TeacherId: str
        :param SdkAppId: LCIC SdkAppId	
        :type SdkAppId: int
        :param Resolution: Resolution. Valid values: `1`: SD; `2`: HD; `3`: FHD	
        :type Resolution: int
        :param MaxMicNumber: Maximum number of mic-on users (excluding teachers). Value range: [0, 16]	
        :type MaxMicNumber: int
        :param AutoMic: Whether to automatically turn the mic on when the user enters a room. Valid values: `0`: No (default value); `1`: Yes.	
        :type AutoMic: int
        :param AudioQuality: Whether to enable the high audio quality mode. Valid values: `0`: No (default value); `1`: Yes.	
        :type AudioQuality: int
        :param SubType: Room subtype. Valid values: `videodoc`: Document + Video; `video`: Video only; `coteaching`: Dual-teacher	
        :type SubType: str
        :param DisableRecord: Whether to disable auto recording. Valid values: `0`: No (default); `1`: Yes. If this parameter is `0`, recording will start when the class starts and stops when the class ends.	
        :type DisableRecord: int
        :param Assistants: Assistant ID list	
Note: This field may return null, indicating that no valid values can be obtained.
        :type Assistants: list of str
        :param RecordUrl: Recording URL. This parameter exists only after a room is ended.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.StartTime = None
        self.EndTime = None
        self.TeacherId = None
        self.SdkAppId = None
        self.Resolution = None
        self.MaxMicNumber = None
        self.AutoMic = None
        self.AudioQuality = None
        self.SubType = None
        self.DisableRecord = None
        self.Assistants = None
        self.RecordUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TeacherId = params.get("TeacherId")
        self.SdkAppId = params.get("SdkAppId")
        self.Resolution = params.get("Resolution")
        self.MaxMicNumber = params.get("MaxMicNumber")
        self.AutoMic = params.get("AutoMic")
        self.AudioQuality = params.get("AudioQuality")
        self.SubType = params.get("SubType")
        self.DisableRecord = params.get("DisableRecord")
        self.Assistants = params.get("Assistants")
        self.RecordUrl = params.get("RecordUrl")
        self.RequestId = params.get("RequestId")


class DescribeRoomStatisticsRequest(AbstractModel):
    """DescribeRoomStatistics request structure.

    """

    def __init__(self):
        r"""
        :param RoomId: Room ID
        :type RoomId: int
        :param Page: Current page in pagination, which starts from 1.
        :type Page: int
        :param Limit: Number of data entries to return per page. Maximum value: 1000
        :type Limit: int
        """
        self.RoomId = None
        self.Page = None
        self.Limit = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.Page = params.get("Page")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomStatisticsResponse(AbstractModel):
    """DescribeRoomStatistics response structure.

    """

    def __init__(self):
        r"""
        :param PeakMemberNumber: Peak number of online members
        :type PeakMemberNumber: int
        :param MemberNumber: Accumulated number of online members
        :type MemberNumber: int
        :param Total: Total number of records, including members who entered the room and members who should attend the class but did not
        :type Total: int
        :param MemberRecords: Member record list
        :type MemberRecords: list of MemberRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PeakMemberNumber = None
        self.MemberNumber = None
        self.Total = None
        self.MemberRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PeakMemberNumber = params.get("PeakMemberNumber")
        self.MemberNumber = params.get("MemberNumber")
        self.Total = params.get("Total")
        if params.get("MemberRecords") is not None:
            self.MemberRecords = []
            for item in params.get("MemberRecords"):
                obj = MemberRecord()
                obj._deserialize(item)
                self.MemberRecords.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    """DescribeUser request structure.

    """

    def __init__(self):
        r"""
        :param UserId: User ID	
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    """DescribeUser response structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The application ID.	
        :type SdkAppId: int
        :param UserId: User ID	
        :type UserId: str
        :param Name: Username	
        :type Name: str
        :param Avatar: URL of user profile photo.	
        :type Avatar: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SdkAppId = None
        self.UserId = None
        self.Name = None
        self.Avatar = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.UserId = params.get("UserId")
        self.Name = params.get("Name")
        self.Avatar = params.get("Avatar")
        self.RequestId = params.get("RequestId")


class LoginOriginIdRequest(AbstractModel):
    """LoginOriginId request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: LCIC SdkAppId
        :type SdkAppId: int
        :param OriginId: User's ID in the customer system, which should be unique under the same application
        :type OriginId: str
        """
        self.SdkAppId = None
        self.OriginId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginOriginIdResponse(AbstractModel):
    """LoginOriginId response structure.

    """

    def __init__(self):
        r"""
        :param UserId: User ID
        :type UserId: str
        :param Token: Login status token returned after successful login or registration. The token is valid for seven days.
        :type Token: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserId = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class LoginUserRequest(AbstractModel):
    """LoginUser request structure.

    """

    def __init__(self):
        r"""
        :param UserId: User ID obtained during registration
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginUserResponse(AbstractModel):
    """LoginUser response structure.

    """

    def __init__(self):
        r"""
        :param UserId: User ID
        :type UserId: str
        :param Token: Login status token returned after successful login or registration. The token is valid for seven days.
        :type Token: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserId = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class MemberRecord(AbstractModel):
    """Member record information

    """

    def __init__(self):
        r"""
        :param UserId: User ID
        :type UserId: str
        :param UserName: Username
        :type UserName: str
        :param PresentTime: Online duration, in seconds
        :type PresentTime: int
        :param Camera: Whether the camera is enabled
        :type Camera: int
        :param Mic: Whether the mic is enabled
        :type Mic: int
        :param Silence: Whether the user is muted
        :type Silence: int
        :param AnswerQuestions: Number of questions answered by the user
        :type AnswerQuestions: int
        :param HandUps: Number of hand raising times
        :type HandUps: int
        :param FirstJoinTimestamp: First time that the user entered the room, in UNIX timestamp format
        :type FirstJoinTimestamp: int
        :param LastQuitTimestamp: Last time that the user left the room, in UNIX timestamp format
        :type LastQuitTimestamp: int
        :param Rewords: Number of rewards received
        :type Rewords: int
        """
        self.UserId = None
        self.UserName = None
        self.PresentTime = None
        self.Camera = None
        self.Mic = None
        self.Silence = None
        self.AnswerQuestions = None
        self.HandUps = None
        self.FirstJoinTimestamp = None
        self.LastQuitTimestamp = None
        self.Rewords = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        self.PresentTime = params.get("PresentTime")
        self.Camera = params.get("Camera")
        self.Mic = params.get("Mic")
        self.Silence = params.get("Silence")
        self.AnswerQuestions = params.get("AnswerQuestions")
        self.HandUps = params.get("HandUps")
        self.FirstJoinTimestamp = params.get("FirstJoinTimestamp")
        self.LastQuitTimestamp = params.get("LastQuitTimestamp")
        self.Rewords = params.get("Rewords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppRequest(AbstractModel):
    """ModifyApp request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: LCIC SdkAppId
        :type SdkAppId: int
        :param Callback: Callback URL. Currently, only port 80 and port 443 are supported.
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
        


class ModifyAppResponse(AbstractModel):
    """ModifyApp response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterUserRequest(AbstractModel):
    """RegisterUser request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: LCIC SdkAppId	
        :type SdkAppId: int
        :param Name: Username	
        :type Name: str
        :param OriginId: User's ID in the customer system, which should be unique under the same application	
        :type OriginId: str
        :param Avatar: User's profile photo	
        :type Avatar: str
        """
        self.SdkAppId = None
        self.Name = None
        self.OriginId = None
        self.Avatar = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Name = params.get("Name")
        self.OriginId = params.get("OriginId")
        self.Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterUserResponse(AbstractModel):
    """RegisterUser response structure.

    """

    def __init__(self):
        r"""
        :param UserId: User ID	
        :type UserId: str
        :param Token: Login status token returned after successful login or registration. The token is valid for seven days.	
        :type Token: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserId = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class SetAppCustomContentRequest(AbstractModel):
    """SetAppCustomContent request structure.

    """

    def __init__(self):
        r"""
        :param CustomContent: Custom content
        :type CustomContent: list of AppCustomContent
        :param SdkAppId: Application ID
        :type SdkAppId: int
        """
        self.CustomContent = None
        self.SdkAppId = None


    def _deserialize(self, params):
        if params.get("CustomContent") is not None:
            self.CustomContent = []
            for item in params.get("CustomContent"):
                obj = AppCustomContent()
                obj._deserialize(item)
                self.CustomContent.append(obj)
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAppCustomContentResponse(AbstractModel):
    """SetAppCustomContent response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindDocumentFromRoomRequest(AbstractModel):
    """UnbindDocumentFromRoom request structure.

    """

    def __init__(self):
        r"""
        :param RoomId: Room ID	
        :type RoomId: int
        :param DocumentId: Document ID	
        :type DocumentId: str
        """
        self.RoomId = None
        self.DocumentId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDocumentFromRoomResponse(AbstractModel):
    """UnbindDocumentFromRoom response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")