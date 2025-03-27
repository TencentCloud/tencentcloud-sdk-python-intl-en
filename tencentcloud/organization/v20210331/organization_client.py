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
from tencentcloud.organization.v20210331 import models


class OrganizationClient(AbstractClient):
    _apiVersion = '2021-03-31'
    _endpoint = 'organization.intl.tencentcloudapi.com'
    _service = 'organization'


    def AcceptJoinShareUnitInvitation(self, request):
        """This API is used to accept an invitation to join a shared unit.

        :param request: Request instance for AcceptJoinShareUnitInvitation.
        :type request: :class:`tencentcloud.organization.v20210331.models.AcceptJoinShareUnitInvitationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AcceptJoinShareUnitInvitationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcceptJoinShareUnitInvitation", params, headers=headers)
            response = json.loads(body)
            model = models.AcceptJoinShareUnitInvitationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddExternalSAMLIdPCertificate(self, request):
        """This API is used to add SAML signing certificates.

        :param request: Request instance for AddExternalSAMLIdPCertificate.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddExternalSAMLIdPCertificateRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddExternalSAMLIdPCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddExternalSAMLIdPCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.AddExternalSAMLIdPCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddOrganizationMemberEmail(self, request):
        """This API is used to add an organization member's mailbox.

        :param request: Request instance for AddOrganizationMemberEmail.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddOrganizationMemberEmailRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddOrganizationMemberEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddOrganizationMemberEmail", params, headers=headers)
            response = json.loads(body)
            model = models.AddOrganizationMemberEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddOrganizationNode(self, request):
        """This API is used to add an organization node.

        :param request: Request instance for AddOrganizationNode.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddOrganizationNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddOrganizationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddOrganizationNode", params, headers=headers)
            response = json.loads(body)
            model = models.AddOrganizationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddPermissionPolicyToRoleConfiguration(self, request):
        """This API is used to add policies to permission configurations.

        :param request: Request instance for AddPermissionPolicyToRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddPermissionPolicyToRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddPermissionPolicyToRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddPermissionPolicyToRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.AddPermissionPolicyToRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddShareUnit(self, request):
        """This API is used to create a shared unit.

        :param request: Request instance for AddShareUnit.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddShareUnitRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddShareUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddShareUnit", params, headers=headers)
            response = json.loads(body)
            model = models.AddShareUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddShareUnitMembers(self, request):
        """This API is used to add a shared unit member.

        :param request: Request instance for AddShareUnitMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddShareUnitMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddShareUnitMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddShareUnitMembers", params, headers=headers)
            response = json.loads(body)
            model = models.AddShareUnitMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddShareUnitResources(self, request):
        """This API is used to add resources to a shared unit.

        :param request: Request instance for AddShareUnitResources.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddShareUnitResourcesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddShareUnitResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddShareUnitResources", params, headers=headers)
            response = json.loads(body)
            model = models.AddShareUnitResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddUserToGroup(self, request):
        """This API is used to add users to a user group.

        :param request: Request instance for AddUserToGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddUserToGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddUserToGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUserToGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddUserToGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindOrganizationMemberAuthAccount(self, request):
        """This API is used to bind an organization member to a sub-account of the organization admin.

        :param request: Request instance for BindOrganizationMemberAuthAccount.
        :type request: :class:`tencentcloud.organization.v20210331.models.BindOrganizationMemberAuthAccountRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.BindOrganizationMemberAuthAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindOrganizationMemberAuthAccount", params, headers=headers)
            response = json.loads(body)
            model = models.BindOrganizationMemberAuthAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelOrganizationMemberAuthAccount(self, request):
        """This API is used to unbind an organization member from a sub-account of the organization admin.

        :param request: Request instance for CancelOrganizationMemberAuthAccount.
        :type request: :class:`tencentcloud.organization.v20210331.models.CancelOrganizationMemberAuthAccountRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CancelOrganizationMemberAuthAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelOrganizationMemberAuthAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CancelOrganizationMemberAuthAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearExternalSAMLIdentityProvider(self, request):
        """This API is used to clear the SAML identity provider configuration information.

        :param request: Request instance for ClearExternalSAMLIdentityProvider.
        :type request: :class:`tencentcloud.organization.v20210331.models.ClearExternalSAMLIdentityProviderRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ClearExternalSAMLIdentityProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearExternalSAMLIdentityProvider", params, headers=headers)
            response = json.loads(body)
            model = models.ClearExternalSAMLIdentityProviderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGroup(self, request):
        """This API is used to create user groups.

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrgServiceAssign(self, request):
        """This API is used to add a delegated admin of the organization service.

        :param request: Request instance for CreateOrgServiceAssign.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrgServiceAssignRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrgServiceAssignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrgServiceAssign", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrgServiceAssignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganization(self, request):
        """This API is used to create an organization.

        :param request: Request instance for CreateOrganization.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationIdentity(self, request):
        """This API is used to add an organization identity.

        :param request: Request instance for CreateOrganizationIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMember(self, request):
        """This API is used to create an organization member.

        :param request: Request instance for CreateOrganizationMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMember", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMemberAuthIdentity(self, request):
        """This API is used to add organization member access authorization.

        :param request: Request instance for CreateOrganizationMemberAuthIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberAuthIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberAuthIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMemberAuthIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMemberAuthIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMemberPolicy(self, request):
        """This API is used to create an organization member access authorization policy.

        :param request: Request instance for CreateOrganizationMemberPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMemberPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMemberPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMembersPolicy(self, request):
        """This API is used to create an organization member access policy.

        :param request: Request instance for CreateOrganizationMembersPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMembersPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMembersPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMembersPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMembersPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoleAssignment(self, request):
        """This API is used to grant authorizations on member accounts.

        :param request: Request instance for CreateRoleAssignment.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateRoleAssignmentRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateRoleAssignmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoleAssignment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoleAssignmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoleConfiguration(self, request):
        """This API is used to create permission configurations.

        :param request: Request instance for CreateRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSCIMCredential(self, request):
        """This API is used to create a SCIM key.

        :param request: Request instance for CreateSCIMCredential.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateSCIMCredentialRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateSCIMCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSCIMCredential", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSCIMCredentialResponse()
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
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateUserResponse`

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


    def CreateUserSyncProvisioning(self, request):
        """This API is used to create sub-user synchronization tasks.

        :param request: Request instance for CreateUserSyncProvisioning.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateUserSyncProvisioningRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateUserSyncProvisioningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserSyncProvisioning", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserSyncProvisioningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGroup(self, request):
        """This API is used to delete user groups.

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteGroupResponse`

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


    def DeleteOrgServiceAssign(self, request):
        """This API is used to delete a delegated admin of the organization service.

        :param request: Request instance for DeleteOrgServiceAssign.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrgServiceAssignRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrgServiceAssignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrgServiceAssign", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrgServiceAssignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganization(self, request):
        """This API is used to delete an organization.

        :param request: Request instance for DeleteOrganization.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationIdentity(self, request):
        """This API is used to delete an organization identity.

        :param request: Request instance for DeleteOrganizationIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationMemberAuthIdentity(self, request):
        """This API is used to delete organization member access authorization.

        :param request: Request instance for DeleteOrganizationMemberAuthIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMemberAuthIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMemberAuthIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationMemberAuthIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationMemberAuthIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationMembers(self, request):
        """This API is used to remove a member account from the organization, rather than delete the account.

        :param request: Request instance for DeleteOrganizationMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationMembersPolicy(self, request):
        """This API is used to delete an organization member access policy.

        :param request: Request instance for DeleteOrganizationMembersPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationMembersPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationMembersPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationNodes(self, request):
        """This API is used to batch delete organization nodes.

        :param request: Request instance for DeleteOrganizationNodes.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationNodesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoleAssignment(self, request):
        """This API is used to remove authorizations on member accounts.

        :param request: Request instance for DeleteRoleAssignment.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteRoleAssignmentRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteRoleAssignmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoleAssignment", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoleAssignmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoleConfiguration(self, request):
        """This API is used to delete the permission configuration information.

        :param request: Request instance for DeleteRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSCIMCredential(self, request):
        """This API is used to delete a SCIM key.

        :param request: Request instance for DeleteSCIMCredential.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteSCIMCredentialRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteSCIMCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSCIMCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSCIMCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShareUnit(self, request):
        """This API is used to delete a shared unit.

        :param request: Request instance for DeleteShareUnit.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShareUnit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShareUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShareUnitMembers(self, request):
        """This API is used to delete a shared unit member.

        :param request: Request instance for DeleteShareUnitMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShareUnitMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShareUnitMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShareUnitResources(self, request):
        """This API is used to delete shared unit resources.

        :param request: Request instance for DeleteShareUnitResources.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitResourcesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteShareUnitResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShareUnitResources", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShareUnitResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUser(self, request):
        """This API is used to delete a user.

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserSyncProvisioning(self, request):
        """This API is used to delete sub-user synchronization tasks.

        :param request: Request instance for DeleteUserSyncProvisioning.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteUserSyncProvisioningRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteUserSyncProvisioningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserSyncProvisioning", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserSyncProvisioningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdentityCenter(self, request):
        """This API is used to obtain TCO Identity Center service information.

        :param request: Request instance for DescribeIdentityCenter.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeIdentityCenterRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeIdentityCenterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdentityCenter", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdentityCenterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganization(self, request):
        """This API is used to get the organization information.

        :param request: Request instance for DescribeOrganization.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberAuthAccounts(self, request):
        """This API is used to get the list of sub-accounts bound to an organization member.

        :param request: Request instance for DescribeOrganizationMemberAuthAccounts.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthAccountsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberAuthAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberAuthAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberAuthIdentities(self, request):
        """This API is used to obtain the list of organization member access authorization.

        :param request: Request instance for DescribeOrganizationMemberAuthIdentities.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthIdentitiesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthIdentitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberAuthIdentities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberAuthIdentitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberEmailBind(self, request):
        """This API is used to query detailed information about member mailbox binding.

        :param request: Request instance for DescribeOrganizationMemberEmailBind.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberEmailBindRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberEmailBindResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberEmailBind", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberEmailBindResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberPolicies(self, request):
        """This API is used to get the list of authorization policies of an organization member.

        :param request: Request instance for DescribeOrganizationMemberPolicies.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberPoliciesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMembers(self, request):
        """This API is used to get the list of organization members.

        :param request: Request instance for DescribeOrganizationMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationNodes(self, request):
        """This API is used to get the list of organization nodes.

        :param request: Request instance for DescribeOrganizationNodes.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationNodesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShareAreas(self, request):
        """This API is used to obtain a list of shareable regions.

        :param request: Request instance for DescribeShareAreas.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeShareAreasRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeShareAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShareAreas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShareAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShareUnitMembers(self, request):
        """This API is used to obtain the member list of a shared unit.

        :param request: Request instance for DescribeShareUnitMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShareUnitMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShareUnitMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShareUnitResources(self, request):
        """This API is used to obtain the resource list of a shared unit.

        :param request: Request instance for DescribeShareUnitResources.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitResourcesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShareUnitResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShareUnitResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShareUnits(self, request):
        """This API is used to obtain a list of shared units.

        :param request: Request instance for DescribeShareUnits.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeShareUnitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShareUnits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShareUnitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DismantleRoleConfiguration(self, request):
        """This API is used to undeploy permission configurations on member accounts.

        :param request: Request instance for DismantleRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.DismantleRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DismantleRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DismantleRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DismantleRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetExternalSAMLIdentityProvider(self, request):
        """This API is used to query the SAML identity provider configuration information.

        :param request: Request instance for GetExternalSAMLIdentityProvider.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetExternalSAMLIdentityProviderRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetExternalSAMLIdentityProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetExternalSAMLIdentityProvider", params, headers=headers)
            response = json.loads(body)
            model = models.GetExternalSAMLIdentityProviderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGroup(self, request):
        """This API is used to query the user group information.

        :param request: Request instance for GetGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.GetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetProvisioningTaskStatus(self, request):
        """This API is used to query the status of async tasks of user synchronization.

        :param request: Request instance for GetProvisioningTaskStatus.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetProvisioningTaskStatusRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetProvisioningTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetProvisioningTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetProvisioningTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRoleConfiguration(self, request):
        """This API is used to query the permission configuration information.

        :param request: Request instance for GetRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.GetRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSCIMSynchronizationStatus(self, request):
        """This API is used to query SCIM synchronization status.

        :param request: Request instance for GetSCIMSynchronizationStatus.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetSCIMSynchronizationStatusRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetSCIMSynchronizationStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSCIMSynchronizationStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetSCIMSynchronizationStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskStatus(self, request):
        """This API is used to query the status of async tasks.

        :param request: Request instance for GetTaskStatus.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetTaskStatusRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetUser(self, request):
        """This API is used to query the user information.

        :param request: Request instance for GetUser.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetUserRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUser", params, headers=headers)
            response = json.loads(body)
            model = models.GetUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetUserSyncProvisioning(self, request):
        """This API is used to query the CAM user synchronization.

        :param request: Request instance for GetUserSyncProvisioning.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetUserSyncProvisioningRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetUserSyncProvisioningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUserSyncProvisioning", params, headers=headers)
            response = json.loads(body)
            model = models.GetUserSyncProvisioningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetZoneSAMLServiceProviderInfo(self, request):
        """This API is used to query the SAML service provider configuration information.

        :param request: Request instance for GetZoneSAMLServiceProviderInfo.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetZoneSAMLServiceProviderInfoRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetZoneSAMLServiceProviderInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetZoneSAMLServiceProviderInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetZoneSAMLServiceProviderInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetZoneStatistics(self, request):
        """This API is used to query space statistics.

        :param request: Request instance for GetZoneStatistics.
        :type request: :class:`tencentcloud.organization.v20210331.models.GetZoneStatisticsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.GetZoneStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetZoneStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.GetZoneStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InviteOrganizationMember(self, request):
        """This API is used to invite a member.

        :param request: Request instance for InviteOrganizationMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.InviteOrganizationMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.InviteOrganizationMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InviteOrganizationMember", params, headers=headers)
            response = json.loads(body)
            model = models.InviteOrganizationMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListExternalSAMLIdPCertificates(self, request):
        """This API is used to query the SAML signing certificate list.

        :param request: Request instance for ListExternalSAMLIdPCertificates.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListExternalSAMLIdPCertificatesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListExternalSAMLIdPCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListExternalSAMLIdPCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.ListExternalSAMLIdPCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListGroupMembers(self, request):
        """This API is used to query the user list of the user group.

        :param request: Request instance for ListGroupMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListGroupMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListGroupMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListGroupMembers", params, headers=headers)
            response = json.loads(body)
            model = models.ListGroupMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListGroups(self, request):
        """This API is used to query the user group list.

        :param request: Request instance for ListGroups.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListGroupsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ListGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListJoinedGroupsForUser(self, request):
        """This API is used to query the user group joined by users.

        :param request: Request instance for ListJoinedGroupsForUser.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListJoinedGroupsForUserRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListJoinedGroupsForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListJoinedGroupsForUser", params, headers=headers)
            response = json.loads(body)
            model = models.ListJoinedGroupsForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrgServiceAssignMember(self, request):
        """This API is used to obtain the list of delegated admins of the organization service.

        :param request: Request instance for ListOrgServiceAssignMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListOrgServiceAssignMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListOrgServiceAssignMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrgServiceAssignMember", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrgServiceAssignMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationIdentity(self, request):
        """This API is used to get the list of access identities of an organization member.

        :param request: Request instance for ListOrganizationIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListOrganizationIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListOrganizationIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationService(self, request):
        """This API is used to obtain the list of organization service settings.

        :param request: Request instance for ListOrganizationService.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListOrganizationServiceRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListOrganizationServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationService", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListPermissionPoliciesInRoleConfiguration(self, request):
        """This API is used to obtain the policy list in permission configurations.

        :param request: Request instance for ListPermissionPoliciesInRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListPermissionPoliciesInRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListPermissionPoliciesInRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPermissionPoliciesInRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.ListPermissionPoliciesInRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRoleAssignments(self, request):
        """This API is used to query the authorization list.

        :param request: Request instance for ListRoleAssignments.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListRoleAssignmentsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListRoleAssignmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRoleAssignments", params, headers=headers)
            response = json.loads(body)
            model = models.ListRoleAssignmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRoleConfigurationProvisionings(self, request):
        """This API is used to query the permission configuration deployment list.

        :param request: Request instance for ListRoleConfigurationProvisionings.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListRoleConfigurationProvisioningsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListRoleConfigurationProvisioningsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRoleConfigurationProvisionings", params, headers=headers)
            response = json.loads(body)
            model = models.ListRoleConfigurationProvisioningsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRoleConfigurations(self, request):
        """This API is used to query the permission configuration list.

        :param request: Request instance for ListRoleConfigurations.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListRoleConfigurationsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListRoleConfigurationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRoleConfigurations", params, headers=headers)
            response = json.loads(body)
            model = models.ListRoleConfigurationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSCIMCredentials(self, request):
        """This API is used to query the user SCIM key list.

        :param request: Request instance for ListSCIMCredentials.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListSCIMCredentialsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListSCIMCredentialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSCIMCredentials", params, headers=headers)
            response = json.loads(body)
            model = models.ListSCIMCredentialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTasks(self, request):
        """This API is used to query the async task list.

        :param request: Request instance for ListTasks.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListTasksRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUserSyncProvisionings(self, request):
        """This API is used to query the CAM user synchronization list.

        :param request: Request instance for ListUserSyncProvisionings.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListUserSyncProvisioningsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListUserSyncProvisioningsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUserSyncProvisionings", params, headers=headers)
            response = json.loads(body)
            model = models.ListUserSyncProvisioningsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUsers(self, request):
        """This API is used to query the user list.

        :param request: Request instance for ListUsers.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListUsersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUsers", params, headers=headers)
            response = json.loads(body)
            model = models.ListUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MoveOrganizationNodeMembers(self, request):
        """This API is used to move a member to the specified organization node.

        :param request: Request instance for MoveOrganizationNodeMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.MoveOrganizationNodeMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.MoveOrganizationNodeMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MoveOrganizationNodeMembers", params, headers=headers)
            response = json.loads(body)
            model = models.MoveOrganizationNodeMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenIdentityCenter(self, request):
        """This API is used to activate Identity Center service (CIC).

        :param request: Request instance for OpenIdentityCenter.
        :type request: :class:`tencentcloud.organization.v20210331.models.OpenIdentityCenterRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.OpenIdentityCenterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenIdentityCenter", params, headers=headers)
            response = json.loads(body)
            model = models.OpenIdentityCenterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProvisionRoleConfiguration(self, request):
        """This API is used to deploy permission configurations on member accounts.

        :param request: Request instance for ProvisionRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.ProvisionRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ProvisionRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProvisionRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.ProvisionRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QuitOrganization(self, request):
        """This API is used to exit an organization.

        :param request: Request instance for QuitOrganization.
        :type request: :class:`tencentcloud.organization.v20210331.models.QuitOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.QuitOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QuitOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.QuitOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RejectJoinShareUnitInvitation(self, request):
        """This API is used to reject an invitation to join a shared unit.

        :param request: Request instance for RejectJoinShareUnitInvitation.
        :type request: :class:`tencentcloud.organization.v20210331.models.RejectJoinShareUnitInvitationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.RejectJoinShareUnitInvitationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RejectJoinShareUnitInvitation", params, headers=headers)
            response = json.loads(body)
            model = models.RejectJoinShareUnitInvitationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveExternalSAMLIdPCertificate(self, request):
        """This API is used to remove SAML signing certificates.

        :param request: Request instance for RemoveExternalSAMLIdPCertificate.
        :type request: :class:`tencentcloud.organization.v20210331.models.RemoveExternalSAMLIdPCertificateRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.RemoveExternalSAMLIdPCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveExternalSAMLIdPCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveExternalSAMLIdPCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemovePermissionPolicyFromRoleConfiguration(self, request):
        """This API is used to remove policies from permission configurations.

        :param request: Request instance for RemovePermissionPolicyFromRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.RemovePermissionPolicyFromRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.RemovePermissionPolicyFromRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemovePermissionPolicyFromRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.RemovePermissionPolicyFromRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveUserFromGroup(self, request):
        """This API is used to removes users from a user group.

        :param request: Request instance for RemoveUserFromGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.RemoveUserFromGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.RemoveUserFromGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveUserFromGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveUserFromGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendOrgMemberAccountBindEmail(self, request):
        """This API is used to resend an email for activating the member's bound mailbox.

        :param request: Request instance for SendOrgMemberAccountBindEmail.
        :type request: :class:`tencentcloud.organization.v20210331.models.SendOrgMemberAccountBindEmailRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.SendOrgMemberAccountBindEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendOrgMemberAccountBindEmail", params, headers=headers)
            response = json.loads(body)
            model = models.SendOrgMemberAccountBindEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetExternalSAMLIdentityProvider(self, request):
        """This API is used to configure the SAML identity provider information.

        :param request: Request instance for SetExternalSAMLIdentityProvider.
        :type request: :class:`tencentcloud.organization.v20210331.models.SetExternalSAMLIdentityProviderRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.SetExternalSAMLIdentityProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetExternalSAMLIdentityProvider", params, headers=headers)
            response = json.loads(body)
            model = models.SetExternalSAMLIdentityProviderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCustomPolicyForRoleConfiguration(self, request):
        """This API is used to modify a custom policy for permission configurations.

        :param request: Request instance for UpdateCustomPolicyForRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateCustomPolicyForRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateCustomPolicyForRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCustomPolicyForRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCustomPolicyForRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateGroup(self, request):
        """This API is used to modify user group information.

        :param request: Request instance for UpdateGroup.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateGroupRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationIdentity(self, request):
        """This API is used to update an organization identity.

        :param request: Request instance for UpdateOrganizationIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationMember(self, request):
        """This API is used to update organization member information.

        :param request: Request instance for UpdateOrganizationMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationMember", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationMemberEmailBind(self, request):
        """This API is used to modify the mailbox of a bound member.

        :param request: Request instance for UpdateOrganizationMemberEmailBind.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberEmailBindRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberEmailBindResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationMemberEmailBind", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationMemberEmailBindResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationNode(self, request):
        """This API is used to update an organization node.

        :param request: Request instance for UpdateOrganizationNode.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationNode", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRoleConfiguration(self, request):
        """This API is used to modify the permission configuration information.

        :param request: Request instance for UpdateRoleConfiguration.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateRoleConfigurationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateRoleConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRoleConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRoleConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSCIMCredentialStatus(self, request):
        """This API is used to enable or disable a SCIM key.

        :param request: Request instance for UpdateSCIMCredentialStatus.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateSCIMCredentialStatusRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateSCIMCredentialStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSCIMCredentialStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSCIMCredentialStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSCIMSynchronizationStatus(self, request):
        """This API is used to enable or disable user SCIM synchronization.

        :param request: Request instance for UpdateSCIMSynchronizationStatus.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateSCIMSynchronizationStatusRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateSCIMSynchronizationStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSCIMSynchronizationStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSCIMSynchronizationStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateShareUnit(self, request):
        """This API is used to update a shared unit.

        :param request: Request instance for UpdateShareUnit.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateShareUnitRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateShareUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateShareUnit", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateShareUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUser(self, request):
        """This API is used to modify user information.

        :param request: Request instance for UpdateUser.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateUserRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateUserResponse`

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
        """This API is used to modify the user status.

        :param request: Request instance for UpdateUserStatus.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateUserStatusRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateUserStatusResponse`

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


    def UpdateUserSyncProvisioning(self, request):
        """This API is used to create sub-user synchronization tasks.

        :param request: Request instance for UpdateUserSyncProvisioning.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateUserSyncProvisioningRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateUserSyncProvisioningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserSyncProvisioning", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserSyncProvisioningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateZone(self, request):
        """This API is used to update the user's space name.

        :param request: Request instance for UpdateZone.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateZoneRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateZone", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))