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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.pts.v20210728 import models
from typing import Dict


class PtsClient(AbstractClient):
    _apiVersion = '2021-07-28'
    _endpoint = 'pts.intl.tencentcloudapi.com'
    _service = 'pts'

    async def AbortCronJobs(
            self,
            request: models.AbortCronJobsRequest,
            opts: Dict = None,
    ) -> models.AbortCronJobsResponse:
        """
        This API is used to stop cron jobs.
        """
        
        kwargs = {}
        kwargs["action"] = "AbortCronJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AbortCronJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AbortJob(
            self,
            request: models.AbortJobRequest,
            opts: Dict = None,
    ) -> models.AbortJobResponse:
        """
        This API is used to stop test job.
        """
        
        kwargs = {}
        kwargs["action"] = "AbortJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AbortJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AdjustJobSpeed(
            self,
            request: models.AdjustJobSpeedRequest,
            opts: Dict = None,
    ) -> models.AdjustJobSpeedResponse:
        """
        This API is used to adjust the target RPS of a job.
        """
        
        kwargs = {}
        kwargs["action"] = "AdjustJobSpeed"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AdjustJobSpeedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyScenario(
            self,
            request: models.CopyScenarioRequest,
            opts: Dict = None,
    ) -> models.CopyScenarioResponse:
        """
        This API is used to copy a scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "CopyScenario"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyScenarioResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlertChannel(
            self,
            request: models.CreateAlertChannelRequest,
            opts: Dict = None,
    ) -> models.CreateAlertChannelResponse:
        """
        This API is used to create an alert recipient group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlertChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlertChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCronJob(
            self,
            request: models.CreateCronJobRequest,
            opts: Dict = None,
    ) -> models.CreateCronJobResponse:
        """
        This API is used to create a cron job.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCronJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCronJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnvironment(
            self,
            request: models.CreateEnvironmentRequest,
            opts: Dict = None,
    ) -> models.CreateEnvironmentResponse:
        """
        This API is used to create an environment.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFile(
            self,
            request: models.CreateFileRequest,
            opts: Dict = None,
    ) -> models.CreateFileResponse:
        """
        This API is used to create a file.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        This API is used to create a project.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScenario(
            self,
            request: models.CreateScenarioRequest,
            opts: Dict = None,
    ) -> models.CreateScenarioResponse:
        """
        This API is used to create a scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScenario"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScenarioResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlertChannel(
            self,
            request: models.DeleteAlertChannelRequest,
            opts: Dict = None,
    ) -> models.DeleteAlertChannelResponse:
        """
        This API is used to delete an alert recipient group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlertChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlertChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCronJobs(
            self,
            request: models.DeleteCronJobsRequest,
            opts: Dict = None,
    ) -> models.DeleteCronJobsResponse:
        """
        This API is used to delete cron jobs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCronJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCronJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnvironments(
            self,
            request: models.DeleteEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DeleteEnvironmentsResponse:
        """
        This API is used to delete environments.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFiles(
            self,
            request: models.DeleteFilesRequest,
            opts: Dict = None,
    ) -> models.DeleteFilesResponse:
        """
        This API is used to delete files.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJobs(
            self,
            request: models.DeleteJobsRequest,
            opts: Dict = None,
    ) -> models.DeleteJobsResponse:
        """
        This API is used to delete jobs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjects(
            self,
            request: models.DeleteProjectsRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectsResponse:
        """
        This API is used to delete projects.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScenarios(
            self,
            request: models.DeleteScenariosRequest,
            opts: Dict = None,
    ) -> models.DeleteScenariosResponse:
        """
        This API is used to delete scenarios.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScenarios"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScenariosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlertChannels(
            self,
            request: models.DescribeAlertChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlertChannelsResponse:
        """
        This API is used to query alert recipient groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlertChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlertChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlertRecords(
            self,
            request: models.DescribeAlertRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlertRecordsResponse:
        """
        This API is used to query alert records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlertRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlertRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableMetrics(
            self,
            request: models.DescribeAvailableMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableMetricsResponse:
        """
        This API is used to query all supported metrics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckSummary(
            self,
            request: models.DescribeCheckSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckSummaryResponse:
        """
        This API is used to query checkpoint summary information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCronJobs(
            self,
            request: models.DescribeCronJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeCronJobsResponse:
        """
        This API is used to list cron jobs, selecting all by default if a non-mandatory array parameter is empty.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCronJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCronJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        This API is used to query the environment list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeErrorSummary(
            self,
            request: models.DescribeErrorSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeErrorSummaryResponse:
        """
        This API is used to query error summary information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeErrorSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeErrorSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFiles(
            self,
            request: models.DescribeFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeFilesResponse:
        """
        This API is used to query file list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobs(
            self,
            request: models.DescribeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobsResponse:
        """
        This API is used to query job list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLabelValues(
            self,
            request: models.DescribeLabelValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeLabelValuesResponse:
        """
        This API is used to query label values.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLabelValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLabelValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricLabelWithValues(
            self,
            request: models.DescribeMetricLabelWithValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricLabelWithValuesResponse:
        """
        This API is used to query all labels and values of metrics
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricLabelWithValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricLabelWithValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNormalLogs(
            self,
            request: models.DescribeNormalLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeNormalLogsResponse:
        """
        This API is used to query logs in performance testing, including engine logs and console logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNormalLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNormalLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        The API is used to query project list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        This API is used to query region list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRequestSummary(
            self,
            request: models.DescribeRequestSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeRequestSummaryResponse:
        """
        This API is used to query request summary information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRequestSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRequestSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleBatchQuery(
            self,
            request: models.DescribeSampleBatchQueryRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleBatchQueryResponse:
        """
        This API is used to query metrics in batch and return metric content at a specific time point.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleBatchQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleBatchQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleLogs(
            self,
            request: models.DescribeSampleLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleLogsResponse:
        """
        This API is used to query sampled request logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleMatrixBatchQuery(
            self,
            request: models.DescribeSampleMatrixBatchQueryRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleMatrixBatchQueryResponse:
        """
        This API is used to batch query metric matrices.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleMatrixBatchQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleMatrixBatchQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleMatrixQuery(
            self,
            request: models.DescribeSampleMatrixQueryRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleMatrixQueryResponse:
        """
        This API is used to query metric matrix.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleMatrixQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleMatrixQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleQuery(
            self,
            request: models.DescribeSampleQueryRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleQueryResponse:
        """
        This API is used to query metrics and return metric content at a specific time point.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScenarioWithJobs(
            self,
            request: models.DescribeScenarioWithJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeScenarioWithJobsResponse:
        """
        This API is used to query scenarios with executed jobs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScenarioWithJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScenarioWithJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScenarios(
            self,
            request: models.DescribeScenariosRequest,
            opts: Dict = None,
    ) -> models.DescribeScenariosResponse:
        """
        This API is used to query scenario list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScenarios"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScenariosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateTmpKey(
            self,
            request: models.GenerateTmpKeyRequest,
            opts: Dict = None,
    ) -> models.GenerateTmpKeyResponse:
        """
        This API is used to generate temporary COS credentials.
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateTmpKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateTmpKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartCronJobs(
            self,
            request: models.RestartCronJobsRequest,
            opts: Dict = None,
    ) -> models.RestartCronJobsResponse:
        """
        This API is used to restart cron jobs that have been aborted.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartCronJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartCronJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartJob(
            self,
            request: models.StartJobRequest,
            opts: Dict = None,
    ) -> models.StartJobResponse:
        """
        This API is used to create and start test job.
        """
        
        kwargs = {}
        kwargs["action"] = "StartJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCronJob(
            self,
            request: models.UpdateCronJobRequest,
            opts: Dict = None,
    ) -> models.UpdateCronJobResponse:
        """
        This API is used to update a cron job.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCronJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCronJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEnvironment(
            self,
            request: models.UpdateEnvironmentRequest,
            opts: Dict = None,
    ) -> models.UpdateEnvironmentResponse:
        """
        This API is used to update environments.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFileScenarioRelation(
            self,
            request: models.UpdateFileScenarioRelationRequest,
            opts: Dict = None,
    ) -> models.UpdateFileScenarioRelationResponse:
        """
        This API is used to update relation between files and scenarios.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFileScenarioRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFileScenarioRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateJob(
            self,
            request: models.UpdateJobRequest,
            opts: Dict = None,
    ) -> models.UpdateJobResponse:
        """
        This API is used to update a job.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProject(
            self,
            request: models.UpdateProjectRequest,
            opts: Dict = None,
    ) -> models.UpdateProjectResponse:
        """
        This API is used to update a project.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateScenario(
            self,
            request: models.UpdateScenarioRequest,
            opts: Dict = None,
    ) -> models.UpdateScenarioResponse:
        """
        This API is used to update a scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateScenario"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateScenarioResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)