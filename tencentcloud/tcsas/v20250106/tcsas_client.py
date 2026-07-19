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


    def ApproveMNPPaymentEnable(self, request):
        r"""This API is used to allow the superapp to approve the activation of mini program payment.

        :param request: Request instance for ApproveMNPPaymentEnable.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ApproveMNPPaymentEnableRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ApproveMNPPaymentEnableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApproveMNPPaymentEnable", params, headers=headers)
            response = json.loads(body)
            model = models.ApproveMNPPaymentEnableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApprovePaymentMerchantBinding(self, request):
        r"""This API is used to allow the superapp to approve the payment merchant binding request of a mini program team.

        :param request: Request instance for ApprovePaymentMerchantBinding.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ApprovePaymentMerchantBindingRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ApprovePaymentMerchantBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApprovePaymentMerchantBinding", params, headers=headers)
            response = json.loads(body)
            model = models.ApprovePaymentMerchantBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangePaymentBoundMerchant(self, request):
        r"""This API is used to change the bound payment merchant.

        :param request: Request instance for ChangePaymentBoundMerchant.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ChangePaymentBoundMerchantRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ChangePaymentBoundMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangePaymentBoundMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.ChangePaymentBoundMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfigureMNGPreview(self, request):
        r"""This API is used to configure the preview of a mini game.

        :param request: Request instance for ConfigureMNGPreview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ConfigureMNGPreviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ConfigureMNGPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfigureMNGPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ConfigureMNGPreviewResponse()
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
        r"""This API is used to create a superapp.

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
        r"""This API is used to create a superapp sensitive API.

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


    def CreateMNG(self, request):
        r"""This API is used to create a mini game.

        :param request: Request instance for CreateMNG.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNG", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNGResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNGAppSecret(self, request):
        r"""This API is used to generate a mini game secret key.

        :param request: Request instance for CreateMNGAppSecret.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGAppSecretRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGAppSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNGAppSecret", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNGAppSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNGApproval(self, request):
        r"""This API is used to create a mini game approval request.

        :param request: Request instance for CreateMNGApproval.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGApprovalRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGApprovalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNGApproval", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNGApprovalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNGDomainACL(self, request):
        r"""This API is used to create a domain allowlist/blocklist for a mini game.

        :param request: Request instance for CreateMNGDomainACL.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGDomainACLRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGDomainACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNGDomainACL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNGDomainACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNGSensitiveAPIPermissionApproval(self, request):
        r"""This API is used to create a permission request to allow a mini game to call sensitive APIs.

        :param request: Request instance for CreateMNGSensitiveAPIPermissionApproval.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGSensitiveAPIPermissionApprovalRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGSensitiveAPIPermissionApprovalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNGSensitiveAPIPermissionApproval", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNGSensitiveAPIPermissionApprovalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNGSubscribeMessageTemplate(self, request):
        r"""This API is used to create a mini game subscription message template.

        :param request: Request instance for CreateMNGSubscribeMessageTemplate.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGSubscribeMessageTemplateRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGSubscribeMessageTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNGSubscribeMessageTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNGSubscribeMessageTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNGVersion(self, request):
        r"""This API is used to create a mini game version.

        :param request: Request instance for CreateMNGVersion.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGVersionRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNGVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNGVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNGVersionResponse()
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


    def CreateMNPAppSecret(self, request):
        r"""This API is used to generate a mini program secret key.

        :param request: Request instance for CreateMNPAppSecret.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPAppSecretRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPAppSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNPAppSecret", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNPAppSecretResponse()
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
        r"""This API is used to create a domain allowlist/blocklist for a mini program.

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


    def CreateMNPSecretKey(self, request):
        r"""This API is used to create a package secret key for a mini program or mini game.

        :param request: Request instance for CreateMNPSecretKey.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPSecretKeyRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPSecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNPSecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNPSecretKeyResponse()
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


    def CreateMNPSubscribeMessageTemplate(self, request):
        r"""This API is used to create a mini program subscription message template.

        :param request: Request instance for CreateMNPSubscribeMessageTemplate.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPSubscribeMessageTemplateRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.CreateMNPSubscribeMessageTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNPSubscribeMessageTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNPSubscribeMessageTemplateResponse()
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
        r"""This API is used to delete a superapp.

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
        r"""This API is used to delete a superapp sensitive API.

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


    def DeleteMNG(self, request):
        r"""This API is used to delete a mini game.

        :param request: Request instance for DeleteMNG.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DeleteMNGRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DeleteMNGResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMNG", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMNGResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMNGSubscribeMessageTemplate(self, request):
        r"""This API is used to delete a mini game subscription message template.

        :param request: Request instance for DeleteMNGSubscribeMessageTemplate.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DeleteMNGSubscribeMessageTemplateRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DeleteMNGSubscribeMessageTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMNGSubscribeMessageTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMNGSubscribeMessageTemplateResponse()
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


    def DeleteMNPSubscribeMessageTemplate(self, request):
        r"""This API is used to delete a mini program subscription message template.

        :param request: Request instance for DeleteMNPSubscribeMessageTemplate.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DeleteMNPSubscribeMessageTemplateRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DeleteMNPSubscribeMessageTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMNPSubscribeMessageTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMNPSubscribeMessageTemplateResponse()
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
        r"""This API is used to query the line chart data for selected superapp metrics.

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
        r"""This API is used to query the data overview for the selected superapp metrics.

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
        r"""This API is used to query the advertising line chart data for a mini program within a specified date range.

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
        r"""This API is used to query the mini program advertising overview.

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
        r"""This API is used to query the superapp details.

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
        r"""This API is used to query the configuration files of a superapp.

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
        r"""This API is used to query the superapp configuration information.

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
        r"""This API is used to query a list of superapps.

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


    def DescribeApplicationMNPList(self, request):
        r"""This API is used to query the mini program or mini game list associated with a superapp.

        :param request: Request instance for DescribeApplicationMNPList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationMNPListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeApplicationMNPListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationMNPList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationMNPListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationSensitiveAPIList(self, request):
        r"""This API is used to query a list of superapp sensitive APIs.

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
        r"""This API is used to query the data summary for the global overview.

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
        r"""This API is used to query the detailed report data for global overview within a specified date range.

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


    def DescribeMNG(self, request):
        r"""This API is used to query the mini game details.

        :param request: Request instance for DescribeMNG.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNG", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGAccessAnalysisDetail(self, request):
        r"""This API is used to query the detailed visit analysis data for a mini game within a specified date range.

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
        r"""This API is used to query the mini game visit analysis line chart.

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
        r"""This API is used to query an overview of visit analysis data for a mini game within a specified date range.

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
        r"""This API is used to query the mini game real-time active user statistics.

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
        r"""This API is used to query the detailed mini game advertising data over a specified period.

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
        r"""This API is used to query the mini game advertising data in a line chart format.

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
        r"""This API is used to query an overview of mini game ad metrics within a specified date range.

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


    def DescribeMNGAllStageVersions(self, request):
        r"""This API is used to query mini game version information across all phases.

        :param request: Request instance for DescribeMNGAllStageVersions.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAllStageVersionsRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAllStageVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGAllStageVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGAllStageVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGAppSecret(self, request):
        r"""This API is used to query mini game secret keys.

        :param request: Request instance for DescribeMNGAppSecret.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAppSecretRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGAppSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGAppSecret", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGAppSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGCategory(self, request):
        r"""This API is used to query the mini game categories.

        :param request: Request instance for DescribeMNGCategory.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGCategoryRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGCategory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGDomainACL(self, request):
        r"""This API is used to query the domain name allowlist/blocklist of a mini game.

        :param request: Request instance for DescribeMNGDomainACL.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGDomainACLRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGDomainACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGDomainACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGDomainACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGList(self, request):
        r"""This API is used to query the list of mini games.

        :param request: Request instance for DescribeMNGList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGMAUDataDetail(self, request):
        r"""This API is used to query the detailed mini game monthly active user data.

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
        r"""This API is used to query the mini game MAU line chart.

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
        r"""This API is used to query the MAU comparison data for a mini game between two months.

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


    def DescribeMNGOfflinePackageURL(self, request):
        r"""This API is used to query the download URL of the mini game package.

        :param request: Request instance for DescribeMNGOfflinePackageURL.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGOfflinePackageURLRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGOfflinePackageURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGOfflinePackageURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGOfflinePackageURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGPaymentLineChart(self, request):
        r"""This API is used to query the mini game payment line chart.

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
        r"""This API is used to query an overview of mini game payment data within a specified period.

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
        r"""This API is used to query a detailed payment report data for a mini game.

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
        r"""This API is used to query the mini game payment retention data.

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


    def DescribeMNGPreview(self, request):
        r"""This API is used to query the mini game preview details.

        :param request: Request instance for DescribeMNGPreview.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGPreviewRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGPreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGReleasedVersionHistory(self, request):
        r"""This API is used to query the release version history of a mini game.

        :param request: Request instance for DescribeMNGReleasedVersionHistory.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGReleasedVersionHistoryRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGReleasedVersionHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGReleasedVersionHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGReleasedVersionHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGRetentionData(self, request):
        r"""This API is used to query the user retention data for a mini game within a specified date range.

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


    def DescribeMNGSensitiveAPIPermissionApproval(self, request):
        r"""This API is used to query the details of permission requests to allow a mini game to call sensitive APIs.

        :param request: Request instance for DescribeMNGSensitiveAPIPermissionApproval.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSensitiveAPIPermissionApprovalRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSensitiveAPIPermissionApprovalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGSensitiveAPIPermissionApproval", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGSensitiveAPIPermissionApprovalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGSensitiveAPIPermissionList(self, request):
        r"""This API is used to query a list of sensitive APIs that are available to the mini game.

        :param request: Request instance for DescribeMNGSensitiveAPIPermissionList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSensitiveAPIPermissionListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSensitiveAPIPermissionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGSensitiveAPIPermissionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGSensitiveAPIPermissionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGSubscribeMessageTemplate(self, request):
        r"""This API is used to query mini game subscription message template details.

        :param request: Request instance for DescribeMNGSubscribeMessageTemplate.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSubscribeMessageTemplateRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSubscribeMessageTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGSubscribeMessageTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGSubscribeMessageTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGSubscribeMessageTemplateLibrary(self, request):
        r"""This API is used to query mini game subscription message template library details.

        :param request: Request instance for DescribeMNGSubscribeMessageTemplateLibrary.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSubscribeMessageTemplateLibraryRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSubscribeMessageTemplateLibraryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGSubscribeMessageTemplateLibrary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGSubscribeMessageTemplateLibraryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGSubscribeMessageTemplateLibraryList(self, request):
        r"""This API is used to query the mini game subscription message template library list.

        :param request: Request instance for DescribeMNGSubscribeMessageTemplateLibraryList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSubscribeMessageTemplateLibraryListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSubscribeMessageTemplateLibraryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGSubscribeMessageTemplateLibraryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGSubscribeMessageTemplateLibraryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGSubscribeMessageTemplateList(self, request):
        r"""This API is used to query the mini game subscription message template list.

        :param request: Request instance for DescribeMNGSubscribeMessageTemplateList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSubscribeMessageTemplateListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGSubscribeMessageTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGSubscribeMessageTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGSubscribeMessageTemplateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGVersion(self, request):
        r"""This API is used to query the mini game version creation results.

        :param request: Request instance for DescribeMNGVersion.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGVersionRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGVersionResponse()
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
        r"""This API is used to query the overview of mini program visit analysis data within a specified date range.

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
        r"""This API is used to query the mini program real-time active user statistics.

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
        r"""This API is used to query the detailed advertising data for a mini program within a specified date range.

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
        r"""This API is used to query mini program version information across all phases.

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


    def DescribeMNPAppSecret(self, request):
        r"""This API is used to query mini program secret keys.

        :param request: Request instance for DescribeMNPAppSecret.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPAppSecretRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPAppSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPAppSecret", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPAppSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPApprovalList(self, request):
        r"""This API is used to query a list of approval requests related with a mini program.

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
        r"""This API is used to query the mini program category list.

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
        r"""This API is used to query the domain allowlist/blocklist of a mini program.

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
        r"""This API is used to query the mini program list.

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
        r"""This API is used to query the detailed mini program monthly active user data.

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
        r"""This API is used to query the mini program monthly active user data in a line chart format.

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
        r"""This API is used to query the MAU comparison data for a mini program between two months.

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
        r"""This API is used to query the download URL of the mini program package.

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
        r"""This API is used to query the detailed mini program page visit data.

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


    def DescribeMNPPaymentApprovalInfo(self, request):
        r"""This API is used to query the mini program payment approval information.

        :param request: Request instance for DescribeMNPPaymentApprovalInfo.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPPaymentApprovalInfoRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPPaymentApprovalInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPPaymentApprovalInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPPaymentApprovalInfoResponse()
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
        r"""This API is used to query the release version history of a mini program.

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
        r"""This API is used to query the mini program visit analysis line chart within a given date range.

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
        r"""This API is used to query the detailed mini program visit analysis data.

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
        r"""This API is used to query the mini program user retention data within a specified date range.

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
        r"""This API is used to query the details of a sensitive API permission request for a mini program.

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
        r"""This API is used to query a list of permission requests to allow a mini program to call sensitive APIs.

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


    def DescribeMNPSubscribeMessageTemplate(self, request):
        r"""This API is used to query mini program subscription message template details.

        :param request: Request instance for DescribeMNPSubscribeMessageTemplate.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSubscribeMessageTemplateRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSubscribeMessageTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPSubscribeMessageTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPSubscribeMessageTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPSubscribeMessageTemplateLibrary(self, request):
        r"""This API is used to query mini program subscription message template library details.

        :param request: Request instance for DescribeMNPSubscribeMessageTemplateLibrary.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSubscribeMessageTemplateLibraryRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSubscribeMessageTemplateLibraryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPSubscribeMessageTemplateLibrary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPSubscribeMessageTemplateLibraryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPSubscribeMessageTemplateLibraryList(self, request):
        r"""This API is used to query the mini program subscription message template library list.

        :param request: Request instance for DescribeMNPSubscribeMessageTemplateLibraryList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSubscribeMessageTemplateLibraryListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSubscribeMessageTemplateLibraryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPSubscribeMessageTemplateLibraryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPSubscribeMessageTemplateLibraryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPSubscribeMessageTemplateList(self, request):
        r"""This API is used to query the mini program subscription message template list.

        :param request: Request instance for DescribeMNPSubscribeMessageTemplateList.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSubscribeMessageTemplateListRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPSubscribeMessageTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPSubscribeMessageTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPSubscribeMessageTemplateListResponse()
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
        r"""This API is used to query the mini program payment data details within a specified date range.

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
        r"""This API is used to query the mini program payment line chart within a specified date range.

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
        r"""This API is used to query an overview of mini program payment data within a specified date range.

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
        r"""This API is used to query a list of roles.

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
        r"""This API is used to query a list of teams.

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
        r"""This API is used to query a list of team members.

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
        r"""This API is used to query a list of users.

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
        r"""This API is used to disable a superapp sensitive API.

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


    def DisableMNPPayment(self, request):
        r"""This API is used to allow the superapp to actively disable mini program payment.

        :param request: Request instance for DisableMNPPayment.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DisableMNPPaymentRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DisableMNPPaymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableMNPPayment", params, headers=headers)
            response = json.loads(body)
            model = models.DisableMNPPaymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableApplicationSensitiveAPI(self, request):
        r"""This API is used to enable a superapp sensitive API.

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
        r"""This API is used to change the superapp information.

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


    def ModifyMNG(self, request):
        r"""This API is used to edit the mini game information.

        :param request: Request instance for ModifyMNG.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNGRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNGResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMNG", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMNGResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMNGAppSecretStatus(self, request):
        r"""This API is used to modify the secret key status of a mini game.

        :param request: Request instance for ModifyMNGAppSecretStatus.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNGAppSecretStatusRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNGAppSecretStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMNGAppSecretStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMNGAppSecretStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMNGDomain(self, request):
        r"""This API is used to edit the mini game domain information.

        :param request: Request instance for ModifyMNGDomain.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNGDomainRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNGDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMNGDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMNGDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMNP(self, request):
        r"""This API is used to edit the mini program information.

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


    def ModifyMNPAppSecretStatus(self, request):
        r"""This API is used to modify the secret key status of a mini program.

        :param request: Request instance for ModifyMNPAppSecretStatus.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNPAppSecretStatusRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ModifyMNPAppSecretStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMNPAppSecretStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMNPAppSecretStatusResponse()
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
        r"""This API is used to process mini program approval requests.

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
        r"""This API is used to process a sensitive API permission request for a mini program.

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


    def QueryMNPMerchantInfo(self, request):
        r"""This API is used to query the merchant information of a mini program.

        :param request: Request instance for QueryMNPMerchantInfo.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.QueryMNPMerchantInfoRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.QueryMNPMerchantInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMNPMerchantInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMNPMerchantInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseMNGVersion(self, request):
        r"""This API is used to release a mini game version.

        :param request: Request instance for ReleaseMNGVersion.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ReleaseMNGVersionRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ReleaseMNGVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseMNGVersion", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseMNGVersionResponse()
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


    def RemoveMNG(self, request):
        r"""This API is used to remove a mini game.

        :param request: Request instance for RemoveMNG.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.RemoveMNGRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.RemoveMNGResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveMNG", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveMNGResponse()
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


    def RequestPaymentEnable(self, request):
        r"""This API is used to request the activation of mini program payment.

        :param request: Request instance for RequestPaymentEnable.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.RequestPaymentEnableRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.RequestPaymentEnableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RequestPaymentEnable", params, headers=headers)
            response = json.loads(body)
            model = models.RequestPaymentEnableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RequestPaymentMerchantBinding(self, request):
        r"""This API is used to request the binding of a payment merchant to a team.

        :param request: Request instance for RequestPaymentMerchantBinding.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.RequestPaymentMerchantBindingRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.RequestPaymentMerchantBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RequestPaymentMerchantBinding", params, headers=headers)
            response = json.loads(body)
            model = models.RequestPaymentMerchantBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetMNGAppSecret(self, request):
        r"""This API is used to reset a mini game secret key.

        :param request: Request instance for ResetMNGAppSecret.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ResetMNGAppSecretRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ResetMNGAppSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetMNGAppSecret", params, headers=headers)
            response = json.loads(body)
            model = models.ResetMNGAppSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetMNPAppSecret(self, request):
        r"""This API is used to reset a mini program secret key.

        :param request: Request instance for ResetMNPAppSecret.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.ResetMNPAppSecretRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.ResetMNPAppSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetMNPAppSecret", params, headers=headers)
            response = json.loads(body)
            model = models.ResetMNPAppSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackMNGVersion(self, request):
        r"""This API is used to roll back the released version of a mini game to a specified version.

        :param request: Request instance for RollbackMNGVersion.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.RollbackMNGVersionRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.RollbackMNGVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackMNGVersion", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackMNGVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackMNPVersion(self, request):
        r"""This API is used to roll back the released version of a mini program to a specified version.

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


    def UnbindMNPPaymentMerchant(self, request):
        r"""This API is used to allow a mini program team to actively unbind the payment merchant.

        :param request: Request instance for UnbindMNPPaymentMerchant.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.UnbindMNPPaymentMerchantRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.UnbindMNPPaymentMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindMNPPaymentMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindMNPPaymentMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindPaymentMerchant(self, request):
        r"""This API is used to allow the superapp to actively unbind the payment merchant.

        :param request: Request instance for UnbindPaymentMerchant.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.UnbindPaymentMerchantRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.UnbindPaymentMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindPaymentMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindPaymentMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))