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
from tencentcloud.teo.v20220106 import models
from typing import Dict


class TeoClient(AbstractClient):
    _apiVersion = '2022-01-06'
    _endpoint = 'teo.intl.tencentcloudapi.com'
    _service = 'teo'

    async def CheckCertificate(
            self,
            request: models.CheckCertificateRequest,
            opts: Dict = None,
    ) -> models.CheckCertificateResponse:
        """
        This API is used to verify a certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationProxy(
            self,
            request: models.CreateApplicationProxyRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationProxyResponse:
        """
        This API is used to create an application proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationProxyRule(
            self,
            request: models.CreateApplicationProxyRuleRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationProxyRuleResponse:
        """
        This API is used to create an application proxy rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationProxyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationProxyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationProxyRules(
            self,
            request: models.CreateApplicationProxyRulesRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationProxyRulesResponse:
        """
        This API is used to batch create application proxy rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationProxyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationProxyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomErrorPage(
            self,
            request: models.CreateCustomErrorPageRequest,
            opts: Dict = None,
    ) -> models.CreateCustomErrorPageResponse:
        """
        This API is used to create a custom error page.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomErrorPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomErrorPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDnsRecord(
            self,
            request: models.CreateDnsRecordRequest,
            opts: Dict = None,
    ) -> models.CreateDnsRecordResponse:
        """
        This API is used to create a DNS record.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDnsRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDnsRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancing(
            self,
            request: models.CreateLoadBalancingRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancingResponse:
        """
        This API is used to create a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancing"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOriginGroup(
            self,
            request: models.CreateOriginGroupRequest,
            opts: Dict = None,
    ) -> models.CreateOriginGroupResponse:
        """
        This API is used to create an origin group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrefetchTask(
            self,
            request: models.CreatePrefetchTaskRequest,
            opts: Dict = None,
    ) -> models.CreatePrefetchTaskResponse:
        """
        This API is used to create a pre-warming task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrefetchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrefetchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePurgeTask(
            self,
            request: models.CreatePurgeTaskRequest,
            opts: Dict = None,
    ) -> models.CreatePurgeTaskResponse:
        """
        This API is used to create a cache purging task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePurgeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePurgeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateZone(
            self,
            request: models.CreateZoneRequest,
            opts: Dict = None,
    ) -> models.CreateZoneResponse:
        """
        This API is used to access a new site.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationProxy(
            self,
            request: models.DeleteApplicationProxyRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationProxyResponse:
        """
        This API is used to delete an application proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationProxyRule(
            self,
            request: models.DeleteApplicationProxyRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationProxyRuleResponse:
        """
        This API is used to delete an application proxy rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationProxyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationProxyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDnsRecords(
            self,
            request: models.DeleteDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.DeleteDnsRecordsResponse:
        """
        This API is used to batch delete DNS records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancing(
            self,
            request: models.DeleteLoadBalancingRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancingResponse:
        """
        This API is used to delete a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancing"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOriginGroup(
            self,
            request: models.DeleteOriginGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteOriginGroupResponse:
        """
        This API is used to delete an origin group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteZone(
            self,
            request: models.DeleteZoneRequest,
            opts: Dict = None,
    ) -> models.DeleteZoneResponse:
        """
        This API is used to delete a site.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationProxy(
            self,
            request: models.DescribeApplicationProxyRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationProxyResponse:
        """
        This API is used to obtain a list of application proxies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationProxyDetail(
            self,
            request: models.DescribeApplicationProxyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationProxyDetailResponse:
        """
        This API is used to obtain the details of an application proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationProxyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationProxyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBotLog(
            self,
            request: models.DescribeBotLogRequest,
            opts: Dict = None,
    ) -> models.DescribeBotLogResponse:
        """
        This API is used to query bot attack logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBotLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBotLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBotManagedRules(
            self,
            request: models.DescribeBotManagedRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBotManagedRulesResponse:
        """
        This API is used to query bot managed rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBotManagedRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBotManagedRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCnameStatus(
            self,
            request: models.DescribeCnameStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeCnameStatusResponse:
        """
        This API is used to query the CNAME status of a domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCnameStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCnameStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSPolicy(
            self,
            request: models.DescribeDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSPolicyResponse:
        """
        This API is used to query the DDoS protection configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDosAttackData(
            self,
            request: models.DescribeDDosAttackDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDDosAttackDataResponse:
        """
        This API is used to query the DDoS attack data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDosAttackData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDosAttackDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDosAttackEvent(
            self,
            request: models.DescribeDDosAttackEventRequest,
            opts: Dict = None,
    ) -> models.DescribeDDosAttackEventResponse:
        """
        This API is used to query DDoS attack events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDosAttackEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDosAttackEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDosAttackEventDetail(
            self,
            request: models.DescribeDDosAttackEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDDosAttackEventDetailResponse:
        """
        This API is used to query DDoS attack event details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDosAttackEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDosAttackEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDosAttackSourceEvent(
            self,
            request: models.DescribeDDosAttackSourceEventRequest,
            opts: Dict = None,
    ) -> models.DescribeDDosAttackSourceEventResponse:
        """
        This API is used to query DDoS attack sources.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDosAttackSourceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDosAttackSourceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDosAttackTopData(
            self,
            request: models.DescribeDDosAttackTopDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDDosAttackTopDataResponse:
        """
        This API is used to query the top data of DDoS attacks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDosAttackTopData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDosAttackTopDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDosMajorAttackEvent(
            self,
            request: models.DescribeDDosMajorAttackEventRequest,
            opts: Dict = None,
    ) -> models.DescribeDDosMajorAttackEventResponse:
        """
        This API is used to query the major DDoS attack event.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDosMajorAttackEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDosMajorAttackEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultCertificates(
            self,
            request: models.DescribeDefaultCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultCertificatesResponse:
        """
        This API is used to query a list of default certificates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDnsData(
            self,
            request: models.DescribeDnsDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDnsDataResponse:
        """
        This API is used to obtain collected DNS requests.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDnsData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDnsDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDnsRecords(
            self,
            request: models.DescribeDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDnsRecordsResponse:
        """
        This API is used to query DNS records. Paging, sorting and filtering are supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDnssec(
            self,
            request: models.DescribeDnssecRequest,
            opts: Dict = None,
    ) -> models.DescribeDnssecResponse:
        """
        This API is used to query DNSSEC information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDnssec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDnssecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostsCertificate(
            self,
            request: models.DescribeHostsCertificateRequest,
            opts: Dict = None,
    ) -> models.DescribeHostsCertificateResponse:
        """
        This API is used to query certificates of domain names. Paging, sorting and filtering are supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostsCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostsCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostsSetting(
            self,
            request: models.DescribeHostsSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeHostsSettingResponse:
        """
        This API is used to query detailed domain name configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostsSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostsSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdentification(
            self,
            request: models.DescribeIdentificationRequest,
            opts: Dict = None,
    ) -> models.DescribeIdentificationResponse:
        """
        This API is used to query verification results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdentification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdentificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancing(
            self,
            request: models.DescribeLoadBalancingRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancingResponse:
        """
        This API is used to obtain a list of CLB instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancing"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancingDetail(
            self,
            request: models.DescribeLoadBalancingDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancingDetailResponse:
        """
        This API is used to query the details of a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancingDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancingDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginGroup(
            self,
            request: models.DescribeOriginGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginGroupResponse:
        """
        This API is used to get the list of origin groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginGroupDetail(
            self,
            request: models.DescribeOriginGroupDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginGroupDetailResponse:
        """
        This API is used to get the details of the origin group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginGroupDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginGroupDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewL7Data(
            self,
            request: models.DescribeOverviewL7DataRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewL7DataResponse:
        """
        This API is used to query the layer-7 time series traffic data for monitoring.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewL7Data"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewL7DataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrefetchTasks(
            self,
            request: models.DescribePrefetchTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePrefetchTasksResponse:
        """
        This API is used to query the pre-warming task status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrefetchTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrefetchTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurgeTasks(
            self,
            request: models.DescribePurgeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePurgeTasksResponse:
        """
        This API is used to query the cache purging history.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurgeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurgeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicy(
            self,
            request: models.DescribeSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyResponse:
        """
        This API is used to query the security protection configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicyList(
            self,
            request: models.DescribeSecurityPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyListResponse:
        """
        This API is used to query all protected subdomain names.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicyManagedRules(
            self,
            request: models.DescribeSecurityPolicyManagedRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyManagedRulesResponse:
        """
        This API is used to query managed rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicyManagedRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyManagedRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicyManagedRulesId(
            self,
            request: models.DescribeSecurityPolicyManagedRulesIdRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyManagedRulesIdResponse:
        """
        This API is used to query the details of a managed rule by rule ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicyManagedRulesId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyManagedRulesIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicyRegions(
            self,
            request: models.DescribeSecurityPolicyRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyRegionsResponse:
        """
        This API is used to query information of all regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicyRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPortraitRules(
            self,
            request: models.DescribeSecurityPortraitRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPortraitRulesResponse:
        """
        This API is used to query user profiling rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPortraitRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPortraitRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL4Data(
            self,
            request: models.DescribeTimingL4DataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL4DataResponse:
        """
        This API is used to query the layer-4 time series traffic data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL4Data"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL4DataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL7AnalysisData(
            self,
            request: models.DescribeTimingL7AnalysisDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL7AnalysisDataResponse:
        """
        This API is used to query the layer-7 time series traffic data for data analysis.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL7AnalysisData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL7AnalysisDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL7CacheData(
            self,
            request: models.DescribeTimingL7CacheDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL7CacheDataResponse:
        """
        This API is used to query time-series L7 cached data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL7CacheData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL7CacheDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopL7AnalysisData(
            self,
            request: models.DescribeTopL7AnalysisDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTopL7AnalysisDataResponse:
        """
        This API is used to query the top traffic data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopL7AnalysisData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopL7AnalysisDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopL7CacheData(
            self,
            request: models.DescribeTopL7CacheDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTopL7CacheDataResponse:
        """
        This API is used to query the top-ranked L7 cached data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopL7CacheData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopL7CacheDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebManagedRulesAttackEvents(
            self,
            request: models.DescribeWebManagedRulesAttackEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeWebManagedRulesAttackEventsResponse:
        """
        This API is used to query web hosting attack events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebManagedRulesAttackEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebManagedRulesAttackEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebManagedRulesData(
            self,
            request: models.DescribeWebManagedRulesDataRequest,
            opts: Dict = None,
    ) -> models.DescribeWebManagedRulesDataResponse:
        """
        This API is used to query the web hosting rule data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebManagedRulesData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebManagedRulesDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebManagedRulesLog(
            self,
            request: models.DescribeWebManagedRulesLogRequest,
            opts: Dict = None,
    ) -> models.DescribeWebManagedRulesLogResponse:
        """
        This API is used to query web hosting logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebManagedRulesLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebManagedRulesLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebManagedRulesTopData(
            self,
            request: models.DescribeWebManagedRulesTopDataRequest,
            opts: Dict = None,
    ) -> models.DescribeWebManagedRulesTopDataResponse:
        """
        This API is used to query the top data of web hosting rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebManagedRulesTopData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebManagedRulesTopDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebProtectionAttackEvents(
            self,
            request: models.DescribeWebProtectionAttackEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeWebProtectionAttackEventsResponse:
        """
        This API is used to query web attack events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebProtectionAttackEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebProtectionAttackEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebProtectionData(
            self,
            request: models.DescribeWebProtectionDataRequest,
            opts: Dict = None,
    ) -> models.DescribeWebProtectionDataResponse:
        """
        This API is used to query the web protection data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebProtectionData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebProtectionDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebProtectionLog(
            self,
            request: models.DescribeWebProtectionLogRequest,
            opts: Dict = None,
    ) -> models.DescribeWebProtectionLogResponse:
        """
        This API is used to query web protection logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebProtectionLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebProtectionLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneDDoSPolicy(
            self,
            request: models.DescribeZoneDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneDDoSPolicyResponse:
        """
        This API is used to query all DDoS mitigation configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneDetails(
            self,
            request: models.DescribeZoneDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneDetailsResponse:
        """
        This API is used to query the details of a site by site ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneSetting(
            self,
            request: models.DescribeZoneSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneSettingResponse:
        """
        This API is used to query the site configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        This API is used to query the list of user sites.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadL7Logs(
            self,
            request: models.DownloadL7LogsRequest,
            opts: Dict = None,
    ) -> models.DownloadL7LogsResponse:
        """
        This API is used to query layer-7 logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadL7Logs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadL7LogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IdentifyZone(
            self,
            request: models.IdentifyZoneRequest,
            opts: Dict = None,
    ) -> models.IdentifyZoneResponse:
        """
        This API is used to verify ownership of the site.
        """
        
        kwargs = {}
        kwargs["action"] = "IdentifyZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IdentifyZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportDnsRecords(
            self,
            request: models.ImportDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.ImportDnsRecordsResponse:
        """
        This API is used to import DNS records.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxy(
            self,
            request: models.ModifyApplicationProxyRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyResponse:
        """
        This API is used to modify an application proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxyRule(
            self,
            request: models.ModifyApplicationProxyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyRuleResponse:
        """
        This API is used to modify an application proxy rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxyRuleStatus(
            self,
            request: models.ModifyApplicationProxyRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyRuleStatusResponse:
        """
        This API is used to modify the status of an application proxy rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxyRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxyStatus(
            self,
            request: models.ModifyApplicationProxyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyStatusResponse:
        """
        This API is used to modify the status of an application proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSPolicy(
            self,
            request: models.ModifyDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSPolicyResponse:
        """
        This API is used to modify DDoS mitigation configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSPolicyHost(
            self,
            request: models.ModifyDDoSPolicyHostRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSPolicyHostResponse:
        """
        This API is used to enable high availability for domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSPolicyHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSPolicyHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDefaultCertificate(
            self,
            request: models.ModifyDefaultCertificateRequest,
            opts: Dict = None,
    ) -> models.ModifyDefaultCertificateResponse:
        """
        This API is used to modify the status of a default certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDefaultCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDefaultCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDnsRecord(
            self,
            request: models.ModifyDnsRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyDnsRecordResponse:
        """
        This API is used to modify DNS records.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDnsRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDnsRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDnssec(
            self,
            request: models.ModifyDnssecRequest,
            opts: Dict = None,
    ) -> models.ModifyDnssecResponse:
        """
        This API is used to modify the DNSSEC status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDnssec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDnssecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostsCertificate(
            self,
            request: models.ModifyHostsCertificateRequest,
            opts: Dict = None,
    ) -> models.ModifyHostsCertificateResponse:
        """
        This API is used to modify the certificate of a domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostsCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostsCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancing(
            self,
            request: models.ModifyLoadBalancingRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancingResponse:
        """
        This API is used to modify a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancing"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancingStatus(
            self,
            request: models.ModifyLoadBalancingStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancingStatusResponse:
        """
        This API is used to modify the status of a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancingStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancingStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOriginGroup(
            self,
            request: models.ModifyOriginGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyOriginGroupResponse:
        """
        This API is used to modify an origin group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityPolicy(
            self,
            request: models.ModifySecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityPolicyResponse:
        """
        This API is used to modify the web and bot security configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZone(
            self,
            request: models.ModifyZoneRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneResponse:
        """
        This API is used to modify the site information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneCnameSpeedUp(
            self,
            request: models.ModifyZoneCnameSpeedUpRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneCnameSpeedUpResponse:
        """
        This API is used to modify the CNAME acceleration status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneCnameSpeedUp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneCnameSpeedUpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneSetting(
            self,
            request: models.ModifyZoneSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneSettingResponse:
        """
        This API is used to modify the site configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneStatus(
            self,
            request: models.ModifyZoneStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneStatusResponse:
        """
        This API is used to change the site status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReclaimZone(
            self,
            request: models.ReclaimZoneRequest,
            opts: Dict = None,
    ) -> models.ReclaimZoneResponse:
        """
        This API is used to reclaim a site from other users after its ownership is verified.
        """
        
        kwargs = {}
        kwargs["action"] = "ReclaimZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReclaimZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanDnsRecords(
            self,
            request: models.ScanDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.ScanDnsRecordsResponse:
        """
        This API is used to scan resolution records.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)