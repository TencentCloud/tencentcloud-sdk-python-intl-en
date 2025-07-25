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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.pts.v20210728 import models


class PtsClient(AbstractClient):
    _apiVersion = '2021-07-28'
    _endpoint = 'pts.intl.tencentcloudapi.com'
    _service = 'pts'


    def AbortCronJobs(self, request):
        """This API is used to stop cron jobs.

        :param request: Request instance for AbortCronJobs.
        :type request: :class:`tencentcloud.pts.v20210728.models.AbortCronJobsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.AbortCronJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AbortCronJobs", params, headers=headers)
            response = json.loads(body)
            model = models.AbortCronJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AbortJob(self, request):
        """This API is used to stop test job.

        :param request: Request instance for AbortJob.
        :type request: :class:`tencentcloud.pts.v20210728.models.AbortJobRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.AbortJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AbortJob", params, headers=headers)
            response = json.loads(body)
            model = models.AbortJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AdjustJobSpeed(self, request):
        """This API is used to adjust the target RPS of a job.

        :param request: Request instance for AdjustJobSpeed.
        :type request: :class:`tencentcloud.pts.v20210728.models.AdjustJobSpeedRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.AdjustJobSpeedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AdjustJobSpeed", params, headers=headers)
            response = json.loads(body)
            model = models.AdjustJobSpeedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyScenario(self, request):
        """This API is used to copy a scenario.

        :param request: Request instance for CopyScenario.
        :type request: :class:`tencentcloud.pts.v20210728.models.CopyScenarioRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.CopyScenarioResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyScenario", params, headers=headers)
            response = json.loads(body)
            model = models.CopyScenarioResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlertChannel(self, request):
        """This API is used to create an alert recipient group.

        :param request: Request instance for CreateAlertChannel.
        :type request: :class:`tencentcloud.pts.v20210728.models.CreateAlertChannelRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.CreateAlertChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlertChannel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlertChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCronJob(self, request):
        """This API is used to create a cron job.

        :param request: Request instance for CreateCronJob.
        :type request: :class:`tencentcloud.pts.v20210728.models.CreateCronJobRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.CreateCronJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCronJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCronJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEnvironment(self, request):
        """This API is used to create an environment.

        :param request: Request instance for CreateEnvironment.
        :type request: :class:`tencentcloud.pts.v20210728.models.CreateEnvironmentRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.CreateEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFile(self, request):
        """This API is used to create a file.

        :param request: Request instance for CreateFile.
        :type request: :class:`tencentcloud.pts.v20210728.models.CreateFileRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.CreateFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProject(self, request):
        """This API is used to create a project.

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.pts.v20210728.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScenario(self, request):
        """This API is used to create a scenario.

        :param request: Request instance for CreateScenario.
        :type request: :class:`tencentcloud.pts.v20210728.models.CreateScenarioRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.CreateScenarioResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScenario", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScenarioResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAlertChannel(self, request):
        """This API is used to delete an alert recipient group.

        :param request: Request instance for DeleteAlertChannel.
        :type request: :class:`tencentcloud.pts.v20210728.models.DeleteAlertChannelRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DeleteAlertChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlertChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlertChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCronJobs(self, request):
        """This API is used to delete cron jobs.

        :param request: Request instance for DeleteCronJobs.
        :type request: :class:`tencentcloud.pts.v20210728.models.DeleteCronJobsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DeleteCronJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCronJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCronJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEnvironments(self, request):
        """This API is used to delete environments.

        :param request: Request instance for DeleteEnvironments.
        :type request: :class:`tencentcloud.pts.v20210728.models.DeleteEnvironmentsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DeleteEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFiles(self, request):
        """This API is used to delete files.

        :param request: Request instance for DeleteFiles.
        :type request: :class:`tencentcloud.pts.v20210728.models.DeleteFilesRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DeleteFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteJobs(self, request):
        """This API is used to delete jobs.

        :param request: Request instance for DeleteJobs.
        :type request: :class:`tencentcloud.pts.v20210728.models.DeleteJobsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DeleteJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProjects(self, request):
        """This API is used to delete projects.

        :param request: Request instance for DeleteProjects.
        :type request: :class:`tencentcloud.pts.v20210728.models.DeleteProjectsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DeleteProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScenarios(self, request):
        """This API is used to delete scenarios.

        :param request: Request instance for DeleteScenarios.
        :type request: :class:`tencentcloud.pts.v20210728.models.DeleteScenariosRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DeleteScenariosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScenarios", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScenariosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlertChannels(self, request):
        """This API is used to query alert recipient groups.

        :param request: Request instance for DescribeAlertChannels.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeAlertChannelsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeAlertChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlertChannels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlertChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlertRecords(self, request):
        """This API is used to query alert records.

        :param request: Request instance for DescribeAlertRecords.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeAlertRecordsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeAlertRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlertRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlertRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableMetrics(self, request):
        """This API is used to query all supported metrics.

        :param request: Request instance for DescribeAvailableMetrics.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeAvailableMetricsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeAvailableMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCheckSummary(self, request):
        """This API is used to query checkpoint summary information.

        :param request: Request instance for DescribeCheckSummary.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeCheckSummaryRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeCheckSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCheckSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCheckSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCronJobs(self, request):
        """This API is used to list cron jobs, selecting all by default if a non-mandatory array parameter is empty.

        :param request: Request instance for DescribeCronJobs.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeCronJobsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeCronJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCronJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCronJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironments(self, request):
        """This API is used to query the environment list.

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeErrorSummary(self, request):
        """This API is used to query error summary information.

        :param request: Request instance for DescribeErrorSummary.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeErrorSummaryRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeErrorSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeErrorSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeErrorSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFiles(self, request):
        """This API is used to query file list.

        :param request: Request instance for DescribeFiles.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeFilesRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobs(self, request):
        """This API is used to query job list.

        :param request: Request instance for DescribeJobs.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeJobsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLabelValues(self, request):
        """This API is used to query label values.

        :param request: Request instance for DescribeLabelValues.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeLabelValuesRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeLabelValuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLabelValues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLabelValuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMetricLabelWithValues(self, request):
        """This API is used to query all labels and values of metrics

        :param request: Request instance for DescribeMetricLabelWithValues.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeMetricLabelWithValuesRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeMetricLabelWithValuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMetricLabelWithValues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMetricLabelWithValuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNormalLogs(self, request):
        """This API is used to query logs in performance testing, including engine logs and console logs.

        :param request: Request instance for DescribeNormalLogs.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeNormalLogsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeNormalLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNormalLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNormalLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjects(self, request):
        """The API is used to query project list.

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """This API is used to query region list.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRequestSummary(self, request):
        """This API is used to query request summary information.

        :param request: Request instance for DescribeRequestSummary.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeRequestSummaryRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeRequestSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRequestSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRequestSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSampleBatchQuery(self, request):
        """This API is used to query metrics in batch and return metric content at a specific time point.

        :param request: Request instance for DescribeSampleBatchQuery.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeSampleBatchQueryRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeSampleBatchQueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSampleBatchQuery", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSampleBatchQueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSampleLogs(self, request):
        """This API is used to query sampled request logs.

        :param request: Request instance for DescribeSampleLogs.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeSampleLogsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeSampleLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSampleLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSampleLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSampleMatrixBatchQuery(self, request):
        """This API is used to batch query metric matrices.

        :param request: Request instance for DescribeSampleMatrixBatchQuery.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeSampleMatrixBatchQueryRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeSampleMatrixBatchQueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSampleMatrixBatchQuery", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSampleMatrixBatchQueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSampleMatrixQuery(self, request):
        """This API is used to query metric matrix.

        :param request: Request instance for DescribeSampleMatrixQuery.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeSampleMatrixQueryRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeSampleMatrixQueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSampleMatrixQuery", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSampleMatrixQueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSampleQuery(self, request):
        """This API is used to query metrics and return metric content at a specific time point.

        :param request: Request instance for DescribeSampleQuery.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeSampleQueryRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeSampleQueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSampleQuery", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSampleQueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScenarioWithJobs(self, request):
        """This API is used to query scenarios with executed jobs.

        :param request: Request instance for DescribeScenarioWithJobs.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeScenarioWithJobsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeScenarioWithJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScenarioWithJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScenarioWithJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScenarios(self, request):
        """This API is used to query scenario list.

        :param request: Request instance for DescribeScenarios.
        :type request: :class:`tencentcloud.pts.v20210728.models.DescribeScenariosRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.DescribeScenariosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScenarios", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScenariosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateTmpKey(self, request):
        """This API is used to generate temporary COS credentials.

        :param request: Request instance for GenerateTmpKey.
        :type request: :class:`tencentcloud.pts.v20210728.models.GenerateTmpKeyRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.GenerateTmpKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateTmpKey", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateTmpKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartCronJobs(self, request):
        """This API is used to restart cron jobs that have been aborted.

        :param request: Request instance for RestartCronJobs.
        :type request: :class:`tencentcloud.pts.v20210728.models.RestartCronJobsRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.RestartCronJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartCronJobs", params, headers=headers)
            response = json.loads(body)
            model = models.RestartCronJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartJob(self, request):
        """This API is used to create and start test job.

        :param request: Request instance for StartJob.
        :type request: :class:`tencentcloud.pts.v20210728.models.StartJobRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.StartJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartJob", params, headers=headers)
            response = json.loads(body)
            model = models.StartJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCronJob(self, request):
        """This API is used to update a cron job.

        :param request: Request instance for UpdateCronJob.
        :type request: :class:`tencentcloud.pts.v20210728.models.UpdateCronJobRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.UpdateCronJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCronJob", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCronJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEnvironment(self, request):
        """This API is used to update environments.

        :param request: Request instance for UpdateEnvironment.
        :type request: :class:`tencentcloud.pts.v20210728.models.UpdateEnvironmentRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.UpdateEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFileScenarioRelation(self, request):
        """This API is used to update relation between files and scenarios.

        :param request: Request instance for UpdateFileScenarioRelation.
        :type request: :class:`tencentcloud.pts.v20210728.models.UpdateFileScenarioRelationRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.UpdateFileScenarioRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFileScenarioRelation", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFileScenarioRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateJob(self, request):
        """This API is used to update a job.

        :param request: Request instance for UpdateJob.
        :type request: :class:`tencentcloud.pts.v20210728.models.UpdateJobRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.UpdateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateJob", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateProject(self, request):
        """This API is used to update a project.

        :param request: Request instance for UpdateProject.
        :type request: :class:`tencentcloud.pts.v20210728.models.UpdateProjectRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.UpdateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProject", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateScenario(self, request):
        """This API is used to update a scenario.

        :param request: Request instance for UpdateScenario.
        :type request: :class:`tencentcloud.pts.v20210728.models.UpdateScenarioRequest`
        :rtype: :class:`tencentcloud.pts.v20210728.models.UpdateScenarioResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateScenario", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateScenarioResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))