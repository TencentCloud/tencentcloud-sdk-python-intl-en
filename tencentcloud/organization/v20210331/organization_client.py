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
    _endpoint = 'organization.tencentcloudapi.com'
    _service = 'organization'


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


    def CreateOrganizationMemberPolicy(self, request):
        """This API is used to create an organization member access policy.

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
        """This API is used to obtain the CAM Identity Center service information.

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
        """This API is used to activate the CIC service.

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