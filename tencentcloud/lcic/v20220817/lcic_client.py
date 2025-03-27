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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.lcic.v20220817 import models


class LcicClient(AbstractClient):
    _apiVersion = '2022-08-17'
    _endpoint = 'lcic.intl.tencentcloudapi.com'
    _service = 'lcic'


    def AddGroupMember(self, request):
        """This API is used to add users to a group.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for AddGroupMember.
        :type request: :class:`tencentcloud.lcic.v20220817.models.AddGroupMemberRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.AddGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.AddGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchAddGroupMember(self, request):
        """This API is used to add users to multiple groups at a time.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for BatchAddGroupMember.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchAddGroupMemberRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchAddGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchAddGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.BatchAddGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchCreateGroupWithMembers(self, request):
        """This API is used to create multiple groups at a time.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for BatchCreateGroupWithMembers.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchCreateGroupWithMembersRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchCreateGroupWithMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateGroupWithMembers", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateGroupWithMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchCreateRoom(self, request):
        """This API is used to create multiple rooms at a time.

        :param request: Request instance for BatchCreateRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchCreateRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchCreateRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateRoom", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteGroupMember(self, request):
        """This API is used to remove users from multiple groups at a time.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for BatchDeleteGroupMember.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchDeleteGroupMemberRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchDeleteGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteRecord(self, request):
        """This API is used to delete the recordings of multiple rooms.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for BatchDeleteRecord.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchDeleteRecordRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchDeleteRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteRecord", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDescribeDocument(self, request):
        """This API is used to get courseware information.

        :param request: Request instance for BatchDescribeDocument.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchDescribeDocumentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchDescribeDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDescribeDocument", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDescribeDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchRegister(self, request):
        """This API is used to register multiple users (up to 1,000) at a time. If a user ID already exists, the existing one will be overwritten.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for BatchRegister.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchRegisterRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchRegisterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRegister", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRegisterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindDocumentToRoom(self, request):
        """This API is used to bind a document to a room.

        :param request: Request instance for BindDocumentToRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BindDocumentToRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BindDocumentToRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindDocumentToRoom", params, headers=headers)
            response = json.loads(body)
            model = models.BindDocumentToRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDocument(self, request):
        """This API is used to create a document to be used in a room.

        :param request: Request instance for CreateDocument.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateDocumentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDocument", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGroupWithMembers(self, request):
        """his API is used to create a group and specify its members.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for CreateGroupWithMembers.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateGroupWithMembersRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateGroupWithMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroupWithMembers", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGroupWithMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGroupWithSubGroup(self, request):
        """This API is used to merge groups.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for CreateGroupWithSubGroup.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateGroupWithSubGroupRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateGroupWithSubGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroupWithSubGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGroupWithSubGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoom(self, request):
        """This API is used to create a room.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for CreateRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoom", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSupervisor(self, request):
        """This API is used to create a spectator.

        :param request: Request instance for CreateSupervisor.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateSupervisorRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateSupervisorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSupervisor", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSupervisorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAppCustomContent(self, request):
        """This API is used to delete the custom elements. The `Scenes` parameter specifies the custom elements to delete. If `Scenes` is empty, all custom elements will be deleted.

        :param request: Request instance for DeleteAppCustomContent.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteAppCustomContentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteAppCustomContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAppCustomContent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppCustomContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDocument(self, request):
        """This API is used to delete a document.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DeleteDocument.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteDocumentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDocument", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGroup(self, request):
        """This API is used to delete one or multiple groups.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGroupMember(self, request):
        """This API is used to remove users from a group.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DeleteGroupMember.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteGroupMemberRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecord(self, request):
        """This example shows you how to delete the recording files of a specific room.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DeleteRecord.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteRecordRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoom(self, request):
        """This API is used to delete a room.

        :param request: Request instance for DeleteRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoom", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSupervisor(self, request):
        """This API is used to delete spectators.

        :param request: Request instance for DeleteSupervisor.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteSupervisorRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteSupervisorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSupervisor", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSupervisorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAnswerList(self, request):
        """This API is used to get the answers to a quiz question in a room.

        :param request: Request instance for DescribeAnswerList.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeAnswerListRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeAnswerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAnswerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAnswerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCurrentMemberList(self, request):
        """This API is used to get the user list of a room. This API will not work if a room has ended or expired.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DescribeCurrentMemberList.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeCurrentMemberListRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeCurrentMemberListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCurrentMemberList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCurrentMemberListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeveloper(self, request):
        """This API is used to get developer information.

        :param request: Request instance for DescribeDeveloper.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeDeveloperRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeDeveloperResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeveloper", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeveloperResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDocument(self, request):
        """This API is used to get the information of a specific document.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DescribeDocument.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDocument", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDocuments(self, request):
        """A new API is offered for this action now.

        This API is used to query courseware. It has been deprecated. Please use `BatchDescribeDocument` instead.

        :param request: Request instance for DescribeDocuments.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentsRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDocuments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDocumentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDocumentsByRoom(self, request):
        """This API is used to get the document list of a specific room.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DescribeDocumentsByRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentsByRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentsByRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDocumentsByRoom", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDocumentsByRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroup(self, request):
        """This API is used to get the details of a group.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DescribeGroup.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupList(self, request):
        """This API is used to query groups.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DescribeGroupList.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupListRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupMemberList(self, request):
        """This API is used to get the members of a group.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DescribeGroupMemberList.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupMemberListRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupMemberListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupMemberList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupMemberListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuestionList(self, request):
        """This API is used to get the quiz details of a room.

        :param request: Request instance for DescribeQuestionList.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeQuestionListRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeQuestionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuestionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuestionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoom(self, request):
        """This API is used to get room information.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DescribeRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoom", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoomStatistics(self, request):
        """This API is used to obtain the statistics of a room. It can be called only after the room is ended.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DescribeRoomStatistics.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomStatisticsRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoomStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoomStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSdkAppIdUsers(self, request):
        """This API is used to get the user list of a specific application.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for DescribeSdkAppIdUsers.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeSdkAppIdUsersRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeSdkAppIdUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSdkAppIdUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSdkAppIdUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSupervisors(self, request):
        """This API is used to get the spectators of a room.

        :param request: Request instance for DescribeSupervisors.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeSupervisorsRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeSupervisorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSupervisors", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSupervisorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUser(self, request):
        """This API is used to obtain user profile.

        :param request: Request instance for DescribeUser.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeUserRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EndRoom(self, request):
        """This API is used to end a room.

        :param request: Request instance for EndRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.EndRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.EndRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EndRoom", params, headers=headers)
            response = json.loads(body)
            model = models.EndRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRoomEvent(self, request):
        """This API is used to get the events of a room. It only works within one hour after a class ends.

        :param request: Request instance for GetRoomEvent.
        :type request: :class:`tencentcloud.lcic.v20220817.models.GetRoomEventRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.GetRoomEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRoomEvent", params, headers=headers)
            response = json.loads(body)
            model = models.GetRoomEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRoomMessage(self, request):
        """This API is used to get the message history of a room (room messages are retained for seven days).

        :param request: Request instance for GetRoomMessage.
        :type request: :class:`tencentcloud.lcic.v20220817.models.GetRoomMessageRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.GetRoomMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRoomMessage", params, headers=headers)
            response = json.loads(body)
            model = models.GetRoomMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRooms(self, request):
        """This API is used to get the room list.

        :param request: Request instance for GetRooms.
        :type request: :class:`tencentcloud.lcic.v20220817.models.GetRoomsRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.GetRoomsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRooms", params, headers=headers)
            response = json.loads(body)
            model = models.GetRoomsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWatermark(self, request):
        """This API is used to get watermark settings.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for GetWatermark.
        :type request: :class:`tencentcloud.lcic.v20220817.models.GetWatermarkRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.GetWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.GetWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KickUserFromRoom(self, request):
        """This API is used to remove a user from the room.

        :param request: Request instance for KickUserFromRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.KickUserFromRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.KickUserFromRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KickUserFromRoom", params, headers=headers)
            response = json.loads(body)
            model = models.KickUserFromRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LoginOriginId(self, request):
        """This API is used to log in with an origin account, which is the `originId` entered during registration.

        :param request: Request instance for LoginOriginId.
        :type request: :class:`tencentcloud.lcic.v20220817.models.LoginOriginIdRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.LoginOriginIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LoginOriginId", params, headers=headers)
            response = json.loads(body)
            model = models.LoginOriginIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LoginUser(self, request):
        """This API is used to log in.

        :param request: Request instance for LoginUser.
        :type request: :class:`tencentcloud.lcic.v20220817.models.LoginUserRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.LoginUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LoginUser", params, headers=headers)
            response = json.loads(body)
            model = models.LoginUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApp(self, request):
        """This API is used to modify an application.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for ModifyApp.
        :type request: :class:`tencentcloud.lcic.v20220817.models.ModifyAppRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.ModifyAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGroup(self, request):
        """This API is used to modify a group.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for ModifyGroup.
        :type request: :class:`tencentcloud.lcic.v20220817.models.ModifyGroupRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.ModifyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRoom(self, request):
        """This API is used to modify a room.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for ModifyRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.ModifyRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.ModifyRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoom", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserProfile(self, request):
        """This API is used to modify a user profile such as the nickname and profile photo.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for ModifyUserProfile.
        :type request: :class:`tencentcloud.lcic.v20220817.models.ModifyUserProfileRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.ModifyUserProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserProfile", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterUser(self, request):
        """This API is used to register a user.

        :param request: Request instance for RegisterUser.
        :type request: :class:`tencentcloud.lcic.v20220817.models.RegisterUserRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.RegisterUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterUser", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetAppCustomContent(self, request):
        """This API is used to set or update the custom content of an application, including the application icon and custom code. After you update JS and CSS content, you also need to call this API for the updates to take effect.

        :param request: Request instance for SetAppCustomContent.
        :type request: :class:`tencentcloud.lcic.v20220817.models.SetAppCustomContentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.SetAppCustomContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAppCustomContent", params, headers=headers)
            response = json.loads(body)
            model = models.SetAppCustomContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetWatermark(self, request):
        """This API is used to configure watermarks.
        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for SetWatermark.
        :type request: :class:`tencentcloud.lcic.v20220817.models.SetWatermarkRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.SetWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.SetWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartRoom(self, request):
        """This API is used to start a room. Before you call this API, make sure a user has entered the room so that the class is initialized.

        :param request: Request instance for StartRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.StartRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.StartRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartRoom", params, headers=headers)
            response = json.loads(body)
            model = models.StartRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindDocumentFromRoom(self, request):
        """This API is used to unbind a document from a room.

        :param request: Request instance for UnbindDocumentFromRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.UnbindDocumentFromRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.UnbindDocumentFromRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindDocumentFromRoom", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindDocumentFromRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))