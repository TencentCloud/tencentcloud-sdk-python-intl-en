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
from tencentcloud.cwp.v20180228 import models
from typing import Dict


class CwpClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'cwp.intl.tencentcloudapi.com'
    _service = 'cwp'

    async def AddLoginWhiteLists(
            self,
            request: models.AddLoginWhiteListsRequest,
            opts: Dict = None,
    ) -> models.AddLoginWhiteListsResponse:
        """
        This API is used to add cross-region log-in allowlists in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "AddLoginWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddLoginWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelIgnoreVul(
            self,
            request: models.CancelIgnoreVulRequest,
            opts: Dict = None,
    ) -> models.CancelIgnoreVulResponse:
        """
        This API is used to unignore the vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelIgnoreVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelIgnoreVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeRuleEventsIgnoreStatus(
            self,
            request: models.ChangeRuleEventsIgnoreStatusRequest,
            opts: Dict = None,
    ) -> models.ChangeRuleEventsIgnoreStatusResponse:
        """
        This API is used to ignore events or cancel ignoring in batches based on check item ID or event ID.
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeRuleEventsIgnoreStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeRuleEventsIgnoreStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeStrategyEnableStatus(
            self,
            request: models.ChangeStrategyEnableStatusRequest,
            opts: Dict = None,
    ) -> models.ChangeStrategyEnableStatusResponse:
        """
        This API is used to change the policy availability status by policy ID.
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeStrategyEnableStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeStrategyEnableStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBashPolicyParams(
            self,
            request: models.CheckBashPolicyParamsRequest,
            opts: Dict = None,
    ) -> models.CheckBashPolicyParamsResponse:
        """
        This API is used to verify parameters entered for adding and editing high-risk command user rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBashPolicyParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBashPolicyParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBashRuleParams(
            self,
            request: models.CheckBashRuleParamsRequest,
            opts: Dict = None,
    ) -> models.CheckBashRuleParamsResponse:
        """
        This API is used to verify parameters entered for adding and editing high-risk command user rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBashRuleParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBashRuleParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckFileTamperRule(
            self,
            request: models.CheckFileTamperRuleRequest,
            opts: Dict = None,
    ) -> models.CheckFileTamperRuleResponse:
        """
        This API is used to check the rule parameters entered at the core file monitoring frontend.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckFileTamperRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckFileTamperRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckFirstScanBaseline(
            self,
            request: models.CheckFirstScanBaselineRequest,
            opts: Dict = None,
    ) -> models.CheckFirstScanBaselineResponse:
        """
        This API is used to query whether the baseline is detected for the first time.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckFirstScanBaseline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckFirstScanBaselineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckLogKafkaConnectionState(
            self,
            request: models.CheckLogKafkaConnectionStateRequest,
            opts: Dict = None,
    ) -> models.CheckLogKafkaConnectionStateResponse:
        """
        This API is used to check the connectivity for log shipping from Kafka.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckLogKafkaConnectionState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckLogKafkaConnectionStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearLocalStorage(
            self,
            request: models.ClearLocalStorageRequest,
            opts: Dict = None,
    ) -> models.ClearLocalStorageResponse:
        """
        This API is used to clean up the locally stored data.
        """
        
        kwargs = {}
        kwargs["action"] = "ClearLocalStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearLocalStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBanWhiteList(
            self,
            request: models.CreateBanWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateBanWhiteListResponse:
        """
        This API is used to add the list of block allowlists.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBanWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBanWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaselineStrategy(
            self,
            request: models.CreateBaselineStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateBaselineStrategyResponse:
        """
        This API is used to create a baseline policy based on the policy information.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaselineStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaselineStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBuyBindTask(
            self,
            request: models.CreateBuyBindTaskRequest,
            opts: Dict = None,
    ) -> models.CreateBuyBindTaskResponse:
        """
        This API is used to create an automatic binding task for newly purchased authorizations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBuyBindTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBuyBindTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmergencyVulScan(
            self,
            request: models.CreateEmergencyVulScanRequest,
            opts: Dict = None,
    ) -> models.CreateEmergencyVulScanResponse:
        """
        This API is used to create emergency vulnerability scan tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmergencyVulScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmergencyVulScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIncidentBacktracking(
            self,
            request: models.CreateIncidentBacktrackingRequest,
            opts: Dict = None,
    ) -> models.CreateIncidentBacktrackingResponse:
        """
        This API is used to trigger event investigation and alarm backtracking for Ultimate Edition machines.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIncidentBacktracking"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIncidentBacktrackingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLicenseOrder(
            self,
            request: models.CreateLicenseOrderRequest,
            opts: Dict = None,
    ) -> models.CreateLicenseOrderResponse:
        """
        This API is used to create Professional/Flagship edition orders
        .This API is used to support creating orders through prepaid and pay-as-you-go.
        This API is used to directly create postpaid orders.
        This API is used to call the billing payment API for payment since prepaid orders are only placed but not paid.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLicenseOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLicenseOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLogExport(
            self,
            request: models.CreateLogExportRequest,
            opts: Dict = None,
    ) -> models.CreateLogExportResponse:
        """
        This API is used to create log download tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMaliciousRequestWhiteList(
            self,
            request: models.CreateMaliciousRequestWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateMaliciousRequestWhiteListResponse:
        """
        This API is used to add malicious request allowlists.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMaliciousRequestWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMaliciousRequestWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMalwareWhiteList(
            self,
            request: models.CreateMalwareWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateMalwareWhiteListResponse:
        """
        This API is used to create the Trojan allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMalwareWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMalwareWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetAttackWhiteList(
            self,
            request: models.CreateNetAttackWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateNetAttackWhiteListResponse:
        """
        This API is used to create a network attack allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetAttackWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetAttackWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRansomDefenseStrategy(
            self,
            request: models.CreateRansomDefenseStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateRansomDefenseStrategyResponse:
        """
        This API is used to create or modify anti-ransomware policies.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRansomDefenseStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRansomDefenseStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScanMalwareSetting(
            self,
            request: models.CreateScanMalwareSettingRequest,
            opts: Dict = None,
    ) -> models.CreateScanMalwareSettingResponse:
        """
        This API is used to detect the intrusion and virus scanning.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScanMalwareSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScanMalwareSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSearchLog(
            self,
            request: models.CreateSearchLogRequest,
            opts: Dict = None,
    ) -> models.CreateSearchLogResponse:
        """
        This API is used to add history search records.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSearchTemplate(
            self,
            request: models.CreateSearchTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSearchTemplateResponse:
        """
        This API is used to add the	retrieval template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSearchTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSearchTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulFix(
            self,
            request: models.CreateVulFixRequest,
            opts: Dict = None,
    ) -> models.CreateVulFixResponse:
        """
        This API is used to submit the vulnerabilities and fix them.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulFix"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulFixResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWhiteListOrder(
            self,
            request: models.CreateWhiteListOrderRequest,
            opts: Dict = None,
    ) -> models.CreateWhiteListOrderResponse:
        """
        This API is used to create allowlist orders.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWhiteListOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWhiteListOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAllJavaMemShells(
            self,
            request: models.DeleteAllJavaMemShellsRequest,
            opts: Dict = None,
    ) -> models.DeleteAllJavaMemShellsResponse:
        """
        This API is used to delete all Java webshell events.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAllJavaMemShells"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAllJavaMemShellsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBanWhiteList(
            self,
            request: models.DeleteBanWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteBanWhiteListResponse:
        """
        This API is used to delete the list of blocking allowlists.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBanWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBanWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBaselinePolicy(
            self,
            request: models.DeleteBaselinePolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteBaselinePolicyResponse:
        """
        This API is used to delete the baseline policy configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBaselinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBaselinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBaselineStrategy(
            self,
            request: models.DeleteBaselineStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteBaselineStrategyResponse:
        """
        This API is used to delete the policy by baseline policy ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBaselineStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBaselineStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBashEvents(
            self,
            request: models.DeleteBashEventsRequest,
            opts: Dict = None,
    ) -> models.DeleteBashEventsResponse:
        """
        This API is used to delete high-risk command events based on IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBashEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBashEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBashPolicies(
            self,
            request: models.DeleteBashPoliciesRequest,
            opts: Dict = None,
    ) -> models.DeleteBashPoliciesResponse:
        """
        This API is used to delete high-risk command policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBashPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBashPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBashRules(
            self,
            request: models.DeleteBashRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteBashRulesResponse:
        """
        This API is used to delete high-risk command rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBruteAttacks(
            self,
            request: models.DeleteBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.DeleteBruteAttacksResponse:
        """
        This API is used to delete brute force attack records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLicenseRecord(
            self,
            request: models.DeleteLicenseRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteLicenseRecordResponse:
        """
        This API is used to delete expired orders in Authorization Management - Order List. (Deleted orders are not counted in statistics.)
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLicenseRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLicenseRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLicenseRecordAll(
            self,
            request: models.DeleteLicenseRecordAllRequest,
            opts: Dict = None,
    ) -> models.DeleteLicenseRecordAllResponse:
        """
        This API is used to delete all authorization records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLicenseRecordAll"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLicenseRecordAllResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogExport(
            self,
            request: models.DeleteLogExportRequest,
            opts: Dict = None,
    ) -> models.DeleteLogExportResponse:
        """
        This API is used to delete log download tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoginWhiteList(
            self,
            request: models.DeleteLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteLoginWhiteListResponse:
        """
        This API is used to delete the cross-region log-in allowlist rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachine(
            self,
            request: models.DeleteMachineRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineResponse:
        """
        This API is used to uninstall the CWPP client.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineClearHistory(
            self,
            request: models.DeleteMachineClearHistoryRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineClearHistoryResponse:
        """
        This API is used to delete clearing records of a machine.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineClearHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineClearHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineTag(
            self,
            request: models.DeleteMachineTagRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineTagResponse:
        """
        This API is used to delete tags associated with the server.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMaliciousRequestWhiteList(
            self,
            request: models.DeleteMaliciousRequestWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteMaliciousRequestWhiteListResponse:
        """
        This API is used to delete the malicious request allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMaliciousRequestWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMaliciousRequestWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMaliciousRequests(
            self,
            request: models.DeleteMaliciousRequestsRequest,
            opts: Dict = None,
    ) -> models.DeleteMaliciousRequestsResponse:
        """
        This API is used to delete malicious request records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMaliciousRequests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMaliciousRequestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMalwareScanTask(
            self,
            request: models.DeleteMalwareScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteMalwareScanTaskResponse:
        """
        This API is used to terminate the scan tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMalwareScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMalwareScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMalwareWhiteList(
            self,
            request: models.DeleteMalwareWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteMalwareWhiteListResponse:
        """
        This API is used to delete the Trojan whitelist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMalwareWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMalwareWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMalwares(
            self,
            request: models.DeleteMalwaresRequest,
            opts: Dict = None,
    ) -> models.DeleteMalwaresResponse:
        """
        This API is used to delete Trojan records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetAttackWhiteList(
            self,
            request: models.DeleteNetAttackWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteNetAttackWhiteListResponse:
        """
        This API is used to delete the network attack allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetAttackWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetAttackWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNonlocalLoginPlaces(
            self,
            request: models.DeleteNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DeleteNonlocalLoginPlacesResponse:
        """
        This API is used to delete cross-region log-in records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivilegeEvents(
            self,
            request: models.DeletePrivilegeEventsRequest,
            opts: Dict = None,
    ) -> models.DeletePrivilegeEventsResponse:
        """
        This API is used to delete local privilege escalation based on IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivilegeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivilegeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivilegeRules(
            self,
            request: models.DeletePrivilegeRulesRequest,
            opts: Dict = None,
    ) -> models.DeletePrivilegeRulesResponse:
        """
        This API is used to delete local privilege elevation rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivilegeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivilegeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReverseShellEvents(
            self,
            request: models.DeleteReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.DeleteReverseShellEventsResponse:
        """
        This API is used to delete Reverse Shell events based on IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReverseShellRules(
            self,
            request: models.DeleteReverseShellRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteReverseShellRulesResponse:
        """
        This API is used to delete Reverse Shell rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReverseShellRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReverseShellRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRiskDnsEvent(
            self,
            request: models.DeleteRiskDnsEventRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskDnsEventResponse:
        """
        This API is used to delete malicious request events.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskDnsEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskDnsEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRiskDnsPolicy(
            self,
            request: models.DeleteRiskDnsPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskDnsPolicyResponse:
        """
        This API is used to delete malicious request policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskDnsPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskDnsPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScanTask(
            self,
            request: models.DeleteScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteScanTaskResponse:
        """
        This API is used to stop scan tasks of a specified type.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSearchTemplate(
            self,
            request: models.DeleteSearchTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSearchTemplateResponse:
        """
        This API is used to delete the retrieval template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSearchTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSearchTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTags(
            self,
            request: models.DeleteTagsRequest,
            opts: Dict = None,
    ) -> models.DeleteTagsResponse:
        """
        This API is used to delete tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebHookPolicy(
            self,
            request: models.DeleteWebHookPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteWebHookPolicyResponse:
        """
        This API is used to delete alarm policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebHookPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebHookPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebHookReceiver(
            self,
            request: models.DeleteWebHookReceiverRequest,
            opts: Dict = None,
    ) -> models.DeleteWebHookReceiverResponse:
        """
        This API is used to delete the alert recipient.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebHookReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebHookReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebHookRule(
            self,
            request: models.DeleteWebHookRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteWebHookRuleResponse:
        """
        This API is used to delete the rules of WeCom chatbots.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebHookRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebHookRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeABTestConfig(
            self,
            request: models.DescribeABTestConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeABTestConfigResponse:
        """
        This API is used to obtain the current grayscale configuration of the user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeABTestConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeABTestConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAESKey(
            self,
            request: models.DescribeAESKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeAESKeyResponse:
        """
        This API is used to obtain the configured aeskey and aesiv.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAESKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAESKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountStatistics(
            self,
            request: models.DescribeAccountStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountStatisticsResponse:
        """
        This API is used to obtain the account statistics data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentInstallCommand(
            self,
            request: models.DescribeAgentInstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentInstallCommandResponse:
        """
        This API is used to obtain the agent installation command.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentInstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentInstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentInstallationToken(
            self,
            request: models.DescribeAgentInstallationTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentInstallationTokenResponse:
        """
        This API is used to obtain the token for installing the agent in a hybrid cloud environment.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentInstallationToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentInstallationTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmIncidentNodes(
            self,
            request: models.DescribeAlarmIncidentNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmIncidentNodesResponse:
        """
        This API is used to obtain all node information on the event corresponding to an alarm.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmIncidentNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmIncidentNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmVertexId(
            self,
            request: models.DescribeAlarmVertexIdRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmVertexIdResponse:
        """
        This API is used to query the list of alarm IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmVertexId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmVertexIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetAppCount(
            self,
            request: models.DescribeAssetAppCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetAppCountResponse:
        """
        This API is used to obtain the number of all software applications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetAppCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetAppCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetAppList(
            self,
            request: models.DescribeAssetAppListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetAppListResponse:
        """
        This API is used to query the application list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetAppProcessList(
            self,
            request: models.DescribeAssetAppProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetAppProcessListResponse:
        """
        This API is used to obtain the list of software's associated processes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetAppProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetAppProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetCoreModuleInfo(
            self,
            request: models.DescribeAssetCoreModuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetCoreModuleInfoResponse:
        """
        This API is used to obtain the kernel module details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetCoreModuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetCoreModuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetCoreModuleList(
            self,
            request: models.DescribeAssetCoreModuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetCoreModuleListResponse:
        """
        This API is used to query the list of asset management kernel modules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetCoreModuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetCoreModuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDatabaseCount(
            self,
            request: models.DescribeAssetDatabaseCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDatabaseCountResponse:
        """
        This API is used to obtain the number of all databases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDatabaseCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDatabaseCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDatabaseInfo(
            self,
            request: models.DescribeAssetDatabaseInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDatabaseInfoResponse:
        """
        This API is used to obtain the asset management database details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDatabaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDatabaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDatabaseList(
            self,
            request: models.DescribeAssetDatabaseListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDatabaseListResponse:
        """
        This API is used to query the list of asset management databases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDatabaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDatabaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDiskList(
            self,
            request: models.DescribeAssetDiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDiskListResponse:
        """
        This API is used to obtain the host disk partition list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetEnvList(
            self,
            request: models.DescribeAssetEnvListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetEnvListResponse:
        """
        This API is used to query the list of asset management environment variables.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetEnvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetEnvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetHostTotalCount(
            self,
            request: models.DescribeAssetHostTotalCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetHostTotalCountResponse:
        """
        This API is used to obtain the total number of resources of the host.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetHostTotalCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetHostTotalCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetInfo(
            self,
            request: models.DescribeAssetInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetInfoResponse:
        """
        This API is used to obtain the number of assets, including hosts, accounts, ports, processes, software, databases, web applications, web frameworks, web services, and web sites.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetInitServiceList(
            self,
            request: models.DescribeAssetInitServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetInitServiceListResponse:
        """
        This API is used to query the list of asset management start services.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetInitServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetInitServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetJarInfo(
            self,
            request: models.DescribeAssetJarInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetJarInfoResponse:
        """
        This API is used to obtain Jar package details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetJarInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetJarInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetJarList(
            self,
            request: models.DescribeAssetJarListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetJarListResponse:
        """
        This API is used to query the list of Jar packages.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetJarList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetJarListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetLoadInfo(
            self,
            request: models.DescribeAssetLoadInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetLoadInfoResponse:
        """
        This API is used to obtain the utilization of the system load, memory, and hard disk.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetLoadInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetLoadInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetMachineDetail(
            self,
            request: models.DescribeAssetMachineDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetMachineDetailResponse:
        """
        This API is used to obtain asset management host resource details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetMachineDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetMachineDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetMachineList(
            self,
            request: models.DescribeAssetMachineListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetMachineListResponse:
        """
        This API is used to obtain the resource monitoring list of the asset fingerprint page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetMachineTagTop(
            self,
            request: models.DescribeAssetMachineTagTopRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetMachineTagTopResponse:
        """
        This API is used to obtain top 5 host tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetMachineTagTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetMachineTagTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetPlanTaskList(
            self,
            request: models.DescribeAssetPlanTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetPlanTaskListResponse:
        """
        This API is used to query the list of asset management plan tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetPlanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetPlanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetPortCount(
            self,
            request: models.DescribeAssetPortCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetPortCountResponse:
        """
        This API is used to obtain the total number of ports.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetPortCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetPortCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetPortInfoList(
            self,
            request: models.DescribeAssetPortInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetPortInfoListResponse:
        """
        This API is used to obtain the list of asset management ports.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetPortInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetPortInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetProcessCount(
            self,
            request: models.DescribeAssetProcessCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetProcessCountResponse:
        """
        This API is used to obtain the total number of processes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetProcessCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetProcessCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetProcessInfoList(
            self,
            request: models.DescribeAssetProcessInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetProcessInfoListResponse:
        """
        This API is used to obtain the list of asset management processes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetProcessInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetProcessInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetRecentMachineInfo(
            self,
            request: models.DescribeAssetRecentMachineInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetRecentMachineInfoResponse:
        """
        This API is used to obtain the latest trend of hosts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetRecentMachineInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetRecentMachineInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSystemPackageList(
            self,
            request: models.DescribeAssetSystemPackageListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSystemPackageListResponse:
        """
        This API is used to obtain the list of system installation packages for asset management.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSystemPackageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSystemPackageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTotalCount(
            self,
            request: models.DescribeAssetTotalCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTotalCountResponse:
        """
        This API is used to obtain the number of resources, including hosts, accounts, ports, processes, software, databases, web applications, web frameworks, web services, and web sites.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTotalCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTotalCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTypeTop(
            self,
            request: models.DescribeAssetTypeTopRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTypeTopResponse:
        """
        This API is used to obtain Top5 resources of various types.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTypeTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTypeTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTypes(
            self,
            request: models.DescribeAssetTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTypesResponse:
        """
        This API is used to obtain the asset fingerprint type list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetUserCount(
            self,
            request: models.DescribeAssetUserCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetUserCountResponse:
        """
        This API is used to obtain the total number of accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetUserCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetUserCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetUserInfo(
            self,
            request: models.DescribeAssetUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetUserInfoResponse:
        """
        This API is used to obtain host account details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetUserKeyList(
            self,
            request: models.DescribeAssetUserKeyListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetUserKeyListResponse:
        """
        This API is used to obtain the list of host account Keys.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetUserKeyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetUserKeyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetUserList(
            self,
            request: models.DescribeAssetUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetUserListResponse:
        """
        This API is used to obtain the list of accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebAppCount(
            self,
            request: models.DescribeAssetWebAppCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebAppCountResponse:
        """
        This API is used to obtain the number of all web applications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebAppCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebAppCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebAppList(
            self,
            request: models.DescribeAssetWebAppListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebAppListResponse:
        """
        This API is used to obtain the list of asset management web applications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebAppPluginList(
            self,
            request: models.DescribeAssetWebAppPluginListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebAppPluginListResponse:
        """
        This API is used to obtain the list of asset management Web application plugins.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebAppPluginList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebAppPluginListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebFrameCount(
            self,
            request: models.DescribeAssetWebFrameCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebFrameCountResponse:
        """
        This API is used to obtain the number of all Web frameworks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebFrameCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebFrameCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebFrameList(
            self,
            request: models.DescribeAssetWebFrameListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebFrameListResponse:
        """
        This API is used to obtain the list of asset management Web frameworks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebFrameList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebFrameListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebLocationCount(
            self,
            request: models.DescribeAssetWebLocationCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebLocationCountResponse:
        """
        This API is used to obtain the total number of Web sites.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebLocationCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebLocationCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebLocationInfo(
            self,
            request: models.DescribeAssetWebLocationInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebLocationInfoResponse:
        """
        This API is used to obtain the Web site details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebLocationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebLocationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebLocationList(
            self,
            request: models.DescribeAssetWebLocationListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebLocationListResponse:
        """
        This API is used to obtain the list of Web sites.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebLocationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebLocationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebLocationPathList(
            self,
            request: models.DescribeAssetWebLocationPathListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebLocationPathListResponse:
        """
        This API is used to obtain the list of Web sites' virtual directories.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebLocationPathList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebLocationPathListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebServiceCount(
            self,
            request: models.DescribeAssetWebServiceCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebServiceCountResponse:
        """
        This API is used to obtain the number of all web services.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebServiceCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebServiceCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebServiceInfoList(
            self,
            request: models.DescribeAssetWebServiceInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebServiceInfoListResponse:
        """
        This API is used to query the list of asset management Web services.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebServiceInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebServiceInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebServiceProcessList(
            self,
            request: models.DescribeAssetWebServiceProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebServiceProcessListResponse:
        """
        This API is used to obtain the list of processes associated with Web services.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebServiceProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebServiceProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackEventInfo(
            self,
            request: models.DescribeAttackEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackEventInfoResponse:
        """
        This API is used to obtain network attack details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackEvents(
            self,
            request: models.DescribeAttackEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackEventsResponse:
        """
        This API is used to display the list of network attack detection events in pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackLogs(
            self,
            request: models.DescribeAttackLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackLogsResponse:
        """
        DescribeAttackEvents 代替

        This API is used to display the list of network attack logs in pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackSource(
            self,
            request: models.DescribeAttackSourceRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackSourceResponse:
        """
        已废弃

        This API is used to backtrack attacks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackSourceEvents(
            self,
            request: models.DescribeAttackSourceEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackSourceEventsResponse:
        """
        已废弃

        This API is used to query attack backtracking events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackSourceEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackSourceEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackStatistics(
            self,
            request: models.DescribeAttackStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackStatisticsResponse:
        """
        This API is used to obtain the statistics of network attack data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackTop(
            self,
            request: models.DescribeAttackTopRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackTopResponse:
        """
        This API is used to obtain the list of Top 5 network attacks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackTrends(
            self,
            request: models.DescribeAttackTrendsRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackTrendsResponse:
        """
        This API is used to obtain the network attack trend data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackTrends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackTrendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackVulTypeList(
            self,
            request: models.DescribeAttackVulTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackVulTypeListResponse:
        """
        This API is used to obtain the list of network attack threat types.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackVulTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackVulTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableExpertServiceDetail(
            self,
            request: models.DescribeAvailableExpertServiceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableExpertServiceDetailResponse:
        """
        This API is used to obtain available order details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableExpertServiceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableExpertServiceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBanMode(
            self,
            request: models.DescribeBanModeRequest,
            opts: Dict = None,
    ) -> models.DescribeBanModeResponse:
        """
        This API is used to obtain the brute-force blocking mode.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBanMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBanModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBanRegions(
            self,
            request: models.DescribeBanRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeBanRegionsResponse:
        """
        This API is used to obtain the block region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBanRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBanRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBanStatus(
            self,
            request: models.DescribeBanStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBanStatusResponse:
        """
        This API is used to obtain the block button status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBanStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBanWhiteList(
            self,
            request: models.DescribeBanWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeBanWhiteListResponse:
        """
        This API is used to obtain the blocking allowlist list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBanWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBanWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineBasicInfo(
            self,
            request: models.DescribeBaselineBasicInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineBasicInfoResponse:
        """
        This API is used to query the list of baseline basic information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineBasicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineBasicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineDefaultStrategyList(
            self,
            request: models.DescribeBaselineDefaultStrategyListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineDefaultStrategyListResponse:
        """
        This API is used to query the list information of default policies of the baseline.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineDefaultStrategyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineDefaultStrategyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineDetail(
            self,
            request: models.DescribeBaselineDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineDetailResponse:
        """
        This API is used to query baseline details by baseline ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineEffectHostList(
            self,
            request: models.DescribeBaselineEffectHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineEffectHostListResponse:
        """
        This API is used to query the list of hosts affected by a baseline based on baseline ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineHostDetectList(
            self,
            request: models.DescribeBaselineHostDetectListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineHostDetectListResponse:
        """
        This API is used to obtain the list of hosts for baseline detection.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineHostDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineHostDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineHostTop(
            self,
            request: models.DescribeBaselineHostTopRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineHostTopResponse:
        """
        This API is used to return Top N risky servers.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineHostTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineHostTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineItemDetectList(
            self,
            request: models.DescribeBaselineItemDetectListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineItemDetectListResponse:
        """
        This API is used to obtain the list of baseline detection items.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineItemDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineItemDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineItemList(
            self,
            request: models.DescribeBaselineItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineItemListResponse:
        """
        This API is used to obtain the list of check results on baseline check items.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineList(
            self,
            request: models.DescribeBaselineListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineListResponse:
        """
        This API is used to query the information of the baseline list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselinePolicyList(
            self,
            request: models.DescribeBaselinePolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselinePolicyListResponse:
        """
        This API is used to obtain the list of baseline policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselinePolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselinePolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineRule(
            self,
            request: models.DescribeBaselineRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineRuleResponse:
        """
        This API is used to query the information on corresponding check items based on baseline ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineScanSchedule(
            self,
            request: models.DescribeBaselineScanScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineScanScheduleResponse:
        """
        This API is used to query the baseline detection progress by task ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineScanSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineScanScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineStrategyDetail(
            self,
            request: models.DescribeBaselineStrategyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineStrategyDetailResponse:
        """
        This API is used to query policy details by baseline policy ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineStrategyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineStrategyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineStrategyList(
            self,
            request: models.DescribeBaselineStrategyListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineStrategyListResponse:
        """
        This API is used to query the information of baseline policies under the same user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineStrategyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineStrategyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineTop(
            self,
            request: models.DescribeBaselineTopRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineTopResponse:
        """
        This API is used to query TOP baseline detection items based on policy IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineWeakPasswordList(
            self,
            request: models.DescribeBaselineWeakPasswordListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineWeakPasswordListResponse:
        """
        This API is used to obtain the list of baseline weak passwords.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineWeakPasswordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineWeakPasswordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashEvents(
            self,
            request: models.DescribeBashEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeBashEventsResponse:
        """
        This API is used to obtain the high-risk command list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashEventsInfo(
            self,
            request: models.DescribeBashEventsInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeBashEventsInfoResponse:
        """
        This API is used to query high-risk command event details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashEventsInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashEventsInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashEventsInfoNew(
            self,
            request: models.DescribeBashEventsInfoNewRequest,
            opts: Dict = None,
    ) -> models.DescribeBashEventsInfoNewResponse:
        """
        This API is used to query high-risk command event details (new).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashEventsInfoNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashEventsInfoNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashEventsNew(
            self,
            request: models.DescribeBashEventsNewRequest,
            opts: Dict = None,
    ) -> models.DescribeBashEventsNewResponse:
        """
        This API is used to obtain the list of high-risk commands (new).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashEventsNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashEventsNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashPolicies(
            self,
            request: models.DescribeBashPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeBashPoliciesResponse:
        """
        This API is used to obtain the list of high-risk command policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashRules(
            self,
            request: models.DescribeBashRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBashRulesResponse:
        """
        This API is used to obtain the list of high-risk command rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBruteAttackList(
            self,
            request: models.DescribeBruteAttackListRequest,
            opts: Dict = None,
    ) -> models.DescribeBruteAttackListResponse:
        """
        This API is used to obtain the list of password cracking.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBruteAttackList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBruteAttackListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBruteAttackRules(
            self,
            request: models.DescribeBruteAttackRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBruteAttackRulesResponse:
        """
        This API is used to obtain brute force cracking rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBruteAttackRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBruteAttackRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCanFixVulMachine(
            self,
            request: models.DescribeCanFixVulMachineRequest,
            opts: Dict = None,
    ) -> models.DescribeCanFixVulMachineResponse:
        """
        This API is used to query the fixable host information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCanFixVulMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCanFixVulMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCanNotSeparateMachine(
            self,
            request: models.DescribeCanNotSeparateMachineRequest,
            opts: Dict = None,
    ) -> models.DescribeCanNotSeparateMachineResponse:
        """
        This API is used to obtain hosts where Trojans cannot be isolated.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCanNotSeparateMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCanNotSeparateMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientException(
            self,
            request: models.DescribeClientExceptionRequest,
            opts: Dict = None,
    ) -> models.DescribeClientExceptionResponse:
        """
        This API is used to obtain client exception events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientException"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientExceptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComponentStatistics(
            self,
            request: models.DescribeComponentStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeComponentStatisticsResponse:
        """
        接口已无效

        This API is used to obtain the data of the component statistics list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComponentStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComponentStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefenceEventDetail(
            self,
            request: models.DescribeDefenceEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDefenceEventDetailResponse:
        """
        This API is used to obtain vulnerability defense event details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefenceEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefenceEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnectInstallCommand(
            self,
            request: models.DescribeDirectConnectInstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectInstallCommandResponse:
        """
        This API is used to obtain DC agent installation command, including the token.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnectInstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectInstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeESAggregations(
            self,
            request: models.DescribeESAggregationsRequest,
            opts: Dict = None,
    ) -> models.DescribeESAggregationsResponse:
        """
        This API is used to obtain the aggregation result of the ES field.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeESAggregations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeESAggregationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEmergencyResponseList(
            self,
            request: models.DescribeEmergencyResponseListRequest,
            opts: Dict = None,
    ) -> models.DescribeEmergencyResponseListResponse:
        """
        This API is used to obtain the emergency response list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEmergencyResponseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEmergencyResponseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEmergencyVulList(
            self,
            request: models.DescribeEmergencyVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeEmergencyVulListResponse:
        """
        This API is used to obtain the list of emergency vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEmergencyVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEmergencyVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventByTable(
            self,
            request: models.DescribeEventByTableRequest,
            opts: Dict = None,
    ) -> models.DescribeEventByTableResponse:
        """
        This API is used to query alarm event details based on event table names and IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventByTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventByTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExpertServiceList(
            self,
            request: models.DescribeExpertServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeExpertServiceListResponse:
        """
        This API is used to obtain the security manager list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExpertServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExpertServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExpertServiceOrderList(
            self,
            request: models.DescribeExpertServiceOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeExpertServiceOrderListResponse:
        """
        This API is used to obtain the expert service order list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExpertServiceOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExpertServiceOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportMachines(
            self,
            request: models.DescribeExportMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeExportMachinesResponse:
        """
        This API is used to export the list of hosts in a specific region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFastAnalysis(
            self,
            request: models.DescribeFastAnalysisRequest,
            opts: Dict = None,
    ) -> models.DescribeFastAnalysisResponse:
        """
        This API is used to quickly analyze and count logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFastAnalysis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFastAnalysisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTamperEventRuleInfo(
            self,
            request: models.DescribeFileTamperEventRuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTamperEventRuleInfoResponse:
        """
        This API is used to view the rule details API when an event occurs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTamperEventRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTamperEventRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTamperEvents(
            self,
            request: models.DescribeFileTamperEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTamperEventsResponse:
        """
        This API is used to obtain the list of core file monitoring events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTamperEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTamperEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTamperRuleCount(
            self,
            request: models.DescribeFileTamperRuleCountRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTamperRuleCountResponse:
        """
        This API is used to query the number of rules for monitoring files associated with a host.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTamperRuleCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTamperRuleCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTamperRuleInfo(
            self,
            request: models.DescribeFileTamperRuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTamperRuleInfoResponse:
        """
        This API is used to query details of a monitoring rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTamperRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTamperRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTamperRules(
            self,
            request: models.DescribeFileTamperRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTamperRulesResponse:
        """
        This API is used to obtain the list of core file monitoring rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTamperRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTamperRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralStat(
            self,
            request: models.DescribeGeneralStatRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralStatResponse:
        """
        This API is used to obtain the statistics data of hosts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHistoryAccounts(
            self,
            request: models.DescribeHistoryAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeHistoryAccountsResponse:
        """
        This API is used to obtain the data of the account change history list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHistoryAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHistoryAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHistoryService(
            self,
            request: models.DescribeHistoryServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeHistoryServiceResponse:
        """
        This API is used to query the log retrieval service information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHistoryService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHistoryServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostInfo(
            self,
            request: models.DescribeHostInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeHostInfoResponse:
        """
        This API is used to query the host and tag information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostLoginList(
            self,
            request: models.DescribeHostLoginListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostLoginListResponse:
        """
        This API is used to retrieve the log-in audit list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostLoginList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostLoginListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHotVulTop(
            self,
            request: models.DescribeHotVulTopRequest,
            opts: Dict = None,
    ) -> models.DescribeHotVulTopResponse:
        """
        This API is used to obtain hot spot vulnerabilities across the entire network.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHotVulTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHotVulTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIgnoreBaselineRule(
            self,
            request: models.DescribeIgnoreBaselineRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeIgnoreBaselineRuleResponse:
        """
        This API is used to query the information of ignored inspection items.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIgnoreBaselineRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIgnoreBaselineRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIgnoreHostAndItemConfig(
            self,
            request: models.DescribeIgnoreHostAndItemConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeIgnoreHostAndItemConfigResponse:
        """
        This API is used to obtain the information of affected inspection items and hosts ignored with one click.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIgnoreHostAndItemConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIgnoreHostAndItemConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIgnoreRuleEffectHostList(
            self,
            request: models.DescribeIgnoreRuleEffectHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeIgnoreRuleEffectHostListResponse:
        """
        This API is used to query the information on the list of hosts affected by ignored detection items based on detection item IDs and filter criteria.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIgnoreRuleEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIgnoreRuleEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndexList(
            self,
            request: models.DescribeIndexListRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexListResponse:
        """
        接口已废弃

        This API is used to obtain the index list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndexList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJavaMemShellInfo(
            self,
            request: models.DescribeJavaMemShellInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeJavaMemShellInfoResponse:
        """
        This API is used to query Java webshell event details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJavaMemShellInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJavaMemShellInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJavaMemShellList(
            self,
            request: models.DescribeJavaMemShellListRequest,
            opts: Dict = None,
    ) -> models.DescribeJavaMemShellListResponse:
        """
        This API is used to query the list of Java webshell events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJavaMemShellList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJavaMemShellListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJavaMemShellPluginInfo(
            self,
            request: models.DescribeJavaMemShellPluginInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeJavaMemShellPluginInfoResponse:
        """
        This API is used to query the Java webshell plugin information of the given host.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJavaMemShellPluginInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJavaMemShellPluginInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJavaMemShellPluginList(
            self,
            request: models.DescribeJavaMemShellPluginListRequest,
            opts: Dict = None,
    ) -> models.DescribeJavaMemShellPluginListResponse:
        """
        This API is used to query the Java webshell plugin list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJavaMemShellPluginList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJavaMemShellPluginListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicense(
            self,
            request: models.DescribeLicenseRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseResponse:
        """
        This API is used to query the authorization information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseBindList(
            self,
            request: models.DescribeLicenseBindListRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseBindListResponse:
        """
        This API is used to obtain the list of authorized machines bound to an authorization under the Settings Center-Authorization Management.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseBindList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseBindListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseBindSchedule(
            self,
            request: models.DescribeLicenseBindScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseBindScheduleResponse:
        """
        This API is used to query the binding task progress of the authorization.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseBindSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseBindScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseGeneral(
            self,
            request: models.DescribeLicenseGeneralRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseGeneralResponse:
        """
        This API is used to obtain the authorization overview information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseGeneral"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseGeneralResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseList(
            self,
            request: models.DescribeLicenseListRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseListResponse:
        """
        This API is used to obtain all authorization orders of a user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseWhiteConfig(
            self,
            request: models.DescribeLicenseWhiteConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseWhiteConfigResponse:
        """
        This API is used to query the available configurations for authorization allowlists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseWhiteConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseWhiteConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogDeliveryKafkaOptions(
            self,
            request: models.DescribeLogDeliveryKafkaOptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogDeliveryKafkaOptionsResponse:
        """
        This API is used to query the list of logs available for shipping to Kafka.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogDeliveryKafkaOptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogDeliveryKafkaOptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogExports(
            self,
            request: models.DescribeLogExportsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogExportsResponse:
        """
        This API is used to obtain the list of log download tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogExports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogExportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogHistogram(
            self,
            request: models.DescribeLogHistogramRequest,
            opts: Dict = None,
    ) -> models.DescribeLogHistogramResponse:
        """
        This API is used to obtain the log histogram information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogHistogram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogHistogramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogIndex(
            self,
            request: models.DescribeLogIndexRequest,
            opts: Dict = None,
    ) -> models.DescribeLogIndexResponse:
        """
        This API is used to query the index.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogKafkaDeliverInfo(
            self,
            request: models.DescribeLogKafkaDeliverInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLogKafkaDeliverInfoResponse:
        """
        This API is used to obtain the information of Kafka shipping.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogKafkaDeliverInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogKafkaDeliverInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogStorageConfig(
            self,
            request: models.DescribeLogStorageConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeLogStorageConfigResponse:
        """
        This API is used to obtain the log storage configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogStorageConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogStorageConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogStorageRecord(
            self,
            request: models.DescribeLogStorageRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeLogStorageRecordResponse:
        """
        This API is used to obtain the record of stored log size.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogStorageRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogStorageRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogStorageStatistic(
            self,
            request: models.DescribeLogStorageStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeLogStorageStatisticResponse:
        """
        This API is used to obtain the statistics of the used log retrieval capacity.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogStorageStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogStorageStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogType(
            self,
            request: models.DescribeLogTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeLogTypeResponse:
        """
        This API is used to obtain log types, and the returned result of this API indicates temporarily filterable log types.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginWhiteCombinedList(
            self,
            request: models.DescribeLoginWhiteCombinedListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginWhiteCombinedListResponse:
        """
        This API is used to obtain the list of cross-region log-in allowlists after merge.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginWhiteCombinedList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginWhiteCombinedListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginWhiteHostList(
            self,
            request: models.DescribeLoginWhiteHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginWhiteHostListResponse:
        """
        This API is used to query the list of allowlisted machines after merge.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginWhiteHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginWhiteHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginWhiteList(
            self,
            request: models.DescribeLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginWhiteListResponse:
        """
        This API is used to obtain the cross-region log-in allowlist list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineClearHistory(
            self,
            request: models.DescribeMachineClearHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineClearHistoryResponse:
        """
        This API is used to query the clearing history records of a machine.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineClearHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineClearHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineDefenseCnt(
            self,
            request: models.DescribeMachineDefenseCntRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineDefenseCntResponse:
        """
        This API is used to query the statistics of advanced defense events for hosts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineDefenseCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineDefenseCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineFileTamperRules(
            self,
            request: models.DescribeMachineFileTamperRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineFileTamperRulesResponse:
        """
        This API is used to query the list of host-related core file monitoring rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineFileTamperRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineFileTamperRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineGeneral(
            self,
            request: models.DescribeMachineGeneralRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineGeneralResponse:
        """
        This API is used to query the information of the host overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineGeneral"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineGeneralResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineLicenseDetail(
            self,
            request: models.DescribeMachineLicenseDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineLicenseDetailResponse:
        """
        This API is used to query the machine authorization information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineLicenseDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineLicenseDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineOsList(
            self,
            request: models.DescribeMachineOsListRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineOsListResponse:
        """
        This API is used to query the machine operating system list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineOsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineOsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineRegionList(
            self,
            request: models.DescribeMachineRegionListRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineRegionListResponse:
        """
        This API is used to query the list of host regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineRegionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineRegionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineRegions(
            self,
            request: models.DescribeMachineRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineRegionsResponse:
        """
        This API is used to obtain the list of machine regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineRiskCnt(
            self,
            request: models.DescribeMachineRiskCntRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineRiskCntResponse:
        """
        This API is used to query the statistics of host intrusion detection events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineRiskCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineRiskCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineSnapshot(
            self,
            request: models.DescribeMachineSnapshotRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineSnapshotResponse:
        """
        This API is used to query snapshots created by the host.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachines(
            self,
            request: models.DescribeMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeMachinesResponse:
        """
        This API is used to obtain the list of hosts in a specific region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachinesSimple(
            self,
            request: models.DescribeMachinesSimpleRequest,
            opts: Dict = None,
    ) -> models.DescribeMachinesSimpleResponse:
        """
        This API is used to obtain the list of hosts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachinesSimple"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachinesSimpleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalWareList(
            self,
            request: models.DescribeMalWareListRequest,
            opts: Dict = None,
    ) -> models.DescribeMalWareListResponse:
        """
        This API is used to obtain the Trojan list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalWareList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalWareListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaliciousRequestWhiteList(
            self,
            request: models.DescribeMaliciousRequestWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeMaliciousRequestWhiteListResponse:
        """
        This API is used to query the list of malicious request allowlists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaliciousRequestWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaliciousRequestWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareFile(
            self,
            request: models.DescribeMalwareFileRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareFileResponse:
        """
        This API is used to obtain Trojan file download addresses.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareInfo(
            self,
            request: models.DescribeMalwareInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareInfoResponse:
        """
        This API is used to view malicious file details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareRiskOverview(
            self,
            request: models.DescribeMalwareRiskOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareRiskOverviewResponse:
        """
        This API is used to obtain the information of virus scanning overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareRiskOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareRiskOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareRiskWarning(
            self,
            request: models.DescribeMalwareRiskWarningRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareRiskWarningResponse:
        """
        This API is used to open Intrusion Detection - Virus Scanning, and the risk warning content pops up.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareRiskWarning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareRiskWarningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareTimingScanSetting(
            self,
            request: models.DescribeMalwareTimingScanSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareTimingScanSettingResponse:
        """
        This API is used to query the scheduled scan configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareTimingScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareTimingScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareWhiteList(
            self,
            request: models.DescribeMalwareWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareWhiteListResponse:
        """
        This API is used to obtain the list of Trojan allowlists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareWhiteListAffectList(
            self,
            request: models.DescribeMalwareWhiteListAffectListRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareWhiteListAffectListResponse:
        """
        This API is used to obtain the list of affected Trojan allowlists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareWhiteListAffectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareWhiteListAffectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonthInspectionReport(
            self,
            request: models.DescribeMonthInspectionReportRequest,
            opts: Dict = None,
    ) -> models.DescribeMonthInspectionReportResponse:
        """
        This API is used to download the monthly inspection report of the security manager.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonthInspectionReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonthInspectionReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetAttackSetting(
            self,
            request: models.DescribeNetAttackSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeNetAttackSettingResponse:
        """
        This API is used to query network attack settings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetAttackSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetAttackSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetAttackWhiteList(
            self,
            request: models.DescribeNetAttackWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetAttackWhiteListResponse:
        """
        This API is used to obtain the network attack allowlist list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetAttackWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetAttackWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpenPortStatistics(
            self,
            request: models.DescribeOpenPortStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeOpenPortStatisticsResponse:
        """
        This API is used to obtain the list of port statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpenPortStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpenPortStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewStatistics(
            self,
            request: models.DescribeOverviewStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewStatisticsResponse:
        """
        This API is used to obtain the overview statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivilegeEventInfo(
            self,
            request: models.DescribePrivilegeEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePrivilegeEventInfoResponse:
        """
        This API is used to obtain local privilege escalation information details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivilegeEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivilegeEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivilegeRules(
            self,
            request: models.DescribePrivilegeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribePrivilegeRulesResponse:
        """
        This API is used to obtain the list of local privilege escalation rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivilegeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivilegeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProVersionInfo(
            self,
            request: models.DescribeProVersionInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProVersionInfoResponse:
        """
        This API is used to obtain the overview information of the Professional edition.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProVersionInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProVersionInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProVersionStatus(
            self,
            request: models.DescribeProVersionStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeProVersionStatusResponse:
        """
        This API is used to check whether a single host or all hosts enable the professional version.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProVersionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProVersionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessStatistics(
            self,
            request: models.DescribeProcessStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessStatisticsResponse:
        """
        This API is used to obtain the process statistics data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductStatus(
            self,
            request: models.DescribeProductStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeProductStatusResponse:
        """
        This API is used to query the product trial status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicProxyInstallCommand(
            self,
            request: models.DescribePublicProxyInstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribePublicProxyInstallCommandResponse:
        """
        This API is used to obtain the installation command of the public network access proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicProxyInstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicProxyInstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseBackupList(
            self,
            request: models.DescribeRansomDefenseBackupListRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseBackupListResponse:
        """
        This API is used to query the list of host snapshot backups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseBackupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseBackupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseEventsList(
            self,
            request: models.DescribeRansomDefenseEventsListRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseEventsListResponse:
        """
        This API is used to query the anti-ransomware event list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseEventsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseEventsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseMachineList(
            self,
            request: models.DescribeRansomDefenseMachineListRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseMachineListResponse:
        """
        This API is used to query the list of backup details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseMachineStrategyInfo(
            self,
            request: models.DescribeRansomDefenseMachineStrategyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseMachineStrategyInfoResponse:
        """
        This API is used to obtain the list of policies bound to a host.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseMachineStrategyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseMachineStrategyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseRollBackTaskList(
            self,
            request: models.DescribeRansomDefenseRollBackTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseRollBackTaskListResponse:
        """
        This API is used to query the rollback task list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseRollBackTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseRollBackTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseState(
            self,
            request: models.DescribeRansomDefenseStateRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseStateResponse:
        """
        This API is used to obtain user anti-ransomware trends.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseStrategyDetail(
            self,
            request: models.DescribeRansomDefenseStrategyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseStrategyDetailResponse:
        """
        This API is used to obtain the policy details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseStrategyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseStrategyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseStrategyList(
            self,
            request: models.DescribeRansomDefenseStrategyListRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseStrategyListResponse:
        """
        This API is used to query the list of anti-ransomware policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseStrategyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseStrategyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseStrategyMachines(
            self,
            request: models.DescribeRansomDefenseStrategyMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseStrategyMachinesResponse:
        """
        This API is used to query the list of machines bound to an anti-ransomware policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseStrategyMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseStrategyMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseTrend(
            self,
            request: models.DescribeRansomDefenseTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseTrendResponse:
        """
        This API is used to obtain the ransomware situation across the entire network.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecommendedProtectCpu(
            self,
            request: models.DescribeRecommendedProtectCpuRequest,
            opts: Dict = None,
    ) -> models.DescribeRecommendedProtectCpuResponse:
        """
        This API is used to query the recommended number of protection cores for purchase.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecommendedProtectCpu"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecommendedProtectCpuResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellEventInfo(
            self,
            request: models.DescribeReverseShellEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellEventInfoResponse:
        """
        This API is used to query reverse shell details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellEvents(
            self,
            request: models.DescribeReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellEventsResponse:
        """
        This API is used to obtain the list of Reverse Shell.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellRules(
            self,
            request: models.DescribeReverseShellRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellRulesResponse:
        """
        This API is used to obtain the list of Reverse Shell rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskBatchStatus(
            self,
            request: models.DescribeRiskBatchStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskBatchStatusResponse:
        """
        This API is used to query if the intrusion detection event update task is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskBatchStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskBatchStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsEventInfo(
            self,
            request: models.DescribeRiskDnsEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsEventInfoResponse:
        """
        This API is used to query malicious request event details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsEventList(
            self,
            request: models.DescribeRiskDnsEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsEventListResponse:
        """
        This API is used to obtain the list of malicious request events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsInfo(
            self,
            request: models.DescribeRiskDnsInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsInfoResponse:
        """
        This API is used to query malicious request details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsList(
            self,
            request: models.DescribeRiskDnsListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsListResponse:
        """
        This API is used to obtain the malicious request list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsPolicyList(
            self,
            request: models.DescribeRiskDnsPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsPolicyListResponse:
        """
        This API is used to obtain the list of malicious request policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskProcessEvents(
            self,
            request: models.DescribeRiskProcessEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskProcessEventsResponse:
        """
        This API is used to obtain the list of abnormal processes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskProcessEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskProcessEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSafeInfo(
            self,
            request: models.DescribeSafeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSafeInfoResponse:
        """
        This API is used to query the .security notification information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSafeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSafeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanMalwareSchedule(
            self,
            request: models.DescribeScanMalwareScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeScanMalwareScheduleResponse:
        """
        This API is used to query the Trojan scan progress.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanMalwareSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanMalwareScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanSchedule(
            self,
            request: models.DescribeScanScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeScanScheduleResponse:
        """
        This API is used to query the detection progress by taskid.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanState(
            self,
            request: models.DescribeScanStateRequest,
            opts: Dict = None,
    ) -> models.DescribeScanStateResponse:
        """
        This API is used to query the status of recent scan tasks of the corresponding module.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskDetails(
            self,
            request: models.DescribeScanTaskDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskDetailsResponse:
        """
        This API is used to query the scan task details and scan progress information/exceptions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskStatus(
            self,
            request: models.DescribeScanTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskStatusResponse:
        """
        This API is used to query the list of machine scan statuses for filtering.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanVulSetting(
            self,
            request: models.DescribeScanVulSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeScanVulSettingResponse:
        """
        This API is used to query the configuration for regular detection.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanVulSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanVulSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenAttackHotspot(
            self,
            request: models.DescribeScreenAttackHotspotRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenAttackHotspotResponse:
        """
        This API is used to visually obtain the attacked hot spots across the entire network on the large screen.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenAttackHotspot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenAttackHotspotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenBroadcasts(
            self,
            request: models.DescribeScreenBroadcastsRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenBroadcastsResponse:
        """
        This API is used to obtain the security report on the large screen.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenBroadcasts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenBroadcastsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenDefenseTrends(
            self,
            request: models.DescribeScreenDefenseTrendsRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenDefenseTrendsResponse:
        """
        This API is used to obtain the visualized attack and defense trends on the large screen.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenDefenseTrends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenDefenseTrendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenEmergentMsg(
            self,
            request: models.DescribeScreenEmergentMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenEmergentMsgResponse:
        """
        This API is used to obtain the visualized emergency notification on the large screen.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenEmergentMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenEmergentMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenEventsCnt(
            self,
            request: models.DescribeScreenEventsCntRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenEventsCntResponse:
        """
        This API is used to obtain the statistics data of events on the security overview page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenEventsCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenEventsCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenGeneralStat(
            self,
            request: models.DescribeScreenGeneralStatRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenGeneralStatResponse:
        """
        This API is used to obtain the visualized statistics data of hosts on the screen.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenGeneralStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenGeneralStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenHostInvasion(
            self,
            request: models.DescribeScreenHostInvasionRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenHostInvasionResponse:
        """
        This API is used to obtain the visualized host intrusion details on the large screen.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenHostInvasion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenHostInvasionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenMachineRegions(
            self,
            request: models.DescribeScreenMachineRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenMachineRegionsResponse:
        """
        This API is used to obtain the list of available visualized host regions on the large screen.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenMachineRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenMachineRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenMachines(
            self,
            request: models.DescribeScreenMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenMachinesResponse:
        """
        This API is used to obtain the visualized list of host regions on the large screen.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenProtectionCnt(
            self,
            request: models.DescribeScreenProtectionCntRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenProtectionCntResponse:
        """
        This API is used to obtain the visualized introduction of CWPP engine on the large screen.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenProtectionCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenProtectionCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenProtectionStat(
            self,
            request: models.DescribeScreenProtectionStatRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenProtectionStatResponse:
        """
        This API is used to obtain the security protection status on the large screen.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenProtectionStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenProtectionStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenRiskAssetsTop(
            self,
            request: models.DescribeScreenRiskAssetsTopRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenRiskAssetsTopResponse:
        """
        This API is used to count today's risky assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenRiskAssetsTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenRiskAssetsTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchLogs(
            self,
            request: models.DescribeSearchLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchLogsResponse:
        """
        This API is used to obtain historical search records.
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
        This API is used to obtain the list of quick retrievals.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityBroadcastInfo(
            self,
            request: models.DescribeSecurityBroadcastInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityBroadcastInfoResponse:
        """
        This API is used to query the information of security report articles.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityBroadcastInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityBroadcastInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityBroadcasts(
            self,
            request: models.DescribeSecurityBroadcastsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityBroadcastsResponse:
        """
        This API is used to obtain the security report list page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityBroadcasts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityBroadcastsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityDynamics(
            self,
            request: models.DescribeSecurityDynamicsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityDynamicsResponse:
        """
        This API is used to obtain the dynamic message data of security events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityDynamics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityDynamicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityEventStat(
            self,
            request: models.DescribeSecurityEventStatRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityEventStatResponse:
        """
        This API is used to obtain the statistics of security events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityEventStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityEventStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityEventsCnt(
            self,
            request: models.DescribeSecurityEventsCntRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityEventsCntResponse:
        """
        This API is used to obtain the statistics data of security overview-related events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityEventsCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityEventsCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityProtectionStat(
            self,
            request: models.DescribeSecurityProtectionStatRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityProtectionStatResponse:
        """
        接口已无效

        This API is used to obtain the summary of security protection statuses.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityProtectionStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityProtectionStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityTrends(
            self,
            request: models.DescribeSecurityTrendsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityTrendsResponse:
        """
        This API is used to obtain the security event statistics data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityTrends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityTrendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServersAndRiskAndFirstInfo(
            self,
            request: models.DescribeServersAndRiskAndFirstInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeServersAndRiskAndFirstInfoResponse:
        """
        This API is used to obtain the number of risky files pending to be processed + the number of affected servers + whether to try to detect + last detection time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServersAndRiskAndFirstInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServersAndRiskAndFirstInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStrategyExist(
            self,
            request: models.DescribeStrategyExistRequest,
            opts: Dict = None,
    ) -> models.DescribeStrategyExistResponse:
        """
        This API is used to query whether a policy exists by policy name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStrategyExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStrategyExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagMachines(
            self,
            request: models.DescribeTagMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeTagMachinesResponse:
        """
        This API is used to obtain the server information associated with the specified tag.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTags(
            self,
            request: models.DescribeTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsResponse:
        """
        This API is used to obtain all host tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrialReport(
            self,
            request: models.DescribeTrialReportRequest,
            opts: Dict = None,
    ) -> models.DescribeTrialReportResponse:
        """
        This API is used to query the CWPP authorized trial report (only available for console applications).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrialReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrialReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUndoVulCounts(
            self,
            request: models.DescribeUndoVulCountsRequest,
            opts: Dict = None,
    ) -> models.DescribeUndoVulCountsResponse:
        """
        This API is used to obtain the number of pending vulnerabilities of a specified category and the number of hosts in the vulnerability management module.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUndoVulCounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUndoVulCountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsersConfig(
            self,
            request: models.DescribeUsersConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersConfigResponse:
        """
        This API is used to query the user's custom configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsersConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsualLoginPlaces(
            self,
            request: models.DescribeUsualLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DescribeUsualLoginPlacesResponse:
        """
        This API is used to query common log-in locations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsualLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsualLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVdbAndPocInfo(
            self,
            request: models.DescribeVdbAndPocInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVdbAndPocInfoResponse:
        """
        This API is used to obtain virus database and POC updates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVdbAndPocInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVdbAndPocInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVersionCompareChart(
            self,
            request: models.DescribeVersionCompareChartRequest,
            opts: Dict = None,
    ) -> models.DescribeVersionCompareChartResponse:
        """
        This API is used to obtain the version comparison information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVersionCompareChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVersionCompareChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVersionStatistics(
            self,
            request: models.DescribeVersionStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeVersionStatisticsResponse:
        """
        This API is used to count the number of machines of Professional and Basic editions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVersionStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVersionStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVertexDetail(
            self,
            request: models.DescribeVertexDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVertexDetailResponse:
        """
        This API is used to obtain the attribute information of the specified point.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVertexDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVertexDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulCountByDates(
            self,
            request: models.DescribeVulCountByDatesRequest,
            opts: Dict = None,
    ) -> models.DescribeVulCountByDatesResponse:
        """
        This API is used to obtain the number of vulnerabilities of specified types in recent days and the number of hosts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulCountByDates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulCountByDatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulCveIdInfo(
            self,
            request: models.DescribeVulCveIdInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVulCveIdInfoResponse:
        """
        This API is used to query vulnerability details by CveId.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulCveIdInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulCveIdInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceEvent(
            self,
            request: models.DescribeVulDefenceEventRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceEventResponse:
        """
        This API is used to obtain the list of vulnerability defense events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceList(
            self,
            request: models.DescribeVulDefenceListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceListResponse:
        """
        This API is used to query the vulnerability defense list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceOverview(
            self,
            request: models.DescribeVulDefenceOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceOverviewResponse:
        """
        This API is used to obtain the vulnerability defense overview information, including event trend and plugin enabling status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefencePluginDetail(
            self,
            request: models.DescribeVulDefencePluginDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefencePluginDetailResponse:
        """
        This API is used to obtain the vulnerability defense plugin information on a single host.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefencePluginDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefencePluginDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefencePluginExceptionCount(
            self,
            request: models.DescribeVulDefencePluginExceptionCountRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefencePluginExceptionCountResponse:
        """
        This API is used to obtain the current number of abnormal plugins.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefencePluginExceptionCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefencePluginExceptionCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefencePluginStatus(
            self,
            request: models.DescribeVulDefencePluginStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefencePluginStatusResponse:
        """
        This API is used to obtain the vulnerability defense plugin status of each host.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefencePluginStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefencePluginStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceSetting(
            self,
            request: models.DescribeVulDefenceSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceSettingResponse:
        """
        This API is used to obtain the current vulnerability defense plugin settings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulEffectHostList(
            self,
            request: models.DescribeVulEffectHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulEffectHostListResponse:
        """
        This API is used to obtain the list of hosts affected by vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulEffectModules(
            self,
            request: models.DescribeVulEffectModulesRequest,
            opts: Dict = None,
    ) -> models.DescribeVulEffectModulesResponse:
        """
        This API is used to obtain the list of components affected by vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulEffectModules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulEffectModulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulEmergentMsg(
            self,
            request: models.DescribeVulEmergentMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeVulEmergentMsgResponse:
        """
        This API is used to obtain vulnerability emergency notifications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulEmergentMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulEmergentMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixStatus(
            self,
            request: models.DescribeVulFixStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixStatusResponse:
        """
        This API is used to check the host vulnerability fixing progress.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulHostCountScanTime(
            self,
            request: models.DescribeVulHostCountScanTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeVulHostCountScanTimeResponse:
        """
        This API is used to obtain the number of vulnerabilities pending to be processed and affected hosts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulHostCountScanTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulHostCountScanTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulHostTop(
            self,
            request: models.DescribeVulHostTopRequest,
            opts: Dict = None,
    ) -> models.DescribeVulHostTopResponse:
        """
        This API is used to obtain the list of top server risks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulHostTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulHostTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulInfoCvss(
            self,
            request: models.DescribeVulInfoCvssRequest,
            opts: Dict = None,
    ) -> models.DescribeVulInfoCvssResponse:
        """
        This API is used to obtain vulnerability details with the CVSS version.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulInfoCvss"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulInfoCvssResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulLabels(
            self,
            request: models.DescribeVulLabelsRequest,
            opts: Dict = None,
    ) -> models.DescribeVulLabelsResponse:
        """
        This API is used to obtain the list of all user vulnerability tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulLabels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulLabelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulLevelCount(
            self,
            request: models.DescribeVulLevelCountRequest,
            opts: Dict = None,
    ) -> models.DescribeVulLevelCountResponse:
        """
        This API is used to obtain the statistics of vulnerability quantity and level distribution.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulLevelCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulLevelCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulList(
            self,
            request: models.DescribeVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulListResponse:
        """
        This API is used to obtain the data of the vulnerability list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulOverview(
            self,
            request: models.DescribeVulOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeVulOverviewResponse:
        """
        This API is used to obtain the data for the vulnerability overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulStoreList(
            self,
            request: models.DescribeVulStoreListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulStoreListResponse:
        """
        This API is used to obtain the vulnerability database list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulStoreList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulStoreListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulTop(
            self,
            request: models.DescribeVulTopRequest,
            opts: Dict = None,
    ) -> models.DescribeVulTopResponse:
        """
        This API is used to count top vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulTrend(
            self,
            request: models.DescribeVulTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeVulTrendResponse:
        """
        This API is used to obtain information of the vulnerability situation.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWarningHostConfig(
            self,
            request: models.DescribeWarningHostConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeWarningHostConfigResponse:
        """
        This API is used to query the alarming machine scope settings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWarningHostConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWarningHostConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWarningList(
            self,
            request: models.DescribeWarningListRequest,
            opts: Dict = None,
    ) -> models.DescribeWarningListResponse:
        """
        This API is used to obtain the list of the current user's alarms.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWarningList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWarningListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebHookPolicy(
            self,
            request: models.DescribeWebHookPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeWebHookPolicyResponse:
        """
        This API is used to query alarm policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebHookPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebHookPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebHookReceiver(
            self,
            request: models.DescribeWebHookReceiverRequest,
            opts: Dict = None,
    ) -> models.DescribeWebHookReceiverResponse:
        """
        This API is used to query the list of alarm recipients.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebHookReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebHookReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebHookReceiverUsage(
            self,
            request: models.DescribeWebHookReceiverUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeWebHookReceiverUsageResponse:
        """
        This API is used to query the usage of policies associated with the specified alarm recipient.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebHookReceiverUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebHookReceiverUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebHookRule(
            self,
            request: models.DescribeWebHookRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeWebHookRuleResponse:
        """
        This API is used to obtain the details of the WeCom chatbot rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebHookRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebHookRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebHookRules(
            self,
            request: models.DescribeWebHookRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeWebHookRulesResponse:
        """
        This API is used to obtain the list of WeCom chatbot rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebHookRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebHookRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyOrder(
            self,
            request: models.DestroyOrderRequest,
            opts: Dict = None,
    ) -> models.DestroyOrderResponse:
        """
        This API is used to terminate resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditBashRules(
            self,
            request: models.EditBashRulesRequest,
            opts: Dict = None,
    ) -> models.EditBashRulesResponse:
        """
        This API is used to add or modify high-risk command rules.
        """
        
        kwargs = {}
        kwargs["action"] = "EditBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditPrivilegeRules(
            self,
            request: models.EditPrivilegeRulesRequest,
            opts: Dict = None,
    ) -> models.EditPrivilegeRulesResponse:
        """
        This API is used to add or modify local privilege escalation rules (multiple servers supported).
        """
        
        kwargs = {}
        kwargs["action"] = "EditPrivilegeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditPrivilegeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditReverseShellRules(
            self,
            request: models.EditReverseShellRulesRequest,
            opts: Dict = None,
    ) -> models.EditReverseShellRulesResponse:
        """
        This API is used to edit reverse shell rules (multiple servers supported).
        """
        
        kwargs = {}
        kwargs["action"] = "EditReverseShellRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditReverseShellRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditTags(
            self,
            request: models.EditTagsRequest,
            opts: Dict = None,
    ) -> models.EditTagsResponse:
        """
        This API is used to add or edit tags.
        """
        
        kwargs = {}
        kwargs["action"] = "EditTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetAppList(
            self,
            request: models.ExportAssetAppListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetAppListResponse:
        """
        This API is used to export the list of asset management applications.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetCoreModuleList(
            self,
            request: models.ExportAssetCoreModuleListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetCoreModuleListResponse:
        """
        This API is used to export the list of asset management kernel modules.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetCoreModuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetCoreModuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetDatabaseList(
            self,
            request: models.ExportAssetDatabaseListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetDatabaseListResponse:
        """
        This API is used to export the list of asset management databases.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetDatabaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetDatabaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetEnvList(
            self,
            request: models.ExportAssetEnvListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetEnvListResponse:
        """
        This API is used to export the list of asset management environment variables.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetEnvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetEnvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetInitServiceList(
            self,
            request: models.ExportAssetInitServiceListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetInitServiceListResponse:
        """
        This API is used to export the list of asset management startup services.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetInitServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetInitServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetJarList(
            self,
            request: models.ExportAssetJarListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetJarListResponse:
        """
        This API is used to export the list of Jar packages.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetJarList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetJarListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetMachineDetail(
            self,
            request: models.ExportAssetMachineDetailRequest,
            opts: Dict = None,
    ) -> models.ExportAssetMachineDetailResponse:
        """
        This API is used to export asset management host resource details.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetMachineDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetMachineDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetMachineList(
            self,
            request: models.ExportAssetMachineListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetMachineListResponse:
        """
        This API is used to export the list of resource monitoring.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetPlanTaskList(
            self,
            request: models.ExportAssetPlanTaskListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetPlanTaskListResponse:
        """
        This API is used to export the list of scheduled asset management tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetPlanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetPlanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetPortInfoList(
            self,
            request: models.ExportAssetPortInfoListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetPortInfoListResponse:
        """
        This API is used to export the list of asset management ports.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetPortInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetPortInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetProcessInfoList(
            self,
            request: models.ExportAssetProcessInfoListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetProcessInfoListResponse:
        """
        This API is used to export the asset management process list.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetProcessInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetProcessInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetRecentMachineInfo(
            self,
            request: models.ExportAssetRecentMachineInfoRequest,
            opts: Dict = None,
    ) -> models.ExportAssetRecentMachineInfoResponse:
        """
        This API is used to export host trends of recent days (up to last 90 days).
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetRecentMachineInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetRecentMachineInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetSystemPackageList(
            self,
            request: models.ExportAssetSystemPackageListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetSystemPackageListResponse:
        """
        This API is used to export the list of system installation packages for asset management.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetSystemPackageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetSystemPackageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetUserList(
            self,
            request: models.ExportAssetUserListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetUserListResponse:
        """
        This API is used to export the account list.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetWebAppList(
            self,
            request: models.ExportAssetWebAppListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetWebAppListResponse:
        """
        This API is used to export the list of asset management Web applications.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetWebAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetWebAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetWebFrameList(
            self,
            request: models.ExportAssetWebFrameListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetWebFrameListResponse:
        """
        This API is used to export the list of asset management Web frameworks.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetWebFrameList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetWebFrameListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetWebLocationList(
            self,
            request: models.ExportAssetWebLocationListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetWebLocationListResponse:
        """
        This API is used to export the list of Web sites.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetWebLocationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetWebLocationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetWebServiceInfoList(
            self,
            request: models.ExportAssetWebServiceInfoListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetWebServiceInfoListResponse:
        """
        This API is used to export the list of asset management Web services.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetWebServiceInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetWebServiceInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAttackEvents(
            self,
            request: models.ExportAttackEventsRequest,
            opts: Dict = None,
    ) -> models.ExportAttackEventsResponse:
        """
        This API is used to export network attack events.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAttackEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAttackEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineEffectHostList(
            self,
            request: models.ExportBaselineEffectHostListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineEffectHostListResponse:
        """
        This API is used to export the list of hosts affected by baseline.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineFixList(
            self,
            request: models.ExportBaselineFixListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineFixListResponse:
        """
        This API is used to export the list of fixing baselines.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineFixList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineFixListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineHostDetectList(
            self,
            request: models.ExportBaselineHostDetectListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineHostDetectListResponse:
        """
        This API is used to export the baseline for host detection.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineHostDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineHostDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineItemDetectList(
            self,
            request: models.ExportBaselineItemDetectListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineItemDetectListResponse:
        """
        This API is used to export baseline check items.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineItemDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineItemDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineList(
            self,
            request: models.ExportBaselineListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineListResponse:
        """
        This API is used to export the list of baselines.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBashEvents(
            self,
            request: models.ExportBashEventsRequest,
            opts: Dict = None,
    ) -> models.ExportBashEventsResponse:
        """
        This API is used to export high-risk command events.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBashEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBashEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBashEventsNew(
            self,
            request: models.ExportBashEventsNewRequest,
            opts: Dict = None,
    ) -> models.ExportBashEventsNewResponse:
        """
        This API is used to export high-risk command events (new).
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBashEventsNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBashEventsNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBashPolicies(
            self,
            request: models.ExportBashPoliciesRequest,
            opts: Dict = None,
    ) -> models.ExportBashPoliciesResponse:
        """
        This API is used to export the high-risk command policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBashPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBashPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBruteAttacks(
            self,
            request: models.ExportBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.ExportBruteAttacksResponse:
        """
        This API is used to export password cracking records to a CSV file.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportFileTamperEvents(
            self,
            request: models.ExportFileTamperEventsRequest,
            opts: Dict = None,
    ) -> models.ExportFileTamperEventsResponse:
        """
        This API is used to export core file events.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportFileTamperEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportFileTamperEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportFileTamperRules(
            self,
            request: models.ExportFileTamperRulesRequest,
            opts: Dict = None,
    ) -> models.ExportFileTamperRulesResponse:
        """
        This API is used to export core file monitoring rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportFileTamperRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportFileTamperRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportIgnoreBaselineRule(
            self,
            request: models.ExportIgnoreBaselineRuleRequest,
            opts: Dict = None,
    ) -> models.ExportIgnoreBaselineRuleResponse:
        """
        This API is used to export information of ignored baseline detection items.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportIgnoreBaselineRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportIgnoreBaselineRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportIgnoreRuleEffectHostList(
            self,
            request: models.ExportIgnoreRuleEffectHostListRequest,
            opts: Dict = None,
    ) -> models.ExportIgnoreRuleEffectHostListResponse:
        """
        This API is used to export the list of hosts affected by ignored detection items based on detection item IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportIgnoreRuleEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportIgnoreRuleEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportJavaMemShellPlugins(
            self,
            request: models.ExportJavaMemShellPluginsRequest,
            opts: Dict = None,
    ) -> models.ExportJavaMemShellPluginsResponse:
        """
        This API is used to export the Java webshell plugin information.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportJavaMemShellPlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportJavaMemShellPluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportJavaMemShells(
            self,
            request: models.ExportJavaMemShellsRequest,
            opts: Dict = None,
    ) -> models.ExportJavaMemShellsResponse:
        """
        This API is used to export the list of Java webshell events.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportJavaMemShells"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportJavaMemShellsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportLicenseDetail(
            self,
            request: models.ExportLicenseDetailRequest,
            opts: Dict = None,
    ) -> models.ExportLicenseDetailResponse:
        """
        This API is used to export authorization details.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportLicenseDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportLicenseDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportMaliciousRequests(
            self,
            request: models.ExportMaliciousRequestsRequest,
            opts: Dict = None,
    ) -> models.ExportMaliciousRequestsResponse:
        """
        This API is used to export the downloaded malicious request files.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportMaliciousRequests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportMaliciousRequestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportMalwares(
            self,
            request: models.ExportMalwaresRequest,
            opts: Dict = None,
    ) -> models.ExportMalwaresResponse:
        """
        This API is used to export Trojan records to a CSV file.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportNonlocalLoginPlaces(
            self,
            request: models.ExportNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.ExportNonlocalLoginPlacesResponse:
        """
        This API is used to export cross-region log-in event records in CSV format.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportPrivilegeEvents(
            self,
            request: models.ExportPrivilegeEventsRequest,
            opts: Dict = None,
    ) -> models.ExportPrivilegeEventsResponse:
        """
        This API is used to export local privilege escalation events.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportPrivilegeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportPrivilegeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRansomDefenseBackupList(
            self,
            request: models.ExportRansomDefenseBackupListRequest,
            opts: Dict = None,
    ) -> models.ExportRansomDefenseBackupListResponse:
        """
        This API is used to export the list of host snapshot backups.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRansomDefenseBackupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRansomDefenseBackupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRansomDefenseEventsList(
            self,
            request: models.ExportRansomDefenseEventsListRequest,
            opts: Dict = None,
    ) -> models.ExportRansomDefenseEventsListResponse:
        """
        This API is used to export the list of anti-ransomware events.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRansomDefenseEventsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRansomDefenseEventsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRansomDefenseMachineList(
            self,
            request: models.ExportRansomDefenseMachineListRequest,
            opts: Dict = None,
    ) -> models.ExportRansomDefenseMachineListResponse:
        """
        This API is used to export the backup details list.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRansomDefenseMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRansomDefenseMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRansomDefenseStrategyList(
            self,
            request: models.ExportRansomDefenseStrategyListRequest,
            opts: Dict = None,
    ) -> models.ExportRansomDefenseStrategyListResponse:
        """
        This API is used to export the anti-ransomware policy list.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRansomDefenseStrategyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRansomDefenseStrategyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRansomDefenseStrategyMachines(
            self,
            request: models.ExportRansomDefenseStrategyMachinesRequest,
            opts: Dict = None,
    ) -> models.ExportRansomDefenseStrategyMachinesResponse:
        """
        This API is used to export the list of machines bound to ransomware defense policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRansomDefenseStrategyMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRansomDefenseStrategyMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportReverseShellEvents(
            self,
            request: models.ExportReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.ExportReverseShellEventsResponse:
        """
        This API is used to export reverse shell events.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRiskDnsEventList(
            self,
            request: models.ExportRiskDnsEventListRequest,
            opts: Dict = None,
    ) -> models.ExportRiskDnsEventListResponse:
        """
        This API is used to export the malicious request event list.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRiskDnsEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRiskDnsEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRiskDnsPolicyList(
            self,
            request: models.ExportRiskDnsPolicyListRequest,
            opts: Dict = None,
    ) -> models.ExportRiskDnsPolicyListResponse:
        """
        This API is used to export the malicious request policy list.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRiskDnsPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRiskDnsPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRiskProcessEvents(
            self,
            request: models.ExportRiskProcessEventsRequest,
            opts: Dict = None,
    ) -> models.ExportRiskProcessEventsResponse:
        """
        This API is used to export abnormal process events.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRiskProcessEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRiskProcessEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportScanTaskDetails(
            self,
            request: models.ExportScanTaskDetailsRequest,
            opts: Dict = None,
    ) -> models.ExportScanTaskDetailsResponse:
        """
        This API is used to export the specified scan task details by task ID.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportScanTaskDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportScanTaskDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportSecurityTrends(
            self,
            request: models.ExportSecurityTrendsRequest,
            opts: Dict = None,
    ) -> models.ExportSecurityTrendsResponse:
        """
        This API is used to export risk trends.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportSecurityTrends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportSecurityTrendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportTasks(
            self,
            request: models.ExportTasksRequest,
            opts: Dict = None,
    ) -> models.ExportTasksResponse:
        """
        This API is used to export log files with large data volumes asynchronously.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulDefenceEvent(
            self,
            request: models.ExportVulDefenceEventRequest,
            opts: Dict = None,
    ) -> models.ExportVulDefenceEventResponse:
        """
        This API is used to export vulnerability defense events.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulDefenceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulDefenceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulDefenceList(
            self,
            request: models.ExportVulDefenceListRequest,
            opts: Dict = None,
    ) -> models.ExportVulDefenceListResponse:
        """
        This API is used to export the list of vulnerability defenses.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulDefenceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulDefenceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulDefencePluginEvent(
            self,
            request: models.ExportVulDefencePluginEventRequest,
            opts: Dict = None,
    ) -> models.ExportVulDefencePluginEventResponse:
        """
        This API is used to export vulnerability defense plugin events.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulDefencePluginEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulDefencePluginEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulDetectionExcel(
            self,
            request: models.ExportVulDetectionExcelRequest,
            opts: Dict = None,
    ) -> models.ExportVulDetectionExcelResponse:
        """
        This API is used to export the vulnerability detection Excel document.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulDetectionExcel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulDetectionExcelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulDetectionReport(
            self,
            request: models.ExportVulDetectionReportRequest,
            opts: Dict = None,
    ) -> models.ExportVulDetectionReportResponse:
        """
        This API is used to export the vulnerability detection report.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulDetectionReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulDetectionReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulEffectHostList(
            self,
            request: models.ExportVulEffectHostListRequest,
            opts: Dict = None,
    ) -> models.ExportVulEffectHostListResponse:
        """
        This API is used to export the list of hosts affected by vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulInfo(
            self,
            request: models.ExportVulInfoRequest,
            opts: Dict = None,
    ) -> models.ExportVulInfoResponse:
        """
        This API is used to export the vulnerability information, including the list of affected hosts and component information.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulList(
            self,
            request: models.ExportVulListRequest,
            opts: Dict = None,
    ) -> models.ExportVulListResponse:
        """
        This API is used to export the vulnerability list.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLocalStorageItem(
            self,
            request: models.GetLocalStorageItemRequest,
            opts: Dict = None,
    ) -> models.GetLocalStorageItemResponse:
        """
        This API is used to obtain the locally stored data.
        """
        
        kwargs = {}
        kwargs["action"] = "GetLocalStorageItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLocalStorageItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IgnoreImpactedHosts(
            self,
            request: models.IgnoreImpactedHostsRequest,
            opts: Dict = None,
    ) -> models.IgnoreImpactedHostsResponse:
        """
        This API is used to ignore vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "IgnoreImpactedHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IgnoreImpactedHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KeysLocalStorage(
            self,
            request: models.KeysLocalStorageRequest,
            opts: Dict = None,
    ) -> models.KeysLocalStorageResponse:
        """
        This API is used to obtain the list of locally stored key values.
        """
        
        kwargs = {}
        kwargs["action"] = "KeysLocalStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KeysLocalStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoOpenProVersionConfig(
            self,
            request: models.ModifyAutoOpenProVersionConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoOpenProVersionConfigResponse:
        """
        This API is used to enable the configuration of automatically enabling the professional protection configuration for newly added hosts.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoOpenProVersionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoOpenProVersionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBanMode(
            self,
            request: models.ModifyBanModeRequest,
            opts: Dict = None,
    ) -> models.ModifyBanModeResponse:
        """
        This API is used to modify the brute-force blocking mode.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBanMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBanModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBanStatus(
            self,
            request: models.ModifyBanStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBanStatusResponse:
        """
        This API is used to set the block switch status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBanStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBanWhiteList(
            self,
            request: models.ModifyBanWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyBanWhiteListResponse:
        """
        This API is used to modify the blocking allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBanWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBanWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselinePolicy(
            self,
            request: models.ModifyBaselinePolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselinePolicyResponse:
        """
        This API is used to change the baseline policy settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBashPolicy(
            self,
            request: models.ModifyBashPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyBashPolicyResponse:
        """
        This API is used to add or modify high-risk command policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBashPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBashPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBashPolicyStatus(
            self,
            request: models.ModifyBashPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBashPolicyStatusResponse:
        """
        This API is used to switch the statuses of high-risk command policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBashPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBashPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBruteAttackRules(
            self,
            request: models.ModifyBruteAttackRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyBruteAttackRulesResponse:
        """
        This API is used to modify brute force cracking rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBruteAttackRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBruteAttackRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEventAttackStatus(
            self,
            request: models.ModifyEventAttackStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEventAttackStatusResponse:
        """
        This API is used to modify the status of network attack events.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEventAttackStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEventAttackStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileTamperEvents(
            self,
            request: models.ModifyFileTamperEventsRequest,
            opts: Dict = None,
    ) -> models.ModifyFileTamperEventsResponse:
        """
        This API is used to update the core file events.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileTamperEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileTamperEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileTamperRule(
            self,
            request: models.ModifyFileTamperRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyFileTamperRuleResponse:
        """
        This API is used to edit and add core file monitoring rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileTamperRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileTamperRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileTamperRuleStatus(
            self,
            request: models.ModifyFileTamperRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyFileTamperRuleStatusResponse:
        """
        This API is used to update the core file rule status (batch deletion and disabling supported).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileTamperRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileTamperRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyJavaMemShellPluginSwitch(
            self,
            request: models.ModifyJavaMemShellPluginSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyJavaMemShellPluginSwitchResponse:
        """
        This API is used to enable and disable Java webshell plugins.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyJavaMemShellPluginSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyJavaMemShellPluginSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyJavaMemShellsStatus(
            self,
            request: models.ModifyJavaMemShellsStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyJavaMemShellsStatusResponse:
        """
        This API is used to modify the Java webshell event status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyJavaMemShellsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyJavaMemShellsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLicenseBinds(
            self,
            request: models.ModifyLicenseBindsRequest,
            opts: Dict = None,
    ) -> models.ModifyLicenseBindsResponse:
        """
        This API is used to bind machines to an authorization in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLicenseBinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLicenseBindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLicenseOrder(
            self,
            request: models.ModifyLicenseOrderRequest,
            opts: Dict = None,
    ) -> models.ModifyLicenseOrderResponse:
        """
        This API is used to edit CWPP - pay-as-you-go authorization orders.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLicenseOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLicenseOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogKafkaAccess(
            self,
            request: models.ModifyLogKafkaAccessRequest,
            opts: Dict = None,
    ) -> models.ModifyLogKafkaAccessResponse:
        """
        This API is used to add or modify the access configuration of logs shipped to Kafka.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogKafkaAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogKafkaAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogKafkaDeliverType(
            self,
            request: models.ModifyLogKafkaDeliverTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyLogKafkaDeliverTypeResponse:
        """
        This API is used to modify the shipping configuration and switch of the specified log category.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogKafkaDeliverType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogKafkaDeliverTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogKafkaState(
            self,
            request: models.ModifyLogKafkaStateRequest,
            opts: Dict = None,
    ) -> models.ModifyLogKafkaStateResponse:
        """
        This API is used to modify the information of log shipping statuses.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogKafkaState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogKafkaStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogStorageConfig(
            self,
            request: models.ModifyLogStorageConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyLogStorageConfigResponse:
        """
        This API is used to modify the log storage configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogStorageConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogStorageConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoginWhiteInfo(
            self,
            request: models.ModifyLoginWhiteInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyLoginWhiteInfoResponse:
        """
        This API is used to update the log-in audit allowlist information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoginWhiteInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoginWhiteInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoginWhiteRecord(
            self,
            request: models.ModifyLoginWhiteRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyLoginWhiteRecordResponse:
        """
        This API is used to update the log-in audit allowlist information. (The number of server lists needs to be less than 1,000.)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoginWhiteRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoginWhiteRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMachineAutoClearConfig(
            self,
            request: models.ModifyMachineAutoClearConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyMachineAutoClearConfigResponse:
        """
        This API is used to modify the cleanup configuration of the machine.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachineAutoClearConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachineAutoClearConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaliciousRequestWhiteList(
            self,
            request: models.ModifyMaliciousRequestWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyMaliciousRequestWhiteListResponse:
        """
        This API is used to update the malicious request allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaliciousRequestWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaliciousRequestWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMalwareTimingScanSettings(
            self,
            request: models.ModifyMalwareTimingScanSettingsRequest,
            opts: Dict = None,
    ) -> models.ModifyMalwareTimingScanSettingsResponse:
        """
        This API is used to set scheduled scan.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMalwareTimingScanSettings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMalwareTimingScanSettingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMalwareWhiteList(
            self,
            request: models.ModifyMalwareWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyMalwareWhiteListResponse:
        """
        This API is used to edit the Trojan allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMalwareWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMalwareWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetAttackSetting(
            self,
            request: models.ModifyNetAttackSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyNetAttackSettingResponse:
        """
        This API is used to modify network attack settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetAttackSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetAttackSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetAttackWhiteList(
            self,
            request: models.ModifyNetAttackWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyNetAttackWhiteListResponse:
        """
        This API is used to edit the network attack whitelist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetAttackWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetAttackWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRansomDefenseEventsStatus(
            self,
            request: models.ModifyRansomDefenseEventsStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRansomDefenseEventsStatusResponse:
        """
        This API is used to modify the status of anti-ransomware events.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRansomDefenseEventsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRansomDefenseEventsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRansomDefenseStrategyStatus(
            self,
            request: models.ModifyRansomDefenseStrategyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRansomDefenseStrategyStatusResponse:
        """
        This API is used to modify the anti-ransomware policy status in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRansomDefenseStrategyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRansomDefenseStrategyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskDnsPolicy(
            self,
            request: models.ModifyRiskDnsPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskDnsPolicyResponse:
        """
        This API is used to modify malicious request policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskDnsPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskDnsPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskDnsPolicyStatus(
            self,
            request: models.ModifyRiskDnsPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskDnsPolicyStatusResponse:
        """
        This API is used to modify the status of malicious request policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskDnsPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskDnsPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskEventsStatus(
            self,
            request: models.ModifyRiskEventsStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskEventsStatusResponse:
        """
        This API is used to change the status of intrusion detection events, including virus scanning, abnormal log-ins, password cracking, high-risk commands, reverse shells, and local privilege escalations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskEventsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskEventsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUsersConfig(
            self,
            request: models.ModifyUsersConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyUsersConfigResponse:
        """
        This API is used to create or modify user custom settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUsersConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUsersConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulDefenceEventStatus(
            self,
            request: models.ModifyVulDefenceEventStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyVulDefenceEventStatusResponse:
        """
        This API is used to change the vulnerability defense event status. (Vulnerability fixing is carried out using another API.)
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
        This API is used to modify vulnerability defense plugin settings.
        1) The new settings apply to new hosts automatically. scope is set to 1, and quuids is left blank.
        2) The new settings do not apply to Ultimate Edition hosts. scope is set to 0, and the current QUUID list is specified as the value of quuids.
        3) For a given QUUID list, when scope is set to 0, QUUID selected by the user is specified as the value of quuids.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulDefenceSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulDefenceSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWarningHostConfig(
            self,
            request: models.ModifyWarningHostConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyWarningHostConfigResponse:
        """
        This API is used to modify the alarming machine scope settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWarningHostConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWarningHostConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWarningSetting(
            self,
            request: models.ModifyWarningSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyWarningSettingResponse:
        """
        This API is used to modify alarm settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWarningSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWarningSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebHookPolicy(
            self,
            request: models.ModifyWebHookPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyWebHookPolicyResponse:
        """
        This API is used to add or modify alarm policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebHookPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebHookPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebHookPolicyStatus(
            self,
            request: models.ModifyWebHookPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyWebHookPolicyStatusResponse:
        """
        This API is used to modify the alarm policy switch.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebHookPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebHookPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebHookReceiver(
            self,
            request: models.ModifyWebHookReceiverRequest,
            opts: Dict = None,
    ) -> models.ModifyWebHookReceiverResponse:
        """
        This API is used to add or update the alarm recipient.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebHookReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebHookReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebHookRule(
            self,
            request: models.ModifyWebHookRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyWebHookRuleResponse:
        """
        This API is used to add or modify the rules of WeCom chatbots.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebHookRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebHookRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebHookRuleStatus(
            self,
            request: models.ModifyWebHookRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyWebHookRuleStatusResponse:
        """
        This API is used to modify the rules of WeCom chatbots.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebHookRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebHookRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebPageProtectSwitch(
            self,
            request: models.ModifyWebPageProtectSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyWebPageProtectSwitchResponse:
        """
        This API is used to enable or disable website anti-tampering protection.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebPageProtectSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebPageProtectSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RansomDefenseRollback(
            self,
            request: models.RansomDefenseRollbackRequest,
            opts: Dict = None,
    ) -> models.RansomDefenseRollbackResponse:
        """
        This API is used to roll back anti-ransomware snapshots.
        """
        
        kwargs = {}
        kwargs["action"] = "RansomDefenseRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RansomDefenseRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverMalwares(
            self,
            request: models.RecoverMalwaresRequest,
            opts: Dict = None,
    ) -> models.RecoverMalwaresResponse:
        """
        This API is used to batch recover quarantined Trojan files.
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveLocalStorageItem(
            self,
            request: models.RemoveLocalStorageItemRequest,
            opts: Dict = None,
    ) -> models.RemoveLocalStorageItemResponse:
        """
        This API is used to delete the locally stored data.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveLocalStorageItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveLocalStorageItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveMachine(
            self,
            request: models.RemoveMachineRequest,
            opts: Dict = None,
    ) -> models.RemoveMachineResponse:
        """
        This API is used to delete all records of the host. Currently, it only supports non-Tencent Cloud hosts, and the host needs to be offline.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryCreateSnapshot(
            self,
            request: models.RetryCreateSnapshotRequest,
            opts: Dict = None,
    ) -> models.RetryCreateSnapshotResponse:
        """
        This API is used to retry to create snapshots and automatically fix vulnerabilities when the creation fails.
        """
        
        kwargs = {}
        kwargs["action"] = "RetryCreateSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryCreateSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryVulFix(
            self,
            request: models.RetryVulFixRequest,
            opts: Dict = None,
    ) -> models.RetryVulFixResponse:
        """
        This API is used to fix vulnerabilities on a single host when the fix fails.
        """
        
        kwargs = {}
        kwargs["action"] = "RetryVulFix"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryVulFixResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanBaseline(
            self,
            request: models.ScanBaselineRequest,
            opts: Dict = None,
    ) -> models.ScanBaselineResponse:
        """
        This API is used to obtain baseline detection and re-detection APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanBaseline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanBaselineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanTaskAgain(
            self,
            request: models.ScanTaskAgainRequest,
            opts: Dict = None,
    ) -> models.ScanTaskAgainResponse:
        """
        This API is used to restart the scan task. Specifying the machine is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanTaskAgain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanTaskAgainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanVul(
            self,
            request: models.ScanVulRequest,
            opts: Dict = None,
    ) -> models.ScanVulResponse:
        """
        This API is used to perform one-click vulnerability scans.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanVulAgain(
            self,
            request: models.ScanVulAgainRequest,
            opts: Dict = None,
    ) -> models.ScanVulAgainResponse:
        """
        This API is used to redetect the API.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanVulAgain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanVulAgainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanVulSetting(
            self,
            request: models.ScanVulSettingRequest,
            opts: Dict = None,
    ) -> models.ScanVulSettingResponse:
        """
        This API is used to complete regular vulnerability scan settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanVulSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanVulSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchLog(
            self,
            request: models.SearchLogRequest,
            opts: Dict = None,
    ) -> models.SearchLogResponse:
        """
        This API is used to query logs.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SeparateMalwares(
            self,
            request: models.SeparateMalwaresRequest,
            opts: Dict = None,
    ) -> models.SeparateMalwaresResponse:
        """
        This API is used to isolate Trojans.
        """
        
        kwargs = {}
        kwargs["action"] = "SeparateMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SeparateMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetBashEventsStatus(
            self,
            request: models.SetBashEventsStatusRequest,
            opts: Dict = None,
    ) -> models.SetBashEventsStatusResponse:
        """
        This API is used to set the high-risk command event status.
        """
        
        kwargs = {}
        kwargs["action"] = "SetBashEventsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetBashEventsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLocalStorageExpire(
            self,
            request: models.SetLocalStorageExpireRequest,
            opts: Dict = None,
    ) -> models.SetLocalStorageExpireResponse:
        """
        This API is used to set the expiration time of the locally stored data.
        """
        
        kwargs = {}
        kwargs["action"] = "SetLocalStorageExpire"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLocalStorageExpireResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLocalStorageItem(
            self,
            request: models.SetLocalStorageItemRequest,
            opts: Dict = None,
    ) -> models.SetLocalStorageItemResponse:
        """
        This API is used to set the locally stored data.
        """
        
        kwargs = {}
        kwargs["action"] = "SetLocalStorageItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLocalStorageItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartBaselineDetect(
            self,
            request: models.StartBaselineDetectRequest,
            opts: Dict = None,
    ) -> models.StartBaselineDetectResponse:
        """
        This API is used to perform baseline checks.
        """
        
        kwargs = {}
        kwargs["action"] = "StartBaselineDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartBaselineDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAssetScan(
            self,
            request: models.StopAssetScanRequest,
            opts: Dict = None,
    ) -> models.StopAssetScanResponse:
        """
        This API is used to stop the asset scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "StopAssetScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAssetScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopBaselineDetect(
            self,
            request: models.StopBaselineDetectRequest,
            opts: Dict = None,
    ) -> models.StopBaselineDetectResponse:
        """
        This API is used to stop baseline check.
        """
        
        kwargs = {}
        kwargs["action"] = "StopBaselineDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopBaselineDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopNoticeBanTips(
            self,
            request: models.StopNoticeBanTipsRequest,
            opts: Dict = None,
    ) -> models.StopNoticeBanTipsResponse:
        """
        This API is used to stop displaying pop-up prompts about brute force cracking blocking.
        """
        
        kwargs = {}
        kwargs["action"] = "StopNoticeBanTips"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopNoticeBanTipsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchBashRules(
            self,
            request: models.SwitchBashRulesRequest,
            opts: Dict = None,
    ) -> models.SwitchBashRulesResponse:
        """
        This API is used to switch the statuses of high-risk command rules.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncAssetScan(
            self,
            request: models.SyncAssetScanRequest,
            opts: Dict = None,
    ) -> models.SyncAssetScanResponse:
        """
        This API is used to synchronize the asset scan information.
        """
        
        kwargs = {}
        kwargs["action"] = "SyncAssetScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncAssetScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncBaselineDetectSummary(
            self,
            request: models.SyncBaselineDetectSummaryRequest,
            opts: Dict = None,
    ) -> models.SyncBaselineDetectSummaryResponse:
        """
        This API is used to sync the summary of baseline detection progress.
        """
        
        kwargs = {}
        kwargs["action"] = "SyncBaselineDetectSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncBaselineDetectSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncMachines(
            self,
            request: models.SyncMachinesRequest,
            opts: Dict = None,
    ) -> models.SyncMachinesResponse:
        """
        This API is used to sync the machine information.
        """
        
        kwargs = {}
        kwargs["action"] = "SyncMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TestWebHookRule(
            self,
            request: models.TestWebHookRuleRequest,
            opts: Dict = None,
    ) -> models.TestWebHookRuleResponse:
        """
        This API is used to test the rules of WeCom chatbots.
        """
        
        kwargs = {}
        kwargs["action"] = "TestWebHookRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TestWebHookRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TrustMalwares(
            self,
            request: models.TrustMalwaresRequest,
            opts: Dict = None,
    ) -> models.TrustMalwaresResponse:
        """
        This API is used to mark identified Trojan files as Trusted.
        """
        
        kwargs = {}
        kwargs["action"] = "TrustMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TrustMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UntrustMalwares(
            self,
            request: models.UntrustMalwaresRequest,
            opts: Dict = None,
    ) -> models.UntrustMalwaresResponse:
        """
        This API is used to untrust Trojan files.
        """
        
        kwargs = {}
        kwargs["action"] = "UntrustMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UntrustMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateBaselineStrategy(
            self,
            request: models.UpdateBaselineStrategyRequest,
            opts: Dict = None,
    ) -> models.UpdateBaselineStrategyResponse:
        """
        This API is used to update the policy information based on baseline policy IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateBaselineStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateBaselineStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateMachineTags(
            self,
            request: models.UpdateMachineTagsRequest,
            opts: Dict = None,
    ) -> models.UpdateMachineTagsResponse:
        """
        This API is used to obtain the list of tags associated with machines.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateMachineTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateMachineTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)