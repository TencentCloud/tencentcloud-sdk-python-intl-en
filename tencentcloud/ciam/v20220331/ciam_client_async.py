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
from tencentcloud.ciam.v20220331 import models
from typing import Dict


class CiamClient(AbstractClient):
    _apiVersion = '2022-03-31'
    _endpoint = 'ciam.intl.tencentcloudapi.com'
    _service = 'ciam'

    async def CreateApiImportUserJob(
            self,
            request: models.CreateApiImportUserJobRequest,
            opts: Dict = None,
    ) -> models.CreateApiImportUserJobResponse:
        """
        This API is used to create an API for user import task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiImportUserJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiImportUserJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileExportUserJob(
            self,
            request: models.CreateFileExportUserJobRequest,
            opts: Dict = None,
    ) -> models.CreateFileExportUserJobResponse:
        """
        This API is used to create a file for user export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileExportUserJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileExportUserJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        This API is used to create a user.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsers(
            self,
            request: models.DeleteUsersRequest,
            opts: Dict = None,
    ) -> models.DeleteUsersResponse:
        """
        This API is used to delete users in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUser(
            self,
            request: models.DescribeUserRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResponse:
        """
        This API is used to query the user information with multiple conditions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserById(
            self,
            request: models.DescribeUserByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeUserByIdResponse:
        """
        This API is used to query a user by ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LinkAccount(
            self,
            request: models.LinkAccountRequest,
            opts: Dict = None,
    ) -> models.LinkAccountResponse:
        """
        This API is used to merge accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "LinkAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LinkAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListJobs(
            self,
            request: models.ListJobsRequest,
            opts: Dict = None,
    ) -> models.ListJobsResponse:
        """
        This API is used to query the details of a task.
        """
        
        kwargs = {}
        kwargs["action"] = "ListJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListLogMessageByCondition(
            self,
            request: models.ListLogMessageByConditionRequest,
            opts: Dict = None,
    ) -> models.ListLogMessageByConditionResponse:
        """
        This API is used to query a specified log.
        """
        
        kwargs = {}
        kwargs["action"] = "ListLogMessageByCondition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLogMessageByConditionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUser(
            self,
            request: models.ListUserRequest,
            opts: Dict = None,
    ) -> models.ListUserResponse:
        """
        This API is used to query the list of users.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUserByProperty(
            self,
            request: models.ListUserByPropertyRequest,
            opts: Dict = None,
    ) -> models.ListUserByPropertyResponse:
        """
        This API is used to query the list of users by attribute.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUserByProperty"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserByPropertyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetPassword(
            self,
            request: models.ResetPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetPasswordResponse:
        """
        This API is used to reset the password for a user.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetPassword(
            self,
            request: models.SetPasswordRequest,
            opts: Dict = None,
    ) -> models.SetPasswordResponse:
        """
        This API is used to set the password for a user.
        """
        
        kwargs = {}
        kwargs["action"] = "SetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUser(
            self,
            request: models.UpdateUserRequest,
            opts: Dict = None,
    ) -> models.UpdateUserResponse:
        """
        This API is used to update a user.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserStatus(
            self,
            request: models.UpdateUserStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateUserStatusResponse:
        """
        This API is used to update the status of a user.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)