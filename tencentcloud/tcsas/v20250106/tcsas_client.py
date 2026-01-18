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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tcsas.v20250106 import models


class TcsasClient(AbstractClient):
    _apiVersion = '2025-01-06'
    _endpoint = 'tcsas.intl.tencentcloudapi.com'
    _service = 'tcsas'


    def AddTeamMember(self, request):
        r"""This API is used to add a team member.

        :param request: Request instance for AddTeamMember.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.AddTeamMemberRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.AddTeamMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddTeamMember", params, headers=headers)
            response = json.loads(body)
            model = models.AddTeamMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfigureMNPPreview(self, request):
        r"""This API is used to configure the preview of a mini program.

        :param request: Request instance for ConfigureMNPPreview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ConfigureMNPPreviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ConfigureMNPPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfigureMNPPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ConfigureMNPPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplication(self, request):
        r"""This API is used to create an application.

        :param request: Request instance for CreateApplication.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateApplicationRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplication", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationConfig(self, request):
        r"""This API is used to create the configuration for a specified superapp.

        :param request: Request instance for CreateApplicationConfig.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateApplicationConfigRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationSensitiveAPI(self, request):
        r"""This API is used to create a sensitive API of an application.

        :param request: Request instance for CreateApplicationSensitiveAPI.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateApplicationSensitiveAPIRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateApplicationSensitiveAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationSensitiveAPI", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationSensitiveAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlobalDomainACL(self, request):
        r"""This API is used to create a global domain allowlist or blocklist.

        :param request: Request instance for CreateGlobalDomainACL.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateGlobalDomainACLRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateGlobalDomainACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlobalDomainACL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlobalDomainACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNP(self, request):
        r"""This API is used to create a mini program.

        :param request: Request instance for CreateMNP.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNP", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNPApproval(self, request):
        r"""This API is used to create a mini program approval request.

        :param request: Request instance for CreateMNPApproval.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPApprovalRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPApprovalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNPApproval", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNPApprovalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNPDomainACL(self, request):
        r"""This API is used to add a domain name to the allowlist / blocklist of a mini program.

        :param request: Request instance for CreateMNPDomainACL.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPDomainACLRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPDomainACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNPDomainACL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNPDomainACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNPSensitiveAPIPermissionApproval(self, request):
        r"""This API is used to create a permission request to allow a mini program to call sensitive APIs.

        :param request: Request instance for CreateMNPSensitiveAPIPermissionApproval.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPSensitiveAPIPermissionApprovalRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPSensitiveAPIPermissionApprovalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNPSensitiveAPIPermissionApproval", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNPSensitiveAPIPermissionApprovalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNPVersion(self, request):
        r"""This API is used to create a mini program version.

        :param request: Request instance for CreateMNPVersion.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPVersionRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNPVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNPVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePresetKey(self, request):
        r"""This API is used to obtain the encryption key.

        :param request: Request instance for CreatePresetKey.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreatePresetKeyRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreatePresetKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePresetKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePresetKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTeam(self, request):
        r"""This API is used to create a team.

        :param request: Request instance for CreateTeam.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateTeamRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTeam", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        r"""This API is used to create a user.

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateUserResponse`

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


    def DeleteApplication(self, request):
        r"""This API is used to delete the applications.

        :param request: Request instance for DeleteApplication.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DeleteApplicationRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DeleteApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationSensitiveAPI(self, request):
        r"""This API is used to delete a sensitive API.

        :param request: Request instance for DeleteApplicationSensitiveAPI.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DeleteApplicationSensitiveAPIRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DeleteApplicationSensitiveAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationSensitiveAPI", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationSensitiveAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlobalDomain(self, request):
        r"""This API is used to delete domains from the allowlist or blocklist.

        :param request: Request instance for DeleteGlobalDomain.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DeleteGlobalDomainRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DeleteGlobalDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlobalDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlobalDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMNP(self, request):
        r"""This API is used to delete a mini program.

        :param request: Request instance for DeleteMNP.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DeleteMNPRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DeleteMNPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMNP", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMNPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTeam(self, request):
        r"""This API is used to deletes a team.

        :param request: Request instance for DeleteTeam.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DeleteTeamRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DeleteTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTeam", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTeamMember(self, request):
        r"""This API is used to delete a team member.

        :param request: Request instance for DeleteTeamMember.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DeleteTeamMemberRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DeleteTeamMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTeamMember", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTeamMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUser(self, request):
        r"""This API is used to delete a user.

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DeleteUserResponse`

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


    def DescribeAPPDataDetailLineChart(self, request):
        r"""This API is used to retrieve the line chart data for selected superapp metrics.

        :param request: Request instance for DescribeAPPDataDetailLineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeAPPDataDetailLineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeAPPDataDetailLineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPPDataDetailLineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPPDataDetailLineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAPPDataOverview(self, request):
        r"""This API is used to retrieve an overview of the superapp data.

        :param request: Request instance for DescribeAPPDataOverview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeAPPDataOverviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeAPPDataOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPPDataOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPPDataOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAdvertisingLineChart(self, request):
        r"""This API is used to retrieve the advertising line chart data for a mini program within a specified date range.

        :param request: Request instance for DescribeAdvertisingLineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeAdvertisingLineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeAdvertisingLineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAdvertisingLineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAdvertisingLineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAdvertisingOverview(self, request):
        r"""This API is used to retrieve an overview of mini program ad metrics within a specified date range.

        :param request: Request instance for DescribeAdvertisingOverview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeAdvertisingOverviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeAdvertisingOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAdvertisingOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAdvertisingOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplication(self, request):
        r"""This API is used to query the application details.

        :param request: Request instance for DescribeApplication.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationConfigFile(self, request):
        r"""This API is used to query the configuration files of an application.

        :param request: Request instance for DescribeApplicationConfigFile.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationConfigFileRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationConfigFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationConfigFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationConfigFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationConfigInfos(self, request):
        r"""This API is used to retrieve the configuration details for an superapp.

        :param request: Request instance for DescribeApplicationConfigInfos.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationConfigInfosRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationConfigInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationConfigInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationConfigInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationList(self, request):
        r"""This API is used to query the applications.

        :param request: Request instance for DescribeApplicationList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationSensitiveAPIList(self, request):
        r"""This API is used to list sensitive APIs of an application.

        :param request: Request instance for DescribeApplicationSensitiveAPIList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationSensitiveAPIListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationSensitiveAPIListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationSensitiveAPIList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationSensitiveAPIListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalDomainACL(self, request):
        r"""This API is used to query the global domain allowlist and blocklist.

        :param request: Request instance for DescribeGlobalDomainACL.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeGlobalDomainACLRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeGlobalDomainACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalDomainACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalDomainACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalOverviewDataSummary(self, request):
        r"""This API is used to retrieve a global overview summary of usage statistics.

        :param request: Request instance for DescribeGlobalOverviewDataSummary.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeGlobalOverviewDataSummaryRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeGlobalOverviewDataSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalOverviewDataSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalOverviewDataSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalOverviewReportDetail(self, request):
        r"""This API is used to retrieve the detailed report data for global overview within a specified date range.

        :param request: Request instance for DescribeGlobalOverviewReportDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeGlobalOverviewReportDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeGlobalOverviewReportDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalOverviewReportDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalOverviewReportDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGAccessAnalysisDetail(self, request):
        r"""This API is used to retrieve the detailed visit analysis data for a mini game within a specified date range.

        :param request: Request instance for DescribeMNGAccessAnalysisDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAccessAnalysisDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAccessAnalysisDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGAccessAnalysisDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGAccessAnalysisDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGAccessAnalysisLineChart(self, request):
        r"""This API is used to retrieve line chart analysis data for mini game visits.

        :param request: Request instance for DescribeMNGAccessAnalysisLineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAccessAnalysisLineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAccessAnalysisLineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGAccessAnalysisLineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGAccessAnalysisLineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGAccessAnalysisOverview(self, request):
        r"""This API is used to retrieve an overview of visit analysis data for a mini game within a specified date range.

        :param request: Request instance for DescribeMNGAccessAnalysisOverview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAccessAnalysisOverviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAccessAnalysisOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGAccessAnalysisOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGAccessAnalysisOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGActiveUserRealTimeStatistics(self, request):
        r"""This API is used to retrieve the real-time active user statistics for a mini game.

        :param request: Request instance for DescribeMNGActiveUserRealTimeStatistics.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGActiveUserRealTimeStatisticsRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGActiveUserRealTimeStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGActiveUserRealTimeStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGActiveUserRealTimeStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGAdvertisingDetail(self, request):
        r"""This API is used to retrieve the advertising detailed data for a mini game over a specified period.

        :param request: Request instance for DescribeMNGAdvertisingDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAdvertisingDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAdvertisingDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGAdvertisingDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGAdvertisingDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGAdvertisingLineChart(self, request):
        r"""This API is used to retrieve mini game advertising data in a line chart format.

        :param request: Request instance for DescribeMNGAdvertisingLineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAdvertisingLineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAdvertisingLineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGAdvertisingLineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGAdvertisingLineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGAdvertisingOverview(self, request):
        r"""This API is used to retrieve an overview of mini game ad metrics within a specified date range.

        :param request: Request instance for DescribeMNGAdvertisingOverview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAdvertisingOverviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAdvertisingOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGAdvertisingOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGAdvertisingOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGMAUDataDetail(self, request):
        r"""This API is used to retrieve the detailed mini game monthly active user data.

        :param request: Request instance for DescribeMNGMAUDataDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAUDataDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAUDataDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGMAUDataDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGMAUDataDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGMAULineChart(self, request):
        r"""This API is used to retrieve mini game monthly active user data in a line chart format.

        :param request: Request instance for DescribeMNGMAULineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAULineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAULineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGMAULineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGMAULineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGMAUMonthlyComparisonMetricCard(self, request):
        r"""This API is used to retrieve MAU comparison data for a mini game between two months.

        :param request: Request instance for DescribeMNGMAUMonthlyComparisonMetricCard.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAUMonthlyComparisonMetricCardRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAUMonthlyComparisonMetricCardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGMAUMonthlyComparisonMetricCard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGMAUMonthlyComparisonMetricCardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGPaymentLineChart(self, request):
        r"""This API is used to retrieve the line chart data for mini game payment.

        :param request: Request instance for DescribeMNGPaymentLineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGPaymentLineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGPaymentLineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGPaymentLineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGPaymentLineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGPaymentOverview(self, request):
        r"""This API is used to retrieve an overview of mini game payment data within a specified period.

        :param request: Request instance for DescribeMNGPaymentOverview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGPaymentOverviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGPaymentOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGPaymentOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGPaymentOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGPaymentReportDetail(self, request):
        r"""This API is used to retrieve a detailed payment report data for a mini game.

        :param request: Request instance for DescribeMNGPaymentReportDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGPaymentReportDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGPaymentReportDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGPaymentReportDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGPaymentReportDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGPaymentRetentionAnalysis(self, request):
        r"""This API is used to retrieve the mini game payment retention data.

        :param request: Request instance for DescribeMNGPaymentRetentionAnalysis.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGPaymentRetentionAnalysisRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGPaymentRetentionAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGPaymentRetentionAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGPaymentRetentionAnalysisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGRetentionData(self, request):
        r"""This API is used to retrieve user retention data for a mini game within a specified date range.

        :param request: Request instance for DescribeMNGRetentionData.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGRetentionDataRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGRetentionDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGRetentionData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGRetentionDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNP(self, request):
        r"""This API is used to query the mini program details.

        :param request: Request instance for DescribeMNP.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNP", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPAccessAnalysisOverview(self, request):
        r"""This API is used to retrieve an overview of visit analysis data for a mini program within a specified date range.

        :param request: Request instance for DescribeMNPAccessAnalysisOverview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPAccessAnalysisOverviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPAccessAnalysisOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPAccessAnalysisOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPAccessAnalysisOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPActiveUserRealTimeStatistics(self, request):
        r"""This API is used to retrieve the real-time active user statistics for a mini program.

        :param request: Request instance for DescribeMNPActiveUserRealTimeStatistics.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPActiveUserRealTimeStatisticsRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPActiveUserRealTimeStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPActiveUserRealTimeStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPActiveUserRealTimeStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPAdvertisingDetail(self, request):
        r"""This API is used to retrieve the detailed advertising data for a mini program within a specified date range.

        :param request: Request instance for DescribeMNPAdvertisingDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPAdvertisingDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPAdvertisingDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPAdvertisingDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPAdvertisingDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPAllStageVersions(self, request):
        r"""This API is used to query the mini program version management information.

        :param request: Request instance for DescribeMNPAllStageVersions.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPAllStageVersionsRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPAllStageVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPAllStageVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPAllStageVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPApprovalList(self, request):
        r"""This API is used to list the approval requests related with a mini program version.

        :param request: Request instance for DescribeMNPApprovalList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPApprovalListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPApprovalListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPApprovalList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPApprovalListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPCategory(self, request):
        r"""This API is used to query the mini program types.

        :param request: Request instance for DescribeMNPCategory.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPCategoryRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPCategory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPDomainACL(self, request):
        r"""This API is used to query the domain allowlist / blocklist of a mini program.

        :param request: Request instance for DescribeMNPDomainACL.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPDomainACLRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPDomainACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPDomainACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPDomainACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPList(self, request):
        r"""This API is used to query the mini programs.

        :param request: Request instance for DescribeMNPList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPMAUDataDetail(self, request):
        r"""This API is used to retrieve the detailed mini program monthly active user data.

        :param request: Request instance for DescribeMNPMAUDataDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAUDataDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAUDataDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPMAUDataDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPMAUDataDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPMAULineChart(self, request):
        r"""This API is used to retrieve mini program monthly active user data in a line chart format.

        :param request: Request instance for DescribeMNPMAULineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAULineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAULineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPMAULineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPMAULineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPMAUMetricCard(self, request):
        r"""This API is used to retrieve MAU comparison data for a mini program between two months.

        :param request: Request instance for DescribeMNPMAUMetricCard.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAUMetricCardRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAUMetricCardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPMAUMetricCard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPMAUMetricCardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPOfflinePackageURL(self, request):
        r"""DescribeMNPOfflinePackageURL

        :param request: Request instance for DescribeMNPOfflinePackageURL.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPOfflinePackageURLRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPOfflinePackageURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPOfflinePackageURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPOfflinePackageURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPPageAnalysisDetail(self, request):
        r"""This API is used to retrieve the detailed page visit data for a mini program over a specified period.

        :param request: Request instance for DescribeMNPPageAnalysisDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPPageAnalysisDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPPageAnalysisDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPPageAnalysisDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPPageAnalysisDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPPreview(self, request):
        r"""This API is used to query the mini program preview details.

        :param request: Request instance for DescribeMNPPreview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPPreviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPPreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPReleasedVersionHistory(self, request):
        r"""This API is used to list all released versions of a mini program.

        :param request: Request instance for DescribeMNPReleasedVersionHistory.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPReleasedVersionHistoryRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPReleasedVersionHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPReleasedVersionHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPReleasedVersionHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPReportDataLineChart(self, request):
        r"""This API is used to retrieve the line chart data for mini program visit analysis within a given date range.

        :param request: Request instance for DescribeMNPReportDataLineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPReportDataLineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPReportDataLineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPReportDataLineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPReportDataLineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPReportDetail(self, request):
        r"""This API is used to retrieve the detailed mini program visit analysis data.

        :param request: Request instance for DescribeMNPReportDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPReportDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPReportDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPReportDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPReportDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPRetentionData(self, request):
        r"""This API is used to retrieve user retention data for a mini program within a specified date range.

        :param request: Request instance for DescribeMNPRetentionData.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPRetentionDataRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPRetentionDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPRetentionData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPRetentionDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPSensitiveAPIPermissionApproval(self, request):
        r"""This API is used to query details of a specific permission request to call sensitive APIs.

        :param request: Request instance for DescribeMNPSensitiveAPIPermissionApproval.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionApprovalRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionApprovalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPSensitiveAPIPermissionApproval", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPSensitiveAPIPermissionApprovalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPSensitiveAPIPermissionApprovalList(self, request):
        r"""This API is used to query permission requests to allow a mini program calling sensitive APIs.

        :param request: Request instance for DescribeMNPSensitiveAPIPermissionApprovalList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionApprovalListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionApprovalListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPSensitiveAPIPermissionApprovalList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPSensitiveAPIPermissionApprovalListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPSensitiveAPIPermissionList(self, request):
        r"""This API is used to query the list of sensitive APIs that available to a mini program.

        :param request: Request instance for DescribeMNPSensitiveAPIPermissionList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSensitiveAPIPermissionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPSensitiveAPIPermissionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPSensitiveAPIPermissionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPVersion(self, request):
        r"""This API is used to query the mini program version creation results.

        :param request: Request instance for DescribeMNPVersion.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPVersionRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePaymentDataDetail(self, request):
        r"""This API is used to retrieve the detailed standard payment data for specified  mini programs within a specified date range.

        :param request: Request instance for DescribePaymentDataDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribePaymentDataDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribePaymentDataDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePaymentDataDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePaymentDataDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePaymentDataLineChart(self, request):
        r"""This API is used to retrieve the line chart data related to standard payment for a mini program within a specified date range.

        :param request: Request instance for DescribePaymentDataLineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribePaymentDataLineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribePaymentDataLineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePaymentDataLineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePaymentDataLineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePaymentDataOverview(self, request):
        r"""This API is used to retrieve an overview of mini program payment data within a specified date range.

        :param request: Request instance for DescribePaymentDataOverview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribePaymentDataOverviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribePaymentDataOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePaymentDataOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePaymentDataOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoleList(self, request):
        r"""This API is used to query the roles.

        :param request: Request instance for DescribeRoleList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeRoleListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeRoleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTeam(self, request):
        r"""This API is used to query the team details.

        :param request: Request instance for DescribeTeam.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTeam", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTeamList(self, request):
        r"""This API is used to query the teams.

        :param request: Request instance for DescribeTeamList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTeamList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTeamListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTeamMemberList(self, request):
        r"""This API is used to query the team members.

        :param request: Request instance for DescribeTeamMemberList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamMemberListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeTeamMemberListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTeamMemberList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTeamMemberListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTempSecret4UploadFile2Cos(self, request):
        r"""This API is used to obtain a temporary key for file uploads.

        :param request: Request instance for DescribeTempSecret4UploadFile2Cos.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeTempSecret4UploadFile2CosRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeTempSecret4UploadFile2CosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTempSecret4UploadFile2Cos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTempSecret4UploadFile2CosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUser(self, request):
        r"""This API is used to query the user details.

        :param request: Request instance for DescribeUser.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeUserRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeUserResponse`

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


    def DescribeUserList(self, request):
        r"""This API is used to query the users.

        :param request: Request instance for DescribeUserList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeUserListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableApplicationSensitiveAPI(self, request):
        r"""This API is used to set a sensitive API to restricted.

        :param request: Request instance for DisableApplicationSensitiveAPI.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DisableApplicationSensitiveAPIRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DisableApplicationSensitiveAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableApplicationSensitiveAPI", params, headers=headers)
            response = json.loads(body)
            model = models.DisableApplicationSensitiveAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableApplicationSensitiveAPI(self, request):
        r"""This API is used to set an application sensitive API to public.

        :param request: Request instance for EnableApplicationSensitiveAPI.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.EnableApplicationSensitiveAPIRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.EnableApplicationSensitiveAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableApplicationSensitiveAPI", params, headers=headers)
            response = json.loads(body)
            model = models.EnableApplicationSensitiveAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplication(self, request):
        r"""This API is used to change the application information.

        :param request: Request instance for ModifyApplication.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyApplicationRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationConfig(self, request):
        r"""This API is used to edit the configuration of a superapp.

        :param request: Request instance for ModifyApplicationConfig.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyApplicationConfigRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalDomain(self, request):
        r"""This API is used to modify the domain allowlist or blocklist.

        :param request: Request instance for ModifyGlobalDomain.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyGlobalDomainRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyGlobalDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMNP(self, request):
        r"""This API is used to modify the mini program information.

        :param request: Request instance for ModifyMNP.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNPRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMNP", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMNPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMNPDomain(self, request):
        r"""This API is used to edit the mini program domain information.

        :param request: Request instance for ModifyMNPDomain.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNPDomainRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNPDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMNPDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMNPDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTeam(self, request):
        r"""This API is used to change the team information.

        :param request: Request instance for ModifyTeam.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyTeamRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTeam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTeamMember(self, request):
        r"""This API is used to modify the team member information.

        :param request: Request instance for ModifyTeamMember.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyTeamMemberRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyTeamMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTeamMember", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTeamMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUser(self, request):
        r"""This API is used to modify the user information.

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessMNPApproval(self, request):
        r"""This API is used to approve or reject the release of a mini program version.

        :param request: Request instance for ProcessMNPApproval.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ProcessMNPApprovalRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ProcessMNPApprovalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMNPApproval", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessMNPApprovalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessMNPSensitiveAPIPermissionApproval(self, request):
        r"""This API is used to approve or reject the sensitive API permission requests.

        :param request: Request instance for ProcessMNPSensitiveAPIPermissionApproval.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ProcessMNPSensitiveAPIPermissionApprovalRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ProcessMNPSensitiveAPIPermissionApprovalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMNPSensitiveAPIPermissionApproval", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessMNPSensitiveAPIPermissionApprovalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseMNPVersion(self, request):
        r"""This API is used to release a mini program version.

        :param request: Request instance for ReleaseMNPVersion.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ReleaseMNPVersionRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ReleaseMNPVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseMNPVersion", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseMNPVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveMNP(self, request):
        r"""This API is used to remove a mini program.

        :param request: Request instance for RemoveMNP.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.RemoveMNPRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.RemoveMNPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveMNP", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveMNPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackMNPVersion(self, request):
        r"""This API is used to rollback a mini program online version.

        :param request: Request instance for RollbackMNPVersion.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.RollbackMNPVersionRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.RollbackMNPVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackMNPVersion", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackMNPVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))