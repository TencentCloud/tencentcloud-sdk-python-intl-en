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
from tencentcloud.tcss.v20201101 import models


class TcssClient(AbstractClient):
    _apiVersion = '2020-11-01'
    _endpoint = 'tcss.intl.tencentcloudapi.com'
    _service = 'tcss'


    def AddAndPublishNetworkFirewallPolicyDetail(self, request):
        """This API is used to create a task to add and publish a network policy in the container network.

        :param request: Request instance for AddAndPublishNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddAndPublishNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddAndPublishNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAndPublishNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.AddAndPublishNetworkFirewallPolicyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddAndPublishNetworkFirewallPolicyYamlDetail(self, request):
        """This API is used to create a task to configure and publish a YAML network policy in the container network.

        :param request: Request instance for AddAndPublishNetworkFirewallPolicyYamlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddAndPublishNetworkFirewallPolicyYamlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddAndPublishNetworkFirewallPolicyYamlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAndPublishNetworkFirewallPolicyYamlDetail", params, headers=headers)
            response = json.loads(body)
            model = models.AddAndPublishNetworkFirewallPolicyYamlDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddAssetImageRegistryRegistryDetail(self, request):
        """This API is used to add the details of an image repository.

        :param request: Request instance for AddAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAssetImageRegistryRegistryDetail", params, headers=headers)
            response = json.loads(body)
            model = models.AddAssetImageRegistryRegistryDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddComplianceAssetPolicySetToWhitelist(self, request):
        """This API is used to ignore the specified asset IDs and check item IDs so as to hide the assets contained in the specified check items.
        `AddCompliancePolicyItemToWhitelist` is the reference API. Except for the input field, others should be the same, and if not, it may be due to the definition.

        :param request: Request instance for AddComplianceAssetPolicySetToWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddComplianceAssetPolicySetToWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddComplianceAssetPolicySetToWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddComplianceAssetPolicySetToWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.AddComplianceAssetPolicySetToWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCompliancePolicyAssetSetToWhitelist(self, request):
        """This API is used to ignore the specified asset IDs and check item IDs so as to hide the assets contained in the specified check items.
        `AddCompliancePolicyItemToWhitelist` is the reference API. Except for the input field, others should be the same, and if not, it may be due to the definition.

        :param request: Request instance for AddCompliancePolicyAssetSetToWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddCompliancePolicyAssetSetToWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddCompliancePolicyAssetSetToWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCompliancePolicyAssetSetToWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.AddCompliancePolicyAssetSetToWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCompliancePolicyItemToWhitelist(self, request):
        """This API is used to add the specified check item IDs to the allowlist so as to hide the failure result.

        :param request: Request instance for AddCompliancePolicyItemToWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddCompliancePolicyItemToWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddCompliancePolicyItemToWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCompliancePolicyItemToWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.AddCompliancePolicyItemToWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddEditAbnormalProcessRule(self, request):
        """This API is used to add or edit an abnormal process policy at runtime.

        :param request: Request instance for AddEditAbnormalProcessRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditAbnormalProcessRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditAbnormalProcessRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditAbnormalProcessRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddEditAbnormalProcessRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddEditAccessControlRule(self, request):
        """This API is used to add or edit an access control policy at runtime.

        :param request: Request instance for AddEditAccessControlRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditAccessControlRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditAccessControlRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditAccessControlRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddEditAccessControlRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddEditImageAutoAuthorizedRule(self, request):
        """This API is used to add or edit an automatic licensing rule for local images.

        :param request: Request instance for AddEditImageAutoAuthorizedRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditImageAutoAuthorizedRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditImageAutoAuthorizedRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditImageAutoAuthorizedRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddEditImageAutoAuthorizedRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddEditReverseShellWhiteList(self, request):
        """This API is used to add or edit an allowed reverse shell at runtime.

        :param request: Request instance for AddEditReverseShellWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditReverseShellWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditReverseShellWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditReverseShellWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.AddEditReverseShellWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddEditRiskSyscallWhiteList(self, request):
        """This API is used to add or edit an allowed high-risk syscall at runtime.

        :param request: Request instance for AddEditRiskSyscallWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditRiskSyscallWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditRiskSyscallWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditRiskSyscallWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.AddEditRiskSyscallWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddEditWarningRules(self, request):
        """This API is used to add or edit an alert policy.

        :param request: Request instance for AddEditWarningRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditWarningRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditWarningRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditWarningRules", params, headers=headers)
            response = json.loads(body)
            model = models.AddEditWarningRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddEscapeWhiteList(self, request):
        """This API is used to add an allowed escape.

        :param request: Request instance for AddEscapeWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEscapeWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEscapeWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEscapeWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.AddEscapeWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddIgnoreVul(self, request):
        """This API is used to add ignored vulnerabilities in a vulnerability scan.

        :param request: Request instance for AddIgnoreVul.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddIgnoreVulRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddIgnoreVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddIgnoreVul", params, headers=headers)
            response = json.loads(body)
            model = models.AddIgnoreVulResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddNetworkFirewallPolicyDetail(self, request):
        """This API is used to create a task to add a network policy in the container network.

        :param request: Request instance for AddNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.AddNetworkFirewallPolicyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddNetworkFirewallPolicyYamlDetail(self, request):
        """This API is used to create a task to add a YAML network policy in the container network.

        :param request: Request instance for AddNetworkFirewallPolicyYamlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddNetworkFirewallPolicyYamlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddNetworkFirewallPolicyYamlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNetworkFirewallPolicyYamlDetail", params, headers=headers)
            response = json.loads(body)
            model = models.AddNetworkFirewallPolicyYamlDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckNetworkFirewallPolicyYaml(self, request):
        """This API is used to create a task to check a YAML network policy in the container network.

        :param request: Request instance for CheckNetworkFirewallPolicyYaml.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CheckNetworkFirewallPolicyYamlRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CheckNetworkFirewallPolicyYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckNetworkFirewallPolicyYaml", params, headers=headers)
            response = json.loads(body)
            model = models.CheckNetworkFirewallPolicyYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckRepeatAssetImageRegistry(self, request):
        """This API is used to check whether an image repository name is duplicated.

        :param request: Request instance for CheckRepeatAssetImageRegistry.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CheckRepeatAssetImageRegistryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CheckRepeatAssetImageRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckRepeatAssetImageRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.CheckRepeatAssetImageRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfirmNetworkFirewallPolicy(self, request):
        """This API is used to create a task to confirm a network policy in the container network.

        :param request: Request instance for ConfirmNetworkFirewallPolicy.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ConfirmNetworkFirewallPolicyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ConfirmNetworkFirewallPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmNetworkFirewallPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmNetworkFirewallPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAbnormalProcessRulesExportJob(self, request):
        """This API is used to export abnormal process rules.

        :param request: Request instance for CreateAbnormalProcessRulesExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAbnormalProcessRulesExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAbnormalProcessRulesExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAbnormalProcessRulesExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAbnormalProcessRulesExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccessControlsRuleExportJob(self, request):
        """This API is used to export file tampering detection rules.

        :param request: Request instance for CreateAccessControlsRuleExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAccessControlsRuleExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAccessControlsRuleExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccessControlsRuleExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccessControlsRuleExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetImageRegistryScanTask(self, request):
        """This API is used to create an image scan task for an image repository.

        :param request: Request instance for CreateAssetImageRegistryScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetImageRegistryScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetImageRegistryScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetImageRegistryScanTaskOneKey(self, request):
        """This API is used to create a quick image scan task for an image repository.

        :param request: Request instance for CreateAssetImageRegistryScanTaskOneKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskOneKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskOneKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetImageRegistryScanTaskOneKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetImageRegistryScanTaskOneKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetImageScanSetting(self, request):
        """This API is used to set an image scan.

        :param request: Request instance for CreateAssetImageScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetImageScanSetting", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetImageScanSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetImageScanTask(self, request):
        """This API is used to create an image scan task.

        :param request: Request instance for CreateAssetImageScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetImageScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetImageScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetImageVirusExportJob(self, request):
        """This API is used to create a task to export the list of trojans in a local image.

        :param request: Request instance for CreateAssetImageVirusExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageVirusExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageVirusExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetImageVirusExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetImageVirusExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCheckComponent(self, request):
        """This API is used to install the check component and create a defender.

        :param request: Request instance for CreateCheckComponent.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateCheckComponentRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateCheckComponentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCheckComponent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCheckComponentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterCheckTask(self, request):
        """This API is used to create a cluster check task to check it for risk items.

        :param request: Request instance for CreateClusterCheckTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateClusterCheckTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateClusterCheckTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterCheckTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterCheckTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateComplianceTask(self, request):
        """This API is used to create a compliance check task for another check triggered at the asset level.

        :param request: Request instance for CreateComplianceTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateComplianceTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateComplianceTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateComplianceTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateComplianceTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateComponentExportJob(self, request):
        """This API is used to export the list of components in a local image.

        :param request: Request instance for CreateComponentExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateComponentExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateComponentExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateComponentExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateComponentExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDefenceVulExportJob(self, request):
        """This API is used to create a task to export vulnerabilities that can be prevented.

        :param request: Request instance for CreateDefenceVulExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateDefenceVulExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateDefenceVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDefenceVulExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDefenceVulExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmergencyVulExportJob(self, request):
        """This API is used to create a task to export emergency vulnerabilities.

        :param request: Request instance for CreateEmergencyVulExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateEmergencyVulExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateEmergencyVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmergencyVulExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmergencyVulExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEscapeEventsExportJob(self, request):
        """This API is used to create a task to asynchronously export escape events.

        :param request: Request instance for CreateEscapeEventsExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateEscapeEventsExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateEscapeEventsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEscapeEventsExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEscapeEventsExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEscapeWhiteListExportJob(self, request):
        """This API is used to create a task to export the allowlist of escapes.

        :param request: Request instance for CreateEscapeWhiteListExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateEscapeWhiteListExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateEscapeWhiteListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEscapeWhiteListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEscapeWhiteListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExportComplianceStatusListJob(self, request):
        """This API is used to create a task to export security compliance information.

        :param request: Request instance for CreateExportComplianceStatusListJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateExportComplianceStatusListJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateExportComplianceStatusListJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExportComplianceStatusListJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExportComplianceStatusListJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHostExportJob(self, request):
        """This API is used to create a task to export the list of servers.

        :param request: Request instance for CreateHostExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateHostExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateHostExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHostExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageExportJob(self, request):
        """This API is used to create an image export task.

        :param request: Request instance for CreateImageExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateImageExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateImageExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateK8sApiAbnormalEventExportJob(self, request):
        """This API is used to create K8sApi abnormal event export jobs.

        :param request: Request instance for CreateK8sApiAbnormalEventExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateK8sApiAbnormalEventExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateK8sApiAbnormalEventExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateK8sApiAbnormalEventExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateK8sApiAbnormalEventExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateK8sApiAbnormalRuleExportJob(self, request):
        """This API is used to export rules of K8sApi exceptions.

        :param request: Request instance for CreateK8sApiAbnormalRuleExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateK8sApiAbnormalRuleExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateK8sApiAbnormalRuleExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateK8sApiAbnormalRuleExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateK8sApiAbnormalRuleExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateK8sApiAbnormalRuleInfo(self, request):
        """This API is used to create K8sApi abnormal event rules.

        :param request: Request instance for CreateK8sApiAbnormalRuleInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateK8sApiAbnormalRuleInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateK8sApiAbnormalRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateK8sApiAbnormalRuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.CreateK8sApiAbnormalRuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkFirewallClusterRefresh(self, request):
        """This API is used to distribute a refresh task in the container network cluster.

        :param request: Request instance for CreateNetworkFirewallClusterRefresh.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallClusterRefreshRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallClusterRefreshResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkFirewallClusterRefresh", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkFirewallClusterRefreshResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkFirewallPolicyDiscover(self, request):
        """This API is used to create a task to sync a network policy from the container network cluster.

        :param request: Request instance for CreateNetworkFirewallPolicyDiscover.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallPolicyDiscoverRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallPolicyDiscoverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkFirewallPolicyDiscover", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkFirewallPolicyDiscoverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkFirewallPublish(self, request):
        """This API is used to create a task to publish a network policy in the container network.

        :param request: Request instance for CreateNetworkFirewallPublish.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallPublishRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallPublishResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkFirewallPublish", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkFirewallPublishResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkFirewallUndoPublish(self, request):
        """This API is used to create a task to revoke a network policy in the container network.

        :param request: Request instance for CreateNetworkFirewallUndoPublish.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallUndoPublishRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallUndoPublishResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkFirewallUndoPublish", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkFirewallUndoPublishResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrModifyPostPayCores(self, request):
        """This API is used to create or edit the upper limit for elastic billing.

        :param request: Request instance for CreateOrModifyPostPayCores.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateOrModifyPostPayCoresRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateOrModifyPostPayCoresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrModifyPostPayCores", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrModifyPostPayCoresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProcessEventsExportJob(self, request):
        """This API is used to create a task to asynchronously export abnormal process events.

        :param request: Request instance for CreateProcessEventsExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateProcessEventsExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateProcessEventsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProcessEventsExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProcessEventsExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRefreshTask(self, request):
        """This API is used to distribute a task to refresh the asset information.

        :param request: Request instance for CreateRefreshTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateRefreshTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateRefreshTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRefreshTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRefreshTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRiskDnsEventExportJob(self, request):
        """This API is used to export malicious request events.

        :param request: Request instance for CreateRiskDnsEventExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateRiskDnsEventExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateRiskDnsEventExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRiskDnsEventExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRiskDnsEventExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSearchTemplate(self, request):
        """This API is used to add a search template.

        :param request: Request instance for CreateSearchTemplate.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateSearchTemplateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateSearchTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSearchTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSearchTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSystemVulExportJob(self, request):
        """This API is used to create a task to export system vulnerabilities.

        :param request: Request instance for CreateSystemVulExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateSystemVulExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateSystemVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSystemVulExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSystemVulExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVirusScanAgain(self, request):
        """This API is used to perform another virus scan at runtime.

        :param request: Request instance for CreateVirusScanAgain.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanAgainRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVirusScanAgain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVirusScanAgainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVirusScanTask(self, request):
        """This API is used to perform a quick virus scan at runtime.

        :param request: Request instance for CreateVirusScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVirusScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVirusScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulContainerExportJob(self, request):
        """This API is used to create a task to export containers affected by vulnerabilities.

        :param request: Request instance for CreateVulContainerExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulContainerExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulContainerExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulContainerExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulContainerExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulDefenceEventExportJob(self, request):
        """This API is used to create an exploit prevention event export task.

        :param request: Request instance for CreateVulDefenceEventExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulDefenceEventExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulDefenceEventExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulDefenceEventExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulDefenceEventExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulDefenceHostExportJob(self, request):
        """This API is used to create a task to export servers with exploit prevention enabled.

        :param request: Request instance for CreateVulDefenceHostExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulDefenceHostExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulDefenceHostExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulDefenceHostExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulDefenceHostExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulExportJob(self, request):
        """This API is used to export the list of vulnerabilities in a local image.

        :param request: Request instance for CreateVulExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulImageExportJob(self, request):
        """This API is used to create a task to export images affected by vulnerabilities.

        :param request: Request instance for CreateVulImageExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulImageExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulImageExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulImageExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulImageExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulScanTask(self, request):
        """This API is used to create a vulnerability scan task.

        :param request: Request instance for CreateVulScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWebVulExportJob(self, request):
        """This API is used to create a task to export web vulnerabilities.

        :param request: Request instance for CreateWebVulExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateWebVulExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateWebVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebVulExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWebVulExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAbnormalProcessRules(self, request):
        """This API is used to delete an abnormal process policy at runtime.

        :param request: Request instance for DeleteAbnormalProcessRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteAbnormalProcessRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteAbnormalProcessRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAbnormalProcessRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAbnormalProcessRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccessControlRules(self, request):
        """This API is used to delete an access control policy at runtime.

        :param request: Request instance for DeleteAccessControlRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteAccessControlRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteAccessControlRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccessControlRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccessControlRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteComplianceAssetPolicySetFromWhitelist(self, request):
        """This API is used to unignore the specified asset IDs and check item IDs so as to show the assets contained in the specified check items.
        `AddCompliancePolicyAssetSetToWhitelist` is the reference API. Except for the input field, others should be the same, and if not, it may be due to the definition.

        :param request: Request instance for DeleteComplianceAssetPolicySetFromWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteComplianceAssetPolicySetFromWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteComplianceAssetPolicySetFromWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteComplianceAssetPolicySetFromWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteComplianceAssetPolicySetFromWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCompliancePolicyAssetSetFromWhitelist(self, request):
        """This API is used to unignore the specified asset IDs and check item IDs so as to show the assets contained in the specified check items.

        :param request: Request instance for DeleteCompliancePolicyAssetSetFromWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteCompliancePolicyAssetSetFromWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteCompliancePolicyAssetSetFromWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCompliancePolicyAssetSetFromWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCompliancePolicyAssetSetFromWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCompliancePolicyItemFromWhitelist(self, request):
        """This API is used to remove the specified check item from the allowlist.

        :param request: Request instance for DeleteCompliancePolicyItemFromWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteCompliancePolicyItemFromWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteCompliancePolicyItemFromWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCompliancePolicyItemFromWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCompliancePolicyItemFromWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEscapeWhiteList(self, request):
        """This API is used to delete an allowed escape.

        :param request: Request instance for DeleteEscapeWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteEscapeWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteEscapeWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEscapeWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEscapeWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIgnoreVul(self, request):
        """This API is used to unignore vulnerabilities in a vulnerability scan.

        :param request: Request instance for DeleteIgnoreVul.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteIgnoreVulRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteIgnoreVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIgnoreVul", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIgnoreVulResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteK8sApiAbnormalRule(self, request):
        """This API is used to delete a K8sApi abnormal event rules.

        :param request: Request instance for DeleteK8sApiAbnormalRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteK8sApiAbnormalRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteK8sApiAbnormalRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteK8sApiAbnormalRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteK8sApiAbnormalRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachine(self, request):
        """This API is used to uninstall the agent.

        :param request: Request instance for DeleteMachine.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteMachineRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetworkFirewallPolicyDetail(self, request):
        """This API is used to create a task to delete a network policy in the container network.

        :param request: Request instance for DeleteNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetworkFirewallPolicyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReverseShellEvents(self, request):
        """This API is used to delete a reverse shell event at runtime.

        :param request: Request instance for DeleteReverseShellEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReverseShellWhiteLists(self, request):
        """This API is used to delete an allowed reverse shell at runtime.

        :param request: Request instance for DeleteReverseShellWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteReverseShellWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteReverseShellWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellWhiteLists", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReverseShellWhiteListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRiskSyscallEvents(self, request):
        """This API is used to delete a high-risk syscall event at runtime.

        :param request: Request instance for DeleteRiskSyscallEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteRiskSyscallEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteRiskSyscallEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskSyscallEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRiskSyscallEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRiskSyscallWhiteLists(self, request):
        """This API is used to delete an allowed high-risk syscall at runtime.

        :param request: Request instance for DeleteRiskSyscallWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteRiskSyscallWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteRiskSyscallWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskSyscallWhiteLists", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRiskSyscallWhiteListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSearchTemplate(self, request):
        """This API is used to delete a search template.

        :param request: Request instance for DeleteSearchTemplate.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteSearchTemplateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteSearchTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSearchTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSearchTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeABTestConfig(self, request):
        """This API is used to get the current canary configuration of the user.

        :param request: Request instance for DescribeABTestConfig.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeABTestConfigRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeABTestConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeABTestConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeABTestConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbnormalProcessDetail(self, request):
        """This API is used to query the details of an abnormal process event at runtime.

        :param request: Request instance for DescribeAbnormalProcessDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbnormalProcessDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbnormalProcessEventTendency(self, request):
        """This API is used to query the trend of pending abnormal process events.

        :param request: Request instance for DescribeAbnormalProcessEventTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessEventTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbnormalProcessEventTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbnormalProcessEvents(self, request):
        """This API is used to query the list of abnormal process events at runtime.

        :param request: Request instance for DescribeAbnormalProcessEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbnormalProcessEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbnormalProcessEventsExport(self, request):
        """接口已废弃

        This API is used to query and export the list of abnormal process events at runtime.

        :param request: Request instance for DescribeAbnormalProcessEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessEventsExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbnormalProcessEventsExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbnormalProcessLevelSummary(self, request):
        """This API is used to count the number of pending abnormal process events at each severity level.

        :param request: Request instance for DescribeAbnormalProcessLevelSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessLevelSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessLevelSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessLevelSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbnormalProcessLevelSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbnormalProcessRuleDetail(self, request):
        """This API is used to query the details of an abnormal process policy at runtime.

        :param request: Request instance for DescribeAbnormalProcessRuleDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRuleDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbnormalProcessRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbnormalProcessRules(self, request):
        """This API is used to query the list of abnormal process policies at runtime.

        :param request: Request instance for DescribeAbnormalProcessRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbnormalProcessRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbnormalProcessRulesExport(self, request):
        """接口已废弃

        This API is used to query and export the list of abnormal process policies at runtime.

        :param request: Request instance for DescribeAbnormalProcessRulesExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessRulesExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbnormalProcessRulesExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessControlDetail(self, request):
        """This API is used to query the details of an access control event at runtime.

        :param request: Request instance for DescribeAccessControlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessControlDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessControlEvents(self, request):
        """This API is used to query the list of access control events at runtime.

        :param request: Request instance for DescribeAccessControlEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessControlEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessControlEventsExport(self, request):
        """This API is used to export the list of access control events at runtime.

        :param request: Request instance for DescribeAccessControlEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlEventsExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessControlEventsExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessControlRuleDetail(self, request):
        """This API is used to query the details of an access control policy at runtime.

        :param request: Request instance for DescribeAccessControlRuleDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRuleDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessControlRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessControlRules(self, request):
        """This API is used to query the list of access control policies at runtime.

        :param request: Request instance for DescribeAccessControlRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessControlRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessControlRulesExport(self, request):
        """接口已废弃

        This API is used to export the list of access control policies at runtime.

        :param request: Request instance for DescribeAccessControlRulesExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlRulesExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessControlRulesExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAffectedClusterCount(self, request):
        """This API is used to get and return the number of affected clusters.

        :param request: Request instance for DescribeAffectedClusterCount.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedClusterCountRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedClusterCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAffectedClusterCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAffectedClusterCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAffectedNodeList(self, request):
        """This API is used to query affected node types and return the node list.

        :param request: Request instance for DescribeAffectedNodeList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedNodeListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedNodeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAffectedNodeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAffectedNodeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAffectedWorkloadList(self, request):
        """This API is used to query affected workload types and return the workload list.

        :param request: Request instance for DescribeAffectedWorkloadList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedWorkloadListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedWorkloadListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAffectedWorkloadList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAffectedWorkloadListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentDaemonSetCmd(self, request):
        """This API is used to query parallel container installation commands.

        :param request: Request instance for DescribeAgentDaemonSetCmd.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAgentDaemonSetCmdRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAgentDaemonSetCmdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentDaemonSetCmd", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentDaemonSetCmdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentInstallCommand(self, request):
        """This API is used to query agent installation commands.

        :param request: Request instance for DescribeAgentInstallCommand.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAgentInstallCommandRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAgentInstallCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentInstallCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentInstallCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetAppServiceList(self, request):
        """This API is used to query the list of application services.

        :param request: Request instance for DescribeAssetAppServiceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetAppServiceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetAppServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetAppServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetAppServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetClusterList(self, request):
        """This API is used to query the list of clusters.

        :param request: Request instance for DescribeAssetClusterList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetClusterListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetClusterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetClusterList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetClusterListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetComponentList(self, request):
        """This API is used to query the list of container components.

        :param request: Request instance for DescribeAssetComponentList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetComponentListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetComponentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetComponentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetContainerDetail(self, request):
        """This API is used to query the information of a container.

        :param request: Request instance for DescribeAssetContainerDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetContainerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetContainerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetContainerList(self, request):
        """This API is used to query the list of containers.

        :param request: Request instance for DescribeAssetContainerList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetContainerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetContainerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDBServiceList(self, request):
        """This API is used to query the list of database services.

        :param request: Request instance for DescribeAssetDBServiceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetDBServiceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetDBServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDBServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDBServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetHostDetail(self, request):
        """This API is used to query the details of a server.

        :param request: Request instance for DescribeAssetHostDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetHostDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetHostDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetHostList(self, request):
        """This API is used to query the list of servers.

        :param request: Request instance for DescribeAssetHostList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageBindRuleInfo(self, request):
        """This API is used to query the list of rules bound to images, including runtime access control and abnormal process rules.

        :param request: Request instance for DescribeAssetImageBindRuleInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageBindRuleInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageBindRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageBindRuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageBindRuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageDetail(self, request):
        """This API is used to query the details of an image.

        :param request: Request instance for DescribeAssetImageDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageHostList(self, request):
        """This API is used to query the servers associated with an image.

        :param request: Request instance for DescribeAssetImageHostList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageHostListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageList(self, request):
        """This API is used to query the list of images.

        :param request: Request instance for DescribeAssetImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageListExport(self, request):
        """接口已废弃

        This API is used to export the list of images.

        :param request: Request instance for DescribeAssetImageListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageListExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageListExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryAssetStatus(self, request):
        """This API is used to view the update progress of the assets in an image repository.

        :param request: Request instance for DescribeAssetImageRegistryAssetStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryAssetStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryAssetStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryAssetStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryAssetStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryDetail(self, request):
        """This API is used to query the image repository details.

        :param request: Request instance for DescribeAssetImageRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryList(self, request):
        """This API is used to query the list of image repositories.

        :param request: Request instance for DescribeAssetImageRegistryList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryListExport(self, request):
        """This API is used to export the list of images for an image repository.

        :param request: Request instance for DescribeAssetImageRegistryListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryListExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryListExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryRegistryDetail(self, request):
        """This API is used to view the details of an image repository.

        :param request: Request instance for DescribeAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryRegistryDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryRegistryDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryRegistryList(self, request):
        """This API is used to query the list of image registries.

        :param request: Request instance for DescribeAssetImageRegistryRegistryList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryRegistryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryRegistryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryRiskInfoList(self, request):
        """This API is used to query the list of image high-risk behaviors of an image repository.

        :param request: Request instance for DescribeAssetImageRegistryRiskInfoList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskInfoListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryRiskInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryRiskInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryRiskListExport(self, request):
        """This API is used to export the list of sensitive data for an image repository.

        :param request: Request instance for DescribeAssetImageRegistryRiskListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryRiskListExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryRiskListExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryScanStatusOneKey(self, request):
        """This API is used to query the quick image scanning status of an image repository.

        :param request: Request instance for DescribeAssetImageRegistryScanStatusOneKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryScanStatusOneKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryScanStatusOneKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryScanStatusOneKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryScanStatusOneKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistrySummary(self, request):
        """This API is used to query the image statistics of an image repository.

        :param request: Request instance for DescribeAssetImageRegistrySummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistrySummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistrySummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistrySummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistrySummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryVirusList(self, request):
        """This API is used to query the list of viruses and trojans in an image repository.

        :param request: Request instance for DescribeAssetImageRegistryVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryVirusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryVirusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryVirusListExport(self, request):
        """This API is used to export the list of trojan information for an image repository.

        :param request: Request instance for DescribeAssetImageRegistryVirusListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryVirusListExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryVirusListExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryVulList(self, request):
        """This API is used to query the list of image vulnerabilities of an image repository

        :param request: Request instance for DescribeAssetImageRegistryVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRegistryVulListExport(self, request):
        """This API is used to export the list of vulnerabilities for an image repository.

        :param request: Request instance for DescribeAssetImageRegistryVulListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryVulListExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRegistryVulListExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRiskList(self, request):
        """This API is used to query the list of risks in an image.

        :param request: Request instance for DescribeAssetImageRiskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageRiskListExport(self, request):
        """This API is used to export the list of risks in an image.

        :param request: Request instance for DescribeAssetImageRiskListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRiskListExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageRiskListExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageScanSetting(self, request):
        """This API is used to get the image scan settings.

        :param request: Request instance for DescribeAssetImageScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageScanSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageScanSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageScanStatus(self, request):
        """This API is used to query the image scanning status.

        :param request: Request instance for DescribeAssetImageScanStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageScanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageScanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageScanTask(self, request):
        """This API is used to query the ID of a running quick image scan task.

        :param request: Request instance for DescribeAssetImageScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageSimpleList(self, request):
        """This API is used to query the brief information list of an image.

        :param request: Request instance for DescribeAssetImageSimpleList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageSimpleListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageSimpleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageSimpleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageSimpleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageVirusList(self, request):
        """This API is used to query the list of viruses in an image.

        :param request: Request instance for DescribeAssetImageVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageVirusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageVirusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageVirusListExport(self, request):
        """This API is used to export the list of trojans in an image.

        :param request: Request instance for DescribeAssetImageVirusListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageVirusListExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageVirusListExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageVulList(self, request):
        """This API is used to query the list of vulnerabilities in an image.

        :param request: Request instance for DescribeAssetImageVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetImageVulListExport(self, request):
        """This API is used to export the list of vulnerabilities in an image.

        :param request: Request instance for DescribeAssetImageVulListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageVulListExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetImageVulListExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetPortList(self, request):
        """This API is used to query the list of occupied ports.

        :param request: Request instance for DescribeAssetPortList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetPortListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetPortListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetPortList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetPortListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetProcessList(self, request):
        """This API is used to query the list of processes.

        :param request: Request instance for DescribeAssetProcessList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetProcessListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetSummary(self, request):
        """This API is used to query the statistics of containers and images under an account.

        :param request: Request instance for DescribeAssetSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetSyncLastTime(self, request):
        """This API is used to query the last asset sync time.

        :param request: Request instance for DescribeAssetSyncLastTime.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetSyncLastTimeRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetSyncLastTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSyncLastTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetSyncLastTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebServiceList(self, request):
        """This API is used to query the list of web services.

        :param request: Request instance for DescribeAssetWebServiceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetWebServiceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetWebServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoAuthorizedRuleHost(self, request):
        """This API is used to query the servers licensed according to an automatic licensing rule.

        :param request: Request instance for DescribeAutoAuthorizedRuleHost.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAutoAuthorizedRuleHostRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAutoAuthorizedRuleHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoAuthorizedRuleHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoAuthorizedRuleHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCheckItemList(self, request):
        """This API is used to query all check items and return the total number and list of check items.

        :param request: Request instance for DescribeCheckItemList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCheckItemListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCheckItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCheckItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCheckItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterDetail(self, request):
        """This API is used to query the details of a cluster.

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterSummary(self, request):
        """This API is used to query the overview of cluster assets.

        :param request: Request instance for DescribeClusterSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceAssetDetailInfo(self, request):
        """This API is used to query the details of an asset.

        :param request: Request instance for DescribeComplianceAssetDetailInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetDetailInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceAssetDetailInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceAssetDetailInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceAssetList(self, request):
        """This API is used to query the list of assets of a certain type.

        :param request: Request instance for DescribeComplianceAssetList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceAssetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceAssetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceAssetPolicyItemList(self, request):
        """This API is used to query the list of check items of an asset.

        :param request: Request instance for DescribeComplianceAssetPolicyItemList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetPolicyItemListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetPolicyItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceAssetPolicyItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceAssetPolicyItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompliancePeriodTaskList(self, request):
        """This API is used to query the list of scheduled tasks.

        :param request: Request instance for DescribeCompliancePeriodTaskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePeriodTaskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePeriodTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompliancePeriodTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompliancePeriodTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompliancePolicyItemAffectedAssetList(self, request):
        """This API is used to apply the asset level in the "check item + asset" two-level structure.

        :param request: Request instance for DescribeCompliancePolicyItemAffectedAssetList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedAssetListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompliancePolicyItemAffectedAssetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompliancePolicyItemAffectedAssetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompliancePolicyItemAffectedSummary(self, request):
        """This API is used to apply the check item level in the "check item + asset" two-level structure.

        :param request: Request instance for DescribeCompliancePolicyItemAffectedSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompliancePolicyItemAffectedSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompliancePolicyItemAffectedSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceScanFailedAssetList(self, request):
        """This API is used to query the aggregate information of the pass rate at the asset level, the first level in the "asset + check item" two-level structure.

        :param request: Request instance for DescribeComplianceScanFailedAssetList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceScanFailedAssetListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceScanFailedAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceScanFailedAssetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceScanFailedAssetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceTaskAssetSummary(self, request):
        """This API is used to query the aggregated information of the asset pass rate in the last task.

        :param request: Request instance for DescribeComplianceTaskAssetSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskAssetSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskAssetSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceTaskAssetSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceTaskAssetSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceTaskPolicyItemSummaryList(self, request):
        """This API is used to query the list of aggregated information of check items identified in the last task in line with the "check item + asset" two-level structure.

        :param request: Request instance for DescribeComplianceTaskPolicyItemSummaryList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskPolicyItemSummaryListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskPolicyItemSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceTaskPolicyItemSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceTaskPolicyItemSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceWhitelistItemList(self, request):
        """This API is used to query the allowlist.

        :param request: Request instance for DescribeComplianceWhitelistItemList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceWhitelistItemListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceWhitelistItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceWhitelistItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceWhitelistItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerAssetSummary(self, request):
        """This API is used to query the asset overview.

        :param request: Request instance for DescribeContainerAssetSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerAssetSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerAssetSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerAssetSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerAssetSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerSecEventSummary(self, request):
        """This API is used to query the overview of pending events.

        :param request: Request instance for DescribeContainerSecEventSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerSecEventSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerSecEventSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerSecEventSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerSecEventSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeESAggregations(self, request):
        """This API is used to get the aggregation result of the ES field.

        :param request: Request instance for DescribeESAggregations.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeESAggregationsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeESAggregationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeESAggregations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeESAggregationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeESHits(self, request):
        """This API is used to get the list of ES query files.

        :param request: Request instance for DescribeESHits.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeESHitsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeESHitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeESHits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeESHitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmergencyVulList(self, request):
        """This API is used to query the list of emergency vulnerabilities.

        :param request: Request instance for DescribeEmergencyVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEmergencyVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEmergencyVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmergencyVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmergencyVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEscapeEventDetail(self, request):
        """This API is used to query the details of a container escape event.

        :param request: Request instance for DescribeEscapeEventDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeEventDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEscapeEventDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEscapeEventInfo(self, request):
        """This API is used to query the list of container escape events.

        :param request: Request instance for DescribeEscapeEventInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEscapeEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEscapeEventTendency(self, request):
        """This API is used to query the trend of pending escape events.

        :param request: Request instance for DescribeEscapeEventTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeEventTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEscapeEventTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEscapeEventTypeSummary(self, request):
        """This API is used to query the types of container escape events and the number of pending events.

        :param request: Request instance for DescribeEscapeEventTypeSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventTypeSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventTypeSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeEventTypeSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEscapeEventTypeSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEscapeEventsExport(self, request):
        """接口已废弃

        This API is used to export the list of container escape events.

        :param request: Request instance for DescribeEscapeEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventsExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeEventsExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEscapeEventsExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEscapeRuleInfo(self, request):
        """This API is used to query the information of a container escape scan rule.

        :param request: Request instance for DescribeEscapeRuleInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeRuleInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeRuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEscapeRuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEscapeSafeState(self, request):
        """This API is used to query the container escape security status.

        :param request: Request instance for DescribeEscapeSafeState.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeSafeStateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeSafeStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeSafeState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEscapeSafeStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEscapeWhiteList(self, request):
        """This API is used to query the allowlist of escapes.

        :param request: Request instance for DescribeEscapeWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEscapeWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportJobDownloadURL(self, request):
        """This API is used to query the URL to download the result of an exportation task.

        :param request: Request instance for DescribeExportJobDownloadURL.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeExportJobDownloadURLRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeExportJobDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportJobDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportJobDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportJobManageList(self, request):
        """This API is used to query the export job management list.

        :param request: Request instance for DescribeExportJobManageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeExportJobManageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeExportJobManageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportJobManageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportJobManageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportJobResult(self, request):
        """This API is used to query the result of an export task.

        :param request: Request instance for DescribeExportJobResult.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeExportJobResultRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeExportJobResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportJobResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportJobResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAuthorizedInfo(self, request):
        """This API is used to query the image licensing information.

        :param request: Request instance for DescribeImageAuthorizedInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAuthorizedInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAuthorizedInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAuthorizedInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAuthorizedInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAutoAuthorizedLogList(self, request):
        """This API is used to query the list of automatic image licensing results.

        :param request: Request instance for DescribeImageAutoAuthorizedLogList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedLogListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAutoAuthorizedLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAutoAuthorizedLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAutoAuthorizedRule(self, request):
        """This API is used to query an automatic licensing rule for local images.

        :param request: Request instance for DescribeImageAutoAuthorizedRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAutoAuthorizedRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAutoAuthorizedRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAutoAuthorizedTaskList(self, request):
        """This API is used to query the list of automatic image licensing tasks.

        :param request: Request instance for DescribeImageAutoAuthorizedTaskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedTaskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAutoAuthorizedTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAutoAuthorizedTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageComponentList(self, request):
        """This API is used to query the list of components in an local image.

        :param request: Request instance for DescribeImageComponentList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageComponentListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageComponentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageComponentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryNamespaceList(self, request):
        """This API is used to query the list of namespaces for an image repository.

        :param request: Request instance for DescribeImageRegistryNamespaceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRegistryNamespaceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRegistryNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryNamespaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryNamespaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryTimingScanTask(self, request):
        """This API is used to view a scheduled task of an image repository.

        :param request: Request instance for DescribeImageRegistryTimingScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRegistryTimingScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRegistryTimingScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryTimingScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryTimingScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRiskSummary(self, request):
        """This API is used to query the overview of local image risks.

        :param request: Request instance for DescribeImageRiskSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRiskSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRiskSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRiskTendency(self, request):
        """This API is used to query the trend of local image risks.

        :param request: Request instance for DescribeImageRiskTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRiskTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRiskTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageSimpleList(self, request):
        """This API is used to query the list of all images.

        :param request: Request instance for DescribeImageSimpleList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageSimpleListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageSimpleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageSimpleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageSimpleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexList(self, request):
        """This API is used to get the index list.

        :param request: Request instance for DescribeIndexList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeIndexListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeIndexListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndexList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIndexListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInspectionReport(self, request):
        """This API is used to query check reports.

        :param request: Request instance for DescribeInspectionReport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeInspectionReportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeInspectionReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInspectionReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInspectionReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeK8sApiAbnormalEventInfo(self, request):
        """Querying details of a K8s API exception event

        :param request: Request instance for DescribeK8sApiAbnormalEventInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalEventInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeK8sApiAbnormalEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeK8sApiAbnormalEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeK8sApiAbnormalEventList(self, request):
        """This API is used to query the K8sApi abnormal event list.

        :param request: Request instance for DescribeK8sApiAbnormalEventList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalEventListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeK8sApiAbnormalEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeK8sApiAbnormalEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeK8sApiAbnormalRuleInfo(self, request):
        """This API is used to query K8sApi abnormal request rule details.

        :param request: Request instance for DescribeK8sApiAbnormalRuleInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalRuleInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeK8sApiAbnormalRuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeK8sApiAbnormalRuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeK8sApiAbnormalRuleList(self, request):
        """This API is used to the K8sApi abnormal request rule list.

        :param request: Request instance for DescribeK8sApiAbnormalRuleList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalRuleListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeK8sApiAbnormalRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeK8sApiAbnormalRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeK8sApiAbnormalRuleScopeList(self, request):
        """This API is used to query rules for K8s API exceptions.

        :param request: Request instance for DescribeK8sApiAbnormalRuleScopeList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalRuleScopeListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalRuleScopeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeK8sApiAbnormalRuleScopeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeK8sApiAbnormalRuleScopeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeK8sApiAbnormalSummary(self, request):
        """This API is used to query the statistics of K8sApi abnormal events.

        :param request: Request instance for DescribeK8sApiAbnormalSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeK8sApiAbnormalSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeK8sApiAbnormalSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeK8sApiAbnormalTendency(self, request):
        """This API is used to query the trend of K8sApi abnormal events.

        :param request: Request instance for DescribeK8sApiAbnormalTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeK8sApiAbnormalTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeK8sApiAbnormalTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeK8sApiAbnormalTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogStorageStatistic(self, request):
        """This API is used to get the statistics of the log search usage.

        :param request: Request instance for DescribeLogStorageStatistic.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeLogStorageStatisticRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeLogStorageStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogStorageStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogStorageStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkFirewallAuditRecord(self, request):
        """This API is used to query the list of cluster policy audits.

        :param request: Request instance for DescribeNetworkFirewallAuditRecord.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallAuditRecordRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallAuditRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallAuditRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkFirewallAuditRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkFirewallClusterList(self, request):
        """This API is used to query the list of clusters.

        :param request: Request instance for DescribeNetworkFirewallClusterList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallClusterListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallClusterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallClusterList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkFirewallClusterListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkFirewallClusterRefreshStatus(self, request):
        """This API is used to query the progress of the asset query task in the container network.

        :param request: Request instance for DescribeNetworkFirewallClusterRefreshStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallClusterRefreshStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallClusterRefreshStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallClusterRefreshStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkFirewallClusterRefreshStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkFirewallNamespaceLabelList(self, request):
        """This API is used to query the list of cluster network namespace labels.

        :param request: Request instance for DescribeNetworkFirewallNamespaceLabelList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallNamespaceLabelListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallNamespaceLabelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallNamespaceLabelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkFirewallNamespaceLabelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkFirewallPodLabelsList(self, request):
        """This API is used to query cluster network Pod labels.

        :param request: Request instance for DescribeNetworkFirewallPodLabelsList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPodLabelsListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPodLabelsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPodLabelsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkFirewallPodLabelsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkFirewallPolicyDetail(self, request):
        """This API is used to view the details of a policy in the container network cluster.

        :param request: Request instance for DescribeNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkFirewallPolicyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkFirewallPolicyDiscover(self, request):
        """This API is used to query the progress of a network policy sync task in the container network.

        :param request: Request instance for DescribeNetworkFirewallPolicyDiscover.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyDiscoverRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyDiscoverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPolicyDiscover", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkFirewallPolicyDiscoverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkFirewallPolicyList(self, request):
        """This API is used to query the list of cluster network policies.

        :param request: Request instance for DescribeNetworkFirewallPolicyList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkFirewallPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkFirewallPolicyStatus(self, request):
        """This API is used to query the execution status of a network policy in the container network.

        :param request: Request instance for DescribeNetworkFirewallPolicyStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkFirewallPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkFirewallPolicyYamlDetail(self, request):
        """This API is used to view the details of a YAML network policy in the container network cluster.

        :param request: Request instance for DescribeNetworkFirewallPolicyYamlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyYamlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyYamlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPolicyYamlDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkFirewallPolicyYamlDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNewestVul(self, request):
        """This API is used to query the latest list of vulnerabilities.

        :param request: Request instance for DescribeNewestVul.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNewestVulRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNewestVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNewestVul", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNewestVulResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePostPayDetail(self, request):
        """This API is used to query the pay-as-you-go billing details.

        :param request: Request instance for DescribePostPayDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribePostPayDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribePostPayDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePostPayDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePostPayDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProVersionInfo(self, request):
        """This API is used to check whether the Pro Edition needs to be purchased.

        :param request: Request instance for DescribeProVersionInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeProVersionInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeProVersionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProVersionInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProVersionInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePromotionActivity(self, request):
        """This API is used to query promotions.

        :param request: Request instance for DescribePromotionActivity.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribePromotionActivityRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribePromotionActivityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePromotionActivity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePromotionActivityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicKey(self, request):
        """This API is used to get the public key.

        :param request: Request instance for DescribePublicKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribePublicKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribePublicKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePurchaseStateInfo(self, request):
        """This API is used to check whether TCSS is purchased.

        :param request: Request instance for DescribePurchaseStateInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribePurchaseStateInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribePurchaseStateInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurchaseStateInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePurchaseStateInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRefreshTask(self, request):
        """This API is used to query a refresh task.

        :param request: Request instance for DescribeRefreshTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRefreshTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRefreshTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRefreshTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRefreshTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellDetail(self, request):
        """This API is used to query the details of a reverse shell event at runtime.

        :param request: Request instance for DescribeReverseShellDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellEvents(self, request):
        """This API is used to query the list of reverse shell events at runtime.

        :param request: Request instance for DescribeReverseShellEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellEventsExport(self, request):
        """This API is used to query and export the list of reverse shell events at runtime.

        :param request: Request instance for DescribeReverseShellEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellEventsExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellEventsExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellWhiteListDetail(self, request):
        """This API is used to query the details of the allowlist of reverse shells at runtime.

        :param request: Request instance for DescribeReverseShellWhiteListDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellWhiteListDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellWhiteListDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellWhiteLists(self, request):
        """This API is used to query the allowlist of reverse shells at runtime.

        :param request: Request instance for DescribeReverseShellWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellWhiteLists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellWhiteListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskList(self, request):
        """This API is used to query the list of risk items identified in the last task and filter them by special field.

        :param request: Request instance for DescribeRiskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskSyscallDetail(self, request):
        """This API is used to query the details of a high-risk syscall event.

        :param request: Request instance for DescribeRiskSyscallDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskSyscallDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskSyscallEvents(self, request):
        """This API is used to query the list of high-risk syscalls at runtime.

        :param request: Request instance for DescribeRiskSyscallEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskSyscallEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskSyscallEventsExport(self, request):
        """This API is used to export the list of high-risk syscalls at runtime.

        :param request: Request instance for DescribeRiskSyscallEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallEventsExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskSyscallEventsExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskSyscallNames(self, request):
        """This API is used to query the list of names of high-risk syscalls at runtime.

        :param request: Request instance for DescribeRiskSyscallNames.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallNamesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallNamesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallNames", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskSyscallNamesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskSyscallWhiteListDetail(self, request):
        """This API is used to query the details of the allowlist of high-risk syscalls at runtime.

        :param request: Request instance for DescribeRiskSyscallWhiteListDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallWhiteListDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskSyscallWhiteListDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskSyscallWhiteLists(self, request):
        """This API is used to query the allowlist of high-risk syscalls at runtime.

        :param request: Request instance for DescribeRiskSyscallWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallWhiteLists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskSyscallWhiteListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanIgnoreVulList(self, request):
        """This API is used to query the list of vulnerabilities ignored in a scan.

        :param request: Request instance for DescribeScanIgnoreVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeScanIgnoreVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeScanIgnoreVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanIgnoreVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanIgnoreVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchExportList(self, request):
        """This API is used to export the list of ES query files.

        :param request: Request instance for DescribeSearchExportList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchExportListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchExportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchExportList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchExportListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchLogs(self, request):
        """This API is used to get historical search records.

        :param request: Request instance for DescribeSearchLogs.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchLogsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchTemplates(self, request):
        """This API is used to get the list of search templates.

        :param request: Request instance for DescribeSearchTemplates.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchTemplatesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecEventsTendency(self, request):
        """This API is used to query the trend of security events at runtime.

        :param request: Request instance for DescribeSecEventsTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecEventsTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecEventsTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecEventsTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecEventsTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecLogAlertMsg(self, request):
        """This API is used to query a security log alert message.

        :param request: Request instance for DescribeSecLogAlertMsg.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogAlertMsgRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogAlertMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogAlertMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecLogAlertMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecLogCleanSettingInfo(self, request):
        """This API is used to query the settings of security log cleanup.

        :param request: Request instance for DescribeSecLogCleanSettingInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogCleanSettingInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogCleanSettingInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogCleanSettingInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecLogCleanSettingInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecLogDeliveryClsOptions(self, request):
        """This API is used to query the options of security log delivery to CLS.

        :param request: Request instance for DescribeSecLogDeliveryClsOptions.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryClsOptionsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryClsOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogDeliveryClsOptions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecLogDeliveryClsOptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecLogDeliveryClsSetting(self, request):
        """This API is used to query the settings of security log delivery to CLS.

        :param request: Request instance for DescribeSecLogDeliveryClsSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryClsSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryClsSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogDeliveryClsSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecLogDeliveryClsSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecLogDeliveryKafkaOptions(self, request):
        """This API is used to query the options of security log delivery to Kafka.

        :param request: Request instance for DescribeSecLogDeliveryKafkaOptions.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryKafkaOptionsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryKafkaOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogDeliveryKafkaOptions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecLogDeliveryKafkaOptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecLogDeliveryKafkaSetting(self, request):
        """This API is used to query the settings of security log delivery to Kafka.

        :param request: Request instance for DescribeSecLogDeliveryKafkaSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryKafkaSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryKafkaSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogDeliveryKafkaSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecLogDeliveryKafkaSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecLogJoinObjectList(self, request):
        """This API is used to query the list of accessed security log objects.

        :param request: Request instance for DescribeSecLogJoinObjectList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogJoinObjectListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogJoinObjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogJoinObjectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecLogJoinObjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecLogJoinTypeList(self, request):
        """This API is used to query the list of security log access types.

        :param request: Request instance for DescribeSecLogJoinTypeList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogJoinTypeListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogJoinTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogJoinTypeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecLogJoinTypeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecLogKafkaUIN(self, request):
        """This API is used to query the UIN of a Kafka security log.

        :param request: Request instance for DescribeSecLogKafkaUIN.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogKafkaUINRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogKafkaUINResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogKafkaUIN", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecLogKafkaUINResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecLogVasInfo(self, request):
        """This API is used to query the information of the security log product.

        :param request: Request instance for DescribeSecLogVasInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogVasInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogVasInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogVasInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecLogVasInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSupportDefenceVul(self, request):
        """This API is used to query the list of vulnerabilities that can be prevented

        :param request: Request instance for DescribeSupportDefenceVul.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSupportDefenceVulRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSupportDefenceVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSupportDefenceVul", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSupportDefenceVulResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSystemVulList(self, request):
        """This API is used to query the list of system vulnerabilities.

        :param request: Request instance for DescribeSystemVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSystemVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSystemVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSystemVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskResultSummary(self, request):
        """This API is used to query the overview of a check result and return the number of affected nodes in the last seven days.

        :param request: Request instance for DescribeTaskResultSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeTaskResultSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeTaskResultSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskResultSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResultSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTcssSummary(self, request):
        """This API is used to query the TCSS overview.

        :param request: Request instance for DescribeTcssSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeTcssSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeTcssSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTcssSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTcssSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnauthorizedCoresTendency(self, request):
        """This API is used to query the trend of daily unlicensed cores.

        :param request: Request instance for DescribeUnauthorizedCoresTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeUnauthorizedCoresTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeUnauthorizedCoresTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnauthorizedCoresTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnauthorizedCoresTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnfinishRefreshTask(self, request):
        """This API is used to query the information of an unfinished asset refreshing task.

        :param request: Request instance for DescribeUnfinishRefreshTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeUnfinishRefreshTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeUnfinishRefreshTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnfinishRefreshTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnfinishRefreshTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCluster(self, request):
        """This API is used to query the information of a cluster on the Security Dashboard and Cluster Security pages.

        :param request: Request instance for DescribeUserCluster.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeUserClusterRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeUserClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeValueAddedSrvInfo(self, request):
        """This API is used to query the information of the required value-added service.

        :param request: Request instance for DescribeValueAddedSrvInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeValueAddedSrvInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeValueAddedSrvInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeValueAddedSrvInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeValueAddedSrvInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusAutoIsolateSampleDetail(self, request):
        """This API is used to query the details of an automatically isolated trojan sample.

        :param request: Request instance for DescribeVirusAutoIsolateSampleDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusAutoIsolateSampleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusAutoIsolateSampleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusAutoIsolateSampleDownloadURL(self, request):
        """This API is used to query the download URL of an automatically isolated trojan sample.

        :param request: Request instance for DescribeVirusAutoIsolateSampleDownloadURL.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleDownloadURLRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusAutoIsolateSampleDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusAutoIsolateSampleDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusAutoIsolateSampleList(self, request):
        """This API is used to query the list of automatically isolated trojan samples.

        :param request: Request instance for DescribeVirusAutoIsolateSampleList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusAutoIsolateSampleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusAutoIsolateSampleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusAutoIsolateSetting(self, request):
        """This API is used to query the settings of automatic trojan isolation.

        :param request: Request instance for DescribeVirusAutoIsolateSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusAutoIsolateSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusAutoIsolateSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusDetail(self, request):
        """This API is used to query the information of a trojan file at runtime.

        :param request: Request instance for DescribeVirusDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusEventTendency(self, request):
        """This API is used to query the trend of trojan events.

        :param request: Request instance for DescribeVirusEventTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusEventTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusEventTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusEventTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusEventTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusList(self, request):
        """This API is used to query the list of virus scanning events at runtime.

        :param request: Request instance for DescribeVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusManualScanEstimateTimeout(self, request):
        """This API is used to query the estimated timeout period of a quick trojan scan.

        :param request: Request instance for DescribeVirusManualScanEstimateTimeout.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusManualScanEstimateTimeoutRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusManualScanEstimateTimeoutResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusManualScanEstimateTimeout", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusManualScanEstimateTimeoutResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusMonitorSetting(self, request):
        """This API is used to query the real-time monitoring settings of virus scanning at runtime.

        :param request: Request instance for DescribeVirusMonitorSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusMonitorSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusMonitorSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusMonitorSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusMonitorSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusSampleDownloadUrl(self, request):
        """This API is used to query the download URL of a trojan sample.

        :param request: Request instance for DescribeVirusSampleDownloadUrl.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusSampleDownloadUrlRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusSampleDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusSampleDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusSampleDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusScanSetting(self, request):
        """This API is used to query virus scanning settings at runtime.

        :param request: Request instance for DescribeVirusScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusScanSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusScanSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusScanTaskStatus(self, request):
        """This API is used to query the status of a virus scanning task at runtime.

        :param request: Request instance for DescribeVirusScanTaskStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusScanTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusScanTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusScanTimeoutSetting(self, request):
        """This API is used to query the timeout settings of a file scan at runtime.

        :param request: Request instance for DescribeVirusScanTimeoutSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTimeoutSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTimeoutSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusScanTimeoutSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusScanTimeoutSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusSummary(self, request):
        """This API is used to query the trojan overview at runtime.

        :param request: Request instance for DescribeVirusSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVirusTaskList(self, request):
        """This API is used to query the list of virus scanning tasks at runtime.

        :param request: Request instance for DescribeVirusTaskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusTaskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVirusTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulContainerList(self, request):
        """This API is used to query the list of containers affected by vulnerabilities.

        :param request: Request instance for DescribeVulContainerList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulContainerListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulContainerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulContainerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulContainerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceEvent(self, request):
        """This API is used to query the list of exploit prevention events.

        :param request: Request instance for DescribeVulDefenceEvent.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceEventDetail(self, request):
        """This API is used to query the details of an exploit prevention event.

        :param request: Request instance for DescribeVulDefenceEventDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceEventDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceEventDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceEventTendency(self, request):
        """This API is used to query the trend of exploit prevention events.

        :param request: Request instance for DescribeVulDefenceEventTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceEventTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceEventTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceHost(self, request):
        """This API is used to query the list of servers with exploit prevention enabled.

        :param request: Request instance for DescribeVulDefenceHost.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceHostRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefencePlugin(self, request):
        """This API is used to query the list of exploit prevention plugins.

        :param request: Request instance for DescribeVulDefencePlugin.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefencePluginRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefencePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefencePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefencePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceSetting(self, request):
        """This API is used to query the exploit prevention settings.

        :param request: Request instance for DescribeVulDefenceSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDetail(self, request):
        """This API is used to query vulnerability details.

        :param request: Request instance for DescribeVulDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulIgnoreLocalImageList(self, request):
        """This API is used to query the list of local images ignored in a vulnerability scan.

        :param request: Request instance for DescribeVulIgnoreLocalImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulIgnoreLocalImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulIgnoreLocalImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulIgnoreLocalImageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulIgnoreLocalImageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulIgnoreRegistryImageList(self, request):
        """This API is used to query the list of repository images ignored in a vulnerability scan.

        :param request: Request instance for DescribeVulIgnoreRegistryImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulIgnoreRegistryImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulIgnoreRegistryImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulIgnoreRegistryImageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulIgnoreRegistryImageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulImageList(self, request):
        """This API is used to query the list of images affected by vulnerabilities.

        :param request: Request instance for DescribeVulImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulImageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulImageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulImageSummary(self, request):
        """This API is used to query the statistics of images affected by vulnerabilities.

        :param request: Request instance for DescribeVulImageSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulImageSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulImageSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulImageSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulImageSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulLevelImageSummary(self, request):
        """This API is used to query the numbers of images affected by emergency vulnerabilities at each severity level.

        :param request: Request instance for DescribeVulLevelImageSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulLevelImageSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulLevelImageSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLevelImageSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulLevelImageSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulLevelSummary(self, request):
        """This API is used to query the numbers of vulnerabilities at each severity level.

        :param request: Request instance for DescribeVulLevelSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulLevelSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulLevelSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLevelSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulLevelSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulRegistryImageList(self, request):
        """This API is used to query the list of repository images affected by vulnerabilities.

        :param request: Request instance for DescribeVulRegistryImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulRegistryImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulRegistryImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulRegistryImageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulRegistryImageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulScanAuthorizedImageSummary(self, request):
        """This API is used to count the number of licensed but not scanned images on the vulnerability scanning page.

        :param request: Request instance for DescribeVulScanAuthorizedImageSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanAuthorizedImageSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanAuthorizedImageSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanAuthorizedImageSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanAuthorizedImageSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulScanInfo(self, request):
        """This API is used to query the information of a vulnerability scan task.

        :param request: Request instance for DescribeVulScanInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulScanLocalImageList(self, request):
        """This API is used to query the list of local images in a vulnerability scan task.

        :param request: Request instance for DescribeVulScanLocalImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanLocalImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanLocalImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanLocalImageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanLocalImageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulSummary(self, request):
        """This API is used to query the overview of vulnerability risks.

        :param request: Request instance for DescribeVulSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulTendency(self, request):
        """This API is used to query the trend of critical and high-risk vulnerabilities in local and repository images.

        :param request: Request instance for DescribeVulTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulTopRanking(self, request):
        """This API is used to query the list of top vulnerabilities.

        :param request: Request instance for DescribeVulTopRanking.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulTopRankingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulTopRankingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulTopRanking", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulTopRankingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWarningRules(self, request):
        """This API is used to get the list of alert policies.

        :param request: Request instance for DescribeWarningRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeWarningRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeWarningRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarningRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWarningRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebVulList(self, request):
        """This API is used to query the list of web application vulnerabilities.

        :param request: Request instance for DescribeWebVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeWebVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeWebVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVirusList(self, request):
        """This API is used to export the list of virus scanning events at runtime.

        :param request: Request instance for ExportVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ExportVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ExportVirusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVirusList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVirusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InitializeUserComplianceEnvironment(self, request):
        """This API is used to initialize the compliance baseline environment and create necessary data and options.

        :param request: Request instance for InitializeUserComplianceEnvironment.
        :type request: :class:`tencentcloud.tcss.v20201101.models.InitializeUserComplianceEnvironmentRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.InitializeUserComplianceEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitializeUserComplianceEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.InitializeUserComplianceEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAbnormalProcessRuleStatus(self, request):
        """This API is used to change the status of an abnormal process policy at runtime.

        :param request: Request instance for ModifyAbnormalProcessRuleStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessRuleStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAbnormalProcessRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAbnormalProcessRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAbnormalProcessStatus(self, request):
        """This API is used to change the status of an abnormal process event.

        :param request: Request instance for ModifyAbnormalProcessStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAbnormalProcessStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAbnormalProcessStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccessControlRuleStatus(self, request):
        """This API is used to change the status of an access control policy at runtime, i.e., enable or disable it.

        :param request: Request instance for ModifyAccessControlRuleStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlRuleStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccessControlRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccessControlRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccessControlStatus(self, request):
        """This API is used to change the status of an access control event at runtime.

        :param request: Request instance for ModifyAccessControlStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccessControlStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccessControlStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAsset(self, request):
        """This API is used to refresh server assets.

        :param request: Request instance for ModifyAsset.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAsset", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetImageRegistryScanStop(self, request):
        """This API is used to stop an image scan task for an image repository.

        :param request: Request instance for ModifyAssetImageRegistryScanStop.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetImageRegistryScanStop", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetImageRegistryScanStopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetImageRegistryScanStopOneKey(self, request):
        """This API is used to stop a quick image scan task for an image repository.

        :param request: Request instance for ModifyAssetImageRegistryScanStopOneKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopOneKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopOneKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetImageRegistryScanStopOneKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetImageRegistryScanStopOneKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetImageScanStop(self, request):
        """This API is used to stop an image scan.

        :param request: Request instance for ModifyAssetImageScanStop.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageScanStopRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageScanStopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetImageScanStop", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetImageScanStopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCompliancePeriodTask(self, request):
        """This API is used to modify the settings of a scheduled task, including the check cycle and the status of the compliance benchmark.

        :param request: Request instance for ModifyCompliancePeriodTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyCompliancePeriodTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyCompliancePeriodTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCompliancePeriodTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCompliancePeriodTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyContainerNetStatus(self, request):
        """This API is used to isolate a container.

        :param request: Request instance for ModifyContainerNetStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyContainerNetStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyContainerNetStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyContainerNetStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyContainerNetStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEscapeEventStatus(self, request):
        """This API is used to change the status of a container escape scan event.

        :param request: Request instance for ModifyEscapeEventStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeEventStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeEventStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEscapeEventStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEscapeEventStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEscapeRule(self, request):
        """This API is used to modify the information of a container escape scan rule.

        :param request: Request instance for ModifyEscapeRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEscapeRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEscapeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEscapeWhiteList(self, request):
        """This API is used to modify an allowed escape.

        :param request: Request instance for ModifyEscapeWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEscapeWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEscapeWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageAuthorized(self, request):
        """This API is used to batch license images to be scanned (v2.0).

        :param request: Request instance for ModifyImageAuthorized.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyImageAuthorizedRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyImageAuthorizedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageAuthorized", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageAuthorizedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyK8sApiAbnormalEventStatus(self, request):
        """This API is used to modify the status of K8sApi exception events.

        :param request: Request instance for ModifyK8sApiAbnormalEventStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyK8sApiAbnormalEventStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyK8sApiAbnormalEventStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyK8sApiAbnormalEventStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyK8sApiAbnormalEventStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyK8sApiAbnormalRuleInfo(self, request):
        """This API is used to modify the information of K8sApi abnormal rules.

        :param request: Request instance for ModifyK8sApiAbnormalRuleInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyK8sApiAbnormalRuleInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyK8sApiAbnormalRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyK8sApiAbnormalRuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyK8sApiAbnormalRuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyK8sApiAbnormalRuleStatus(self, request):
        """This API is used to modify the status of K8sApi abnormal event rules.

        :param request: Request instance for ModifyK8sApiAbnormalRuleStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyK8sApiAbnormalRuleStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyK8sApiAbnormalRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyK8sApiAbnormalRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyK8sApiAbnormalRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReverseShellStatus(self, request):
        """This API is used to change the status of a reverse shell event.

        :param request: Request instance for ModifyReverseShellStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyReverseShellStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyReverseShellStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReverseShellStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReverseShellStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskSyscallStatus(self, request):
        """This API is used to change the status of a high-risk syscall event.

        :param request: Request instance for ModifyRiskSyscallStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyRiskSyscallStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyRiskSyscallStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskSyscallStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskSyscallStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecLogCleanSettingInfo(self, request):
        """This API is used to modify the settings of security log cleanup.

        :param request: Request instance for ModifySecLogCleanSettingInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogCleanSettingInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogCleanSettingInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogCleanSettingInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecLogCleanSettingInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecLogDeliveryClsSetting(self, request):
        """This API is used to update the configuration of security log delivery to CLS.

        :param request: Request instance for ModifySecLogDeliveryClsSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogDeliveryClsSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogDeliveryClsSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogDeliveryClsSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecLogDeliveryClsSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecLogDeliveryKafkaSetting(self, request):
        """This API is used to update the settings of security log delivery to Kafka.

        :param request: Request instance for ModifySecLogDeliveryKafkaSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogDeliveryKafkaSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogDeliveryKafkaSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogDeliveryKafkaSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecLogDeliveryKafkaSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecLogJoinObjects(self, request):
        """This API is used to modify an accessed security log object.

        :param request: Request instance for ModifySecLogJoinObjects.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogJoinObjectsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogJoinObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogJoinObjects", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecLogJoinObjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecLogJoinState(self, request):
        """This API is used to change the security log access status.

        :param request: Request instance for ModifySecLogJoinState.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogJoinStateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogJoinStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogJoinState", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecLogJoinStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecLogKafkaUIN(self, request):
        """This API is used to modify the UIN of a Kafka security log.

        :param request: Request instance for ModifySecLogKafkaUIN.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogKafkaUINRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogKafkaUINResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogKafkaUIN", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecLogKafkaUINResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVirusAutoIsolateExampleSwitch(self, request):
        """This API is used to enable/disable automatic trojan sample isolation.

        :param request: Request instance for ModifyVirusAutoIsolateExampleSwitch.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusAutoIsolateExampleSwitchRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusAutoIsolateExampleSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusAutoIsolateExampleSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVirusAutoIsolateExampleSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVirusAutoIsolateSetting(self, request):
        """This API is used to modify the settings of automatic trojan isolation.

        :param request: Request instance for ModifyVirusAutoIsolateSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusAutoIsolateSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusAutoIsolateSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusAutoIsolateSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVirusAutoIsolateSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVirusFileStatus(self, request):
        """This API is used to update the status of a trojan file at runtime.

        :param request: Request instance for ModifyVirusFileStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusFileStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusFileStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusFileStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVirusFileStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVirusMonitorSetting(self, request):
        """This API is used to update the real-time monitoring settings of virus scanning at runtime.

        :param request: Request instance for ModifyVirusMonitorSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusMonitorSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusMonitorSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusMonitorSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVirusMonitorSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVirusScanSetting(self, request):
        """This API is used to update virus scanning settings at runtime.

        :param request: Request instance for ModifyVirusScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusScanSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVirusScanSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVirusScanTimeoutSetting(self, request):
        """This API is used to modify the timeout settings of a file scan at runtime.

        :param request: Request instance for ModifyVirusScanTimeoutSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanTimeoutSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanTimeoutSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusScanTimeoutSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVirusScanTimeoutSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVulDefenceEventStatus(self, request):
        """This API is used to change the status of an exploit prevention event.

        :param request: Request instance for ModifyVulDefenceEventStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVulDefenceEventStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVulDefenceEventStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulDefenceEventStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVulDefenceEventStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVulDefenceSetting(self, request):
        """This API is used to edit the exploit prevention settings.

        :param request: Request instance for ModifyVulDefenceSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVulDefenceSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVulDefenceSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulDefenceSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVulDefenceSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenTcssTrial(self, request):
        """This API is used to activate TCSS trial.

        :param request: Request instance for OpenTcssTrial.
        :type request: :class:`tencentcloud.tcss.v20201101.models.OpenTcssTrialRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.OpenTcssTrialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenTcssTrial", params, headers=headers)
            response = json.loads(body)
            model = models.OpenTcssTrialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveAssetImageRegistryRegistryDetail(self, request):
        """This API is used to delete the details of an image repository.

        :param request: Request instance for RemoveAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.RemoveAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.RemoveAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveAssetImageRegistryRegistryDetail", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveAssetImageRegistryRegistryDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewImageAuthorizeState(self, request):
        """This API is used to license an image to be scanned.

        :param request: Request instance for RenewImageAuthorizeState.
        :type request: :class:`tencentcloud.tcss.v20201101.models.RenewImageAuthorizeStateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.RenewImageAuthorizeStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewImageAuthorizeState", params, headers=headers)
            response = json.loads(body)
            model = models.RenewImageAuthorizeStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetSecLogTopicConfig(self, request):
        """This API is used to reset a security log topic.

        :param request: Request instance for ResetSecLogTopicConfig.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ResetSecLogTopicConfigRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ResetSecLogTopicConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetSecLogTopicConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ResetSecLogTopicConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanComplianceAssets(self, request):
        """This API is used to check the specified asset again.

        :param request: Request instance for ScanComplianceAssets.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanComplianceAssets", params, headers=headers)
            response = json.loads(body)
            model = models.ScanComplianceAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanComplianceAssetsByPolicyItem(self, request):
        """This API is used to check the specified asset again with the specified check item and return the ID of the created compliance check task.

        :param request: Request instance for ScanComplianceAssetsByPolicyItem.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsByPolicyItemRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsByPolicyItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanComplianceAssetsByPolicyItem", params, headers=headers)
            response = json.loads(body)
            model = models.ScanComplianceAssetsByPolicyItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanCompliancePolicyItems(self, request):
        """This API is used to check all the assets of the specified check item again and return the ID of the created compliance check task.

        :param request: Request instance for ScanCompliancePolicyItems.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanCompliancePolicyItemsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanCompliancePolicyItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanCompliancePolicyItems", params, headers=headers)
            response = json.loads(body)
            model = models.ScanCompliancePolicyItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanComplianceScanFailedAssets(self, request):
        """This API is used to check all the failed check items of the specified asset again and return the ID of the created compliance check task.

        :param request: Request instance for ScanComplianceScanFailedAssets.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceScanFailedAssetsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceScanFailedAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanComplianceScanFailedAssets", params, headers=headers)
            response = json.loads(body)
            model = models.ScanComplianceScanFailedAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetCheckMode(self, request):
        """This API is used to set the check mode and automatic check.

        :param request: Request instance for SetCheckMode.
        :type request: :class:`tencentcloud.tcss.v20201101.models.SetCheckModeRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.SetCheckModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetCheckMode", params, headers=headers)
            response = json.loads(body)
            model = models.SetCheckModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopVirusScanTask(self, request):
        """This API is used to stop a trojan scan task at runtime.

        :param request: Request instance for StopVirusScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.StopVirusScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.StopVirusScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopVirusScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopVirusScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopVulScanTask(self, request):
        """This API is used to stop a vulnerability scan task.

        :param request: Request instance for StopVulScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.StopVulScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.StopVulScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopVulScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopVulScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchImageAutoAuthorizedRule(self, request):
        """This API is used to enable/disable automatic licensing for local images.

        :param request: Request instance for SwitchImageAutoAuthorizedRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.SwitchImageAutoAuthorizedRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.SwitchImageAutoAuthorizedRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchImageAutoAuthorizedRule", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchImageAutoAuthorizedRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncAssetImageRegistryAsset(self, request):
        """This API is used to refresh the assets in an image repository.

        :param request: Request instance for SyncAssetImageRegistryAsset.
        :type request: :class:`tencentcloud.tcss.v20201101.models.SyncAssetImageRegistryAssetRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.SyncAssetImageRegistryAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncAssetImageRegistryAsset", params, headers=headers)
            response = json.loads(body)
            model = models.SyncAssetImageRegistryAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAndPublishNetworkFirewallPolicyDetail(self, request):
        """This API is used to create a task to update and publish a network policy in the container network.

        :param request: Request instance for UpdateAndPublishNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateAndPublishNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateAndPublishNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAndPublishNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAndPublishNetworkFirewallPolicyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAndPublishNetworkFirewallPolicyYamlDetail(self, request):
        """This API is used to create a task to update and publish a YAML network policy in the container network.

        :param request: Request instance for UpdateAndPublishNetworkFirewallPolicyYamlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateAndPublishNetworkFirewallPolicyYamlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateAndPublishNetworkFirewallPolicyYamlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAndPublishNetworkFirewallPolicyYamlDetail", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAndPublishNetworkFirewallPolicyYamlDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAssetImageRegistryRegistryDetail(self, request):
        """This API is used to update the details of an image repository.

        :param request: Request instance for UpdateAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAssetImageRegistryRegistryDetail", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAssetImageRegistryRegistryDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateImageRegistryTimingScanTask(self, request):
        """This API is used to update a scheduled task for an image repository.

        :param request: Request instance for UpdateImageRegistryTimingScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateImageRegistryTimingScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateImageRegistryTimingScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateImageRegistryTimingScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateImageRegistryTimingScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateNetworkFirewallPolicyDetail(self, request):
        """This API is used to create a task to update a network policy in the container network.

        :param request: Request instance for UpdateNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateNetworkFirewallPolicyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateNetworkFirewallPolicyYamlDetail(self, request):
        """This API is used to create a task to update a YAML network policy in the container network.

        :param request: Request instance for UpdateNetworkFirewallPolicyYamlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateNetworkFirewallPolicyYamlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateNetworkFirewallPolicyYamlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateNetworkFirewallPolicyYamlDetail", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateNetworkFirewallPolicyYamlDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))