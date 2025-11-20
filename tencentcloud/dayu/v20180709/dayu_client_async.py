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
from tencentcloud.dayu.v20180709 import models
from typing import Dict


class DayuClient(AbstractClient):
    _apiVersion = '2018-07-09'
    _endpoint = 'dayu.intl.tencentcloudapi.com'
    _service = 'dayu'

    async def CreateBasicDDoSAlarmThreshold(
            self,
            request: models.CreateBasicDDoSAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.CreateBasicDDoSAlarmThresholdResponse:
        """
        This API is used to set the DDoS alarm threshold for Anti-DDoS Basic, which is only supported for Anti-DDoS Basic.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBasicDDoSAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBasicDDoSAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBoundIP(
            self,
            request: models.CreateBoundIPRequest,
            opts: Dict = None,
    ) -> models.CreateBoundIPResponse:
        """
        This API is used to bind an IP to an Anti-DDoS Pro instance, which supports both single IP instances and multi-IP instances. It should be noted that this API is async; therefore, if a binding/unbinding operation is in progress, new binding/unbinding operations cannot be initiated.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBoundIP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBoundIPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCCFrequencyRules(
            self,
            request: models.CreateCCFrequencyRulesRequest,
            opts: Dict = None,
    ) -> models.CreateCCFrequencyRulesResponse:
        """
        This API is used to add an access frequency control rule for CC protection.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCCFrequencyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCCFrequencyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCCSelfDefinePolicy(
            self,
            request: models.CreateCCSelfDefinePolicyRequest,
            opts: Dict = None,
    ) -> models.CreateCCSelfDefinePolicyResponse:
        """
        This API is used to create a custom CC policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCCSelfDefinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCCSelfDefinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSPolicy(
            self,
            request: models.CreateDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSPolicyResponse:
        """
        This API is used to add an advanced DDoS policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSPolicyCase(
            self,
            request: models.CreateDDoSPolicyCaseRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSPolicyCaseResponse:
        """
        This API is used to add a policy scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSPolicyCase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSPolicyCaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceName(
            self,
            request: models.CreateInstanceNameRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceNameResponse:
        """
        This API is used to rename a resource instance, which supports single IP instances, multi-IP instances, Anti-DDoS Advanced, and Anti-DDoS Ultimate.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL4HealthConfig(
            self,
            request: models.CreateL4HealthConfigRequest,
            opts: Dict = None,
    ) -> models.CreateL4HealthConfigResponse:
        """
        This API is used to upload layer-4 health check configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL4HealthConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL4HealthConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL4Rules(
            self,
            request: models.CreateL4RulesRequest,
            opts: Dict = None,
    ) -> models.CreateL4RulesResponse:
        """
        This API is used to add a layer-4 forwarding rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7CCRule(
            self,
            request: models.CreateL7CCRuleRequest,
            opts: Dict = None,
    ) -> models.CreateL7CCRuleResponse:
        """
        This API is used to add a custom frequency control rule for layer-7 CC access (it works in the IP + Host dimension and does not support specific URIs). As it has been disused, please call the new `CreateCCFrequencyRules` API, which supports both IP + Host and URI.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7CCRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7CCRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7HealthConfig(
            self,
            request: models.CreateL7HealthConfigRequest,
            opts: Dict = None,
    ) -> models.CreateL7HealthConfigResponse:
        """
        This API is used to upload layer-7 health check configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7HealthConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7HealthConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7RuleCert(
            self,
            request: models.CreateL7RuleCertRequest,
            opts: Dict = None,
    ) -> models.CreateL7RuleCertResponse:
        """
        This API is used to configure a certificate for a layer-7 forwarding rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7RuleCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7RuleCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7Rules(
            self,
            request: models.CreateL7RulesRequest,
            opts: Dict = None,
    ) -> models.CreateL7RulesResponse:
        """
        This API is used to add a layer-7 (website) forwarding rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7RulesUpload(
            self,
            request: models.CreateL7RulesUploadRequest,
            opts: Dict = None,
    ) -> models.CreateL7RulesUploadResponse:
        """
        This API is used to upload layer-7 forwarding rules in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7RulesUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7RulesUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetReturn(
            self,
            request: models.CreateNetReturnRequest,
            opts: Dict = None,
    ) -> models.CreateNetReturnResponse:
        """
        This API is used to switch to the real server in Anti-DDoS Ultimate.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetReturn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetReturnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNewL7RulesUpload(
            self,
            request: models.CreateNewL7RulesUploadRequest,
            opts: Dict = None,
    ) -> models.CreateNewL7RulesUploadResponse:
        """
        This API is used to batch upload Layer-7 forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNewL7RulesUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNewL7RulesUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUnblockIp(
            self,
            request: models.CreateUnblockIpRequest,
            opts: Dict = None,
    ) -> models.CreateUnblockIpResponse:
        """
        This API is used to unblock an IP.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUnblockIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUnblockIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCFrequencyRules(
            self,
            request: models.DeleteCCFrequencyRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteCCFrequencyRulesResponse:
        """
        This API is used to delete an access frequency control rule for CC protection.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCFrequencyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCFrequencyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCSelfDefinePolicy(
            self,
            request: models.DeleteCCSelfDefinePolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteCCSelfDefinePolicyResponse:
        """
        This API is used to delete a custom CC policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCSelfDefinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCSelfDefinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDDoSPolicy(
            self,
            request: models.DeleteDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteDDoSPolicyResponse:
        """
        This API is used to delete an advanced DDoS protection policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDDoSPolicyCase(
            self,
            request: models.DeleteDDoSPolicyCaseRequest,
            opts: Dict = None,
    ) -> models.DeleteDDoSPolicyCaseResponse:
        """
        This API is used to delete a policy scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDDoSPolicyCase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDDoSPolicyCaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL4Rules(
            self,
            request: models.DeleteL4RulesRequest,
            opts: Dict = None,
    ) -> models.DeleteL4RulesResponse:
        """
        This API is used to delete one or more layer-4 forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL7Rules(
            self,
            request: models.DeleteL7RulesRequest,
            opts: Dict = None,
    ) -> models.DeleteL7RulesResponse:
        """
        This API is used to delete one or more layer-7 forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActionLog(
            self,
            request: models.DescribeActionLogRequest,
            opts: Dict = None,
    ) -> models.DescribeActionLogResponse:
        """
        This API is used to get operation logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActionLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActionLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBGPIPL7RuleMaxCnt(
            self,
            request: models.DescribeBGPIPL7RuleMaxCntRequest,
            opts: Dict = None,
    ) -> models.DescribeBGPIPL7RuleMaxCntResponse:
        """
        This API is used to get the maximum number of layer-7 rules that can be added for Anti-DDoS Advanced.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBGPIPL7RuleMaxCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBGPIPL7RuleMaxCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaradData(
            self,
            request: models.DescribeBaradDataRequest,
            opts: Dict = None,
    ) -> models.DescribeBaradDataResponse:
        """
        This API is used to provide business forwarding metric data of Anti-DDoS services.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaradData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaradDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBasicCCThreshold(
            self,
            request: models.DescribeBasicCCThresholdRequest,
            opts: Dict = None,
    ) -> models.DescribeBasicCCThresholdResponse:
        """
        This API is used to get the CC protection threshold of Anti-DDoS Basic.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBasicCCThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBasicCCThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBasicDeviceThreshold(
            self,
            request: models.DescribeBasicDeviceThresholdRequest,
            opts: Dict = None,
    ) -> models.DescribeBasicDeviceThresholdResponse:
        """
        This API is used to get the blackhole threshold of Anti-DDoS Basic.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBasicDeviceThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBasicDeviceThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBizHttpStatus(
            self,
            request: models.DescribeBizHttpStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBizHttpStatusResponse:
        """
        This API is used to get the statistics on the status codes of business traffic.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBizHttpStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBizHttpStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCAlarmThreshold(
            self,
            request: models.DescribeCCAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.DescribeCCAlarmThresholdResponse:
        """
        This API is used to get the alarm notification threshold set for CC attacks in Anti-DDoS Pro, Anti-DDoS Advanced, Anti-DDoS Ultimate, and Chess Shield.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCEvList(
            self,
            request: models.DescribeCCEvListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCEvListResponse:
        """
        This API is used to get the CC attack event list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCEvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCEvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCFrequencyRules(
            self,
            request: models.DescribeCCFrequencyRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeCCFrequencyRulesResponse:
        """
        This API is used to get an access frequency control rule for CC protection.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCFrequencyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCFrequencyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCIpAllowDeny(
            self,
            request: models.DescribeCCIpAllowDenyRequest,
            opts: Dict = None,
    ) -> models.DescribeCCIpAllowDenyResponse:
        """
        This API is used to get the CC IP blocklist/allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCIpAllowDeny"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCIpAllowDenyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCSelfDefinePolicy(
            self,
            request: models.DescribeCCSelfDefinePolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeCCSelfDefinePolicyResponse:
        """
        This API is used to get a custom CC policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCSelfDefinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCSelfDefinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCTrend(
            self,
            request: models.DescribeCCTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeCCTrendResponse:
        """
        This API is used to get CC attack metric data, including total requests peak (QPS) and attack requests (QPS).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCUrlAllow(
            self,
            request: models.DescribeCCUrlAllowRequest,
            opts: Dict = None,
    ) -> models.DescribeCCUrlAllowResponse:
        """
        This API is used to get the CC URL allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCUrlAllow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCUrlAllowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAlarmThreshold(
            self,
            request: models.DescribeDDoSAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAlarmThresholdResponse:
        """
        This API is used to get the alarm notification threshold set for DDoS attacks in Anti-DDoS Pro, Anti-DDoS Advanced, Anti-DDoS Ultimate, and Chess Shield.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackIPRegionMap(
            self,
            request: models.DescribeDDoSAttackIPRegionMapRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackIPRegionMapResponse:
        """
        This API is used to get the geographical distribution map of DDoS attack source IPs. It supports display by global regions and Chinese provinces.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAttackIPRegionMap"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAttackIPRegionMapResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackSource(
            self,
            request: models.DescribeDDoSAttackSourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackSourceResponse:
        """
        This API is used to get the DDoS attack source list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAttackSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAttackSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSCount(
            self,
            request: models.DescribeDDoSCountRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSCountResponse:
        """
        This API is used to get the DDoS attack proportion analysis.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSDefendStatus(
            self,
            request: models.DescribeDDoSDefendStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSDefendStatusResponse:
        """
        This API is used to get the DDoS protection status (temporarily disabled status). It is supported for Anti-DDoS Basic, single IP instance, multi-IP instance, Anti-DDoS Advanced, and Anti-DDoS Ultimate. It is used to query whether DDoS protection is temporarily disabled, and if yes, return parameters such as temporary disablement duration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSDefendStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSDefendStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSEvInfo(
            self,
            request: models.DescribeDDoSEvInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSEvInfoResponse:
        """
        This API is used to get details of a specific DDoS attack.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSEvInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSEvInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSEvList(
            self,
            request: models.DescribeDDoSEvListRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSEvListResponse:
        """
        This API is used to get the DDoS attack event list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSEvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSEvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSIpLog(
            self,
            request: models.DescribeDDoSIpLogRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSIpLogResponse:
        """
        This API is used to get a DDoS IP attack log.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSIpLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSIpLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSNetCount(
            self,
            request: models.DescribeDDoSNetCountRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSNetCountResponse:
        """
        This API is used to get the DDoS attack proportion analysis for an Anti-DDoS Ultimate resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSNetCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSNetCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSNetEvInfo(
            self,
            request: models.DescribeDDoSNetEvInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSNetEvInfoResponse:
        """
        This API is used to get the DDoS attack event details of an Anti-DDoS Ultimate resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSNetEvInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSNetEvInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSNetEvList(
            self,
            request: models.DescribeDDoSNetEvListRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSNetEvListResponse:
        """
        This API is used to get the DDoS attack event list of an Anti-DDoS Ultimate resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSNetEvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSNetEvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSNetIpLog(
            self,
            request: models.DescribeDDoSNetIpLogRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSNetIpLogResponse:
        """
        This API is used to get the DDoS IP attack logs of an Anti-DDoS Ultimate resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSNetIpLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSNetIpLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSNetTrend(
            self,
            request: models.DescribeDDoSNetTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSNetTrendResponse:
        """
        This API is used to get the DDoS attack metric data of an Anti-DDoS Ultimate resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSNetTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSNetTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSPolicy(
            self,
            request: models.DescribeDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSPolicyResponse:
        """
        This API is used to get an advanced DDoS policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSTrend(
            self,
            request: models.DescribeDDoSTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSTrendResponse:
        """
        This API is used to get the data of DDoS attack traffic bandwidth and attack packet rate.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSUsedStatis(
            self,
            request: models.DescribeDDoSUsedStatisRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSUsedStatisResponse:
        """
        This API is used to count the number of days of Anti-DDoS resource use and number of DDoS attacks defended against.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSUsedStatis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSUsedStatisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPProductInfo(
            self,
            request: models.DescribeIPProductInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeIPProductInfoResponse:
        """
        This API is used to get the Tencent Cloud asset information corresponding to an IP of a single IP instance or multi-IP instance, which is supported only for IPs of single IP instances and multi-IP instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPProductInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPProductInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInsurePacks(
            self,
            request: models.DescribeInsurePacksRequest,
            opts: Dict = None,
    ) -> models.DescribeInsurePacksResponse:
        """
        This API is used to get the guarantee package list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInsurePacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInsurePacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpBlockList(
            self,
            request: models.DescribeIpBlockListRequest,
            opts: Dict = None,
    ) -> models.DescribeIpBlockListResponse:
        """
        This API is used to get the blocked IP list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpBlockList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpBlockListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpUnBlockList(
            self,
            request: models.DescribeIpUnBlockListRequest,
            opts: Dict = None,
    ) -> models.DescribeIpUnBlockListResponse:
        """
        This API is used to get the IP unblocking records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpUnBlockList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpUnBlockListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4HealthConfig(
            self,
            request: models.DescribeL4HealthConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeL4HealthConfigResponse:
        """
        This API is used to export the layer-4 health check configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4HealthConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4HealthConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4RulesErrHealth(
            self,
            request: models.DescribeL4RulesErrHealthRequest,
            opts: Dict = None,
    ) -> models.DescribeL4RulesErrHealthResponse:
        """
        This API is used to get the exception result of a layer-4 forwarding rule health check.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4RulesErrHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4RulesErrHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7HealthConfig(
            self,
            request: models.DescribeL7HealthConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeL7HealthConfigResponse:
        """
        This API is used to export the layer-7 health check configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7HealthConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7HealthConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePackIndex(
            self,
            request: models.DescribePackIndexRequest,
            opts: Dict = None,
    ) -> models.DescribePackIndexResponse:
        """
        This API is used to get the product overview statistics. It is supported for Anti-DDoS Pro, Anti-DDoS Advanced, and Anti-DDoS Ultimate.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePackIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePackIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePcap(
            self,
            request: models.DescribePcapRequest,
            opts: Dict = None,
    ) -> models.DescribePcapResponse:
        """
        This API is used to download the PCAP packet of an attack event.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePcap"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePcapResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyCase(
            self,
            request: models.DescribePolicyCaseRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyCaseResponse:
        """
        This API is used to get the policy scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyCase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyCaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResIpList(
            self,
            request: models.DescribeResIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeResIpListResponse:
        """
        This API is used to get the IP list of a resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceList(
            self,
            request: models.DescribeResourceListRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceListResponse:
        """
        This API is used to get the resource list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleSets(
            self,
            request: models.DescribeRuleSetsRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleSetsResponse:
        """
        This API is used to get the number of rules of a resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleSets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleSetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedulingDomainList(
            self,
            request: models.DescribeSchedulingDomainListRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulingDomainListResponse:
        """
        Get scheduling domain name list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedulingDomainList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulingDomainListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecIndex(
            self,
            request: models.DescribeSecIndexRequest,
            opts: Dict = None,
    ) -> models.DescribeSecIndexResponse:
        """
        This API is used to get the security statistics of the current month.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSourceIpSegment(
            self,
            request: models.DescribeSourceIpSegmentRequest,
            opts: Dict = None,
    ) -> models.DescribeSourceIpSegmentResponse:
        """
        This API is used to get the intermediate IP range. It is supported for Anti-DDoS Advanced and Anti-DDoS Ultimate.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSourceIpSegment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSourceIpSegmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTransmitStatis(
            self,
            request: models.DescribeTransmitStatisRequest,
            opts: Dict = None,
    ) -> models.DescribeTransmitStatisResponse:
        """
        This API is used to get the business forwarding statistics, including forwarded traffic and packet forwarding rate.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTransmitStatis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTransmitStatisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnBlockStatis(
            self,
            request: models.DescribeUnBlockStatisRequest,
            opts: Dict = None,
    ) -> models.DescribeUnBlockStatisResponse:
        """
        This API is used to get the number of blackhole unblockings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnBlockStatis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnBlockStatisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribleL4Rules(
            self,
            request: models.DescribleL4RulesRequest,
            opts: Dict = None,
    ) -> models.DescribleL4RulesResponse:
        """
        This API is used to get a layer-4 forwarding rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribleL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribleL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribleL7Rules(
            self,
            request: models.DescribleL7RulesRequest,
            opts: Dict = None,
    ) -> models.DescribleL7RulesResponse:
        """
        This API is used to get a layer-7 forwarding rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribleL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribleL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribleRegionCount(
            self,
            request: models.DescribleRegionCountRequest,
            opts: Dict = None,
    ) -> models.DescribleRegionCountResponse:
        """
        This API is used to get the number of resource instances in a region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribleRegionCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribleRegionCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCAlarmThreshold(
            self,
            request: models.ModifyCCAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.ModifyCCAlarmThresholdResponse:
        """
        This API is used to set the alarm notification threshold for CC attacks in Anti-DDoS Pro, Anti-DDoS Advanced, Anti-DDoS Ultimate, and Chess Shield.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCFrequencyRules(
            self,
            request: models.ModifyCCFrequencyRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyCCFrequencyRulesResponse:
        """
        This API is used to modify an access frequency control rule for CC protection.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCFrequencyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCFrequencyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCFrequencyRulesStatus(
            self,
            request: models.ModifyCCFrequencyRulesStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCCFrequencyRulesStatusResponse:
        """
        This API is used to enable or disable an access frequency control rule for CC protection.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCFrequencyRulesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCFrequencyRulesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCHostProtection(
            self,
            request: models.ModifyCCHostProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifyCCHostProtectionResponse:
        """
        This API is used to enable or disable CC domain name protection.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCHostProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCHostProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCIpAllowDeny(
            self,
            request: models.ModifyCCIpAllowDenyRequest,
            opts: Dict = None,
    ) -> models.ModifyCCIpAllowDenyResponse:
        """
        This API is used to add/remove a CC IP to/from the blocklist/allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCIpAllowDeny"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCIpAllowDenyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCLevel(
            self,
            request: models.ModifyCCLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyCCLevelResponse:
        """
        This API is used to modify CC protection level.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCPolicySwitch(
            self,
            request: models.ModifyCCPolicySwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyCCPolicySwitchResponse:
        """
        This API is used to enable or disable a custom CC policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCPolicySwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCPolicySwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCSelfDefinePolicy(
            self,
            request: models.ModifyCCSelfDefinePolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyCCSelfDefinePolicyResponse:
        """
        This API is used to modify a custom CC policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCSelfDefinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCSelfDefinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCThreshold(
            self,
            request: models.ModifyCCThresholdRequest,
            opts: Dict = None,
    ) -> models.ModifyCCThresholdResponse:
        """
        This API is used to modify the CC protection threshold.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCUrlAllow(
            self,
            request: models.ModifyCCUrlAllowRequest,
            opts: Dict = None,
    ) -> models.ModifyCCUrlAllowResponse:
        """
        This API is used to add/remove a CC URL to/from the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCUrlAllow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCUrlAllowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSAIStatus(
            self,
            request: models.ModifyDDoSAIStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSAIStatusResponse:
        """
        This API is used to read or modify DDoS AI protection status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSAIStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSAIStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSAlarmThreshold(
            self,
            request: models.ModifyDDoSAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSAlarmThresholdResponse:
        """
        This API is used to set the alarm notification threshold for DDoS attacks in Anti-DDoS Pro, Anti-DDoS Advanced, Anti-DDoS Ultimate, and Chess Shield.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSDefendStatus(
            self,
            request: models.ModifyDDoSDefendStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSDefendStatusResponse:
        """
        This API is used to enable or disable DDoS. It can disable DDoS protection for a period of time, which will be automatically enabled after the period of time elapses.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSDefendStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSDefendStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSLevel(
            self,
            request: models.ModifyDDoSLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSLevelResponse:
        """
        This API is used to read or modify DDoS protection level.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSPolicy(
            self,
            request: models.ModifyDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSPolicyResponse:
        """
        This API is used to modify an advanced DDoS policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSPolicyCase(
            self,
            request: models.ModifyDDoSPolicyCaseRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSPolicyCaseResponse:
        """
        This API is used to modify a policy scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSPolicyCase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSPolicyCaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSPolicyName(
            self,
            request: models.ModifyDDoSPolicyNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSPolicyNameResponse:
        """
        This API is used to rename an advanced DDoS policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSPolicyName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSPolicyNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSSwitch(
            self,
            request: models.ModifyDDoSSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSSwitchResponse:
        """
        This API is used to enable or disable DDoS protection, which is only supported for Anti-DDoS Basic.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSThreshold(
            self,
            request: models.ModifyDDoSThresholdRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSThresholdResponse:
        """
        This API is used to modify the DDoS cleansing threshold.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSWaterKey(
            self,
            request: models.ModifyDDoSWaterKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSWaterKeyResponse:
        """
        This API is used to add, delete, enable, or disable a watermark key.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSWaterKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSWaterKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyElasticLimit(
            self,
            request: models.ModifyElasticLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyElasticLimitResponse:
        """
        This API is used to modify the elastic protection threshold.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyElasticLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyElasticLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4Health(
            self,
            request: models.ModifyL4HealthRequest,
            opts: Dict = None,
    ) -> models.ModifyL4HealthResponse:
        """
        This API is used to modify the health check parameters of a layer-4 forwarding rule. It is supported for Anti-DDoS Advanced and Anti-DDoS Ultimate.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4Health"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4HealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4KeepTime(
            self,
            request: models.ModifyL4KeepTimeRequest,
            opts: Dict = None,
    ) -> models.ModifyL4KeepTimeResponse:
        """
        This API is used to modify the session persistence of a layer-4 forwarding rule. It is supported for Anti-DDoS Advanced and Anti-DDoS Ultimate.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4KeepTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4KeepTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4Rules(
            self,
            request: models.ModifyL4RulesRequest,
            opts: Dict = None,
    ) -> models.ModifyL4RulesResponse:
        """
        This API is used to modify a layer-4 forwarding rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7Rules(
            self,
            request: models.ModifyL7RulesRequest,
            opts: Dict = None,
    ) -> models.ModifyL7RulesResponse:
        """
        This API is used to modify the layer-7 forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetReturnSwitch(
            self,
            request: models.ModifyNetReturnSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyNetReturnSwitchResponse:
        """
        This API is used to switch a client to the real server and set the switch duration when the client is under attack or blocked.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetReturnSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetReturnSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNewDomainRules(
            self,
            request: models.ModifyNewDomainRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyNewDomainRulesResponse:
        """
        This API is used to modify layer-7 forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNewDomainRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNewDomainRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNewL4Rule(
            self,
            request: models.ModifyNewL4RuleRequest,
            opts: Dict = None,
    ) -> models.ModifyNewL4RuleResponse:
        """
        This API is used to modify layer-4 forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNewL4Rule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNewL4RuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResBindDDoSPolicy(
            self,
            request: models.ModifyResBindDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyResBindDDoSPolicyResponse:
        """
        This API is used to bind an advanced DDoS policy to an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResBindDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResBindDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceRenewFlag(
            self,
            request: models.ModifyResourceRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceRenewFlagResponse:
        """
        This API is used to enable or disable auto-renewal for a resource.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)