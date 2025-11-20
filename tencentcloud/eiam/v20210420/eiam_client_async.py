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
from tencentcloud.eiam.v20210420 import models
from typing import Dict


class EiamClient(AbstractClient):
    _apiVersion = '2021-04-20'
    _endpoint = 'eiam.intl.tencentcloudapi.com'
    _service = 'eiam'

    async def AddAccountToAccountGroup(
            self,
            request: models.AddAccountToAccountGroupRequest,
            opts: Dict = None,
    ) -> models.AddAccountToAccountGroupResponse:
        """
        This API is used to add an account to an account group.
        """
        
        kwargs = {}
        kwargs["action"] = "AddAccountToAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAccountToAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUserToUserGroup(
            self,
            request: models.AddUserToUserGroupRequest,
            opts: Dict = None,
    ) -> models.AddUserToUserGroupResponse:
        """
        This API is used to add a user to a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserToUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserToUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccountGroup(
            self,
            request: models.CreateAccountGroupRequest,
            opts: Dict = None,
    ) -> models.CreateAccountGroupResponse:
        """
        This API is used to create an account group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAppAccount(
            self,
            request: models.CreateAppAccountRequest,
            opts: Dict = None,
    ) -> models.CreateAppAccountResponse:
        """
        This API is used to create an application account.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAppAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrgNode(
            self,
            request: models.CreateOrgNodeRequest,
            opts: Dict = None,
    ) -> models.CreateOrgNodeResponse:
        """
        This API is used to create an organization node.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrgNodeResponse
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
        
    async def CreateUserGroup(
            self,
            request: models.CreateUserGroupRequest,
            opts: Dict = None,
    ) -> models.CreateUserGroupResponse:
        """
        This API is used to create a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccountGroup(
            self,
            request: models.DeleteAccountGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountGroupResponse:
        """
        This API is used to delete an account group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAppAccount(
            self,
            request: models.DeleteAppAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteAppAccountResponse:
        """
        This API is used to delete an application account.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAppAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrgNode(
            self,
            request: models.DeleteOrgNodeRequest,
            opts: Dict = None,
    ) -> models.DeleteOrgNodeResponse:
        """
        This API is used to delete an organization node.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        This API is used to delete a user by username or user ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserGroup(
            self,
            request: models.DeleteUserGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteUserGroupResponse:
        """
        This API is used to delete a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsers(
            self,
            request: models.DeleteUsersRequest,
            opts: Dict = None,
    ) -> models.DeleteUsersResponse:
        """
        This API is used to batch delete the users under the current node. If an error occurs when a user is deleted, the deletion of other selected users will not be affected, and the username/ID of the user who fails to be deleted will be prompted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountGroup(
            self,
            request: models.DescribeAccountGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountGroupResponse:
        """
        This API is used to query the list of account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppAccount(
            self,
            request: models.DescribeAppAccountRequest,
            opts: Dict = None,
    ) -> models.DescribeAppAccountResponse:
        """
        This API is used to query the list of application accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplication(
            self,
            request: models.DescribeApplicationRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationResponse:
        """
        This API is used to get the information of an application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrgNode(
            self,
            request: models.DescribeOrgNodeRequest,
            opts: Dict = None,
    ) -> models.DescribeOrgNodeResponse:
        """
        This API is used to read the information of an organization node by organization node ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicKey(
            self,
            request: models.DescribePublicKeyRequest,
            opts: Dict = None,
    ) -> models.DescribePublicKeyResponse:
        """
        This API is used to get the information of a JWT public key.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserGroup(
            self,
            request: models.DescribeUserGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeUserGroupResponse:
        """
        This API is used to get the information of a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserInfo(
            self,
            request: models.DescribeUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserInfoResponse:
        """
        This API is used to search for a user by username or user ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserResourcesAuthorization(
            self,
            request: models.DescribeUserResourcesAuthorizationRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResourcesAuthorizationResponse:
        """
        This API is used to query the list of resource authorizations under the specified user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserResourcesAuthorization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResourcesAuthorizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserThirdPartyAccountInfo(
            self,
            request: models.DescribeUserThirdPartyAccountInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserThirdPartyAccountInfoResponse:
        """
        This API is used to get the third-party account binding information by username or user ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserThirdPartyAccountInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserThirdPartyAccountInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAccountInAccountGroup(
            self,
            request: models.ListAccountInAccountGroupRequest,
            opts: Dict = None,
    ) -> models.ListAccountInAccountGroupResponse:
        """
        This API is used to get the list of accounts in an account group.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAccountInAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAccountInAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListApplicationAuthorizations(
            self,
            request: models.ListApplicationAuthorizationsRequest,
            opts: Dict = None,
    ) -> models.ListApplicationAuthorizationsResponse:
        """
        This API is used to get the list of authorization relationships of an application (including search criteria-based match).
        """
        
        kwargs = {}
        kwargs["action"] = "ListApplicationAuthorizations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListApplicationAuthorizationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListApplications(
            self,
            request: models.ListApplicationsRequest,
            opts: Dict = None,
    ) -> models.ListApplicationsResponse:
        """
        This API is used to get the list of applications.
        """
        
        kwargs = {}
        kwargs["action"] = "ListApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAuthorizedApplicationsToOrgNode(
            self,
            request: models.ListAuthorizedApplicationsToOrgNodeRequest,
            opts: Dict = None,
    ) -> models.ListAuthorizedApplicationsToOrgNodeResponse:
        """
        This API is used to get the list of accessible applications by organization node ID.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAuthorizedApplicationsToOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAuthorizedApplicationsToOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAuthorizedApplicationsToUser(
            self,
            request: models.ListAuthorizedApplicationsToUserRequest,
            opts: Dict = None,
    ) -> models.ListAuthorizedApplicationsToUserResponse:
        """
        This API is used to get the list of accessible applications by user ID.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAuthorizedApplicationsToUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAuthorizedApplicationsToUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAuthorizedApplicationsToUserGroup(
            self,
            request: models.ListAuthorizedApplicationsToUserGroupRequest,
            opts: Dict = None,
    ) -> models.ListAuthorizedApplicationsToUserGroupResponse:
        """
        This API is used to get the list of accessible applications by user group ID.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAuthorizedApplicationsToUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAuthorizedApplicationsToUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUserGroups(
            self,
            request: models.ListUserGroupsRequest,
            opts: Dict = None,
    ) -> models.ListUserGroupsResponse:
        """
        This API is used to get the information of the user group list (including query conditions).
        """
        
        kwargs = {}
        kwargs["action"] = "ListUserGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUserGroupsOfUser(
            self,
            request: models.ListUserGroupsOfUserRequest,
            opts: Dict = None,
    ) -> models.ListUserGroupsOfUserResponse:
        """
        This API is used to get the list of a user's user groups.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUserGroupsOfUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserGroupsOfUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsers(
            self,
            request: models.ListUsersRequest,
            opts: Dict = None,
    ) -> models.ListUsersResponse:
        """
        This API is used to get the information of the user list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsersInOrgNode(
            self,
            request: models.ListUsersInOrgNodeRequest,
            opts: Dict = None,
    ) -> models.ListUsersInOrgNodeResponse:
        """
        This API is used to read the users under an organization node by organization node ID.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsersInOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersInOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsersInUserGroup(
            self,
            request: models.ListUsersInUserGroupRequest,
            opts: Dict = None,
    ) -> models.ListUsersInUserGroupResponse:
        """
        This API is used to get the list of the users in a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsersInUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersInUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountGroup(
            self,
            request: models.ModifyAccountGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountGroupResponse:
        """
        This API is used to modify an account group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAppAccount(
            self,
            request: models.ModifyAppAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyAppAccountResponse:
        """
        This API is used to modify an application account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAppAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAppAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplication(
            self,
            request: models.ModifyApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationResponse:
        """
        This API is used to update the information of an application.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserInfo(
            self,
            request: models.ModifyUserInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyUserInfoResponse:
        """
        This API is used to modify the information of a user by username or user ID.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveAccountFromAccountGroup(
            self,
            request: models.RemoveAccountFromAccountGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveAccountFromAccountGroupResponse:
        """
        This API is used to remove an account from an account group.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveAccountFromAccountGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveAccountFromAccountGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveUserFromUserGroup(
            self,
            request: models.RemoveUserFromUserGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveUserFromUserGroupResponse:
        """
        This API is used to remove a user from a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveUserFromUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveUserFromUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrgNode(
            self,
            request: models.UpdateOrgNodeRequest,
            opts: Dict = None,
    ) -> models.UpdateOrgNodeResponse:
        """
        This API is used to create an organization node.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrgNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrgNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)