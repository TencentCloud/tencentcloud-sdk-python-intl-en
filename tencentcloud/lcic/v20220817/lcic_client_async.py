# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.lcic.v20220817 import models
from typing import Dict


class LcicClient(AbstractClient):
    _apiVersion = '2022-08-17'
    _endpoint = 'lcic.intl.tencentcloudapi.com'
    _service = 'lcic'

    async def AddGroupMember(
            self,
            request: models.AddGroupMemberRequest,
            opts: Dict = None,
    ) -> models.AddGroupMemberResponse:
        """
        This API is used to add users to a group.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "AddGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchAddGroupMember(
            self,
            request: models.BatchAddGroupMemberRequest,
            opts: Dict = None,
    ) -> models.BatchAddGroupMemberResponse:
        """
        This API is used to add users to multiple groups at a time.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchAddGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchAddGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateGroupWithMembers(
            self,
            request: models.BatchCreateGroupWithMembersRequest,
            opts: Dict = None,
    ) -> models.BatchCreateGroupWithMembersResponse:
        """
        This API is used to create multiple groups at a time.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateGroupWithMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateGroupWithMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateRoom(
            self,
            request: models.BatchCreateRoomRequest,
            opts: Dict = None,
    ) -> models.BatchCreateRoomResponse:
        """
        This API is used to create multiple rooms at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteGroupMember(
            self,
            request: models.BatchDeleteGroupMemberRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteGroupMemberResponse:
        """
        This API is used to remove users from multiple groups at a time.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteRecord(
            self,
            request: models.BatchDeleteRecordRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteRecordResponse:
        """
        This API is used to delete the recordings of multiple rooms.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDescribeDocument(
            self,
            request: models.BatchDescribeDocumentRequest,
            opts: Dict = None,
    ) -> models.BatchDescribeDocumentResponse:
        """
        This API is used to get courseware information.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDescribeDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDescribeDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchRegister(
            self,
            request: models.BatchRegisterRequest,
            opts: Dict = None,
    ) -> models.BatchRegisterResponse:
        """
        This API is used to register multiple users (up to 1,000) at a time. If a user ID already exists, the existing one will be overwritten.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchRegister"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchRegisterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindDocumentToRoom(
            self,
            request: models.BindDocumentToRoomRequest,
            opts: Dict = None,
    ) -> models.BindDocumentToRoomResponse:
        """
        This API is used to bind a document to a room.
        """
        
        kwargs = {}
        kwargs["action"] = "BindDocumentToRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindDocumentToRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDocument(
            self,
            request: models.CreateDocumentRequest,
            opts: Dict = None,
    ) -> models.CreateDocumentResponse:
        """
        This API is used to create a document to be used in a room.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroupWithMembers(
            self,
            request: models.CreateGroupWithMembersRequest,
            opts: Dict = None,
    ) -> models.CreateGroupWithMembersResponse:
        """
        his API is used to create a group and specify its members.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroupWithMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupWithMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroupWithSubGroup(
            self,
            request: models.CreateGroupWithSubGroupRequest,
            opts: Dict = None,
    ) -> models.CreateGroupWithSubGroupResponse:
        """
        This API is used to merge groups.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroupWithSubGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupWithSubGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoom(
            self,
            request: models.CreateRoomRequest,
            opts: Dict = None,
    ) -> models.CreateRoomResponse:
        """
        This API is used to create a room.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSupervisor(
            self,
            request: models.CreateSupervisorRequest,
            opts: Dict = None,
    ) -> models.CreateSupervisorResponse:
        """
        This API is used to create a spectator.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSupervisor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSupervisorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAppCustomContent(
            self,
            request: models.DeleteAppCustomContentRequest,
            opts: Dict = None,
    ) -> models.DeleteAppCustomContentResponse:
        """
        This API is used to delete the custom elements. The `Scenes` parameter specifies the custom elements to delete. If `Scenes` is empty, all custom elements will be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAppCustomContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppCustomContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDocument(
            self,
            request: models.DeleteDocumentRequest,
            opts: Dict = None,
    ) -> models.DeleteDocumentResponse:
        """
        This API is used to delete a document.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        This API is used to delete one or multiple groups.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroupMember(
            self,
            request: models.DeleteGroupMemberRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupMemberResponse:
        """
        This API is used to remove users from a group.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecord(
            self,
            request: models.DeleteRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordResponse:
        """
        This example shows you how to delete the recording files of a specific room.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoom(
            self,
            request: models.DeleteRoomRequest,
            opts: Dict = None,
    ) -> models.DeleteRoomResponse:
        """
        This API is used to delete a room.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSupervisor(
            self,
            request: models.DeleteSupervisorRequest,
            opts: Dict = None,
    ) -> models.DeleteSupervisorResponse:
        """
        This API is used to delete spectators.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSupervisor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSupervisorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAnswerList(
            self,
            request: models.DescribeAnswerListRequest,
            opts: Dict = None,
    ) -> models.DescribeAnswerListResponse:
        """
        This API is used to get the answers to a quiz question in a room.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAnswerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAnswerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCurrentMemberList(
            self,
            request: models.DescribeCurrentMemberListRequest,
            opts: Dict = None,
    ) -> models.DescribeCurrentMemberListResponse:
        """
        This API is used to get the user list of a room. This API will not work if a room has ended or expired.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCurrentMemberList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCurrentMemberListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeveloper(
            self,
            request: models.DescribeDeveloperRequest,
            opts: Dict = None,
    ) -> models.DescribeDeveloperResponse:
        """
        This API is used to get developer information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeveloper"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeveloperResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDocument(
            self,
            request: models.DescribeDocumentRequest,
            opts: Dict = None,
    ) -> models.DescribeDocumentResponse:
        """
        This API is used to get the information of a specific document.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDocuments(
            self,
            request: models.DescribeDocumentsRequest,
            opts: Dict = None,
    ) -> models.DescribeDocumentsResponse:
        """
        A new API is offered for this action now.

        This API is used to query courseware. It has been deprecated. Please use `BatchDescribeDocument` instead.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDocuments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDocumentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDocumentsByRoom(
            self,
            request: models.DescribeDocumentsByRoomRequest,
            opts: Dict = None,
    ) -> models.DescribeDocumentsByRoomResponse:
        """
        This API is used to get the document list of a specific room.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDocumentsByRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDocumentsByRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroup(
            self,
            request: models.DescribeGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupResponse:
        """
        This API is used to get the details of a group.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupList(
            self,
            request: models.DescribeGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupListResponse:
        """
        This API is used to query groups.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupMemberList(
            self,
            request: models.DescribeGroupMemberListRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupMemberListResponse:
        """
        This API is used to get the members of a group.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupMemberList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupMemberListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuestionList(
            self,
            request: models.DescribeQuestionListRequest,
            opts: Dict = None,
    ) -> models.DescribeQuestionListResponse:
        """
        This API is used to get the quiz details of a room.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuestionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuestionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoom(
            self,
            request: models.DescribeRoomRequest,
            opts: Dict = None,
    ) -> models.DescribeRoomResponse:
        """
        This API is used to get room information.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoomStatistics(
            self,
            request: models.DescribeRoomStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeRoomStatisticsResponse:
        """
        This API is used to obtain the statistics of a room. It can be called only after the room is ended.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoomStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoomStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSdkAppIdUsers(
            self,
            request: models.DescribeSdkAppIdUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeSdkAppIdUsersResponse:
        """
        This API is used to get the user list of a specific application.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSdkAppIdUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSdkAppIdUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupervisors(
            self,
            request: models.DescribeSupervisorsRequest,
            opts: Dict = None,
    ) -> models.DescribeSupervisorsResponse:
        """
        This API is used to get the spectators of a room.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupervisors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupervisorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUser(
            self,
            request: models.DescribeUserRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResponse:
        """
        This API is used to obtain user profile.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EndRoom(
            self,
            request: models.EndRoomRequest,
            opts: Dict = None,
    ) -> models.EndRoomResponse:
        """
        This API is used to end a room.
        """
        
        kwargs = {}
        kwargs["action"] = "EndRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EndRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRoomEvent(
            self,
            request: models.GetRoomEventRequest,
            opts: Dict = None,
    ) -> models.GetRoomEventResponse:
        """
        This API is used to get the events of a room. It only works within one hour after a class ends.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRoomEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRoomEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRoomMessage(
            self,
            request: models.GetRoomMessageRequest,
            opts: Dict = None,
    ) -> models.GetRoomMessageResponse:
        """
        This API is used to get the message history of a room (room messages are retained for seven days).
        """
        
        kwargs = {}
        kwargs["action"] = "GetRoomMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRoomMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRooms(
            self,
            request: models.GetRoomsRequest,
            opts: Dict = None,
    ) -> models.GetRoomsResponse:
        """
        This API is used to get the room list.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRooms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRoomsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWatermark(
            self,
            request: models.GetWatermarkRequest,
            opts: Dict = None,
    ) -> models.GetWatermarkResponse:
        """
        This API is used to get watermark settings.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "GetWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KickUserFromRoom(
            self,
            request: models.KickUserFromRoomRequest,
            opts: Dict = None,
    ) -> models.KickUserFromRoomResponse:
        """
        This API is used to remove a user from the room.
        """
        
        kwargs = {}
        kwargs["action"] = "KickUserFromRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KickUserFromRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LoginOriginId(
            self,
            request: models.LoginOriginIdRequest,
            opts: Dict = None,
    ) -> models.LoginOriginIdResponse:
        """
        This API is used to log in with an origin account, which is the `originId` entered during registration.
        """
        
        kwargs = {}
        kwargs["action"] = "LoginOriginId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LoginOriginIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LoginUser(
            self,
            request: models.LoginUserRequest,
            opts: Dict = None,
    ) -> models.LoginUserResponse:
        """
        This API is used to log in.
        """
        
        kwargs = {}
        kwargs["action"] = "LoginUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LoginUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApp(
            self,
            request: models.ModifyAppRequest,
            opts: Dict = None,
    ) -> models.ModifyAppResponse:
        """
        This API is used to modify an application.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGroup(
            self,
            request: models.ModifyGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyGroupResponse:
        """
        This API is used to modify a group.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoom(
            self,
            request: models.ModifyRoomRequest,
            opts: Dict = None,
    ) -> models.ModifyRoomResponse:
        """
        This API is used to modify a room.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserProfile(
            self,
            request: models.ModifyUserProfileRequest,
            opts: Dict = None,
    ) -> models.ModifyUserProfileResponse:
        """
        This API is used to modify a user profile such as the nickname and profile photo.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterUser(
            self,
            request: models.RegisterUserRequest,
            opts: Dict = None,
    ) -> models.RegisterUserResponse:
        """
        This API is used to register a user.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAppCustomContent(
            self,
            request: models.SetAppCustomContentRequest,
            opts: Dict = None,
    ) -> models.SetAppCustomContentResponse:
        """
        This API is used to set or update the custom content of an application, including the application icon and custom code. After you update JS and CSS content, you also need to call this API for the updates to take effect.
        """
        
        kwargs = {}
        kwargs["action"] = "SetAppCustomContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAppCustomContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetWatermark(
            self,
            request: models.SetWatermarkRequest,
            opts: Dict = None,
    ) -> models.SetWatermarkResponse:
        """
        This API is used to configure watermarks.
        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "SetWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartRoom(
            self,
            request: models.StartRoomRequest,
            opts: Dict = None,
    ) -> models.StartRoomResponse:
        """
        This API is used to start a room. Before you call this API, make sure a user has entered the room so that the class is initialized.
        """
        
        kwargs = {}
        kwargs["action"] = "StartRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindDocumentFromRoom(
            self,
            request: models.UnbindDocumentFromRoomRequest,
            opts: Dict = None,
    ) -> models.UnbindDocumentFromRoomResponse:
        """
        This API is used to unbind a document from a room.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindDocumentFromRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindDocumentFromRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)