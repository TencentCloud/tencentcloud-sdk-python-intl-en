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
from tencentcloud.dbbrain.v20191016 import models


class DbbrainClient(AbstractClient):
    _apiVersion = '2019-10-16'
    _endpoint = 'dbbrain.tencentcloudapi.com'
    _service = 'dbbrain'


    def CreateDBDiagReportTask(self, request):
        """This API is used to create a health report and send it via email as configured.

        :param request: Request instance for CreateDBDiagReportTask.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.CreateDBDiagReportTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.CreateDBDiagReportTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBDiagReportTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBDiagReportTaskResponse()
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


    def CreateMailProfile(self, request):
        """This API is used to create the email configuration. The input parameter `ProfileType` represents the type of the email configuration. Valid values: `dbScan_mail_configuration` (email configuration of database inspection report) and `scheduler_mail_configuration` (email configuration of scheduled task report).

        :param request: Request instance for CreateMailProfile.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.CreateMailProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.CreateMailProfileResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMailProfile", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMailProfileResponse()
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


    def DescribeAllUserContact(self, request):
        """This API is used to obtain the information of the contact in the email.

        :param request: Request instance for DescribeAllUserContact.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeAllUserContactRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeAllUserContactResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAllUserContact", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAllUserContactResponse()
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


    def DescribeAllUserGroup(self, request):
        """This API is used to obtain the information of the contact group in the email.

        :param request: Request instance for DescribeAllUserGroup.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeAllUserGroupRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeAllUserGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAllUserGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAllUserGroupResponse()
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


    def DescribeDBDiagEvent(self, request):
        """This API is used to get the details of an instance exception diagnosis event.

        :param request: Request instance for DescribeDBDiagEvent.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagEventRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagEventResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBDiagEvent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBDiagEventResponse()
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


    def DescribeDBDiagHistory(self, request):
        """This API is used to get the list of instance diagnosis events.

        :param request: Request instance for DescribeDBDiagHistory.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagHistoryRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBDiagHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBDiagHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBDiagHistoryResponse()
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


    def DescribeDBSpaceStatus(self, request):
        """This API is used to query the overview of instance space usage during a specified time period, including disk usage growth (MB), available disk space (MB), total disk space (MB), and estimated number of available days.

        :param request: Request instance for DescribeDBSpaceStatus.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBSpaceStatusRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeDBSpaceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSpaceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSpaceStatusResponse()
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


    def DescribeSlowLogTimeSeriesStats(self, request):
        """This API is used to get the slow log statistics histogram.

        :param request: Request instance for DescribeSlowLogTimeSeriesStats.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTimeSeriesStatsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTimeSeriesStatsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogTimeSeriesStats", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogTimeSeriesStatsResponse()
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


    def DescribeSlowLogTopSqls(self, request):
        """This API is used to get and sort the top slow SQL statements in a specified time period by the aggregation mode of SQL template plus schema.

        :param request: Request instance for DescribeSlowLogTopSqls.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTopSqlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeSlowLogTopSqlsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogTopSqls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogTopSqlsResponse()
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


    def DescribeTopSpaceTableTimeSeries(self, request):
        """This API is used to query the daily space data of top tables consuming the most instance space. The data is daily collected by DBbrain during a specified time period. The return results are sorted by size by default.

        :param request: Request instance for DescribeTopSpaceTableTimeSeries.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceTableTimeSeriesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceTableTimeSeriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopSpaceTableTimeSeries", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopSpaceTableTimeSeriesResponse()
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


    def DescribeTopSpaceTables(self, request):
        """This API is used to query real-time space statistics of top tables of an instance. The return results are sorted by size by default.

        :param request: Request instance for DescribeTopSpaceTables.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceTablesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.DescribeTopSpaceTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopSpaceTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopSpaceTablesResponse()
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


    def ModifyDiagDBInstanceConf(self, request):
        """This API is used to enable/disable instance inspection.

        :param request: Request instance for ModifyDiagDBInstanceConf.
        :type request: :class:`tencentcloud.dbbrain.v20191016.models.ModifyDiagDBInstanceConfRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20191016.models.ModifyDiagDBInstanceConfResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDiagDBInstanceConf", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDiagDBInstanceConfResponse()
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