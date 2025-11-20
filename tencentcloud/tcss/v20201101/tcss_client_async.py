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
from tencentcloud.tcss.v20201101 import models
from typing import Dict


class TcssClient(AbstractClient):
    _apiVersion = '2020-11-01'
    _endpoint = 'tcss.intl.tencentcloudapi.com'
    _service = 'tcss'

    async def AddAndPublishNetworkFirewallPolicyDetail(
            self,
            request: models.AddAndPublishNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.AddAndPublishNetworkFirewallPolicyDetailResponse:
        """
        This API is used to create a task to add and publish a network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "AddAndPublishNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAndPublishNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAndPublishNetworkFirewallPolicyYamlDetail(
            self,
            request: models.AddAndPublishNetworkFirewallPolicyYamlDetailRequest,
            opts: Dict = None,
    ) -> models.AddAndPublishNetworkFirewallPolicyYamlDetailResponse:
        """
        This API is used to create a task to configure and publish a YAML network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "AddAndPublishNetworkFirewallPolicyYamlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAndPublishNetworkFirewallPolicyYamlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAssetImageRegistryRegistryDetail(
            self,
            request: models.AddAssetImageRegistryRegistryDetailRequest,
            opts: Dict = None,
    ) -> models.AddAssetImageRegistryRegistryDetailResponse:
        """
        This API is used to add the details of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "AddAssetImageRegistryRegistryDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAssetImageRegistryRegistryDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddComplianceAssetPolicySetToWhitelist(
            self,
            request: models.AddComplianceAssetPolicySetToWhitelistRequest,
            opts: Dict = None,
    ) -> models.AddComplianceAssetPolicySetToWhitelistResponse:
        """
        This API is used to ignore the specified asset IDs and check item IDs so as to hide the assets contained in the specified check items.
        `AddCompliancePolicyItemToWhitelist` is the reference API. Except for the input field, others should be the same, and if not, it may be due to the definition.
        """
        
        kwargs = {}
        kwargs["action"] = "AddComplianceAssetPolicySetToWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddComplianceAssetPolicySetToWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCompliancePolicyAssetSetToWhitelist(
            self,
            request: models.AddCompliancePolicyAssetSetToWhitelistRequest,
            opts: Dict = None,
    ) -> models.AddCompliancePolicyAssetSetToWhitelistResponse:
        """
        This API is used to ignore the specified asset IDs and check item IDs so as to hide the assets contained in the specified check items.
        `AddCompliancePolicyItemToWhitelist` is the reference API. Except for the input field, others should be the same, and if not, it may be due to the definition.
        """
        
        kwargs = {}
        kwargs["action"] = "AddCompliancePolicyAssetSetToWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCompliancePolicyAssetSetToWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCompliancePolicyItemToWhitelist(
            self,
            request: models.AddCompliancePolicyItemToWhitelistRequest,
            opts: Dict = None,
    ) -> models.AddCompliancePolicyItemToWhitelistResponse:
        """
        This API is used to add the specified check item IDs to the allowlist so as to hide the failure result.
        """
        
        kwargs = {}
        kwargs["action"] = "AddCompliancePolicyItemToWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCompliancePolicyItemToWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditAbnormalProcessRule(
            self,
            request: models.AddEditAbnormalProcessRuleRequest,
            opts: Dict = None,
    ) -> models.AddEditAbnormalProcessRuleResponse:
        """
        This API is used to add or edit an abnormal process policy at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditAbnormalProcessRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditAbnormalProcessRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditAccessControlRule(
            self,
            request: models.AddEditAccessControlRuleRequest,
            opts: Dict = None,
    ) -> models.AddEditAccessControlRuleResponse:
        """
        This API is used to add or edit an access control policy at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditAccessControlRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditAccessControlRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditImageAutoAuthorizedRule(
            self,
            request: models.AddEditImageAutoAuthorizedRuleRequest,
            opts: Dict = None,
    ) -> models.AddEditImageAutoAuthorizedRuleResponse:
        """
        This API is used to add or edit an automatic licensing rule for local images.
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditImageAutoAuthorizedRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditImageAutoAuthorizedRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditReverseShellWhiteList(
            self,
            request: models.AddEditReverseShellWhiteListRequest,
            opts: Dict = None,
    ) -> models.AddEditReverseShellWhiteListResponse:
        """
        This API is used to add or edit an allowed reverse shell at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditReverseShellWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditReverseShellWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditRiskSyscallWhiteList(
            self,
            request: models.AddEditRiskSyscallWhiteListRequest,
            opts: Dict = None,
    ) -> models.AddEditRiskSyscallWhiteListResponse:
        """
        This API is used to add or edit an allowed high-risk syscall at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditRiskSyscallWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditRiskSyscallWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditWarningRules(
            self,
            request: models.AddEditWarningRulesRequest,
            opts: Dict = None,
    ) -> models.AddEditWarningRulesResponse:
        """
        This API is used to add or edit an alert policy.
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditWarningRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditWarningRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEscapeWhiteList(
            self,
            request: models.AddEscapeWhiteListRequest,
            opts: Dict = None,
    ) -> models.AddEscapeWhiteListResponse:
        """
        This API is used to add an allowed escape.
        """
        
        kwargs = {}
        kwargs["action"] = "AddEscapeWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEscapeWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddIgnoreVul(
            self,
            request: models.AddIgnoreVulRequest,
            opts: Dict = None,
    ) -> models.AddIgnoreVulResponse:
        """
        This API is used to add ignored vulnerabilities in a vulnerability scan.
        """
        
        kwargs = {}
        kwargs["action"] = "AddIgnoreVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddIgnoreVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNetworkFirewallPolicyDetail(
            self,
            request: models.AddNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.AddNetworkFirewallPolicyDetailResponse:
        """
        This API is used to create a task to add a network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "AddNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNetworkFirewallPolicyYamlDetail(
            self,
            request: models.AddNetworkFirewallPolicyYamlDetailRequest,
            opts: Dict = None,
    ) -> models.AddNetworkFirewallPolicyYamlDetailResponse:
        """
        This API is used to create a task to add a YAML network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "AddNetworkFirewallPolicyYamlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNetworkFirewallPolicyYamlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckNetworkFirewallPolicyYaml(
            self,
            request: models.CheckNetworkFirewallPolicyYamlRequest,
            opts: Dict = None,
    ) -> models.CheckNetworkFirewallPolicyYamlResponse:
        """
        This API is used to create a task to check a YAML network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckNetworkFirewallPolicyYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckNetworkFirewallPolicyYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckRepeatAssetImageRegistry(
            self,
            request: models.CheckRepeatAssetImageRegistryRequest,
            opts: Dict = None,
    ) -> models.CheckRepeatAssetImageRegistryResponse:
        """
        This API is used to check whether an image repository name is duplicated.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckRepeatAssetImageRegistry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckRepeatAssetImageRegistryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfirmNetworkFirewallPolicy(
            self,
            request: models.ConfirmNetworkFirewallPolicyRequest,
            opts: Dict = None,
    ) -> models.ConfirmNetworkFirewallPolicyResponse:
        """
        This API is used to create a task to confirm a network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "ConfirmNetworkFirewallPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfirmNetworkFirewallPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAbnormalProcessRulesExportJob(
            self,
            request: models.CreateAbnormalProcessRulesExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAbnormalProcessRulesExportJobResponse:
        """
        This API is used to export abnormal process rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAbnormalProcessRulesExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAbnormalProcessRulesExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessControlsRuleExportJob(
            self,
            request: models.CreateAccessControlsRuleExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAccessControlsRuleExportJobResponse:
        """
        This API is used to export file tampering detection rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessControlsRuleExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessControlsRuleExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetImageRegistryScanTask(
            self,
            request: models.CreateAssetImageRegistryScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAssetImageRegistryScanTaskResponse:
        """
        This API is used to create an image scan task for an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetImageRegistryScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetImageRegistryScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetImageRegistryScanTaskOneKey(
            self,
            request: models.CreateAssetImageRegistryScanTaskOneKeyRequest,
            opts: Dict = None,
    ) -> models.CreateAssetImageRegistryScanTaskOneKeyResponse:
        """
        This API is used to create a quick image scan task for an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetImageRegistryScanTaskOneKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetImageRegistryScanTaskOneKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetImageScanSetting(
            self,
            request: models.CreateAssetImageScanSettingRequest,
            opts: Dict = None,
    ) -> models.CreateAssetImageScanSettingResponse:
        """
        This API is used to set an image scan.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetImageScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetImageScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetImageScanTask(
            self,
            request: models.CreateAssetImageScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAssetImageScanTaskResponse:
        """
        This API is used to create an image scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetImageScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetImageScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetImageVirusExportJob(
            self,
            request: models.CreateAssetImageVirusExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAssetImageVirusExportJobResponse:
        """
        This API is used to create a task to export the list of trojans in a local image.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetImageVirusExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetImageVirusExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCheckComponent(
            self,
            request: models.CreateCheckComponentRequest,
            opts: Dict = None,
    ) -> models.CreateCheckComponentResponse:
        """
        This API is used to install the check component and create a defender.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCheckComponent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCheckComponentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterCheckTask(
            self,
            request: models.CreateClusterCheckTaskRequest,
            opts: Dict = None,
    ) -> models.CreateClusterCheckTaskResponse:
        """
        This API is used to create a cluster check task to check it for risk items.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterCheckTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterCheckTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateComplianceTask(
            self,
            request: models.CreateComplianceTaskRequest,
            opts: Dict = None,
    ) -> models.CreateComplianceTaskResponse:
        """
        This API is used to create a compliance check task for another check triggered at the asset level.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateComplianceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateComplianceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateComponentExportJob(
            self,
            request: models.CreateComponentExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateComponentExportJobResponse:
        """
        This API is used to export the list of components in a local image.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateComponentExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateComponentExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDefenceVulExportJob(
            self,
            request: models.CreateDefenceVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDefenceVulExportJobResponse:
        """
        This API is used to create a task to export vulnerabilities that can be prevented.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDefenceVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDefenceVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmergencyVulExportJob(
            self,
            request: models.CreateEmergencyVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateEmergencyVulExportJobResponse:
        """
        This API is used to create a task to export emergency vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmergencyVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmergencyVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEscapeEventsExportJob(
            self,
            request: models.CreateEscapeEventsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateEscapeEventsExportJobResponse:
        """
        This API is used to create a task to asynchronously export escape events.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEscapeEventsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEscapeEventsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEscapeWhiteListExportJob(
            self,
            request: models.CreateEscapeWhiteListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateEscapeWhiteListExportJobResponse:
        """
        This API is used to create a task to export the allowlist of escapes.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEscapeWhiteListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEscapeWhiteListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExportComplianceStatusListJob(
            self,
            request: models.CreateExportComplianceStatusListJobRequest,
            opts: Dict = None,
    ) -> models.CreateExportComplianceStatusListJobResponse:
        """
        This API is used to create a task to export security compliance information.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExportComplianceStatusListJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExportComplianceStatusListJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHostExportJob(
            self,
            request: models.CreateHostExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateHostExportJobResponse:
        """
        This API is used to create a task to export the list of servers.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHostExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageExportJob(
            self,
            request: models.CreateImageExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageExportJobResponse:
        """
        This API is used to create an image export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateK8sApiAbnormalEventExportJob(
            self,
            request: models.CreateK8sApiAbnormalEventExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateK8sApiAbnormalEventExportJobResponse:
        """
        This API is used to create K8sApi abnormal event export jobs.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateK8sApiAbnormalEventExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateK8sApiAbnormalEventExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateK8sApiAbnormalRuleExportJob(
            self,
            request: models.CreateK8sApiAbnormalRuleExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateK8sApiAbnormalRuleExportJobResponse:
        """
        This API is used to export rules of K8sApi exceptions.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateK8sApiAbnormalRuleExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateK8sApiAbnormalRuleExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateK8sApiAbnormalRuleInfo(
            self,
            request: models.CreateK8sApiAbnormalRuleInfoRequest,
            opts: Dict = None,
    ) -> models.CreateK8sApiAbnormalRuleInfoResponse:
        """
        This API is used to create K8sApi abnormal event rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateK8sApiAbnormalRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateK8sApiAbnormalRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkFirewallClusterRefresh(
            self,
            request: models.CreateNetworkFirewallClusterRefreshRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkFirewallClusterRefreshResponse:
        """
        This API is used to distribute a refresh task in the container network cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkFirewallClusterRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkFirewallClusterRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkFirewallPolicyDiscover(
            self,
            request: models.CreateNetworkFirewallPolicyDiscoverRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkFirewallPolicyDiscoverResponse:
        """
        This API is used to create a task to sync a network policy from the container network cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkFirewallPolicyDiscover"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkFirewallPolicyDiscoverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkFirewallPublish(
            self,
            request: models.CreateNetworkFirewallPublishRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkFirewallPublishResponse:
        """
        This API is used to create a task to publish a network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkFirewallPublish"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkFirewallPublishResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkFirewallUndoPublish(
            self,
            request: models.CreateNetworkFirewallUndoPublishRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkFirewallUndoPublishResponse:
        """
        This API is used to create a task to revoke a network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkFirewallUndoPublish"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkFirewallUndoPublishResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrModifyPostPayCores(
            self,
            request: models.CreateOrModifyPostPayCoresRequest,
            opts: Dict = None,
    ) -> models.CreateOrModifyPostPayCoresResponse:
        """
        This API is used to create or edit the upper limit for elastic billing.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrModifyPostPayCores"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrModifyPostPayCoresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProcessEventsExportJob(
            self,
            request: models.CreateProcessEventsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateProcessEventsExportJobResponse:
        """
        This API is used to create a task to asynchronously export abnormal process events.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProcessEventsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProcessEventsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRefreshTask(
            self,
            request: models.CreateRefreshTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRefreshTaskResponse:
        """
        This API is used to distribute a task to refresh the asset information.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRefreshTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRefreshTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRiskDnsEventExportJob(
            self,
            request: models.CreateRiskDnsEventExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateRiskDnsEventExportJobResponse:
        """
        This API is used to export malicious request events.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRiskDnsEventExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRiskDnsEventExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSearchTemplate(
            self,
            request: models.CreateSearchTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSearchTemplateResponse:
        """
        This API is used to add a search template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSearchTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSearchTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSystemVulExportJob(
            self,
            request: models.CreateSystemVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateSystemVulExportJobResponse:
        """
        This API is used to create a task to export system vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSystemVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSystemVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVirusScanAgain(
            self,
            request: models.CreateVirusScanAgainRequest,
            opts: Dict = None,
    ) -> models.CreateVirusScanAgainResponse:
        """
        This API is used to perform another virus scan at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVirusScanAgain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVirusScanAgainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVirusScanTask(
            self,
            request: models.CreateVirusScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVirusScanTaskResponse:
        """
        This API is used to perform a quick virus scan at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVirusScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVirusScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulContainerExportJob(
            self,
            request: models.CreateVulContainerExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulContainerExportJobResponse:
        """
        This API is used to create a task to export containers affected by vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulContainerExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulContainerExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulDefenceEventExportJob(
            self,
            request: models.CreateVulDefenceEventExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulDefenceEventExportJobResponse:
        """
        This API is used to create an exploit prevention event export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulDefenceEventExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulDefenceEventExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulDefenceHostExportJob(
            self,
            request: models.CreateVulDefenceHostExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulDefenceHostExportJobResponse:
        """
        This API is used to create a task to export servers with exploit prevention enabled.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulDefenceHostExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulDefenceHostExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulExportJob(
            self,
            request: models.CreateVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulExportJobResponse:
        """
        This API is used to export the list of vulnerabilities in a local image.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulImageExportJob(
            self,
            request: models.CreateVulImageExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulImageExportJobResponse:
        """
        This API is used to create a task to export images affected by vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulImageExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulImageExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulScanTask(
            self,
            request: models.CreateVulScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVulScanTaskResponse:
        """
        This API is used to create a vulnerability scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWebVulExportJob(
            self,
            request: models.CreateWebVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateWebVulExportJobResponse:
        """
        This API is used to create a task to export web vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWebVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWebVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAbnormalProcessRules(
            self,
            request: models.DeleteAbnormalProcessRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteAbnormalProcessRulesResponse:
        """
        This API is used to delete an abnormal process policy at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAbnormalProcessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAbnormalProcessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccessControlRules(
            self,
            request: models.DeleteAccessControlRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteAccessControlRulesResponse:
        """
        This API is used to delete an access control policy at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccessControlRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccessControlRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteComplianceAssetPolicySetFromWhitelist(
            self,
            request: models.DeleteComplianceAssetPolicySetFromWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteComplianceAssetPolicySetFromWhitelistResponse:
        """
        This API is used to unignore the specified asset IDs and check item IDs so as to show the assets contained in the specified check items.
        `AddCompliancePolicyAssetSetToWhitelist` is the reference API. Except for the input field, others should be the same, and if not, it may be due to the definition.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteComplianceAssetPolicySetFromWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteComplianceAssetPolicySetFromWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCompliancePolicyAssetSetFromWhitelist(
            self,
            request: models.DeleteCompliancePolicyAssetSetFromWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteCompliancePolicyAssetSetFromWhitelistResponse:
        """
        This API is used to unignore the specified asset IDs and check item IDs so as to show the assets contained in the specified check items.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCompliancePolicyAssetSetFromWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCompliancePolicyAssetSetFromWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCompliancePolicyItemFromWhitelist(
            self,
            request: models.DeleteCompliancePolicyItemFromWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteCompliancePolicyItemFromWhitelistResponse:
        """
        This API is used to remove the specified check item from the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCompliancePolicyItemFromWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCompliancePolicyItemFromWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEscapeWhiteList(
            self,
            request: models.DeleteEscapeWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteEscapeWhiteListResponse:
        """
        This API is used to delete an allowed escape.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEscapeWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEscapeWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIgnoreVul(
            self,
            request: models.DeleteIgnoreVulRequest,
            opts: Dict = None,
    ) -> models.DeleteIgnoreVulResponse:
        """
        This API is used to unignore vulnerabilities in a vulnerability scan.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIgnoreVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIgnoreVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteK8sApiAbnormalRule(
            self,
            request: models.DeleteK8sApiAbnormalRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteK8sApiAbnormalRuleResponse:
        """
        This API is used to delete a K8sApi abnormal event rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteK8sApiAbnormalRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteK8sApiAbnormalRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachine(
            self,
            request: models.DeleteMachineRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineResponse:
        """
        This API is used to uninstall the agent.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkFirewallPolicyDetail(
            self,
            request: models.DeleteNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkFirewallPolicyDetailResponse:
        """
        This API is used to create a task to delete a network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReverseShellEvents(
            self,
            request: models.DeleteReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.DeleteReverseShellEventsResponse:
        """
        This API is used to delete a reverse shell event at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReverseShellWhiteLists(
            self,
            request: models.DeleteReverseShellWhiteListsRequest,
            opts: Dict = None,
    ) -> models.DeleteReverseShellWhiteListsResponse:
        """
        This API is used to delete an allowed reverse shell at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReverseShellWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReverseShellWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRiskSyscallEvents(
            self,
            request: models.DeleteRiskSyscallEventsRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskSyscallEventsResponse:
        """
        This API is used to delete a high-risk syscall event at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskSyscallEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskSyscallEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRiskSyscallWhiteLists(
            self,
            request: models.DeleteRiskSyscallWhiteListsRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskSyscallWhiteListsResponse:
        """
        This API is used to delete an allowed high-risk syscall at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskSyscallWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskSyscallWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSearchTemplate(
            self,
            request: models.DeleteSearchTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSearchTemplateResponse:
        """
        This API is used to delete a search template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSearchTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSearchTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeABTestConfig(
            self,
            request: models.DescribeABTestConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeABTestConfigResponse:
        """
        This API is used to get the current canary configuration of the user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeABTestConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeABTestConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessDetail(
            self,
            request: models.DescribeAbnormalProcessDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessDetailResponse:
        """
        This API is used to query the details of an abnormal process event at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessEventTendency(
            self,
            request: models.DescribeAbnormalProcessEventTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessEventTendencyResponse:
        """
        This API is used to query the trend of pending abnormal process events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessEventTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessEventTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessEvents(
            self,
            request: models.DescribeAbnormalProcessEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessEventsResponse:
        """
        This API is used to query the list of abnormal process events at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessEventsExport(
            self,
            request: models.DescribeAbnormalProcessEventsExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessEventsExportResponse:
        """
        接口已废弃

        This API is used to query and export the list of abnormal process events at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessEventsExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessEventsExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessLevelSummary(
            self,
            request: models.DescribeAbnormalProcessLevelSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessLevelSummaryResponse:
        """
        This API is used to count the number of pending abnormal process events at each severity level.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessLevelSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessLevelSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessRuleDetail(
            self,
            request: models.DescribeAbnormalProcessRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessRuleDetailResponse:
        """
        This API is used to query the details of an abnormal process policy at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessRules(
            self,
            request: models.DescribeAbnormalProcessRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessRulesResponse:
        """
        This API is used to query the list of abnormal process policies at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessRulesExport(
            self,
            request: models.DescribeAbnormalProcessRulesExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessRulesExportResponse:
        """
        接口已废弃

        This API is used to query and export the list of abnormal process policies at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessRulesExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessRulesExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlDetail(
            self,
            request: models.DescribeAccessControlDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlDetailResponse:
        """
        This API is used to query the details of an access control event at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlEvents(
            self,
            request: models.DescribeAccessControlEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlEventsResponse:
        """
        This API is used to query the list of access control events at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlEventsExport(
            self,
            request: models.DescribeAccessControlEventsExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlEventsExportResponse:
        """
        This API is used to export the list of access control events at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlEventsExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlEventsExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlRuleDetail(
            self,
            request: models.DescribeAccessControlRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlRuleDetailResponse:
        """
        This API is used to query the details of an access control policy at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlRules(
            self,
            request: models.DescribeAccessControlRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlRulesResponse:
        """
        This API is used to query the list of access control policies at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlRulesExport(
            self,
            request: models.DescribeAccessControlRulesExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlRulesExportResponse:
        """
        接口已废弃

        This API is used to export the list of access control policies at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlRulesExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlRulesExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAffectedClusterCount(
            self,
            request: models.DescribeAffectedClusterCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAffectedClusterCountResponse:
        """
        This API is used to get and return the number of affected clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAffectedClusterCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAffectedClusterCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAffectedNodeList(
            self,
            request: models.DescribeAffectedNodeListRequest,
            opts: Dict = None,
    ) -> models.DescribeAffectedNodeListResponse:
        """
        This API is used to query affected node types and return the node list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAffectedNodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAffectedNodeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAffectedWorkloadList(
            self,
            request: models.DescribeAffectedWorkloadListRequest,
            opts: Dict = None,
    ) -> models.DescribeAffectedWorkloadListResponse:
        """
        This API is used to query affected workload types and return the workload list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAffectedWorkloadList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAffectedWorkloadListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentDaemonSetCmd(
            self,
            request: models.DescribeAgentDaemonSetCmdRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentDaemonSetCmdResponse:
        """
        This API is used to query parallel container installation commands.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentDaemonSetCmd"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentDaemonSetCmdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentInstallCommand(
            self,
            request: models.DescribeAgentInstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentInstallCommandResponse:
        """
        This API is used to query agent installation commands.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentInstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentInstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetAppServiceList(
            self,
            request: models.DescribeAssetAppServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetAppServiceListResponse:
        """
        This API is used to query the list of application services.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetAppServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetAppServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetClusterList(
            self,
            request: models.DescribeAssetClusterListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetClusterListResponse:
        """
        This API is used to query the list of clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetClusterList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetClusterListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetComponentList(
            self,
            request: models.DescribeAssetComponentListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetComponentListResponse:
        """
        This API is used to query the list of container components.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetComponentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetComponentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetContainerDetail(
            self,
            request: models.DescribeAssetContainerDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetContainerDetailResponse:
        """
        This API is used to query the information of a container.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetContainerDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetContainerDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetContainerList(
            self,
            request: models.DescribeAssetContainerListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetContainerListResponse:
        """
        This API is used to query the list of containers.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetContainerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetContainerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDBServiceList(
            self,
            request: models.DescribeAssetDBServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDBServiceListResponse:
        """
        This API is used to query the list of database services.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDBServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDBServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetHostDetail(
            self,
            request: models.DescribeAssetHostDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetHostDetailResponse:
        """
        This API is used to query the details of a server.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetHostDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetHostDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetHostList(
            self,
            request: models.DescribeAssetHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetHostListResponse:
        """
        This API is used to query the list of servers.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageBindRuleInfo(
            self,
            request: models.DescribeAssetImageBindRuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageBindRuleInfoResponse:
        """
        This API is used to query the list of rules bound to images, including runtime access control and abnormal process rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageBindRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageBindRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageDetail(
            self,
            request: models.DescribeAssetImageDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageDetailResponse:
        """
        This API is used to query the details of an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageHostList(
            self,
            request: models.DescribeAssetImageHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageHostListResponse:
        """
        This API is used to query the servers associated with an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageList(
            self,
            request: models.DescribeAssetImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageListResponse:
        """
        This API is used to query the list of images.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageListExport(
            self,
            request: models.DescribeAssetImageListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageListExportResponse:
        """
        接口已废弃

        This API is used to export the list of images.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryAssetStatus(
            self,
            request: models.DescribeAssetImageRegistryAssetStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryAssetStatusResponse:
        """
        This API is used to view the update progress of the assets in an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryAssetStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryAssetStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryDetail(
            self,
            request: models.DescribeAssetImageRegistryDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryDetailResponse:
        """
        This API is used to query the image repository details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryList(
            self,
            request: models.DescribeAssetImageRegistryListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryListResponse:
        """
        This API is used to query the list of image repositories.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryListExport(
            self,
            request: models.DescribeAssetImageRegistryListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryListExportResponse:
        """
        This API is used to export the list of images for an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryRegistryDetail(
            self,
            request: models.DescribeAssetImageRegistryRegistryDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryRegistryDetailResponse:
        """
        This API is used to view the details of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryRegistryDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryRegistryDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryRegistryList(
            self,
            request: models.DescribeAssetImageRegistryRegistryListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryRegistryListResponse:
        """
        This API is used to query the list of image registries.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryRegistryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryRegistryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryRiskInfoList(
            self,
            request: models.DescribeAssetImageRegistryRiskInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryRiskInfoListResponse:
        """
        This API is used to query the list of image high-risk behaviors of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryRiskInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryRiskInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryRiskListExport(
            self,
            request: models.DescribeAssetImageRegistryRiskListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryRiskListExportResponse:
        """
        This API is used to export the list of sensitive data for an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryRiskListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryRiskListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryScanStatusOneKey(
            self,
            request: models.DescribeAssetImageRegistryScanStatusOneKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryScanStatusOneKeyResponse:
        """
        This API is used to query the quick image scanning status of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryScanStatusOneKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryScanStatusOneKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistrySummary(
            self,
            request: models.DescribeAssetImageRegistrySummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistrySummaryResponse:
        """
        This API is used to query the image statistics of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistrySummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistrySummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryVirusList(
            self,
            request: models.DescribeAssetImageRegistryVirusListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryVirusListResponse:
        """
        This API is used to query the list of viruses and trojans in an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryVirusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryVirusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryVirusListExport(
            self,
            request: models.DescribeAssetImageRegistryVirusListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryVirusListExportResponse:
        """
        This API is used to export the list of trojan information for an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryVirusListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryVirusListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryVulList(
            self,
            request: models.DescribeAssetImageRegistryVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryVulListResponse:
        """
        This API is used to query the list of image vulnerabilities of an image repository
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryVulListExport(
            self,
            request: models.DescribeAssetImageRegistryVulListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryVulListExportResponse:
        """
        This API is used to export the list of vulnerabilities for an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryVulListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryVulListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRiskList(
            self,
            request: models.DescribeAssetImageRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRiskListResponse:
        """
        This API is used to query the list of risks in an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRiskListExport(
            self,
            request: models.DescribeAssetImageRiskListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRiskListExportResponse:
        """
        This API is used to export the list of risks in an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRiskListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRiskListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageScanSetting(
            self,
            request: models.DescribeAssetImageScanSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageScanSettingResponse:
        """
        This API is used to get the image scan settings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageScanStatus(
            self,
            request: models.DescribeAssetImageScanStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageScanStatusResponse:
        """
        This API is used to query the image scanning status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageScanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageScanStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageScanTask(
            self,
            request: models.DescribeAssetImageScanTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageScanTaskResponse:
        """
        This API is used to query the ID of a running quick image scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageSimpleList(
            self,
            request: models.DescribeAssetImageSimpleListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageSimpleListResponse:
        """
        This API is used to query the brief information list of an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageSimpleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageSimpleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageVirusList(
            self,
            request: models.DescribeAssetImageVirusListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageVirusListResponse:
        """
        This API is used to query the list of viruses in an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageVirusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageVirusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageVirusListExport(
            self,
            request: models.DescribeAssetImageVirusListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageVirusListExportResponse:
        """
        This API is used to export the list of trojans in an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageVirusListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageVirusListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageVulList(
            self,
            request: models.DescribeAssetImageVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageVulListResponse:
        """
        This API is used to query the list of vulnerabilities in an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageVulListExport(
            self,
            request: models.DescribeAssetImageVulListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageVulListExportResponse:
        """
        This API is used to export the list of vulnerabilities in an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageVulListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageVulListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetPortList(
            self,
            request: models.DescribeAssetPortListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetPortListResponse:
        """
        This API is used to query the list of occupied ports.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetPortList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetPortListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetProcessList(
            self,
            request: models.DescribeAssetProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetProcessListResponse:
        """
        This API is used to query the list of processes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSummary(
            self,
            request: models.DescribeAssetSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSummaryResponse:
        """
        This API is used to query the statistics of containers and images under an account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSyncLastTime(
            self,
            request: models.DescribeAssetSyncLastTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSyncLastTimeResponse:
        """
        This API is used to query the last asset sync time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSyncLastTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSyncLastTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebServiceList(
            self,
            request: models.DescribeAssetWebServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebServiceListResponse:
        """
        This API is used to query the list of web services.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoAuthorizedRuleHost(
            self,
            request: models.DescribeAutoAuthorizedRuleHostRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoAuthorizedRuleHostResponse:
        """
        This API is used to query the servers licensed according to an automatic licensing rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoAuthorizedRuleHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoAuthorizedRuleHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckItemList(
            self,
            request: models.DescribeCheckItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckItemListResponse:
        """
        This API is used to query all check items and return the total number and list of check items.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDetail(
            self,
            request: models.DescribeClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDetailResponse:
        """
        This API is used to query the details of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterSummary(
            self,
            request: models.DescribeClusterSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterSummaryResponse:
        """
        This API is used to query the overview of cluster assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceAssetDetailInfo(
            self,
            request: models.DescribeComplianceAssetDetailInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceAssetDetailInfoResponse:
        """
        This API is used to query the details of an asset.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceAssetDetailInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceAssetDetailInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceAssetList(
            self,
            request: models.DescribeComplianceAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceAssetListResponse:
        """
        This API is used to query the list of assets of a certain type.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceAssetPolicyItemList(
            self,
            request: models.DescribeComplianceAssetPolicyItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceAssetPolicyItemListResponse:
        """
        This API is used to query the list of check items of an asset.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceAssetPolicyItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceAssetPolicyItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompliancePeriodTaskList(
            self,
            request: models.DescribeCompliancePeriodTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeCompliancePeriodTaskListResponse:
        """
        This API is used to query the list of scheduled tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompliancePeriodTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompliancePeriodTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompliancePolicyItemAffectedAssetList(
            self,
            request: models.DescribeCompliancePolicyItemAffectedAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeCompliancePolicyItemAffectedAssetListResponse:
        """
        This API is used to apply the asset level in the "check item + asset" two-level structure.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompliancePolicyItemAffectedAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompliancePolicyItemAffectedAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompliancePolicyItemAffectedSummary(
            self,
            request: models.DescribeCompliancePolicyItemAffectedSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeCompliancePolicyItemAffectedSummaryResponse:
        """
        This API is used to apply the check item level in the "check item + asset" two-level structure.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompliancePolicyItemAffectedSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompliancePolicyItemAffectedSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceScanFailedAssetList(
            self,
            request: models.DescribeComplianceScanFailedAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceScanFailedAssetListResponse:
        """
        This API is used to query the aggregate information of the pass rate at the asset level, the first level in the "asset + check item" two-level structure.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceScanFailedAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceScanFailedAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceTaskAssetSummary(
            self,
            request: models.DescribeComplianceTaskAssetSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceTaskAssetSummaryResponse:
        """
        This API is used to query the aggregated information of the asset pass rate in the last task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceTaskAssetSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceTaskAssetSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceTaskPolicyItemSummaryList(
            self,
            request: models.DescribeComplianceTaskPolicyItemSummaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceTaskPolicyItemSummaryListResponse:
        """
        This API is used to query the list of aggregated information of check items identified in the last task in line with the "check item + asset" two-level structure.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceTaskPolicyItemSummaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceTaskPolicyItemSummaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceWhitelistItemList(
            self,
            request: models.DescribeComplianceWhitelistItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceWhitelistItemListResponse:
        """
        This API is used to query the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceWhitelistItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceWhitelistItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContainerAssetSummary(
            self,
            request: models.DescribeContainerAssetSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeContainerAssetSummaryResponse:
        """
        This API is used to query the asset overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContainerAssetSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContainerAssetSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContainerSecEventSummary(
            self,
            request: models.DescribeContainerSecEventSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeContainerSecEventSummaryResponse:
        """
        This API is used to query the overview of pending events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContainerSecEventSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContainerSecEventSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeESAggregations(
            self,
            request: models.DescribeESAggregationsRequest,
            opts: Dict = None,
    ) -> models.DescribeESAggregationsResponse:
        """
        This API is used to get the aggregation result of the ES field.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeESAggregations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeESAggregationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeESHits(
            self,
            request: models.DescribeESHitsRequest,
            opts: Dict = None,
    ) -> models.DescribeESHitsResponse:
        """
        This API is used to get the list of ES query files.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeESHits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeESHitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEmergencyVulList(
            self,
            request: models.DescribeEmergencyVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeEmergencyVulListResponse:
        """
        This API is used to query the list of emergency vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEmergencyVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEmergencyVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeEventDetail(
            self,
            request: models.DescribeEscapeEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeEventDetailResponse:
        """
        This API is used to query the details of a container escape event.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeEventInfo(
            self,
            request: models.DescribeEscapeEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeEventInfoResponse:
        """
        This API is used to query the list of container escape events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeEventTendency(
            self,
            request: models.DescribeEscapeEventTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeEventTendencyResponse:
        """
        This API is used to query the trend of pending escape events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeEventTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeEventTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeEventTypeSummary(
            self,
            request: models.DescribeEscapeEventTypeSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeEventTypeSummaryResponse:
        """
        This API is used to query the types of container escape events and the number of pending events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeEventTypeSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeEventTypeSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeEventsExport(
            self,
            request: models.DescribeEscapeEventsExportRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeEventsExportResponse:
        """
        接口已废弃

        This API is used to export the list of container escape events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeEventsExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeEventsExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeRuleInfo(
            self,
            request: models.DescribeEscapeRuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeRuleInfoResponse:
        """
        This API is used to query the information of a container escape scan rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeSafeState(
            self,
            request: models.DescribeEscapeSafeStateRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeSafeStateResponse:
        """
        This API is used to query the container escape security status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeSafeState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeSafeStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeWhiteList(
            self,
            request: models.DescribeEscapeWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeWhiteListResponse:
        """
        This API is used to query the allowlist of escapes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportJobDownloadURL(
            self,
            request: models.DescribeExportJobDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeExportJobDownloadURLResponse:
        """
        This API is used to query the URL to download the result of an exportation task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportJobDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportJobDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportJobManageList(
            self,
            request: models.DescribeExportJobManageListRequest,
            opts: Dict = None,
    ) -> models.DescribeExportJobManageListResponse:
        """
        This API is used to query the export job management list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportJobManageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportJobManageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportJobResult(
            self,
            request: models.DescribeExportJobResultRequest,
            opts: Dict = None,
    ) -> models.DescribeExportJobResultResponse:
        """
        This API is used to query the result of an export task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportJobResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportJobResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAuthorizedInfo(
            self,
            request: models.DescribeImageAuthorizedInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAuthorizedInfoResponse:
        """
        This API is used to query the image licensing information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAuthorizedInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAuthorizedInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAutoAuthorizedLogList(
            self,
            request: models.DescribeImageAutoAuthorizedLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAutoAuthorizedLogListResponse:
        """
        This API is used to query the list of automatic image licensing results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAutoAuthorizedLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAutoAuthorizedLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAutoAuthorizedRule(
            self,
            request: models.DescribeImageAutoAuthorizedRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAutoAuthorizedRuleResponse:
        """
        This API is used to query an automatic licensing rule for local images.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAutoAuthorizedRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAutoAuthorizedRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAutoAuthorizedTaskList(
            self,
            request: models.DescribeImageAutoAuthorizedTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAutoAuthorizedTaskListResponse:
        """
        This API is used to query the list of automatic image licensing tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAutoAuthorizedTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAutoAuthorizedTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageComponentList(
            self,
            request: models.DescribeImageComponentListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageComponentListResponse:
        """
        This API is used to query the list of components in an local image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageComponentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageComponentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryNamespaceList(
            self,
            request: models.DescribeImageRegistryNamespaceListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryNamespaceListResponse:
        """
        This API is used to query the list of namespaces for an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryNamespaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryNamespaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryTimingScanTask(
            self,
            request: models.DescribeImageRegistryTimingScanTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryTimingScanTaskResponse:
        """
        This API is used to view a scheduled task of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryTimingScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryTimingScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRiskSummary(
            self,
            request: models.DescribeImageRiskSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRiskSummaryResponse:
        """
        This API is used to query the overview of local image risks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRiskSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRiskSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRiskTendency(
            self,
            request: models.DescribeImageRiskTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRiskTendencyResponse:
        """
        This API is used to query the trend of local image risks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRiskTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRiskTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageSimpleList(
            self,
            request: models.DescribeImageSimpleListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageSimpleListResponse:
        """
        This API is used to query the list of all images.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageSimpleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageSimpleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndexList(
            self,
            request: models.DescribeIndexListRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexListResponse:
        """
        This API is used to get the index list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndexList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInspectionReport(
            self,
            request: models.DescribeInspectionReportRequest,
            opts: Dict = None,
    ) -> models.DescribeInspectionReportResponse:
        """
        This API is used to query check reports.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInspectionReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInspectionReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalEventInfo(
            self,
            request: models.DescribeK8sApiAbnormalEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalEventInfoResponse:
        """
        Querying details of a K8s API exception event
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalEventList(
            self,
            request: models.DescribeK8sApiAbnormalEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalEventListResponse:
        """
        This API is used to query the K8sApi abnormal event list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalRuleInfo(
            self,
            request: models.DescribeK8sApiAbnormalRuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalRuleInfoResponse:
        """
        This API is used to query K8sApi abnormal request rule details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalRuleList(
            self,
            request: models.DescribeK8sApiAbnormalRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalRuleListResponse:
        """
        This API is used to the K8sApi abnormal request rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalRuleScopeList(
            self,
            request: models.DescribeK8sApiAbnormalRuleScopeListRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalRuleScopeListResponse:
        """
        This API is used to query rules for K8s API exceptions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalRuleScopeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalRuleScopeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalSummary(
            self,
            request: models.DescribeK8sApiAbnormalSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalSummaryResponse:
        """
        This API is used to query the statistics of K8sApi abnormal events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalTendency(
            self,
            request: models.DescribeK8sApiAbnormalTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalTendencyResponse:
        """
        This API is used to query the trend of K8sApi abnormal events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogStorageStatistic(
            self,
            request: models.DescribeLogStorageStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeLogStorageStatisticResponse:
        """
        This API is used to get the statistics of the log search usage.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogStorageStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogStorageStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallAuditRecord(
            self,
            request: models.DescribeNetworkFirewallAuditRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallAuditRecordResponse:
        """
        This API is used to query the list of cluster policy audits.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallAuditRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallAuditRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallClusterList(
            self,
            request: models.DescribeNetworkFirewallClusterListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallClusterListResponse:
        """
        This API is used to query the list of clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallClusterList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallClusterListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallClusterRefreshStatus(
            self,
            request: models.DescribeNetworkFirewallClusterRefreshStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallClusterRefreshStatusResponse:
        """
        This API is used to query the progress of the asset query task in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallClusterRefreshStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallClusterRefreshStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallNamespaceLabelList(
            self,
            request: models.DescribeNetworkFirewallNamespaceLabelListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallNamespaceLabelListResponse:
        """
        This API is used to query the list of cluster network namespace labels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallNamespaceLabelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallNamespaceLabelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPodLabelsList(
            self,
            request: models.DescribeNetworkFirewallPodLabelsListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPodLabelsListResponse:
        """
        This API is used to query cluster network Pod labels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPodLabelsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPodLabelsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPolicyDetail(
            self,
            request: models.DescribeNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPolicyDetailResponse:
        """
        This API is used to view the details of a policy in the container network cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPolicyDiscover(
            self,
            request: models.DescribeNetworkFirewallPolicyDiscoverRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPolicyDiscoverResponse:
        """
        This API is used to query the progress of a network policy sync task in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPolicyDiscover"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPolicyDiscoverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPolicyList(
            self,
            request: models.DescribeNetworkFirewallPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPolicyListResponse:
        """
        This API is used to query the list of cluster network policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPolicyStatus(
            self,
            request: models.DescribeNetworkFirewallPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPolicyStatusResponse:
        """
        This API is used to query the execution status of a network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPolicyYamlDetail(
            self,
            request: models.DescribeNetworkFirewallPolicyYamlDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPolicyYamlDetailResponse:
        """
        This API is used to view the details of a YAML network policy in the container network cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPolicyYamlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPolicyYamlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNewestVul(
            self,
            request: models.DescribeNewestVulRequest,
            opts: Dict = None,
    ) -> models.DescribeNewestVulResponse:
        """
        This API is used to query the latest list of vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNewestVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNewestVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePostPayDetail(
            self,
            request: models.DescribePostPayDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePostPayDetailResponse:
        """
        This API is used to query the pay-as-you-go billing details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePostPayDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePostPayDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProVersionInfo(
            self,
            request: models.DescribeProVersionInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProVersionInfoResponse:
        """
        This API is used to check whether the Pro Edition needs to be purchased.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProVersionInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProVersionInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePromotionActivity(
            self,
            request: models.DescribePromotionActivityRequest,
            opts: Dict = None,
    ) -> models.DescribePromotionActivityResponse:
        """
        This API is used to query promotions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePromotionActivity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePromotionActivityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicKey(
            self,
            request: models.DescribePublicKeyRequest,
            opts: Dict = None,
    ) -> models.DescribePublicKeyResponse:
        """
        This API is used to get the public key.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurchaseStateInfo(
            self,
            request: models.DescribePurchaseStateInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePurchaseStateInfoResponse:
        """
        This API is used to check whether TCSS is purchased.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurchaseStateInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurchaseStateInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRefreshTask(
            self,
            request: models.DescribeRefreshTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRefreshTaskResponse:
        """
        This API is used to query a refresh task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRefreshTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRefreshTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellDetail(
            self,
            request: models.DescribeReverseShellDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellDetailResponse:
        """
        This API is used to query the details of a reverse shell event at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellEvents(
            self,
            request: models.DescribeReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellEventsResponse:
        """
        This API is used to query the list of reverse shell events at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellEventsExport(
            self,
            request: models.DescribeReverseShellEventsExportRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellEventsExportResponse:
        """
        This API is used to query and export the list of reverse shell events at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellEventsExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellEventsExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellWhiteListDetail(
            self,
            request: models.DescribeReverseShellWhiteListDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellWhiteListDetailResponse:
        """
        This API is used to query the details of the allowlist of reverse shells at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellWhiteListDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellWhiteListDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellWhiteLists(
            self,
            request: models.DescribeReverseShellWhiteListsRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellWhiteListsResponse:
        """
        This API is used to query the allowlist of reverse shells at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskList(
            self,
            request: models.DescribeRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskListResponse:
        """
        This API is used to query the list of risk items identified in the last task and filter them by special field.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallDetail(
            self,
            request: models.DescribeRiskSyscallDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallDetailResponse:
        """
        This API is used to query the details of a high-risk syscall event.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallEvents(
            self,
            request: models.DescribeRiskSyscallEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallEventsResponse:
        """
        This API is used to query the list of high-risk syscalls at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallEventsExport(
            self,
            request: models.DescribeRiskSyscallEventsExportRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallEventsExportResponse:
        """
        This API is used to export the list of high-risk syscalls at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallEventsExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallEventsExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallNames(
            self,
            request: models.DescribeRiskSyscallNamesRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallNamesResponse:
        """
        This API is used to query the list of names of high-risk syscalls at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallNamesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallWhiteListDetail(
            self,
            request: models.DescribeRiskSyscallWhiteListDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallWhiteListDetailResponse:
        """
        This API is used to query the details of the allowlist of high-risk syscalls at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallWhiteListDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallWhiteListDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallWhiteLists(
            self,
            request: models.DescribeRiskSyscallWhiteListsRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallWhiteListsResponse:
        """
        This API is used to query the allowlist of high-risk syscalls at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanIgnoreVulList(
            self,
            request: models.DescribeScanIgnoreVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanIgnoreVulListResponse:
        """
        This API is used to query the list of vulnerabilities ignored in a scan.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanIgnoreVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanIgnoreVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchExportList(
            self,
            request: models.DescribeSearchExportListRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchExportListResponse:
        """
        This API is used to export the list of ES query files.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchExportList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchExportListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchLogs(
            self,
            request: models.DescribeSearchLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchLogsResponse:
        """
        This API is used to get historical search records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchTemplates(
            self,
            request: models.DescribeSearchTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchTemplatesResponse:
        """
        This API is used to get the list of search templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecEventsTendency(
            self,
            request: models.DescribeSecEventsTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeSecEventsTendencyResponse:
        """
        This API is used to query the trend of security events at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecEventsTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecEventsTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogAlertMsg(
            self,
            request: models.DescribeSecLogAlertMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogAlertMsgResponse:
        """
        This API is used to query a security log alert message.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogAlertMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogAlertMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogCleanSettingInfo(
            self,
            request: models.DescribeSecLogCleanSettingInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogCleanSettingInfoResponse:
        """
        This API is used to query the settings of security log cleanup.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogCleanSettingInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogCleanSettingInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogDeliveryClsOptions(
            self,
            request: models.DescribeSecLogDeliveryClsOptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogDeliveryClsOptionsResponse:
        """
        This API is used to query the options of security log delivery to CLS.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogDeliveryClsOptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogDeliveryClsOptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogDeliveryClsSetting(
            self,
            request: models.DescribeSecLogDeliveryClsSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogDeliveryClsSettingResponse:
        """
        This API is used to query the settings of security log delivery to CLS.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogDeliveryClsSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogDeliveryClsSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogDeliveryKafkaOptions(
            self,
            request: models.DescribeSecLogDeliveryKafkaOptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogDeliveryKafkaOptionsResponse:
        """
        This API is used to query the options of security log delivery to Kafka.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogDeliveryKafkaOptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogDeliveryKafkaOptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogDeliveryKafkaSetting(
            self,
            request: models.DescribeSecLogDeliveryKafkaSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogDeliveryKafkaSettingResponse:
        """
        This API is used to query the settings of security log delivery to Kafka.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogDeliveryKafkaSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogDeliveryKafkaSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogJoinObjectList(
            self,
            request: models.DescribeSecLogJoinObjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogJoinObjectListResponse:
        """
        This API is used to query the list of accessed security log objects.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogJoinObjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogJoinObjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogJoinTypeList(
            self,
            request: models.DescribeSecLogJoinTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogJoinTypeListResponse:
        """
        This API is used to query the list of security log access types.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogJoinTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogJoinTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogKafkaUIN(
            self,
            request: models.DescribeSecLogKafkaUINRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogKafkaUINResponse:
        """
        This API is used to query the UIN of a Kafka security log.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogKafkaUIN"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogKafkaUINResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogVasInfo(
            self,
            request: models.DescribeSecLogVasInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogVasInfoResponse:
        """
        This API is used to query the information of the security log product.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogVasInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogVasInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportDefenceVul(
            self,
            request: models.DescribeSupportDefenceVulRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportDefenceVulResponse:
        """
        This API is used to query the list of vulnerabilities that can be prevented
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportDefenceVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportDefenceVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSystemVulList(
            self,
            request: models.DescribeSystemVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeSystemVulListResponse:
        """
        This API is used to query the list of system vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSystemVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSystemVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResultSummary(
            self,
            request: models.DescribeTaskResultSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResultSummaryResponse:
        """
        This API is used to query the overview of a check result and return the number of affected nodes in the last seven days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResultSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResultSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTcssSummary(
            self,
            request: models.DescribeTcssSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeTcssSummaryResponse:
        """
        This API is used to query the TCSS overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTcssSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTcssSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnauthorizedCoresTendency(
            self,
            request: models.DescribeUnauthorizedCoresTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeUnauthorizedCoresTendencyResponse:
        """
        This API is used to query the trend of daily unlicensed cores.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnauthorizedCoresTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnauthorizedCoresTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnfinishRefreshTask(
            self,
            request: models.DescribeUnfinishRefreshTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeUnfinishRefreshTaskResponse:
        """
        This API is used to query the information of an unfinished asset refreshing task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnfinishRefreshTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnfinishRefreshTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCluster(
            self,
            request: models.DescribeUserClusterRequest,
            opts: Dict = None,
    ) -> models.DescribeUserClusterResponse:
        """
        This API is used to query the information of a cluster on the Security Dashboard and Cluster Security pages.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeValueAddedSrvInfo(
            self,
            request: models.DescribeValueAddedSrvInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeValueAddedSrvInfoResponse:
        """
        This API is used to query the information of the required value-added service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeValueAddedSrvInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeValueAddedSrvInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusAutoIsolateSampleDetail(
            self,
            request: models.DescribeVirusAutoIsolateSampleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusAutoIsolateSampleDetailResponse:
        """
        This API is used to query the details of an automatically isolated trojan sample.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusAutoIsolateSampleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusAutoIsolateSampleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusAutoIsolateSampleDownloadURL(
            self,
            request: models.DescribeVirusAutoIsolateSampleDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusAutoIsolateSampleDownloadURLResponse:
        """
        This API is used to query the download URL of an automatically isolated trojan sample.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusAutoIsolateSampleDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusAutoIsolateSampleDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusAutoIsolateSampleList(
            self,
            request: models.DescribeVirusAutoIsolateSampleListRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusAutoIsolateSampleListResponse:
        """
        This API is used to query the list of automatically isolated trojan samples.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusAutoIsolateSampleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusAutoIsolateSampleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusAutoIsolateSetting(
            self,
            request: models.DescribeVirusAutoIsolateSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusAutoIsolateSettingResponse:
        """
        This API is used to query the settings of automatic trojan isolation.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusAutoIsolateSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusAutoIsolateSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusDetail(
            self,
            request: models.DescribeVirusDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusDetailResponse:
        """
        This API is used to query the information of a trojan file at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusEventTendency(
            self,
            request: models.DescribeVirusEventTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusEventTendencyResponse:
        """
        This API is used to query the trend of trojan events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusEventTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusEventTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusList(
            self,
            request: models.DescribeVirusListRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusListResponse:
        """
        This API is used to query the list of virus scanning events at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusManualScanEstimateTimeout(
            self,
            request: models.DescribeVirusManualScanEstimateTimeoutRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusManualScanEstimateTimeoutResponse:
        """
        This API is used to query the estimated timeout period of a quick trojan scan.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusManualScanEstimateTimeout"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusManualScanEstimateTimeoutResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusMonitorSetting(
            self,
            request: models.DescribeVirusMonitorSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusMonitorSettingResponse:
        """
        This API is used to query the real-time monitoring settings of virus scanning at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusMonitorSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusMonitorSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusSampleDownloadUrl(
            self,
            request: models.DescribeVirusSampleDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusSampleDownloadUrlResponse:
        """
        This API is used to query the download URL of a trojan sample.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusSampleDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusSampleDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusScanSetting(
            self,
            request: models.DescribeVirusScanSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusScanSettingResponse:
        """
        This API is used to query virus scanning settings at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusScanTaskStatus(
            self,
            request: models.DescribeVirusScanTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusScanTaskStatusResponse:
        """
        This API is used to query the status of a virus scanning task at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusScanTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusScanTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusScanTimeoutSetting(
            self,
            request: models.DescribeVirusScanTimeoutSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusScanTimeoutSettingResponse:
        """
        This API is used to query the timeout settings of a file scan at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusScanTimeoutSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusScanTimeoutSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusSummary(
            self,
            request: models.DescribeVirusSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusSummaryResponse:
        """
        This API is used to query the trojan overview at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusTaskList(
            self,
            request: models.DescribeVirusTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusTaskListResponse:
        """
        This API is used to query the list of virus scanning tasks at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulContainerList(
            self,
            request: models.DescribeVulContainerListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulContainerListResponse:
        """
        This API is used to query the list of containers affected by vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulContainerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulContainerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceEvent(
            self,
            request: models.DescribeVulDefenceEventRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceEventResponse:
        """
        This API is used to query the list of exploit prevention events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceEventDetail(
            self,
            request: models.DescribeVulDefenceEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceEventDetailResponse:
        """
        This API is used to query the details of an exploit prevention event.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceEventTendency(
            self,
            request: models.DescribeVulDefenceEventTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceEventTendencyResponse:
        """
        This API is used to query the trend of exploit prevention events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceEventTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceEventTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceHost(
            self,
            request: models.DescribeVulDefenceHostRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceHostResponse:
        """
        This API is used to query the list of servers with exploit prevention enabled.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefencePlugin(
            self,
            request: models.DescribeVulDefencePluginRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefencePluginResponse:
        """
        This API is used to query the list of exploit prevention plugins.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefencePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefencePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceSetting(
            self,
            request: models.DescribeVulDefenceSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceSettingResponse:
        """
        This API is used to query the exploit prevention settings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDetail(
            self,
            request: models.DescribeVulDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDetailResponse:
        """
        This API is used to query vulnerability details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulIgnoreLocalImageList(
            self,
            request: models.DescribeVulIgnoreLocalImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulIgnoreLocalImageListResponse:
        """
        This API is used to query the list of local images ignored in a vulnerability scan.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulIgnoreLocalImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulIgnoreLocalImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulIgnoreRegistryImageList(
            self,
            request: models.DescribeVulIgnoreRegistryImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulIgnoreRegistryImageListResponse:
        """
        This API is used to query the list of repository images ignored in a vulnerability scan.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulIgnoreRegistryImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulIgnoreRegistryImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulImageList(
            self,
            request: models.DescribeVulImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulImageListResponse:
        """
        This API is used to query the list of images affected by vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulImageSummary(
            self,
            request: models.DescribeVulImageSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVulImageSummaryResponse:
        """
        This API is used to query the statistics of images affected by vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulImageSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulImageSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulLevelImageSummary(
            self,
            request: models.DescribeVulLevelImageSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVulLevelImageSummaryResponse:
        """
        This API is used to query the numbers of images affected by emergency vulnerabilities at each severity level.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulLevelImageSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulLevelImageSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulLevelSummary(
            self,
            request: models.DescribeVulLevelSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVulLevelSummaryResponse:
        """
        This API is used to query the numbers of vulnerabilities at each severity level.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulLevelSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulLevelSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulRegistryImageList(
            self,
            request: models.DescribeVulRegistryImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulRegistryImageListResponse:
        """
        This API is used to query the list of repository images affected by vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulRegistryImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulRegistryImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanAuthorizedImageSummary(
            self,
            request: models.DescribeVulScanAuthorizedImageSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanAuthorizedImageSummaryResponse:
        """
        This API is used to count the number of licensed but not scanned images on the vulnerability scanning page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanAuthorizedImageSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanAuthorizedImageSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanInfo(
            self,
            request: models.DescribeVulScanInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanInfoResponse:
        """
        This API is used to query the information of a vulnerability scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanLocalImageList(
            self,
            request: models.DescribeVulScanLocalImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanLocalImageListResponse:
        """
        This API is used to query the list of local images in a vulnerability scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanLocalImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanLocalImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulSummary(
            self,
            request: models.DescribeVulSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVulSummaryResponse:
        """
        This API is used to query the overview of vulnerability risks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulTendency(
            self,
            request: models.DescribeVulTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeVulTendencyResponse:
        """
        This API is used to query the trend of critical and high-risk vulnerabilities in local and repository images.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulTopRanking(
            self,
            request: models.DescribeVulTopRankingRequest,
            opts: Dict = None,
    ) -> models.DescribeVulTopRankingResponse:
        """
        This API is used to query the list of top vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulTopRanking"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulTopRankingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWarningRules(
            self,
            request: models.DescribeWarningRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeWarningRulesResponse:
        """
        This API is used to get the list of alert policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWarningRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWarningRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebVulList(
            self,
            request: models.DescribeWebVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeWebVulListResponse:
        """
        This API is used to query the list of web application vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVirusList(
            self,
            request: models.ExportVirusListRequest,
            opts: Dict = None,
    ) -> models.ExportVirusListResponse:
        """
        This API is used to export the list of virus scanning events at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVirusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVirusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InitializeUserComplianceEnvironment(
            self,
            request: models.InitializeUserComplianceEnvironmentRequest,
            opts: Dict = None,
    ) -> models.InitializeUserComplianceEnvironmentResponse:
        """
        This API is used to initialize the compliance baseline environment and create necessary data and options.
        """
        
        kwargs = {}
        kwargs["action"] = "InitializeUserComplianceEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InitializeUserComplianceEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAbnormalProcessRuleStatus(
            self,
            request: models.ModifyAbnormalProcessRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAbnormalProcessRuleStatusResponse:
        """
        This API is used to change the status of an abnormal process policy at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAbnormalProcessRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAbnormalProcessRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAbnormalProcessStatus(
            self,
            request: models.ModifyAbnormalProcessStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAbnormalProcessStatusResponse:
        """
        This API is used to change the status of an abnormal process event.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAbnormalProcessStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAbnormalProcessStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessControlRuleStatus(
            self,
            request: models.ModifyAccessControlRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessControlRuleStatusResponse:
        """
        This API is used to change the status of an access control policy at runtime, i.e., enable or disable it.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessControlRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessControlRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessControlStatus(
            self,
            request: models.ModifyAccessControlStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessControlStatusResponse:
        """
        This API is used to change the status of an access control event at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessControlStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessControlStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAsset(
            self,
            request: models.ModifyAssetRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetResponse:
        """
        This API is used to refresh server assets.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetImageRegistryScanStop(
            self,
            request: models.ModifyAssetImageRegistryScanStopRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetImageRegistryScanStopResponse:
        """
        This API is used to stop an image scan task for an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetImageRegistryScanStop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetImageRegistryScanStopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetImageRegistryScanStopOneKey(
            self,
            request: models.ModifyAssetImageRegistryScanStopOneKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetImageRegistryScanStopOneKeyResponse:
        """
        This API is used to stop a quick image scan task for an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetImageRegistryScanStopOneKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetImageRegistryScanStopOneKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetImageScanStop(
            self,
            request: models.ModifyAssetImageScanStopRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetImageScanStopResponse:
        """
        This API is used to stop an image scan.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetImageScanStop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetImageScanStopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCompliancePeriodTask(
            self,
            request: models.ModifyCompliancePeriodTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyCompliancePeriodTaskResponse:
        """
        This API is used to modify the settings of a scheduled task, including the check cycle and the status of the compliance benchmark.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCompliancePeriodTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCompliancePeriodTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyContainerNetStatus(
            self,
            request: models.ModifyContainerNetStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyContainerNetStatusResponse:
        """
        This API is used to isolate a container.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContainerNetStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContainerNetStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEscapeEventStatus(
            self,
            request: models.ModifyEscapeEventStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEscapeEventStatusResponse:
        """
        This API is used to change the status of a container escape scan event.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEscapeEventStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEscapeEventStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEscapeRule(
            self,
            request: models.ModifyEscapeRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyEscapeRuleResponse:
        """
        This API is used to modify the information of a container escape scan rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEscapeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEscapeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEscapeWhiteList(
            self,
            request: models.ModifyEscapeWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyEscapeWhiteListResponse:
        """
        This API is used to modify an allowed escape.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEscapeWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEscapeWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageAuthorized(
            self,
            request: models.ModifyImageAuthorizedRequest,
            opts: Dict = None,
    ) -> models.ModifyImageAuthorizedResponse:
        """
        This API is used to batch license images to be scanned (v2.0).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageAuthorized"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageAuthorizedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyK8sApiAbnormalEventStatus(
            self,
            request: models.ModifyK8sApiAbnormalEventStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyK8sApiAbnormalEventStatusResponse:
        """
        This API is used to modify the status of K8sApi exception events.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyK8sApiAbnormalEventStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyK8sApiAbnormalEventStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyK8sApiAbnormalRuleInfo(
            self,
            request: models.ModifyK8sApiAbnormalRuleInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyK8sApiAbnormalRuleInfoResponse:
        """
        This API is used to modify the information of K8sApi abnormal rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyK8sApiAbnormalRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyK8sApiAbnormalRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyK8sApiAbnormalRuleStatus(
            self,
            request: models.ModifyK8sApiAbnormalRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyK8sApiAbnormalRuleStatusResponse:
        """
        This API is used to modify the status of K8sApi abnormal event rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyK8sApiAbnormalRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyK8sApiAbnormalRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReverseShellStatus(
            self,
            request: models.ModifyReverseShellStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyReverseShellStatusResponse:
        """
        This API is used to change the status of a reverse shell event.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReverseShellStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReverseShellStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskSyscallStatus(
            self,
            request: models.ModifyRiskSyscallStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskSyscallStatusResponse:
        """
        This API is used to change the status of a high-risk syscall event.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskSyscallStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskSyscallStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogCleanSettingInfo(
            self,
            request: models.ModifySecLogCleanSettingInfoRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogCleanSettingInfoResponse:
        """
        This API is used to modify the settings of security log cleanup.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogCleanSettingInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogCleanSettingInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogDeliveryClsSetting(
            self,
            request: models.ModifySecLogDeliveryClsSettingRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogDeliveryClsSettingResponse:
        """
        This API is used to update the configuration of security log delivery to CLS.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogDeliveryClsSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogDeliveryClsSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogDeliveryKafkaSetting(
            self,
            request: models.ModifySecLogDeliveryKafkaSettingRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogDeliveryKafkaSettingResponse:
        """
        This API is used to update the settings of security log delivery to Kafka.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogDeliveryKafkaSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogDeliveryKafkaSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogJoinObjects(
            self,
            request: models.ModifySecLogJoinObjectsRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogJoinObjectsResponse:
        """
        This API is used to modify an accessed security log object.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogJoinObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogJoinObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogJoinState(
            self,
            request: models.ModifySecLogJoinStateRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogJoinStateResponse:
        """
        This API is used to change the security log access status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogJoinState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogJoinStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogKafkaUIN(
            self,
            request: models.ModifySecLogKafkaUINRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogKafkaUINResponse:
        """
        This API is used to modify the UIN of a Kafka security log.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogKafkaUIN"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogKafkaUINResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusAutoIsolateExampleSwitch(
            self,
            request: models.ModifyVirusAutoIsolateExampleSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusAutoIsolateExampleSwitchResponse:
        """
        This API is used to enable/disable automatic trojan sample isolation.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusAutoIsolateExampleSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusAutoIsolateExampleSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusAutoIsolateSetting(
            self,
            request: models.ModifyVirusAutoIsolateSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusAutoIsolateSettingResponse:
        """
        This API is used to modify the settings of automatic trojan isolation.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusAutoIsolateSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusAutoIsolateSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusFileStatus(
            self,
            request: models.ModifyVirusFileStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusFileStatusResponse:
        """
        This API is used to update the status of a trojan file at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusFileStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusFileStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusMonitorSetting(
            self,
            request: models.ModifyVirusMonitorSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusMonitorSettingResponse:
        """
        This API is used to update the real-time monitoring settings of virus scanning at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusMonitorSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusMonitorSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusScanSetting(
            self,
            request: models.ModifyVirusScanSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusScanSettingResponse:
        """
        This API is used to update virus scanning settings at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusScanTimeoutSetting(
            self,
            request: models.ModifyVirusScanTimeoutSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusScanTimeoutSettingResponse:
        """
        This API is used to modify the timeout settings of a file scan at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusScanTimeoutSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusScanTimeoutSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulDefenceEventStatus(
            self,
            request: models.ModifyVulDefenceEventStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyVulDefenceEventStatusResponse:
        """
        This API is used to change the status of an exploit prevention event.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulDefenceEventStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulDefenceEventStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulDefenceSetting(
            self,
            request: models.ModifyVulDefenceSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVulDefenceSettingResponse:
        """
        This API is used to edit the exploit prevention settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulDefenceSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulDefenceSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenTcssTrial(
            self,
            request: models.OpenTcssTrialRequest,
            opts: Dict = None,
    ) -> models.OpenTcssTrialResponse:
        """
        This API is used to activate TCSS trial.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenTcssTrial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenTcssTrialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveAssetImageRegistryRegistryDetail(
            self,
            request: models.RemoveAssetImageRegistryRegistryDetailRequest,
            opts: Dict = None,
    ) -> models.RemoveAssetImageRegistryRegistryDetailResponse:
        """
        This API is used to delete the details of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveAssetImageRegistryRegistryDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveAssetImageRegistryRegistryDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewImageAuthorizeState(
            self,
            request: models.RenewImageAuthorizeStateRequest,
            opts: Dict = None,
    ) -> models.RenewImageAuthorizeStateResponse:
        """
        This API is used to license an image to be scanned.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewImageAuthorizeState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewImageAuthorizeStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetSecLogTopicConfig(
            self,
            request: models.ResetSecLogTopicConfigRequest,
            opts: Dict = None,
    ) -> models.ResetSecLogTopicConfigResponse:
        """
        This API is used to reset a security log topic.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetSecLogTopicConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetSecLogTopicConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanComplianceAssets(
            self,
            request: models.ScanComplianceAssetsRequest,
            opts: Dict = None,
    ) -> models.ScanComplianceAssetsResponse:
        """
        This API is used to check the specified asset again.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanComplianceAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanComplianceAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanComplianceAssetsByPolicyItem(
            self,
            request: models.ScanComplianceAssetsByPolicyItemRequest,
            opts: Dict = None,
    ) -> models.ScanComplianceAssetsByPolicyItemResponse:
        """
        This API is used to check the specified asset again with the specified check item and return the ID of the created compliance check task.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanComplianceAssetsByPolicyItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanComplianceAssetsByPolicyItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanCompliancePolicyItems(
            self,
            request: models.ScanCompliancePolicyItemsRequest,
            opts: Dict = None,
    ) -> models.ScanCompliancePolicyItemsResponse:
        """
        This API is used to check all the assets of the specified check item again and return the ID of the created compliance check task.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanCompliancePolicyItems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanCompliancePolicyItemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanComplianceScanFailedAssets(
            self,
            request: models.ScanComplianceScanFailedAssetsRequest,
            opts: Dict = None,
    ) -> models.ScanComplianceScanFailedAssetsResponse:
        """
        This API is used to check all the failed check items of the specified asset again and return the ID of the created compliance check task.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanComplianceScanFailedAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanComplianceScanFailedAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetCheckMode(
            self,
            request: models.SetCheckModeRequest,
            opts: Dict = None,
    ) -> models.SetCheckModeResponse:
        """
        This API is used to set the check mode and automatic check.
        """
        
        kwargs = {}
        kwargs["action"] = "SetCheckMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetCheckModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopVirusScanTask(
            self,
            request: models.StopVirusScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopVirusScanTaskResponse:
        """
        This API is used to stop a trojan scan task at runtime.
        """
        
        kwargs = {}
        kwargs["action"] = "StopVirusScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopVirusScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopVulScanTask(
            self,
            request: models.StopVulScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopVulScanTaskResponse:
        """
        This API is used to stop a vulnerability scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "StopVulScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopVulScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchImageAutoAuthorizedRule(
            self,
            request: models.SwitchImageAutoAuthorizedRuleRequest,
            opts: Dict = None,
    ) -> models.SwitchImageAutoAuthorizedRuleResponse:
        """
        This API is used to enable/disable automatic licensing for local images.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchImageAutoAuthorizedRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchImageAutoAuthorizedRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncAssetImageRegistryAsset(
            self,
            request: models.SyncAssetImageRegistryAssetRequest,
            opts: Dict = None,
    ) -> models.SyncAssetImageRegistryAssetResponse:
        """
        This API is used to refresh the assets in an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "SyncAssetImageRegistryAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncAssetImageRegistryAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAndPublishNetworkFirewallPolicyDetail(
            self,
            request: models.UpdateAndPublishNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.UpdateAndPublishNetworkFirewallPolicyDetailResponse:
        """
        This API is used to create a task to update and publish a network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAndPublishNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAndPublishNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAndPublishNetworkFirewallPolicyYamlDetail(
            self,
            request: models.UpdateAndPublishNetworkFirewallPolicyYamlDetailRequest,
            opts: Dict = None,
    ) -> models.UpdateAndPublishNetworkFirewallPolicyYamlDetailResponse:
        """
        This API is used to create a task to update and publish a YAML network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAndPublishNetworkFirewallPolicyYamlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAndPublishNetworkFirewallPolicyYamlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAssetImageRegistryRegistryDetail(
            self,
            request: models.UpdateAssetImageRegistryRegistryDetailRequest,
            opts: Dict = None,
    ) -> models.UpdateAssetImageRegistryRegistryDetailResponse:
        """
        This API is used to update the details of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAssetImageRegistryRegistryDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAssetImageRegistryRegistryDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateImageRegistryTimingScanTask(
            self,
            request: models.UpdateImageRegistryTimingScanTaskRequest,
            opts: Dict = None,
    ) -> models.UpdateImageRegistryTimingScanTaskResponse:
        """
        This API is used to update a scheduled task for an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateImageRegistryTimingScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateImageRegistryTimingScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateNetworkFirewallPolicyDetail(
            self,
            request: models.UpdateNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.UpdateNetworkFirewallPolicyDetailResponse:
        """
        This API is used to create a task to update a network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateNetworkFirewallPolicyYamlDetail(
            self,
            request: models.UpdateNetworkFirewallPolicyYamlDetailRequest,
            opts: Dict = None,
    ) -> models.UpdateNetworkFirewallPolicyYamlDetailResponse:
        """
        This API is used to create a task to update a YAML network policy in the container network.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateNetworkFirewallPolicyYamlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateNetworkFirewallPolicyYamlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)