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
from tencentcloud.antiddos.v20200309 import models
from typing import Dict


class AntiddosClient(AbstractClient):
    _apiVersion = '2020-03-09'
    _endpoint = 'antiddos.intl.tencentcloudapi.com'
    _service = 'antiddos'

    async def AssociateDDoSEipAddress(
            self,
            request: models.AssociateDDoSEipAddressRequest,
            opts: Dict = None,
    ) -> models.AssociateDDoSEipAddressResponse:
        """
        This API is used to bind an EIP to an Anti-DDoS Advanced instance or a specified private IP of an ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateDDoSEipAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateDDoSEipAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateDDoSEipLoadBalancer(
            self,
            request: models.AssociateDDoSEipLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.AssociateDDoSEipLoadBalancerResponse:
        """
        This API is used to bind an Anti-DDoS EIP to the specified private IP of a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateDDoSEipLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateDDoSEipLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBlackWhiteIpList(
            self,
            request: models.CreateBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.CreateBlackWhiteIpListResponse:
        """
        This API is used to add an Anti-DDoS IP blocklist/allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBoundIP(
            self,
            request: models.CreateBoundIPRequest,
            opts: Dict = None,
    ) -> models.CreateBoundIPResponse:
        """
        This API is used to bind an IP to an Anti-DDoS Pro instance Both single IP instances and multi-IP instances are available. Note that you should wait until the current binding or unbinding completes before using this async API for new operations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBoundIP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBoundIPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCCPrecisionPolicy(
            self,
            request: models.CreateCCPrecisionPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateCCPrecisionPolicyResponse:
        """
        This API is used to create a CC precise protection policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCCPrecisionPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCCPrecisionPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCCReqLimitPolicy(
            self,
            request: models.CreateCCReqLimitPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateCCReqLimitPolicyResponse:
        """
        This API is used to create a CC frequency limit policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCCReqLimitPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCCReqLimitPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCcBlackWhiteIpList(
            self,
            request: models.CreateCcBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.CreateCcBlackWhiteIpListResponse:
        """
        This API is used to create a layer 4 access control list to prevent CC attacks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCcBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCcBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCcGeoIPBlockConfig(
            self,
            request: models.CreateCcGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.CreateCcGeoIPBlockConfigResponse:
        """
        This API is used to create a regional blocking configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCcGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCcGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSAI(
            self,
            request: models.CreateDDoSAIRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSAIResponse:
        """
        This API is used to set Anti-DDoS AI protection switches.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSAI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSAIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSGeoIPBlockConfig(
            self,
            request: models.CreateDDoSGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSGeoIPBlockConfigResponse:
        """
        This API is used to add an Anti-DDoS region blocking configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSSpeedLimitConfig(
            self,
            request: models.CreateDDoSSpeedLimitConfigRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSSpeedLimitConfigResponse:
        """
        This API is used to add Anti-DDoS access rate limit configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSSpeedLimitConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSSpeedLimitConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDefaultAlarmThreshold(
            self,
            request: models.CreateDefaultAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.CreateDefaultAlarmThresholdResponse:
        """
        This API is used to set the default alarm threshold of an IP.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDefaultAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDefaultAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIPAlarmThresholdConfig(
            self,
            request: models.CreateIPAlarmThresholdConfigRequest,
            opts: Dict = None,
    ) -> models.CreateIPAlarmThresholdConfigResponse:
        """
        This API is used to set the default alarm threshold of an IP.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIPAlarmThresholdConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIPAlarmThresholdConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7RuleCerts(
            self,
            request: models.CreateL7RuleCertsRequest,
            opts: Dict = None,
    ) -> models.CreateL7RuleCertsResponse:
        """
        This API is used to configure certificates with layer-7 forwarding rules in a batch for SSL testing.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7RuleCerts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7RuleCertsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNewL7Rules(
            self,
            request: models.CreateNewL7RulesRequest,
            opts: Dict = None,
    ) -> models.CreateNewL7RulesResponse:
        """
        This API is used to add layer-7 forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNewL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNewL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePacketFilterConfig(
            self,
            request: models.CreatePacketFilterConfigRequest,
            opts: Dict = None,
    ) -> models.CreatePacketFilterConfigResponse:
        """
        This API is used to add Anti-DDoS feature filtering rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePacketFilterConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePacketFilterConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProtocolBlockConfig(
            self,
            request: models.CreateProtocolBlockConfigRequest,
            opts: Dict = None,
    ) -> models.CreateProtocolBlockConfigResponse:
        """
        This API is used to set Anti-DDoS protocol blocking configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProtocolBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProtocolBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSchedulingDomain(
            self,
            request: models.CreateSchedulingDomainRequest,
            opts: Dict = None,
    ) -> models.CreateSchedulingDomainResponse:
        """
        This API is used to create a domain name for IP scheduling and switching.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSchedulingDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSchedulingDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWaterPrintConfig(
            self,
            request: models.CreateWaterPrintConfigRequest,
            opts: Dict = None,
    ) -> models.CreateWaterPrintConfigResponse:
        """
        This API is used to add Anti-DDoS watermark configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWaterPrintConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWaterPrintConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWaterPrintKey(
            self,
            request: models.CreateWaterPrintKeyRequest,
            opts: Dict = None,
    ) -> models.CreateWaterPrintKeyResponse:
        """
        This API is used to add Anti-DDoS watermark keys.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWaterPrintKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWaterPrintKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCLevelPolicy(
            self,
            request: models.DeleteCCLevelPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteCCLevelPolicyResponse:
        """
        This API is used to delete a level-defining policy of CC attacks.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCLevelPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCLevelPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCPrecisionPolicy(
            self,
            request: models.DeleteCCPrecisionPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteCCPrecisionPolicyResponse:
        """
        This API is used to delete a CC precise protection policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCPrecisionPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCPrecisionPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCThresholdPolicy(
            self,
            request: models.DeleteCCThresholdPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteCCThresholdPolicyResponse:
        """
        This API is used to delete a CC cleansing threshold policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCThresholdPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCThresholdPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCcBlackWhiteIpList(
            self,
            request: models.DeleteCcBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.DeleteCcBlackWhiteIpListResponse:
        """
        This API is used to delete a layer-4 access control list.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCcBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCcBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCcGeoIPBlockConfig(
            self,
            request: models.DeleteCcGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteCcGeoIPBlockConfigResponse:
        """
        This API is used to delete a regional blocking configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCcGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCcGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDDoSGeoIPBlockConfig(
            self,
            request: models.DeleteDDoSGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteDDoSGeoIPBlockConfigResponse:
        """
        This API is used to delete Anti-DDoS region blocking configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDDoSGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDDoSGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDDoSSpeedLimitConfig(
            self,
            request: models.DeleteDDoSSpeedLimitConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteDDoSSpeedLimitConfigResponse:
        """
        This API is used to delete Anti-DDoS access rate limit configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDDoSSpeedLimitConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDDoSSpeedLimitConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePacketFilterConfig(
            self,
            request: models.DeletePacketFilterConfigRequest,
            opts: Dict = None,
    ) -> models.DeletePacketFilterConfigResponse:
        """
        This API is used to delete Anti-DDoS feature filtering rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePacketFilterConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePacketFilterConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWaterPrintConfig(
            self,
            request: models.DeleteWaterPrintConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteWaterPrintConfigResponse:
        """
        This API is used to delete Anti-DDoS watermark configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWaterPrintConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWaterPrintConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWaterPrintKey(
            self,
            request: models.DeleteWaterPrintKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteWaterPrintKeyResponse:
        """
        This API is used to delete Anti-DDoS watermark keys.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWaterPrintKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWaterPrintKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBasicDeviceStatus(
            self,
            request: models.DescribeBasicDeviceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBasicDeviceStatusResponse:
        """
        This API is used to querying the status of Anti-DDoS IP.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBasicDeviceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBasicDeviceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBgpBizTrend(
            self,
            request: models.DescribeBgpBizTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeBgpBizTrendResponse:
        """
        This API is used to obtain Anti-DDoS Pro traffic data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBgpBizTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBgpBizTrendResponse
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
        
    async def DescribeBizTrend(
            self,
            request: models.DescribeBizTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeBizTrendResponse:
        """
        This API is used to get the traffic flow data collected in the specified period.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBizTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBizTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCLevelList(
            self,
            request: models.DescribeCCLevelListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCLevelListResponse:
        """
        Gets the list of CC protection levels
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCLevelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCLevelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCLevelPolicy(
            self,
            request: models.DescribeCCLevelPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeCCLevelPolicyResponse:
        """
        This API is used the query a level-defining policy of CC attacks
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCLevelPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCLevelPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCPrecisionPlyList(
            self,
            request: models.DescribeCCPrecisionPlyListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCPrecisionPlyListResponse:
        """
        This API is used to obtain the list of CC precise protection policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCPrecisionPlyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCPrecisionPlyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCThresholdList(
            self,
            request: models.DescribeCCThresholdListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCThresholdListResponse:
        """
        This API is used to query the list of CC cleansing thresholds.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCThresholdList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCThresholdListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCTrend(
            self,
            request: models.DescribeCCTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeCCTrendResponse:
        """
        This API is used to get CC attack data, including total QPS peaks, attack QPS, total number of requests and number of attack requests.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcBlackWhiteIpList(
            self,
            request: models.DescribeCcBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeCcBlackWhiteIpListResponse:
        """
        This API is used to obtain the layer-4 access control list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcGeoIPBlockConfigList(
            self,
            request: models.DescribeCcGeoIPBlockConfigListRequest,
            opts: Dict = None,
    ) -> models.DescribeCcGeoIPBlockConfigListResponse:
        """
        This API is used to obtain a list of regional blocking configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcGeoIPBlockConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcGeoIPBlockConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSTrend(
            self,
            request: models.DescribeDDoSTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSTrendResponse:
        """
        This API is used to get DDoS attack traffic bandwidth and attack packet rate.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultAlarmThreshold(
            self,
            request: models.DescribeDefaultAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultAlarmThresholdResponse:
        """
        This API is used to get the default alarm threshold of an IP.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpBlockList(
            self,
            request: models.DescribeIpBlockListRequest,
            opts: Dict = None,
    ) -> models.DescribeIpBlockListResponse:
        """
        
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpBlockList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpBlockListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7RulesBySSLCertId(
            self,
            request: models.DescribeL7RulesBySSLCertIdRequest,
            opts: Dict = None,
    ) -> models.DescribeL7RulesBySSLCertIdResponse:
        """
        This API is used to query layer-7 rules matched with certificate IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7RulesBySSLCertId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7RulesBySSLCertIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListBGPIPInstances(
            self,
            request: models.DescribeListBGPIPInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeListBGPIPInstancesResponse:
        """
        This API is used to get a list of Anti-DDoS Advanced instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListBGPIPInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListBGPIPInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListBGPInstances(
            self,
            request: models.DescribeListBGPInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeListBGPInstancesResponse:
        """
        This API is used to get the list of Anti-DDoS Pro instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListBGPInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListBGPInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListBlackWhiteIpList(
            self,
            request: models.DescribeListBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeListBlackWhiteIpListResponse:
        """
        This API is used to get a list of Anti-DDoS IP blocklists/allowlists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListDDoSAI(
            self,
            request: models.DescribeListDDoSAIRequest,
            opts: Dict = None,
    ) -> models.DescribeListDDoSAIResponse:
        """
        This API is used to get a list of Anti-DDoS AI protection switches.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListDDoSAI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListDDoSAIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListDDoSGeoIPBlockConfig(
            self,
            request: models.DescribeListDDoSGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListDDoSGeoIPBlockConfigResponse:
        """
        This API is used to get a list of Anti-DDoS region blocking configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListDDoSGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListDDoSGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListDDoSSpeedLimitConfig(
            self,
            request: models.DescribeListDDoSSpeedLimitConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListDDoSSpeedLimitConfigResponse:
        """
        This API is used to get a list of Anti-DDoS access rate limit configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListDDoSSpeedLimitConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListDDoSSpeedLimitConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListIPAlarmConfig(
            self,
            request: models.DescribeListIPAlarmConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListIPAlarmConfigResponse:
        """
        This API is used to get a list of IP alarm threshold configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListIPAlarmConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListIPAlarmConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListListener(
            self,
            request: models.DescribeListListenerRequest,
            opts: Dict = None,
    ) -> models.DescribeListListenerResponse:
        """
        This API is used to get a list of forwarding listeners.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListPacketFilterConfig(
            self,
            request: models.DescribeListPacketFilterConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListPacketFilterConfigResponse:
        """
        This API is used to get a list of Anti-DDoS feature filtering rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListPacketFilterConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListPacketFilterConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListProtocolBlockConfig(
            self,
            request: models.DescribeListProtocolBlockConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListProtocolBlockConfigResponse:
        """
        This API is used to get a list of Anti-DDoS protocol blocking configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListProtocolBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListProtocolBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListSchedulingDomain(
            self,
            request: models.DescribeListSchedulingDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeListSchedulingDomainResponse:
        """
        This API is used to get a list of intelligent scheduling domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListSchedulingDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListSchedulingDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListWaterPrintConfig(
            self,
            request: models.DescribeListWaterPrintConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListWaterPrintConfigResponse:
        """
        This API is used to get a list of Anti-DDoS watermark configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListWaterPrintConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListWaterPrintConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNewL7Rules(
            self,
            request: models.DescribeNewL7RulesRequest,
            opts: Dict = None,
    ) -> models.DescribeNewL7RulesResponse:
        """
        This API is used to obtain layer-7 forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNewL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNewL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNewL7RulesErrHealth(
            self,
            request: models.DescribeNewL7RulesErrHealthRequest,
            opts: Dict = None,
    ) -> models.DescribeNewL7RulesErrHealthResponse:
        """
        This API is used to getting the exception results of the health check on layer-7 forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNewL7RulesErrHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNewL7RulesErrHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewDDoSEventList(
            self,
            request: models.DescribeOverviewDDoSEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewDDoSEventListResponse:
        """
        This API is used to obtain the list of DDoS attacks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewDDoSEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewDDoSEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePendingRiskInfo(
            self,
            request: models.DescribePendingRiskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePendingRiskInfoResponse:
        """
        This API is used to query the information of pending risks at the account level.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePendingRiskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePendingRiskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateDDoSEipAddress(
            self,
            request: models.DisassociateDDoSEipAddressRequest,
            opts: Dict = None,
    ) -> models.DisassociateDDoSEipAddressResponse:
        """
        This API is used to unbind an Anti-DDoS EIP.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateDDoSEipAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateDDoSEipAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCPrecisionPolicy(
            self,
            request: models.ModifyCCPrecisionPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyCCPrecisionPolicyResponse:
        """
        This API is used to modify a CC precise protection policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCPrecisionPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCPrecisionPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCcBlackWhiteIpList(
            self,
            request: models.ModifyCcBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.ModifyCcBlackWhiteIpListResponse:
        """
        This API is used to modify a layer-4 access control list.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCcBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCcBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSGeoIPBlockConfig(
            self,
            request: models.ModifyDDoSGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSGeoIPBlockConfigResponse:
        """
        This API is used to modify Anti-DDoS region blocking configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSSpeedLimitConfig(
            self,
            request: models.ModifyDDoSSpeedLimitConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSSpeedLimitConfigResponse:
        """
        This API is used to modify Anti-DDoS access rate limit configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSSpeedLimitConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSSpeedLimitConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainUsrName(
            self,
            request: models.ModifyDomainUsrNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainUsrNameResponse:
        """
        This API is used to modify intelligent scheduling domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainUsrName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainUsrNameResponse
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
        
    async def ModifyPacketFilterConfig(
            self,
            request: models.ModifyPacketFilterConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyPacketFilterConfigResponse:
        """
        This API is used to modify Anti-DDoS feature filtering rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPacketFilterConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPacketFilterConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchWaterPrintConfig(
            self,
            request: models.SwitchWaterPrintConfigRequest,
            opts: Dict = None,
    ) -> models.SwitchWaterPrintConfigResponse:
        """
        This API is used to enable or disable Anti-DDoS watermark configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchWaterPrintConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchWaterPrintConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)