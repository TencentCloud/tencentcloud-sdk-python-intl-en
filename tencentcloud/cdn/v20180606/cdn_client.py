# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
    _endpoint = 'cdn.tencentcloudapi.com'


    def DescribeCdnData(self, request):
        """This API (DescribeCdnData) is used to query CDN real-time access monitoring data and supports the following metrics:

        + Traffic (in bytes)
        + Bandwidth (in bps)
        + Number of requests
        + Traffic hit rate (in % with two decimal digits)
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
            body = self.call("DescribeCdnData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCdnDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCdnDomainLogs(self, request):
        """This API is used to query the download link of an access log. You can use this API for access logs in the last 30 days either within or outside Mainland China.

        :param request: Request instance for DescribeCdnDomainLogs.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDomainLogsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDomainLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCdnDomainLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCdnDomainLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCdnIp(self, request):
        """This API is used to query CDN IP ownership.

        :param request: Request instance for DescribeCdnIp.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnIpRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCdnIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCdnIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DescribeIpVisit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpVisitResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMapInfo(self, request):
        """This API (DescribeMapInfo) is used to query the IDs of districts or ISPs.

        :param request: Request instance for DescribeMapInfo.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeMapInfoRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeMapInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMapInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMapInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOriginData(self, request):
        """This API (DescribeOriginData) is used to query CDN real-time origin-pull monitoring data and supports the following metrics:

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
            body = self.call("DescribeOriginData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOriginDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePayType(self, request):
        """This API (DescribePayType) is used to query billing information of the current account, such as billing mode and billing cycle.

        :param request: Request instance for DescribePayType.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePayTypeRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePayTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePayType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePayTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePurgeTasks(self, request):
        """This API is used to query the record and progress of URL or directory purge tasks submitted via the `PurgePathCache` or `PurgeUrlsCache` APIs.

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePurgeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurgeTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePushTasks(self, request):
        """This API is used to query the submission record and progress of prefetch tasks.
        This API is in beta test and not fully available yet. Please stay tuned.

        :param request: Request instance for DescribePushTasks.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePushTasksRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePushTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePushTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePushTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableCaches(self, request):
        """This API (DisableCaches) is used to block access to a specific URL on CDN. After a URL is blocked, error 403 will be returned for all access requests to it. (This API is during beta test and not fully available now.)

        :param request: Request instance for DisableCaches.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DisableCachesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DisableCachesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableCaches", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableCachesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableCaches(self, request):
        """This API (EnableCaches) is used to unblock manually blocked URLs. After a URL is successfully unblocked, it takes about 5 to 10 minutes to take effect across the entire network. (This API is during beta test and not fully available now.)

        :param request: Request instance for EnableCaches.
        :type request: :class:`tencentcloud.cdn.v20180606.models.EnableCachesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.EnableCachesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableCaches", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableCachesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDisableRecords(self, request):
        """This API (GetDisableRecords) is used to query the resource blocking history and the current URL status. (This API is during beta test and not fully available now.)

        :param request: Request instance for GetDisableRecords.
        :type request: :class:`tencentcloud.cdn.v20180606.models.GetDisableRecordsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.GetDisableRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDisableRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDisableRecordsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListTopData(self, request):
        """This API (ListTopData) is used to query the following sorting data by using different combinations of the `Metric` and `Filter` input parameters:

        + Sorts access URLs by total traffic and total requests and returns top 1,000 URLs in descending order.
        + Sorts client districts by total traffic and total requests and returns the list of districts in descending order.
        + Sorts client ISPs by total traffic and total requests and returns the list of ISPs in descending order.
        + Sorts domain names by total traffic, peak bandwidth, total requests, average hit rate, and 2XX/3XX/4XX/5XX status codes and returns the list of domain names in descending order.
        + Sorts domain names by total origin-pull traffic, peak origin-pull bandwidth, total origin-pull requests, average origin-pull failure rate, and 2XX/3XX/4XX/5XX origin-pull status codes and returns the list of domain names in descending order.

        :param request: Request instance for ListTopData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListTopDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListTopDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListTopData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTopDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PurgePathCache(self, request):
        """This API is used to submit multiple directory purge tasks, which are carried out according to the acceleration region of the domain names.
        By default, a maximum of 100 directories can be purged per day for acceleration regions either within or outside Mainland China, and up to 20 tasks can be submitted at a time.

        :param request: Request instance for PurgePathCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PurgePathCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PurgePathCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PurgePathCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PurgePathCacheResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PurgeUrlsCache(self, request):
        """This API is used to submit multiple URL purge tasks, which are carried out according to the current acceleration region of the domain names in the URLs.
        By default, a maximum of 10,000 URLs can be purged per day for acceleration regions either within or outside Mainland China, and up to 1,000 tasks can be submitted at a time.

        :param request: Request instance for PurgeUrlsCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PurgeUrlsCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PurgeUrlsCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PurgeUrlsCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PurgeUrlsCacheResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PushUrlsCache(self, request):
        """This API is used to cache specified URL resources to CDN nodes. You can specify acceleration regions for the prefetch.
        By default, a maximum of 1,000 URLs can be prefetched per day either within or outside Mainland China, and up to 20 tasks can be submitted at a time.
        This API is in beta test and not fully available yet. Please stay tuned.

        :param request: Request instance for PushUrlsCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PushUrlsCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PushUrlsCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PushUrlsCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PushUrlsCacheResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)