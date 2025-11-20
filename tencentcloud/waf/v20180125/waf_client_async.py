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
from tencentcloud.waf.v20180125 import models
from typing import Dict


class WafClient(AbstractClient):
    _apiVersion = '2018-01-25'
    _endpoint = 'waf.intl.tencentcloudapi.com'
    _service = 'waf'

    async def AddAntiFakeUrl(
            self,
            request: models.AddAntiFakeUrlRequest,
            opts: Dict = None,
    ) -> models.AddAntiFakeUrlResponse:
        """
        Add tamper-proof URL
        """
        
        kwargs = {}
        kwargs["action"] = "AddAntiFakeUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAntiFakeUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAntiInfoLeakRules(
            self,
            request: models.AddAntiInfoLeakRulesRequest,
            opts: Dict = None,
    ) -> models.AddAntiInfoLeakRulesResponse:
        """
        Add information leakage prevention rule
        """
        
        kwargs = {}
        kwargs["action"] = "AddAntiInfoLeakRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAntiInfoLeakRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCustomRule(
            self,
            request: models.AddCustomRuleRequest,
            opts: Dict = None,
    ) -> models.AddCustomRuleResponse:
        """
        Add access control (from custom policy)
        """
        
        kwargs = {}
        kwargs["action"] = "AddCustomRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCustomRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCustomWhiteRule(
            self,
            request: models.AddCustomWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.AddCustomWhiteRuleResponse:
        """
        Add precision allowlist rules
        """
        
        kwargs = {}
        kwargs["action"] = "AddCustomWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCustomWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddSpartaProtection(
            self,
            request: models.AddSpartaProtectionRequest,
            opts: Dict = None,
    ) -> models.AddSpartaProtectionResponse:
        """
        Add SaaS WAF protection domain
        """
        
        kwargs = {}
        kwargs["action"] = "AddSpartaProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddSpartaProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeals(
            self,
            request: models.CreateDealsRequest,
            opts: Dict = None,
    ) -> models.CreateDealsResponse:
        """
        Billing Resource Purchase, Renewal Order API
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeals"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDealsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHost(
            self,
            request: models.CreateHostRequest,
            opts: Dict = None,
    ) -> models.CreateHostResponse:
        """
        Add a protection domain in CLB-WAF
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIpAccessControl(
            self,
            request: models.CreateIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.CreateIpAccessControlResponse:
        """
        This API is used to add WAF IP allowlists/blocklists.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOwaspWhiteRule(
            self,
            request: models.CreateOwaspWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.CreateOwaspWhiteRuleResponse:
        """
        This API is used to add a rule engine allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOwaspWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOwaspWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAntiFakeUrl(
            self,
            request: models.DeleteAntiFakeUrlRequest,
            opts: Dict = None,
    ) -> models.DeleteAntiFakeUrlResponse:
        """
        Delete tamper-proof URL
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAntiFakeUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAntiFakeUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAntiInfoLeakRule(
            self,
            request: models.DeleteAntiInfoLeakRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAntiInfoLeakRuleResponse:
        """
        Delete information leakage prevention rule
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAntiInfoLeakRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAntiInfoLeakRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCRule(
            self,
            request: models.DeleteCCRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteCCRuleResponse:
        """
        WAF CC V2 deletion API
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomRule(
            self,
            request: models.DeleteCustomRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomRuleResponse:
        """
        Delete custom rule
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomWhiteRule(
            self,
            request: models.DeleteCustomWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomWhiteRuleResponse:
        """
        Delete precision allowlist rules
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHost(
            self,
            request: models.DeleteHostRequest,
            opts: Dict = None,
    ) -> models.DeleteHostResponse:
        """
        This API is used to delete a domain name protected by CLB WAF. Batch operation is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIpAccessControlV2(
            self,
            request: models.DeleteIpAccessControlV2Request,
            opts: Dict = None,
    ) -> models.DeleteIpAccessControlV2Response:
        """
        This API is used to delete latest versions of WAF IP allowlists/blocklists.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIpAccessControlV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIpAccessControlV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOwaspRuleStatus(
            self,
            request: models.DeleteOwaspRuleStatusRequest,
            opts: Dict = None,
    ) -> models.DeleteOwaspRuleStatusResponse:
        """
        This API is used to unlock the Door God rule status.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOwaspRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOwaspRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOwaspWhiteRule(
            self,
            request: models.DeleteOwaspWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteOwaspWhiteRuleResponse:
        """
        This API is used to delete a user rule engine allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOwaspWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOwaspWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSession(
            self,
            request: models.DeleteSessionRequest,
            opts: Dict = None,
    ) -> models.DeleteSessionResponse:
        """
        Delete CC attack session settings
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSpartaProtection(
            self,
            request: models.DeleteSpartaProtectionRequest,
            opts: Dict = None,
    ) -> models.DeleteSpartaProtectionResponse:
        """
        This API is used to delete a domain name protected by SaaS WAF.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSpartaProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSpartaProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAntiFakeRules(
            self,
            request: models.DescribeAntiFakeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAntiFakeRulesResponse:
        """
        Obtain a tamper-proof URL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAntiFakeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAntiFakeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAntiInfoLeakageRules(
            self,
            request: models.DescribeAntiInfoLeakageRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAntiInfoLeakageRulesResponse:
        """
        Obtain the information leakage prevention rule list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAntiInfoLeakageRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAntiInfoLeakageRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackOverview(
            self,
            request: models.DescribeAttackOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackOverviewResponse:
        """
        This API is used to describe the attack overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackType(
            self,
            request: models.DescribeAttackTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackTypeResponse:
        """
        Query the top N attack types for a specified domain
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchIpAccessControl(
            self,
            request: models.DescribeBatchIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchIpAccessControlResponse:
        """
        This API is used to query the IP blocklist and allowlist for WAF batch protection.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCRule(
            self,
            request: models.DescribeCCRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeCCRuleResponse:
        """
        WAF CC V2 query API
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCRuleList(
            self,
            request: models.DescribeCCRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCRuleListResponse:
        """
        Query CC rules based on multiple conditions
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateVerifyResult(
            self,
            request: models.DescribeCertificateVerifyResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateVerifyResultResponse:
        """
        Obtain certificate inspection result
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateVerifyResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateVerifyResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCiphersDetail(
            self,
            request: models.DescribeCiphersDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCiphersDetailResponse:
        """
        Query SaaS WAF cipher suite information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCiphersDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCiphersDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomRuleList(
            self,
            request: models.DescribeCustomRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomRuleListResponse:
        """
        Obtain the access control policy list in the protection configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomWhiteRule(
            self,
            request: models.DescribeCustomWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomWhiteRuleResponse:
        """
        Obtain the precision allowlist policy list in the protection configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainCountInfo(
            self,
            request: models.DescribeDomainCountInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainCountInfoResponse:
        """
        Obtain domain overview
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainCountInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainCountInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainDetailsClb(
            self,
            request: models.DescribeDomainDetailsClbRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainDetailsClbResponse:
        """
        Obtain CLB WAF domain details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainDetailsClb"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainDetailsClbResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainDetailsSaas(
            self,
            request: models.DescribeDomainDetailsSaasRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainDetailsSaasResponse:
        """
        Query individual SaaS WAF domain details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainDetailsSaas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainDetailsSaasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainVerifyResult(
            self,
            request: models.DescribeDomainVerifyResultRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainVerifyResultResponse:
        """
        Obtain the result of adding domain operation
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainVerifyResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainVerifyResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomains(
            self,
            request: models.DescribeDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainsResponse:
        """
        Query detailed information of all user domains
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFindDomainList(
            self,
            request: models.DescribeFindDomainListRequest,
            opts: Dict = None,
    ) -> models.DescribeFindDomainListResponse:
        """
        Obtain discovered domain name list API
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFindDomainList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFindDomainListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHistogram(
            self,
            request: models.DescribeHistogramRequest,
            opts: Dict = None,
    ) -> models.DescribeHistogramResponse:
        """
        Query various conditions of cluster analysis
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHistogram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHistogramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHost(
            self,
            request: models.DescribeHostRequest,
            opts: Dict = None,
    ) -> models.DescribeHostResponse:
        """
        Obtain protection domain details in CLB-WAF
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostLimit(
            self,
            request: models.DescribeHostLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeHostLimitResponse:
        """
        Firstly verify when adding a domain whether a package has been purchased, whether the limit of purchased package has not been reached, and whether the domain has already been added
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHosts(
            self,
            request: models.DescribeHostsRequest,
            opts: Dict = None,
    ) -> models.DescribeHostsResponse:
        """
        Obtain protection domain list in CLB-WAF
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        Query detailed information of all user instances
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpAccessControl(
            self,
            request: models.DescribeIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.DescribeIpAccessControlResponse:
        """
        WAF IP blocklist/allowlist query
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModuleStatus(
            self,
            request: models.DescribeModuleStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeModuleStatusResponse:
        """
        Query the switch status of each WAF basic security module, check if each module is enabled
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeObjects(
            self,
            request: models.DescribeObjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeObjectsResponse:
        """
        View protected object list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOwaspRuleTypes(
            self,
            request: models.DescribeOwaspRuleTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeOwaspRuleTypesResponse:
        """
        This API is used to query the rule types of the rule engine.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOwaspRuleTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOwaspRuleTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOwaspRules(
            self,
            request: models.DescribeOwaspRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeOwaspRulesResponse:
        """
        This API is used to query the rule list of the rule engine.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOwaspRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOwaspRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOwaspWhiteRules(
            self,
            request: models.DescribeOwaspWhiteRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeOwaspWhiteRulesResponse:
        """
        This API is used to retrieve the allowlist for the rule engine.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOwaspWhiteRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOwaspWhiteRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePeakPoints(
            self,
            request: models.DescribePeakPointsRequest,
            opts: Dict = None,
    ) -> models.DescribePeakPointsResponse:
        """
        Query business and attack summary trends
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePeakPoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePeakPointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyStatus(
            self,
            request: models.DescribePolicyStatusRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyStatusResponse:
        """
        Obtain protection status and the effective instance ID
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePorts(
            self,
            request: models.DescribePortsRequest,
            opts: Dict = None,
    ) -> models.DescribePortsResponse:
        """
        Obtain the SaaS-type WAF protection port list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePorts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePortsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleLimit(
            self,
            request: models.DescribeRuleLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleLimitResponse:
        """
        Obtain specific specification limits for each module
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSession(
            self,
            request: models.DescribeSessionRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionResponse:
        """
        WAF session definition query API
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpartaProtectionInfo(
            self,
            request: models.DescribeSpartaProtectionInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSpartaProtectionInfoResponse:
        """
        WAF Sparta - Obtain protection domain information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpartaProtectionInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpartaProtectionInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTlsVersion(
            self,
            request: models.DescribeTlsVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeTlsVersionResponse:
        """
        This API is used to query TLS versions supported by SaaS WAF.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTlsVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTlsVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopAttackDomain(
            self,
            request: models.DescribeTopAttackDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeTopAttackDomainResponse:
        """
        Query top 5 attack domains
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopAttackDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopAttackDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserClbWafRegions(
            self,
            request: models.DescribeUserClbWafRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeUserClbWafRegionsResponse:
        """
        During the addition and modification of Domain Configuration for CLB-type WAF, it is required to display the supported region list for CLB-type WAF (clb-waf) through DescribeUserClbWafRegions to obtain the currently available region list for the customer.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserClbWafRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserClbWafRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDomainInfo(
            self,
            request: models.DescribeUserDomainInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDomainInfoResponse:
        """
        Query Domain Information for SaaS and CLB
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDomainInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDomainInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserLevel(
            self,
            request: models.DescribeUserLevelRequest,
            opts: Dict = None,
    ) -> models.DescribeUserLevelResponse:
        """
        Obtain the user protection rule level
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVipInfo(
            self,
            request: models.DescribeVipInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVipInfoResponse:
        """
        Query VIP information based on filter criteria
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVipInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVipInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebshellStatus(
            self,
            request: models.DescribeWebshellStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeWebshellStatusResponse:
        """
        Obtain the webshell status of a domain
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebshellStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebshellStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FreshAntiFakeUrl(
            self,
            request: models.FreshAntiFakeUrlRequest,
            opts: Dict = None,
    ) -> models.FreshAntiFakeUrlResponse:
        """
        Refresh a tamper-proof URL
        """
        
        kwargs = {}
        kwargs["action"] = "FreshAntiFakeUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FreshAntiFakeUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateDealsAndPayNew(
            self,
            request: models.GenerateDealsAndPayNewRequest,
            opts: Dict = None,
    ) -> models.GenerateDealsAndPayNewResponse:
        """
        Billing Resource Purchase, Renewal Order API
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateDealsAndPayNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateDealsAndPayNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAttackHistogram(
            self,
            request: models.GetAttackHistogramRequest,
            opts: Dict = None,
    ) -> models.GetAttackHistogramResponse:
        """
        This API is used to generate a bar chart for the generation time of attack logs.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAttackHistogram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAttackHistogramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAttackTotalCount(
            self,
            request: models.GetAttackTotalCountRequest,
            opts: Dict = None,
    ) -> models.GetAttackTotalCountResponse:
        """
        Display total attack count by querying based on conditions
        """
        
        kwargs = {}
        kwargs["action"] = "GetAttackTotalCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAttackTotalCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetInstanceQpsLimit(
            self,
            request: models.GetInstanceQpsLimitRequest,
            opts: Dict = None,
    ) -> models.GetInstanceQpsLimitResponse:
        """
        Obtain the elastic QPS limit of package instances
        """
        
        kwargs = {}
        kwargs["action"] = "GetInstanceQpsLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetInstanceQpsLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportIpAccessControl(
            self,
            request: models.ImportIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.ImportIpAccessControlResponse:
        """
        This API is used to import IP allowlists/blocklists.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAntiFakeUrl(
            self,
            request: models.ModifyAntiFakeUrlRequest,
            opts: Dict = None,
    ) -> models.ModifyAntiFakeUrlResponse:
        """
        Edit a tamper-proof URL
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAntiFakeUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAntiFakeUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAntiFakeUrlStatus(
            self,
            request: models.ModifyAntiFakeUrlStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAntiFakeUrlStatusResponse:
        """
        Toggle tamper-proof switch
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAntiFakeUrlStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAntiFakeUrlStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAntiInfoLeakRuleStatus(
            self,
            request: models.ModifyAntiInfoLeakRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAntiInfoLeakRuleStatusResponse:
        """
        Information leakage prevention toggle rule switch
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAntiInfoLeakRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAntiInfoLeakRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAntiInfoLeakRules(
            self,
            request: models.ModifyAntiInfoLeakRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyAntiInfoLeakRulesResponse:
        """
        Edit an information leakage prevention rule
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAntiInfoLeakRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAntiInfoLeakRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiAnalyzeStatus(
            self,
            request: models.ModifyApiAnalyzeStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApiAnalyzeStatusResponse:
        """
        API analysis page switch
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiAnalyzeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiAnalyzeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBotStatus(
            self,
            request: models.ModifyBotStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBotStatusResponse:
        """
        Bot_V2 bot master switch update
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBotStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBotStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomRule(
            self,
            request: models.ModifyCustomRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomRuleResponse:
        """
        This API is used to edit a custom rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomRuleStatus(
            self,
            request: models.ModifyCustomRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomRuleStatusResponse:
        """
        Enable or disable access control (from custom policy)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomWhiteRule(
            self,
            request: models.ModifyCustomWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomWhiteRuleResponse:
        """
        This API is used to edit a precise allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomWhiteRuleStatus(
            self,
            request: models.ModifyCustomWhiteRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomWhiteRuleStatusResponse:
        """
        Enable or disable a precision allowlist
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomWhiteRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomWhiteRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainIpv6Status(
            self,
            request: models.ModifyDomainIpv6StatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainIpv6StatusResponse:
        """
        Toggle the IPv6 switch
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainIpv6Status"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainIpv6StatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainPostAction(
            self,
            request: models.ModifyDomainPostActionRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainPostActionResponse:
        """
        This API is used to modify the domain shipping status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainPostAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainPostActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainsCLSStatus(
            self,
            request: models.ModifyDomainsCLSStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainsCLSStatusResponse:
        """
        Enable or disable access log for domain list
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainsCLSStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainsCLSStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHost(
            self,
            request: models.ModifyHostRequest,
            opts: Dict = None,
    ) -> models.ModifyHostResponse:
        """
        This API is used to edit the configuration of domain names protected by CLB WAF.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostFlowMode(
            self,
            request: models.ModifyHostFlowModeRequest,
            opts: Dict = None,
    ) -> models.ModifyHostFlowModeResponse:
        """
        This API is used to set the traffic mode for domain names protected by CLB WAF. The mode can be mirror mode or cleaning mode.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostFlowMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostFlowModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostMode(
            self,
            request: models.ModifyHostModeRequest,
            opts: Dict = None,
    ) -> models.ModifyHostModeResponse:
        """
        Set CLB WAF protection domain status
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostStatus(
            self,
            request: models.ModifyHostStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyHostStatusResponse:
        """
        This API is used to enable or disable CLB WAF for a protected domain name.
        Batch operation is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceElasticMode(
            self,
            request: models.ModifyInstanceElasticModeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceElasticModeResponse:
        """
        Modify the QPS elastic billing switch for an instance
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceElasticMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceElasticModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceName(
            self,
            request: models.ModifyInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNameResponse:
        """
        Modify instance name
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceQpsLimit(
            self,
            request: models.ModifyInstanceQpsLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceQpsLimitResponse:
        """
        Set elastic QPS limit for package instances
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceQpsLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceQpsLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceRenewFlag(
            self,
            request: models.ModifyInstanceRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceRenewFlagResponse:
        """
        Enable or disable auto-renewal for instance
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIpAccessControl(
            self,
            request: models.ModifyIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.ModifyIpAccessControlResponse:
        """
        This API is used to edit WAF IP allowlists/blocklists.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleStatus(
            self,
            request: models.ModifyModuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleStatusResponse:
        """
        Set the switch for the basic security module under a certain domain
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyObject(
            self,
            request: models.ModifyObjectRequest,
            opts: Dict = None,
    ) -> models.ModifyObjectResponse:
        """
        Modify protection object
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwaspRuleStatus(
            self,
            request: models.ModifyOwaspRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyOwaspRuleStatusResponse:
        """
        This API is used to refresh the rule switch.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwaspRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwaspRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwaspRuleTypeAction(
            self,
            request: models.ModifyOwaspRuleTypeActionRequest,
            opts: Dict = None,
    ) -> models.ModifyOwaspRuleTypeActionResponse:
        """
        This API is used to update the protection mode of the rule type.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwaspRuleTypeAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwaspRuleTypeActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwaspRuleTypeLevel(
            self,
            request: models.ModifyOwaspRuleTypeLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyOwaspRuleTypeLevelResponse:
        """
        This API is used to update the protection level of a rule type.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwaspRuleTypeLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwaspRuleTypeLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwaspRuleTypeStatus(
            self,
            request: models.ModifyOwaspRuleTypeStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyOwaspRuleTypeStatusResponse:
        """
        This API is used to update the rule type switch.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwaspRuleTypeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwaspRuleTypeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwaspWhiteRule(
            self,
            request: models.ModifyOwaspWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyOwaspWhiteRuleResponse:
        """
        This API is used to edit the allowlist for the rule engine.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwaspWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwaspWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProtectionStatus(
            self,
            request: models.ModifyProtectionStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyProtectionStatusResponse:
        """
        This API is used to obtain the enabling status of the basic security protection module of WAF.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProtectionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProtectionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySpartaProtection(
            self,
            request: models.ModifySpartaProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifySpartaProtectionResponse:
        """
        This API is used to edit the configuration of domain names protected by SaaS WAF.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySpartaProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySpartaProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySpartaProtectionMode(
            self,
            request: models.ModifySpartaProtectionModeRequest,
            opts: Dict = None,
    ) -> models.ModifySpartaProtectionModeResponse:
        """
        Set WAF protection status
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySpartaProtectionMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySpartaProtectionModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserLevel(
            self,
            request: models.ModifyUserLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyUserLevelResponse:
        """
        Modify the user protection rule level
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserSignatureRule(
            self,
            request: models.ModifyUserSignatureRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyUserSignatureRuleResponse:
        """
        Modify user protection rules, turn on/off specific rules
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserSignatureRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserSignatureRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebshellStatus(
            self,
            request: models.ModifyWebshellStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyWebshellStatusResponse:
        """
        Set the Webshell status of a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebshellStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebshellStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshAccessCheckResult(
            self,
            request: models.RefreshAccessCheckResultRequest,
            opts: Dict = None,
    ) -> models.RefreshAccessCheckResultResponse:
        """
        Refresh integration check results. The backend will generate integration check tasks
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshAccessCheckResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshAccessCheckResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchAttackLog(
            self,
            request: models.SearchAttackLogRequest,
            opts: Dict = None,
    ) -> models.SearchAttackLogResponse:
        """
        The new version of the CLS API has parameter changes, with query changed to query_string to support Lucene syntax for API search queries.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchAttackLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchAttackLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchElasticMode(
            self,
            request: models.SwitchElasticModeRequest,
            opts: Dict = None,
    ) -> models.SwitchElasticModeResponse:
        """
        Toggle elasticity switch
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchElasticMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchElasticModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpsertCCRule(
            self,
            request: models.UpsertCCRuleRequest,
            opts: Dict = None,
    ) -> models.UpsertCCRuleResponse:
        """
        WAF CC V2 upsert API
        """
        
        kwargs = {}
        kwargs["action"] = "UpsertCCRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpsertCCRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpsertSession(
            self,
            request: models.UpsertSessionRequest,
            opts: Dict = None,
    ) -> models.UpsertSessionResponse:
        """
        WAF session definition upsert API
        """
        
        kwargs = {}
        kwargs["action"] = "UpsertSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpsertSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)