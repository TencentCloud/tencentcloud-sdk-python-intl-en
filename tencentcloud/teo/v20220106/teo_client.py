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
from tencentcloud.teo.v20220106 import models


class TeoClient(AbstractClient):
    _apiVersion = '2022-01-06'
    _endpoint = 'teo.tencentcloudapi.com'
    _service = 'teo'


    def CheckCertificate(self, request):
        """This API is used to verify a certificate.

        :param request: Request instance for CheckCertificate.
        :type request: :class:`tencentcloud.teo.v20220106.models.CheckCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CheckCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCertificateResponse()
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
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyResponse`

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
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyRuleResponse`

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


    def CreateApplicationProxyRules(self, request):
        """This API is used to batch create application proxy rules.

        :param request: Request instance for CreateApplicationProxyRules.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxyRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationProxyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomErrorPage(self, request):
        """This API is used to create a custom error page.

        :param request: Request instance for CreateCustomErrorPage.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateCustomErrorPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateCustomErrorPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomErrorPage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomErrorPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDnsRecord(self, request):
        """This API is used to create a DNS record.

        :param request: Request instance for CreateDnsRecord.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateDnsRecordRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateDnsRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDnsRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDnsRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoadBalancing(self, request):
        """This API is used to create a CLB instance.

        :param request: Request instance for CreateLoadBalancing.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateLoadBalancingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadBalancing", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoadBalancingResponse()
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
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateOriginGroupResponse`

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


    def CreatePrefetchTask(self, request):
        """This API is used to create a pre-warming task.

        :param request: Request instance for CreatePrefetchTask.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreatePrefetchTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreatePrefetchTaskResponse`

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
        """This API is used to create a cache purging task.

        :param request: Request instance for CreatePurgeTask.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreatePurgeTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreatePurgeTaskResponse`

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


    def CreateZone(self, request):
        """This API is used to access a new site.

        :param request: Request instance for CreateZone.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateZoneResponse`

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


    def DeleteApplicationProxy(self, request):
        """This API is used to delete an application proxy.

        :param request: Request instance for DeleteApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteApplicationProxyResponse`

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
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteApplicationProxyRuleResponse`

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


    def DeleteDnsRecords(self, request):
        """This API is used to batch delete DNS records.

        :param request: Request instance for DeleteDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDnsRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDnsRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancing(self, request):
        """This API is used to delete a CLB instance.

        :param request: Request instance for DeleteLoadBalancing.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteLoadBalancingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancing", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancingResponse()
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
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteOriginGroupResponse`

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


    def DeleteZone(self, request):
        """This API is used to delete a site.

        :param request: Request instance for DeleteZone.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteZoneResponse`

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


    def DescribeApplicationProxy(self, request):
        """This API is used to obtain a list of application proxies.

        :param request: Request instance for DescribeApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationProxyDetail(self, request):
        """This API is used to obtain the details of an application proxy.

        :param request: Request instance for DescribeApplicationProxyDetail.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeApplicationProxyDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeApplicationProxyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProxyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationProxyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBotLog(self, request):
        """This API is used to query bot attack logs.

        :param request: Request instance for DescribeBotLog.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeBotLogRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeBotLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBotLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBotManagedRules(self, request):
        """This API is used to query bot managed rules.

        :param request: Request instance for DescribeBotManagedRules.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeBotManagedRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeBotManagedRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotManagedRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBotManagedRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCnameStatus(self, request):
        """This API is used to query the CNAME status of a domain name.

        :param request: Request instance for DescribeCnameStatus.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeCnameStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeCnameStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCnameStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCnameStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSPolicy(self, request):
        """This API is used to query the DDoS protection configuration.

        :param request: Request instance for DescribeDDoSPolicy.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDosAttackData(self, request):
        """This API is used to query the DDoS attack data.

        :param request: Request instance for DescribeDDosAttackData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosAttackData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDosAttackDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDosAttackEvent(self, request):
        """This API is used to query DDoS attack events.

        :param request: Request instance for DescribeDDosAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosAttackEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDosAttackEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDosAttackEventDetail(self, request):
        """This API is used to query DDoS attack event details.

        :param request: Request instance for DescribeDDosAttackEventDetail.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackEventDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosAttackEventDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDosAttackEventDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDosAttackSourceEvent(self, request):
        """This API is used to query DDoS attack sources.

        :param request: Request instance for DescribeDDosAttackSourceEvent.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackSourceEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackSourceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosAttackSourceEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDosAttackSourceEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDosAttackTopData(self, request):
        """This API is used to query the top data of DDoS attacks.

        :param request: Request instance for DescribeDDosAttackTopData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosAttackTopData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDosAttackTopDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDosMajorAttackEvent(self, request):
        """This API is used to query the major DDoS attack event.

        :param request: Request instance for DescribeDDosMajorAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosMajorAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosMajorAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosMajorAttackEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDosMajorAttackEventResponse()
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
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDefaultCertificatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDefaultCertificatesResponse`

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


    def DescribeDnsData(self, request):
        """This API is used to obtain collected DNS requests.

        :param request: Request instance for DescribeDnsData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDnsDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDnsDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnsData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDnsDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDnsRecords(self, request):
        """This API is used to query DNS records. Paging, sorting and filtering are supported.

        :param request: Request instance for DescribeDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnsRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDnsRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDnssec(self, request):
        """This API is used to query DNSSEC information.

        :param request: Request instance for DescribeDnssec.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDnssecRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDnssecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnssec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDnssecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostsCertificate(self, request):
        """This API is used to query certificates of domain names. Paging, sorting and filtering are supported.

        :param request: Request instance for DescribeHostsCertificate.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeHostsCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeHostsCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostsCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostsCertificateResponse()
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
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeHostsSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeHostsSettingResponse`

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


    def DescribeIdentification(self, request):
        """This API is used to query verification results.

        :param request: Request instance for DescribeIdentification.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeIdentificationRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeIdentificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdentification", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdentificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancing(self, request):
        """This API is used to obtain a list of CLB instances.

        :param request: Request instance for DescribeLoadBalancing.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeLoadBalancingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancing", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancingDetail(self, request):
        """This API is used to query the details of a CLB instance.

        :param request: Request instance for DescribeLoadBalancingDetail.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeLoadBalancingDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeLoadBalancingDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancingDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancingDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginGroup(self, request):
        """This API is used to get the list of origin groups.

        :param request: Request instance for DescribeOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeOriginGroupResponse`

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


    def DescribeOriginGroupDetail(self, request):
        """This API is used to get the details of the origin group.

        :param request: Request instance for DescribeOriginGroupDetail.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeOriginGroupDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeOriginGroupDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginGroupDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginGroupDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewL7Data(self, request):
        """This API is used to query the layer-7 time series traffic data for monitoring.

        :param request: Request instance for DescribeOverviewL7Data.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeOverviewL7DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeOverviewL7DataResponse`

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
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribePrefetchTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribePrefetchTasksResponse`

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
        """This API is used to query the cache purging history.

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribePurgeTasksResponse`

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


    def DescribeSecurityPolicy(self, request):
        """This API is used to query the security protection configuration.

        :param request: Request instance for DescribeSecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicyList(self, request):
        """This API is used to query all protected subdomain names.

        :param request: Request instance for DescribeSecurityPolicyList.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyListRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicyManagedRules(self, request):
        """This API is used to query managed rules.

        :param request: Request instance for DescribeSecurityPolicyManagedRules.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyManagedRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyManagedRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyManagedRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyManagedRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicyManagedRulesId(self, request):
        """This API is used to query the details of a managed rule by rule ID.

        :param request: Request instance for DescribeSecurityPolicyManagedRulesId.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyManagedRulesIdRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyManagedRulesIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyManagedRulesId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyManagedRulesIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicyRegions(self, request):
        """This API is used to query information of all regions.

        :param request: Request instance for DescribeSecurityPolicyRegions.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyRegionsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPortraitRules(self, request):
        """This API is used to query user profiling rules.

        :param request: Request instance for DescribeSecurityPortraitRules.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPortraitRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPortraitRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPortraitRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPortraitRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL4Data(self, request):
        """This API is used to query the layer-4 time series traffic data.

        :param request: Request instance for DescribeTimingL4Data.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL4DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL4DataResponse`

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
        """This API is used to query the layer-7 time series traffic data for data analysis.

        :param request: Request instance for DescribeTimingL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL7AnalysisDataResponse`

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
        """This API is used to query time-series L7 cached data.

        :param request: Request instance for DescribeTimingL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL7CacheDataResponse`

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
        """This API is used to query the top traffic data.

        :param request: Request instance for DescribeTopL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeTopL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeTopL7AnalysisDataResponse`

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
        """This API is used to query the top-ranked L7 cached data.

        :param request: Request instance for DescribeTopL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeTopL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeTopL7CacheDataResponse`

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


    def DescribeWebManagedRulesAttackEvents(self, request):
        """This API is used to query web hosting attack events.

        :param request: Request instance for DescribeWebManagedRulesAttackEvents.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesAttackEventsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesAttackEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesAttackEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebManagedRulesAttackEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebManagedRulesData(self, request):
        """This API is used to query the web hosting rule data.

        :param request: Request instance for DescribeWebManagedRulesData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebManagedRulesDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebManagedRulesLog(self, request):
        """This API is used to query web hosting logs.

        :param request: Request instance for DescribeWebManagedRulesLog.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesLogRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebManagedRulesLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebManagedRulesTopData(self, request):
        """This API is used to query the top data of web hosting rules.

        :param request: Request instance for DescribeWebManagedRulesTopData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesTopData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebManagedRulesTopDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebProtectionAttackEvents(self, request):
        """This API is used to query web attack events.

        :param request: Request instance for DescribeWebProtectionAttackEvents.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionAttackEventsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionAttackEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionAttackEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebProtectionAttackEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebProtectionData(self, request):
        """This API is used to query the web protection data.

        :param request: Request instance for DescribeWebProtectionData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebProtectionDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebProtectionLog(self, request):
        """This API is used to query web protection logs.

        :param request: Request instance for DescribeWebProtectionLog.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionLogRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebProtectionLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneDDoSPolicy(self, request):
        """This API is used to query all DDoS mitigation configuration.

        :param request: Request instance for DescribeZoneDDoSPolicy.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeZoneDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeZoneDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneDDoSPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneDDoSPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneDetails(self, request):
        """This API is used to query the details of a site by site ID.

        :param request: Request instance for DescribeZoneDetails.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeZoneDetailsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeZoneDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneDetailsResponse()
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
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeZoneSettingResponse`

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
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeZonesResponse`

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


    def DownloadL7Logs(self, request):
        """This API is used to query layer-7 logs.

        :param request: Request instance for DownloadL7Logs.
        :type request: :class:`tencentcloud.teo.v20220106.models.DownloadL7LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DownloadL7LogsResponse`

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
        :type request: :class:`tencentcloud.teo.v20220106.models.IdentifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.IdentifyZoneResponse`

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


    def ImportDnsRecords(self, request):
        """This API is used to import DNS records.

        :param request: Request instance for ImportDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220106.models.ImportDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ImportDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportDnsRecords", params, headers=headers)
            response = json.loads(body)
            model = models.ImportDnsRecordsResponse()
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
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyResponse`

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
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyRuleResponse`

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
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyRuleStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyRuleStatusResponse`

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
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyStatusResponse`

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


    def ModifyDDoSPolicy(self, request):
        """This API is used to modify DDoS mitigation configuration.

        :param request: Request instance for ModifyDDoSPolicy.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDDoSPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDDoSPolicyHost(self, request):
        """This API is used to enable high availability for domain names.

        :param request: Request instance for ModifyDDoSPolicyHost.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyDDoSPolicyHostRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyDDoSPolicyHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSPolicyHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDDoSPolicyHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDefaultCertificate(self, request):
        """This API is used to modify the status of a default certificate.

        :param request: Request instance for ModifyDefaultCertificate.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyDefaultCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyDefaultCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDefaultCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDefaultCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDnsRecord(self, request):
        """This API is used to modify DNS records.

        :param request: Request instance for ModifyDnsRecord.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyDnsRecordRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyDnsRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDnsRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDnsRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDnssec(self, request):
        """This API is used to modify the DNSSEC status.

        :param request: Request instance for ModifyDnssec.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyDnssecRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyDnssecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDnssec", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDnssecResponse()
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
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyHostsCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyHostsCertificateResponse`

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


    def ModifyLoadBalancing(self, request):
        """This API is used to modify a CLB instance.

        :param request: Request instance for ModifyLoadBalancing.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyLoadBalancingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancing", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancingStatus(self, request):
        """This API is used to modify the status of a CLB instance.

        :param request: Request instance for ModifyLoadBalancingStatus.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyLoadBalancingStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyLoadBalancingStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancingStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancingStatusResponse()
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
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyOriginGroupResponse`

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


    def ModifySecurityPolicy(self, request):
        """This API is used to modify the web and bot security configurations.

        :param request: Request instance for ModifySecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifySecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifySecurityPolicyResponse`

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
        """This API is used to modify the site information.

        :param request: Request instance for ModifyZone.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyZoneResponse`

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


    def ModifyZoneCnameSpeedUp(self, request):
        """This API is used to modify the CNAME acceleration status.

        :param request: Request instance for ModifyZoneCnameSpeedUp.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyZoneCnameSpeedUpRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyZoneCnameSpeedUpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneCnameSpeedUp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneCnameSpeedUpResponse()
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
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyZoneSettingResponse`

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
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyZoneStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyZoneStatusResponse`

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


    def ReclaimZone(self, request):
        """This API is used to reclaim a site from other users after its ownership is verified.

        :param request: Request instance for ReclaimZone.
        :type request: :class:`tencentcloud.teo.v20220106.models.ReclaimZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ReclaimZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReclaimZone", params, headers=headers)
            response = json.loads(body)
            model = models.ReclaimZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanDnsRecords(self, request):
        """This API is used to scan resolution records.

        :param request: Request instance for ScanDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220106.models.ScanDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ScanDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanDnsRecords", params, headers=headers)
            response = json.loads(body)
            model = models.ScanDnsRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))