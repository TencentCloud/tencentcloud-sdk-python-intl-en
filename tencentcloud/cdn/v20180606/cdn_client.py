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
from tencentcloud.cdn.v20180606 import models


class CdnClient(AbstractClient):
    _apiVersion = '2018-06-06'
    _endpoint = 'cdn.intl.tencentcloudapi.com'
    _service = 'cdn'


    def AddCLSTopicDomains(self, request):
        """This API is used to add one or more domains to a specified log topic.

        :param request: Request instance for AddCLSTopicDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.AddCLSTopicDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AddCLSTopicDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCLSTopicDomains", params, headers=headers)
            response = json.loads(body)
            model = models.AddCLSTopicDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCdnDomain(self, request):
        """This API is used to add a CDN acceleration domain name. Up to 100 domain names can be added per minute.

        :param request: Request instance for AddCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.AddCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AddCdnDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCdnDomain", params, headers=headers)
            response = json.loads(body)
            model = models.AddCdnDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClsLogTopic(self, request):
        """This API is used to create a log topic. Up to 10 log topics can be created under one logset.

        :param request: Request instance for CreateClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClsLogTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClsLogTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScdnFailedLogTask(self, request):
        """This API is used to recreate a failed event log task.

        :param request: Request instance for CreateScdnFailedLogTask.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateScdnFailedLogTaskRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateScdnFailedLogTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScdnFailedLogTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScdnFailedLogTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCdnDomain(self, request):
        """This API is used to delete a specified acceleration domain name.

        :param request: Request instance for DeleteCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DeleteCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DeleteCdnDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCdnDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCdnDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClsLogTopic(self, request):
        """This API is used to delete a log topic. Note: when a log topic is deleted, all logs of the domain names bound to it will no longer be published to the topic, and the logs previously published to the topic will be deleted. This action will take effect within 5–15 minutes.

        :param request: Request instance for DeleteClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DeleteClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DeleteClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClsLogTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClsLogTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingData(self, request):
        """This API is used to query billing data details.

        :param request: Request instance for DescribeBillingData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeBillingDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeBillingDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdnData(self, request):
        """This API is used to query CDN real-time access monitoring data and supports the following metrics:

        + Traffic (in bytes)
        + Bandwidth (in bps)
        + Number of requests
        + Number of hit requests
        + Request hit rate (in %)
        + Hit traffic (in bytes)
        + Traffic hit rate (in %)
        + Aggregate list of 2xx status codes and the details of status codes starting with 2 (in entries)
        + Aggregate list of 3xx status codes and the details of status codes starting with 3 (in entries)
        + Aggregate list of 4xx status codes and the details of status codes starting with 4 (in entries)
        + Aggregate list of 5xx status codes and the details of status codes starting with 5 (in entries)

        :param request: Request instance for DescribeCdnData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdnData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdnDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdnDomainLogs(self, request):
        """This API is used to query the download link of an access log. You can use this API for access logs in the last 30 days either within or outside Mainland China.

        :param request: Request instance for DescribeCdnDomainLogs.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDomainLogsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDomainLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdnDomainLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdnDomainLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdnIp(self, request):
        """This API is used to query CDN IP ownership.

        :param request: Request instance for DescribeCdnIp.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnIpRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdnIp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdnIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdnOriginIp(self, request):
        """This API is used to query the IP information of CDN intermediate nodes. Note: this API will be deactivated soon and no longer be maintained. Please call `DescribeIpStatus` instead.

        :param request: Request instance for DescribeCdnOriginIp.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnOriginIpRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnOriginIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdnOriginIp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdnOriginIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertDomains(self, request):
        """This API is used to verify a SSL certificate and obtain its domain names.

        :param request: Request instance for DescribeCertDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCertDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCertDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomains(self, request):
        """This API is used to query the basic configuration information of CDN acceleration domain names (inside and outside mainland China), including the project ID, service status, service type, creation time, and update time, etc.

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsResponse`

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


    def DescribeDomainsConfig(self, request):
        """This API is used to query the complete configuration information of CDN acceleration domain names (inside and outside mainland China).

        :param request: Request instance for DescribeDomainsConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainsConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainsConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpStatus(self, request):
        """This API is used to query the IP details of edge nodes (available soon) and intermediate nodes. Note that there is a certain delay in data availability.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/api/228/41954?from_cn_redirect=1">corresponding CDN API</a>.

        :param request: Request instance for DescribeIpStatus.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeIpStatusRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeIpStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpVisit(self, request):
        """This API (DescribeIpVisit) is used to query the number of users who remain active for 5 minutes and the detailed number of daily active users.

        + Number of users who remain active for 5 minutes: Collects deduplicated statistics based on client IP addresses in the log with the 5-minute granularity.
        + Number of daily active users: Collects deduplicated statistics based on client IP addresses in the log with the 1-day granularity.

        :param request: Request instance for DescribeIpVisit.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeIpVisitRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeIpVisitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpVisit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpVisitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMapInfo(self, request):
        """This API (DescribeMapInfo) is used to query the IDs of districts or ISPs.

        :param request: Request instance for DescribeMapInfo.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeMapInfoRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeMapInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMapInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMapInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginData(self, request):
        """This API is used to query CDN real-time origin-pull monitoring data and supports the following metrics:

        + Origin-pull traffic (in bytes)
        + Origin-pull bandwidth (in bps)
        + Number of origin-pull requests
        + Number of failed origin-pull requests
        + Origin-pull failure rate (in % with two decimal digits)
        + Aggregate list of 2xx origin-pull status codes and the details of origin-pull status codes starting with 2 (in entries)
        + Aggregate list of 3xx origin-pull status codes and the details of origin-pull status codes starting with 3 (in entries)
        + Aggregate list of 4xx origin-pull status codes and the details of origin-pull status codes starting with 4 (in entries)
        + Aggregate list of 5xx origin-pull status codes and the details of origin-pull status codes starting with 5 (in entries)

        :param request: Request instance for DescribeOriginData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeOriginDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeOriginDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePayType(self, request):
        """This API (DescribePayType) is used to query billing information of the current account, such as billing mode and billing cycle.

        :param request: Request instance for DescribePayType.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePayTypeRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePayTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePayType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePayTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePurgeQuota(self, request):
        """This API is used to query the purge usage quota and daily available usage for an account.

        :param request: Request instance for DescribePurgeQuota.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeQuotaRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurgeQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePurgeQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePurgeTasks(self, request):
        """This API is used to query the record and progress of URL or directory purge tasks submitted via the `PurgePathCache` or `PurgeUrlsCache` APIs.

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeTasksResponse`

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


    def DescribePushQuota(self, request):
        """This API is used to query the prefetch quota and daily available usage.

        :param request: Request instance for DescribePushQuota.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePushQuotaRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePushQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePushQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePushQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePushTasks(self, request):
        """This API is used to query the submission record and progress of prefetch tasks.

        :param request: Request instance for DescribePushTasks.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePushTasksRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePushTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePushTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePushTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReportData(self, request):
        """This API is used to query the daily/weekly/monthly report data at domain name/project levels.

        :param request: Request instance for DescribeReportData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeReportDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeReportDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReportData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReportDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUrlViolations(self, request):
        """This API is used to query the list of domain name URLs containing regulation-violating content scanned and detected by the CDN system, and the current status of the URLs.
        It corresponds to the **Pornography Detection** page on the CDN Console.

        :param request: Request instance for DescribeUrlViolations.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeUrlViolationsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeUrlViolationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUrlViolations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUrlViolationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableCaches(self, request):
        """This API is used to block access to a specific URL on CDN. When a URL is blocked, error 403 will be returned for requests from the Chinese mainland. URL blocking is not permanent. Note that this API is only available to beta users now.

        :param request: Request instance for DisableCaches.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DisableCachesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DisableCachesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableCaches", params, headers=headers)
            response = json.loads(body)
            model = models.DisableCachesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableClsLogTopic(self, request):
        """This API is used to stop publishing to a log topic. Note: after a log topic is disabled, all logs of the domain names bound to it will no longer be published to the topic, and the logs that have already been published will be retained. This action will take effect within 5–15 minutes.

        :param request: Request instance for DisableClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DisableClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DisableClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableClsLogTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DisableClsLogTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableCaches(self, request):
        """This API (EnableCaches) is used to unblock manually blocked URLs. After a URL is successfully unblocked, it takes about 5 to 10 minutes to take effect across the entire network. (This API is during beta test and not fully available now.)

        :param request: Request instance for EnableCaches.
        :type request: :class:`tencentcloud.cdn.v20180606.models.EnableCachesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.EnableCachesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableCaches", params, headers=headers)
            response = json.loads(body)
            model = models.EnableCachesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableClsLogTopic(self, request):
        """This API is used to start publishing to a log topic. Note: after a log topic is enabled, all logs of the domain names bound to the topic will be published to it. This action will take effect within 5–15 minutes.

        :param request: Request instance for EnableClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.EnableClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.EnableClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableClsLogTopic", params, headers=headers)
            response = json.loads(body)
            model = models.EnableClsLogTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDisableRecords(self, request):
        """This API is used to query the resource blocking history and the current URL status. (This API is in beta test and not generally available yet.)

        :param request: Request instance for GetDisableRecords.
        :type request: :class:`tencentcloud.cdn.v20180606.models.GetDisableRecordsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.GetDisableRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDisableRecords", params, headers=headers)
            response = json.loads(body)
            model = models.GetDisableRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListClsLogTopics(self, request):
        """This API is used to display the list of log topics. Note: a logset can contain up to 10 log topics.

        :param request: Request instance for ListClsLogTopics.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListClsLogTopicsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListClsLogTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListClsLogTopics", params, headers=headers)
            response = json.loads(body)
            model = models.ListClsLogTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListClsTopicDomains(self, request):
        """This API is used to get the list of domain names bound to a log topic.

        :param request: Request instance for ListClsTopicDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListClsTopicDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListClsTopicDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListClsTopicDomains", params, headers=headers)
            response = json.loads(body)
            model = models.ListClsTopicDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTopData(self, request):
        """This API is used to list data sorted the following ways by using different combinations of the Metric and Filter input parameters:

        + It sorts access URLs by total traffic and total requests, and returns the top 1,000 URLs in descending order.
        + It sorts client districts by total traffic and total requests, and returns the list of districts in descending order.
        + It sorts client ISPs by total traffic and total requests, and returns the list of ISPs in descending order.
        + It sorts domain names by total traffic, peak bandwidth, total requests, average hit rate, and 2XX/3XX/4XX/5XX status codes, and returns the list of domain names in descending order.
        + It sorts domain names by total origin-pull traffic, peak origin-pull bandwidth, total origin-pull requests, average origin-pull failure rate, and 2XX/3XX/4XX/5XX origin-pull status codes, and returns the list of domain names in descending order.

        Note: only data from the last 90 days will be queried.

        :param request: Request instance for ListTopData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListTopDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTopData", params, headers=headers)
            response = json.loads(body)
            model = models.ListTopDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageClsTopicDomains(self, request):
        """This API is used to manage the list of domain names bound to a log topic.

        :param request: Request instance for ManageClsTopicDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ManageClsTopicDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ManageClsTopicDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageClsTopicDomains", params, headers=headers)
            response = json.loads(body)
            model = models.ManageClsTopicDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainConfig(self, request):
        """This API is used to modify the configuration of a CDN acceleration domain name in a finer manner than `UpdateDomainConfig`.
        Notes:
        In `Route`, separate values by dots (.). The last value is called a leaf node. For non-leaf nodes, keep the configuration unchanged.
        The Value field is serialized to a JSON string {key:value}, where **key** is fixed to `update` and **value** is used to specify the value of the configuration parameter. To specify configurations with complex types, see https://intl.cloud.tencent.com/document/product/228/41116.?from_cn_redirect=1
        The input parameters of this API are not reported to CloudAudit as it may contain sensitive data, such as keys and secrets.

        :param request: Request instance for ModifyDomainConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ModifyDomainConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ModifyDomainConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PurgePathCache(self, request):
        """This API is used to submit multiple directory purge tasks, which are carried out according to the acceleration region of the domain names.
        By default, a maximum of 100 directories can be purged per day for acceleration regions either within or outside the Chinese mainland, and up to 500 tasks can be submitted at a time.

        :param request: Request instance for PurgePathCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PurgePathCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PurgePathCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PurgePathCache", params, headers=headers)
            response = json.loads(body)
            model = models.PurgePathCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PurgeUrlsCache(self, request):
        """This API is used to submit multiple URL purge tasks, which are carried out according to the current acceleration region of the domain names in the URLs.
        By default, a maximum of 10,000 URLs can be purged per day for acceleration regions either within or outside Mainland China, and up to 1,000 tasks can be submitted at a time.

        :param request: Request instance for PurgeUrlsCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PurgeUrlsCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PurgeUrlsCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PurgeUrlsCache", params, headers=headers)
            response = json.loads(body)
            model = models.PurgeUrlsCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PushUrlsCache(self, request):
        """This API is used to cache specified URL resources to CDN nodes. You can specify acceleration regions for the prefetch.
        By default, a maximum of 1000 URLs can be prefetched per day for regions either within or outside the Chinese mainland, and up to 500 tasks can be submitted at a time. Note that resources prefetched outside the Chinese mainland will be cached to CDN nodes outside the Chinese mainland and the traffic generated will incur costs.

        :param request: Request instance for PushUrlsCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PushUrlsCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PushUrlsCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PushUrlsCache", params, headers=headers)
            response = json.loads(body)
            model = models.PushUrlsCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchClsLog(self, request):
        """This API is used to search for CLS logs. Search filters can be set to today, 24 hours (one of the last 7 days), and the last 7 days.

        :param request: Request instance for SearchClsLog.
        :type request: :class:`tencentcloud.cdn.v20180606.models.SearchClsLogRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.SearchClsLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchClsLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchClsLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartCdnDomain(self, request):
        """This API is used to enable the acceleration service for a disabled domain name.

        :param request: Request instance for StartCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.StartCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StartCdnDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartCdnDomain", params, headers=headers)
            response = json.loads(body)
            model = models.StartCdnDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCdnDomain(self, request):
        """This API is used to suspend the acceleration service for a domain name.
        Note: after the acceleration service has been suspended, requests to the cache node will return a 404 error. In order to avoid impact to your business, please move the domain name to another service before suspending the acceleration service.

        :param request: Request instance for StopCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.StopCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StopCdnDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCdnDomain", params, headers=headers)
            response = json.loads(body)
            model = models.StopCdnDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDomainConfig(self, request):
        """This API is used to modify the configuration of CDN acceleration domain names.
        Note: To update complex configuration items, all attributes of the object must be specified, or the default values are used. We recommend calling the querying API to get attributes before modifying and passing them to this API.
        The input parameters of this API are not reported to CloudAudit as it may contain sensitive data, such as keys and secrets.

        :param request: Request instance for UpdateDomainConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.UpdateDomainConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UpdateDomainConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDomainConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDomainConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdatePayType(self, request):
        """This API is used to modify the billing mode of an account. At present, the billing mode of accounts on a monthly billing cycle and sub-accounts cannot be modified.

        :param request: Request instance for UpdatePayType.
        :type request: :class:`tencentcloud.cdn.v20180606.models.UpdatePayTypeRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UpdatePayTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePayType", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePayTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateScdnDomain(self, request):
        """This API is used to modify security configurations of SCDN acceleration domain names.

        :param request: Request instance for UpdateScdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.UpdateScdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UpdateScdnDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateScdnDomain", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateScdnDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))