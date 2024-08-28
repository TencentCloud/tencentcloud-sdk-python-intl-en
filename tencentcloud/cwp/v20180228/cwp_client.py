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
from tencentcloud.cwp.v20180228 import models


class CwpClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'cwp.tencentcloudapi.com'
    _service = 'cwp'


    def AddLoginWhiteLists(self, request):
        """This API is used to add cross-region log-in allowlists in batches.

        :param request: Request instance for AddLoginWhiteLists.
        :type request: :class:`tencentcloud.cwp.v20180228.models.AddLoginWhiteListsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.AddLoginWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLoginWhiteLists", params, headers=headers)
            response = json.loads(body)
            model = models.AddLoginWhiteListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelIgnoreVul(self, request):
        """This API is used to unignore the vulnerabilities.

        :param request: Request instance for CancelIgnoreVul.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CancelIgnoreVulRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CancelIgnoreVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelIgnoreVul", params, headers=headers)
            response = json.loads(body)
            model = models.CancelIgnoreVulResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeRuleEventsIgnoreStatus(self, request):
        """This API is used to ignore events or cancel ignoring in batches based on check item ID or event ID.

        :param request: Request instance for ChangeRuleEventsIgnoreStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ChangeRuleEventsIgnoreStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ChangeRuleEventsIgnoreStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeRuleEventsIgnoreStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeRuleEventsIgnoreStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeStrategyEnableStatus(self, request):
        """This API is used to change the policy availability status by policy ID.

        :param request: Request instance for ChangeStrategyEnableStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ChangeStrategyEnableStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ChangeStrategyEnableStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeStrategyEnableStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeStrategyEnableStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckBashPolicyParams(self, request):
        """This API is used to verify parameters entered for adding and editing high-risk command user rules.

        :param request: Request instance for CheckBashPolicyParams.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckBashPolicyParamsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckBashPolicyParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBashPolicyParams", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBashPolicyParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckBashRuleParams(self, request):
        """This API is used to verify parameters entered for adding and editing high-risk command user rules.

        :param request: Request instance for CheckBashRuleParams.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckBashRuleParamsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckBashRuleParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBashRuleParams", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBashRuleParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckFileTamperRule(self, request):
        """This API is used to check the rule parameters entered at the core file monitoring frontend.

        :param request: Request instance for CheckFileTamperRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckFileTamperRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckFileTamperRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFileTamperRule", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFileTamperRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckFirstScanBaseline(self, request):
        """This API is used to query whether the baseline is detected for the first time.

        :param request: Request instance for CheckFirstScanBaseline.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckFirstScanBaselineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckFirstScanBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFirstScanBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFirstScanBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckLogKafkaConnectionState(self, request):
        """This API is used to check the connectivity for log shipping from Kafka.

        :param request: Request instance for CheckLogKafkaConnectionState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckLogKafkaConnectionStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckLogKafkaConnectionStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckLogKafkaConnectionState", params, headers=headers)
            response = json.loads(body)
            model = models.CheckLogKafkaConnectionStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearLocalStorage(self, request):
        """This API is used to clean up the locally stored data.

        :param request: Request instance for ClearLocalStorage.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ClearLocalStorageRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ClearLocalStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearLocalStorage", params, headers=headers)
            response = json.loads(body)
            model = models.ClearLocalStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBanWhiteList(self, request):
        """This API is used to add the list of block allowlists.

        :param request: Request instance for CreateBanWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateBanWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateBanWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBanWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBanWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaselineStrategy(self, request):
        """This API is used to create a baseline policy based on the policy information.

        :param request: Request instance for CreateBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaselineStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBuyBindTask(self, request):
        """This API is used to create an automatic binding task for newly purchased authorizations.

        :param request: Request instance for CreateBuyBindTask.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateBuyBindTaskRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateBuyBindTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBuyBindTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBuyBindTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudProtectServiceOrderRecord(self, request):
        """云护航计费产品已下线

        This API is used to confirm the receipt after using the cloud escort service.

        :param request: Request instance for CreateCloudProtectServiceOrderRecord.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateCloudProtectServiceOrderRecordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateCloudProtectServiceOrderRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudProtectServiceOrderRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudProtectServiceOrderRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmergencyVulScan(self, request):
        """This API is used to create emergency vulnerability scan tasks.

        :param request: Request instance for CreateEmergencyVulScan.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateEmergencyVulScanRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateEmergencyVulScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmergencyVulScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmergencyVulScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIncidentBacktracking(self, request):
        """This API is used to trigger event investigation and alarm backtracking for Ultimate Edition machines.

        :param request: Request instance for CreateIncidentBacktracking.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateIncidentBacktrackingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateIncidentBacktrackingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIncidentBacktracking", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIncidentBacktrackingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLicenseOrder(self, request):
        """This API is used to create Professional/Flagship edition orders
        .This API is used to support creating orders through prepaid and pay-as-you-go.
        This API is used to directly create postpaid orders.
        This API is used to call the billing payment API for payment since prepaid orders are only placed but not paid.

        :param request: Request instance for CreateLicenseOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateLicenseOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateLicenseOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLicenseOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLicenseOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLogExport(self, request):
        """This API is used to create log download tasks.

        :param request: Request instance for CreateLogExport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateLogExportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateLogExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogExport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLogExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMaliciousRequestWhiteList(self, request):
        """This API is used to add malicious request allowlists.

        :param request: Request instance for CreateMaliciousRequestWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateMaliciousRequestWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateMaliciousRequestWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMaliciousRequestWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMaliciousRequestWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMalwareWhiteList(self, request):
        """This API is used to create the Trojan allowlist.

        :param request: Request instance for CreateMalwareWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateMalwareWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateMalwareWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMalwareWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMalwareWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetAttackWhiteList(self, request):
        """This API is used to create a network attack allowlist.

        :param request: Request instance for CreateNetAttackWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateNetAttackWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateNetAttackWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetAttackWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetAttackWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRansomDefenseStrategy(self, request):
        """This API is used to create or modify anti-ransomware policies.

        :param request: Request instance for CreateRansomDefenseStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateRansomDefenseStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateRansomDefenseStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRansomDefenseStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRansomDefenseStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScanMalwareSetting(self, request):
        """This API is used to detect the intrusion and virus scanning.

        :param request: Request instance for CreateScanMalwareSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateScanMalwareSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateScanMalwareSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScanMalwareSetting", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScanMalwareSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSearchLog(self, request):
        """This API is used to add history search records.

        :param request: Request instance for CreateSearchLog.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateSearchLogRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateSearchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSearchLog", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSearchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSearchTemplate(self, request):
        """This API is used to add the	retrieval template.

        :param request: Request instance for CreateSearchTemplate.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateSearchTemplateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateSearchTemplateResponse`

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


    def CreateVulFix(self, request):
        """This API is used to submit the vulnerabilities and fix them.

        :param request: Request instance for CreateVulFix.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateVulFixRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateVulFixResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulFix", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulFixResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWhiteListOrder(self, request):
        """This API is used to create allowlist orders.

        :param request: Request instance for CreateWhiteListOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateWhiteListOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateWhiteListOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWhiteListOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWhiteListOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAllJavaMemShells(self, request):
        """This API is used to delete all Java webshell events.

        :param request: Request instance for DeleteAllJavaMemShells.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteAllJavaMemShellsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteAllJavaMemShellsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAllJavaMemShells", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAllJavaMemShellsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBanWhiteList(self, request):
        """This API is used to delete the list of blocking allowlists.

        :param request: Request instance for DeleteBanWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBanWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBanWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBanWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBanWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselinePolicy(self, request):
        """This API is used to delete the baseline policy configuration.

        :param request: Request instance for DeleteBaselinePolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineStrategy(self, request):
        """This API is used to delete the policy by baseline policy ID.

        :param request: Request instance for DeleteBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBashEvents(self, request):
        """This API is used to delete high-risk command events based on IDs.

        :param request: Request instance for DeleteBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBashPolicies(self, request):
        """This API is used to delete high-risk command policies.

        :param request: Request instance for DeleteBashPolicies.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBashPoliciesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBashPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBashPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBashPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBashRules(self, request):
        """This API is used to delete high-risk command rules.

        :param request: Request instance for DeleteBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBruteAttacks(self, request):
        """This API is used to delete brute force attack records.

        :param request: Request instance for DeleteBruteAttacks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBruteAttacksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLicenseRecord(self, request):
        """This API is used to delete expired orders in Authorization Management - Order List. (Deleted orders are not counted in statistics.)

        :param request: Request instance for DeleteLicenseRecord.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLicenseRecordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLicenseRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLicenseRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLicenseRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLicenseRecordAll(self, request):
        """This API is used to delete all authorization records.

        :param request: Request instance for DeleteLicenseRecordAll.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLicenseRecordAllRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLicenseRecordAllResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLicenseRecordAll", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLicenseRecordAllResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLogExport(self, request):
        """This API is used to delete log download tasks.

        :param request: Request instance for DeleteLogExport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLogExportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLogExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogExport", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoginWhiteList(self, request):
        """This API is used to delete the cross-region log-in allowlist rules.

        :param request: Request instance for DeleteLoginWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachine(self, request):
        """This API is used to uninstall the CWPP client.

        :param request: Request instance for DeleteMachine.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineResponse`

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


    def DeleteMachineClearHistory(self, request):
        """This API is used to delete clearing records of a machine.

        :param request: Request instance for DeleteMachineClearHistory.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineClearHistoryRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineClearHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineClearHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineClearHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachineTag(self, request):
        """This API is used to delete tags associated with the server.

        :param request: Request instance for DeleteMachineTag.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineTagRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMaliciousRequestWhiteList(self, request):
        """This API is used to delete the malicious request allowlist.

        :param request: Request instance for DeleteMaliciousRequestWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMaliciousRequestWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMaliciousRequestWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMaliciousRequests(self, request):
        """This API is used to delete malicious request records.

        :param request: Request instance for DeleteMaliciousRequests.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMalwareScanTask(self, request):
        """This API is used to terminate the scan tasks.

        :param request: Request instance for DeleteMalwareScanTask.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwareScanTaskRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwareScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMalwareScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMalwareScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMalwareWhiteList(self, request):
        """This API is used to delete the Trojan whitelist.

        :param request: Request instance for DeleteMalwareWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwareWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwareWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMalwareWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMalwareWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMalwares(self, request):
        """This API is used to delete Trojan records.

        :param request: Request instance for DeleteMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetAttackWhiteList(self, request):
        """This API is used to delete the network attack allowlist.

        :param request: Request instance for DeleteNetAttackWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteNetAttackWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteNetAttackWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetAttackWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetAttackWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNonlocalLoginPlaces(self, request):
        """This API is used to delete cross-region log-in records.

        :param request: Request instance for DeleteNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivilegeEvents(self, request):
        """This API is used to delete local privilege escalation based on IDs.

        :param request: Request instance for DeletePrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivilegeRules(self, request):
        """This API is used to delete local privilege elevation rules.

        :param request: Request instance for DeletePrivilegeRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivilegeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivilegeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReverseShellEvents(self, request):
        """This API is used to delete Reverse Shell events based on IDs.

        :param request: Request instance for DeleteReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellEventsResponse`

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


    def DeleteReverseShellRules(self, request):
        """This API is used to delete Reverse Shell rules.

        :param request: Request instance for DeleteReverseShellRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReverseShellRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRiskDnsEvent(self, request):
        """This API is used to delete malicious request events.

        :param request: Request instance for DeleteRiskDnsEvent.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteRiskDnsEventRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteRiskDnsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskDnsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRiskDnsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRiskDnsPolicy(self, request):
        """This API is used to delete malicious request policies.

        :param request: Request instance for DeleteRiskDnsPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteRiskDnsPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteRiskDnsPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskDnsPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRiskDnsPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScanTask(self, request):
        """This API is used to stop scan tasks of a specified type.

        :param request: Request instance for DeleteScanTask.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteScanTaskRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSearchTemplate(self, request):
        """This API is used to delete the retrieval template.

        :param request: Request instance for DeleteSearchTemplate.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteSearchTemplateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteSearchTemplateResponse`

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


    def DeleteTags(self, request):
        """This API is used to delete tags.

        :param request: Request instance for DeleteTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTags", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebHookPolicy(self, request):
        """This API is used to delete alarm policies.

        :param request: Request instance for DeleteWebHookPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebHookPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebHookPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebHookReceiver(self, request):
        """This API is used to delete the alert recipient.

        :param request: Request instance for DeleteWebHookReceiver.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookReceiverRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebHookReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebHookReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebHookRule(self, request):
        """This API is used to delete the rules of WeCom chatbots.

        :param request: Request instance for DeleteWebHookRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebHookRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebHookRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeABTestConfig(self, request):
        """This API is used to obtain the current grayscale configuration of the user.

        :param request: Request instance for DescribeABTestConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeABTestConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeABTestConfigResponse`

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


    def DescribeAESKey(self, request):
        """This API is used to obtain the configured aeskey and aesiv.

        :param request: Request instance for DescribeAESKey.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAESKeyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAESKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAESKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAESKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountStatistics(self, request):
        """This API is used to obtain the account statistics data.

        :param request: Request instance for DescribeAccountStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAccountStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAccountStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentInstallCommand(self, request):
        """This API is used to obtain the agent installation command.

        :param request: Request instance for DescribeAgentInstallCommand.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAgentInstallCommandRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAgentInstallCommandResponse`

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


    def DescribeAgentInstallationToken(self, request):
        """This API is used to obtain the token for installing the agent in a hybrid cloud environment.

        :param request: Request instance for DescribeAgentInstallationToken.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAgentInstallationTokenRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAgentInstallationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentInstallationToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentInstallationTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmIncidentNodes(self, request):
        """This API is used to obtain all node information on the event corresponding to an alarm.

        :param request: Request instance for DescribeAlarmIncidentNodes.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmIncidentNodesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmIncidentNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmIncidentNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmIncidentNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmVertexId(self, request):
        """This API is used to query the list of alarm IDs.

        :param request: Request instance for DescribeAlarmVertexId.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmVertexIdRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmVertexIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmVertexId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmVertexIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetAppCount(self, request):
        """This API is used to obtain the number of all software applications.

        :param request: Request instance for DescribeAssetAppCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetAppCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetAppCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetAppList(self, request):
        """This API is used to query the application list.

        :param request: Request instance for DescribeAssetAppList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetAppList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetAppProcessList(self, request):
        """This API is used to obtain the list of software's associated processes.

        :param request: Request instance for DescribeAssetAppProcessList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppProcessListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetAppProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetAppProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetCoreModuleInfo(self, request):
        """This API is used to obtain the kernel module details.

        :param request: Request instance for DescribeAssetCoreModuleInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetCoreModuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetCoreModuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetCoreModuleList(self, request):
        """This API is used to query the list of asset management kernel modules.

        :param request: Request instance for DescribeAssetCoreModuleList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetCoreModuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetCoreModuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDatabaseCount(self, request):
        """This API is used to obtain the number of all databases.

        :param request: Request instance for DescribeAssetDatabaseCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDatabaseCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDatabaseCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDatabaseInfo(self, request):
        """This API is used to obtain the asset management database details.

        :param request: Request instance for DescribeAssetDatabaseInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDatabaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDatabaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDatabaseList(self, request):
        """This API is used to query the list of asset management databases.

        :param request: Request instance for DescribeAssetDatabaseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDatabaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDatabaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDiskList(self, request):
        """This API is used to obtain the host disk partition list.

        :param request: Request instance for DescribeAssetDiskList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDiskListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetEnvList(self, request):
        """This API is used to query the list of asset management environment variables.

        :param request: Request instance for DescribeAssetEnvList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetEnvListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetEnvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetEnvList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetEnvListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetHostTotalCount(self, request):
        """This API is used to obtain the total number of resources of the host.

        :param request: Request instance for DescribeAssetHostTotalCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetHostTotalCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetHostTotalCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetHostTotalCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetHostTotalCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetInfo(self, request):
        """This API is used to obtain the number of assets, including hosts, accounts, ports, processes, software, databases, web applications, web frameworks, web services, and web sites.

        :param request: Request instance for DescribeAssetInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetInitServiceList(self, request):
        """This API is used to query the list of asset management start services.

        :param request: Request instance for DescribeAssetInitServiceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInitServiceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInitServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetInitServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetInitServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetJarInfo(self, request):
        """This API is used to obtain Jar package details.

        :param request: Request instance for DescribeAssetJarInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetJarInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetJarInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetJarList(self, request):
        """This API is used to query the list of Jar packages.

        :param request: Request instance for DescribeAssetJarList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetJarList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetJarListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetLoadInfo(self, request):
        """This API is used to obtain the utilization of the system load, memory, and hard disk.

        :param request: Request instance for DescribeAssetLoadInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetLoadInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetLoadInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetLoadInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetLoadInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetMachineDetail(self, request):
        """This API is used to obtain asset management host resource details.

        :param request: Request instance for DescribeAssetMachineDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetMachineDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetMachineDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetMachineList(self, request):
        """This API is used to obtain the resource monitoring list of the asset fingerprint page.

        :param request: Request instance for DescribeAssetMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetMachineTagTop(self, request):
        """This API is used to obtain top 5 host tags.

        :param request: Request instance for DescribeAssetMachineTagTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineTagTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineTagTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetMachineTagTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetMachineTagTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetPlanTaskList(self, request):
        """This API is used to query the list of asset management plan tasks.

        :param request: Request instance for DescribeAssetPlanTaskList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPlanTaskListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPlanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetPlanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetPlanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetPortCount(self, request):
        """This API is used to obtain the total number of ports.

        :param request: Request instance for DescribeAssetPortCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPortCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPortCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetPortCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetPortCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetPortInfoList(self, request):
        """This API is used to obtain the list of asset management ports.

        :param request: Request instance for DescribeAssetPortInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPortInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPortInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetPortInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetPortInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetProcessCount(self, request):
        """This API is used to obtain the total number of processes.

        :param request: Request instance for DescribeAssetProcessCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetProcessCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetProcessCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetProcessCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetProcessCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetProcessInfoList(self, request):
        """This API is used to obtain the list of asset management processes.

        :param request: Request instance for DescribeAssetProcessInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetProcessInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetProcessInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetProcessInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetProcessInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetRecentMachineInfo(self, request):
        """This API is used to obtain the latest trend of hosts.

        :param request: Request instance for DescribeAssetRecentMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetRecentMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetRecentMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetRecentMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetRecentMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetSystemPackageList(self, request):
        """This API is used to obtain the list of system installation packages for asset management.

        :param request: Request instance for DescribeAssetSystemPackageList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetSystemPackageListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetSystemPackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSystemPackageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetSystemPackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTotalCount(self, request):
        """This API is used to obtain the number of resources, including hosts, accounts, ports, processes, software, databases, web applications, web frameworks, web services, and web sites.

        :param request: Request instance for DescribeAssetTotalCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTotalCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTotalCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTotalCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTotalCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTypeTop(self, request):
        """This API is used to obtain Top5 resources of various types.

        :param request: Request instance for DescribeAssetTypeTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTypeTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTypeTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTypeTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTypeTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTypes(self, request):
        """This API is used to obtain the asset fingerprint type list.

        :param request: Request instance for DescribeAssetTypes.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTypesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetUserCount(self, request):
        """This API is used to obtain the total number of accounts.

        :param request: Request instance for DescribeAssetUserCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetUserCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetUserCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetUserInfo(self, request):
        """This API is used to obtain host account details.

        :param request: Request instance for DescribeAssetUserInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetUserKeyList(self, request):
        """This API is used to obtain the list of host account Keys.

        :param request: Request instance for DescribeAssetUserKeyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserKeyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetUserKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetUserKeyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetUserList(self, request):
        """This API is used to obtain the list of accounts.

        :param request: Request instance for DescribeAssetUserList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebAppCount(self, request):
        """This API is used to obtain the number of all web applications.

        :param request: Request instance for DescribeAssetWebAppCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebAppCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebAppCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebAppList(self, request):
        """This API is used to obtain the list of asset management web applications.

        :param request: Request instance for DescribeAssetWebAppList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebAppList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebAppPluginList(self, request):
        """This API is used to obtain the list of asset management Web application plugins.

        :param request: Request instance for DescribeAssetWebAppPluginList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppPluginListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppPluginListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebAppPluginList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebAppPluginListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebFrameCount(self, request):
        """This API is used to obtain the number of all Web frameworks.

        :param request: Request instance for DescribeAssetWebFrameCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebFrameCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebFrameCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebFrameCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebFrameCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebFrameList(self, request):
        """This API is used to obtain the list of asset management Web frameworks.

        :param request: Request instance for DescribeAssetWebFrameList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebFrameListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebFrameListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebFrameList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebFrameListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebLocationCount(self, request):
        """This API is used to obtain the total number of Web sites.

        :param request: Request instance for DescribeAssetWebLocationCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebLocationCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebLocationCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebLocationInfo(self, request):
        """This API is used to obtain the Web site details.

        :param request: Request instance for DescribeAssetWebLocationInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebLocationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebLocationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebLocationList(self, request):
        """This API is used to obtain the list of Web sites.

        :param request: Request instance for DescribeAssetWebLocationList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebLocationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebLocationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebLocationPathList(self, request):
        """This API is used to obtain the list of Web sites' virtual directories.

        :param request: Request instance for DescribeAssetWebLocationPathList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationPathListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationPathListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebLocationPathList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebLocationPathListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebServiceCount(self, request):
        """This API is used to obtain the number of all web services.

        :param request: Request instance for DescribeAssetWebServiceCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebServiceCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebServiceCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebServiceInfoList(self, request):
        """This API is used to query the list of asset management Web services.

        :param request: Request instance for DescribeAssetWebServiceInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebServiceInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebServiceInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebServiceProcessList(self, request):
        """This API is used to obtain the list of processes associated with Web services.

        :param request: Request instance for DescribeAssetWebServiceProcessList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceProcessListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebServiceProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebServiceProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackEventInfo(self, request):
        """This API is used to obtain network attack details.

        :param request: Request instance for DescribeAttackEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackEvents(self, request):
        """This API is used to display the list of network attack detection events in pagination.

        :param request: Request instance for DescribeAttackEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackLogs(self, request):
        """This API is used to display the list of network attack logs in pagination.

        :param request: Request instance for DescribeAttackLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackSource(self, request):
        """This API is used to backtrack attacks.

        :param request: Request instance for DescribeAttackSource.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackSourceRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackSource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackSourceEvents(self, request):
        """This API is used to query attack backtracking events.

        :param request: Request instance for DescribeAttackSourceEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackSourceEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackSourceEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackSourceEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackSourceEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackStatistics(self, request):
        """This API is used to obtain the statistics of network attack data.

        :param request: Request instance for DescribeAttackStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackTop(self, request):
        """This API is used to obtain the list of Top 5 network attacks.

        :param request: Request instance for DescribeAttackTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackTrends(self, request):
        """This API is used to obtain the network attack trend data.

        :param request: Request instance for DescribeAttackTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackTrends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackVulTypeList(self, request):
        """This API is used to obtain the list of network attack threat types.

        :param request: Request instance for DescribeAttackVulTypeList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackVulTypeListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackVulTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackVulTypeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackVulTypeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableExpertServiceDetail(self, request):
        """This API is used to obtain available order details.

        :param request: Request instance for DescribeAvailableExpertServiceDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAvailableExpertServiceDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAvailableExpertServiceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableExpertServiceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableExpertServiceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanMode(self, request):
        """This API is used to obtain the brute-force blocking mode.

        :param request: Request instance for DescribeBanMode.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanModeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanRegions(self, request):
        """This API is used to obtain the block region.

        :param request: Request instance for DescribeBanRegions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanRegionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanStatus(self, request):
        """This API is used to obtain the block button status.

        :param request: Request instance for DescribeBanStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanWhiteList(self, request):
        """This API is used to obtain the blocking allowlist list.

        :param request: Request instance for DescribeBanWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineBasicInfo(self, request):
        """This API is used to query the list of baseline basic information.

        :param request: Request instance for DescribeBaselineBasicInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineBasicInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDefaultStrategyList(self, request):
        """This API is used to query the list information of default policies of the baseline.

        :param request: Request instance for DescribeBaselineDefaultStrategyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDefaultStrategyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDefaultStrategyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDefaultStrategyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDefaultStrategyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDetail(self, request):
        """This API is used to query baseline details by baseline ID.

        :param request: Request instance for DescribeBaselineDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineEffectHostList(self, request):
        """This API is used to query the list of hosts affected by a baseline based on baseline ID.

        :param request: Request instance for DescribeBaselineEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineHostDetectList(self, request):
        """This API is used to obtain the list of hosts for baseline detection.

        :param request: Request instance for DescribeBaselineHostDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineHostDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineHostDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineHostTop(self, request):
        """This API is used to return Top N risky servers.

        :param request: Request instance for DescribeBaselineHostTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineHostTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineHostTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemDetectList(self, request):
        """This API is used to obtain the list of baseline detection items.

        :param request: Request instance for DescribeBaselineItemDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemList(self, request):
        """This API is used to obtain the list of check results on baseline check items.

        :param request: Request instance for DescribeBaselineItemList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineList(self, request):
        """This API is used to query the information of the baseline list.

        :param request: Request instance for DescribeBaselineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselinePolicyList(self, request):
        """This API is used to obtain the list of baseline policies.

        :param request: Request instance for DescribeBaselinePolicyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselinePolicyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselinePolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselinePolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinePolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRule(self, request):
        """This API is used to query the information on corresponding check items based on baseline ID.

        :param request: Request instance for DescribeBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineScanSchedule(self, request):
        """This API is used to query the baseline detection progress by task ID.

        :param request: Request instance for DescribeBaselineScanSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineScanScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineScanScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineScanSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineScanScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineStrategyDetail(self, request):
        """This API is used to query policy details by baseline policy ID.

        :param request: Request instance for DescribeBaselineStrategyDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineStrategyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineStrategyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineStrategyList(self, request):
        """This API is used to query the information of baseline policies under the same user.

        :param request: Request instance for DescribeBaselineStrategyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineStrategyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineStrategyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineTop(self, request):
        """This API is used to query TOP baseline detection items based on policy IDs.

        :param request: Request instance for DescribeBaselineTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineWeakPasswordList(self, request):
        """This API is used to obtain the list of baseline weak passwords.

        :param request: Request instance for DescribeBaselineWeakPasswordList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineWeakPasswordListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineWeakPasswordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineWeakPasswordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineWeakPasswordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEvents(self, request):
        """This API is used to obtain the high-risk command list.

        :param request: Request instance for DescribeBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEventsInfo(self, request):
        """This API is used to query high-risk command event details.

        :param request: Request instance for DescribeBashEventsInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEventsInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEventsInfoNew(self, request):
        """This API is used to query high-risk command event details (new).

        :param request: Request instance for DescribeBashEventsInfoNew.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsInfoNewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsInfoNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEventsInfoNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsInfoNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEventsNew(self, request):
        """This API is used to obtain the list of high-risk commands (new).

        :param request: Request instance for DescribeBashEventsNew.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsNewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEventsNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashPolicies(self, request):
        """This API is used to obtain the list of high-risk command policies.

        :param request: Request instance for DescribeBashPolicies.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashPoliciesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashRules(self, request):
        """This API is used to obtain the list of high-risk command rules.

        :param request: Request instance for DescribeBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBruteAttackList(self, request):
        """This API is used to obtain the list of password cracking.

        :param request: Request instance for DescribeBruteAttackList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBruteAttackList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBruteAttackListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBruteAttackRules(self, request):
        """This API is used to obtain brute force cracking rules.

        :param request: Request instance for DescribeBruteAttackRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBruteAttackRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBruteAttackRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCanFixVulMachine(self, request):
        """This API is used to query the fixable host information.

        :param request: Request instance for DescribeCanFixVulMachine.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeCanFixVulMachineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeCanFixVulMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCanFixVulMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCanFixVulMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCanNotSeparateMachine(self, request):
        """This API is used to obtain hosts where Trojans cannot be isolated.

        :param request: Request instance for DescribeCanNotSeparateMachine.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeCanNotSeparateMachineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeCanNotSeparateMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCanNotSeparateMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCanNotSeparateMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientException(self, request):
        """This API is used to obtain client exception events.

        :param request: Request instance for DescribeClientException.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeClientExceptionRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeClientExceptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientException", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientExceptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudProtectServiceOrderList(self, request):
        """云护航计费产品已下线

        This API is used to query the list of cloud escort service orders.

        :param request: Request instance for DescribeCloudProtectServiceOrderList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeCloudProtectServiceOrderListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeCloudProtectServiceOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudProtectServiceOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudProtectServiceOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComponentStatistics(self, request):
        """This API is used to obtain the data of the component statistics list.

        :param request: Request instance for DescribeComponentStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeComponentStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeComponentStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComponentStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComponentStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefenceEventDetail(self, request):
        """This API is used to obtain vulnerability defense event details.

        :param request: Request instance for DescribeDefenceEventDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeDefenceEventDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeDefenceEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefenceEventDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefenceEventDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDirectConnectInstallCommand(self, request):
        """This API is used to obtain DC agent installation command, including the token.

        :param request: Request instance for DescribeDirectConnectInstallCommand.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeDirectConnectInstallCommandRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeDirectConnectInstallCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDirectConnectInstallCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDirectConnectInstallCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeESAggregations(self, request):
        """This API is used to obtain the aggregation result of the ES field.

        :param request: Request instance for DescribeESAggregations.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeESAggregationsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeESAggregationsResponse`

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


    def DescribeEmergencyResponseList(self, request):
        """This API is used to obtain the emergency response list.

        :param request: Request instance for DescribeEmergencyResponseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyResponseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyResponseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmergencyResponseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmergencyResponseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmergencyVulList(self, request):
        """This API is used to obtain the list of emergency vulnerabilities.

        :param request: Request instance for DescribeEmergencyVulList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyVulListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyVulListResponse`

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


    def DescribeEventByTable(self, request):
        """This API is used to query alarm event details based on event table names and IDs.

        :param request: Request instance for DescribeEventByTable.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeEventByTableRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeEventByTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventByTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventByTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExpertServiceList(self, request):
        """This API is used to obtain the security manager list.

        :param request: Request instance for DescribeExpertServiceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExpertServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExpertServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExpertServiceOrderList(self, request):
        """This API is used to obtain the expert service order list.

        :param request: Request instance for DescribeExpertServiceOrderList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceOrderListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExpertServiceOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExpertServiceOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportMachines(self, request):
        """This API is used to export the list of hosts in a specific region.

        :param request: Request instance for DescribeExportMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExportMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExportMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFastAnalysis(self, request):
        """This API is used to quickly analyze and count logs.

        :param request: Request instance for DescribeFastAnalysis.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFastAnalysisRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFastAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFastAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFastAnalysisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperEventRuleInfo(self, request):
        """This API is used to view the rule details API when an event occurs.

        :param request: Request instance for DescribeFileTamperEventRuleInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperEventRuleInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperEventRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperEventRuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperEventRuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperEvents(self, request):
        """This API is used to obtain the list of core file monitoring events.

        :param request: Request instance for DescribeFileTamperEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperRuleCount(self, request):
        """This API is used to query the number of rules for monitoring files associated with a host.

        :param request: Request instance for DescribeFileTamperRuleCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRuleCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRuleCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperRuleCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperRuleCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperRuleInfo(self, request):
        """This API is used to query details of a monitoring rule.

        :param request: Request instance for DescribeFileTamperRuleInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRuleInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperRuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperRuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperRules(self, request):
        """This API is used to obtain the list of core file monitoring rules.

        :param request: Request instance for DescribeFileTamperRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralStat(self, request):
        """This API is used to obtain the statistics data of hosts.

        :param request: Request instance for DescribeGeneralStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeGeneralStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeGeneralStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHistoryAccounts(self, request):
        """This API is used to obtain the data of the account change history list.

        :param request: Request instance for DescribeHistoryAccounts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryAccountsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistoryAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistoryAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHistoryService(self, request):
        """This API is used to query the log retrieval service information.

        :param request: Request instance for DescribeHistoryService.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryServiceRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistoryService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistoryServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostInfo(self, request):
        """This API is used to query the host and tag information.

        :param request: Request instance for DescribeHostInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHostInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHostInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostLoginList(self, request):
        """This API is used to retrieve the log-in audit list.

        :param request: Request instance for DescribeHostLoginList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHostLoginListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHostLoginListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostLoginList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostLoginListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHotVulTop(self, request):
        """This API is used to obtain hot spot vulnerabilities across the entire network.

        :param request: Request instance for DescribeHotVulTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHotVulTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHotVulTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHotVulTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHotVulTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIgnoreBaselineRule(self, request):
        """This API is used to query the information of ignored inspection items.

        :param request: Request instance for DescribeIgnoreBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIgnoreBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIgnoreBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIgnoreHostAndItemConfig(self, request):
        """This API is used to obtain the information of affected inspection items and hosts ignored with one click.

        :param request: Request instance for DescribeIgnoreHostAndItemConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreHostAndItemConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreHostAndItemConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIgnoreHostAndItemConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIgnoreHostAndItemConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIgnoreRuleEffectHostList(self, request):
        """This API is used to query the information on the list of hosts affected by ignored detection items based on detection item IDs and filter criteria.

        :param request: Request instance for DescribeIgnoreRuleEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreRuleEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreRuleEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIgnoreRuleEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIgnoreRuleEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexList(self, request):
        """This API is used to obtain the index list.

        :param request: Request instance for DescribeIndexList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIndexListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIndexListResponse`

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


    def DescribeJavaMemShellInfo(self, request):
        """This API is used to query Java webshell event details.

        :param request: Request instance for DescribeJavaMemShellInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJavaMemShellInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJavaMemShellInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJavaMemShellList(self, request):
        """This API is used to query the list of Java webshell events.

        :param request: Request instance for DescribeJavaMemShellList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJavaMemShellList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJavaMemShellListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJavaMemShellPluginInfo(self, request):
        """This API is used to query the Java webshell plugin information of the given host.

        :param request: Request instance for DescribeJavaMemShellPluginInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellPluginInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellPluginInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJavaMemShellPluginInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJavaMemShellPluginInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJavaMemShellPluginList(self, request):
        """This API is used to query the Java webshell plugin list.

        :param request: Request instance for DescribeJavaMemShellPluginList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellPluginListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellPluginListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJavaMemShellPluginList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJavaMemShellPluginListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicense(self, request):
        """This API is used to query the authorization information.

        :param request: Request instance for DescribeLicense.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicense", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseBindList(self, request):
        """This API is used to obtain the list of authorized machines bound to an authorization under the Settings Center-Authorization Management.

        :param request: Request instance for DescribeLicenseBindList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseBindList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseBindListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseBindSchedule(self, request):
        """This API is used to query the binding task progress of the authorization.

        :param request: Request instance for DescribeLicenseBindSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseBindSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseBindScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseGeneral(self, request):
        """This API is used to obtain the authorization overview information.

        :param request: Request instance for DescribeLicenseGeneral.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseGeneralRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseGeneralResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseGeneral", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseGeneralResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseList(self, request):
        """This API is used to obtain all authorization orders of a user.

        :param request: Request instance for DescribeLicenseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseWhiteConfig(self, request):
        """This API is used to query the available configurations for authorization allowlists.

        :param request: Request instance for DescribeLicenseWhiteConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseWhiteConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseWhiteConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseWhiteConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseWhiteConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogDeliveryKafkaOptions(self, request):
        """This API is used to query the list of logs available for shipping to Kafka.

        :param request: Request instance for DescribeLogDeliveryKafkaOptions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogDeliveryKafkaOptionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogDeliveryKafkaOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogDeliveryKafkaOptions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogDeliveryKafkaOptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogExports(self, request):
        """This API is used to obtain the list of log download tasks.

        :param request: Request instance for DescribeLogExports.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogExportsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogExportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogExports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogExportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogHistogram(self, request):
        """This API is used to obtain the log histogram information.

        :param request: Request instance for DescribeLogHistogram.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogHistogramRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogHistogramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogHistogram", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogHistogramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogIndex(self, request):
        """This API is used to query the index.

        :param request: Request instance for DescribeLogIndex.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogIndexRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogKafkaDeliverInfo(self, request):
        """This API is used to obtain the information of Kafka shipping.

        :param request: Request instance for DescribeLogKafkaDeliverInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogKafkaDeliverInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogKafkaDeliverInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogKafkaDeliverInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogKafkaDeliverInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogStorageConfig(self, request):
        """This API is used to obtain the log storage configuration.

        :param request: Request instance for DescribeLogStorageConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogStorageConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogStorageConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogStorageRecord(self, request):
        """This API is used to obtain the record of stored log size.

        :param request: Request instance for DescribeLogStorageRecord.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageRecordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogStorageRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogStorageRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogStorageStatistic(self, request):
        """This API is used to obtain the statistics of the used log retrieval capacity.

        :param request: Request instance for DescribeLogStorageStatistic.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageStatisticRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageStatisticResponse`

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


    def DescribeLogType(self, request):
        """This API is used to obtain log types, and the returned result of this API indicates temporarily filterable log types.

        :param request: Request instance for DescribeLogType.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogTypeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteCombinedList(self, request):
        """This API is used to obtain the list of cross-region log-in allowlists after merge.

        :param request: Request instance for DescribeLoginWhiteCombinedList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteCombinedListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteCombinedListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteCombinedList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteCombinedListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteHostList(self, request):
        """This API is used to query the list of allowlisted machines after merge.

        :param request: Request instance for DescribeLoginWhiteHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteList(self, request):
        """This API is used to obtain the cross-region log-in allowlist list.

        :param request: Request instance for DescribeLoginWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineClearHistory(self, request):
        """This API is used to query the clearing history records of a machine.

        :param request: Request instance for DescribeMachineClearHistory.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineClearHistoryRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineClearHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineClearHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineClearHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineDefenseCnt(self, request):
        """This API is used to query the statistics of advanced defense events for hosts.

        :param request: Request instance for DescribeMachineDefenseCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineDefenseCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineDefenseCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineDefenseCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineDefenseCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineFileTamperRules(self, request):
        """This API is used to query the list of host-related core file monitoring rules.

        :param request: Request instance for DescribeMachineFileTamperRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineFileTamperRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineFileTamperRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineFileTamperRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineFileTamperRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineGeneral(self, request):
        """This API is used to query the information of the host overview.

        :param request: Request instance for DescribeMachineGeneral.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineGeneralRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineGeneralResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineGeneral", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineGeneralResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineLicenseDetail(self, request):
        """This API is used to query the machine authorization information.

        :param request: Request instance for DescribeMachineLicenseDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineLicenseDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineLicenseDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineLicenseDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineLicenseDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineOsList(self, request):
        """This API is used to query the machine operating system list.

        :param request: Request instance for DescribeMachineOsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineOsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineOsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineOsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineOsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineRegionList(self, request):
        """This API is used to query the list of host regions.

        :param request: Request instance for DescribeMachineRegionList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineRegionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineRegionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineRegions(self, request):
        """This API is used to obtain the list of machine regions.

        :param request: Request instance for DescribeMachineRegions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineRiskCnt(self, request):
        """This API is used to query the statistics of host intrusion detection events.

        :param request: Request instance for DescribeMachineRiskCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRiskCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRiskCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineRiskCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineRiskCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineSnapshot(self, request):
        """This API is used to query snapshots created by the host.

        :param request: Request instance for DescribeMachineSnapshot.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineSnapshotRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachines(self, request):
        """This API is used to obtain the list of hosts in a specific region.

        :param request: Request instance for DescribeMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachinesSimple(self, request):
        """This API is used to obtain the list of hosts.

        :param request: Request instance for DescribeMachinesSimple.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesSimpleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesSimpleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachinesSimple", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachinesSimpleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalWareList(self, request):
        """This API is used to obtain the Trojan list.

        :param request: Request instance for DescribeMalWareList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalWareListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalWareListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalWareList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalWareListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMaliciousRequestWhiteList(self, request):
        """This API is used to query the list of malicious request allowlists.

        :param request: Request instance for DescribeMaliciousRequestWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMaliciousRequestWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMaliciousRequestWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaliciousRequestWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaliciousRequestWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareFile(self, request):
        """This API is used to obtain Trojan file download addresses.

        :param request: Request instance for DescribeMalwareFile.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareFileRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareInfo(self, request):
        """This API is used to view malicious file details.

        :param request: Request instance for DescribeMalwareInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareRiskOverview(self, request):
        """This API is used to obtain the information of virus scanning overview.

        :param request: Request instance for DescribeMalwareRiskOverview.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareRiskOverviewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareRiskOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareRiskOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareRiskOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareRiskWarning(self, request):
        """This API is used to open Intrusion Detection - Virus Scanning, and the risk warning content pops up.

        :param request: Request instance for DescribeMalwareRiskWarning.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareRiskWarningRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareRiskWarningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareRiskWarning", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareRiskWarningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareTimingScanSetting(self, request):
        """This API is used to query the scheduled scan configuration.

        :param request: Request instance for DescribeMalwareTimingScanSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareTimingScanSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareTimingScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareTimingScanSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareTimingScanSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareWhiteList(self, request):
        """This API is used to obtain the list of Trojan allowlists.

        :param request: Request instance for DescribeMalwareWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareWhiteListAffectList(self, request):
        """This API is used to obtain the list of affected Trojan allowlists.

        :param request: Request instance for DescribeMalwareWhiteListAffectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareWhiteListAffectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareWhiteListAffectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareWhiteListAffectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareWhiteListAffectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMonthInspectionReport(self, request):
        """This API is used to download the monthly inspection report of the security manager.

        :param request: Request instance for DescribeMonthInspectionReport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMonthInspectionReportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMonthInspectionReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonthInspectionReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonthInspectionReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetAttackSetting(self, request):
        """This API is used to query network attack settings.

        :param request: Request instance for DescribeNetAttackSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeNetAttackSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeNetAttackSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetAttackSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetAttackSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetAttackWhiteList(self, request):
        """This API is used to obtain the network attack allowlist list.

        :param request: Request instance for DescribeNetAttackWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeNetAttackWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeNetAttackWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetAttackWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetAttackWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpenPortStatistics(self, request):
        """This API is used to obtain the list of port statistics.

        :param request: Request instance for DescribeOpenPortStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeOpenPortStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeOpenPortStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpenPortStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpenPortStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewStatistics(self, request):
        """This API is used to obtain the overview statistics.

        :param request: Request instance for DescribeOverviewStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeOverviewStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeOverviewStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivilegeEventInfo(self, request):
        """This API is used to obtain local privilege escalation information details.

        :param request: Request instance for DescribePrivilegeEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivilegeEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivilegeEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivilegeRules(self, request):
        """This API is used to obtain the list of local privilege escalation rules.

        :param request: Request instance for DescribePrivilegeRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivilegeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivilegeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProVersionInfo(self, request):
        """This API is used to obtain the overview information of the Professional edition.

        :param request: Request instance for DescribeProVersionInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionInfoResponse`

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


    def DescribeProVersionStatus(self, request):
        """This API is used to check whether a single host or all hosts enable the professional version.

        :param request: Request instance for DescribeProVersionStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProVersionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProVersionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcessStatistics(self, request):
        """This API is used to obtain the process statistics data.

        :param request: Request instance for DescribeProcessStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProcessStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProcessStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductStatus(self, request):
        """This API is used to query the product trial status.

        :param request: Request instance for DescribeProductStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProductStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProductStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicProxyInstallCommand(self, request):
        """This API is used to obtain the installation command of the public network access proxy.

        :param request: Request instance for DescribePublicProxyInstallCommand.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePublicProxyInstallCommandRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePublicProxyInstallCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicProxyInstallCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicProxyInstallCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseBackupList(self, request):
        """This API is used to query the list of host snapshot backups.

        :param request: Request instance for DescribeRansomDefenseBackupList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseBackupListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseBackupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseBackupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseBackupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseEventsList(self, request):
        """This API is used to query the anti-ransomware event list.

        :param request: Request instance for DescribeRansomDefenseEventsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseEventsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseEventsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseEventsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseEventsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseMachineList(self, request):
        """This API is used to query the list of backup details.

        :param request: Request instance for DescribeRansomDefenseMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseMachineStrategyInfo(self, request):
        """This API is used to obtain the list of policies bound to a host.

        :param request: Request instance for DescribeRansomDefenseMachineStrategyInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseMachineStrategyInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseMachineStrategyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseMachineStrategyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseMachineStrategyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseRollBackTaskList(self, request):
        """This API is used to query the rollback task list.

        :param request: Request instance for DescribeRansomDefenseRollBackTaskList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseRollBackTaskListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseRollBackTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseRollBackTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseRollBackTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseState(self, request):
        """This API is used to obtain user anti-ransomware trends.

        :param request: Request instance for DescribeRansomDefenseState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseStrategyDetail(self, request):
        """This API is used to obtain the policy details.

        :param request: Request instance for DescribeRansomDefenseStrategyDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseStrategyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseStrategyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseStrategyList(self, request):
        """This API is used to query the list of anti-ransomware policies.

        :param request: Request instance for DescribeRansomDefenseStrategyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseStrategyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseStrategyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseStrategyMachines(self, request):
        """This API is used to query the list of machines bound to an anti-ransomware policy.

        :param request: Request instance for DescribeRansomDefenseStrategyMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseStrategyMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseStrategyMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseTrend(self, request):
        """This API is used to obtain the ransomware situation across the entire network.

        :param request: Request instance for DescribeRansomDefenseTrend.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseTrendRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecommendedProtectCpu(self, request):
        """This API is used to query the recommended number of protection cores for purchase.

        :param request: Request instance for DescribeRecommendedProtectCpu.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRecommendedProtectCpuRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRecommendedProtectCpuResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecommendedProtectCpu", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecommendedProtectCpuResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellEventInfo(self, request):
        """This API is used to query reverse shell details.

        :param request: Request instance for DescribeReverseShellEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellEvents(self, request):
        """This API is used to obtain the list of Reverse Shell.

        :param request: Request instance for DescribeReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventsResponse`

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


    def DescribeReverseShellRules(self, request):
        """This API is used to obtain the list of Reverse Shell rules.

        :param request: Request instance for DescribeReverseShellRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskBatchStatus(self, request):
        """This API is used to query if the intrusion detection event update task is completed.

        :param request: Request instance for DescribeRiskBatchStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskBatchStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskBatchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskBatchStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskBatchStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsEventInfo(self, request):
        """This API is used to query malicious request event details.

        :param request: Request instance for DescribeRiskDnsEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsEventList(self, request):
        """This API is used to obtain the list of malicious request events.

        :param request: Request instance for DescribeRiskDnsEventList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsInfo(self, request):
        """This API is used to query malicious request details.

        :param request: Request instance for DescribeRiskDnsInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsList(self, request):
        """This API is used to obtain the malicious request list.

        :param request: Request instance for DescribeRiskDnsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsPolicyList(self, request):
        """This API is used to obtain the list of malicious request policies.

        :param request: Request instance for DescribeRiskDnsPolicyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsPolicyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskProcessEvents(self, request):
        """This API is used to obtain the list of abnormal processes.

        :param request: Request instance for DescribeRiskProcessEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskProcessEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskProcessEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskProcessEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskProcessEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSafeInfo(self, request):
        """This API is used to query the .security notification information.

        :param request: Request instance for DescribeSafeInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSafeInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSafeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSafeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSafeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanMalwareSchedule(self, request):
        """This API is used to query the Trojan scan progress.

        :param request: Request instance for DescribeScanMalwareSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanMalwareScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanMalwareScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanMalwareSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanMalwareScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanSchedule(self, request):
        """This API is used to query the detection progress by taskid.

        :param request: Request instance for DescribeScanSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanState(self, request):
        """This API is used to query the status of recent scan tasks of the corresponding module.

        :param request: Request instance for DescribeScanState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanTaskDetails(self, request):
        """This API is used to query the scan task details and scan progress information/exceptions.

        :param request: Request instance for DescribeScanTaskDetails.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskDetailsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanTaskStatus(self, request):
        """This API is used to query the list of machine scan statuses for filtering.

        :param request: Request instance for DescribeScanTaskStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanVulSetting(self, request):
        """This API is used to query the configuration for regular detection.

        :param request: Request instance for DescribeScanVulSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanVulSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanVulSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanVulSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanVulSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenAttackHotspot(self, request):
        """This API is used to visually obtain the attacked hot spots across the entire network on the large screen.

        :param request: Request instance for DescribeScreenAttackHotspot.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenAttackHotspotRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenAttackHotspotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenAttackHotspot", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenAttackHotspotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenBroadcasts(self, request):
        """This API is used to obtain the security report on the large screen.

        :param request: Request instance for DescribeScreenBroadcasts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenBroadcastsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenBroadcastsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenBroadcasts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenBroadcastsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenDefenseTrends(self, request):
        """This API is used to obtain the visualized attack and defense trends on the large screen.

        :param request: Request instance for DescribeScreenDefenseTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenDefenseTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenDefenseTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenDefenseTrends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenDefenseTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenEmergentMsg(self, request):
        """This API is used to obtain the visualized emergency notification on the large screen.

        :param request: Request instance for DescribeScreenEmergentMsg.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenEmergentMsgRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenEmergentMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenEmergentMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenEmergentMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenEventsCnt(self, request):
        """This API is used to obtain the statistics data of events on the security overview page.

        :param request: Request instance for DescribeScreenEventsCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenEventsCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenEventsCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenEventsCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenEventsCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenGeneralStat(self, request):
        """This API is used to obtain the visualized statistics data of hosts on the screen.

        :param request: Request instance for DescribeScreenGeneralStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenGeneralStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenGeneralStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenGeneralStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenGeneralStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenHostInvasion(self, request):
        """This API is used to obtain the visualized host intrusion details on the large screen.

        :param request: Request instance for DescribeScreenHostInvasion.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenHostInvasionRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenHostInvasionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenHostInvasion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenHostInvasionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenMachineRegions(self, request):
        """This API is used to obtain the list of available visualized host regions on the large screen.

        :param request: Request instance for DescribeScreenMachineRegions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenMachineRegionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenMachineRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenMachineRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenMachineRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenMachines(self, request):
        """This API is used to obtain the visualized list of host regions on the large screen.

        :param request: Request instance for DescribeScreenMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenProtectionCnt(self, request):
        """This API is used to obtain the visualized introduction of CWPP engine on the large screen.

        :param request: Request instance for DescribeScreenProtectionCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenProtectionCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenProtectionCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenProtectionCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenProtectionCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenProtectionStat(self, request):
        """This API is used to obtain the security protection status on the large screen.

        :param request: Request instance for DescribeScreenProtectionStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenProtectionStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenProtectionStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenProtectionStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenProtectionStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenRiskAssetsTop(self, request):
        """This API is used to count today's risky assets.

        :param request: Request instance for DescribeScreenRiskAssetsTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenRiskAssetsTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenRiskAssetsTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenRiskAssetsTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenRiskAssetsTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchLogs(self, request):
        """This API is used to obtain historical search records.

        :param request: Request instance for DescribeSearchLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchLogsResponse`

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
        """This API is used to obtain the list of quick retrievals.

        :param request: Request instance for DescribeSearchTemplates.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchTemplatesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchTemplatesResponse`

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


    def DescribeSecurityBroadcastInfo(self, request):
        """This API is used to query the information of security report articles.

        :param request: Request instance for DescribeSecurityBroadcastInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityBroadcastInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityBroadcastInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityBroadcastInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityBroadcastInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityBroadcasts(self, request):
        """This API is used to obtain the security report list page.

        :param request: Request instance for DescribeSecurityBroadcasts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityBroadcastsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityBroadcastsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityBroadcasts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityBroadcastsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityDynamics(self, request):
        """This API is used to obtain the dynamic message data of security events.

        :param request: Request instance for DescribeSecurityDynamics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityDynamicsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityDynamicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityDynamics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityDynamicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityEventStat(self, request):
        """This API is used to obtain the statistics of security events.

        :param request: Request instance for DescribeSecurityEventStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityEventStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityEventStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityEventsCnt(self, request):
        """This API is used to obtain the statistics data of security overview-related events.

        :param request: Request instance for DescribeSecurityEventsCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventsCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventsCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityEventsCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityEventsCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityProtectionStat(self, request):
        """This API is used to obtain the summary of security protection statuses.

        :param request: Request instance for DescribeSecurityProtectionStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityProtectionStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityProtectionStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityProtectionStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityProtectionStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityTrends(self, request):
        """This API is used to obtain the security event statistics data.

        :param request: Request instance for DescribeSecurityTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityTrends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServersAndRiskAndFirstInfo(self, request):
        """This API is used to obtain the number of risky files pending to be processed + the number of affected servers + whether to try to detect + last detection time.

        :param request: Request instance for DescribeServersAndRiskAndFirstInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeServersAndRiskAndFirstInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeServersAndRiskAndFirstInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServersAndRiskAndFirstInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServersAndRiskAndFirstInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStrategyExist(self, request):
        """This API is used to query whether a policy exists by policy name.

        :param request: Request instance for DescribeStrategyExist.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeStrategyExistRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeStrategyExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStrategyExist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStrategyExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagMachines(self, request):
        """This API is used to obtain the server information associated with the specified tag.

        :param request: Request instance for DescribeTagMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeTagMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeTagMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTags(self, request):
        """This API is used to obtain all host tags.

        :param request: Request instance for DescribeTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrialReport(self, request):
        """This API is used to query the CWPP authorized trial report (only available for console applications).

        :param request: Request instance for DescribeTrialReport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeTrialReportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeTrialReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrialReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrialReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUndoVulCounts(self, request):
        """This API is used to obtain the number of pending vulnerabilities of a specified category and the number of hosts in the vulnerability management module.

        :param request: Request instance for DescribeUndoVulCounts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeUndoVulCountsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeUndoVulCountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUndoVulCounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUndoVulCountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsersConfig(self, request):
        """This API is used to query the user's custom configurations.

        :param request: Request instance for DescribeUsersConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeUsersConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeUsersConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsersConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsersConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsualLoginPlaces(self, request):
        """This API is used to query common log-in locations.

        :param request: Request instance for DescribeUsualLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsualLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsualLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVdbAndPocInfo(self, request):
        """This API is used to obtain virus database and POC updates.

        :param request: Request instance for DescribeVdbAndPocInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVdbAndPocInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVdbAndPocInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVdbAndPocInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVdbAndPocInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVersionCompareChart(self, request):
        """This API is used to obtain the version comparison information.

        :param request: Request instance for DescribeVersionCompareChart.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVersionCompareChartRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVersionCompareChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVersionCompareChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVersionCompareChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVersionStatistics(self, request):
        """This API is used to count the number of machines of Professional and Basic editions.

        :param request: Request instance for DescribeVersionStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVersionStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVersionStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVersionStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVersionStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVertexDetail(self, request):
        """This API is used to obtain the attribute information of the specified point.

        :param request: Request instance for DescribeVertexDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVertexDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVertexDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVertexDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVertexDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulCountByDates(self, request):
        """This API is used to obtain the number of vulnerabilities of specified types in recent days and the number of hosts.

        :param request: Request instance for DescribeVulCountByDates.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCountByDatesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCountByDatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulCountByDates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulCountByDatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulCveIdInfo(self, request):
        """This API is used to query vulnerability details by CveId.

        :param request: Request instance for DescribeVulCveIdInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCveIdInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCveIdInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulCveIdInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulCveIdInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceEvent(self, request):
        """This API is used to obtain the list of vulnerability defense events.

        :param request: Request instance for DescribeVulDefenceEvent.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceEventRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceEventResponse`

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


    def DescribeVulDefenceList(self, request):
        """This API is used to query the vulnerability defense list.

        :param request: Request instance for DescribeVulDefenceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceOverview(self, request):
        """This API is used to obtain the vulnerability defense overview information, including event trend and plugin enabling status.

        :param request: Request instance for DescribeVulDefenceOverview.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceOverviewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefencePluginDetail(self, request):
        """This API is used to obtain the vulnerability defense plugin information on a single host.

        :param request: Request instance for DescribeVulDefencePluginDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefencePluginDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefencePluginDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefencePluginExceptionCount(self, request):
        """This API is used to obtain the current number of abnormal plugins.

        :param request: Request instance for DescribeVulDefencePluginExceptionCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginExceptionCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginExceptionCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefencePluginExceptionCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefencePluginExceptionCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefencePluginStatus(self, request):
        """This API is used to obtain the vulnerability defense plugin status of each host.

        :param request: Request instance for DescribeVulDefencePluginStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefencePluginStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefencePluginStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceSetting(self, request):
        """This API is used to obtain the current vulnerability defense plugin settings.

        :param request: Request instance for DescribeVulDefenceSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceSettingResponse`

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


    def DescribeVulEffectHostList(self, request):
        """This API is used to obtain the list of hosts affected by vulnerabilities.

        :param request: Request instance for DescribeVulEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulEffectModules(self, request):
        """This API is used to obtain the list of components affected by vulnerabilities.

        :param request: Request instance for DescribeVulEffectModules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEffectModulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEffectModulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulEffectModules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulEffectModulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulEmergentMsg(self, request):
        """This API is used to obtain vulnerability emergency notifications.

        :param request: Request instance for DescribeVulEmergentMsg.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEmergentMsgRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEmergentMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulEmergentMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulEmergentMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixStatus(self, request):
        """This API is used to check the host vulnerability fixing progress.

        :param request: Request instance for DescribeVulFixStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulFixStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulFixStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulHostCountScanTime(self, request):
        """This API is used to obtain the number of vulnerabilities pending to be processed and affected hosts.

        :param request: Request instance for DescribeVulHostCountScanTime.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostCountScanTimeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostCountScanTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulHostCountScanTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulHostCountScanTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulHostTop(self, request):
        """This API is used to obtain the list of top server risks.

        :param request: Request instance for DescribeVulHostTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulHostTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulHostTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulInfoCvss(self, request):
        """This API is used to obtain vulnerability details with the CVSS version.

        :param request: Request instance for DescribeVulInfoCvss.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulInfoCvssRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulInfoCvssResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulInfoCvss", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulInfoCvssResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulLabels(self, request):
        """This API is used to obtain the list of all user vulnerability tags.

        :param request: Request instance for DescribeVulLabels.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulLabelsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulLabelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLabels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulLabelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulLevelCount(self, request):
        """This API is used to obtain the statistics of vulnerability quantity and level distribution.

        :param request: Request instance for DescribeVulLevelCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulLevelCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulLevelCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLevelCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulLevelCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulList(self, request):
        """This API is used to obtain the data of the vulnerability list.

        :param request: Request instance for DescribeVulList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulOverview(self, request):
        """This API is used to obtain the data for the vulnerability overview.

        :param request: Request instance for DescribeVulOverview.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulOverviewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulStoreList(self, request):
        """This API is used to obtain the vulnerability database list.

        :param request: Request instance for DescribeVulStoreList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulStoreListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulStoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulStoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulStoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulTop(self, request):
        """This API is used to count top vulnerabilities.

        :param request: Request instance for DescribeVulTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulTrend(self, request):
        """This API is used to obtain information of the vulnerability situation.

        :param request: Request instance for DescribeVulTrend.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulTrendRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWarningHostConfig(self, request):
        """This API is used to query the alarming machine scope settings.

        :param request: Request instance for DescribeWarningHostConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWarningHostConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWarningHostConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarningHostConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWarningHostConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWarningList(self, request):
        """This API is used to obtain the list of the current user's alarms.

        :param request: Request instance for DescribeWarningList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWarningListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWarningListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarningList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWarningListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebHookPolicy(self, request):
        """This API is used to query alarm policies.

        :param request: Request instance for DescribeWebHookPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebHookPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebHookPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebHookReceiver(self, request):
        """This API is used to query the list of alarm recipients.

        :param request: Request instance for DescribeWebHookReceiver.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookReceiverRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebHookReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebHookReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebHookReceiverUsage(self, request):
        """This API is used to query the usage of policies associated with the specified alarm recipient.

        :param request: Request instance for DescribeWebHookReceiverUsage.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookReceiverUsageRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookReceiverUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebHookReceiverUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebHookReceiverUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebHookRule(self, request):
        """This API is used to obtain the details of the WeCom chatbot rules.

        :param request: Request instance for DescribeWebHookRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebHookRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebHookRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebHookRules(self, request):
        """This API is used to obtain the list of WeCom chatbot rules.

        :param request: Request instance for DescribeWebHookRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebHookRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebHookRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyOrder(self, request):
        """This API is used to terminate resources.

        :param request: Request instance for DestroyOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DestroyOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DestroyOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyOrder", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditBashRules(self, request):
        """This API is used to add or modify high-risk command rules.

        :param request: Request instance for EditBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.EditBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditPrivilegeRules(self, request):
        """This API is used to add or modify local privilege escalation rules (multiple servers supported).

        :param request: Request instance for EditPrivilegeRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditPrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditPrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditPrivilegeRules", params, headers=headers)
            response = json.loads(body)
            model = models.EditPrivilegeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditReverseShellRules(self, request):
        """This API is used to edit reverse shell rules (multiple servers supported).

        :param request: Request instance for EditReverseShellRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditReverseShellRules", params, headers=headers)
            response = json.loads(body)
            model = models.EditReverseShellRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditTags(self, request):
        """This API is used to add or edit tags.

        :param request: Request instance for EditTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditTags", params, headers=headers)
            response = json.loads(body)
            model = models.EditTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetAppList(self, request):
        """This API is used to export the list of asset management applications.

        :param request: Request instance for ExportAssetAppList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetAppListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetAppList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetCoreModuleList(self, request):
        """This API is used to export the list of asset management kernel modules.

        :param request: Request instance for ExportAssetCoreModuleList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetCoreModuleListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetCoreModuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetCoreModuleList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetCoreModuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetDatabaseList(self, request):
        """This API is used to export the list of asset management databases.

        :param request: Request instance for ExportAssetDatabaseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetDatabaseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetDatabaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetDatabaseList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetDatabaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetEnvList(self, request):
        """This API is used to export the list of asset management environment variables.

        :param request: Request instance for ExportAssetEnvList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetEnvListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetEnvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetEnvList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetEnvListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetInitServiceList(self, request):
        """This API is used to export the list of asset management startup services.

        :param request: Request instance for ExportAssetInitServiceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetInitServiceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetInitServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetInitServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetInitServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetJarList(self, request):
        """This API is used to export the list of Jar packages.

        :param request: Request instance for ExportAssetJarList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetJarListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetJarListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetJarList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetJarListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetMachineDetail(self, request):
        """This API is used to export asset management host resource details.

        :param request: Request instance for ExportAssetMachineDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetMachineDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetMachineDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetMachineDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetMachineDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetMachineList(self, request):
        """This API is used to export the list of resource monitoring.

        :param request: Request instance for ExportAssetMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetPlanTaskList(self, request):
        """This API is used to export the list of scheduled asset management tasks.

        :param request: Request instance for ExportAssetPlanTaskList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetPlanTaskListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetPlanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetPlanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetPlanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetPortInfoList(self, request):
        """This API is used to export the list of asset management ports.

        :param request: Request instance for ExportAssetPortInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetPortInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetPortInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetPortInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetPortInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetProcessInfoList(self, request):
        """This API is used to export the asset management process list.

        :param request: Request instance for ExportAssetProcessInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetProcessInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetProcessInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetProcessInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetProcessInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetRecentMachineInfo(self, request):
        """This API is used to export host trends of recent days (up to last 90 days).

        :param request: Request instance for ExportAssetRecentMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetRecentMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetRecentMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetRecentMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetRecentMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetSystemPackageList(self, request):
        """This API is used to export the list of system installation packages for asset management.

        :param request: Request instance for ExportAssetSystemPackageList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetSystemPackageListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetSystemPackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetSystemPackageList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetSystemPackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetUserList(self, request):
        """This API is used to export the account list.

        :param request: Request instance for ExportAssetUserList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetUserListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetUserList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetWebAppList(self, request):
        """This API is used to export the list of asset management Web applications.

        :param request: Request instance for ExportAssetWebAppList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebAppListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetWebAppList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetWebAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetWebFrameList(self, request):
        """This API is used to export the list of asset management Web frameworks.

        :param request: Request instance for ExportAssetWebFrameList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebFrameListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebFrameListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetWebFrameList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetWebFrameListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetWebLocationList(self, request):
        """This API is used to export the list of Web sites.

        :param request: Request instance for ExportAssetWebLocationList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebLocationListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebLocationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetWebLocationList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetWebLocationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetWebServiceInfoList(self, request):
        """This API is used to export the list of asset management Web services.

        :param request: Request instance for ExportAssetWebServiceInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebServiceInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebServiceInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetWebServiceInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetWebServiceInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAttackEvents(self, request):
        """This API is used to export network attack events.

        :param request: Request instance for ExportAttackEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAttackEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAttackEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAttackEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAttackEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineEffectHostList(self, request):
        """This API is used to export the list of hosts affected by baseline.

        :param request: Request instance for ExportBaselineEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineFixList(self, request):
        """This API is used to export the list of fixing baselines.

        :param request: Request instance for ExportBaselineFixList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineFixListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineFixListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineFixList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineFixListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineHostDetectList(self, request):
        """This API is used to export the baseline for host detection.

        :param request: Request instance for ExportBaselineHostDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineHostDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineHostDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineHostDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineHostDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineItemDetectList(self, request):
        """This API is used to export baseline check items.

        :param request: Request instance for ExportBaselineItemDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineItemDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineItemDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineItemDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineItemDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineList(self, request):
        """This API is used to export the list of baselines.

        :param request: Request instance for ExportBaselineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBashEvents(self, request):
        """This API is used to export high-risk command events.

        :param request: Request instance for ExportBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBashEventsNew(self, request):
        """This API is used to export high-risk command events (new).

        :param request: Request instance for ExportBashEventsNew.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsNewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBashEventsNew", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBashEventsNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBashPolicies(self, request):
        """This API is used to export the high-risk command policy.

        :param request: Request instance for ExportBashPolicies.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBashPoliciesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBashPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBashPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBashPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBruteAttacks(self, request):
        """This API is used to export password cracking records to a CSV file.

        :param request: Request instance for ExportBruteAttacks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBruteAttacksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportFileTamperEvents(self, request):
        """This API is used to export core file events.

        :param request: Request instance for ExportFileTamperEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportFileTamperEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportFileTamperEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportFileTamperEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportFileTamperEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportFileTamperRules(self, request):
        """This API is used to export core file monitoring rules.

        :param request: Request instance for ExportFileTamperRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportFileTamperRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportFileTamperRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportFileTamperRules", params, headers=headers)
            response = json.loads(body)
            model = models.ExportFileTamperRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportIgnoreBaselineRule(self, request):
        """This API is used to export information of ignored baseline detection items.

        :param request: Request instance for ExportIgnoreBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportIgnoreBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.ExportIgnoreBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportIgnoreRuleEffectHostList(self, request):
        """This API is used to export the list of hosts affected by ignored detection items based on detection item IDs.

        :param request: Request instance for ExportIgnoreRuleEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreRuleEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreRuleEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportIgnoreRuleEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportIgnoreRuleEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportJavaMemShellPlugins(self, request):
        """This API is used to export the Java webshell plugin information.

        :param request: Request instance for ExportJavaMemShellPlugins.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportJavaMemShellPluginsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportJavaMemShellPluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportJavaMemShellPlugins", params, headers=headers)
            response = json.loads(body)
            model = models.ExportJavaMemShellPluginsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportJavaMemShells(self, request):
        """This API is used to export the list of Java webshell events.

        :param request: Request instance for ExportJavaMemShells.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportJavaMemShellsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportJavaMemShellsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportJavaMemShells", params, headers=headers)
            response = json.loads(body)
            model = models.ExportJavaMemShellsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportLicenseDetail(self, request):
        """This API is used to export authorization details.

        :param request: Request instance for ExportLicenseDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportLicenseDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportLicenseDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportLicenseDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ExportLicenseDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportMaliciousRequests(self, request):
        """This API is used to export the downloaded malicious request files.

        :param request: Request instance for ExportMaliciousRequests.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.ExportMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportMalwares(self, request):
        """This API is used to export Trojan records to a CSV file.

        :param request: Request instance for ExportMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.ExportMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportNonlocalLoginPlaces(self, request):
        """This API is used to export cross-region log-in event records in CSV format.

        :param request: Request instance for ExportNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.ExportNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportPrivilegeEvents(self, request):
        """This API is used to export local privilege escalation events.

        :param request: Request instance for ExportPrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportPrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportPrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportPrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportPrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRansomDefenseBackupList(self, request):
        """This API is used to export the list of host snapshot backups.

        :param request: Request instance for ExportRansomDefenseBackupList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseBackupListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseBackupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRansomDefenseBackupList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRansomDefenseBackupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRansomDefenseEventsList(self, request):
        """This API is used to export the list of anti-ransomware events.

        :param request: Request instance for ExportRansomDefenseEventsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseEventsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseEventsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRansomDefenseEventsList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRansomDefenseEventsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRansomDefenseMachineList(self, request):
        """This API is used to export the backup details list.

        :param request: Request instance for ExportRansomDefenseMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRansomDefenseMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRansomDefenseMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRansomDefenseStrategyList(self, request):
        """This API is used to export the anti-ransomware policy list.

        :param request: Request instance for ExportRansomDefenseStrategyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseStrategyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseStrategyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRansomDefenseStrategyList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRansomDefenseStrategyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRansomDefenseStrategyMachines(self, request):
        """This API is used to export the list of machines bound to ransomware defense policies.

        :param request: Request instance for ExportRansomDefenseStrategyMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseStrategyMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseStrategyMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRansomDefenseStrategyMachines", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRansomDefenseStrategyMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportReverseShellEvents(self, request):
        """This API is used to export reverse shell events.

        :param request: Request instance for ExportReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRiskDnsEventList(self, request):
        """This API is used to export the malicious request event list.

        :param request: Request instance for ExportRiskDnsEventList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRiskDnsEventListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRiskDnsEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRiskDnsEventList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRiskDnsEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRiskDnsPolicyList(self, request):
        """This API is used to export the malicious request policy list.

        :param request: Request instance for ExportRiskDnsPolicyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRiskDnsPolicyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRiskDnsPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRiskDnsPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRiskDnsPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRiskProcessEvents(self, request):
        """This API is used to export abnormal process events.

        :param request: Request instance for ExportRiskProcessEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRiskProcessEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRiskProcessEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRiskProcessEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRiskProcessEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportScanTaskDetails(self, request):
        """This API is used to export the specified scan task details by task ID.

        :param request: Request instance for ExportScanTaskDetails.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportScanTaskDetailsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportScanTaskDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportScanTaskDetails", params, headers=headers)
            response = json.loads(body)
            model = models.ExportScanTaskDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportSecurityTrends(self, request):
        """This API is used to export risk trends.

        :param request: Request instance for ExportSecurityTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportSecurityTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportSecurityTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportSecurityTrends", params, headers=headers)
            response = json.loads(body)
            model = models.ExportSecurityTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportTasks(self, request):
        """This API is used to export log files with large data volumes asynchronously.

        :param request: Request instance for ExportTasks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportTasksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ExportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDefenceEvent(self, request):
        """This API is used to export vulnerability defense events.

        :param request: Request instance for ExportVulDefenceEvent.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefenceEventRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefenceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDefenceEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDefenceEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDefenceList(self, request):
        """This API is used to export the list of vulnerability defenses.

        :param request: Request instance for ExportVulDefenceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefenceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefenceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDefenceList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDefenceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDefencePluginEvent(self, request):
        """This API is used to export vulnerability defense plugin events.

        :param request: Request instance for ExportVulDefencePluginEvent.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefencePluginEventRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefencePluginEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDefencePluginEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDefencePluginEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDetectionExcel(self, request):
        """This API is used to export the vulnerability detection Excel document.

        :param request: Request instance for ExportVulDetectionExcel.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionExcelRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionExcelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDetectionExcel", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDetectionExcelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDetectionReport(self, request):
        """This API is used to export the vulnerability detection report.

        :param request: Request instance for ExportVulDetectionReport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionReportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDetectionReport", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDetectionReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulEffectHostList(self, request):
        """This API is used to export the list of hosts affected by vulnerabilities.

        :param request: Request instance for ExportVulEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulInfo(self, request):
        """This API is used to export the vulnerability information, including the list of affected hosts and component information.

        :param request: Request instance for ExportVulInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulList(self, request):
        """This API is used to export the vulnerability list.

        :param request: Request instance for ExportVulList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLocalStorageItem(self, request):
        """This API is used to obtain the locally stored data.

        :param request: Request instance for GetLocalStorageItem.
        :type request: :class:`tencentcloud.cwp.v20180228.models.GetLocalStorageItemRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.GetLocalStorageItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLocalStorageItem", params, headers=headers)
            response = json.loads(body)
            model = models.GetLocalStorageItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IgnoreImpactedHosts(self, request):
        """This API is used to ignore vulnerabilities.

        :param request: Request instance for IgnoreImpactedHosts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.IgnoreImpactedHostsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.IgnoreImpactedHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IgnoreImpactedHosts", params, headers=headers)
            response = json.loads(body)
            model = models.IgnoreImpactedHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KeysLocalStorage(self, request):
        """This API is used to obtain the list of locally stored key values.

        :param request: Request instance for KeysLocalStorage.
        :type request: :class:`tencentcloud.cwp.v20180228.models.KeysLocalStorageRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.KeysLocalStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KeysLocalStorage", params, headers=headers)
            response = json.loads(body)
            model = models.KeysLocalStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoOpenProVersionConfig(self, request):
        """This API is used to enable the configuration of automatically enabling the professional protection configuration for newly added hosts.

        :param request: Request instance for ModifyAutoOpenProVersionConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyAutoOpenProVersionConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyAutoOpenProVersionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoOpenProVersionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoOpenProVersionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBanMode(self, request):
        """This API is used to modify the brute-force blocking mode.

        :param request: Request instance for ModifyBanMode.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBanModeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBanModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBanMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBanModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBanStatus(self, request):
        """This API is used to set the block switch status.

        :param request: Request instance for ModifyBanStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBanStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBanWhiteList(self, request):
        """This API is used to modify the blocking allowlist.

        :param request: Request instance for ModifyBanWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBanWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBanWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBanWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBanWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselinePolicy(self, request):
        """This API is used to change the baseline policy settings.

        :param request: Request instance for ModifyBaselinePolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBashPolicy(self, request):
        """This API is used to add or modify high-risk command policies.

        :param request: Request instance for ModifyBashPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBashPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBashPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBashPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBashPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBashPolicyStatus(self, request):
        """This API is used to switch the statuses of high-risk command policies.

        :param request: Request instance for ModifyBashPolicyStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBashPolicyStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBashPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBashPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBashPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBruteAttackRules(self, request):
        """This API is used to modify brute force cracking rules.

        :param request: Request instance for ModifyBruteAttackRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBruteAttackRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBruteAttackRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBruteAttackRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBruteAttackRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEventAttackStatus(self, request):
        """This API is used to modify the status of network attack events.

        :param request: Request instance for ModifyEventAttackStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyEventAttackStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyEventAttackStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEventAttackStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEventAttackStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileTamperEvents(self, request):
        """This API is used to update the core file events.

        :param request: Request instance for ModifyFileTamperEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileTamperEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileTamperEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileTamperRule(self, request):
        """This API is used to edit and add core file monitoring rules.

        :param request: Request instance for ModifyFileTamperRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileTamperRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileTamperRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileTamperRuleStatus(self, request):
        """This API is used to update the core file rule status (batch deletion and disabling supported).

        :param request: Request instance for ModifyFileTamperRuleStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperRuleStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileTamperRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileTamperRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyJavaMemShellPluginSwitch(self, request):
        """This API is used to enable and disable Java webshell plugins.

        :param request: Request instance for ModifyJavaMemShellPluginSwitch.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyJavaMemShellPluginSwitchRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyJavaMemShellPluginSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyJavaMemShellPluginSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyJavaMemShellPluginSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyJavaMemShellsStatus(self, request):
        """This API is used to modify the Java webshell event status.

        :param request: Request instance for ModifyJavaMemShellsStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyJavaMemShellsStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyJavaMemShellsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyJavaMemShellsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyJavaMemShellsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLicenseBinds(self, request):
        """This API is used to bind machines to an authorization in batches.

        :param request: Request instance for ModifyLicenseBinds.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseBindsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLicenseBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLicenseBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLicenseOrder(self, request):
        """This API is used to edit CWPP - pay-as-you-go authorization orders.

        :param request: Request instance for ModifyLicenseOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLicenseOrder", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLicenseOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogKafkaAccess(self, request):
        """This API is used to add or modify the access configuration of logs shipped to Kafka.

        :param request: Request instance for ModifyLogKafkaAccess.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaAccessRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogKafkaAccess", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogKafkaAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogKafkaDeliverType(self, request):
        """This API is used to modify the shipping configuration and switch of the specified log category.

        :param request: Request instance for ModifyLogKafkaDeliverType.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaDeliverTypeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaDeliverTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogKafkaDeliverType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogKafkaDeliverTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogKafkaState(self, request):
        """This API is used to modify the information of log shipping statuses.

        :param request: Request instance for ModifyLogKafkaState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogKafkaState", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogKafkaStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogStorageConfig(self, request):
        """This API is used to modify the log storage configuration.

        :param request: Request instance for ModifyLogStorageConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLogStorageConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLogStorageConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogStorageConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogStorageConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoginWhiteInfo(self, request):
        """This API is used to update the log-in audit allowlist information.

        :param request: Request instance for ModifyLoginWhiteInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLoginWhiteInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLoginWhiteInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoginWhiteInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoginWhiteInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoginWhiteRecord(self, request):
        """This API is used to update the log-in audit allowlist information. (The number of server lists needs to be less than 1,000.)

        :param request: Request instance for ModifyLoginWhiteRecord.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLoginWhiteRecordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLoginWhiteRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoginWhiteRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoginWhiteRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMachineAutoClearConfig(self, request):
        """This API is used to modify the cleanup configuration of the machine.

        :param request: Request instance for ModifyMachineAutoClearConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMachineAutoClearConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMachineAutoClearConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMachineAutoClearConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMachineAutoClearConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMaliciousRequestWhiteList(self, request):
        """This API is used to update the malicious request allowlist.

        :param request: Request instance for ModifyMaliciousRequestWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMaliciousRequestWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMaliciousRequestWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaliciousRequestWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMaliciousRequestWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMalwareTimingScanSettings(self, request):
        """This API is used to set scheduled scan.

        :param request: Request instance for ModifyMalwareTimingScanSettings.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareTimingScanSettingsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareTimingScanSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMalwareTimingScanSettings", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMalwareTimingScanSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMalwareWhiteList(self, request):
        """This API is used to edit the Trojan allowlist.

        :param request: Request instance for ModifyMalwareWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMalwareWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMalwareWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetAttackSetting(self, request):
        """This API is used to modify network attack settings.

        :param request: Request instance for ModifyNetAttackSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyNetAttackSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyNetAttackSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetAttackSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetAttackSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetAttackWhiteList(self, request):
        """This API is used to edit the network attack whitelist.

        :param request: Request instance for ModifyNetAttackWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyNetAttackWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyNetAttackWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetAttackWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetAttackWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRansomDefenseEventsStatus(self, request):
        """This API is used to modify the status of anti-ransomware events.

        :param request: Request instance for ModifyRansomDefenseEventsStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRansomDefenseEventsStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRansomDefenseEventsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRansomDefenseEventsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRansomDefenseEventsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRansomDefenseStrategyStatus(self, request):
        """This API is used to modify the anti-ransomware policy status in batches.

        :param request: Request instance for ModifyRansomDefenseStrategyStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRansomDefenseStrategyStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRansomDefenseStrategyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRansomDefenseStrategyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRansomDefenseStrategyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskDnsPolicy(self, request):
        """This API is used to modify malicious request policies.

        :param request: Request instance for ModifyRiskDnsPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskDnsPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskDnsPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskDnsPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskDnsPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskDnsPolicyStatus(self, request):
        """This API is used to modify the status of malicious request policies.

        :param request: Request instance for ModifyRiskDnsPolicyStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskDnsPolicyStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskDnsPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskDnsPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskDnsPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskEventsStatus(self, request):
        """This API is used to change the status of intrusion detection events, including virus scanning, abnormal log-ins, password cracking, high-risk commands, reverse shells, and local privilege escalations.

        :param request: Request instance for ModifyRiskEventsStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskEventsStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskEventsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskEventsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskEventsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUsersConfig(self, request):
        """This API is used to create or modify user custom settings.

        :param request: Request instance for ModifyUsersConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyUsersConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyUsersConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUsersConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUsersConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVulDefenceEventStatus(self, request):
        """This API is used to change the vulnerability defense event status. (Vulnerability fixing is carried out using another API.)

        :param request: Request instance for ModifyVulDefenceEventStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyVulDefenceEventStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyVulDefenceEventStatusResponse`

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
        """This API is used to modify vulnerability defense plugin settings.
        1) The new settings apply to new hosts automatically. scope is set to 1, and quuids is left blank.
        2) The new settings do not apply to Ultimate Edition hosts. scope is set to 0, and the current QUUID list is specified as the value of quuids.
        3) For a given QUUID list, when scope is set to 0, QUUID selected by the user is specified as the value of quuids.

        :param request: Request instance for ModifyVulDefenceSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyVulDefenceSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyVulDefenceSettingResponse`

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


    def ModifyWarningHostConfig(self, request):
        """This API is used to modify the alarming machine scope settings.

        :param request: Request instance for ModifyWarningHostConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningHostConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningHostConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWarningHostConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWarningHostConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWarningSetting(self, request):
        """This API is used to modify alarm settings.

        :param request: Request instance for ModifyWarningSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWarningSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWarningSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebHookPolicy(self, request):
        """This API is used to add or modify alarm policies.

        :param request: Request instance for ModifyWebHookPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebHookPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebHookPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebHookPolicyStatus(self, request):
        """This API is used to modify the alarm policy switch.

        :param request: Request instance for ModifyWebHookPolicyStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookPolicyStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebHookPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebHookPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebHookReceiver(self, request):
        """This API is used to add or update the alarm recipient.

        :param request: Request instance for ModifyWebHookReceiver.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookReceiverRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebHookReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebHookReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebHookRule(self, request):
        """This API is used to add or modify the rules of WeCom chatbots.

        :param request: Request instance for ModifyWebHookRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebHookRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebHookRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebHookRuleStatus(self, request):
        """This API is used to modify the rules of WeCom chatbots.

        :param request: Request instance for ModifyWebHookRuleStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookRuleStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebHookRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebHookRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebPageProtectSwitch(self, request):
        """This API is used to enable or disable website anti-tampering protection.

        :param request: Request instance for ModifyWebPageProtectSwitch.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSwitchRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebPageProtectSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebPageProtectSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RansomDefenseRollback(self, request):
        """This API is used to roll back anti-ransomware snapshots.

        :param request: Request instance for RansomDefenseRollback.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RansomDefenseRollbackRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RansomDefenseRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RansomDefenseRollback", params, headers=headers)
            response = json.loads(body)
            model = models.RansomDefenseRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverMalwares(self, request):
        """This API is used to batch recover quarantined Trojan files.

        :param request: Request instance for RecoverMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RecoverMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RecoverMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveLocalStorageItem(self, request):
        """This API is used to delete the locally stored data.

        :param request: Request instance for RemoveLocalStorageItem.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RemoveLocalStorageItemRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RemoveLocalStorageItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveLocalStorageItem", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveLocalStorageItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveMachine(self, request):
        """This API is used to delete all records of the host. Currently, it only supports non-Tencent Cloud hosts, and the host needs to be offline.

        :param request: Request instance for RemoveMachine.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RemoveMachineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RemoveMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveMachine", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryCreateSnapshot(self, request):
        """This API is used to retry to create snapshots and automatically fix vulnerabilities when the creation fails.

        :param request: Request instance for RetryCreateSnapshot.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RetryCreateSnapshotRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RetryCreateSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryCreateSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.RetryCreateSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryVulFix(self, request):
        """This API is used to fix vulnerabilities on a single host when the fix fails.

        :param request: Request instance for RetryVulFix.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RetryVulFixRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RetryVulFixResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryVulFix", params, headers=headers)
            response = json.loads(body)
            model = models.RetryVulFixResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanBaseline(self, request):
        """This API is used to obtain baseline detection and re-detection APIs.

        :param request: Request instance for ScanBaseline.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanBaselineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.ScanBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanTaskAgain(self, request):
        """This API is used to restart the scan task. Specifying the machine is supported.

        :param request: Request instance for ScanTaskAgain.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanTaskAgainRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanTaskAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanTaskAgain", params, headers=headers)
            response = json.loads(body)
            model = models.ScanTaskAgainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanVul(self, request):
        """This API is used to perform one-click vulnerability scans.

        :param request: Request instance for ScanVul.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanVul", params, headers=headers)
            response = json.loads(body)
            model = models.ScanVulResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanVulAgain(self, request):
        """This API is used to redetect the API.

        :param request: Request instance for ScanVulAgain.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulAgainRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanVulAgain", params, headers=headers)
            response = json.loads(body)
            model = models.ScanVulAgainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanVulSetting(self, request):
        """This API is used to complete regular vulnerability scan settings.

        :param request: Request instance for ScanVulSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanVulSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ScanVulSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchLog(self, request):
        """This API is used to query logs.

        :param request: Request instance for SearchLog.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SearchLogRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SearchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SeparateMalwares(self, request):
        """This API is used to isolate Trojans.

        :param request: Request instance for SeparateMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SeparateMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SeparateMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SeparateMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.SeparateMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetBashEventsStatus(self, request):
        """This API is used to set the high-risk command event status.

        :param request: Request instance for SetBashEventsStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SetBashEventsStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SetBashEventsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetBashEventsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.SetBashEventsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLocalStorageExpire(self, request):
        """This API is used to set the expiration time of the locally stored data.

        :param request: Request instance for SetLocalStorageExpire.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SetLocalStorageExpireRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SetLocalStorageExpireResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLocalStorageExpire", params, headers=headers)
            response = json.loads(body)
            model = models.SetLocalStorageExpireResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLocalStorageItem(self, request):
        """This API is used to set the locally stored data.

        :param request: Request instance for SetLocalStorageItem.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SetLocalStorageItemRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SetLocalStorageItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLocalStorageItem", params, headers=headers)
            response = json.loads(body)
            model = models.SetLocalStorageItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartBaselineDetect(self, request):
        """This API is used to perform baseline checks.

        :param request: Request instance for StartBaselineDetect.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StartBaselineDetectRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StartBaselineDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartBaselineDetect", params, headers=headers)
            response = json.loads(body)
            model = models.StartBaselineDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAssetScan(self, request):
        """This API is used to stop the asset scan task.

        :param request: Request instance for StopAssetScan.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StopAssetScanRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StopAssetScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAssetScan", params, headers=headers)
            response = json.loads(body)
            model = models.StopAssetScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopBaselineDetect(self, request):
        """This API is used to stop baseline check.

        :param request: Request instance for StopBaselineDetect.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StopBaselineDetectRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StopBaselineDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopBaselineDetect", params, headers=headers)
            response = json.loads(body)
            model = models.StopBaselineDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopNoticeBanTips(self, request):
        """This API is used to stop displaying pop-up prompts about brute force cracking blocking.

        :param request: Request instance for StopNoticeBanTips.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StopNoticeBanTipsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StopNoticeBanTipsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopNoticeBanTips", params, headers=headers)
            response = json.loads(body)
            model = models.StopNoticeBanTipsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchBashRules(self, request):
        """This API is used to switch the statuses of high-risk command rules.

        :param request: Request instance for SwitchBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SwitchBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SwitchBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncAssetScan(self, request):
        """This API is used to synchronize the asset scan information.

        :param request: Request instance for SyncAssetScan.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SyncAssetScanRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SyncAssetScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncAssetScan", params, headers=headers)
            response = json.loads(body)
            model = models.SyncAssetScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncBaselineDetectSummary(self, request):
        """This API is used to sync the summary of baseline detection progress.

        :param request: Request instance for SyncBaselineDetectSummary.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SyncBaselineDetectSummaryRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SyncBaselineDetectSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncBaselineDetectSummary", params, headers=headers)
            response = json.loads(body)
            model = models.SyncBaselineDetectSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncMachines(self, request):
        """This API is used to sync the machine information.

        :param request: Request instance for SyncMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SyncMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SyncMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncMachines", params, headers=headers)
            response = json.loads(body)
            model = models.SyncMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TestWebHookRule(self, request):
        """This API is used to test the rules of WeCom chatbots.

        :param request: Request instance for TestWebHookRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.TestWebHookRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.TestWebHookRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TestWebHookRule", params, headers=headers)
            response = json.loads(body)
            model = models.TestWebHookRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TrustMalwares(self, request):
        """This API is used to mark identified Trojan files as Trusted.

        :param request: Request instance for TrustMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.TrustMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.TrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TrustMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.TrustMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UntrustMalwares(self, request):
        """This API is used to untrust Trojan files.

        :param request: Request instance for UntrustMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UntrustMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UntrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UntrustMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.UntrustMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBaselineStrategy(self, request):
        """This API is used to update the policy information based on baseline policy IDs.

        :param request: Request instance for UpdateBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UpdateBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UpdateBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBaselineStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBaselineStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateMachineTags(self, request):
        """This API is used to obtain the list of tags associated with machines.

        :param request: Request instance for UpdateMachineTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UpdateMachineTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UpdateMachineTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateMachineTags", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateMachineTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))