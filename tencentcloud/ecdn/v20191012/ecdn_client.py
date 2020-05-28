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
from tencentcloud.ecdn.v20191012 import models


class EcdnClient(AbstractClient):
    _apiVersion = '2019-10-12'
    _endpoint = 'ecdn.tencentcloudapi.com'


    def AddEcdnDomain(self, request):
        """This API is used to create an acceleration domain name.

        :param request: Request instance for AddEcdnDomain.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.AddEcdnDomainRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.AddEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEcdnDomainResponse()
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


    def DeleteEcdnDomain(self, request):
        """This API is used to delete a specified acceleration domain name. The acceleration domain name to be deleted must be in disabled status.

        :param request: Request instance for DeleteEcdnDomain.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DeleteEcdnDomainRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DeleteEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEcdnDomainResponse()
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


    def DescribeDomains(self, request):
        """This API is used to query the basic information of a CDN domain name, including the project ID, status, business type, creation time, update time, etc.

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainsResponse()
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


    def DescribeDomainsConfig(self, request):
        """This API is used to query the detailed configuration information of a CDN acceleration domain name.

        :param request: Request instance for DescribeDomainsConfig.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsConfigRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainsConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainsConfigResponse()
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


    def DescribeEcdnDomainLogs(self, request):
        """This API is used to query the access log download link of a domain name.

        :param request: Request instance for DescribeEcdnDomainLogs.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainLogsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEcdnDomainLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEcdnDomainLogsResponse()
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


    def DescribeEcdnDomainStatistics(self, request):
        """This API is used to query the statistical metrics of domain name access within a specified time period.

        :param request: Request instance for DescribeEcdnDomainStatistics.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainStatisticsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEcdnDomainStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEcdnDomainStatisticsResponse()
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


    def DescribeEcdnStatistics(self, request):
        """This API is used to query ECDN real-time access monitoring data and supports the following metrics:

        + Traffic (in bytes)
        + Bandwidth (in bps)
        + Number of requests
        + Response time (in ms)
        + Number of 2xx status codes and details of status codes starting with 2
        + Number of 3xx status codes and details of status codes starting with 3
        + Number of 4xx status codes and details of status codes starting with 4
        + Number of 5xx status codes and details of status codes starting with 5

        :param request: Request instance for DescribeEcdnStatistics.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnStatisticsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEcdnStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEcdnStatisticsResponse()
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


    def DescribePurgeQuota(self, request):
        """This API is used to query the usage quota of the purge API.

        :param request: Request instance for DescribePurgeQuota.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribePurgeQuotaRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribePurgeQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePurgeQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurgeQuotaResponse()
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
        """This API is used to query the submission history of purge tasks and their execution progress.

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribePurgeTasksResponse`

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


    def PurgePathCache(self, request):
        """This API is used to batch purge cache directories. One purge task ID will be returned for each submission.

        :param request: Request instance for PurgePathCache.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.PurgePathCacheRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.PurgePathCacheResponse`

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
        """This API is used to batch purge URLs. One purge task ID will be returned for each submission.

        :param request: Request instance for PurgeUrlsCache.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.PurgeUrlsCacheRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.PurgeUrlsCacheResponse`

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


    def StartEcdnDomain(self, request):
        """This API is used to enable an acceleration domain name. The domain name to be enabled must be in deactivated status.

        :param request: Request instance for StartEcdnDomain.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.StartEcdnDomainRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.StartEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartEcdnDomainResponse()
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


    def StopEcdnDomain(self, request):
        """This API is used to disable an acceleration domain name. The domain name to be disabled must be in enabled or deploying status.

        :param request: Request instance for StopEcdnDomain.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.StopEcdnDomainRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.StopEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopEcdnDomainResponse()
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


    def UpdateDomainConfig(self, request):
        """This API is used to update the configuration information of an ECDN acceleration domain name.
        Note: if you need to update a complex configuration item, you must pass in all attributes of the entire object, and the default values will be used for the attributes that are not passed in. You are recommended to get the configuration attribute through the query API first and then directly modify and pass it to this API. Due to the special nature of the certificate for HTTPS configuration, you do not need to pass in the certificate and key fields during the update.

        :param request: Request instance for UpdateDomainConfig.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.UpdateDomainConfigRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.UpdateDomainConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDomainConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDomainConfigResponse()
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