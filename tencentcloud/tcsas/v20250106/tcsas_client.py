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
from tencentcloud.tcsas.v20250106 import models


class TcsasClient(AbstractClient):
    _apiVersion = '2025-01-06'
    _endpoint = 'tcsas.intl.tencentcloudapi.com'
    _service = 'tcsas'


    def AddTeamMember(self, request):
        """This API is used to add a team member.

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
        """This API is used to configure the preview of a mini program.

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
        """This API is used to create an application.

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


    def CreateApplicationSensitiveAPI(self, request):
        """This API is used to create a sensitive API of an application.

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
        """This API is used to create a global domain allowlist or blocklist.

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
        """This API is used to create a mini program.

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
        """This API is used to create a mini program approval request.

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
        """This API is used to add a domain name to the allowlist / blocklist of a mini program.

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
        """This API is used to create a permission request to allow a mini program to call sensitive APIs.

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
        """This API is used to create a mini program version.

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
        """This API is used to obtain the encryption key.

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
        """This API is used to create a team.

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
        """This API is used to create a user.

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
        """This API is used to delete the applications.

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
        """This API is used to delete a sensitive API.

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
        """This API is used to delete domains from the allowlist or blocklist.

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
        """This API is used to delete a mini program.

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
        """This API is used to deletes a team.

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
        """This API is used to delete a team member.

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
        """This API is used to delete a user.

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


    def DescribeApplication(self, request):
        """This API is used to query the application details.

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
        """This API is used to query the configuration files of an application.

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


    def DescribeApplicationList(self, request):
        """This API is used to query the applications.

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
        """This API is used to list sensitive APIs of an application.

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
        """This API is used to query the global domain allowlist and blocklist.

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


    def DescribeMNP(self, request):
        """This API is used to query the mini program details.

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


    def DescribeMNPAllStageVersions(self, request):
        """This API is used to query the mini program version management information.

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
        """This API is used to list the approval requests related with a mini program version.

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
        """This API is used to query the mini program types.

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
        """This API is used to query the domain allowlist / blocklist of a mini program.

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
        """This API is used to query the mini programs.

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


    def DescribeMNPOfflinePackageURL(self, request):
        """DescribeMNPOfflinePackageURL

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


    def DescribeMNPPreview(self, request):
        """This API is used to query the mini program preview details.

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
        """This API is used to list all released versions of a mini program.

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


    def DescribeMNPSensitiveAPIPermissionApproval(self, request):
        """This API is used to query details of a specific permission request to call sensitive APIs.

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
        """This API is used to query permission requests to allow a mini program calling sensitive APIs.

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
        """This API is used to query the list of sensitive APIs that available to a mini program.

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
        """This API is used to query the mini program version creation results.

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


    def DescribeRoleList(self, request):
        """This API is used to query the roles.

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
        """This API is used to query the team details.

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
        """This API is used to query the teams.

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
        """This API is used to query the team members.

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
        """This API is used to obtain a temporary key for file uploads.

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
        """This API is used to query the user details.

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
        """This API is used to query the users.

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
        """This API is used to set a sensitive API to restricted.

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
        """This API is used to set an application sensitive API to public.

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
        """This API is used to change the application information.

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


    def ModifyGlobalDomain(self, request):
        """This API is used to modify the domain allowlist or blocklist.

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
        """This API is used to modify the mini program information.

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
        """This API is used to edit the mini program domain information.

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
        """This API is used to change the team information.

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
        """This API is used to modify the team member information.

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
        """This API is used to modify the user information.

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
        """This API is used to approve or reject the release of a mini program version.

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
        """This API is used to approve or reject the sensitive API permission requests.

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
        """This API is used to release a mini program version.

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
        """This API is used to remove a mini program.

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
        """This API is used to rollback a mini program online version.

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