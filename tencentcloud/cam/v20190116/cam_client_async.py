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
from tencentcloud.cam.v20190116 import models
from typing import Dict


class CamClient(AbstractClient):
    _apiVersion = '2019-01-16'
    _endpoint = 'cam.intl.tencentcloudapi.com'
    _service = 'cam'

    async def AddUser(
            self,
            request: models.AddUserRequest,
            opts: Dict = None,
    ) -> models.AddUserResponse:
        """
        This API is used to create a sub-user.
        """
        
        kwargs = {}
        kwargs["action"] = "AddUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUserToGroup(
            self,
            request: models.AddUserToGroupRequest,
            opts: Dict = None,
    ) -> models.AddUserToGroupResponse:
        """
        This API is used to add users to a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserToGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserToGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachGroupPolicy(
            self,
            request: models.AttachGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachGroupPolicyResponse:
        """
        This API (AttachGroupPolicy) is used to associate a policy with a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachRolePolicy(
            self,
            request: models.AttachRolePolicyRequest,
            opts: Dict = None,
    ) -> models.AttachRolePolicyResponse:
        """
        This API (AttachRolePolicy) is used to associate a policy with a role.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachRolePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachRolePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachUserPolicy(
            self,
            request: models.AttachUserPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachUserPolicyResponse:
        """
        This API (AttachUserPolicy) is used to associates a policy with a user.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachUserPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachUserPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConsumeCustomMFAToken(
            self,
            request: models.ConsumeCustomMFATokenRequest,
            opts: Dict = None,
    ) -> models.ConsumeCustomMFATokenResponse:
        """
        This API is used to verify a custom multi-factor Token.
        """
        
        kwargs = {}
        kwargs["action"] = "ConsumeCustomMFAToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConsumeCustomMFATokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessKey(
            self,
            request: models.CreateAccessKeyRequest,
            opts: Dict = None,
    ) -> models.CreateAccessKeyResponse:
        """
        This API is used to create an access key for a CAM user.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroup(
            self,
            request: models.CreateGroupRequest,
            opts: Dict = None,
    ) -> models.CreateGroupResponse:
        """
        This API is used to create a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOIDCConfig(
            self,
            request: models.CreateOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.CreateOIDCConfigResponse:
        """
        This API is used to create role OIDC configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePolicy(
            self,
            request: models.CreatePolicyRequest,
            opts: Dict = None,
    ) -> models.CreatePolicyResponse:
        """
        This API (CreatePolicy) is used to create a policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePolicyVersion(
            self,
            request: models.CreatePolicyVersionRequest,
            opts: Dict = None,
    ) -> models.CreatePolicyVersionResponse:
        """
        This API is used to add a policy version. After creating a policy version, you can easily change the policy by changing the policy version.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePolicyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePolicyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRole(
            self,
            request: models.CreateRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRoleResponse:
        """
        This API (CreateRole) is used to create a role.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSAMLProvider(
            self,
            request: models.CreateSAMLProviderRequest,
            opts: Dict = None,
    ) -> models.CreateSAMLProviderResponse:
        """
        This API is used to create a SAML identity provider.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSAMLProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSAMLProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceLinkedRole(
            self,
            request: models.CreateServiceLinkedRoleRequest,
            opts: Dict = None,
    ) -> models.CreateServiceLinkedRoleResponse:
        """
        This API is used to create a service-linked role.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceLinkedRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceLinkedRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserOIDCConfig(
            self,
            request: models.CreateUserOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.CreateUserOIDCConfigResponse:
        """
        This API is used to create a user OIDC configuration. Only one user OIDC IdP can be created, and the user SAML SSO IdP will be automatically disabled after it is created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserSAMLConfig(
            self,
            request: models.CreateUserSAMLConfigRequest,
            opts: Dict = None,
    ) -> models.CreateUserSAMLConfigResponse:
        """
        This API is used to create user SAML configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserSAMLConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserSAMLConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccessKey(
            self,
            request: models.DeleteAccessKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteAccessKeyResponse:
        """
        This API is used to delete an access key for a CAM user.
        Calling this API is a high-risk operation because the key cannot be recovered once deleted and Tencent Cloud will deny all requests that use this key. Proceed with caution.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccessKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccessKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        This API is used to delete a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOIDCConfig(
            self,
            request: models.DeleteOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteOIDCConfigResponse:
        """
        This API is used to delete OIDC IdPs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePolicy(
            self,
            request: models.DeletePolicyRequest,
            opts: Dict = None,
    ) -> models.DeletePolicyResponse:
        """
        This API (DeletePolicy) is used to delete a policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePolicyVersion(
            self,
            request: models.DeletePolicyVersionRequest,
            opts: Dict = None,
    ) -> models.DeletePolicyVersionResponse:
        """
        This API is used to delete a policy version of a policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePolicyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePolicyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRole(
            self,
            request: models.DeleteRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteRoleResponse:
        """
        This API (DeleteRole) is used to delete a specified role.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRolePermissionsBoundary(
            self,
            request: models.DeleteRolePermissionsBoundaryRequest,
            opts: Dict = None,
    ) -> models.DeleteRolePermissionsBoundaryResponse:
        """
        This API is used to delete a role permission boundary.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRolePermissionsBoundary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRolePermissionsBoundaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSAMLProvider(
            self,
            request: models.DeleteSAMLProviderRequest,
            opts: Dict = None,
    ) -> models.DeleteSAMLProviderResponse:
        """
        This API is used to delete a SAML identity provider.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSAMLProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSAMLProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceLinkedRole(
            self,
            request: models.DeleteServiceLinkedRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceLinkedRoleResponse:
        """
        This API is used to delete a service-linked role.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceLinkedRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceLinkedRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        This API is used to delete a sub-user.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserPermissionsBoundary(
            self,
            request: models.DeleteUserPermissionsBoundaryRequest,
            opts: Dict = None,
    ) -> models.DeleteUserPermissionsBoundaryResponse:
        """
        This API is used to delete a user permission boundary.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserPermissionsBoundary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserPermissionsBoundaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOIDCConfig(
            self,
            request: models.DescribeOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeOIDCConfigResponse:
        """
        This API is used to query role OIDC configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoleList(
            self,
            request: models.DescribeRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeRoleListResponse:
        """
        This API (DescribeRoleList) is used to get the role list under the account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSafeAuthFlagColl(
            self,
            request: models.DescribeSafeAuthFlagCollRequest,
            opts: Dict = None,
    ) -> models.DescribeSafeAuthFlagCollResponse:
        """
        This API is used to get a sub-account’s security settings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSafeAuthFlagColl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSafeAuthFlagCollResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSafeAuthFlagIntl(
            self,
            request: models.DescribeSafeAuthFlagIntlRequest,
            opts: Dict = None,
    ) -> models.DescribeSafeAuthFlagIntlResponse:
        """
        This API is used to query security settings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSafeAuthFlagIntl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSafeAuthFlagIntlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubAccounts(
            self,
            request: models.DescribeSubAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubAccountsResponse:
        """
        This API is used to query sub-users through the sub-user UIN list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserOIDCConfig(
            self,
            request: models.DescribeUserOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUserOIDCConfigResponse:
        """
        This API is used to query the user OIDC configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserSAMLConfig(
            self,
            request: models.DescribeUserSAMLConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUserSAMLConfigResponse:
        """
        This API is used to query user SAML configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserSAMLConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserSAMLConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachGroupPolicy(
            self,
            request: models.DetachGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.DetachGroupPolicyResponse:
        """
        This API (DetachGroupPolicy) is used to unassociate a policy and a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachRolePolicy(
            self,
            request: models.DetachRolePolicyRequest,
            opts: Dict = None,
    ) -> models.DetachRolePolicyResponse:
        """
        This API (DetachRolePolicy) is used to unassociate a policy and a role.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachRolePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachRolePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachUserPolicy(
            self,
            request: models.DetachUserPolicyRequest,
            opts: Dict = None,
    ) -> models.DetachUserPolicyResponse:
        """
        This API (DetachUserPolicy) is used to unassociate a policy and a user.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachUserPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachUserPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableUserSSO(
            self,
            request: models.DisableUserSSORequest,
            opts: Dict = None,
    ) -> models.DisableUserSSOResponse:
        """
        This API is used to disable user SSO.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableUserSSO"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableUserSSOResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAccountSummary(
            self,
            request: models.GetAccountSummaryRequest,
            opts: Dict = None,
    ) -> models.GetAccountSummaryResponse:
        """
        This API is used to query account summary.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAccountSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAccountSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCustomMFATokenInfo(
            self,
            request: models.GetCustomMFATokenInfoRequest,
            opts: Dict = None,
    ) -> models.GetCustomMFATokenInfoResponse:
        """
        This API is used to get information associated with a custom multi-factor Token
        """
        
        kwargs = {}
        kwargs["action"] = "GetCustomMFATokenInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCustomMFATokenInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroup(
            self,
            request: models.GetGroupRequest,
            opts: Dict = None,
    ) -> models.GetGroupResponse:
        """
        This API is used to query user group details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPolicy(
            self,
            request: models.GetPolicyRequest,
            opts: Dict = None,
    ) -> models.GetPolicyResponse:
        """
        This API (GetPolicy) is used to query and view policy details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPolicyVersion(
            self,
            request: models.GetPolicyVersionRequest,
            opts: Dict = None,
    ) -> models.GetPolicyVersionResponse:
        """
        This API is used to query policy version details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetPolicyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPolicyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRole(
            self,
            request: models.GetRoleRequest,
            opts: Dict = None,
    ) -> models.GetRoleResponse:
        """
        This API (GetRole) is used to get the details of a specified role.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSAMLProvider(
            self,
            request: models.GetSAMLProviderRequest,
            opts: Dict = None,
    ) -> models.GetSAMLProviderResponse:
        """
        This API is used to query SAML identity provider details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSAMLProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSAMLProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSecurityLastUsed(
            self,
            request: models.GetSecurityLastUsedRequest,
            opts: Dict = None,
    ) -> models.GetSecurityLastUsedResponse:
        """
        This API is used to get a key’s recent usage details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSecurityLastUsed"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSecurityLastUsedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetServiceLinkedRoleDeletionStatus(
            self,
            request: models.GetServiceLinkedRoleDeletionStatusRequest,
            opts: Dict = None,
    ) -> models.GetServiceLinkedRoleDeletionStatusResponse:
        """
        This API is used to get the status of the service-linked role deletion based on the `TaskId`
        """
        
        kwargs = {}
        kwargs["action"] = "GetServiceLinkedRoleDeletionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetServiceLinkedRoleDeletionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUser(
            self,
            request: models.GetUserRequest,
            opts: Dict = None,
    ) -> models.GetUserResponse:
        """
        This API is used to query sub-users.
        """
        
        kwargs = {}
        kwargs["action"] = "GetUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUserAppId(
            self,
            request: models.GetUserAppIdRequest,
            opts: Dict = None,
    ) -> models.GetUserAppIdResponse:
        """
        This API is used to get the user AppId.
        """
        
        kwargs = {}
        kwargs["action"] = "GetUserAppId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserAppIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAccessKeys(
            self,
            request: models.ListAccessKeysRequest,
            opts: Dict = None,
    ) -> models.ListAccessKeysResponse:
        """
        This API is used to list the access keys associated with a specified CAM user.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAccessKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAccessKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAttachedGroupPolicies(
            self,
            request: models.ListAttachedGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.ListAttachedGroupPoliciesResponse:
        """
        This API (ListAttachedGroupPolicies) is used to query the list of policies associated with a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAttachedGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAttachedGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAttachedRolePolicies(
            self,
            request: models.ListAttachedRolePoliciesRequest,
            opts: Dict = None,
    ) -> models.ListAttachedRolePoliciesResponse:
        """
        This API (ListAttachedRolePolicies) is used to obtain the list of the policies associated with a role.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAttachedRolePolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAttachedRolePoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAttachedUserAllPolicies(
            self,
            request: models.ListAttachedUserAllPoliciesRequest,
            opts: Dict = None,
    ) -> models.ListAttachedUserAllPoliciesResponse:
        """
        This API is used to list policies associated with the user (including those inherited from the user group).
        """
        
        kwargs = {}
        kwargs["action"] = "ListAttachedUserAllPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAttachedUserAllPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAttachedUserPolicies(
            self,
            request: models.ListAttachedUserPoliciesRequest,
            opts: Dict = None,
    ) -> models.ListAttachedUserPoliciesResponse:
        """
        This API (ListAttachedUserPolicies) is used to query the list of policies associated with a sub-account.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAttachedUserPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAttachedUserPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCollaborators(
            self,
            request: models.ListCollaboratorsRequest,
            opts: Dict = None,
    ) -> models.ListCollaboratorsResponse:
        """
        This API is used to get the collaborator list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListCollaborators"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCollaboratorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEntitiesForPolicy(
            self,
            request: models.ListEntitiesForPolicyRequest,
            opts: Dict = None,
    ) -> models.ListEntitiesForPolicyResponse:
        """
        This API (ListEntitiesForPolicy) is used to query the list of entities associated with a policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ListEntitiesForPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEntitiesForPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListGroups(
            self,
            request: models.ListGroupsRequest,
            opts: Dict = None,
    ) -> models.ListGroupsResponse:
        """
        This API is used to query the list of user groups.
        """
        
        kwargs = {}
        kwargs["action"] = "ListGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListGroupsForUser(
            self,
            request: models.ListGroupsForUserRequest,
            opts: Dict = None,
    ) -> models.ListGroupsForUserResponse:
        """
        This API is used to list user groups associated with a user.
        """
        
        kwargs = {}
        kwargs["action"] = "ListGroupsForUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListGroupsForUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPolicies(
            self,
            request: models.ListPoliciesRequest,
            opts: Dict = None,
    ) -> models.ListPoliciesResponse:
        """
        This API is used to query the policy list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPolicyVersions(
            self,
            request: models.ListPolicyVersionsRequest,
            opts: Dict = None,
    ) -> models.ListPolicyVersionsResponse:
        """
        This API is used to get the list of policy versions.
        """
        
        kwargs = {}
        kwargs["action"] = "ListPolicyVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPolicyVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSAMLProviders(
            self,
            request: models.ListSAMLProvidersRequest,
            opts: Dict = None,
    ) -> models.ListSAMLProvidersResponse:
        """
        This API is used to query the list of SAML identity providers.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSAMLProviders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSAMLProvidersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsers(
            self,
            request: models.ListUsersRequest,
            opts: Dict = None,
    ) -> models.ListUsersResponse:
        """
        This API is used to pull sub-users.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsersForGroup(
            self,
            request: models.ListUsersForGroupRequest,
            opts: Dict = None,
    ) -> models.ListUsersForGroupResponse:
        """
        This API is used to query the list of users associated with a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsersForGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersForGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutRolePermissionsBoundary(
            self,
            request: models.PutRolePermissionsBoundaryRequest,
            opts: Dict = None,
    ) -> models.PutRolePermissionsBoundaryResponse:
        """
        This API is used to set a role permission boundary.
        """
        
        kwargs = {}
        kwargs["action"] = "PutRolePermissionsBoundary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutRolePermissionsBoundaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutUserPermissionsBoundary(
            self,
            request: models.PutUserPermissionsBoundaryRequest,
            opts: Dict = None,
    ) -> models.PutUserPermissionsBoundaryResponse:
        """
        This API is used to set a user permission boundary.
        """
        
        kwargs = {}
        kwargs["action"] = "PutUserPermissionsBoundary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutUserPermissionsBoundaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveUserFromGroup(
            self,
            request: models.RemoveUserFromGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveUserFromGroupResponse:
        """
        This API is used to delete users from a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveUserFromGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveUserFromGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetDefaultPolicyVersion(
            self,
            request: models.SetDefaultPolicyVersionRequest,
            opts: Dict = None,
    ) -> models.SetDefaultPolicyVersionResponse:
        """
        This API is used to set the operative policy version.
        """
        
        kwargs = {}
        kwargs["action"] = "SetDefaultPolicyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetDefaultPolicyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetMfaFlag(
            self,
            request: models.SetMfaFlagRequest,
            opts: Dict = None,
    ) -> models.SetMfaFlagResponse:
        """
        This API is used to set account verification for login and sensitive operations for sub-users.
        """
        
        kwargs = {}
        kwargs["action"] = "SetMfaFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetMfaFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TagRole(
            self,
            request: models.TagRoleRequest,
            opts: Dict = None,
    ) -> models.TagRoleResponse:
        """
        This API is used to bind tags to a role.
        """
        
        kwargs = {}
        kwargs["action"] = "TagRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TagRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UntagRole(
            self,
            request: models.UntagRoleRequest,
            opts: Dict = None,
    ) -> models.UntagRoleResponse:
        """
        This API is used to unbind tags from a role.
        """
        
        kwargs = {}
        kwargs["action"] = "UntagRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UntagRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAccessKey(
            self,
            request: models.UpdateAccessKeyRequest,
            opts: Dict = None,
    ) -> models.UpdateAccessKeyResponse:
        """
        This API is used to update an access key for a CAM user.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAccessKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAccessKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAssumeRolePolicy(
            self,
            request: models.UpdateAssumeRolePolicyRequest,
            opts: Dict = None,
    ) -> models.UpdateAssumeRolePolicyResponse:
        """
        This API (UpdateAssumeRolePolicy) is used to modify the trust policy of a role.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAssumeRolePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAssumeRolePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGroup(
            self,
            request: models.UpdateGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateGroupResponse:
        """
        This API is used to update a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOIDCConfig(
            self,
            request: models.UpdateOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateOIDCConfigResponse:
        """
        This API is used to modify role OIDC configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePolicy(
            self,
            request: models.UpdatePolicyRequest,
            opts: Dict = None,
    ) -> models.UpdatePolicyResponse:
        """
        This API is used to update a policy.
        This API will update the default version of an existing policy instead of creating a new one. If no policy exists, a default version will be created.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRoleConsoleLogin(
            self,
            request: models.UpdateRoleConsoleLoginRequest,
            opts: Dict = None,
    ) -> models.UpdateRoleConsoleLoginResponse:
        """
        This API is used to modify a role's login permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRoleConsoleLogin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRoleConsoleLoginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRoleDescription(
            self,
            request: models.UpdateRoleDescriptionRequest,
            opts: Dict = None,
    ) -> models.UpdateRoleDescriptionResponse:
        """
        This API (UpdateRoleDescription) is used to modify the description of a role.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRoleDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRoleDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSAMLProvider(
            self,
            request: models.UpdateSAMLProviderRequest,
            opts: Dict = None,
    ) -> models.UpdateSAMLProviderResponse:
        """
        This API is used to update SAML identity provider information.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSAMLProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSAMLProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUser(
            self,
            request: models.UpdateUserRequest,
            opts: Dict = None,
    ) -> models.UpdateUserResponse:
        """
        This API is used to update a sub-user.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserOIDCConfig(
            self,
            request: models.UpdateUserOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateUserOIDCConfigResponse:
        """
        This API is used to modify the user OIDC configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserSAMLConfig(
            self,
            request: models.UpdateUserSAMLConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateUserSAMLConfigResponse:
        """
        This API is used to modify user SAML configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserSAMLConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserSAMLConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)