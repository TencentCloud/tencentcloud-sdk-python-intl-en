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
from tencentcloud.rum.v20210622 import models


class RumClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'rum.tencentcloudapi.com'
    _service = 'rum'


    def CreateLogExport(self, request):
        """API domain name: `rum.tencentcloudapi.com`.

        This API is used to create a log download task.

        Default API request rate limit: 20 requests/sec.

        :param request: Request instance for CreateLogExport.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateLogExportRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateLogExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLogExportResponse()
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


    def CreateOfflineLogConfig(self, request):
        """This API is used to create an offline log listener to report offline logs of particular users.

        :param request: Request instance for CreateOfflineLogConfig.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateOfflineLogConfigRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateOfflineLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOfflineLogConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateOfflineLogConfigResponse()
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


    def CreateProject(self, request):
        """This API is used to create a project (owned by the specified team).

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProjectResponse()
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


    def CreateReleaseFile(self, request):
        """This API is used to create a file record for the specified project.

        :param request: Request instance for CreateReleaseFile.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateReleaseFileRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateReleaseFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReleaseFile", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReleaseFileResponse()
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


    def CreateStarProject(self, request):
        """This API is used to add a starred project.

        :param request: Request instance for CreateStarProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateStarProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateStarProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStarProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStarProjectResponse()
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


    def CreateTawInstance(self, request):
        """This API is used to create a RUM instance.

        :param request: Request instance for CreateTawInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateTawInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateTawInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTawInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTawInstanceResponse()
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


    def CreateWhitelist(self, request):
        """This API is used to create an allowlist.

        :param request: Request instance for CreateWhitelist.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateWhitelistRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWhitelist", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWhitelistResponse()
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


    def DeleteInstance(self, request):
        """This API is used to delete an instance. The deleted instance cannot be recovered.

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteInstanceResponse()
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


    def DeleteLogExport(self, request):
        """API domain name: `rum.tencentcloudapi.com`.

        This API is used to delete a log download task.

        Default API request rate limit: 20 requests/sec.

        :param request: Request instance for DeleteLogExport.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteLogExportRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteLogExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLogExportResponse()
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


    def DeleteOfflineLogConfig(self, request):
        """This API is used to delete an offline RUM log listener. Then, offline logs of particular users will not be reported.

        :param request: Request instance for DeleteOfflineLogConfig.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteOfflineLogConfigRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteOfflineLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOfflineLogConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteOfflineLogConfigResponse()
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


    def DeleteOfflineLogRecord(self, request):
        """This API is used to delete an offline log record.

        :param request: Request instance for DeleteOfflineLogRecord.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteOfflineLogRecordRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteOfflineLogRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOfflineLogRecord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteOfflineLogRecordResponse()
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


    def DeleteProject(self, request):
        """This API is used to delete the specified RUM project.

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProjectResponse()
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


    def DeleteReleaseFile(self, request):
        """This API is used to delete the specified sourcemap file.

        :param request: Request instance for DeleteReleaseFile.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteReleaseFileRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteReleaseFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReleaseFile", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReleaseFileResponse()
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


    def DeleteStarProject(self, request):
        """This API is used to delete a starred project for the specified user.

        :param request: Request instance for DeleteStarProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteStarProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteStarProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStarProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteStarProjectResponse()
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


    def DeleteWhitelist(self, request):
        """This API is used to delete an allowlist.

        :param request: Request instance for DeleteWhitelist.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteWhitelistRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWhitelist", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWhitelistResponse()
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


    def DescribeData(self, request):
        """This API is used to query the forwarding monitor.

        :param request: Request instance for DescribeData.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataResponse()
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


    def DescribeDataCustomUrl(self, request):
        """This API is used to get the DescribeDataCustomUrl information.

        :param request: Request instance for DescribeDataCustomUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataCustomUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataCustomUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataCustomUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataCustomUrlResponse()
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


    def DescribeDataEventUrl(self, request):
        """This API is used to get the DescribeDataEventUrl information.

        :param request: Request instance for DescribeDataEventUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataEventUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataEventUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEventUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataEventUrlResponse()
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


    def DescribeDataFetchProject(self, request):
        """This API is used to get the DescribeDataFetchProject information.

        :param request: Request instance for DescribeDataFetchProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFetchProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataFetchProjectResponse()
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


    def DescribeDataFetchUrl(self, request):
        """This API is used to get the DescribeDataFetchUrl information.

        :param request: Request instance for DescribeDataFetchUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFetchUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataFetchUrlResponse()
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


    def DescribeDataFetchUrlInfo(self, request):
        """This API is used to get the DescribeDataFetchUrlInfo information.

        :param request: Request instance for DescribeDataFetchUrlInfo.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlInfoRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFetchUrlInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataFetchUrlInfoResponse()
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


    def DescribeDataLogUrlInfo(self, request):
        """This API is used to get the loginfo information.

        :param request: Request instance for DescribeDataLogUrlInfo.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlInfoRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataLogUrlInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataLogUrlInfoResponse()
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


    def DescribeDataLogUrlStatistics(self, request):
        """This API is used to get the LogUrlStatistics information.

        :param request: Request instance for DescribeDataLogUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataLogUrlStatistics", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataLogUrlStatisticsResponse()
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


    def DescribeDataPerformancePage(self, request):
        """This API is used to get the PerformancePage information.

        :param request: Request instance for DescribeDataPerformancePage.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformancePageRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformancePageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPerformancePage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataPerformancePageResponse()
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


    def DescribeDataPerformanceProject(self, request):
        """This API is used to get the PerformanceProject information.

        :param request: Request instance for DescribeDataPerformanceProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformanceProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformanceProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPerformanceProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataPerformanceProjectResponse()
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


    def DescribeDataPvUrlInfo(self, request):
        """This API is used to get the PvUrlInfo information.

        :param request: Request instance for DescribeDataPvUrlInfo.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlInfoRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPvUrlInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataPvUrlInfoResponse()
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


    def DescribeDataPvUrlStatistics(self, request):
        """This API is used to get the DescribeDataPvUrlStatistics information.

        :param request: Request instance for DescribeDataPvUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPvUrlStatistics", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataPvUrlStatisticsResponse()
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


    def DescribeDataReportCount(self, request):
        """This API is used to get the number of reported data entries for a project.

        :param request: Request instance for DescribeDataReportCount.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataReportCountRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataReportCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataReportCount", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataReportCountResponse()
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


    def DescribeDataSetUrlStatistics(self, request):
        """This API is used to get the DescribeDataSetUrlStatistics information.

        :param request: Request instance for DescribeDataSetUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataSetUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataSetUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSetUrlStatistics", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataSetUrlStatisticsResponse()
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


    def DescribeDataStaticProject(self, request):
        """This API is used to get the DescribeDataStaticProject information.

        :param request: Request instance for DescribeDataStaticProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataStaticProjectResponse()
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


    def DescribeDataStaticResource(self, request):
        """This API is used to get the DescribeDataStaticResource information.

        :param request: Request instance for DescribeDataStaticResource.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticResourceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticResource", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataStaticResourceResponse()
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


    def DescribeDataStaticUrl(self, request):
        """This API is used to get the DescribeDataStaticUrl information.

        :param request: Request instance for DescribeDataStaticUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataStaticUrlResponse()
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


    def DescribeDataWebVitalsPage(self, request):
        """This API is used to get the DescribeDataWebVitalsPage information, which is about core user activities.
        It includes the Web Vitals metric for the page loading performance.

        :param request: Request instance for DescribeDataWebVitalsPage.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataWebVitalsPageRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataWebVitalsPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataWebVitalsPage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataWebVitalsPageResponse()
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


    def DescribeError(self, request):
        """This API is used to get the homepage error information.

        :param request: Request instance for DescribeError.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeErrorRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeErrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeError", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeErrorResponse()
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


    def DescribeLogExports(self, request):
        """API domain name: `rum.tencentcloudapi.com`.

        This API is used to get the list of log download tasks.

        Default API request rate limit: 20 requests/sec.

        :param request: Request instance for DescribeLogExports.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeLogExportsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeLogExportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogExports", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogExportsResponse()
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


    def DescribeLogList(self, request):
        """This API is used to get the list of logs in a project (created by an instance).

        :param request: Request instance for DescribeLogList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeLogListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogListResponse()
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


    def DescribeOfflineLogConfigs(self, request):
        """This API is used to get the configuration of the set offline log listener and return the unique user ID.

        :param request: Request instance for DescribeOfflineLogConfigs.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogConfigsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineLogConfigs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOfflineLogConfigsResponse()
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


    def DescribeOfflineLogRecords(self, request):
        """This API is used to get all (up to 100) offline log records.

        :param request: Request instance for DescribeOfflineLogRecords.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogRecordsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineLogRecords", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOfflineLogRecordsResponse()
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


    def DescribeOfflineLogs(self, request):
        """This API is used to get the specified offline log.

        :param request: Request instance for DescribeOfflineLogs.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineLogs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOfflineLogsResponse()
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


    def DescribeProjectLimits(self, request):
        """This API is used to get the list of project reporting rates.

        :param request: Request instance for DescribeProjectLimits.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeProjectLimitsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeProjectLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectLimits", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectLimitsResponse()
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


    def DescribeProjects(self, request):
        """This API is used to get the list of projects (under teams created by an instance).

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectsResponse()
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


    def DescribePvList(self, request):
        """This API is used to get the list of PVs under a project.

        :param request: Request instance for DescribePvList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribePvListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribePvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePvList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePvListResponse()
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


    def DescribeReleaseFileSign(self, request):
        """This API is used to get the temporary key for uploaded file storage.

        :param request: Request instance for DescribeReleaseFileSign.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFileSignRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFileSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseFileSign", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReleaseFileSignResponse()
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


    def DescribeReleaseFiles(self, request):
        """This API is used to get the list of sourcemap files of a project.

        :param request: Request instance for DescribeReleaseFiles.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFilesRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseFiles", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReleaseFilesResponse()
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


    def DescribeScores(self, request):
        """This API is used to get the list of homepage scores.

        :param request: Request instance for DescribeScores.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeScoresRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeScoresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScores", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScoresResponse()
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


    def DescribeTawAreas(self, request):
        """This API is used to query region information.

        :param request: Request instance for DescribeTawAreas.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTawAreasRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTawAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTawAreas", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTawAreasResponse()
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


    def DescribeUvList(self, request):
        """This API is used to get the list of UVs under a project.

        :param request: Request instance for DescribeUvList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeUvListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeUvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUvList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUvListResponse()
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


    def DescribeWhitelists(self, request):
        """This API is used to get the list of allowlists.

        :param request: Request instance for DescribeWhitelists.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeWhitelistsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeWhitelistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhitelists", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWhitelistsResponse()
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


    def ModifyInstance(self, request):
        """This API is used to modify an instance.

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceResponse()
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


    def ModifyProject(self, request):
        """This API is used to modify a RUM project.

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProjectResponse()
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


    def ModifyProjectLimit(self, request):
        """This API is used to add or modify data reporting limit.

        :param request: Request instance for ModifyProjectLimit.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyProjectLimitRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyProjectLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProjectLimit", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProjectLimitResponse()
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


    def ResumeInstance(self, request):
        """This API is used to resume an instance.

        :param request: Request instance for ResumeInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.ResumeInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ResumeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeInstanceResponse()
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


    def StopInstance(self, request):
        """This API is used to stop an instance.

        :param request: Request instance for StopInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.StopInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.StopInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopInstanceResponse()
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