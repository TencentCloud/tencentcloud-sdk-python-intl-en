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
from tencentcloud.organization.v20210331 import models
from typing import Dict


class OrganizationClient(AbstractClient):
    _apiVersion = '2021-03-31'
    _endpoint = 'organization.intl.tencentcloudapi.com'
    _service = 'organization'

    async def AcceptJoinShareUnitInvitation(
            self,
            request: models.AcceptJoinShareUnitInvitationRequest,
            opts: Dict = None,
    ) -> models.AcceptJoinShareUnitInvitationResponse:
        """
        This API is used to accept an invitation to join a shared unit.
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptJoinShareUnitInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptJoinShareUnitInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddExternalSAMLIdPCertificate(
            self,
            request: models.AddExternalSAMLIdPCertificateRequest,
            opts: Dict = None,
    ) -> models.AddExternalSAMLIdPCertificateResponse:
        """
        This API is used to add SAML signing certificates.
        """
        
        kwargs = {}
        kwargs["action"] = "AddExternalSAMLIdPCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddExternalSAMLIdPCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddOrganizationMemberEmail(
            self,
            request: models.AddOrganizationMemberEmailRequest,
            opts: Dict = None,
    ) -> models.AddOrganizationMemberEmailResponse:
        """
        This API is used to add an organization member's mailbox.
        """
        
        kwargs = {}
        kwargs["action"] = "AddOrganizationMemberEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddOrganizationMemberEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddOrganizationNode(
            self,
            request: models.AddOrganizationNodeRequest,
            opts: Dict = None,
    ) -> models.AddOrganizationNodeResponse:
        """
        This API is used to add an organization node.
        """
        
        kwargs = {}
        kwargs["action"] = "AddOrganizationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddOrganizationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddPermissionPolicyToRoleConfiguration(
            self,
            request: models.AddPermissionPolicyToRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.AddPermissionPolicyToRoleConfigurationResponse:
        """
        This API is used to add policies to permission configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "AddPermissionPolicyToRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddPermissionPolicyToRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddShareUnit(
            self,
            request: models.AddShareUnitRequest,
            opts: Dict = None,
    ) -> models.AddShareUnitResponse:
        """
        This API is used to create a shared unit.
        """
        
        kwargs = {}
        kwargs["action"] = "AddShareUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddShareUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddShareUnitMembers(
            self,
            request: models.AddShareUnitMembersRequest,
            opts: Dict = None,
    ) -> models.AddShareUnitMembersResponse:
        """
        This API is used to add a shared unit member.
        """
        
        kwargs = {}
        kwargs["action"] = "AddShareUnitMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddShareUnitMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddShareUnitResources(
            self,
            request: models.AddShareUnitResourcesRequest,
            opts: Dict = None,
    ) -> models.AddShareUnitResourcesResponse:
        """
        This API is used to add resources to a shared unit.
        """
        
        kwargs = {}
        kwargs["action"] = "AddShareUnitResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddShareUnitResourcesResponse
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
        
    async def BindOrganizationMemberAuthAccount(
            self,
            request: models.BindOrganizationMemberAuthAccountRequest,
            opts: Dict = None,
    ) -> models.BindOrganizationMemberAuthAccountResponse:
        """
        This API is used to bind an organization member to a sub-account of the organization admin.
        """
        
        kwargs = {}
        kwargs["action"] = "BindOrganizationMemberAuthAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindOrganizationMemberAuthAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelOrganizationMemberAuthAccount(
            self,
            request: models.CancelOrganizationMemberAuthAccountRequest,
            opts: Dict = None,
    ) -> models.CancelOrganizationMemberAuthAccountResponse:
        """
        This API is used to unbind an organization member from a sub-account of the organization admin.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelOrganizationMemberAuthAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelOrganizationMemberAuthAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearExternalSAMLIdentityProvider(
            self,
            request: models.ClearExternalSAMLIdentityProviderRequest,
            opts: Dict = None,
    ) -> models.ClearExternalSAMLIdentityProviderResponse:
        """
        This API is used to clear the SAML identity provider configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "ClearExternalSAMLIdentityProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearExternalSAMLIdentityProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroup(
            self,
            request: models.CreateGroupRequest,
            opts: Dict = None,
    ) -> models.CreateGroupResponse:
        """
        This API is used to create user groups.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrgServiceAssign(
            self,
            request: models.CreateOrgServiceAssignRequest,
            opts: Dict = None,
    ) -> models.CreateOrgServiceAssignResponse:
        """
        This API is used to add a delegated admin of the organization service.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrgServiceAssign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrgServiceAssignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganization(
            self,
            request: models.CreateOrganizationRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationResponse:
        """
        This API is used to create an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganizationIdentity(
            self,
            request: models.CreateOrganizationIdentityRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationIdentityResponse:
        """
        This API is used to add an organization identity.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganizationIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganizationMember(
            self,
            request: models.CreateOrganizationMemberRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationMemberResponse:
        """
        This API is used to create an organization member.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganizationMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganizationMemberAuthIdentity(
            self,
            request: models.CreateOrganizationMemberAuthIdentityRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationMemberAuthIdentityResponse:
        """
        This API is used to add organization member access authorization.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganizationMemberAuthIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationMemberAuthIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganizationMemberPolicy(
            self,
            request: models.CreateOrganizationMemberPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationMemberPolicyResponse:
        """
        This API is used to create an organization member access authorization policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganizationMemberPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationMemberPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganizationMembersPolicy(
            self,
            request: models.CreateOrganizationMembersPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationMembersPolicyResponse:
        """
        This API is used to create an organization member access policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganizationMembersPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationMembersPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoleAssignment(
            self,
            request: models.CreateRoleAssignmentRequest,
            opts: Dict = None,
    ) -> models.CreateRoleAssignmentResponse:
        """
        This API is used to grant authorizations on member accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoleAssignment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleAssignmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoleConfiguration(
            self,
            request: models.CreateRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.CreateRoleConfigurationResponse:
        """
        This API is used to create permission configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSCIMCredential(
            self,
            request: models.CreateSCIMCredentialRequest,
            opts: Dict = None,
    ) -> models.CreateSCIMCredentialResponse:
        """
        This API is used to create a SCIM key.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSCIMCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSCIMCredentialResponse
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
        
    async def CreateUserSyncProvisioning(
            self,
            request: models.CreateUserSyncProvisioningRequest,
            opts: Dict = None,
    ) -> models.CreateUserSyncProvisioningResponse:
        """
        This API is used to create sub-user synchronization tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserSyncProvisioning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserSyncProvisioningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        This API is used to delete user groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrgServiceAssign(
            self,
            request: models.DeleteOrgServiceAssignRequest,
            opts: Dict = None,
    ) -> models.DeleteOrgServiceAssignResponse:
        """
        This API is used to delete a delegated admin of the organization service.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrgServiceAssign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrgServiceAssignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganization(
            self,
            request: models.DeleteOrganizationRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationResponse:
        """
        This API is used to delete an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationIdentity(
            self,
            request: models.DeleteOrganizationIdentityRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationIdentityResponse:
        """
        This API is used to delete an organization identity.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationMemberAuthIdentity(
            self,
            request: models.DeleteOrganizationMemberAuthIdentityRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationMemberAuthIdentityResponse:
        """
        This API is used to delete organization member access authorization.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationMemberAuthIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationMemberAuthIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationMembers(
            self,
            request: models.DeleteOrganizationMembersRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationMembersResponse:
        """
        This API is used to remove a member account from the organization, rather than delete the account.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationMembersPolicy(
            self,
            request: models.DeleteOrganizationMembersPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationMembersPolicyResponse:
        """
        This API is used to delete an organization member access policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationMembersPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationMembersPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationNodes(
            self,
            request: models.DeleteOrganizationNodesRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationNodesResponse:
        """
        This API is used to batch delete organization nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoleAssignment(
            self,
            request: models.DeleteRoleAssignmentRequest,
            opts: Dict = None,
    ) -> models.DeleteRoleAssignmentResponse:
        """
        This API is used to remove authorizations on member accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoleAssignment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoleAssignmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoleConfiguration(
            self,
            request: models.DeleteRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.DeleteRoleConfigurationResponse:
        """
        This API is used to delete the permission configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSCIMCredential(
            self,
            request: models.DeleteSCIMCredentialRequest,
            opts: Dict = None,
    ) -> models.DeleteSCIMCredentialResponse:
        """
        This API is used to delete a SCIM key.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSCIMCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSCIMCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShareUnit(
            self,
            request: models.DeleteShareUnitRequest,
            opts: Dict = None,
    ) -> models.DeleteShareUnitResponse:
        """
        This API is used to delete a shared unit.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShareUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShareUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShareUnitMembers(
            self,
            request: models.DeleteShareUnitMembersRequest,
            opts: Dict = None,
    ) -> models.DeleteShareUnitMembersResponse:
        """
        This API is used to delete a shared unit member.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShareUnitMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShareUnitMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShareUnitResources(
            self,
            request: models.DeleteShareUnitResourcesRequest,
            opts: Dict = None,
    ) -> models.DeleteShareUnitResourcesResponse:
        """
        This API is used to delete shared unit resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShareUnitResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShareUnitResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        This API is used to delete a user.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserSyncProvisioning(
            self,
            request: models.DeleteUserSyncProvisioningRequest,
            opts: Dict = None,
    ) -> models.DeleteUserSyncProvisioningResponse:
        """
        This API is used to delete sub-user synchronization tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserSyncProvisioning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserSyncProvisioningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdentityCenter(
            self,
            request: models.DescribeIdentityCenterRequest,
            opts: Dict = None,
    ) -> models.DescribeIdentityCenterResponse:
        """
        This API is used to obtain TCO Identity Center service information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdentityCenter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdentityCenterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganization(
            self,
            request: models.DescribeOrganizationRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationResponse:
        """
        This API is used to get the organization information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMemberAuthAccounts(
            self,
            request: models.DescribeOrganizationMemberAuthAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMemberAuthAccountsResponse:
        """
        This API is used to get the list of sub-accounts bound to an organization member.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMemberAuthAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMemberAuthAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMemberAuthIdentities(
            self,
            request: models.DescribeOrganizationMemberAuthIdentitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMemberAuthIdentitiesResponse:
        """
        This API is used to obtain the list of organization member access authorization.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMemberAuthIdentities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMemberAuthIdentitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMemberEmailBind(
            self,
            request: models.DescribeOrganizationMemberEmailBindRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMemberEmailBindResponse:
        """
        This API is used to query detailed information about member mailbox binding.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMemberEmailBind"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMemberEmailBindResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMemberPolicies(
            self,
            request: models.DescribeOrganizationMemberPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMemberPoliciesResponse:
        """
        This API is used to get the list of authorization policies of an organization member.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMemberPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMemberPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationMembers(
            self,
            request: models.DescribeOrganizationMembersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationMembersResponse:
        """
        This API is used to get the list of organization members.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationNodes(
            self,
            request: models.DescribeOrganizationNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationNodesResponse:
        """
        This API is used to get the list of organization nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShareAreas(
            self,
            request: models.DescribeShareAreasRequest,
            opts: Dict = None,
    ) -> models.DescribeShareAreasResponse:
        """
        This API is used to obtain a list of shareable regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShareAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShareAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShareUnitMembers(
            self,
            request: models.DescribeShareUnitMembersRequest,
            opts: Dict = None,
    ) -> models.DescribeShareUnitMembersResponse:
        """
        This API is used to obtain the member list of a shared unit.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShareUnitMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShareUnitMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShareUnitResources(
            self,
            request: models.DescribeShareUnitResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeShareUnitResourcesResponse:
        """
        This API is used to obtain the resource list of a shared unit.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShareUnitResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShareUnitResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShareUnits(
            self,
            request: models.DescribeShareUnitsRequest,
            opts: Dict = None,
    ) -> models.DescribeShareUnitsResponse:
        """
        This API is used to obtain a list of shared units.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShareUnits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShareUnitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DismantleRoleConfiguration(
            self,
            request: models.DismantleRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.DismantleRoleConfigurationResponse:
        """
        This API is used to undeploy permission configurations on member accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DismantleRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DismantleRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetExternalSAMLIdentityProvider(
            self,
            request: models.GetExternalSAMLIdentityProviderRequest,
            opts: Dict = None,
    ) -> models.GetExternalSAMLIdentityProviderResponse:
        """
        This API is used to query the SAML identity provider configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetExternalSAMLIdentityProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetExternalSAMLIdentityProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroup(
            self,
            request: models.GetGroupRequest,
            opts: Dict = None,
    ) -> models.GetGroupResponse:
        """
        This API is used to query the user group information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetProvisioningTaskStatus(
            self,
            request: models.GetProvisioningTaskStatusRequest,
            opts: Dict = None,
    ) -> models.GetProvisioningTaskStatusResponse:
        """
        This API is used to query the status of async tasks of user synchronization.
        """
        
        kwargs = {}
        kwargs["action"] = "GetProvisioningTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetProvisioningTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRoleConfiguration(
            self,
            request: models.GetRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.GetRoleConfigurationResponse:
        """
        This API is used to query the permission configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSCIMSynchronizationStatus(
            self,
            request: models.GetSCIMSynchronizationStatusRequest,
            opts: Dict = None,
    ) -> models.GetSCIMSynchronizationStatusResponse:
        """
        This API is used to query SCIM synchronization status.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSCIMSynchronizationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSCIMSynchronizationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskStatus(
            self,
            request: models.GetTaskStatusRequest,
            opts: Dict = None,
    ) -> models.GetTaskStatusResponse:
        """
        This API is used to query the status of async tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUser(
            self,
            request: models.GetUserRequest,
            opts: Dict = None,
    ) -> models.GetUserResponse:
        """
        This API is used to query the user information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUserSyncProvisioning(
            self,
            request: models.GetUserSyncProvisioningRequest,
            opts: Dict = None,
    ) -> models.GetUserSyncProvisioningResponse:
        """
        This API is used to query the CAM user synchronization.
        """
        
        kwargs = {}
        kwargs["action"] = "GetUserSyncProvisioning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserSyncProvisioningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetZoneSAMLServiceProviderInfo(
            self,
            request: models.GetZoneSAMLServiceProviderInfoRequest,
            opts: Dict = None,
    ) -> models.GetZoneSAMLServiceProviderInfoResponse:
        """
        This API is used to query the SAML service provider configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetZoneSAMLServiceProviderInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetZoneSAMLServiceProviderInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetZoneStatistics(
            self,
            request: models.GetZoneStatisticsRequest,
            opts: Dict = None,
    ) -> models.GetZoneStatisticsResponse:
        """
        This API is used to query space statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "GetZoneStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetZoneStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InviteOrganizationMember(
            self,
            request: models.InviteOrganizationMemberRequest,
            opts: Dict = None,
    ) -> models.InviteOrganizationMemberResponse:
        """
        This API is used to invite a member.
        """
        
        kwargs = {}
        kwargs["action"] = "InviteOrganizationMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InviteOrganizationMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListExternalSAMLIdPCertificates(
            self,
            request: models.ListExternalSAMLIdPCertificatesRequest,
            opts: Dict = None,
    ) -> models.ListExternalSAMLIdPCertificatesResponse:
        """
        This API is used to query the SAML signing certificate list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListExternalSAMLIdPCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListExternalSAMLIdPCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListGroupMembers(
            self,
            request: models.ListGroupMembersRequest,
            opts: Dict = None,
    ) -> models.ListGroupMembersResponse:
        """
        This API is used to query the user list of the user group.
        """
        
        kwargs = {}
        kwargs["action"] = "ListGroupMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListGroupMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListGroups(
            self,
            request: models.ListGroupsRequest,
            opts: Dict = None,
    ) -> models.ListGroupsResponse:
        """
        This API is used to query the user group list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListJoinedGroupsForUser(
            self,
            request: models.ListJoinedGroupsForUserRequest,
            opts: Dict = None,
    ) -> models.ListJoinedGroupsForUserResponse:
        """
        This API is used to query the user group joined by users.
        """
        
        kwargs = {}
        kwargs["action"] = "ListJoinedGroupsForUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListJoinedGroupsForUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrgServiceAssignMember(
            self,
            request: models.ListOrgServiceAssignMemberRequest,
            opts: Dict = None,
    ) -> models.ListOrgServiceAssignMemberResponse:
        """
        This API is used to obtain the list of delegated admins of the organization service.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrgServiceAssignMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrgServiceAssignMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationIdentity(
            self,
            request: models.ListOrganizationIdentityRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationIdentityResponse:
        """
        This API is used to get the list of access identities of an organization member.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationService(
            self,
            request: models.ListOrganizationServiceRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationServiceResponse:
        """
        This API is used to obtain the list of organization service settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListPermissionPoliciesInRoleConfiguration(
            self,
            request: models.ListPermissionPoliciesInRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.ListPermissionPoliciesInRoleConfigurationResponse:
        """
        This API is used to obtain the policy list in permission configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ListPermissionPoliciesInRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListPermissionPoliciesInRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRoleAssignments(
            self,
            request: models.ListRoleAssignmentsRequest,
            opts: Dict = None,
    ) -> models.ListRoleAssignmentsResponse:
        """
        This API is used to query the authorization list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRoleAssignments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRoleAssignmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRoleConfigurationProvisionings(
            self,
            request: models.ListRoleConfigurationProvisioningsRequest,
            opts: Dict = None,
    ) -> models.ListRoleConfigurationProvisioningsResponse:
        """
        This API is used to query the permission configuration deployment list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRoleConfigurationProvisionings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRoleConfigurationProvisioningsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRoleConfigurations(
            self,
            request: models.ListRoleConfigurationsRequest,
            opts: Dict = None,
    ) -> models.ListRoleConfigurationsResponse:
        """
        This API is used to query the permission configuration list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRoleConfigurations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRoleConfigurationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSCIMCredentials(
            self,
            request: models.ListSCIMCredentialsRequest,
            opts: Dict = None,
    ) -> models.ListSCIMCredentialsResponse:
        """
        This API is used to query the user SCIM key list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSCIMCredentials"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSCIMCredentialsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTasks(
            self,
            request: models.ListTasksRequest,
            opts: Dict = None,
    ) -> models.ListTasksResponse:
        """
        This API is used to query the async task list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUserSyncProvisionings(
            self,
            request: models.ListUserSyncProvisioningsRequest,
            opts: Dict = None,
    ) -> models.ListUserSyncProvisioningsResponse:
        """
        This API is used to query the CAM user synchronization list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUserSyncProvisionings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUserSyncProvisioningsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsers(
            self,
            request: models.ListUsersRequest,
            opts: Dict = None,
    ) -> models.ListUsersResponse:
        """
        This API is used to query the user list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MoveOrganizationNodeMembers(
            self,
            request: models.MoveOrganizationNodeMembersRequest,
            opts: Dict = None,
    ) -> models.MoveOrganizationNodeMembersResponse:
        """
        This API is used to move a member to the specified organization node.
        """
        
        kwargs = {}
        kwargs["action"] = "MoveOrganizationNodeMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MoveOrganizationNodeMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenIdentityCenter(
            self,
            request: models.OpenIdentityCenterRequest,
            opts: Dict = None,
    ) -> models.OpenIdentityCenterResponse:
        """
        This API is used to activate Identity Center service (CIC).
        """
        
        kwargs = {}
        kwargs["action"] = "OpenIdentityCenter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenIdentityCenterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProvisionRoleConfiguration(
            self,
            request: models.ProvisionRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.ProvisionRoleConfigurationResponse:
        """
        This API is used to deploy permission configurations on member accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "ProvisionRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProvisionRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuitOrganization(
            self,
            request: models.QuitOrganizationRequest,
            opts: Dict = None,
    ) -> models.QuitOrganizationResponse:
        """
        This API is used to exit an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "QuitOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuitOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RejectJoinShareUnitInvitation(
            self,
            request: models.RejectJoinShareUnitInvitationRequest,
            opts: Dict = None,
    ) -> models.RejectJoinShareUnitInvitationResponse:
        """
        This API is used to reject an invitation to join a shared unit.
        """
        
        kwargs = {}
        kwargs["action"] = "RejectJoinShareUnitInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RejectJoinShareUnitInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveExternalSAMLIdPCertificate(
            self,
            request: models.RemoveExternalSAMLIdPCertificateRequest,
            opts: Dict = None,
    ) -> models.RemoveExternalSAMLIdPCertificateResponse:
        """
        This API is used to remove SAML signing certificates.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveExternalSAMLIdPCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveExternalSAMLIdPCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemovePermissionPolicyFromRoleConfiguration(
            self,
            request: models.RemovePermissionPolicyFromRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.RemovePermissionPolicyFromRoleConfigurationResponse:
        """
        This API is used to remove policies from permission configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "RemovePermissionPolicyFromRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemovePermissionPolicyFromRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveUserFromGroup(
            self,
            request: models.RemoveUserFromGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveUserFromGroupResponse:
        """
        This API is used to removes users from a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveUserFromGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveUserFromGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendOrgMemberAccountBindEmail(
            self,
            request: models.SendOrgMemberAccountBindEmailRequest,
            opts: Dict = None,
    ) -> models.SendOrgMemberAccountBindEmailResponse:
        """
        This API is used to resend an email for activating the member's bound mailbox.
        """
        
        kwargs = {}
        kwargs["action"] = "SendOrgMemberAccountBindEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendOrgMemberAccountBindEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetExternalSAMLIdentityProvider(
            self,
            request: models.SetExternalSAMLIdentityProviderRequest,
            opts: Dict = None,
    ) -> models.SetExternalSAMLIdentityProviderResponse:
        """
        This API is used to configure the SAML identity provider information.
        """
        
        kwargs = {}
        kwargs["action"] = "SetExternalSAMLIdentityProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetExternalSAMLIdentityProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCustomPolicyForRoleConfiguration(
            self,
            request: models.UpdateCustomPolicyForRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.UpdateCustomPolicyForRoleConfigurationResponse:
        """
        This API is used to modify a custom policy for permission configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCustomPolicyForRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCustomPolicyForRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGroup(
            self,
            request: models.UpdateGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateGroupResponse:
        """
        This API is used to modify user group information.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationIdentity(
            self,
            request: models.UpdateOrganizationIdentityRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationIdentityResponse:
        """
        This API is used to update an organization identity.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationMember(
            self,
            request: models.UpdateOrganizationMemberRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationMemberResponse:
        """
        This API is used to update organization member information.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationMemberEmailBind(
            self,
            request: models.UpdateOrganizationMemberEmailBindRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationMemberEmailBindResponse:
        """
        This API is used to modify the mailbox of a bound member.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationMemberEmailBind"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationMemberEmailBindResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationNode(
            self,
            request: models.UpdateOrganizationNodeRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationNodeResponse:
        """
        This API is used to update an organization node.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRoleConfiguration(
            self,
            request: models.UpdateRoleConfigurationRequest,
            opts: Dict = None,
    ) -> models.UpdateRoleConfigurationResponse:
        """
        This API is used to modify the permission configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRoleConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRoleConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSCIMCredentialStatus(
            self,
            request: models.UpdateSCIMCredentialStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateSCIMCredentialStatusResponse:
        """
        This API is used to enable or disable a SCIM key.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSCIMCredentialStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSCIMCredentialStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSCIMSynchronizationStatus(
            self,
            request: models.UpdateSCIMSynchronizationStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateSCIMSynchronizationStatusResponse:
        """
        This API is used to enable or disable user SCIM synchronization.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSCIMSynchronizationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSCIMSynchronizationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateShareUnit(
            self,
            request: models.UpdateShareUnitRequest,
            opts: Dict = None,
    ) -> models.UpdateShareUnitResponse:
        """
        This API is used to update a shared unit.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateShareUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateShareUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUser(
            self,
            request: models.UpdateUserRequest,
            opts: Dict = None,
    ) -> models.UpdateUserResponse:
        """
        This API is used to modify user information.
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
        This API is used to modify the user status.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserSyncProvisioning(
            self,
            request: models.UpdateUserSyncProvisioningRequest,
            opts: Dict = None,
    ) -> models.UpdateUserSyncProvisioningResponse:
        """
        This API is used to create sub-user synchronization tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserSyncProvisioning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserSyncProvisioningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateZone(
            self,
            request: models.UpdateZoneRequest,
            opts: Dict = None,
    ) -> models.UpdateZoneResponse:
        """
        This API is used to update the user's space name.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)