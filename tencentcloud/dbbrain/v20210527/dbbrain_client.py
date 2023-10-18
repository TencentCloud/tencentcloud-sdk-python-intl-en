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
from tencentcloud.dbbrain.v20210527 import models


class DbbrainClient(AbstractClient):
    _apiVersion = '2021-05-27'
    _endpoint = 'dbbrain.tencentcloudapi.com'
    _service = 'dbbrain'


    def AddUserContact(self, request):
        """This API is used to add the recipient name and email. The returned value is the ID of the successfully added recipient.

        :param request: Request instance for AddUserContact.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.AddUserContactRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.AddUserContactResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUserContact", params, headers=headers)
            response = json.loads(body)
            model = models.AddUserContactResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseAuditService(self, request):
        """This API is used to disable database audit as needed.

        :param request: Request instance for CloseAuditService.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CloseAuditServiceRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CloseAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.CloseAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBDiagReportTask(self, request):
        """This API is used to create a health report and send it via email as configured.

        :param request: Request instance for CreateDBDiagReportTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateDBDiagReportTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateDBDiagReportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBDiagReportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBDiagReportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBDiagReportUrl(self, request):
        """This API is used to create a URL for a health report.

        :param request: Request instance for CreateDBDiagReportUrl.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateDBDiagReportUrlRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateDBDiagReportUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBDiagReportUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBDiagReportUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKillTask(self, request):
        """This API is used to create a session killing task.

        :param request: Request instance for CreateKillTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateKillTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateKillTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKillTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKillTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMailProfile(self, request):
        """This API is used to create the email configuration. The input parameter `ProfileType` represents the type of the email configuration. Valid values: `dbScan_mail_configuration` (email configuration of database inspection report) and `scheduler_mail_configuration` (email sending configuration of scheduled task health report). Always select Guangzhou for `Region`, regardless of the region where the instance resides.

        :param request: Request instance for CreateMailProfile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateMailProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateMailProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMailProfile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMailProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProxySessionKillTask(self, request):
        """This API is used to create an async task of killing all proxy node connection sessions and is currently supported only for Redis. The async task ID is the returned value, which can be passed to the API `DescribeProxySessionKillTasks` as a parameter to query the execution status of the session killing task.

        :param request: Request instance for CreateProxySessionKillTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateProxySessionKillTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateProxySessionKillTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProxySessionKillTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProxySessionKillTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRedisBigKeyAnalysisTask(self, request):
        """This API is used to create an ad hoc big key analysis task for Redis instances. By default, there can only be up to five running ad hoc analysis tasks.

        :param request: Request instance for CreateRedisBigKeyAnalysisTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateRedisBigKeyAnalysisTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateRedisBigKeyAnalysisTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRedisBigKeyAnalysisTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRedisBigKeyAnalysisTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSchedulerMailProfile(self, request):
        """This API is used to create the regular generation time of health reports and the regular email sending configuration. Pass in the regular generation time of health reports as a parameter (Monday to Sunday) to set the regular generation time, and save the corresponding regular email sending configuration.

        :param request: Request instance for CreateSchedulerMailProfile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateSchedulerMailProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateSchedulerMailProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSchedulerMailProfile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSchedulerMailProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityAuditLogExportTask(self, request):
        """This API is used to create a security audit log export task.

        :param request: Request instance for CreateSecurityAuditLogExportTask.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.CreateSecurityAuditLogExportTaskRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.CreateSecurityAuditLogExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityAuditLogExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityAuditLogExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDBDiagReportTasks(self, request):
        """This API is used to delete health report generation tasks by task ID.

        :param request: Request instance for DeleteDBDiagReportTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DeleteDBDiagReportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DeleteDBDiagReportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDBDiagReportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDBDiagReportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityAuditLogExportTasks(self, request):
        """This API is used to delete a security audit log export task.

        :param request: Request instance for DeleteSecurityAuditLogExportTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DeleteSecurityAuditLogExportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DeleteSecurityAuditLogExportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityAuditLogExportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityAuditLogExportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllUserContact(self, request):
        """This API is used to get the information of the recipient in the email.

        :param request: Request instance for DescribeAllUserContact.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAllUserContactRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAllUserContactResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllUserContact", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllUserContactResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllUserGroup(self, request):
        """This API is used to get the information of the recipient group in the email.

        :param request: Request instance for DescribeAllUserGroup.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAllUserGroupRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAllUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditInstanceList(self, request):
        """This API is used to query the instance list.

        :param request: Request instance for DescribeAuditInstanceList.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAuditInstanceListRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeAuditInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBDiagEvent(self, request):
        """This API is used to get the details of an instance exception diagnosis event.

        :param request: Request instance for DescribeDBDiagEvent.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagEventRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBDiagEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBDiagEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBDiagEvents(self, request):
        """This API is used to obtain the diagnosis event list in a specified time period by risk level, instance ID, etc.

        :param request: Request instance for DescribeDBDiagEvents.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagEventsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBDiagEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBDiagEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBDiagHistory(self, request):
        """This API is used to get the list of instance diagnosis events.

        :param request: Request instance for DescribeDBDiagHistory.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagHistoryRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBDiagHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBDiagHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBDiagReportTasks(self, request):
        """This API is used to query the list of health report generation tasks.

        :param request: Request instance for DescribeDBDiagReportTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagReportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBDiagReportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBDiagReportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBDiagReportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSpaceStatus(self, request):
        """This API is used to query the overview of instance space usage during a specified time period, including disk usage growth (MB), available disk space (MB), total disk space (MB), and estimated number of available days.

        :param request: Request instance for DescribeDBSpaceStatus.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBSpaceStatusRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDBSpaceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSpaceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSpaceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiagDBInstances(self, request):
        """This API is used to get the instance information list. Please always select Guangzhou for `Region`.

        :param request: Request instance for DescribeDiagDBInstances.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDiagDBInstancesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeDiagDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiagDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiagDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHealthScore(self, request):
        """This API is used to get the health score and deduction for exceptions in the specified time period (30 minutes) based on the instance ID.

        :param request: Request instance for DescribeHealthScore.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeHealthScoreRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeHealthScoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHealthScore", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHealthScoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMailProfile(self, request):
        """This API is used to get the email sending configuration, including the email configuration for database inspection and the email sending configuration for scheduled task health reports.

        :param request: Request instance for DescribeMailProfile.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMailProfileRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMailProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMailProfile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMailProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMySqlProcessList(self, request):
        """This API is used to query the real-time thread list of a relational database.

        :param request: Request instance for DescribeMySqlProcessList.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMySqlProcessListRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeMySqlProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMySqlProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMySqlProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyProcessStatistics(self, request):
        """This API is used to get the session statistics of a single proxy under the current instance, and can only be called in particular environments.

        :param request: Request instance for DescribeProxyProcessStatistics.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeProxyProcessStatisticsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeProxyProcessStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyProcessStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyProcessStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxySessionKillTasks(self, request):
        """This API is used to query the result of the session killing task executed by the Redis proxy node. The async task ID (an input parameter) is obtained after the API `CreateProxySessionKillTask` is successfully called. Currently, the only valid value of `product` is `redis`.

        :param request: Request instance for DescribeProxySessionKillTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeProxySessionKillTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeProxySessionKillTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxySessionKillTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxySessionKillTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisTopKeyPrefixList(self, request):
        """This API is used to query the list of top key prefixes for Redis instances.

        :param request: Request instance for DescribeRedisTopKeyPrefixList.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisTopKeyPrefixListRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeRedisTopKeyPrefixListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisTopKeyPrefixList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisTopKeyPrefixListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityAuditLogDownloadUrls(self, request):
        """This API is used to query the download link of a security audit log export file. Currently, log file download only provides a Tencent Cloud private network address. Download it by using a CVM instance in the Guangzhou region.

        :param request: Request instance for DescribeSecurityAuditLogDownloadUrls.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSecurityAuditLogDownloadUrlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSecurityAuditLogDownloadUrlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityAuditLogDownloadUrls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityAuditLogDownloadUrlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityAuditLogExportTasks(self, request):
        """This API is used to query the list of security audit log export tasks.

        :param request: Request instance for DescribeSecurityAuditLogExportTasks.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSecurityAuditLogExportTasksRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSecurityAuditLogExportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityAuditLogExportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityAuditLogExportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogTimeSeriesStats(self, request):
        """This API is used to get the slow log statistics histogram.

        :param request: Request instance for DescribeSlowLogTimeSeriesStats.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogTimeSeriesStatsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogTimeSeriesStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogTimeSeriesStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogTimeSeriesStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogTopSqls(self, request):
        """This API is used to get and sort the top slow SQL statements in a specified time period by the aggregation mode of SQL template plus schema.

        :param request: Request instance for DescribeSlowLogTopSqls.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogTopSqlsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogTopSqlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogTopSqls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogTopSqlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogUserHostStats(self, request):
        """This API is used to get the statistical distribution chart of slow log source addresses.

        :param request: Request instance for DescribeSlowLogUserHostStats.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogUserHostStatsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogUserHostStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogUserHostStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogUserHostStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogs(self, request):
        """This API is used to obtain the slow log details of a SQL template in a specified time period.

        :param request: Request instance for DescribeSlowLogs.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopSpaceSchemaTimeSeries(self, request):
        """This API is used to get the daily space data of top databases consuming the most instance space. The data is daily collected by DBbrain during a specified time period. The returned results are sorted by size by default.

        :param request: Request instance for DescribeTopSpaceSchemaTimeSeries.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceSchemaTimeSeriesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceSchemaTimeSeriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopSpaceSchemaTimeSeries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopSpaceSchemaTimeSeriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopSpaceSchemas(self, request):
        """This API is used to get the real-time space statistics of top databases of an instance. The returned results are sorted by size by default.

        :param request: Request instance for DescribeTopSpaceSchemas.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceSchemasRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceSchemasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopSpaceSchemas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopSpaceSchemasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopSpaceTableTimeSeries(self, request):
        """This API is used to get the daily space data of top tables consuming the most instance space. The data is daily collected by DBbrain during a specified time period. The returned results are sorted by size by default.

        :param request: Request instance for DescribeTopSpaceTableTimeSeries.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceTableTimeSeriesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceTableTimeSeriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopSpaceTableTimeSeries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopSpaceTableTimeSeriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopSpaceTables(self, request):
        """This API is used to get the real-time space statistics of top tables of an instance. The returned results are sorted by size by default.

        :param request: Request instance for DescribeTopSpaceTables.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceTablesRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeTopSpaceTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopSpaceTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopSpaceTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserSqlAdvice(self, request):
        """This API is used to get SQL statement optimization suggestions. It is free of charge for a limited time and will be charged after DBbrain is commercialized.

        :param request: Request instance for DescribeUserSqlAdvice.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.DescribeUserSqlAdviceRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.DescribeUserSqlAdviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserSqlAdvice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserSqlAdviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillMySqlThreads(self, request):
        """This API is used to interrupt the current session by session ID. It needs to be called twice to commit the session interruption task in two stages. In the pre-commit stage, the stage value is `Prepare`, and the returned value is `SqlExecId`. In the commit stage, the stage value is `Commit`, and `SqlExecId` will be passed in as a parameter. Then, the session process will be terminated.

        :param request: Request instance for KillMySqlThreads.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.KillMySqlThreadsRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.KillMySqlThreadsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillMySqlThreads", params, headers=headers)
            response = json.loads(body)
            model = models.KillMySqlThreadsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditService(self, request):
        """u200cThis API is used to modify audit configurations such as the frequent access storage period.

        :param request: Request instance for ModifyAuditService.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.ModifyAuditServiceRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ModifyAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDiagDBInstanceConf(self, request):
        """This API is used to enable/disable instance inspection.

        :param request: Request instance for ModifyDiagDBInstanceConf.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.ModifyDiagDBInstanceConfRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ModifyDiagDBInstanceConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDiagDBInstanceConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDiagDBInstanceConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenAuditService(self, request):
        """This API is used to enable database audit.

        :param request: Request instance for OpenAuditService.
        :type request: :class:`tencentcloud.dbbrain.v20210527.models.OpenAuditServiceRequest`
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.OpenAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.OpenAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))