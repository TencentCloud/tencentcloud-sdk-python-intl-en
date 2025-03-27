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
from tencentcloud.ciam.v20220331 import models


class CiamClient(AbstractClient):
    _apiVersion = '2022-03-31'
    _endpoint = 'ciam.intl.tencentcloudapi.com'
    _service = 'ciam'


    def CreateApiImportUserJob(self, request):
        """This API is used to create an API for user import task.

        :param request: Request instance for CreateApiImportUserJob.
        :type request: :class:`tencentcloud.ciam.v20220331.models.CreateApiImportUserJobRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.CreateApiImportUserJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiImportUserJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiImportUserJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFileExportUserJob(self, request):
        """This API is used to create a file for user export task.

        :param request: Request instance for CreateFileExportUserJob.
        :type request: :class:`tencentcloud.ciam.v20220331.models.CreateFileExportUserJobRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.CreateFileExportUserJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileExportUserJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileExportUserJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        """This API is used to create a user.

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.ciam.v20220331.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUsers(self, request):
        """This API is used to delete users in batches.

        :param request: Request instance for DeleteUsers.
        :type request: :class:`tencentcloud.ciam.v20220331.models.DeleteUsersRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.DeleteUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUser(self, request):
        """This API is used to query the user information with multiple conditions.

        :param request: Request instance for DescribeUser.
        :type request: :class:`tencentcloud.ciam.v20220331.models.DescribeUserRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.DescribeUserResponse`

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


    def DescribeUserById(self, request):
        """This API is used to query a user by ID.

        :param request: Request instance for DescribeUserById.
        :type request: :class:`tencentcloud.ciam.v20220331.models.DescribeUserByIdRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.DescribeUserByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LinkAccount(self, request):
        """This API is used to merge accounts.

        :param request: Request instance for LinkAccount.
        :type request: :class:`tencentcloud.ciam.v20220331.models.LinkAccountRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.LinkAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LinkAccount", params, headers=headers)
            response = json.loads(body)
            model = models.LinkAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListJobs(self, request):
        """This API is used to query the details of a task.

        :param request: Request instance for ListJobs.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ListJobsRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ListJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListJobs", params, headers=headers)
            response = json.loads(body)
            model = models.ListJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListLogMessageByCondition(self, request):
        """This API is used to query a specified log.

        :param request: Request instance for ListLogMessageByCondition.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ListLogMessageByConditionRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ListLogMessageByConditionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLogMessageByCondition", params, headers=headers)
            response = json.loads(body)
            model = models.ListLogMessageByConditionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUser(self, request):
        """This API is used to query the list of users.

        :param request: Request instance for ListUser.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ListUserRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ListUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUser", params, headers=headers)
            response = json.loads(body)
            model = models.ListUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUserByProperty(self, request):
        """This API is used to query the list of users by attribute.

        :param request: Request instance for ListUserByProperty.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ListUserByPropertyRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ListUserByPropertyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUserByProperty", params, headers=headers)
            response = json.loads(body)
            model = models.ListUserByPropertyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetPassword(self, request):
        """This API is used to reset the password for a user.

        :param request: Request instance for ResetPassword.
        :type request: :class:`tencentcloud.ciam.v20220331.models.ResetPasswordRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.ResetPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetPassword(self, request):
        """This API is used to set the password for a user.

        :param request: Request instance for SetPassword.
        :type request: :class:`tencentcloud.ciam.v20220331.models.SetPasswordRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.SetPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetPassword", params, headers=headers)
            response = json.loads(body)
            model = models.SetPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUser(self, request):
        """This API is used to update a user.

        :param request: Request instance for UpdateUser.
        :type request: :class:`tencentcloud.ciam.v20220331.models.UpdateUserRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.UpdateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUser", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUserStatus(self, request):
        """This API is used to update the status of a user.

        :param request: Request instance for UpdateUserStatus.
        :type request: :class:`tencentcloud.ciam.v20220331.models.UpdateUserStatusRequest`
        :rtype: :class:`tencentcloud.ciam.v20220331.models.UpdateUserStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))