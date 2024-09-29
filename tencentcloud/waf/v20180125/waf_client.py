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
from tencentcloud.waf.v20180125 import models


class WafClient(AbstractClient):
    _apiVersion = '2018-01-25'
    _endpoint = 'waf.tencentcloudapi.com'
    _service = 'waf'


    def AddAntiFakeUrl(self, request):
        """Add tamper-proof URL

        :param request: Request instance for AddAntiFakeUrl.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddAntiFakeUrlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddAntiFakeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAntiFakeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.AddAntiFakeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddAntiInfoLeakRules(self, request):
        """Add information leakage prevention rule

        :param request: Request instance for AddAntiInfoLeakRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddAntiInfoLeakRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddAntiInfoLeakRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAntiInfoLeakRules", params, headers=headers)
            response = json.loads(body)
            model = models.AddAntiInfoLeakRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCustomRule(self, request):
        """Add access control (from custom policy)

        :param request: Request instance for AddCustomRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddCustomRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddCustomRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCustomRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddCustomRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddSpartaProtection(self, request):
        """Add SaaS WAF protection domain

        :param request: Request instance for AddSpartaProtection.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddSpartaProtectionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddSpartaProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddSpartaProtection", params, headers=headers)
            response = json.loads(body)
            model = models.AddSpartaProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeals(self, request):
        """Billing Resource Purchase, Renewal Order API

        :param request: Request instance for CreateDeals.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateDealsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateDealsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeals", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDealsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHost(self, request):
        """Add a protection domain in CLB-WAF

        :param request: Request instance for CreateHost.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateHostRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHost", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAntiFakeUrl(self, request):
        """Delete tamper-proof URL

        :param request: Request instance for DeleteAntiFakeUrl.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteAntiFakeUrlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteAntiFakeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAntiFakeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAntiFakeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAntiInfoLeakRule(self, request):
        """Delete information leakage prevention rule

        :param request: Request instance for DeleteAntiInfoLeakRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteAntiInfoLeakRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteAntiInfoLeakRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAntiInfoLeakRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAntiInfoLeakRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCCRule(self, request):
        """WAF CC V2 deletion API

        :param request: Request instance for DeleteCCRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteCCRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteCCRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCCRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCCRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomRule(self, request):
        """Delete custom rule

        :param request: Request instance for DeleteCustomRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteCustomRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteCustomRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHost(self, request):
        """This API is used to delete a domain name protected by CLB WAF. Batch operation is supported.

        :param request: Request instance for DeleteHost.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteHostRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHost", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSpartaProtection(self, request):
        """This API is used to delete a domain name protected by SaaS WAF.

        :param request: Request instance for DeleteSpartaProtection.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteSpartaProtectionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteSpartaProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSpartaProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSpartaProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAntiFakeRules(self, request):
        """Obtain a tamper-proof URL

        :param request: Request instance for DescribeAntiFakeRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAntiFakeRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAntiFakeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAntiFakeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAntiFakeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAntiFakeUrl(self, request):
        """废弃接口

        This API has been deprecated.

        Obtain a tamper-proof URL

        :param request: Request instance for DescribeAntiFakeUrl.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAntiFakeUrlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAntiFakeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAntiFakeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAntiFakeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAntiInfoLeakRules(self, request):
        """老接口已经不再使用。

        The old API is no longer in use.

        Obtain the information leakage prevention rule list

        :param request: Request instance for DescribeAntiInfoLeakRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAntiInfoLeakRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAntiInfoLeakRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAntiInfoLeakRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAntiInfoLeakRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAntiInfoLeakageRules(self, request):
        """Obtain the information leakage prevention rule list

        :param request: Request instance for DescribeAntiInfoLeakageRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAntiInfoLeakageRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAntiInfoLeakageRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAntiInfoLeakageRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAntiInfoLeakageRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackType(self, request):
        """Query the top N attack types for a specified domain

        :param request: Request instance for DescribeAttackType.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAttackTypeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAttackTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchIpAccessControl(self, request):
        """This API is used to query the IP blocklist and allowlist for WAF batch protection.

        :param request: Request instance for DescribeBatchIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeBatchIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeBatchIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCRule(self, request):
        """WAF CC V2 query API

        :param request: Request instance for DescribeCCRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCCRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCCRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCRuleList(self, request):
        """Query CC rules based on multiple conditions

        :param request: Request instance for DescribeCCRuleList.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCCRuleListRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCCRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificateVerifyResult(self, request):
        """Obtain certificate inspection result

        :param request: Request instance for DescribeCertificateVerifyResult.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCertificateVerifyResultRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCertificateVerifyResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateVerifyResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateVerifyResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCiphersDetail(self, request):
        """Query SaaS WAF cipher suite information

        :param request: Request instance for DescribeCiphersDetail.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCiphersDetailRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCiphersDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCiphersDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCiphersDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomRuleList(self, request):
        """Obtain the access control policy list in the protection configuration

        :param request: Request instance for DescribeCustomRuleList.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCustomRuleListRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCustomRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainCountInfo(self, request):
        """Obtain domain overview

        :param request: Request instance for DescribeDomainCountInfo.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainCountInfoRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainCountInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainCountInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainCountInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainDetailsClb(self, request):
        """Obtain CLB WAF domain details

        :param request: Request instance for DescribeDomainDetailsClb.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainDetailsClbRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainDetailsClbResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainDetailsClb", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainDetailsClbResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainDetailsSaas(self, request):
        """Query individual SaaS WAF domain details

        :param request: Request instance for DescribeDomainDetailsSaas.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainDetailsSaasRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainDetailsSaasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainDetailsSaas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainDetailsSaasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomains(self, request):
        """Query detailed information of all user domains

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFindDomainList(self, request):
        """Obtain discovered domain name list API

        :param request: Request instance for DescribeFindDomainList.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeFindDomainListRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeFindDomainListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFindDomainList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFindDomainListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHistogram(self, request):
        """Query various conditions of cluster analysis

        :param request: Request instance for DescribeHistogram.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeHistogramRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeHistogramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistogram", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistogramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHost(self, request):
        """Obtain protection domain details in CLB-WAF

        :param request: Request instance for DescribeHost.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeHostRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostLimit(self, request):
        """Firstly verify when adding a domain whether a package has been purchased, whether the limit of purchased package has not been reached, and whether the domain has already been added

        :param request: Request instance for DescribeHostLimit.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeHostLimitRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeHostLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHosts(self, request):
        """Obtain protection domain list in CLB-WAF

        :param request: Request instance for DescribeHosts.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeHostsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHosts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModuleStatus(self, request):
        """Query the switch status of each WAF basic security module, check if each module is enabled

        :param request: Request instance for DescribeModuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeModuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeModuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeObjects(self, request):
        """View protected object list

        :param request: Request instance for DescribeObjects.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeObjectsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeObjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeObjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePeakPoints(self, request):
        """Query business and attack summary trends

        :param request: Request instance for DescribePeakPoints.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribePeakPointsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribePeakPointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePeakPoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePeakPointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePolicyStatus(self, request):
        """Obtain protection status and the effective instance ID

        :param request: Request instance for DescribePolicyStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribePolicyStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribePolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleLimit(self, request):
        """Obtain specific specification limits for each module

        :param request: Request instance for DescribeRuleLimit.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeRuleLimitRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeRuleLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSession(self, request):
        """WAF session definition query API

        :param request: Request instance for DescribeSession.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeSessionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpartaProtectionInfo(self, request):
        """WAF Sparta - Obtain protection domain information

        :param request: Request instance for DescribeSpartaProtectionInfo.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeSpartaProtectionInfoRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeSpartaProtectionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpartaProtectionInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpartaProtectionInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTlsVersion(self, request):
        """This API is used to query TLS versions supported by SaaS WAF.

        :param request: Request instance for DescribeTlsVersion.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeTlsVersionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeTlsVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTlsVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTlsVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopAttackDomain(self, request):
        """Query top 5 attack domains

        :param request: Request instance for DescribeTopAttackDomain.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeTopAttackDomainRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeTopAttackDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopAttackDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopAttackDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserDomainInfo(self, request):
        """Query Domain Information for SaaS and CLB

        :param request: Request instance for DescribeUserDomainInfo.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeUserDomainInfoRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeUserDomainInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDomainInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDomainInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserLevel(self, request):
        """Obtain the user protection rule level

        :param request: Request instance for DescribeUserLevel.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeUserLevelRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeUserLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserLevel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserLevelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVipInfo(self, request):
        """Query VIP information based on filter criteria

        :param request: Request instance for DescribeVipInfo.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeVipInfoRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeVipInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVipInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVipInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebshellStatus(self, request):
        """Obtain the webshell status of a domain

        :param request: Request instance for DescribeWebshellStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeWebshellStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeWebshellStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebshellStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebshellStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreshAntiFakeUrl(self, request):
        """Refresh a tamper-proof URL

        :param request: Request instance for FreshAntiFakeUrl.
        :type request: :class:`tencentcloud.waf.v20180125.models.FreshAntiFakeUrlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.FreshAntiFakeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreshAntiFakeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.FreshAntiFakeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateDealsAndPayNew(self, request):
        """Billing Resource Purchase, Renewal Order API

        :param request: Request instance for GenerateDealsAndPayNew.
        :type request: :class:`tencentcloud.waf.v20180125.models.GenerateDealsAndPayNewRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.GenerateDealsAndPayNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateDealsAndPayNew", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateDealsAndPayNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAttackTotalCount(self, request):
        """Display total attack count by querying based on conditions

        :param request: Request instance for GetAttackTotalCount.
        :type request: :class:`tencentcloud.waf.v20180125.models.GetAttackTotalCountRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.GetAttackTotalCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAttackTotalCount", params, headers=headers)
            response = json.loads(body)
            model = models.GetAttackTotalCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAntiFakeUrl(self, request):
        """Edit a tamper-proof URL

        :param request: Request instance for ModifyAntiFakeUrl.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAntiFakeUrlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAntiFakeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAntiFakeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAntiFakeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAntiFakeUrlStatus(self, request):
        """Toggle tamper-proof switch

        :param request: Request instance for ModifyAntiFakeUrlStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAntiFakeUrlStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAntiFakeUrlStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAntiFakeUrlStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAntiFakeUrlStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAntiInfoLeakRuleStatus(self, request):
        """Information leakage prevention toggle rule switch

        :param request: Request instance for ModifyAntiInfoLeakRuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAntiInfoLeakRuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAntiInfoLeakRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAntiInfoLeakRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAntiInfoLeakRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAntiInfoLeakRules(self, request):
        """Edit an information leakage prevention rule

        :param request: Request instance for ModifyAntiInfoLeakRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAntiInfoLeakRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAntiInfoLeakRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAntiInfoLeakRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAntiInfoLeakRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApiAnalyzeStatus(self, request):
        """API analysis page switch

        :param request: Request instance for ModifyApiAnalyzeStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyApiAnalyzeStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyApiAnalyzeStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiAnalyzeStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiAnalyzeStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBotStatus(self, request):
        """Bot_V2 bot master switch update

        :param request: Request instance for ModifyBotStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyBotStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyBotStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBotStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBotStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomRule(self, request):
        """This API is used to edit a custom rule.

        :param request: Request instance for ModifyCustomRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyCustomRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyCustomRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomRuleStatus(self, request):
        """Enable or disable access control (from custom policy)

        :param request: Request instance for ModifyCustomRuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyCustomRuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyCustomRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomWhiteRuleStatus(self, request):
        """Enable or disable a precision allowlist

        :param request: Request instance for ModifyCustomWhiteRuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyCustomWhiteRuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyCustomWhiteRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomWhiteRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomWhiteRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainIpv6Status(self, request):
        """Toggle the IPv6 switch

        :param request: Request instance for ModifyDomainIpv6Status.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyDomainIpv6StatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyDomainIpv6StatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainIpv6Status", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainIpv6StatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainsCLSStatus(self, request):
        """Enable or disable access log for domain list

        :param request: Request instance for ModifyDomainsCLSStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyDomainsCLSStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyDomainsCLSStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainsCLSStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainsCLSStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHost(self, request):
        """This API is used to edit the configuration of domain names protected by CLB WAF.

        :param request: Request instance for ModifyHost.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyHostRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostFlowMode(self, request):
        """This API is used to set the traffic mode for domain names protected by CLB WAF. The mode can be mirror mode or cleaning mode.

        :param request: Request instance for ModifyHostFlowMode.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyHostFlowModeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyHostFlowModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostFlowMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostFlowModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostMode(self, request):
        """Set CLB WAF protection domain status

        :param request: Request instance for ModifyHostMode.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyHostModeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyHostModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostStatus(self, request):
        """This API is used to enable or disable CLB WAF for a protected domain name.
        Batch operation is supported.

        :param request: Request instance for ModifyHostStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyHostStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyHostStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModuleStatus(self, request):
        """Set the switch for the basic security module under a certain domain

        :param request: Request instance for ModifyModuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyModuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyModuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyObject(self, request):
        """Modify protection object

        :param request: Request instance for ModifyObject.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyObjectRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyObject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProtectionStatus(self, request):
        """This API is used to obtain the enabling status of the basic security protection module of WAF.

        :param request: Request instance for ModifyProtectionStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyProtectionStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyProtectionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProtectionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProtectionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySpartaProtection(self, request):
        """This API is used to edit the configuration of domain names protected by SaaS WAF.

        :param request: Request instance for ModifySpartaProtection.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifySpartaProtectionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifySpartaProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySpartaProtection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySpartaProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySpartaProtectionMode(self, request):
        """Set WAF protection status

        :param request: Request instance for ModifySpartaProtectionMode.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifySpartaProtectionModeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifySpartaProtectionModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySpartaProtectionMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySpartaProtectionModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserLevel(self, request):
        """Modify the user protection rule level

        :param request: Request instance for ModifyUserLevel.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyUserLevelRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyUserLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserLevel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserLevelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserSignatureRule(self, request):
        """Modify user protection rules, turn on/off specific rules

        :param request: Request instance for ModifyUserSignatureRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyUserSignatureRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyUserSignatureRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserSignatureRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserSignatureRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebshellStatus(self, request):
        """Set the Webshell status of a domain.

        :param request: Request instance for ModifyWebshellStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyWebshellStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyWebshellStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebshellStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebshellStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshAccessCheckResult(self, request):
        """Refresh integration check results. The backend will generate integration check tasks

        :param request: Request instance for RefreshAccessCheckResult.
        :type request: :class:`tencentcloud.waf.v20180125.models.RefreshAccessCheckResultRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.RefreshAccessCheckResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshAccessCheckResult", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshAccessCheckResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpsertCCRule(self, request):
        """WAF CC V2 upsert API

        :param request: Request instance for UpsertCCRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.UpsertCCRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.UpsertCCRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpsertCCRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpsertCCRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpsertSession(self, request):
        """WAF session definition upsert API

        :param request: Request instance for UpsertSession.
        :type request: :class:`tencentcloud.waf.v20180125.models.UpsertSessionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.UpsertSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpsertSession", params, headers=headers)
            response = json.loads(body)
            model = models.UpsertSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))