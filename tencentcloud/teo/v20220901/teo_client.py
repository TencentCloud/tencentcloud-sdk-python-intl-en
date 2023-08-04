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
from tencentcloud.teo.v20220901 import models


class TeoClient(AbstractClient):
    _apiVersion = '2022-09-01'
    _endpoint = 'teo.tencentcloudapi.com'
    _service = 'teo'


    def BindZoneToPlan(self, request):
        """This API is used to bind a site to a plan.

        :param request: Request instance for BindZoneToPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindZoneToPlan", params, headers=headers)
            response = json.loads(body)
            model = models.BindZoneToPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCnameStatus(self, request):
        """This API is used to query the CNAME status of a domain name.

        :param request: Request instance for CheckCnameStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.CheckCnameStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CheckCnameStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCnameStatus", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCnameStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccelerationDomain(self, request):
        """This API is used to connect a domain to EdgeOne.

        :param request: Request instance for CreateAccelerationDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateAccelerationDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateAccelerationDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccelerationDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccelerationDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAliasDomain(self, request):
        """This API is used to create an alias domain name.

        :param request: Request instance for CreateAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationProxy(self, request):
        """This API is used to create an application proxy.

        :param request: Request instance for CreateApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationProxyRule(self, request):
        """This API is used to create an application proxy rule.

        :param request: Request instance for CreateApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOriginGroup(self, request):
        """This API is used to create an origin group.

        :param request: Request instance for CreateOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePlanForZone(self, request):
        """This API is used to purchase a plan for a new site.

        :param request: Request instance for CreatePlanForZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlanForZone", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePlanForZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrefetchTask(self, request):
        """This API is used to create a pre-warming task.

        :param request: Request instance for CreatePrefetchTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrefetchTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrefetchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePurgeTask(self, request):
        """When there are resources updated on the origin with the TTL remaining valid, users cannot access the latest resources. In this case, you can purge the cache using this API. There are two methods: <li>Delete: This method deletes the node cache without verification and retrieves u200dthe latest resources from the origin when receiving a request.</li><li>Invalidate: This method marks the node cache as invalid and sends a request with the If-None-Match and If-Modified-Since headers to the origin. If the origin responses with 200, the latest resources are retrieved to be cached on the node. If a 304 response is returned, the latest resources are not cached on the node.

        </li>For more details, see [Cache Purge](https://intl.cloud.tencent.com/document/product/1552/70759?from_cn_redirect=1). </li>

        :param request: Request instance for CreatePurgeTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePurgeTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePurgeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        """This API is used to create a rule in the rule engine.

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityIPGroup(self, request):
        """This API is used to create a security IP group.

        :param request: Request instance for CreateSecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateZone(self, request):
        """This API is used to access a new site.

        :param request: Request instance for CreateZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateZone", params, headers=headers)
            response = json.loads(body)
            model = models.CreateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccelerationDomains(self, request):
        """This API is used to batch remove accelerated domain names.

        :param request: Request instance for DeleteAccelerationDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteAccelerationDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteAccelerationDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccelerationDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccelerationDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAliasDomain(self, request):
        """This API is used to delete an alias domain name.

        :param request: Request instance for DeleteAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationProxy(self, request):
        """This API is used to delete an application proxy.

        :param request: Request instance for DeleteApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationProxyRule(self, request):
        """This API is used to delete an application proxy rule.

        :param request: Request instance for DeleteApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOriginGroup(self, request):
        """This API is used to delete an origin group.

        :param request: Request instance for DeleteOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRules(self, request):
        """This API is used to batch delete rules from the rule engine.

        :param request: Request instance for DeleteRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityIPGroup(self, request):
        """This API is used to delete a specified security IP group. Note that the security IP group cannot be deleted if it is referenced in a rule.

        :param request: Request instance for DeleteSecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteZone(self, request):
        """This API is used to delete a site.

        :param request: Request instance for DeleteZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteZone", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccelerationDomains(self, request):
        """This API is used to query accelerated domain names. Paging, sorting and filtering are supported.

        :param request: Request instance for DescribeAccelerationDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAccelerationDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAccelerationDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccelerationDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccelerationDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAliasDomains(self, request):
        """This API is used to query the information of alias domain names.

        :param request: Request instance for DescribeAliasDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAliasDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAliasDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationProxies(self, request):
        """This API is used to query the list of application proxies.

        :param request: Request instance for DescribeApplicationProxies.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProxies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailablePlans(self, request):
        """This API is used to query plan options available for purchase.

        :param request: Request instance for DescribeAvailablePlans.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailablePlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailablePlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContentQuota(self, request):
        """This API is used to query content management quotas.

        :param request: Request instance for DescribeContentQuota.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContentQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackData(self, request):
        """This API is used to query the time-series data of DDoS attacks.

        :param request: Request instance for DescribeDDoSAttackData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackEvent(self, request):
        """This API is used to query DDoS attack events.

        :param request: Request instance for DescribeDDoSAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackTopData(self, request):
        """This API is used to query the top-ranked DDoS attack data.

        :param request: Request instance for DescribeDDoSAttackTopData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackTopData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackTopDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultCertificates(self, request):
        """This API is used to query a list of default certificates.

        :param request: Request instance for DescribeDefaultCertificates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostsSetting(self, request):
        """This API is used to query detailed domain name configuration.

        :param request: Request instance for DescribeHostsSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostsSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostsSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdentifications(self, request):
        """This API is used to query the verification information of a site.

        :param request: Request instance for DescribeIdentifications.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdentifications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdentificationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginGroup(self, request):
        """This API is used to obtain a list of origin groups.

        :param request: Request instance for DescribeOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginProtection(self, request):
        """This API is used to query the origin protection configuration.

        :param request: Request instance for DescribeOriginProtection.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginProtectionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewL7Data(self, request):
        """This API is used to query the L7 traffic summary statistics recorded over time.

        :param request: Request instance for DescribeOverviewL7Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewL7Data", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewL7DataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrefetchTasks(self, request):
        """This API is used to query the pre-warming task status.

        :param request: Request instance for DescribePrefetchTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrefetchTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrefetchTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePurgeTasks(self, request):
        """Querying the cache purging history

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurgeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePurgeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRules(self, request):
        """This API is used to query the rules in the rule engine.

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRulesSetting(self, request):
        """This API is used to return the list of the settings of the rule engine that can be used for request match and their detailed recommended configuration information.

        :param request: Request instance for DescribeRulesSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRulesSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL4Data(self, request):
        """This API is used to query the list of L4 traffic data recorded over time.

        :param request: Request instance for DescribeTimingL4Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL4Data", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL4DataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL7AnalysisData(self, request):
        """This API is used to query the L7 data recorded over time.

        :param request: Request instance for DescribeTimingL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL7AnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL7CacheData(self, request):
        """This API is used to query the time-series L7 cached data.

        :param request: Request instance for DescribeTimingL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7CacheData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL7CacheDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopL7AnalysisData(self, request):
        """This API is used to query the top-ranked L7 traffic data.

        :param request: Request instance for DescribeTopL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopL7AnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopL7CacheData(self, request):
        """This API is used to query the cached L7 top-ranked data.

        :param request: Request instance for DescribeTopL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7CacheData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopL7CacheDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneSetting(self, request):
        """This API is used to query the site configuration.

        :param request: Request instance for DescribeZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """This API is used to query the list of user sites.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadL4Logs(self, request):
        """This API is used to download L4 logs.

        :param request: Request instance for DownloadL4Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL4Logs", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadL4LogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadL7Logs(self, request):
        """This API is used to download L7 logs.

        :param request: Request instance for DownloadL7Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL7Logs", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadL7LogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IdentifyZone(self, request):
        """This API is used to verify ownership of the site.

        :param request: Request instance for IdentifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IdentifyZone", params, headers=headers)
            response = json.loads(body)
            model = models.IdentifyZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccelerationDomain(self, request):
        """This API is used to modify an accelerated domain name.

        :param request: Request instance for ModifyAccelerationDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccelerationDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccelerationDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccelerationDomainStatuses(self, request):
        """This API is used to batch modify the status of accelerated domains.

        :param request: Request instance for ModifyAccelerationDomainStatuses.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainStatusesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainStatusesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccelerationDomainStatuses", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccelerationDomainStatusesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAliasDomain(self, request):
        """This API is used to modify an alias domain name.

        :param request: Request instance for ModifyAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAliasDomainStatus(self, request):
        """This API is used to modify the status of an alias domain name.

        :param request: Request instance for ModifyAliasDomainStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomainStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAliasDomainStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxy(self, request):
        """This API is used to modify an application proxy.

        :param request: Request instance for ModifyApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyRule(self, request):
        """This API is used to modify an application proxy rule.

        :param request: Request instance for ModifyApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyRuleStatus(self, request):
        """This API is used to modify the status of an application proxy rule.

        :param request: Request instance for ModifyApplicationProxyRuleStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyStatus(self, request):
        """This API is used to modify the status of an application proxy.

        :param request: Request instance for ModifyApplicationProxyStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostsCertificate(self, request):
        """This API is used to modify the certificate of a domain name.

        :param request: Request instance for ModifyHostsCertificate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostsCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostsCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOriginGroup(self, request):
        """This API is used to modify an origin group.

        :param request: Request instance for ModifyOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRule(self, request):
        """This API is used to modify a rule in the rule engine.

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityIPGroup(self, request):
        """This API is used to modify a security IP group.

        :param request: Request instance for ModifySecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityPolicy(self, request):
        """This API is used to modify the web and bot security configurations.

        :param request: Request instance for ModifySecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZone(self, request):
        """This API is used to modify a site.

        :param request: Request instance for ModifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZone", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneSetting(self, request):
        """This API is used to modify the site configuration.

        :param request: Request instance for ModifyZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneStatus(self, request):
        """This API is used to change the site status.

        :param request: Request instance for ModifyZoneStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))