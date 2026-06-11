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
        
    async def ConfigureMNGPreview(
            self,
            request: models.ConfigureMNGPreviewRequest,
            opts: Dict = None,
    ) -> models.ConfigureMNGPreviewResponse:
        """
        This API is used to configure the preview of a mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "ConfigureMNGPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfigureMNGPreviewResponse
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
        This API is used to create a superapp.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationConfig(
            self,
            request: models.CreateApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationConfigResponse:
        """
        This API is used to create the configuration for a specified superapp.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationSensitiveAPI(
            self,
            request: models.CreateApplicationSensitiveAPIRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationSensitiveAPIResponse:
        """
        This API is used to create a superapp sensitive API.
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
        
    async def CreateMNG(
            self,
            request: models.CreateMNGRequest,
            opts: Dict = None,
    ) -> models.CreateMNGResponse:
        """
        This API is used to create a mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNG"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNGResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNGAppSecret(
            self,
            request: models.CreateMNGAppSecretRequest,
            opts: Dict = None,
    ) -> models.CreateMNGAppSecretResponse:
        """
        This API is used to generate a mini game secret key.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNGAppSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNGAppSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNGApproval(
            self,
            request: models.CreateMNGApprovalRequest,
            opts: Dict = None,
    ) -> models.CreateMNGApprovalResponse:
        """
        This API is used to create a mini game approval request.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNGApproval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNGApprovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNGDomainACL(
            self,
            request: models.CreateMNGDomainACLRequest,
            opts: Dict = None,
    ) -> models.CreateMNGDomainACLResponse:
        """
        This API is used to create a domain allowlist/blocklist for a mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNGDomainACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNGDomainACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNGSensitiveAPIPermissionApproval(
            self,
            request: models.CreateMNGSensitiveAPIPermissionApprovalRequest,
            opts: Dict = None,
    ) -> models.CreateMNGSensitiveAPIPermissionApprovalResponse:
        """
        This API is used to create a permission request to allow a mini game to call sensitive APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNGSensitiveAPIPermissionApproval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNGSensitiveAPIPermissionApprovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNGSubscribeMessageTemplate(
            self,
            request: models.CreateMNGSubscribeMessageTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateMNGSubscribeMessageTemplateResponse:
        """
        This API is used to create a mini game subscription message template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNGSubscribeMessageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNGSubscribeMessageTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNGVersion(
            self,
            request: models.CreateMNGVersionRequest,
            opts: Dict = None,
    ) -> models.CreateMNGVersionResponse:
        """
        This API is used to create a mini game version.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNGVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNGVersionResponse
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
        
    async def CreateMNPAppSecret(
            self,
            request: models.CreateMNPAppSecretRequest,
            opts: Dict = None,
    ) -> models.CreateMNPAppSecretResponse:
        """
        This API is used to generate a mini program secret key.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNPAppSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNPAppSecretResponse
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
        This API is used to create a domain allowlist/blocklist for a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNPDomainACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNPDomainACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMNPSecretKey(
            self,
            request: models.CreateMNPSecretKeyRequest,
            opts: Dict = None,
    ) -> models.CreateMNPSecretKeyResponse:
        """
        This API is used to create a package secret key for a mini program or mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNPSecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNPSecretKeyResponse
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
        
    async def CreateMNPSubscribeMessageTemplate(
            self,
            request: models.CreateMNPSubscribeMessageTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateMNPSubscribeMessageTemplateResponse:
        """
        This API is used to create a mini program subscription message template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMNPSubscribeMessageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMNPSubscribeMessageTemplateResponse
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
        This API is used to delete a superapp.
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
        This API is used to delete a superapp sensitive API.
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
        
    async def DeleteMNG(
            self,
            request: models.DeleteMNGRequest,
            opts: Dict = None,
    ) -> models.DeleteMNGResponse:
        """
        This API is used to delete a mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMNG"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMNGResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMNGSubscribeMessageTemplate(
            self,
            request: models.DeleteMNGSubscribeMessageTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteMNGSubscribeMessageTemplateResponse:
        """
        This API is used to delete a mini game subscription message template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMNGSubscribeMessageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMNGSubscribeMessageTemplateResponse
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
        
    async def DeleteMNPSubscribeMessageTemplate(
            self,
            request: models.DeleteMNPSubscribeMessageTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteMNPSubscribeMessageTemplateResponse:
        """
        This API is used to delete a mini program subscription message template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMNPSubscribeMessageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMNPSubscribeMessageTemplateResponse
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
        
    async def DescribeAPPDataDetailLineChart(
            self,
            request: models.DescribeAPPDataDetailLineChartRequest,
            opts: Dict = None,
    ) -> models.DescribeAPPDataDetailLineChartResponse:
        """
        This API is used to query the line chart data for selected superapp metrics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAPPDataDetailLineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAPPDataDetailLineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAPPDataOverview(
            self,
            request: models.DescribeAPPDataOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeAPPDataOverviewResponse:
        """
        This API is used to query the data overview for the selected superapp metrics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAPPDataOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAPPDataOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAdvertisingLineChart(
            self,
            request: models.DescribeAdvertisingLineChartRequest,
            opts: Dict = None,
    ) -> models.DescribeAdvertisingLineChartResponse:
        """
        This API is used to query the advertising line chart data for a mini program within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAdvertisingLineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAdvertisingLineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAdvertisingOverview(
            self,
            request: models.DescribeAdvertisingOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeAdvertisingOverviewResponse:
        """
        This API is used to query the mini program advertising overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAdvertisingOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAdvertisingOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplication(
            self,
            request: models.DescribeApplicationRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationResponse:
        """
        This API is used to query the superapp details.
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
        This API is used to query the configuration files of a superapp.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationConfigFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationConfigFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationConfigInfos(
            self,
            request: models.DescribeApplicationConfigInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationConfigInfosResponse:
        """
        This API is used to query the superapp configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationConfigInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationConfigInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationList(
            self,
            request: models.DescribeApplicationListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationListResponse:
        """
        This API is used to query a list of superapps.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationMNPList(
            self,
            request: models.DescribeApplicationMNPListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationMNPListResponse:
        """
        This API is used to query the mini program or mini game list associated with a superapp.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationMNPList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationMNPListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationSensitiveAPIList(
            self,
            request: models.DescribeApplicationSensitiveAPIListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationSensitiveAPIListResponse:
        """
        This API is used to query a list of superapp sensitive APIs.
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
        
    async def DescribeGlobalOverviewDataSummary(
            self,
            request: models.DescribeGlobalOverviewDataSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalOverviewDataSummaryResponse:
        """
        This API is used to query the data summary for the global overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalOverviewDataSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalOverviewDataSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalOverviewReportDetail(
            self,
            request: models.DescribeGlobalOverviewReportDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalOverviewReportDetailResponse:
        """
        This API is used to query the detailed report data for global overview within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalOverviewReportDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalOverviewReportDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNG(
            self,
            request: models.DescribeMNGRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGResponse:
        """
        This API is used to query the mini game details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNG"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGAccessAnalysisDetail(
            self,
            request: models.DescribeMNGAccessAnalysisDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGAccessAnalysisDetailResponse:
        """
        This API is used to query the detailed visit analysis data for a mini game within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGAccessAnalysisDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGAccessAnalysisDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGAccessAnalysisLineChart(
            self,
            request: models.DescribeMNGAccessAnalysisLineChartRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGAccessAnalysisLineChartResponse:
        """
        This API is used to query the mini game visit analysis line chart.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGAccessAnalysisLineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGAccessAnalysisLineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGAccessAnalysisOverview(
            self,
            request: models.DescribeMNGAccessAnalysisOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGAccessAnalysisOverviewResponse:
        """
        This API is used to query an overview of visit analysis data for a mini game within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGAccessAnalysisOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGAccessAnalysisOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGActiveUserRealTimeStatistics(
            self,
            request: models.DescribeMNGActiveUserRealTimeStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGActiveUserRealTimeStatisticsResponse:
        """
        This API is used to query the mini game real-time active user statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGActiveUserRealTimeStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGActiveUserRealTimeStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGAdvertisingDetail(
            self,
            request: models.DescribeMNGAdvertisingDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGAdvertisingDetailResponse:
        """
        This API is used to query the detailed mini game advertising data over a specified period.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGAdvertisingDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGAdvertisingDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGAdvertisingLineChart(
            self,
            request: models.DescribeMNGAdvertisingLineChartRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGAdvertisingLineChartResponse:
        """
        This API is used to query the mini game advertising data in a line chart format.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGAdvertisingLineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGAdvertisingLineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGAdvertisingOverview(
            self,
            request: models.DescribeMNGAdvertisingOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGAdvertisingOverviewResponse:
        """
        This API is used to query an overview of mini game ad metrics within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGAdvertisingOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGAdvertisingOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGAllStageVersions(
            self,
            request: models.DescribeMNGAllStageVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGAllStageVersionsResponse:
        """
        This API is used to query mini game version information across all phases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGAllStageVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGAllStageVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGAppSecret(
            self,
            request: models.DescribeMNGAppSecretRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGAppSecretResponse:
        """
        This API is used to query mini game secret keys.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGAppSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGAppSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGCategory(
            self,
            request: models.DescribeMNGCategoryRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGCategoryResponse:
        """
        This API is used to query the mini game categories.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGDomainACL(
            self,
            request: models.DescribeMNGDomainACLRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGDomainACLResponse:
        """
        This API is used to query the domain name allowlist/blocklist of a mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGDomainACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGDomainACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGList(
            self,
            request: models.DescribeMNGListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGListResponse:
        """
        This API is used to query the list of mini games.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGMAUDataDetail(
            self,
            request: models.DescribeMNGMAUDataDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGMAUDataDetailResponse:
        """
        This API is used to query the detailed mini game monthly active user data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGMAUDataDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGMAUDataDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGMAULineChart(
            self,
            request: models.DescribeMNGMAULineChartRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGMAULineChartResponse:
        """
        This API is used to query the mini game MAU line chart.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGMAULineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGMAULineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGMAUMonthlyComparisonMetricCard(
            self,
            request: models.DescribeMNGMAUMonthlyComparisonMetricCardRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGMAUMonthlyComparisonMetricCardResponse:
        """
        This API is used to query the MAU comparison data for a mini game between two months.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGMAUMonthlyComparisonMetricCard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGMAUMonthlyComparisonMetricCardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGOfflinePackageURL(
            self,
            request: models.DescribeMNGOfflinePackageURLRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGOfflinePackageURLResponse:
        """
        This API is used to query the download URL of the mini game package.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGOfflinePackageURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGOfflinePackageURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGPaymentLineChart(
            self,
            request: models.DescribeMNGPaymentLineChartRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGPaymentLineChartResponse:
        """
        This API is used to query the mini game payment line chart.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGPaymentLineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGPaymentLineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGPaymentOverview(
            self,
            request: models.DescribeMNGPaymentOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGPaymentOverviewResponse:
        """
        This API is used to query an overview of mini game payment data within a specified period.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGPaymentOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGPaymentOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGPaymentReportDetail(
            self,
            request: models.DescribeMNGPaymentReportDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGPaymentReportDetailResponse:
        """
        This API is used to query a detailed payment report data for a mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGPaymentReportDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGPaymentReportDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGPaymentRetentionAnalysis(
            self,
            request: models.DescribeMNGPaymentRetentionAnalysisRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGPaymentRetentionAnalysisResponse:
        """
        This API is used to query the mini game payment retention data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGPaymentRetentionAnalysis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGPaymentRetentionAnalysisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGPreview(
            self,
            request: models.DescribeMNGPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGPreviewResponse:
        """
        This API is used to query the mini game preview details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGReleasedVersionHistory(
            self,
            request: models.DescribeMNGReleasedVersionHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGReleasedVersionHistoryResponse:
        """
        This API is used to query the release version history of a mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGReleasedVersionHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGReleasedVersionHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGRetentionData(
            self,
            request: models.DescribeMNGRetentionDataRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGRetentionDataResponse:
        """
        This API is used to query the user retention data for a mini game within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGRetentionData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGRetentionDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGSensitiveAPIPermissionApproval(
            self,
            request: models.DescribeMNGSensitiveAPIPermissionApprovalRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGSensitiveAPIPermissionApprovalResponse:
        """
        This API is used to query the details of permission requests to allow a mini game to call sensitive APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGSensitiveAPIPermissionApproval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGSensitiveAPIPermissionApprovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGSensitiveAPIPermissionList(
            self,
            request: models.DescribeMNGSensitiveAPIPermissionListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGSensitiveAPIPermissionListResponse:
        """
        This API is used to query a list of sensitive APIs that are available to the mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGSensitiveAPIPermissionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGSensitiveAPIPermissionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGSubscribeMessageTemplate(
            self,
            request: models.DescribeMNGSubscribeMessageTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGSubscribeMessageTemplateResponse:
        """
        This API is used to query mini game subscription message template details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGSubscribeMessageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGSubscribeMessageTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGSubscribeMessageTemplateLibrary(
            self,
            request: models.DescribeMNGSubscribeMessageTemplateLibraryRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGSubscribeMessageTemplateLibraryResponse:
        """
        This API is used to query mini game subscription message template library details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGSubscribeMessageTemplateLibrary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGSubscribeMessageTemplateLibraryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGSubscribeMessageTemplateLibraryList(
            self,
            request: models.DescribeMNGSubscribeMessageTemplateLibraryListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGSubscribeMessageTemplateLibraryListResponse:
        """
        This API is used to query the mini game subscription message template library list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGSubscribeMessageTemplateLibraryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGSubscribeMessageTemplateLibraryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGSubscribeMessageTemplateList(
            self,
            request: models.DescribeMNGSubscribeMessageTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGSubscribeMessageTemplateListResponse:
        """
        This API is used to query the mini game subscription message template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGSubscribeMessageTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGSubscribeMessageTemplateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNGVersion(
            self,
            request: models.DescribeMNGVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeMNGVersionResponse:
        """
        This API is used to query the mini game version creation results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNGVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNGVersionResponse
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
        
    async def DescribeMNPAccessAnalysisOverview(
            self,
            request: models.DescribeMNPAccessAnalysisOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPAccessAnalysisOverviewResponse:
        """
        This API is used to query the overview of mini program visit analysis data within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPAccessAnalysisOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPAccessAnalysisOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPActiveUserRealTimeStatistics(
            self,
            request: models.DescribeMNPActiveUserRealTimeStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPActiveUserRealTimeStatisticsResponse:
        """
        This API is used to query the mini program real-time active user statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPActiveUserRealTimeStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPActiveUserRealTimeStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPAdvertisingDetail(
            self,
            request: models.DescribeMNPAdvertisingDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPAdvertisingDetailResponse:
        """
        This API is used to query the detailed advertising data for a mini program within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPAdvertisingDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPAdvertisingDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPAllStageVersions(
            self,
            request: models.DescribeMNPAllStageVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPAllStageVersionsResponse:
        """
        This API is used to query mini program version information across all phases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPAllStageVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPAllStageVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPAppSecret(
            self,
            request: models.DescribeMNPAppSecretRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPAppSecretResponse:
        """
        This API is used to query mini program secret keys.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPAppSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPAppSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPApprovalList(
            self,
            request: models.DescribeMNPApprovalListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPApprovalListResponse:
        """
        This API is used to query a list of approval requests related with a mini program.
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
        This API is used to query the mini program category list.
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
        This API is used to query the domain allowlist/blocklist of a mini program.
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
        This API is used to query the mini program list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPMAUDataDetail(
            self,
            request: models.DescribeMNPMAUDataDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPMAUDataDetailResponse:
        """
        This API is used to query the detailed mini program monthly active user data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPMAUDataDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPMAUDataDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPMAULineChart(
            self,
            request: models.DescribeMNPMAULineChartRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPMAULineChartResponse:
        """
        This API is used to query the mini program monthly active user data in a line chart format.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPMAULineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPMAULineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPMAUMetricCard(
            self,
            request: models.DescribeMNPMAUMetricCardRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPMAUMetricCardResponse:
        """
        This API is used to query the MAU comparison data for a mini program between two months.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPMAUMetricCard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPMAUMetricCardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPOfflinePackageURL(
            self,
            request: models.DescribeMNPOfflinePackageURLRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPOfflinePackageURLResponse:
        """
        This API is used to query the download URL of the mini program package.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPOfflinePackageURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPOfflinePackageURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPPageAnalysisDetail(
            self,
            request: models.DescribeMNPPageAnalysisDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPPageAnalysisDetailResponse:
        """
        This API is used to query the detailed mini program page visit data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPPageAnalysisDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPPageAnalysisDetailResponse
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
        This API is used to query the release version history of a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPReleasedVersionHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPReleasedVersionHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPReportDataLineChart(
            self,
            request: models.DescribeMNPReportDataLineChartRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPReportDataLineChartResponse:
        """
        This API is used to query the mini program visit analysis line chart within a given date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPReportDataLineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPReportDataLineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPReportDetail(
            self,
            request: models.DescribeMNPReportDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPReportDetailResponse:
        """
        This API is used to query the detailed mini program visit analysis data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPReportDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPReportDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPRetentionData(
            self,
            request: models.DescribeMNPRetentionDataRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPRetentionDataResponse:
        """
        This API is used to query the mini program user retention data within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPRetentionData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPRetentionDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPSensitiveAPIPermissionApproval(
            self,
            request: models.DescribeMNPSensitiveAPIPermissionApprovalRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPSensitiveAPIPermissionApprovalResponse:
        """
        This API is used to query the details of a sensitive API permission request for a mini program.
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
        This API is used to query a list of permission requests to allow a mini program to call sensitive APIs.
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
        
    async def DescribeMNPSubscribeMessageTemplate(
            self,
            request: models.DescribeMNPSubscribeMessageTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPSubscribeMessageTemplateResponse:
        """
        This API is used to query mini program subscription message template details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPSubscribeMessageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPSubscribeMessageTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPSubscribeMessageTemplateLibrary(
            self,
            request: models.DescribeMNPSubscribeMessageTemplateLibraryRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPSubscribeMessageTemplateLibraryResponse:
        """
        This API is used to query mini program subscription message template library details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPSubscribeMessageTemplateLibrary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPSubscribeMessageTemplateLibraryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPSubscribeMessageTemplateLibraryList(
            self,
            request: models.DescribeMNPSubscribeMessageTemplateLibraryListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPSubscribeMessageTemplateLibraryListResponse:
        """
        This API is used to query the mini program subscription message template library list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPSubscribeMessageTemplateLibraryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPSubscribeMessageTemplateLibraryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMNPSubscribeMessageTemplateList(
            self,
            request: models.DescribeMNPSubscribeMessageTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeMNPSubscribeMessageTemplateListResponse:
        """
        This API is used to query the mini program subscription message template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMNPSubscribeMessageTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMNPSubscribeMessageTemplateListResponse
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
        
    async def DescribePaymentDataDetail(
            self,
            request: models.DescribePaymentDataDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePaymentDataDetailResponse:
        """
        This API is used to query the mini program payment data details within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePaymentDataDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePaymentDataDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePaymentDataLineChart(
            self,
            request: models.DescribePaymentDataLineChartRequest,
            opts: Dict = None,
    ) -> models.DescribePaymentDataLineChartResponse:
        """
        This API is used to query the mini program payment line chart within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePaymentDataLineChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePaymentDataLineChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePaymentDataOverview(
            self,
            request: models.DescribePaymentDataOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribePaymentDataOverviewResponse:
        """
        This API is used to query an overview of mini program payment data within a specified date range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePaymentDataOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePaymentDataOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoleList(
            self,
            request: models.DescribeRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeRoleListResponse:
        """
        This API is used to query a list of roles.
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
        This API is used to query a list of teams.
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
        This API is used to query a list of team members.
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
        This API is used to query a list of users.
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
        This API is used to disable a superapp sensitive API.
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
        This API is used to enable a superapp sensitive API.
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
        This API is used to change the superapp information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationConfig(
            self,
            request: models.ModifyApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationConfigResponse:
        """
        This API is used to edit the configuration of a superapp.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationConfigResponse
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
        
    async def ModifyMNG(
            self,
            request: models.ModifyMNGRequest,
            opts: Dict = None,
    ) -> models.ModifyMNGResponse:
        """
        This API is used to edit the mini game information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMNG"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMNGResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMNGAppSecretStatus(
            self,
            request: models.ModifyMNGAppSecretStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyMNGAppSecretStatusResponse:
        """
        This API is used to modify the secret key status of a mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMNGAppSecretStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMNGAppSecretStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMNGDomain(
            self,
            request: models.ModifyMNGDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyMNGDomainResponse:
        """
        This API is used to edit the mini game domain information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMNGDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMNGDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMNP(
            self,
            request: models.ModifyMNPRequest,
            opts: Dict = None,
    ) -> models.ModifyMNPResponse:
        """
        This API is used to edit the mini program information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMNP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMNPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMNPAppSecretStatus(
            self,
            request: models.ModifyMNPAppSecretStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyMNPAppSecretStatusResponse:
        """
        This API is used to modify the secret key status of a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMNPAppSecretStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMNPAppSecretStatusResponse
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
        This API is used to process mini program approval requests.
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
        This API is used to process a sensitive API permission request for a mini program.
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMNPSensitiveAPIPermissionApproval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMNPSensitiveAPIPermissionApprovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseMNGVersion(
            self,
            request: models.ReleaseMNGVersionRequest,
            opts: Dict = None,
    ) -> models.ReleaseMNGVersionResponse:
        """
        This API is used to release a mini game version.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseMNGVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseMNGVersionResponse
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
        
    async def RemoveMNG(
            self,
            request: models.RemoveMNGRequest,
            opts: Dict = None,
    ) -> models.RemoveMNGResponse:
        """
        This API is used to remove a mini game.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveMNG"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveMNGResponse
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
        
    async def ResetMNGAppSecret(
            self,
            request: models.ResetMNGAppSecretRequest,
            opts: Dict = None,
    ) -> models.ResetMNGAppSecretResponse:
        """
        This API is used to reset a mini game secret key.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetMNGAppSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetMNGAppSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetMNPAppSecret(
            self,
            request: models.ResetMNPAppSecretRequest,
            opts: Dict = None,
    ) -> models.ResetMNPAppSecretResponse:
        """
        This API is used to reset a mini program secret key.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetMNPAppSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetMNPAppSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackMNGVersion(
            self,
            request: models.RollbackMNGVersionRequest,
            opts: Dict = None,
    ) -> models.RollbackMNGVersionResponse:
        """
        This API is used to roll back the released version of a mini game to a specified version.
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackMNGVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackMNGVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackMNPVersion(
            self,
            request: models.RollbackMNPVersionRequest,
            opts: Dict = None,
    ) -> models.RollbackMNPVersionResponse:
        """
        This API is used to roll back the released version of a mini program to a specified version.
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackMNPVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackMNPVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)