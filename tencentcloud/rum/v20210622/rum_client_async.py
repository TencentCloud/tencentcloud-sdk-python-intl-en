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
from tencentcloud.rum.v20210622 import models
from typing import Dict


class RumClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'rum.intl.tencentcloudapi.com'
    _service = 'rum'

    async def CreateLogExport(
            self,
            request: models.CreateLogExportRequest,
            opts: Dict = None,
    ) -> models.CreateLogExportResponse:
        """
        API domain name: `rum.tencentcloudapi.com`.

        This API is used to create a log download task.

        Default API request rate limit: 20 requests/sec.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOfflineLogConfig(
            self,
            request: models.CreateOfflineLogConfigRequest,
            opts: Dict = None,
    ) -> models.CreateOfflineLogConfigResponse:
        """
        This API is used to create an offline log listener to report offline logs of particular users.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOfflineLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOfflineLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        This API is used to create a RUM application which belongs to a specific team.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReleaseFile(
            self,
            request: models.CreateReleaseFileRequest,
            opts: Dict = None,
    ) -> models.CreateReleaseFileResponse:
        """
        This API is used to create a file record for the specified project.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReleaseFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReleaseFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStarProject(
            self,
            request: models.CreateStarProjectRequest,
            opts: Dict = None,
    ) -> models.CreateStarProjectResponse:
        """
        This API is used to add a starred project.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStarProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStarProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTawInstance(
            self,
            request: models.CreateTawInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateTawInstanceResponse:
        """
        This API is used to create a RUM business system.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTawInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTawInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWhitelist(
            self,
            request: models.CreateWhitelistRequest,
            opts: Dict = None,
    ) -> models.CreateWhitelistResponse:
        """
        This API is used to create an allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        This API is used to delete an instance. The deleted instance cannot be recovered.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogExport(
            self,
            request: models.DeleteLogExportRequest,
            opts: Dict = None,
    ) -> models.DeleteLogExportResponse:
        """
        API domain name: `rum.tencentcloudapi.com`.

        This API is used to delete a log download task.

        Default API request rate limit: 20 requests/sec.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOfflineLogConfig(
            self,
            request: models.DeleteOfflineLogConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteOfflineLogConfigResponse:
        """
        This API is used to delete an offline RUM log listener. Then, offline logs of particular users will not be reported.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOfflineLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOfflineLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOfflineLogRecord(
            self,
            request: models.DeleteOfflineLogRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteOfflineLogRecordResponse:
        """
        This API is used to delete an offline log record.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOfflineLogRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOfflineLogRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        This API is used to delete the specified RUM project.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReleaseFile(
            self,
            request: models.DeleteReleaseFileRequest,
            opts: Dict = None,
    ) -> models.DeleteReleaseFileResponse:
        """
        This API is used to delete the specified sourcemap file.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReleaseFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReleaseFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStarProject(
            self,
            request: models.DeleteStarProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteStarProjectResponse:
        """
        This API is used to delete a starred project for the specified user.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStarProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStarProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWhitelist(
            self,
            request: models.DeleteWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteWhitelistResponse:
        """
        This API is used to delete an allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeData(
            self,
            request: models.DescribeDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDataResponse:
        """
        This API is used to query the forwarding monitor.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataCustomUrl(
            self,
            request: models.DescribeDataCustomUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataCustomUrlResponse:
        """
        This API is used to get the DescribeDataCustomUrl information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataCustomUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataCustomUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEventUrl(
            self,
            request: models.DescribeDataEventUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEventUrlResponse:
        """
        This API is used to get the DescribeDataEventUrl information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEventUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEventUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFetchProject(
            self,
            request: models.DescribeDataFetchProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeDataFetchProjectResponse:
        """
        This API is used to get the `DescribeDataFetchProject` information and has been deprecated. Use `DescribeDataFetchUrl` instead.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFetchProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFetchProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFetchUrl(
            self,
            request: models.DescribeDataFetchUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataFetchUrlResponse:
        """
        This API is used to get the DescribeDataFetchUrl information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFetchUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFetchUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFetchUrlInfo(
            self,
            request: models.DescribeDataFetchUrlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataFetchUrlInfoResponse:
        """
        This API is used to get the DescribeDataFetchUrlInfo information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFetchUrlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFetchUrlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataLogUrlInfo(
            self,
            request: models.DescribeDataLogUrlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataLogUrlInfoResponse:
        """
        This API is used to get the loginfo information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataLogUrlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataLogUrlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataLogUrlStatistics(
            self,
            request: models.DescribeDataLogUrlStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataLogUrlStatisticsResponse:
        """
        This API is used to get the LogUrlStatistics information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataLogUrlStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataLogUrlStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPerformancePage(
            self,
            request: models.DescribeDataPerformancePageRequest,
            opts: Dict = None,
    ) -> models.DescribeDataPerformancePageResponse:
        """
        This API is used to get the PerformancePage information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPerformancePage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPerformancePageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPerformanceProject(
            self,
            request: models.DescribeDataPerformanceProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeDataPerformanceProjectResponse:
        """
        This API is used to get the PerformanceProject information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPerformanceProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPerformanceProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPvUrlInfo(
            self,
            request: models.DescribeDataPvUrlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataPvUrlInfoResponse:
        """
        This API is used to get the PvUrlInfo information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPvUrlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPvUrlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPvUrlStatistics(
            self,
            request: models.DescribeDataPvUrlStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataPvUrlStatisticsResponse:
        """
        This API is used to get the DescribeDataPvUrlStatistics information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPvUrlStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPvUrlStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataReportCount(
            self,
            request: models.DescribeDataReportCountRequest,
            opts: Dict = None,
    ) -> models.DescribeDataReportCountResponse:
        """
        This API is used to get the number of reported data entries for a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataReportCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataReportCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSetUrlStatistics(
            self,
            request: models.DescribeDataSetUrlStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSetUrlStatisticsResponse:
        """
        This API is used to get the DescribeDataSetUrlStatistics information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSetUrlStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSetUrlStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticProject(
            self,
            request: models.DescribeDataStaticProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeDataStaticProjectResponse:
        """
        This API is used to get the DescribeDataStaticProject information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticResource(
            self,
            request: models.DescribeDataStaticResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDataStaticResourceResponse:
        """
        This API is used to get the DescribeDataStaticResource information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticUrl(
            self,
            request: models.DescribeDataStaticUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataStaticUrlResponse:
        """
        This API is used to get the DescribeDataStaticUrl information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataWebVitalsPage(
            self,
            request: models.DescribeDataWebVitalsPageRequest,
            opts: Dict = None,
    ) -> models.DescribeDataWebVitalsPageResponse:
        """
        This API is used to get the DescribeDataWebVitalsPage information, which is about core user activities.
        It includes the Web Vitals metric for the page loading performance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataWebVitalsPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataWebVitalsPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeError(
            self,
            request: models.DescribeErrorRequest,
            opts: Dict = None,
    ) -> models.DescribeErrorResponse:
        """
        This API is used to get the homepage error information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeError"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeErrorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogExports(
            self,
            request: models.DescribeLogExportsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogExportsResponse:
        """
        API domain name: `rum.tencentcloudapi.com`.

        This API is used to get the list of log download tasks.

        Default API request rate limit: 20 requests/sec.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogExports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogExportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogList(
            self,
            request: models.DescribeLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeLogListResponse:
        """
        This API is used to get the log list. It has been deprecated. Use `DescribeRumLogList` instead.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOfflineLogConfigs(
            self,
            request: models.DescribeOfflineLogConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeOfflineLogConfigsResponse:
        """
        This API is used to get the configuration of the set offline log listener and return the unique user ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOfflineLogConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOfflineLogConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOfflineLogRecords(
            self,
            request: models.DescribeOfflineLogRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeOfflineLogRecordsResponse:
        """
        This API is used to get all (up to 100) offline log records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOfflineLogRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOfflineLogRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOfflineLogs(
            self,
            request: models.DescribeOfflineLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeOfflineLogsResponse:
        """
        This API is used to get the specified offline log.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOfflineLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOfflineLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectLimits(
            self,
            request: models.DescribeProjectLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectLimitsResponse:
        """
        This API is used to get the sampling information of an application’s reporting APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        This API is used to get the list of projects (under teams created by an instance).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePvList(
            self,
            request: models.DescribePvListRequest,
            opts: Dict = None,
    ) -> models.DescribePvListResponse:
        """
        This API is used to get the list of PVs under a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseFileSign(
            self,
            request: models.DescribeReleaseFileSignRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseFileSignResponse:
        """
        This API is used to get the temporary key for uploaded file storage.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseFileSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseFileSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseFiles(
            self,
            request: models.DescribeReleaseFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseFilesResponse:
        """
        This API is used to get the list of source maps of an application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumGroupLog(
            self,
            request: models.DescribeRumGroupLogRequest,
            opts: Dict = None,
    ) -> models.DescribeRumGroupLogResponse:
        """
        This API is used to get the log aggregation information under a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumGroupLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumGroupLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogExport(
            self,
            request: models.DescribeRumLogExportRequest,
            opts: Dict = None,
    ) -> models.DescribeRumLogExportResponse:
        """
        This API is used to get the list of logs in a project (created by an instance).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogExports(
            self,
            request: models.DescribeRumLogExportsRequest,
            opts: Dict = None,
    ) -> models.DescribeRumLogExportsResponse:
        """
        This API is used to get the list of exported logs in a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogExports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogExportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogList(
            self,
            request: models.DescribeRumLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeRumLogListResponse:
        """
        This API is used to get the list of logs in a project (created by an instance).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumStatsLogList(
            self,
            request: models.DescribeRumStatsLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeRumStatsLogListResponse:
        """
        This API is used to get the list of logs in a project every minute.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumStatsLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumStatsLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScores(
            self,
            request: models.DescribeScoresRequest,
            opts: Dict = None,
    ) -> models.DescribeScoresResponse:
        """
        This API is used to get the list of homepage scores.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScores"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScoresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTawAreas(
            self,
            request: models.DescribeTawAreasRequest,
            opts: Dict = None,
    ) -> models.DescribeTawAreasResponse:
        """
        This API is used to query region information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTawAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTawAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUvList(
            self,
            request: models.DescribeUvListRequest,
            opts: Dict = None,
    ) -> models.DescribeUvListResponse:
        """
        This API is used to get the list of UVs under a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhitelists(
            self,
            request: models.DescribeWhitelistsRequest,
            opts: Dict = None,
    ) -> models.DescribeWhitelistsResponse:
        """
        This API is used to get the list of allowlists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhitelists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhitelistsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        This API is used to modify a RUM business system.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        This API is used to modify the RUM application information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProjectLimit(
            self,
            request: models.ModifyProjectLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectLimitResponse:
        """
        This API is used to add or modify data reporting limit.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProjectLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeInstance(
            self,
            request: models.ResumeInstanceRequest,
            opts: Dict = None,
    ) -> models.ResumeInstanceResponse:
        """
        This API is used to recover a RUM business system so that you can use the application to report data normally.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeProject(
            self,
            request: models.ResumeProjectRequest,
            opts: Dict = None,
    ) -> models.ResumeProjectResponse:
        """
        This API is used to recover an application and resume data reporting.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstance(
            self,
            request: models.StopInstanceRequest,
            opts: Dict = None,
    ) -> models.StopInstanceResponse:
        """
        This API is used to stop an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopProject(
            self,
            request: models.StopProjectRequest,
            opts: Dict = None,
    ) -> models.StopProjectResponse:
        """
        This API is used to stop a project from reporting data.
        """
        
        kwargs = {}
        kwargs["action"] = "StopProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)