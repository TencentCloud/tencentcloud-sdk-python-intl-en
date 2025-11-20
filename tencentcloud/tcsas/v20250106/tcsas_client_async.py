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
from tencentcloud.tcsas.v20250106 import models
from typing import Dict


class TcsasClient(AbstractClient):
    _apiVersion = '2025-01-06'
    _endpoint = 'tcsas.intl.tencentcloudapi.com'
    _service = 'tcsas'

    async def AddTeamMember(
            self,
            request: models.AddTeamMemberRequest,
            opts: Dict = None,
    ) -> models.AddTeamMemberResponse:
        """
        This API is used to add a team member.
        """
        
        kwargs = {}
        kwargs["action"] = "AddTeamMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddTeamMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfigureMNPPreview(
            self,
            request: models.ConfigureMNPPreviewRequest,
            opts: Dict = None,
    ) -> models.ConfigureMNPPreviewResponse:
        """
        This API is used to configure the preview of a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "ConfigureMNPPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfigureMNPPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplication(
            self,
            request: models.CreateApplicationRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationResponse:
        """
        This API is used to create an application.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationSensitiveAPI(
            self,
            request: models.CreateApplicationSensitiveAPIRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationSensitiveAPIResponse:
        """
        This API is used to create a sensitive API of an application.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationSensitiveAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationSensitiveAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalDomainACL(
            self,
            request: models.CreateGlobalDomainACLRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalDomainACLResponse:
        """
        This API is used to create a global domain allowlist or blocklist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalDomainACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalDomainACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNP(
            self,
            request: models.CreateMNPRequest,
            opts: Dict = None,
    ) -> models.CreateMNPResponse:
        """
        This API is used to create a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNPApproval(
            self,
            request: models.CreateMNPApprovalRequest,
            opts: Dict = None,
    ) -> models.CreateMNPApprovalResponse:
        """
        This API is used to create a mini program approval request.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNPApproval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNPApprovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNPDomainACL(
            self,
            request: models.CreateMNPDomainACLRequest,
            opts: Dict = None,
    ) -> models.CreateMNPDomainACLResponse:
        """
        This API is used to add a domain name to the allowlist / blocklist of a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNPDomainACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNPDomainACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNPSensitiveAPIPermissionApproval(
            self,
            request: models.CreateMNPSensitiveAPIPermissionApprovalRequest,
            opts: Dict = None,
    ) -> models.CreateMNPSensitiveAPIPermissionApprovalResponse:
        """
        This API is used to create a permission request to allow a mini program to call sensitive APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNPSensitiveAPIPermissionApproval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNPSensitiveAPIPermissionApprovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNPVersion(
            self,
            request: models.CreateMNPVersionRequest,
            opts: Dict = None,
    ) -> models.CreateMNPVersionResponse:
        """
        This API is used to create a mini program version.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNPVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNPVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePresetKey(
            self,
            request: models.CreatePresetKeyRequest,
            opts: Dict = None,
    ) -> models.CreatePresetKeyResponse:
        """
        This API is used to obtain the encryption key.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePresetKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePresetKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTeam(
            self,
            request: models.CreateTeamRequest,
            opts: Dict = None,
    ) -> models.CreateTeamResponse:
        """
        This API is used to create a team.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTeam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTeamResponse
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
        
    async def DeleteApplication(
            self,
            request: models.DeleteApplicationRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationResponse:
        """
        This API is used to delete the applications.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationSensitiveAPI(
            self,
            request: models.DeleteApplicationSensitiveAPIRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationSensitiveAPIResponse:
        """
        This API is used to delete a sensitive API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationSensitiveAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationSensitiveAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalDomain(
            self,
            request: models.DeleteGlobalDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalDomainResponse:
        """
        This API is used to delete domains from the allowlist or blocklist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMNP(
            self,
            request: models.DeleteMNPRequest,
            opts: Dict = None,
    ) -> models.DeleteMNPResponse:
        """
        This API is used to delete a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMNP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMNPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTeam(
            self,
            request: models.DeleteTeamRequest,
            opts: Dict = None,
    ) -> models.DeleteTeamResponse:
        """
        This API is used to deletes a team.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTeam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTeamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTeamMember(
            self,
            request: models.DeleteTeamMemberRequest,
            opts: Dict = None,
    ) -> models.DeleteTeamMemberResponse:
        """
        This API is used to delete a team member.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTeamMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTeamMemberResponse
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
        
    async def DescribeApplication(
            self,
            request: models.DescribeApplicationRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationResponse:
        """
        This API is used to query the application details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationConfigFile(
            self,
            request: models.DescribeApplicationConfigFileRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationConfigFileResponse:
        """
        This API is used to query the configuration files of an application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationConfigFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationConfigFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationList(
            self,
            request: models.DescribeApplicationListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationListResponse:
        """
        This API is used to query the applications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationSensitiveAPIList(
            self,
            request: models.DescribeApplicationSensitiveAPIListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationSensitiveAPIListResponse:
        """
        This API is used to list sensitive APIs of an application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationSensitiveAPIList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationSensitiveAPIListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalDomainACL(
            self,
            request: models.DescribeGlobalDomainACLRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalDomainACLResponse:
        """
        This API is used to query the global domain allowlist and blocklist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalDomainACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalDomainACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNP(
            self,
            request: models.DescribeMNPRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPResponse:
        """
        This API is used to query the mini program details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPAllStageVersions(
            self,
            request: models.DescribeMNPAllStageVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPAllStageVersionsResponse:
        """
        This API is used to query the mini program version management information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPAllStageVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPAllStageVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPApprovalList(
            self,
            request: models.DescribeMNPApprovalListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPApprovalListResponse:
        """
        This API is used to list the approval requests related with a mini program version.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPApprovalList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPApprovalListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPCategory(
            self,
            request: models.DescribeMNPCategoryRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPCategoryResponse:
        """
        This API is used to query the mini program types.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPDomainACL(
            self,
            request: models.DescribeMNPDomainACLRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPDomainACLResponse:
        """
        This API is used to query the domain allowlist / blocklist of a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPDomainACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPDomainACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPList(
            self,
            request: models.DescribeMNPListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPListResponse:
        """
        This API is used to query the mini programs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPOfflinePackageURL(
            self,
            request: models.DescribeMNPOfflinePackageURLRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPOfflinePackageURLResponse:
        """
        DescribeMNPOfflinePackageURL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPOfflinePackageURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPOfflinePackageURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPPreview(
            self,
            request: models.DescribeMNPPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPPreviewResponse:
        """
        This API is used to query the mini program preview details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPReleasedVersionHistory(
            self,
            request: models.DescribeMNPReleasedVersionHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPReleasedVersionHistoryResponse:
        """
        This API is used to list all released versions of a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPReleasedVersionHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPReleasedVersionHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPSensitiveAPIPermissionApproval(
            self,
            request: models.DescribeMNPSensitiveAPIPermissionApprovalRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPSensitiveAPIPermissionApprovalResponse:
        """
        This API is used to query details of a specific permission request to call sensitive APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPSensitiveAPIPermissionApproval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPSensitiveAPIPermissionApprovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPSensitiveAPIPermissionApprovalList(
            self,
            request: models.DescribeMNPSensitiveAPIPermissionApprovalListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPSensitiveAPIPermissionApprovalListResponse:
        """
        This API is used to query permission requests to allow a mini program calling sensitive APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPSensitiveAPIPermissionApprovalList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPSensitiveAPIPermissionApprovalListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPSensitiveAPIPermissionList(
            self,
            request: models.DescribeMNPSensitiveAPIPermissionListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPSensitiveAPIPermissionListResponse:
        """
        This API is used to query the list of sensitive APIs that available to a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPSensitiveAPIPermissionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPSensitiveAPIPermissionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPVersion(
            self,
            request: models.DescribeMNPVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPVersionResponse:
        """
        This API is used to query the mini program version creation results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoleList(
            self,
            request: models.DescribeRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeRoleListResponse:
        """
        This API is used to query the roles.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTeam(
            self,
            request: models.DescribeTeamRequest,
            opts: Dict = None,
    ) -> models.DescribeTeamResponse:
        """
        This API is used to query the team details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTeam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTeamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTeamList(
            self,
            request: models.DescribeTeamListRequest,
            opts: Dict = None,
    ) -> models.DescribeTeamListResponse:
        """
        This API is used to query the teams.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTeamList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTeamListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTeamMemberList(
            self,
            request: models.DescribeTeamMemberListRequest,
            opts: Dict = None,
    ) -> models.DescribeTeamMemberListResponse:
        """
        This API is used to query the team members.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTeamMemberList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTeamMemberListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTempSecret4UploadFile2Cos(
            self,
            request: models.DescribeTempSecret4UploadFile2CosRequest,
            opts: Dict = None,
    ) -> models.DescribeTempSecret4UploadFile2CosResponse:
        """
        This API is used to obtain a temporary key for file uploads.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTempSecret4UploadFile2Cos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTempSecret4UploadFile2CosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUser(
            self,
            request: models.DescribeUserRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResponse:
        """
        This API is used to query the user details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserList(
            self,
            request: models.DescribeUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserListResponse:
        """
        This API is used to query the users.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableApplicationSensitiveAPI(
            self,
            request: models.DisableApplicationSensitiveAPIRequest,
            opts: Dict = None,
    ) -> models.DisableApplicationSensitiveAPIResponse:
        """
        This API is used to set a sensitive API to restricted.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableApplicationSensitiveAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableApplicationSensitiveAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableApplicationSensitiveAPI(
            self,
            request: models.EnableApplicationSensitiveAPIRequest,
            opts: Dict = None,
    ) -> models.EnableApplicationSensitiveAPIResponse:
        """
        This API is used to set an application sensitive API to public.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableApplicationSensitiveAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableApplicationSensitiveAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplication(
            self,
            request: models.ModifyApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationResponse:
        """
        This API is used to change the application information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalDomain(
            self,
            request: models.ModifyGlobalDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalDomainResponse:
        """
        This API is used to modify the domain allowlist or blocklist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMNP(
            self,
            request: models.ModifyMNPRequest,
            opts: Dict = None,
    ) -> models.ModifyMNPResponse:
        """
        This API is used to modify the mini program information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMNP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMNPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMNPDomain(
            self,
            request: models.ModifyMNPDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyMNPDomainResponse:
        """
        This API is used to edit the mini program domain information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMNPDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMNPDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTeam(
            self,
            request: models.ModifyTeamRequest,
            opts: Dict = None,
    ) -> models.ModifyTeamResponse:
        """
        This API is used to change the team information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTeam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTeamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTeamMember(
            self,
            request: models.ModifyTeamMemberRequest,
            opts: Dict = None,
    ) -> models.ModifyTeamMemberResponse:
        """
        This API is used to modify the team member information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTeamMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTeamMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUser(
            self,
            request: models.ModifyUserRequest,
            opts: Dict = None,
    ) -> models.ModifyUserResponse:
        """
        This API is used to modify the user information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMNPApproval(
            self,
            request: models.ProcessMNPApprovalRequest,
            opts: Dict = None,
    ) -> models.ProcessMNPApprovalResponse:
        """
        This API is used to approve or reject the release of a mini program version.
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMNPApproval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMNPApprovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMNPSensitiveAPIPermissionApproval(
            self,
            request: models.ProcessMNPSensitiveAPIPermissionApprovalRequest,
            opts: Dict = None,
    ) -> models.ProcessMNPSensitiveAPIPermissionApprovalResponse:
        """
        This API is used to approve or reject the sensitive API permission requests.
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMNPSensitiveAPIPermissionApproval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMNPSensitiveAPIPermissionApprovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseMNPVersion(
            self,
            request: models.ReleaseMNPVersionRequest,
            opts: Dict = None,
    ) -> models.ReleaseMNPVersionResponse:
        """
        This API is used to release a mini program version.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseMNPVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseMNPVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveMNP(
            self,
            request: models.RemoveMNPRequest,
            opts: Dict = None,
    ) -> models.RemoveMNPResponse:
        """
        This API is used to remove a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveMNP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveMNPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackMNPVersion(
            self,
            request: models.RollbackMNPVersionRequest,
            opts: Dict = None,
    ) -> models.RollbackMNPVersionResponse:
        """
        This API is used to rollback a mini program online version.
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackMNPVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackMNPVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)