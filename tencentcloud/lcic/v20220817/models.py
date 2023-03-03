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


class AddGroupMemberRequest(AbstractModel):
    """AddGroupMember request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The group ID.
        :type GroupId: str
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param MemberIds: The users. Array length limit: 200.
        :type MemberIds: list of str
        """
        self.GroupId = None
        self.SdkAppId = None
        self.MemberIds = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.SdkAppId = params.get("SdkAppId")
        self.MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddGroupMemberResponse(AbstractModel):
    """AddGroupMember response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
        


class BackgroundPictureConfig(AbstractModel):
    """Background image settings.

    """

    def __init__(self):
        r"""
        :param Url: The URL of the background image.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchAddGroupMemberRequest(AbstractModel):
    """BatchAddGroupMember request structure.

    """

    def __init__(self):
        r"""
        :param GroupIds: The target group IDs. Array length limit: 100.
        :type GroupIds: list of str
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param MemberIds: The users to add. Array length limit: 200.
        :type MemberIds: list of str
        """
        self.GroupIds = None
        self.SdkAppId = None
        self.MemberIds = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.SdkAppId = params.get("SdkAppId")
        self.MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchAddGroupMemberResponse(AbstractModel):
    """BatchAddGroupMember response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchCreateGroupWithMembersRequest(AbstractModel):
    """BatchCreateGroupWithMembers request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param GroupBaseInfos: The information of the groups to create. Array length limit: 256.
        :type GroupBaseInfos: list of GroupBaseInfo
        :param MemberIds: The group members. Array length limit: 200.
        :type MemberIds: list of str
        """
        self.SdkAppId = None
        self.GroupBaseInfos = None
        self.MemberIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("GroupBaseInfos") is not None:
            self.GroupBaseInfos = []
            for item in params.get("GroupBaseInfos"):
                obj = GroupBaseInfo()
                obj._deserialize(item)
                self.GroupBaseInfos.append(obj)
        self.MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateGroupWithMembersResponse(AbstractModel):
    """BatchCreateGroupWithMembers response structure.

    """

    def __init__(self):
        r"""
        :param GroupIds: The IDs of the groups created, which are in the same order as the elements in the request parameter `GroupBaseInfos.N`.
        :type GroupIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.RequestId = params.get("RequestId")


class BatchCreateRoomRequest(AbstractModel):
    """BatchCreateRoom request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param RoomInfos: The information of the rooms to create.
        :type RoomInfos: list of RoomInfo
        """
        self.SdkAppId = None
        self.RoomInfos = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("RoomInfos") is not None:
            self.RoomInfos = []
            for item in params.get("RoomInfos"):
                obj = RoomInfo()
                obj._deserialize(item)
                self.RoomInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateRoomResponse(AbstractModel):
    """BatchCreateRoom response structure.

    """

    def __init__(self):
        r"""
        :param RoomIds: The IDs of the rooms created, which are in the same order as they are passed in.
        :type RoomIds: list of int non-negative
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoomIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoomIds = params.get("RoomIds")
        self.RequestId = params.get("RequestId")


class BatchDeleteGroupMemberRequest(AbstractModel):
    """BatchDeleteGroupMember request structure.

    """

    def __init__(self):
        r"""
        :param GroupIds: The target group IDs. Array length limit: 100.
        :type GroupIds: list of str
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param MemberIds: The users to remove. Array length limit: 256.
        :type MemberIds: list of str
        """
        self.GroupIds = None
        self.SdkAppId = None
        self.MemberIds = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.SdkAppId = params.get("SdkAppId")
        self.MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteGroupMemberResponse(AbstractModel):
    """BatchDeleteGroupMember response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchDeleteRecordRequest(AbstractModel):
    """BatchDeleteRecord request structure.

    """

    def __init__(self):
        r"""
        :param RoomIds: The room IDs.	
        :type RoomIds: list of int
        :param SdkAppId: The SDKAppID assigned by LCIC.	
        :type SdkAppId: int
        """
        self.RoomIds = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.RoomIds = params.get("RoomIds")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteRecordResponse(AbstractModel):
    """BatchDeleteRecord response structure.

    """

    def __init__(self):
        r"""
        :param RoomIds: The IDs of the rooms whose recordings are deleted.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoomIds: list of int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoomIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoomIds = params.get("RoomIds")
        self.RequestId = params.get("RequestId")


class BatchRegisterRequest(AbstractModel):
    """BatchRegister request structure.

    """

    def __init__(self):
        r"""
        :param Users: The information of the users to register.
        :type Users: list of BatchUserRequest
        """
        self.Users = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = BatchUserRequest()
                obj._deserialize(item)
                self.Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterResponse(AbstractModel):
    """BatchRegister response structure.

    """

    def __init__(self):
        r"""
        :param Users: The information of the successfully registered users.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type Users: list of BatchUserInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = BatchUserInfo()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class BatchUserInfo(AbstractModel):
    """The information of registered users.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The SDKAppID assigned by LCIC.

        :type SdkAppId: int
        :param UserId: The user ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param OriginId: The user’s ID in your system. If the same request parameter is not specified, the value of this parameter will be the same as `UserId`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginId: str
        """
        self.SdkAppId = None
        self.UserId = None
        self.OriginId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.UserId = params.get("UserId")
        self.OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUserRequest(AbstractModel):
    """The information of the users to register.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The SDKAppID assigned by LCIC.

Note: This field may return null, indicating that no valid values can be obtained.
        :type SdkAppId: int
        :param Name: The username.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param OriginId: The user’s ID in your system, which must be unique across the same application.

Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginId: str
        :param Avatar: The user’s profile photo.

Note: This field may return null, indicating that no valid values can be obtained.
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


class CreateGroupWithMembersRequest(AbstractModel):
    """CreateGroupWithMembers request structure.

    """

    def __init__(self):
        r"""
        :param GroupName: The group name.
        :type GroupName: str
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param TeacherId: The user ID of the teacher.
        :type TeacherId: str
        :param MemberIds: The group members. Array length limit: 200.
        :type MemberIds: list of str
        """
        self.GroupName = None
        self.SdkAppId = None
        self.TeacherId = None
        self.MemberIds = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.SdkAppId = params.get("SdkAppId")
        self.TeacherId = params.get("TeacherId")
        self.MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupWithMembersResponse(AbstractModel):
    """CreateGroupWithMembers response structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The ID of the successfully created group.
        :type GroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateGroupWithSubGroupRequest(AbstractModel):
    """CreateGroupWithSubGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupName: The group name after merging.
        :type GroupName: str
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param SubGroupIds: The IDs of the groups to merge. Duplicate group IDs are not allowed. Array length limit: 40.
        :type SubGroupIds: list of str
        :param TeacherId: The user ID of the teacher.
        :type TeacherId: str
        """
        self.GroupName = None
        self.SdkAppId = None
        self.SubGroupIds = None
        self.TeacherId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.SdkAppId = params.get("SdkAppId")
        self.SubGroupIds = params.get("SubGroupIds")
        self.TeacherId = params.get("TeacherId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupWithSubGroupResponse(AbstractModel):
    """CreateGroupWithSubGroup response structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The ID of the merged group.
        :type GroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
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
        :param SubType: The room subtype. Valid values: `videodoc`: Document + Video; `video`: Video only. 
        :type SubType: str
        :param TeacherId: The user ID of the teacher. User IDs are returned by the user registration APIs. The user specified will have teacher permissions in the room created.
        :type TeacherId: str
        :param AutoMic: Whether to automatically turn the mic on when the user enters a room. Valid values: `0`: No (default value); `1`: Yes.
        :type AutoMic: int
        :param AudioQuality: Whether to enable the high audio quality mode. Valid values: `0`: No (default value); `1`: Yes.
        :type AudioQuality: int
        :param DisableRecord: Whether to disable auto recording. Valid values: `0`: No (default); `1`: Yes. If this parameter is `0`, recording will start when the class starts and stops when the class ends.
        :type DisableRecord: int
        :param Assistants: The user IDs of the teaching assistants. User IDs are returned by the user registration APIs. The users specified will have teaching assistant permissions in the room created.
        :type Assistants: list of str
        :param RecordLayout: Recording layout
        :type RecordLayout: int
        :param GroupId: The ID of the group to bind. If you specify this parameter, only members of the group can enter this room.
        :type GroupId: str
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
        self.GroupId = None


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
        self.GroupId = params.get("GroupId")
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


class DeleteDocumentRequest(AbstractModel):
    """DeleteDocument request structure.

    """

    def __init__(self):
        r"""
        :param DocumentId: The document ID.
        :type DocumentId: str
        """
        self.DocumentId = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDocumentResponse(AbstractModel):
    """DeleteDocument response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteGroupMemberRequest(AbstractModel):
    """DeleteGroupMember request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The group ID. You cannot remove members from a merged group.
        :type GroupId: str
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param MemberIds: The users. Array length limit: 200.
        :type MemberIds: list of str
        """
        self.GroupId = None
        self.SdkAppId = None
        self.MemberIds = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.SdkAppId = params.get("SdkAppId")
        self.MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupMemberResponse(AbstractModel):
    """DeleteGroupMember response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupIds: The IDs of the groups to delete.
        :type GroupIds: list of str
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        """
        self.GroupIds = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRecordRequest(AbstractModel):
    """DeleteRecord request structure.

    """

    def __init__(self):
        r"""
        :param RoomId: The room ID.	
        :type RoomId: int
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        """
        self.RoomId = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordResponse(AbstractModel):
    """DeleteRecord response structure.

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


class DescribeCurrentMemberListRequest(AbstractModel):
    """DescribeCurrentMemberList request structure.

    """

    def __init__(self):
        r"""
        :param RoomId: The room ID.
        :type RoomId: int
        :param Page: The page to return records from. Pagination starts from 1.
        :type Page: int
        :param Limit: The maximum number of records per page. The value of this parameter cannot exceed `1000`.
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
        


class DescribeCurrentMemberListResponse(AbstractModel):
    """DescribeCurrentMemberList response structure.

    """

    def __init__(self):
        r"""
        :param Total: The total number of records.
        :type Total: int
        :param MemberRecords: The user list.
        :type MemberRecords: list of MemberRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.MemberRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("MemberRecords") is not None:
            self.MemberRecords = []
            for item in params.get("MemberRecords"):
                obj = MemberRecord()
                obj._deserialize(item)
                self.MemberRecords.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDocumentRequest(AbstractModel):
    """DescribeDocument request structure.

    """

    def __init__(self):
        r"""
        :param DocumentId: The (unique) document ID.
        :type DocumentId: str
        """
        self.DocumentId = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocumentResponse(AbstractModel):
    """DescribeDocument response structure.

    """

    def __init__(self):
        r"""
        :param DocumentId: The document ID.
        :type DocumentId: str
        :param DocumentUrl: The document’s original URL.
        :type DocumentUrl: str
        :param DocumentName: The document title.
        :type DocumentName: str
        :param Owner: The user ID of the document’s owner.
        :type Owner: str
        :param SdkAppId: The application ID.
        :type SdkAppId: int
        :param Permission: The document access type.
        :type Permission: int
        :param TranscodeResult: The transcoding result. If the file is not transcoded, this parameter will be empty. If it is successfully transcoded, this parameter will be the URL of the transcoded file. If transcoding fails, this parameter will indicate the error code.
        :type TranscodeResult: str
        :param TranscodeType: The transcoding type.
        :type TranscodeType: int
        :param TranscodeProgress: The transcoding progress. Value range: 0-100.
        :type TranscodeProgress: int
        :param TranscodeState: The transcoding status. `0`: The file is not transcoded. `1`: The file is being transcoded. `2`: Transcoding failed. `3`: Transcoding is successful.
        :type TranscodeState: int
        :param TranscodeInfo: The error message for failed transcoding.
        :type TranscodeInfo: str
        :param DocumentType: The document type.
        :type DocumentType: str
        :param DocumentSize: The document size (bytes).
        :type DocumentSize: int
        :param UpdateTime: The time (Unix timestamp) when the document was last updated.
        :type UpdateTime: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DocumentId = None
        self.DocumentUrl = None
        self.DocumentName = None
        self.Owner = None
        self.SdkAppId = None
        self.Permission = None
        self.TranscodeResult = None
        self.TranscodeType = None
        self.TranscodeProgress = None
        self.TranscodeState = None
        self.TranscodeInfo = None
        self.DocumentType = None
        self.DocumentSize = None
        self.UpdateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        self.DocumentUrl = params.get("DocumentUrl")
        self.DocumentName = params.get("DocumentName")
        self.Owner = params.get("Owner")
        self.SdkAppId = params.get("SdkAppId")
        self.Permission = params.get("Permission")
        self.TranscodeResult = params.get("TranscodeResult")
        self.TranscodeType = params.get("TranscodeType")
        self.TranscodeProgress = params.get("TranscodeProgress")
        self.TranscodeState = params.get("TranscodeState")
        self.TranscodeInfo = params.get("TranscodeInfo")
        self.DocumentType = params.get("DocumentType")
        self.DocumentSize = params.get("DocumentSize")
        self.UpdateTime = params.get("UpdateTime")
        self.RequestId = params.get("RequestId")


class DescribeDocumentsByRoomRequest(AbstractModel):
    """DescribeDocumentsByRoom request structure.

    """

    def __init__(self):
        r"""
        :param RoomId: The room ID.
        :type RoomId: int
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param Page: The page to return records from. Pagination starts from 1, which is also the default value of this parameter.
        :type Page: int
        :param Limit: The maximum number of records to return per page. The maximum value can be `1000`. The default value is `100`.
        :type Limit: int
        :param Permission: The document access type.
[0]: The private documents of the owner.
[1]: The public documents of the owner.
[0,1]: The private and public documents of the owner.
[2]: The private and public documents of all users (including the owner).
Default value: [2].
        :type Permission: list of int non-negative
        :param Owner: The user ID of the document owner. If you do not specify this, the information of all documents under the application will be returned.
        :type Owner: str
        """
        self.RoomId = None
        self.SdkAppId = None
        self.Page = None
        self.Limit = None
        self.Permission = None
        self.Owner = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.SdkAppId = params.get("SdkAppId")
        self.Page = params.get("Page")
        self.Limit = params.get("Limit")
        self.Permission = params.get("Permission")
        self.Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocumentsByRoomResponse(AbstractModel):
    """DescribeDocumentsByRoom response structure.

    """

    def __init__(self):
        r"""
        :param Documents: The information of the documents.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Documents: list of DocumentInfo
        :param Total: The total number of records that meet the conditions.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Documents = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Documents") is not None:
            self.Documents = []
            for item in params.get("Documents"):
                obj = DocumentInfo()
                obj._deserialize(item)
                self.Documents.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeGroupListRequest(AbstractModel):
    """DescribeGroupList request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param Page: The page to return records from. Pagination starts from 1.
        :type Page: int
        :param Limit: The maximum number of records per page. The value of this parameter cannot exceed `1000` and is `20` by default.
        :type Limit: int
        :param TeacherId: The user ID of the teacher, which is used as the filter. This parameter and `MemberId` are mutually exclusive. If both are specified, only this parameter will take effect.
        :type TeacherId: str
        :param MemberId: The user ID of a member, which is used as the filter. This parameter and `TeacherId` are mutually exclusive.
        :type MemberId: str
        """
        self.SdkAppId = None
        self.Page = None
        self.Limit = None
        self.TeacherId = None
        self.MemberId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Page = params.get("Page")
        self.Limit = params.get("Limit")
        self.TeacherId = params.get("TeacherId")
        self.MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupListResponse(AbstractModel):
    """DescribeGroupList response structure.

    """

    def __init__(self):
        r"""
        :param Total: The total number of groups that meet the conditions.
        :type Total: int
        :param GroupInfos: The information of the groups.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupInfos: list of GroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.GroupInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("GroupInfos") is not None:
            self.GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGroupMemberListRequest(AbstractModel):
    """DescribeGroupMemberList request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The group ID.
        :type GroupId: str
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param Page: The page to return records from. The default value is `1`.
        :type Page: int
        :param Limit: The maximum number of records per page. The value of this parameter cannot exceed `1000` and is `20` by default.
        :type Limit: int
        """
        self.GroupId = None
        self.SdkAppId = None
        self.Page = None
        self.Limit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.SdkAppId = params.get("SdkAppId")
        self.Page = params.get("Page")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupMemberListResponse(AbstractModel):
    """DescribeGroupMemberList response structure.

    """

    def __init__(self):
        r"""
        :param Total: The total number of records that meet the conditions.
        :type Total: int
        :param MemberIds: The user IDs of the members.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemberIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.MemberIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.MemberIds = params.get("MemberIds")
        self.RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The group ID.
        :type GroupId: str
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        """
        self.GroupId = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup response structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The group ID.
        :type GroupId: str
        :param GroupName: The group name.
        :type GroupName: str
        :param TeacherId: The user ID of the group’s teacher.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TeacherId: str
        :param GroupType: The group type.
`0`: Ordinary group.
`1`: Merged group. If the group queried is a merged group, the IDs of the sub-groups will be returned.
        :type GroupType: int
        :param SubGroupIds: The IDs of the sub-groups.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubGroupIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.GroupName = None
        self.TeacherId = None
        self.GroupType = None
        self.SubGroupIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.TeacherId = params.get("TeacherId")
        self.GroupType = params.get("GroupType")
        self.SubGroupIds = params.get("SubGroupIds")
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
        :param SubType: The room subtype. Valid values: `videodoc`: Document + Video; `video`: Video only.
        :type SubType: str
        :param DisableRecord: Whether to disable auto recording. Valid values: `0`: No (default); `1`: Yes. If this parameter is `0`, recording will start when the class starts and stops when the class ends.	
        :type DisableRecord: int
        :param Assistants: Assistant ID list	
Note: This field may return null, indicating that no valid values can be obtained.
        :type Assistants: list of str
        :param RecordUrl: Recording URL. This parameter exists only after a room is ended.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordUrl: str
        :param Status: The class status. `0`: The class has not started. `1`: The class has started. `2`: The class ended. `3`: The class expired.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param GroupId: 
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupId: str
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
        self.Status = None
        self.GroupId = None
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
        self.Status = params.get("Status")
        self.GroupId = params.get("GroupId")
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
        :param RealStartTime: The actual start time of the room, in Unix timestamp, accurate to seconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealStartTime: int
        :param RealEndTime: The actual end time of the room, in Unix timestamp, accurate to seconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealEndTime: int
        :param MessageCount: The total number of room messages.
        :type MessageCount: int
        :param MicCount: The total number of mics in the room.
        :type MicCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PeakMemberNumber = None
        self.MemberNumber = None
        self.Total = None
        self.MemberRecords = None
        self.RealStartTime = None
        self.RealEndTime = None
        self.MessageCount = None
        self.MicCount = None
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
        self.RealStartTime = params.get("RealStartTime")
        self.RealEndTime = params.get("RealEndTime")
        self.MessageCount = params.get("MessageCount")
        self.MicCount = params.get("MicCount")
        self.RequestId = params.get("RequestId")


class DescribeSdkAppIdUsersRequest(AbstractModel):
    """DescribeSdkAppIdUsers request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param Page: The page to return records from. The default value is `1`.
        :type Page: int
        :param Limit: The maximum number of records to return per page. The default value is `20`.
        :type Limit: int
        """
        self.SdkAppId = None
        self.Page = None
        self.Limit = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Page = params.get("Page")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSdkAppIdUsersResponse(AbstractModel):
    """DescribeSdkAppIdUsers response structure.

    """

    def __init__(self):
        r"""
        :param Total: The total number of users.
        :type Total: int
        :param Users: The information of the users.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Users: list of UserInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self.Users.append(obj)
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


class DocumentInfo(AbstractModel):
    """Document Information.

    """

    def __init__(self):
        r"""
        :param DocumentId: The document ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentId: str
        :param DocumentUrl: The document’s original URL.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentUrl: str
        :param DocumentName: The document title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentName: str
        :param Owner: The user ID of the document’s owner.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Owner: str
        :param SdkAppId: The application ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SdkAppId: int
        :param Permission: The document access type. `0`: Private; `1`: Public.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Permission: int
        :param TranscodeResult: The transcoding result. If the file is not transcoded, this parameter will be empty. If it is successfully transcoded, this parameter will be the URL of the transcoded file. If transcoding fails, this parameter will indicate the error code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeResult: str
        :param TranscodeType: The transcoding type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeType: int
        :param TranscodeProgress: The transcoding progress. Value range: 0-100.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeProgress: int
        :param TranscodeState: The transcoding status. `0`: The file is not transcoded. `1`: The file is being transcoded. `2`: Transcoding failed. `3`: Transcoding is successful.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeState: int
        :param TranscodeInfo: The error message for failed transcoding.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranscodeInfo: str
        :param DocumentType: The document type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentType: str
        :param DocumentSize: The document size (bytes).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DocumentSize: int
        :param UpdateTime: The time (Unix timestamp) when the document was last updated.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: int
        """
        self.DocumentId = None
        self.DocumentUrl = None
        self.DocumentName = None
        self.Owner = None
        self.SdkAppId = None
        self.Permission = None
        self.TranscodeResult = None
        self.TranscodeType = None
        self.TranscodeProgress = None
        self.TranscodeState = None
        self.TranscodeInfo = None
        self.DocumentType = None
        self.DocumentSize = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        self.DocumentUrl = params.get("DocumentUrl")
        self.DocumentName = params.get("DocumentName")
        self.Owner = params.get("Owner")
        self.SdkAppId = params.get("SdkAppId")
        self.Permission = params.get("Permission")
        self.TranscodeResult = params.get("TranscodeResult")
        self.TranscodeType = params.get("TranscodeType")
        self.TranscodeProgress = params.get("TranscodeProgress")
        self.TranscodeState = params.get("TranscodeState")
        self.TranscodeInfo = params.get("TranscodeInfo")
        self.DocumentType = params.get("DocumentType")
        self.DocumentSize = params.get("DocumentSize")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWatermarkRequest(AbstractModel):
    """GetWatermark request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The SDKAppID assigned by LCIC.	
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
        


class GetWatermarkResponse(AbstractModel):
    """GetWatermark response structure.

    """

    def __init__(self):
        r"""
        :param TeacherLogo: The watermark settings for the teacher’s video.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TeacherLogo: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        :param BoardLogo: The watermark settings for the whiteboard.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BoardLogo: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        :param BackgroundPicture: The background image.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackgroundPicture: :class:`tencentcloud.lcic.v20220817.models.BackgroundPictureConfig`
        :param Text: The watermark text.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Text: :class:`tencentcloud.lcic.v20220817.models.TextMarkConfig`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TeacherLogo = None
        self.BoardLogo = None
        self.BackgroundPicture = None
        self.Text = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TeacherLogo") is not None:
            self.TeacherLogo = WatermarkConfig()
            self.TeacherLogo._deserialize(params.get("TeacherLogo"))
        if params.get("BoardLogo") is not None:
            self.BoardLogo = WatermarkConfig()
            self.BoardLogo._deserialize(params.get("BoardLogo"))
        if params.get("BackgroundPicture") is not None:
            self.BackgroundPicture = BackgroundPictureConfig()
            self.BackgroundPicture._deserialize(params.get("BackgroundPicture"))
        if params.get("Text") is not None:
            self.Text = TextMarkConfig()
            self.Text._deserialize(params.get("Text"))
        self.RequestId = params.get("RequestId")


class GroupBaseInfo(AbstractModel):
    """The information of the groups to create.

    """

    def __init__(self):
        r"""
        :param GroupName: The group names.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupName: str
        :param TeacherId: The user ID of the teacher.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TeacherId: str
        """
        self.GroupName = None
        self.TeacherId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.TeacherId = params.get("TeacherId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """The information of the groups queried.

    """

    def __init__(self):
        r"""
        :param GroupId: Group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupId: str
        :param GroupName: The group name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupName: str
        :param TeacherId: The user ID of the teacher.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TeacherId: str
        :param GroupType: The group type. 
`0`: Ordinary group. 
`1`: Merged group. If the group queried is a merged group, the IDs of the sub-groups will be returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupType: int
        :param SubGroupIds: The IDs of the sub-groups.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubGroupIds: str
        """
        self.GroupId = None
        self.GroupName = None
        self.TeacherId = None
        self.GroupType = None
        self.SubGroupIds = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.TeacherId = params.get("TeacherId")
        self.GroupType = params.get("GroupType")
        self.SubGroupIds = params.get("SubGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param IPAddress: The user’s IP address.
        :type IPAddress: str
        :param Location: The user’s location.
        :type Location: str
        :param Device: The user’s device type. `0`: Unknown; `1`: Windows; `2`: macOS; `3`: Android; `4`: iOS; `5`: Web; `6`: Mobile webpage; `7`: Weixin Mini Program.
        :type Device: int
        :param PerMemberMicCount: The number of times each member mics.
        :type PerMemberMicCount: int
        :param PerMemberMessageCount: The number of messages sent by each member.
        :type PerMemberMessageCount: int
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
        self.IPAddress = None
        self.Location = None
        self.Device = None
        self.PerMemberMicCount = None
        self.PerMemberMessageCount = None


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
        self.IPAddress = params.get("IPAddress")
        self.Location = params.get("Location")
        self.Device = params.get("Device")
        self.PerMemberMicCount = params.get("PerMemberMicCount")
        self.PerMemberMessageCount = params.get("PerMemberMessageCount")
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
        :param CallbackKey: The callback key.
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.Callback = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
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


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The ID of the group to modify.
        :type GroupId: str
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param TeacherId: The user ID of the teacher.
        :type TeacherId: str
        :param GroupName: The new group name.
        :type GroupName: str
        """
        self.GroupId = None
        self.SdkAppId = None
        self.TeacherId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.SdkAppId = params.get("SdkAppId")
        self.TeacherId = params.get("TeacherId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupResponse(AbstractModel):
    """ModifyGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoomRequest(AbstractModel):
    """ModifyRoom request structure.

    """

    def __init__(self):
        r"""
        :param RoomId: The room ID.
        :type RoomId: int
        :param SdkAppId: The SDKAppID assigned by LCIC.
        :type SdkAppId: int
        :param StartTime: The room start time (Unix timestamp).
        :type StartTime: int
        :param EndTime: The room end time (Unix timestamp).
        :type EndTime: int
        :param TeacherId: The user ID of the teacher. User IDs are returned by the user registration APIs.
        :type TeacherId: str
        :param Name: The room name.
        :type Name: str
        :param Resolution: The resolution. Valid values: `1`: SD; `2`: HD; `3`: FHD.
        :type Resolution: int
        :param MaxMicNumber: The maximum number of mic-on users (excluding the teacher). Value range: 0-16.
        :type MaxMicNumber: int
        :param AutoMic: Whether to automatically turn the mic on when a user enters the room. Valid values: `0`: No (default value); `1`: Yes.
        :type AutoMic: int
        :param AudioQuality: Whether to enable the high audio quality mode. Valid values: `0`: No (default value); `1`: Yes.
        :type AudioQuality: int
        :param SubType: The room subtype. Valid values: `videodoc`: Document + Video; `video`: Video only; `coteaching`: Dual-teacher.
        :type SubType: str
        :param DisableRecord: Whether to disable auto recording. Valid values: `0`: No (default); `1`: Yes. If this parameter is `0`, recording will start when the class starts and stops when the class ends.
        :type DisableRecord: int
        :param Assistants: The user IDs of the teacher assistants. User IDs are returned by the user registration APIs.
        :type Assistants: list of str
        :param GroupId: The ID of the group to bind.
        :type GroupId: str
        """
        self.RoomId = None
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.TeacherId = None
        self.Name = None
        self.Resolution = None
        self.MaxMicNumber = None
        self.AutoMic = None
        self.AudioQuality = None
        self.SubType = None
        self.DisableRecord = None
        self.Assistants = None
        self.GroupId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TeacherId = params.get("TeacherId")
        self.Name = params.get("Name")
        self.Resolution = params.get("Resolution")
        self.MaxMicNumber = params.get("MaxMicNumber")
        self.AutoMic = params.get("AutoMic")
        self.AudioQuality = params.get("AudioQuality")
        self.SubType = params.get("SubType")
        self.DisableRecord = params.get("DisableRecord")
        self.Assistants = params.get("Assistants")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoomResponse(AbstractModel):
    """ModifyRoom response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserProfileRequest(AbstractModel):
    """ModifyUserProfile request structure.

    """

    def __init__(self):
        r"""
        :param UserId: The ID of the user whose profile will be modified.
        :type UserId: str
        :param Nickname: The new username to use.
        :type Nickname: str
        :param Avatar: The URL of the new profile photo.
        :type Avatar: str
        """
        self.UserId = None
        self.Nickname = None
        self.Avatar = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Nickname = params.get("Nickname")
        self.Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserProfileResponse(AbstractModel):
    """ModifyUserProfile response structure.

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


class RoomInfo(AbstractModel):
    """The information of the room to create.

    """

    def __init__(self):
        r"""
        :param Name: The room name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param StartTime: The room start time (Unix timestamp).
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: int
        :param EndTime: The room end time (Unix timestamp).
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: int
        :param Resolution: The resolution. Valid values: `1`: SD; `2`: HD; `3`: FHD.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Resolution: int
        :param MaxMicNumber: The maximum number of mic-on users (excluding the teacher). Value range: 0-16.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxMicNumber: int
        :param SubType: The room subtype. Valid values: `videodoc`: Document + Video; `video`: Video only; `coteaching`: Dual-teacher.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubType: str
        :param TeacherId: The user ID of the teacher. User IDs are returned by the user registration APIs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TeacherId: str
        :param AutoMic: Whether to automatically turn the mic on when a user enters the room. Valid values: `0`: No (default value); `1`: Yes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoMic: int
        :param TurnOffMic: Whether to disconnect communication after audio/video permissions are revoked. Valid values: `0`: Yes (default value); `1`: No.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TurnOffMic: int
        :param AudioQuality: Whether to enable the high audio quality mode. Valid values: `0`: No (default value); `1`: Yes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AudioQuality: int
        :param DisableRecord: Whether to disable auto recording. Valid values: `0`: No (default); `1`: Yes. If this parameter is `0`, recording will start when the class starts and stops when the class ends.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DisableRecord: int
        :param Assistants: The user IDs of the teacher assistants. User IDs are returned by the user registration APIs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Assistants: list of str
        :param RTCAudienceNumber: The number of RTC users.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RTCAudienceNumber: int
        :param AudienceType: The audience type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AudienceType: int
        :param RecordLayout: The recording layout.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordLayout: int
        :param GroupId: The ID of the group to bind.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupId: str
        """
        self.Name = None
        self.StartTime = None
        self.EndTime = None
        self.Resolution = None
        self.MaxMicNumber = None
        self.SubType = None
        self.TeacherId = None
        self.AutoMic = None
        self.TurnOffMic = None
        self.AudioQuality = None
        self.DisableRecord = None
        self.Assistants = None
        self.RTCAudienceNumber = None
        self.AudienceType = None
        self.RecordLayout = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Resolution = params.get("Resolution")
        self.MaxMicNumber = params.get("MaxMicNumber")
        self.SubType = params.get("SubType")
        self.TeacherId = params.get("TeacherId")
        self.AutoMic = params.get("AutoMic")
        self.TurnOffMic = params.get("TurnOffMic")
        self.AudioQuality = params.get("AudioQuality")
        self.DisableRecord = params.get("DisableRecord")
        self.Assistants = params.get("Assistants")
        self.RTCAudienceNumber = params.get("RTCAudienceNumber")
        self.AudienceType = params.get("AudienceType")
        self.RecordLayout = params.get("RecordLayout")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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


class SetWatermarkRequest(AbstractModel):
    """SetWatermark request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The SDKAppID assigned by LCIC.	
        :type SdkAppId: int
        :param TeacherUrl: The URL of the watermark for the teacher’s video. If you pass in an empty string, the teacher’s video will not have a watermark.
        :type TeacherUrl: str
        :param BoardUrl: The URL of the watermark for the whiteboard. If you pass in an empty string, the whiteboard video will not have a watermark.
        :type BoardUrl: str
        :param VideoUrl: The image displayed when there is no video. If you pass in an empty string, no images will be displayed.
        :type VideoUrl: str
        :param BoardW: The width of the whiteboard’s watermark, which is expressed as a percentage of the video width. The value range is 0-100, and the default value is `0`.
        :type BoardW: float
        :param BoardH: The height of the whiteboard’s watermark, which is expressed as a percentage of the video height. The value range is 0-100, and the default value is `0`.
        :type BoardH: float
        :param BoardX: The horizontal offset of the whiteboard’s watermark, which is expressed as a percentage of the video width. For example, `50` indicates that the watermark will appear in the middle horizontally. Value range: 0-100.
        :type BoardX: float
        :param BoardY: The vertical offset of the whiteboard’s watermark, which is expressed as a percentage of the video width. For example, `50` indicates that the watermark will appear in the middle vertically. Value range: 0-100.
        :type BoardY: float
        :param TeacherW: The width of the watermark for the teacher’s video, which is expressed as a percentage of the video width. The value range is 0-100, and the default value is `0`.
        :type TeacherW: float
        :param TeacherH: The height of the watermark for the teacher’s video, which is expressed as a percentage of the video height. The value range is 0-100, and the default value is `0`.
        :type TeacherH: float
        :param TeacherX: The horizontal offset of the watermark for the teacher’s video, which is expressed as a percentage of the video width. For example, `50` indicates that the watermark will appear in the middle horizontally. Value range: 0-100.
        :type TeacherX: float
        :param TeacherY: The vertical offset of the watermark for the teacher’s video, which is expressed as a percentage of the video width. For example, `50` indicates that the watermark will appear in the middle vertically. Value range: 0-100.
        :type TeacherY: float
        :param Text: The watermark text. If you pass in an empty string, there will be no text.
        :type Text: str
        :param TextColor: The watermark text color.
        :type TextColor: str
        """
        self.SdkAppId = None
        self.TeacherUrl = None
        self.BoardUrl = None
        self.VideoUrl = None
        self.BoardW = None
        self.BoardH = None
        self.BoardX = None
        self.BoardY = None
        self.TeacherW = None
        self.TeacherH = None
        self.TeacherX = None
        self.TeacherY = None
        self.Text = None
        self.TextColor = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TeacherUrl = params.get("TeacherUrl")
        self.BoardUrl = params.get("BoardUrl")
        self.VideoUrl = params.get("VideoUrl")
        self.BoardW = params.get("BoardW")
        self.BoardH = params.get("BoardH")
        self.BoardX = params.get("BoardX")
        self.BoardY = params.get("BoardY")
        self.TeacherW = params.get("TeacherW")
        self.TeacherH = params.get("TeacherH")
        self.TeacherX = params.get("TeacherX")
        self.TeacherY = params.get("TeacherY")
        self.Text = params.get("Text")
        self.TextColor = params.get("TextColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWatermarkResponse(AbstractModel):
    """SetWatermark response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TextMarkConfig(AbstractModel):
    """The watermark text.

    """

    def __init__(self):
        r"""
        :param Text: The watermark text.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Text: str
        :param Color: The watermark text color.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Color: str
        """
        self.Text = None
        self.Color = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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


class UserInfo(AbstractModel):
    """The user information.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The application ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SdkAppId: int
        :param UserId: The user ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserId: str
        :param Name: The username.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param Avatar: The URL of profile photo.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Avatar: str
        """
        self.SdkAppId = None
        self.UserId = None
        self.Name = None
        self.Avatar = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.UserId = params.get("UserId")
        self.Name = params.get("Name")
        self.Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkConfig(AbstractModel):
    """Watermark settings.

    """

    def __init__(self):
        r"""
        :param Url: The URL of the watermark image.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param Width: The watermark width, which is expressed as a percentage of the video width.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Width: float
        :param Height: The watermark height, which is expressed as a percentage of the video height.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Height: float
        :param LocationX: The horizontal offset of the watermark, which is expressed as a percentage of the video width. For example, `50` indicates that the watermark will appear in the middle horizontally. Value range: 0-100.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type LocationX: float
        :param LocationY: The vertical offset of the watermark, which is expressed as a percentage of the video width. For example, `50` indicates that the watermark will appear in the middle vertically. Value range: 0-100.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type LocationY: float
        """
        self.Url = None
        self.Width = None
        self.Height = None
        self.LocationX = None
        self.LocationY = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        